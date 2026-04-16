from __future__ import annotations

import random
from .schemas import GraphSpec

def generate_edges(spec: GraphSpec) -> list[tuple[int, int]]:
    spec.validate()

    if spec.graph_type != "gnp":
        raise NotImplementedError(f"Graph type {spec.graph_type} not supported")
    
    rng  = random.Random(spec.seed)
    edges: list[tuple[int, int]] = []

    n = spec.num_vertices
    p = spec.edge_prob
    assert p is not None

    if spec.directed:
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < p:
                    edges.append((u, v))

    else:
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < p:
                    edges.append((u, v))
    return edges