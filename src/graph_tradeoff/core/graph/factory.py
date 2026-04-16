
from .adjacency_list import AdjacencyListGraph
from .adjacency_matrix import AdjacencyMatrixGraph
from enum import Enum

class Representation(str, Enum):
    ADJ_LIST = "adj_list"
    ADJ_MATRIX = "adj_matrix"



def build_graph(
    edges: list[tuple[int, int]],
    num_vertices: int,
    representation: Representation | str,
    directed: bool = False,
):
    representation = Representation(representation) if isinstance(representation, str) else representation
    if representation == Representation.ADJ_LIST:
        graph = AdjacencyListGraph(num_vertices)
    elif representation == Representation.ADJ_MATRIX:
        graph = AdjacencyMatrixGraph(num_vertices)
    else:
        raise ValueError(f"Unknown representation: {representation}")

    for u, v in edges:
        graph.add_edge(u, v)

    return graph