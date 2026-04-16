#include "graph_tradeoff/traversal.hpp"
#include "graph_tradeoff/utils.hpp"
#include <stdexcept>
#include <queue>

namespace graph_tradeoff
{

    TraversalType parse_traversal(const std::string &text)
    {
        const auto normalized = utils::normalized_ascii_lower(text);
        if (normalized == "bfs")
        {
            return TraversalType::BFS;
        }
        if (normalized == "dfs")
        {
            return TraversalType::DFS;
        }
        throw std::invalid_argument("invalid traversal: " + text);
    }

    std::string to_string(TraversalType traversal)
    {
        switch (traversal)
        {
        case TraversalType::BFS:
            return "bfs";
        case TraversalType::DFS:
            return "dfs";
        }
        return "unknown";
    }

    TraversalMetrics run_BFS(const Graph &graph, int start)
    {
        if (graph.num_vertices() == 0)
        {
            return {};
        }

        std::vector<bool> visited(graph.num_vertices(), false);
        std::queue<int> frontier;

        visited[start] = true;
        frontier.push(start);

        TraversalMetrics metrics{};
        while (!frontier.empty())
        {
            metrics.peak_frontier = std::max(metrics.peak_frontier, frontier.size());
            int u = frontier.front();
            frontier.pop();
            metrics.visited_nodes++;

            for (int v : graph.neighbors(u))
            {
                if (!visited[v])
                {
                    visited[v] = true;
                    frontier.push(v);
                }
            }
        }

        return metrics;
    }

    TraversalMetrics run_dfs(const Graph &graph, int start_vertex)
    {
        if (graph.num_vertices() == 0)
        {
            return {};
        }

        std::vector<bool> visited(graph.num_vertices(), false);
        std::vector<int> stack;
        stack.push_back(start_vertex);

        TraversalMetrics metrics{};
        while (!stack.empty())
        {
            metrics.peak_frontier = std::max(metrics.peak_frontier, stack.size());
            const int u = stack.back();
            stack.pop_back();

            if (visited[static_cast<std::size_t>(u)])
            {
                continue;
            }

            visited[static_cast<std::size_t>(u)] = true;
            ++metrics.visited_nodes;

            auto nbrs = graph.neighbors(u);
            for (auto it = nbrs.rbegin(); it != nbrs.rend(); ++it)
            {
                if (!visited[static_cast<std::size_t>(*it)])
                {
                    stack.push_back(*it);
                }
            }
        }
        return metrics;
    }

    TraversalMetrics run_traversal(const Graph &graph, TraversalType traversal_type, int start_vertex)
    {
        utils::validate_vertex(graph, start_vertex);
        switch (traversal_type)
        {
        case TraversalType::BFS:
            return run_BFS(graph, start_vertex);
        case TraversalType::DFS:
            return run_dfs(graph, start_vertex);
        default:
            throw std::invalid_argument("Unsupported traversal type");
        }
    }

}