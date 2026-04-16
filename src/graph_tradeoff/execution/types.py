from dataclasses import dataclass   ,asdict
from graph_tradeoff.core.graph.factory import Representation
from graph_tradeoff.core.traversals.factory import TraversalKind
from graph_tradeoff.core.types import TraversalStatistics
from enum import Enum

from graph_tradeoff.data.schemas import GraphSpec   

class Backend(str, Enum):
    PYTHON = "python"
    CPP = "cpp"



@dataclass(frozen=True, slots=True)
class ExecutionSpec:
    graph_spec: GraphSpec
    backend: Backend
    representation: Representation
    traversal: TraversalKind
    start_vertex: int = 0 # default start vertex for traversal, can be extended to support more complex parameters in the future

    def to_dict(self):
        return asdict(self)
    
    def key(self):
        return (str(self.graph_spec), self.backend, self.representation, self.traversal, self.start_vertex)   
        


@dataclass(frozen=True, slots=True)
class ExecutionResult:
  
    # ---traversal metrics---
    runtime_sec: float
    traversal_stats: TraversalStatistics | None # None if execution failed

    # -- execution status --
    success: bool
    error: str | None = None

    def to_dict(self):
        return asdict(self)
    
    def key(self): # equal to ExecutionSpec.key, but defined here for convenience   
        return (self.graph_spec, self.backend, self.representation, self.traversal, self.start_vertex)
    
    @classmethod
    def from_stats(cls,
                     *,
                    
                     runtime_sec: float,
                     traversal_stats: TraversalStatistics)-> "ExecutionResult":
        return cls(
           
            runtime_sec=runtime_sec,
            traversal_stats=traversal_stats,
            success=True,
            error=None,
        )
    
    @classmethod
    def failure(
        cls,
        *,
        error: str,
    ) -> "ExecutionResult":
        return cls(
           
            runtime_sec=0.0,
            traversal_stats=None,
            success=False,
            error=error,
        )
   