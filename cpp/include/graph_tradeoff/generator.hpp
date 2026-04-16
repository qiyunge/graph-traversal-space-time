#pragma once

#include "graph_tradeoff/graph.hpp"

namespace graph_tradeoff
{

    enum class GraphStructure
    {
        Random,
        Tree,
        Dense
    };

    GraphStructure parse_structure(const std::string &text);
    std::string to_string(GraphStructure structure);

    struct GraphBuildConfig
    {
        std::size_t n{1000};
        double edge_prob{0.01};
        unsigned int seed{42};
        GraphRepresentation representation{GraphRepresentation::AdjacencyList};
        GraphStructure structure{GraphStructure::Random};
       
    };

    
    struct GraphManifest
    {
        std::string graph_id;
        std::string graph_type;
        int num_vertices;
        int num_edges;
        bool directed;
        int seed;
        std::string generator_version;
        std::string edge_file;
        double edge_prob;
    };

 

    std::unique_ptr<Graph> generate_graph(const GraphBuildConfig &config);
    std::unique_ptr<Graph> load_graph_from_manifest(
        const std::string &meta_file,
        const std::string &representation);

} // namespace graph_tradeoff
