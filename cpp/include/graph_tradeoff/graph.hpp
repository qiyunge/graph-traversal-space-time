#ifndef GRAPH_TRADEOFF_GRAPH_HPP
#define GRAPH_TRADEOFF_GRAPH_HPP

#include <vector>
#include <string>
#include <memory>

#include "graph_tradeoff/neighbor_view.hpp"

namespace graph_tradeoff {  
    enum class GraphRepresentation {
        AdjacencyList,
        AdjacencyMatrix,
        
    };

    class Graph {
    public:
        virtual ~Graph() = default;
        virtual std::size_t num_vertices() const = 0;
        virtual void add_edge(int u, int v) = 0;
        virtual bool has_edge(int u, int v) const = 0;
        virtual NeighborView neighbors(int u) const = 0;
        virtual std::string name() const = 0;

    };

    class AdjacencyListGraph final: public Graph {
    public:
        explicit AdjacencyListGraph(std::size_t num_vertices);
        std::size_t num_vertices() const override;
        void add_edge(int u, int v) override;
        bool has_edge(int u, int v) const override;
        NeighborView neighbors(int u) const override;
        std::string name() const override;

        ~AdjacencyListGraph() override = default;

    private:
        std::vector<std::vector<int>> adjacency_list_;

    };  

    class AdjacencyMatrixGraph final : public Graph {
    public:
        explicit AdjacencyMatrixGraph(std::size_t n);

        std::size_t num_vertices() const override;
        void add_edge(int u, int v) override;
        bool has_edge(int u, int v) const override;
        NeighborView neighbors(int u) const override;
        std::string name() const override;
        ~AdjacencyMatrixGraph() override = default;

    private:
        std::vector<std::vector<bool>> matrix_;
    };

    std::unique_ptr<Graph> make_graph(GraphRepresentation repr, std::size_t n);
    GraphRepresentation parse_representation(const std::string& text);
    std::string to_string(GraphRepresentation repr);


}

#endif // GRAPH_TRADEOFF_GRAPH_HPP