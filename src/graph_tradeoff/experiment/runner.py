from time import perf_counter
from typing import Callable

from graph_tradeoff.experiment.results import ExperimentResult
from graph_tradeoff.graph.graph_adt import Graph
from graph_tradeoff.graph.traversals.results import TraversalResult

TraversalFn = Callable[[Graph, int], TraversalResult]


def run_once(
    graph: Graph, traversal_fn: TraversalFn, start: int = 0
) -> ExperimentResult:
    t0 = perf_counter()
    traversal_result = traversal_fn(graph, start)
    t1 = perf_counter()

    return ExperimentResult(
        traversal=traversal_result,
        runtime_sec=t1 - t0,
    )
