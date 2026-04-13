from dataclasses import dataclass

from graph_tradeoff.graph.traversals.results import TraversalResult


@dataclass(frozen=True)
class ExperimentResult:
    traversal: TraversalResult
    runtime_sec: float


@dataclass(frozen=True)
class BenchmarkRecord:
    graph_structure: str
    graph_representation: str
    traversal_type: str
    n: int
    runtime_sec: float
    peak_frontier: int
    edge_prob: float | None = None
    runtime_env:str = "python"
