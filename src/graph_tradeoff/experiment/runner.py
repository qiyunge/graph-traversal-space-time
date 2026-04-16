from pathlib import Path
from graph_tradeoff.core.graph.factory import Representation
from graph_tradeoff.core.traversals.factory import TraversalKind
from graph_tradeoff.data.dataset_manager import DatasetManager
from graph_tradeoff.execution.types import Backend, ExecutionSpec, ExecutionResult   
from graph_tradeoff.execution.factory import get_executor
from graph_tradeoff.data import GraphSpec
from .types import ExperimentRecord, ExperimentSpec, ExperimentResult




def run_experiment_once(

    experiment_spec:ExperimentSpec,
    dataset_split:str = "cache"

   
) -> ExperimentRecord:
    
    dataset_path = Path(experiment_spec.dataset_path)
    dataset_manager = DatasetManager(dataset_path)
    
    graph_spec=GraphSpec(
        num_vertices=experiment_spec.num_vertices,
        edge_prob=experiment_spec.edge_prob,
        seed=experiment_spec.seed,
        graph_type= experiment_spec.graph_type,
        directed=experiment_spec.directed
    )
   
    execution_spec = ExecutionSpec(
    graph_spec= graph_spec,
    backend= Backend(experiment_spec.backend),
    representation=Representation(experiment_spec.graph_repr),
    traversal=TraversalKind(experiment_spec.traversal)
       
    )

    executor = get_executor(execution_spec.backend)
    dataset_manager.ensure_dataset(graph_spec, split=dataset_split)
    
    
    execution_rst = executor(execution_spec,dataset_manager)
    if execution_rst.error is not None:
        raise RuntimeError(f"Execution failed with error: {execution_rst.error}")
    
    result = ExperimentResult(
        traversal_order=execution_rst.traversal_stats.order,
        traversal_visited_count=execution_rst.traversal_stats.visited_count,
        traversal_peak_frontier=execution_rst.traversal_stats.peak_frontier,
        runtime_sec=execution_rst.runtime_sec
    )
    return ExperimentRecord(
        experiment_spec=experiment_spec,
        experiment_result=result
    )

    
    