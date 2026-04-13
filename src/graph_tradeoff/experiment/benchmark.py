import random

from graph_tradeoff.graph.graph_adt import Graph
from graph_tradeoff.experiment.runner import run_once
from graph_tradeoff.graph.traversals.bfs import bfs
from graph_tradeoff.graph.traversals.dfs import dfs
from graph_tradeoff.graph.adjacency_list import AdjacencyListGraph
from graph_tradeoff.graph.adjacency_matrix import AdjacencyMatrixGraph
from graph_tradeoff.experiment.results import BenchmarkRecord


def build_line_graph(graph_cls, n: int) -> Graph:
    g = graph_cls(n)
    for i in range(n - 1):
        g.add_edge(i, i + 1)
    return g

def build_binary_tree(graph_cls, n: int)-> Graph:
    g = graph_cls(n)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            g.add_edge(i, left)
        if right < n:
            g.add_edge(i, right)

    return g




def build_random_graph(graph_cls, n: int, edge_prob: float, seed: int = 42) -> Graph:
    random.seed(seed)
    g = graph_cls(n)

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                g.add_edge(i, j)

    return g

graph_builders = [
    ("line", build_line_graph),
    ("tree", build_binary_tree),
    ("random", None),
]
ps = [0.01, 0.05, 0.1]

graph_types = [
    ("list", AdjacencyListGraph),
    ("matrix", AdjacencyMatrixGraph),
]

traversals = [
    ("bfs", bfs),
    ("dfs", dfs),
]

sizes = [100, 500, 1000, 2000]

def run_benchmark():
    records: list[BenchmarkRecord] = []

    for n in sizes:
        for structure_name, build_fn in graph_builders:
            for graph_name, graph_cls in graph_types:
                if structure_name == "random":
                    for p in ps:
                        g = build_random_graph(graph_cls, n, p)
                        for trav_name, trav_fn in traversals:
                            result = run_once(g, trav_fn, start=0)

                            records.append(
                                BenchmarkRecord(
                                    graph_structure=f"{structure_name}(p={p})",
                                    graph_representation=graph_name,
                                    traversal_type=trav_name,
                                    n=n,
                                    edge_prob=p,
                                    runtime_sec=result.runtime_sec,
                                    peak_frontier=result.traversal.peak_frontier,
                                )
                            )
                else:
                    g = build_fn(graph_cls, n)

                    for trav_name, trav_fn in traversals:
                        result = run_once(g, trav_fn, start=0)

                        records.append(
                            BenchmarkRecord(
                                graph_structure=structure_name,
                                graph_representation=graph_name,
                                traversal_type=trav_name,
                                n=n,
                                edge_prob=None,
                                runtime_sec=result.runtime_sec,
                                peak_frontier=result.traversal.peak_frontier,
                            )
                        )

    return records


def print_records(records):
    for r in records:
        print(
            f"{r.graph_structure:6} | {r.graph_representation:6} | {r.traversal_type:3} | n={r.n:5} "
            f"| edge_prob={r.edge_prob} | runtime={r.runtime_sec:.6f} | peak={r.peak_frontier} | env={r.runtime_env}"
            
        )
