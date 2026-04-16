from typing import Type
from .core.graph.graph_adt import Graph


def build_graph(graph_cls: Type[Graph], n: int, edges: list[tuple[int, int]]) -> Graph:
    g = graph_cls(n)
    for u, v in edges:
        g.add_edge(u, v)
    return g
