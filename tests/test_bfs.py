from graph_tradeoff.core.graph.adjacency_list import AdjacencyListGraph
from graph_tradeoff.core.traversals.bfs import bfs

edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
]


def build_sample_graph():
    g = AdjacencyListGraph(7)

    for u, v in edges:
        g.add_edge(u, v)
    return g


def test_bfs_basic():
    g = build_sample_graph()
    result = bfs(g, 0)

    assert result.order == [0, 1, 2, 3, 4, 5, 6]
    assert result.visited_count == 7
    assert result.peak_frontier == 4
