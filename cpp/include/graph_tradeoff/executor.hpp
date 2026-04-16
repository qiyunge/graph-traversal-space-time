#pragma once

#include <string>


namespace graph_tradeoff
{

    struct ExecutionConfig
    {
        std::string edge_meta_file{""};
        std::string algorithm{"bfs"};
        std::string representation{"list"};
    };

    struct ExectutionResult
    {
        std::size_t visited_nodes{0};
        std::size_t peak_frontier{0};
        double runtime_sec{0.0};
    };


    ExectutionResult execute_traversal(const ExecutionConfig &config);
    

} // namespace graph_tradeoff