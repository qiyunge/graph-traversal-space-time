import time
from graph_tradeoff.core.graph.factory import build_graph, Representation
from graph_tradeoff.core.types import TraversalStatistics
from graph_tradeoff.core.traversals.factory import TraversalKind,get_traversal_function
from graph_tradeoff.core.traversals.bfs import bfs
from graph_tradeoff.core.traversals.dfs import dfs

from graph_tradeoff.data.dataset_manager import DatasetManager

from .types import ExecutionSpec,ExecutionResult



def run_python_executor(execution_spec: ExecutionSpec, dataset_manager: DatasetManager)->ExecutionResult:
    
    graph_spec = execution_spec.graph_spec
    edges = dataset_manager.load_edges(graph_spec)
    nnum_vertices = graph_spec.num_vertices
    representation = execution_spec.representation
    traversal_kind = execution_spec.traversal
    directed = graph_spec.directed
    start_vertex = execution_spec.start_vertex

    # create graph instance based on the specified representation and run the traversal, measuring execution time
    graph = build_graph(edges, nnum_vertices, representation,directed=directed)
    traversal_function = get_traversal_function(traversal_kind)
  

    start = time.perf_counter()
    result = traversal_function(graph, start=start_vertex)
    runtime = time.perf_counter() - start

    return ExecutionResult.from_stats(
        runtime_sec=runtime,
        traversal_stats= result
    )
       
