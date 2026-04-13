from typing import Iterable
from .graph_adt import Graph


class AdjacencyListGraph(Graph):
    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("number of vertices must be non-negative")
        self._n = n
        self._adj: list[list[int]] = [[] for _ in range(n)]

    def num_vertices(self) -> int:
        return self._n

    def neighbors(self, v: int) -> Iterable[int]:
        self._validate_vertex(v)
        return self._adj[v]

    def add_edge(self, u: int, v: int) -> None:
        self._validate_vertex(u)
        self._validate_vertex(v)

        self._adj[u].append(v)
        self._adj[v].append(u)

    def _validate_vertex(self, v: int) -> None:
        if not 0 <= v < self._n:
            raise IndexError(f"vertex {v} out of range [0, {self._n})")

    def __repr__(self) -> str:
        return f"AdjacencyListGraph(n={self._n}, adj={self._adj})"
