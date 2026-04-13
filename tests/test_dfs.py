from graph_tradeoff.graph.adjacency_list import AdjacencyListGraph
from graph_tradeoff.graph.traversals.dfs import dfs


def build_sample_graph():
    g = AdjacencyListGraph(7)
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
    ]
    for u, v in edges:
        g.add_edge(u, v)
    return g


def test_dfs_basic():
    g = build_sample_graph()
    result = dfs(g, 0)

    assert result.order == [0, 1, 3, 4, 2, 5, 6]
    assert result.visited_count == 7
    assert result.peak_frontier == 3
