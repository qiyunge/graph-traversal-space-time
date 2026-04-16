#include <algorithm>
#include <stdexcept>
#include <string>
//
#include "graph_tradeoff/utils.hpp"
#include "graph_tradeoff/graph.hpp"

namespace graph_tradeoff::utils
{

    void normalize_ascii_lower(std::string &text)
    {
        std::ranges::transform(text, text.begin(), [](unsigned char c)
                               { return std::tolower(c); });
    }

    std::string normalized_ascii_lower(std::string text)
    {
        normalize_ascii_lower(text);
        return text;
    }

    void validate_vertex(const Graph &graph, int u)
    {
        if (u < 0 || static_cast<std::size_t>(u) >= graph.num_vertices())
        {
            throw std::out_of_range("Vertex index out of range");
        }
    }

} // end of namespace graph_tradeoff::utils