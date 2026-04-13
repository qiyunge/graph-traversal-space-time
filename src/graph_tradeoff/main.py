
from .config import RESULTS_DIR
from graph_tradeoff.experiment.benchmark import run_benchmark, print_records
from graph_tradeoff.experiment.plotting import (
    plot_peak_frontier_vs_n,
    plot_runtime_vs_n,
)
from graph_tradeoff.experiment.export import export_to_csv

def main():
    records = run_benchmark()
    print_records(records)
    export_to_csv(records, output_path=RESULTS_DIR / "benchmark.csv")

    plot_runtime_vs_n(records, output_dir=RESULTS_DIR)
    plot_peak_frontier_vs_n(records, output_dir=RESULTS_DIR)

    print("Plots saved to results/")


if __name__ == "__main__":
    main()
