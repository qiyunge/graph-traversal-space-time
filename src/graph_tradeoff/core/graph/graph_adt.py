from abc import ABC, abstractmethod
from typing import Iterable


class Graph(ABC):
    """
    Graph Abstract Data Type (ADT)

    This interface defines the minimal contract required by traversal algorithms.
    It decouples algorithm logic from underlying graph representation.
    """

    @abstractmethod
    def num_vertices(self) -> int:
        """Return number of vertices in the graph"""
        pass

    @abstractmethod
    def neighbors(self, v: int) -> Iterable[int]:
        """
        Return an iterable of neighbors of vertex v
        """
        pass

    @abstractmethod
    def add_edge(self, u: int, v: int) -> None:
        """Add an edge between u and v"""
        pass
