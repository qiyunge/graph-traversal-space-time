from collections import deque

from graph_tradeoff.core.graph.graph_adt import Graph
from graph_tradeoff.core.types import TraversalStatistics


def bfs(graph: Graph, start: int) -> TraversalStatistics:
    n = graph.num_vertices()
    if not 0 <= start < n:
        raise IndexError(f"start vertex {start} out of range [0, {n})")

    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    order: list[int] = []
    peak_frontier = 1

    while queue:
        peak_frontier = max(peak_frontier, len(queue))

        v = queue.popleft()
        order.append(v)

        for u in graph.neighbors(v):
            if not visited[u]:
                visited[u] = True
                queue.append(u)

    return TraversalStatistics(
        order=order,
        visited_count=len(order),
        peak_frontier=peak_frontier,
    )
