from graph_tradeoff.experiment.runner import run_once
from graph_tradeoff.graph.adjacency_list import AdjacencyListGraph
from graph_tradeoff.graph.traversals.bfs import bfs


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


def test_run_once_bfs():
    g = build_sample_graph()
    result = run_once(g, bfs, start=0)

    assert result.traversal.order == [0, 1, 2, 3, 4, 5, 6]
    assert result.traversal.visited_count == 7
    assert result.traversal.peak_frontier == 4
    assert result.runtime_sec >= 0.0
