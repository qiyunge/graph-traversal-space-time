# src/graph/adjacency_matrix.py

from typing import Iterable
from .graph_adt import Graph


class AdjacencyMatrixGraph(Graph):
    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("number of vertices must be non-negative")
        self._n = n
        self._mat: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]

    def num_vertices(self) -> int:
        return self._n

    def neighbors(self, v: int) -> Iterable[int]:
        self._validate_vertex(v)
        return [u for u in range(self._n) if self._mat[v][u] == 1]

    def add_edge(self, u: int, v: int) -> None:
        self._validate_vertex(u)
        self._validate_vertex(v)
        self._mat[u][v] = 1
        self._mat[v][u] = 1

    def _validate_vertex(self, v: int) -> None:
        if not 0 <= v < self._n:
            raise IndexError(f"vertex {v} out of range [0, {self._n})")

    def __repr__(self) -> str:
        return f"AdjacencyMatrixGraph(n={self._n}, mat={self._mat})"
