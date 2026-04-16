#include "graph_tradeoff/benchmark.hpp"
#include "graph_tradeoff/generator.hpp"
#include "graph_tradeoff/traversal.hpp"
#include "graph_tradeoff/utils.hpp"
#include "graph_tradeoff/executor.hpp"
#include "nlohmann/json.hpp"

#include <exception>
#include <iostream>
#include <string>

using namespace graph_tradeoff;

namespace {
void print_usage() {
    std::cout
        << "Usage:\n"
        << "  graph_tradeoff --algo bfs --repr list --n 1000 --p 0.01 --structure random --seed 42\n"
        << "  graph_tradeoff --benchmark all --n 1000 --p 0.01 --structure random --seed 42\n";
}
}  // namespace

int main(int argc, char* argv[]) {
    try {
        // GraphBuildConfig config{};
        ExecutionConfig exec_config{};
      
      

        for (int i = 1; i < argc; ++i) {
            const std::string arg = argv[i];
            auto require_value = [&](const std::string& flag) -> std::string {
                if (i + 1 >= argc) {
                    throw std::invalid_argument("missing value for " + flag);
                }
                return argv[++i];
            };

            if (arg == "--algo") {
                exec_config.algorithm = require_value(arg);
                
            } else if (arg == "--repr") {
                // config.representation = parse_representation(require_value(arg));
                exec_config.representation = require_value(arg) ;
            // } else if (arg == "--n") {
            //     config.n = static_cast<std::size_t>(std::stoul(require_value(arg)));
            // } else if (arg == "--p") {
            //     config.edge_prob = std::stod(require_value(arg));
            // } else if (arg == "--seed") {
            //     config.seed = static_cast<unsigned int>(std::stoul(require_value(arg)));
            // } else if (arg == "--structure") {
            //     config.structure = parse_structure(require_value(arg));
            // } else if (arg == "--benchmark") {
            //     const std::string value = require_value(arg);
            //     if (value != "all") {
            //         throw std::invalid_argument("--benchmark only supports 'all'");
            //     }
            //     benchmark_all = true;
            }else if (arg == "--meta" || arg == "-m") {
                exec_config.edge_meta_file = require_value(arg);
              
            }
             else if (arg == "--help" || arg == "-h") {
                print_usage();
                return 0;

            }
             else {
                throw std::invalid_argument("unknown argument: " + arg);
            }
        }

        auto result =  execute_traversal(exec_config);
        nlohmann::json json_result = {
            {"visited_count", result.visited_nodes},
            {"peak_frontier", result.peak_frontier},
            {"runtime_sec", result.runtime_sec}
        };
        std::cout << json_result.dump() << std::endl;

      


        // if (benchmark_all) {
        //     for (const auto& result : run_all_benchmarks(config)) {
        //         print_result(result);
        //     }
        // } else {
        //     print_result(run_single_benchmark(config, traversal));
        // }


        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << '\n';
        print_usage();
        return 1;
    }
}
