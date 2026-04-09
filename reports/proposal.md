# Space–Time Trade-offs in Graph Traversal: An Empirical Study of BFS and DFS

## Motivation

Breadth-First Search (BFS) and Depth-First Search (DFS) are fundamental graph traversal algorithms. Although both have the same asymptotic time complexity, O(V + E), they exhibit different behaviors in practice, particularly in terms of memory usage and traversal order.
This project aims to demonstrate that algorithmic performance is inseparable from its underlying model, and that meaningful differences arise even when algorithms share identical Big-O bounds. By focusing on BFS and DFS, the project highlights the classic space–time trade-off central to data structures and algorithm design.

## Objectives

The objectives of this project are to:

- Define a clean Graph Abstract Data Type (ADT) independent of implementation details.
- Implement two graph representations:
  - Adjacency List
  - Adjacency Matrix
- Implement BFS and DFS against the same ADT.
- Empirically analyze how traversal strategy and representation affect:
  - auxiliary space usage
  - operation behavior
  - execution time
  - Validate that observed trends are algorithmic rather than language-specific.

## Data Structures and Algorithms

ADT: Graph interface with operations such as add_edge and neighbors(u).

### Representations:

- Adjacency List (space-efficient for sparse graphs)
- Adjacency Matrix (higher space cost, direct edge access)

### Algorithms:

- BFS (queue-based, higher auxiliary space)
- DFS (stack/recursion-based, lower auxiliary space)

### Methodology

Graphs will be generated with controlled size n and number of edges m:

- Sparse graphs: m ≈ 3n
- Dense graphs: m ≈ 0.2n²

- Multiple graph sizes will be tested (e.g., n = 200, 400, 800, 1600).
- Primary implementation will be in Python for clarity and rapid experimentation.

Measurements will include:

- wall-clock execution time
- number of neighbor accesses
- maximum queue size (BFS)
- maximum recursion/stack depth (DFS)

A minimal C++implementation will be used as a secondary validation layer to confirm that qualitative trends persist across languages.

### Expected Outcomes

BFS will demonstrate higher memory usage due to frontier expansion, illustrating a space-for-time strategy.

DFS will use less auxiliary space but may explore deeper paths first.

Adjacency lists will outperform adjacency matrices on sparse graphs, while differences will diminish on dense graphs.

Cross-language results will confirm that these behaviors arise from algorithmic strategy and data representation rather than implementation language.

## Deliverables

Python codebase implementing the Graph ADT, two representations, BFS/DFS, and experiment runner.

Minimal C++ validation code for BFS/DFS.

A concise final report summarizing theoretical analysis, experimental results, and interpretation.