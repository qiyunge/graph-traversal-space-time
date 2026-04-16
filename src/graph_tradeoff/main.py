
from graph_tradeoff.data.schemas import GraphSpec

from graph_tradeoff.benchmark import run_benchmark
def main():
    experiment_name = "experiment_1"

    recordes = run_benchmark(experiment_name=experiment_name)
    print("Plots saved to results/")


if __name__ == "__main__":
    main()
