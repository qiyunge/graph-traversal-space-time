from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt

from graph_tradeoff.experiment.benchmark import BenchmarkRecord


def _group_records(
    records: list[BenchmarkRecord],
) -> dict[tuple[str, str, str], list[BenchmarkRecord]]:
    grouped: dict[tuple[str, str, str], list[BenchmarkRecord]] = {}

    for record in records:
        key = (record.graph_structure, record.graph_representation, record.traversal_type)
        grouped.setdefault(key, []).append(record)

    for key in grouped:
        grouped[key] = sorted(grouped[key], key=lambda r: r.n)

    return grouped


def _plot_metric(
    records: list[BenchmarkRecord],
    metric_fn: Callable[[BenchmarkRecord], float],
    ylabel: str,
    title: str,
    filename: str,
    output_dir: str = "results",
) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    grouped = _group_records(records)

    plt.figure(figsize=(8, 5))

    for (graph_structure, graph_representation, traversal_type), group_records in grouped.items():
        xs = [r.n for r in group_records]
        ys = [metric_fn(r) for r in group_records]
        label = f"{graph_structure}-{graph_representation}-{traversal_type}"
        plt.plot(xs, ys, marker="o", label=label)

    plt.xlabel("Number of vertices (n)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(Path(output_dir) / filename)
    plt.close()


def plot_runtime_vs_n(records: list[BenchmarkRecord], output_dir: str = "results") -> None:
    _plot_metric(
        records=records,
        metric_fn=lambda r: r.runtime_sec,
        ylabel="Runtime (sec)",
        title="Runtime vs n",
        filename="runtime_vs_n.png",
        output_dir=output_dir,
    )


def plot_peak_frontier_vs_n(
    records: list[BenchmarkRecord], output_dir: str = "results"
) -> None:
    _plot_metric(
        records=records,
        metric_fn=lambda r: r.peak_frontier,
        ylabel="Peak frontier",
        title="Peak frontier vs n",
        filename="peak_frontier_vs_n.png",
        output_dir=output_dir,
    )