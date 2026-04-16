#include "graph_tradeoff/benchmark.hpp"

#include <chrono>
#include <iomanip>
#include <iostream>

namespace graph_tradeoff {

BenchmarkResult run_single_benchmark(const GraphBuildConfig& config, TraversalType traversal) {
    auto graph = generate_graph(config);

    const auto start = std::chrono::steady_clock::now();
    const auto metrics = run_traversal(*graph, traversal, 0);
    const auto end = std::chrono::steady_clock::now();

    const std::chrono::duration<double> elapsed = end - start;

    return BenchmarkResult{
        config.n,
        config.edge_prob,
        config.seed,
        config.structure,
        config.representation,
        traversal,
        metrics.visited_nodes,
        metrics.peak_frontier,
        elapsed.count(),
    };
}

std::vector<BenchmarkResult> run_all_benchmarks(const GraphBuildConfig& base_config) {
    std::vector<BenchmarkResult> results;

    for (const auto repr : {GraphRepresentation::AdjacencyList, GraphRepresentation::AdjacencyMatrix}) {
        for (const auto traversal : {TraversalType::BFS, TraversalType::DFS}) {
            GraphBuildConfig config = base_config;
            config.representation = repr;
            results.push_back(run_single_benchmark(config, traversal));
        }
    }

    return results;
}

void print_result(const BenchmarkResult& result) {
    std::cout << std::left
              << std::setw(8) << to_string(result.traversal)
              << std::setw(10) << to_string(result.representation)
              << std::setw(10) << to_string(result.structure)
              << "n=" << std::setw(6) << result.n
              << " p=" << std::setw(8) << result.edge_prob
              << " visited=" << std::setw(6) << result.visited_nodes
              << " peak=" << std::setw(6) << result.peak_frontier
              << " runtime=" << std::fixed << std::setprecision(6) << result.runtime_sec << " sec"
              << '\n';
}

}  // namespace graph_tradeoff
