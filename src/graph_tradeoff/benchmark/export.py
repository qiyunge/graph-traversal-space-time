import csv
from pathlib import Path

from .results import BenchmarkRecord


def export_to_csv(
    records: list[BenchmarkRecord],
    output_path: str = "results/benchmark.csv",
) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="") as f:
        writer = csv.writer(f)

        # header
        writer.writerow(
            [
                "graph_structure",
                "graph_representation",
                "traversal_type",
                "n",
                "runtime_sec",
                "peak_frontier",
                "visited_count",
                "runtime_env",
            ]
        )

        # rows
        for r in records:
            writer.writerow(
                [
                    r.graph_structure,
                    r.graph_representation,
                    r.traversal_type,
                    r.n,
                    r.runtime_sec,
                    r.peak_frontier,
                    r.visited_count,
                    r.runtime_env,
                ]
            )