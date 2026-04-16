#include "graph_tradeoff/graph.hpp"
#include "graph_tradeoff/utils.hpp"

// #include <ranges>
#include <algorithm>
#include <string>
#include <stdexcept>

namespace graph_tradeoff
{

    /* --- AdjacencyListGraph implementation --- */
    AdjacencyListGraph::AdjacencyListGraph(std::size_t num_vertices) : adjacency_list_(num_vertices)
    {
    }

    std::size_t AdjacencyListGraph::num_vertices() const
    {
        return adjacency_list_.size();
    }

    void AdjacencyListGraph::add_edge(int u, int v)
    {
        utils::validate_vertex(*this, u);
        utils::validate_vertex(*this, v);
        adjacency_list_[u].push_back(v);
        adjacency_list_[v].push_back(u); // Assuming undirected graph
    }

    bool AdjacencyListGraph::has_edge(int u, int v) const
    {
        utils::validate_vertex(*this, u);
        utils::validate_vertex(*this, v);
        const auto &neighbors = adjacency_list_[u];
        return std::ranges::find(neighbors, v) != neighbors.end();
    }

    std::vector<int> AdjacencyListGraph::neighbors(int u) const
    {
        utils::validate_vertex(*this, u);
        std::vector<int> result;
        const auto &row = adjacency_list_[static_cast<std::size_t>(u)];
        result.reserve(row.size());
        for (int v = 0; v < static_cast<int>(row.size()); ++v)
        {
            if (row[v])
            {
                result.push_back(v);
            }
        }
        return result;
    }

    std::string AdjacencyListGraph::name() const
    {
        return "Adjacency List Graph";
    }

    /* --- AdjacencyMatrixGraph implementation --- */
    AdjacencyMatrixGraph::AdjacencyMatrixGraph(std::size_t n) : matrix_(n, std::vector<bool>(n, false))
    {
    }

    std::size_t AdjacencyMatrixGraph::num_vertices() const
    {
        return matrix_.size();
    }

    void AdjacencyMatrixGraph::add_edge(int u, int v)
    {
        utils::validate_vertex(*this, u);
        utils::validate_vertex(*this, v);
        matrix_[u][v] = true;
        matrix_[v][u] = true; // Assuming undirected graph
    }

    bool AdjacencyMatrixGraph::has_edge(int u, int v) const
    {
        utils::validate_vertex(*this, u);
        utils::validate_vertex(*this, v);
        return matrix_[u][v];
    }

    std::vector<int> AdjacencyMatrixGraph::neighbors(int u) const
    {
        utils::validate_vertex(*this, u);
        std::vector<int> result;
        const auto &row = matrix_[static_cast<std::size_t>(u)];
        result.reserve(row.size());
        for (std::size_t i = 0; i < row.size(); ++i)
        {
            if (row[i])
            {
                result.push_back(static_cast<int>(i));
            }
        }
        return result;
    }

    std::string AdjacencyMatrixGraph::name() const
    {
        return "Adjacency Matrix Graph";
    }

    /* --- Factory functions --- */
    std::unique_ptr<Graph> make_graph(GraphRepresentation repr, std::size_t n)
    {
        switch (repr)
        {
        case GraphRepresentation::AdjacencyList:
            return std::make_unique<AdjacencyListGraph>(n);
        case GraphRepresentation::AdjacencyMatrix:
            return std::make_unique<AdjacencyMatrixGraph>(n);
        default:
            throw std::invalid_argument("Unknown graph representation");
        }
    }

    GraphRepresentation parse_representation(const std::string &text)
    {
        const auto normalized = utils::normalized_ascii_lower(text);
        if (normalized == "list" || normalized == "adj_list" || normalized == "adjacency_list")
        {
            return GraphRepresentation::AdjacencyList;
        }
        if (normalized == "matrix" || normalized == "adj_matrix" || normalized == "adjacency_matrix")
        {
            return GraphRepresentation::AdjacencyMatrix;
        }
        throw std::invalid_argument("invalid graph representation: " + text);
    }

    std::string to_string(GraphRepresentation repr)
    {
        switch (repr)
        {
        case GraphRepresentation::AdjacencyList:
            return "Adjacency List";
        case GraphRepresentation::AdjacencyMatrix:
            return "Adjacency Matrix";
        default:
            throw std::invalid_argument("Unknown graph representation");
        }
    }
} // namespace graph_tradeoff