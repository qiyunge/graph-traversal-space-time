#pragma once

#include <string>
#include "graph_tradeoff/graph.hpp"
namespace graph_tradeoff::utils
{
    void normalize_ascii_lower(std::string &text);

    std::string normalized_ascii_lower(std::string text);

    void validate_vertex(const Graph &graph, int u);
   

} // end of namespace