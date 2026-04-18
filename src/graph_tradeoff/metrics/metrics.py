from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


# =========================
# Loading & preprocessing
# =========================

def load_results(csv_path: str | Path) -> pd.DataFrame:
    csv_path = Path(csv_path)
    df = pd.read_csv(csv_path)

    df = df.copy()
    df["density_p"] = df["graph_structure"].apply(_extract_density_p)

    return df


def _extract_density_p(graph_structure: str) -> float:
    match = re.search(r"p\s*=\s*([0-9]*\.?[0-9]+)", str(graph_structure))
    if not match:
        raise ValueError(f"Cannot parse p from {graph_structure}")
    return float(match.group(1))


# =========================
# Core summaries
# =========================

def build_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic aggregation (ready for report / plotting)

    Currently uses mean (since single-run data).
    Later you can add std, median.
    """

    summary = df.groupby([
        "graph_structure",
        "density_p",
        "graph_representation",
        "traversal_type",
        "runtime_env",
        "n",
    ], as_index=False).agg(
        runtime_mean=("runtime_sec", "mean"),
        peak_frontier_mean=("peak_frontier", "mean"),
        visited_mean=("visited_count", "mean"),
    )

    return summary.sort_values(
        by=["density_p", "traversal_type",  "graph_representation", "runtime_env" ]
    )


# =========================
# Environment comparison
# =========================

def build_env_speedup_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    python vs cpp speedup

    speedup = python / cpp
    """

    pivot = df.pivot_table(
        index=[
            "graph_structure",
            "density_p",
            "graph_representation",
            "traversal_type",
            "n",
        ],
        columns="runtime_env",
        values="runtime_sec",
        aggfunc="mean",
    ).reset_index()

    _check_columns(pivot, ["python", "cpp"], "runtime_env")

    pivot["speedup_python_over_cpp"] = pivot["python"] / pivot["cpp"]

    return pivot.sort_values(
        by=["graph_representation", "traversal_type", "density_p"]
    )


# =========================
# Representation comparison
# =========================

def build_representation_ratio_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    adj_matrix vs adj_list

    ratio = matrix / list
    """

    pivot = df.pivot_table(
        index=[
            "graph_structure",
            "density_p",
            "traversal_type",
            "runtime_env",
            "n",
        ],
        columns="graph_representation",
        values="runtime_sec",
        aggfunc="mean",
    ).reset_index()

    _check_columns(pivot, ["adj_list", "adj_matrix"], "graph_representation")

    pivot["matrix_over_list_runtime"] = (
        pivot["adj_matrix"] / pivot["adj_list"]
    )

    return pivot.sort_values(
        by=["runtime_env", "traversal_type", "density_p"]
    )


# =========================
# Traversal comparison
# =========================

def build_traversal_ratio_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    DFS vs BFS

    ratio = dfs / bfs
    """

    pivot = df.pivot_table(
        index=[
            "graph_structure",
            "density_p",
            "graph_representation",
            "runtime_env",
            "n",
        ],
        columns="traversal_type",
        values="runtime_sec",
        aggfunc="mean",
    ).reset_index()

    _check_columns(pivot, ["bfs", "dfs"], "traversal_type")

    pivot["dfs_over_bfs_runtime"] = pivot["dfs"] / pivot["bfs"]

    return pivot.sort_values(
        by=["runtime_env", "graph_representation", "density_p"]
    )


# =========================
# Helper
# =========================

def _check_columns(df: pd.DataFrame, required: list[str], name: str):
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing {name} columns: {missing}")


# =========================
# Pretty printing (optional)
# =========================

def print_top_speedups(df: pd.DataFrame, top_k: int = 10):
    table = build_env_speedup_table(df)
    table = table.sort_values(by="speedup_python_over_cpp", ascending=False)
    print("\n=== Top speedups (Python / C++) ===")
    print(table.head(top_k).to_string(index=False))


def print_representation_penalty(df: pd.DataFrame, top_k: int = 10):
    table = build_representation_ratio_table(df)
    table = table.sort_values(by="matrix_over_list_runtime", ascending=False)
    print("\n=== Worst adjacency matrix penalties ===")
    print(table.head(top_k).to_string(index=False))


# =========================
# Entry
# =========================

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit("Usage: python metrics.py <csv_path>")

    csv_path = sys.argv[1]
    df = load_results(csv_path)

    print_top_speedups(df)
    print_representation_penalty(df)