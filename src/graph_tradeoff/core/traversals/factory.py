from enum import Enum

from graph_tradeoff.core.graph.graph_adt import Graph
from graph_tradeoff.core.types import TraversalStatistics

from .bfs import bfs
from .dfs import dfs    
from typing import Callable

class TraversalKind(str, Enum):
    BFS = "bfs"
    DFS = "dfs"
    
def get_traversal_function(traversal: TraversalKind | str) -> Callable[[Graph, int], TraversalStatistics]:
    traversal = TraversalKind(traversal) if isinstance(traversal, str) else traversal
    if traversal == TraversalKind.BFS:
        return bfs
    elif traversal == TraversalKind.DFS:
        return dfs
    else:
        raise ValueError(f"unknown traversal: {traversal}")