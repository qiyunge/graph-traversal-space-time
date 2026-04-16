#include "graph_tradeoff/generator.hpp"
#include "graph_tradeoff/utils.hpp"
#include "graph_tradeoff/graph.hpp"
#include "nlohmann/json.hpp "
#include <stdexcept>
#include <random>
#include <fstream>
#include <filesystem>

namespace fs = std::filesystem;

namespace graph_tradeoff
{
    namespace
    {

        using json = nlohmann::json;

        GraphManifest load_manifest(const std::string &path)
        {
            std::ifstream in(path);
            if (!in)
            {
                throw std::runtime_error("Failed to open JSON file: " + path);
            }

            json j;
            in >> j;

            GraphManifest m{
                .graph_id = j.at("graph_id").get<std::string>(),
                .graph_type = j.at("graph_type").get<std::string>(),
                .num_vertices = j.at("num_vertices").get<int>(),
                .num_edges = j.at("num_edges").get<int>(),
                .directed = j.at("directed").get<bool>(),
                .seed = j.at("seed").get<int>(),
                .generator_version = j.at("generator_version").get<std::string>(),
                .edge_file = j.at("edge_file").get<std::string>(),
                .edge_prob = j.at("params").at("edge_prob").get<double>()};

            return m;
        }
    }
    GraphStructure parse_structure(const std::string &text)
    {
        const auto normalized = utils::normalized_ascii_lower(text);
        if (normalized == "random")
        {
            return GraphStructure::Random;
        }
        if (normalized == "tree")
        {
            return GraphStructure::Tree;
        }
        if (normalized == "dense")
        {
            return GraphStructure::Dense;
        }
        throw std::invalid_argument("invalid graph structure: " + text);
    }

    std::string to_string(GraphStructure structure)
    {
        switch (structure)
        {
        case GraphStructure::Random:
            return "random";
        case GraphStructure::Tree:
            return "tree";
        case GraphStructure::Dense:
            return "dense";
        default:
            return "unknown";
        }
    }

    std::unique_ptr<Graph> generate_graph(const GraphBuildConfig &config)
    {
        auto graph = make_graph(config.representation, config.n);
        std::mt19937 rng(config.seed);
        std::bernoulli_distribution edge_dist(config.edge_prob);

        if (config.n == 0)
        {
            return graph;
        }

        if (config.structure == GraphStructure::Tree)
        {
            for (std::size_t v = 1; v < config.n; ++v)
            {
                std::uniform_int_distribution<int> parent_dist(0, static_cast<int>(v - 1));
                const int parent = parent_dist(rng);
                graph->add_edge(parent, static_cast<int>(v));
            }
            return graph;
        }

        if (config.structure == GraphStructure::Dense)
        {
            for (std::size_t u = 0; u < config.n; ++u)
            {
                for (std::size_t v = u + 1; v < config.n; ++v)
                {
                    if (config.edge_prob >= 0.5 || edge_dist(rng))
                    {
                        graph->add_edge(static_cast<int>(u), static_cast<int>(v));
                    }
                }
            }
            return graph;
        }

        for (std::size_t u = 0; u < config.n; ++u)
        {
            for (std::size_t v = u + 1; v < config.n; ++v)
            {
                if (edge_dist(rng))
                {
                    graph->add_edge(static_cast<int>(u), static_cast<int>(v));
                }
            }
        }
        return graph;
    }

    std::unique_ptr<Graph> load_graph_from_manifest(
        const std::string &meta_file,
        const std::string &representation)
    {
        const auto manifest = load_manifest(meta_file);

        if (manifest.edge_file.empty())
        {
            throw std::runtime_error("edge_file is required in manifest to load graph");
        }

        fs::path meta_path(meta_file);
        fs::path edge_path = meta_path.parent_path() / manifest.edge_file;
        std::ifstream edge_file(edge_path);
        if (!edge_file.is_open())
        {
            throw std::runtime_error("Failed to open edge file: " + manifest.edge_file);
        }

        auto graph = make_graph(parse_representation(representation), manifest.num_vertices);

        std::string line;
        std::getline(edge_file, line); // Skip header;
        for (std::size_t i = 0; i < manifest.num_edges; ++i)
        {
            if (!std::getline(edge_file, line))
            {
                throw std::runtime_error("Unexpected end of edge file: " + manifest.edge_file);
            }

            if (line.empty())
            {
                throw std::runtime_error("Empty edge line in file: " + manifest.edge_file);
            }

            std::istringstream iss(line);
            std::string u_str, v_str;

            if (!std::getline(iss, u_str, ',') || !std::getline(iss, v_str))
            {
                throw std::runtime_error("Invalid CSV edge line: " + line);
            }

            int u = std::stoi(u_str);
            int v = std::stoi(v_str);

            graph->add_edge(u, v);
        }

        return graph;
    }
}