from graph_tradeoff.graph.graph_adt import Graph
from graph_tradeoff.graph.traversals.results import TraversalResult


def dfs(graph: Graph, start: int) -> TraversalResult:
    n = graph.num_vertices()
    if not 0 <= start < n:
        raise IndexError(f"start vertex {start} out of range [0, {n})")

    visited = [False] * n
    stack = [start]
    visited[start] = True

    order: list[int] = []
    peak_frontier = 1

    while stack:
        peak_frontier = max(peak_frontier, len(stack))

        v = stack.pop()
        order.append(v)

        neighbors = list(graph.neighbors(v))
        for u in reversed(neighbors):
            if not visited[u]:
                visited[u] = True
                stack.append(u)

    return TraversalResult(
        order=order,
        visited_count=len(order),
        peak_frontier=peak_frontier,
    )
