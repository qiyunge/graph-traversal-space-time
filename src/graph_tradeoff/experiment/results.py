from dataclasses import dataclass


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
