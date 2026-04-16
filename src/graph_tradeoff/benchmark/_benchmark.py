

from graph_tradeoff.benchmark.results import BenchmarkRecord
from graph_tradeoff.experiment.runner import run_experiment_once
from graph_tradeoff.experiment  import ExperimentSpec
from graph_tradeoff.benchmark.export import export_to_csv
from graph_tradeoff  import config

ps = [0.01, 0.05, 0.1,0.6]

graph_reprs = [
    "adj_list",
    "adj_matrix"
]

traversals = [
    "bfs",
    "dfs"
]

backends = [
    "python", 
    "cpp"
]

sizes = [ 1000]
graphy_types = ["gnp"]

dataset_path = "datasets" 

 
seed = 42

def run_benchmark(experiment_name:str = "experiment_1"):
    output_path = config.RESULTS_DIR/ f"{experiment_name}/benchmark.csv"
    records: list[BenchmarkRecord] = []


    for n in sizes:
        for graph_repr in graph_reprs: 
                for p in ps:
                    for trav_name in traversals:
                        for backend in backends:
                           
                            experiment_spec = ExperimentSpec(
                                dataset_path=dataset_path,
                                num_vertices=n,
                                edge_prob=p,
                                seed=seed,
                                graph_type=graphy_types[0],
                                directed=False,
                                backend=backend,
                                graph_repr=graph_repr,
                                traversal=trav_name
                            )
                            record = run_experiment_once(experiment_spec)

                            records.append(
                                BenchmarkRecord(
                                    graph_structure=f"RandomGraph(p={p})",
                                    graph_representation=graph_repr,
                                    traversal_type=trav_name,
                                    n=n,
                                    edge_prob=p,
                                    runtime_sec=record.experiment_result.runtime_sec,
                                    peak_frontier=record.experiment_result.traversal_peak_frontier,
                                    visited_count=record.experiment_result.traversal_visited_count,
                                    runtime_env=backend
                                )
                            )
            
    export_to_csv(records,output_path=output_path)
    print_records(records)
    return records


def print_records(records):
    for r in records:
        print(
            f"{r.graph_structure:6} | {r.graph_representation:6} | {r.traversal_type:3} | n={r.n:5} "
            f"| edge_prob={r.edge_prob} | runtime={r.runtime_sec:.6f} | peak={r.peak_frontier} | visited={r.visited_count} | env={r.runtime_env}"
            
        )
