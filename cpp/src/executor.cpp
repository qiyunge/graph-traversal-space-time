#include "graph_tradeoff/executor.hpp"
#include "graph_tradeoff/generator.hpp"
#include "graph_tradeoff/traversal.hpp"

#include <fstream>
#include <iostream>
#include <chrono>

namespace graph_tradeoff
{

    ExectutionResult execute_traversal(const ExecutionConfig &config)
    {
        auto graph = load_graph_from_manifest(config.edge_meta_file, config.representation);

        const auto start = std::chrono::steady_clock::now();
        const auto metrics = run_traversal(*graph, parse_traversal(config.algorithm), 0);
        const auto end = std::chrono::steady_clock::now();

        const std::chrono::duration<double> elapsed = end - start;

        // Here you would implement the actual traversal logic using the meta information.
        // For now, we return dummy results.
        return ExectutionResult{
            .visited_nodes = std::size_t(metrics.visited_nodes),
            .peak_frontier = std::size_t(metrics.peak_frontier),
            .runtime_sec = elapsed.count()};
        
    }

} // namespace graph_tradeoff