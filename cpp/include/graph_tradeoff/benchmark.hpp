#pragma once
#include "graph_tradeoff/traversal.hpp"
#include "graph_tradeoff/generator.hpp"
#include "graph_tradeoff/utils.hpp"


#include <string>
#include <vector>

namespace graph_tradeoff {

struct BenchmarkResult {
    std::size_t n{0};
    double edge_prob{0.0};
    unsigned int seed{0};
    GraphStructure structure{GraphStructure::Random};
    GraphRepresentation representation{GraphRepresentation::AdjacencyList};
    TraversalType traversal{TraversalType::BFS};
    std::size_t visited_nodes{0};
    std::size_t peak_frontier{0};
    double runtime_sec{0.0};
};

BenchmarkResult run_single_benchmark(const GraphBuildConfig& config, TraversalType traversal);
std::vector<BenchmarkResult> run_all_benchmarks(const GraphBuildConfig& base_config);
void print_result(const BenchmarkResult& result);

}  // namespace graph_tradeoff

