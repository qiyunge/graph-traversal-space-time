 
from dataclasses import dataclass

from graph_tradeoff.core import Representation, TraversalKind
from graph_tradeoff.execution import Backend
@dataclass(frozen=True,slots=True)
class ExperimentSpec:

    num_vertices:int
    edge_prob:float
    graph_repr:str
    traversal:str
    backend:str
    dataset_path:str="datasets"
    directed:bool = False
    seed:int=42
    graph_type:str = "gnp" # only gnp supported for now, but can be extended in the future

@dataclass(frozen=True,slots=True)
class ExperimentResult:
    traversal_order: list[int]
    traversal_visited_count: int
    traversal_peak_frontier: int
    runtime_sec: float

    
@dataclass(frozen=True,slots=True)
class ExperimentRecord:
    experiment_spec: ExperimentSpec
    experiment_result: ExperimentResult

    def __str__(self) -> str:
        spec = self.experiment_spec
        result = self.experiment_result
        return (f"ExperimentRecord(\n"
                f"  num_vertices={spec.num_vertices},\n"
                f"  edge_prob={spec.edge_prob},\n"
                f"  graph_repr='{spec.graph_repr}',\n"
                f"  traversal='{spec.traversal}',\n"
                f"  backend='{spec.backend}',\n"
                f"  directed={spec.directed},\n"
                f"  seed={spec.seed},\n"
                f"  graph_type='{spec.graph_type}',\n"
                f"  runtime_sec={result.runtime_sec},\n"
                f"  traversal_visited_count={result.traversal_visited_count},\n"
                f"  traversal_peak_frontier={result.traversal_peak_frontier}\n"
                f"  traversal_order={result.traversal_order}\n"
                f")")   