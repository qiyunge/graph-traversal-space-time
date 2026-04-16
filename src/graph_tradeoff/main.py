
from graph_tradeoff.data.schemas import GraphSpec

from .config import RESULTS_DIR
from pathlib import Path
from graph_tradeoff.execution.types import ExecutionResult, ExecutionSpec
from dataclasses import replace
from graph_tradeoff.experiment.types import ExperimentSpec, ExperimentResult, ExperimentRecord
from graph_tradeoff.experiment.runner import run_experiment_once
from graph_tradeoff.data.dataset_manager import DatasetManager


def main():
    experiment_spec = ExperimentSpec(
    num_vertices=1000,
    edge_prob=0.01,
    seed=42,
    graph_repr= "adj_list",
    traversal="dfs",
    backend="cpp",
    dataset_path="datasets",
)
    
    dataset_path = Path(experiment_spec.dataset_path)
    data_manager = DatasetManager(dataset_path)

    experment_rst = run_experiment_once(experiment_spec, data_manager)

    record = ExperimentRecord(
        experiment_spec=experiment_spec,
        experiment_result=experment_rst
    )

    # spec_py = replace(execution_spec, backend="python")
    # spec_cpp = replace(execution_spec, backend="cpp")

   

    # result_py = run_experiment_once(spec_py)
    # result_cpp = run_experiment_once(spec_cpp)

    # records = run_benchmark()
    # print_records(records)
    # export_to_csv(records, output_path=RESULTS_DIR / "benchmark.csv")

    # plot_runtime_vs_n(records, output_dir=RESULTS_DIR)
    # plot_peak_frontier_vs_n(records, output_dir=RESULTS_DIR)
    print(record)
    print("Plots saved to results/")


if __name__ == "__main__":
    main()
