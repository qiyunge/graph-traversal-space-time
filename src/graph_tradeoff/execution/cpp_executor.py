import subprocess
import json

from graph_tradeoff.core.graph.factory import build_graph, Representation
from graph_tradeoff.core.types import TraversalStatistics
from graph_tradeoff.core.traversals.factory import TraversalKind,get_traversal_function
from graph_tradeoff.core.traversals.bfs import bfs
from graph_tradeoff.core.traversals.dfs import dfs
from graph_tradeoff.data.dataset_manager import DatasetManager

from .types import ExecutionSpec,ExecutionResult


cpp_executor_path = "cpp/build/Debug/graph_tradeoff.exe"  # Update this path to your C++ executable

def run_cpp_executor(execution_spec: ExecutionSpec, dataset_manager: DatasetManager)->ExecutionResult:
    graph_spec = execution_spec.graph_spec
    meta_path = dataset_manager.get_paths(graph_spec).meta_file
    nnum_vertices = graph_spec.num_vertices
    representation = execution_spec.representation
    traversal_kind = execution_spec.traversal
    directed = graph_spec.directed
    start_vertex = execution_spec.start_vertex

    print(f"Running C++ executor with graph_spec: {graph_spec}, representation: {representation}, traversal: {traversal_kind}, directed: {directed}, start_vertex: {start_vertex}")
    print(f"Running C++ executor with graph_spec: {graph_spec}, representation: {representation.value}, traversal: {traversal_kind.value}, directed: {directed}, start_vertex: {start_vertex}")

    cmd = [cpp_executor_path, "--meta",str(meta_path.resolve()),
           "--repr", representation.value, "--algo", traversal_kind.value]
    print(f"Running C++ executor with command: {' '.join(cmd)}")
    # Convert the input data to JSON format
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"C++ Executor Raw Output:\n{result.stdout}")
    stats = json.loads(result.stdout)  # Ensure the output is valid JSON


    if result.returncode != 0:
        return ExecutionResult.failure(
           
            error=result.stderr
        )
  
    print(f"C++ Executor Output:\n{result.stdout}")
    # cpp_output = json.loads(result.stdout)
    # stats = TraversalStatistics(visited_count=cpp_output["visited_count"], peak_frontier=cpp_output["peak_frontier"], order=cpp_output["order"]  )

    return ExecutionResult.from_stats(
 
        runtime_sec= stats["runtime_sec"] ,  # You might want to capture this from the C++ output
        traversal_stats= TraversalStatistics(visited_count=stats["visited_count"], 
                                             peak_frontier=stats["peak_frontier"], order= [] )
    )
   