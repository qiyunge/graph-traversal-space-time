#ifndef GRAPH_TRADEOFF_TRAVERSAL_HPP
#define GRAPH_TRADEOFF_TRAVERSAL_HPP

#include <string>
#include "graph_tradeoff/graph.hpp"

namespace graph_tradeoff
{
    enum class TraversalType
    {
        DFS,
        BFS
    };

    TraversalType parse_traversal(const std::string &text);

    std::string to_string(TraversalType traversal_type);

    struct TraversalMetrics
    {
        std::size_t visited_nodes{0};
        std::size_t peak_frontier{0};
    };

    TraversalMetrics run_traversal(const Graph &graph, TraversalType traversal_type,int start_vertex =0); 
    TraversalMetrics run_BFS(const Graph &graph, int start_vertex = 0);
    TraversalMetrics run_DFS(const Graph &graph, int start_vertex = 0);
}

#endif // GRAPH_TRADEOFF_TRAVERSAL_HPP