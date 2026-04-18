from __future__ import annotations

from pathlib import Path
from matplotlib.lines import Line2D
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import pandas as pd

from graph_tradeoff.metrics.metrics import (
    build_env_speedup_table,
    build_representation_ratio_table,
)

plotting_config = {
  "linestyle_map": {
    "adj_list": "-",
    "adj_matrix": "--"
  },
  "marker_map": {
    "adj_list": "o",
    "adj_matrix": "s"
},
"color_map": {
    500: "tab:red",
    1000: "tab:blue",
    10000: "tab:orange",
    5000: "tab:green"
},

"linewidth_map": {
    "adj_list": 2.5,
    "adj_matrix": 1.5
},
"legend_n" :[
    Line2D([0], [0],
           color={500: "tab:red", 1000: "tab:blue", 10000: "tab:orange", 5000: "tab:green"}.get(n),
          
           label=f"n={n}")
    for n in [1000, 10000]
],

# Legend 2: representation
"legend_rep" :[
    Line2D([0], [0],
           color="black",
           linestyle={"adj_list": "-", "adj_matrix": "--"}.get(rep),

           label=rep.replace("_", " ").title())
    for rep in ["adj_list", "adj_matrix"]
]

}


def _finalize_plot(fig, ax, title: str, xlabel: str, ylabel: str, save_path=None):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=200)

    return fig, ax


def plot_runtime_vs_density(df: pd.DataFrame, save_path=None):
    plot_df = df.sort_values(
        by=["graph_representation", "traversal_type", "runtime_env", "density_p"]
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    for (representation, traversal, env), group in plot_df.groupby(
        ["graph_representation", "traversal_type", "runtime_env"], sort=True
    ):
        ax.plot(
            group["density_p"],
            group["runtime_sec"],
            marker="o",
            label=f"{representation} | {traversal} | {env}",
        )

    return _finalize_plot(
        fig, ax,
        title="Traversal Runtime vs Graph Density",
        xlabel="Graph density p",
        ylabel="Runtime (seconds)",
        save_path=save_path,
    )


def plot_peak_frontier_vs_density(df: pd.DataFrame, save_path=None):
    plot_df = df.sort_values(
        by=["graph_representation", "traversal_type", "runtime_env", "density_p"]
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    for (representation, traversal, env), group in plot_df.groupby(
        ["graph_representation", "traversal_type", "runtime_env"], sort=True
    ):
        ax.plot(
            group["density_p"],
            group["peak_frontier"],
            marker="o",
            label=f"{representation} | {traversal} | {env}",
        )

    return _finalize_plot(
        fig, ax,
        title="Peak Frontier vs Graph Density",
        xlabel="Graph density p",
        ylabel="Peak frontier",
        save_path=save_path,
    )


def plot_env_speedup(df: pd.DataFrame, save_path=None):
    speedup_df = build_env_speedup_table(df)

    fig, ax = plt.subplots(figsize=(10, 6))

    for (representation, traversal), group in speedup_df.groupby(
        ["graph_representation", "traversal_type"], sort=True
    ):
        ax.plot(
            group["density_p"],
            group["speedup_python_over_cpp"],
            marker="o",
            label=f"{representation} | {traversal}",
        )

    return _finalize_plot(
        fig, ax,
        title="Python / C++ Runtime Speedup vs Graph Density",
        xlabel="Graph density p",
        ylabel="Speedup (python / cpp)",
        save_path=save_path,
    )


def plot_representation_runtime_ratio(df: pd.DataFrame, save_path=None):
    ratio_df = build_representation_ratio_table(df)

    fig, ax = plt.subplots(figsize=(10, 6))

    for (env, traversal), group in ratio_df.groupby(
        ["runtime_env", "traversal_type"], sort=True
    ):
        ax.plot(
            group["density_p"],
            group["matrix_over_list_runtime"],
            marker="o",
            label=f"{env} | {traversal}",
        )

    return _finalize_plot(
        fig, ax,
        title="Adjacency Matrix / Adjacency List Runtime Ratio",
        xlabel="Graph density p",
        ylabel="Runtime ratio (adj_matrix / adj_list)",
        save_path=save_path,
    )