Progress Report

Space–Time Trade-offs in Graph Traversal under a Fixed Graph Model

Student: Qiyun Ge
Course: 420-A10-AS C2 — Introduction aux structures de donnée
Instructor: Ali Moridnejad
Date: March 2026

1. Project Title and Objective

This project studies the space–time trade-offs in graph traversal algorithms, focusing on the behavior of Breadth-First Search (BFS) and Depth-First Search (DFS) under a fixed graph and computation model.

Although BFS and DFS share the same asymptotic time complexity

T(V,E)=O(V+E)

their practical performance differs significantly, particularly in terms of auxiliary memory usage and traversal order.

The main objective of this project is to experimentally analyze these differences and determine how algorithm design and graph representation influence the observed space–time trade-offs.

The study is conducted under a consistent model in order to distinguish algorithmic behavior from implementation-specific effects.

2. Work Completed So Far

The following components of the project have been completed or designed:

Graph Abstraction

A clean Graph Abstract Data Type (ADT) has been designed to separate graph operations from their internal representation.
This abstraction allows traversal algorithms to operate independently of the underlying storage model.

Graph Representations

Two common graph representations have been prepared:

Adjacency List, which stores only existing edges and therefore uses space proportional to the number of vertices and edges.

Adjacency Matrix, which uses a fixed matrix representation and provides constant-time edge lookup at the cost of higher memory usage.

Traversal Algorithms

The traversal algorithms under investigation are:

Breadth-First Search (BFS)

Depth-First Search (DFS)

Both algorithms are implemented against the same Graph ADT to ensure that the comparison reflects algorithmic differences rather than structural ones.

Experimental Design

An experimental framework has been planned to measure:

execution time

number of visited nodes

peak frontier size (as an indicator of memory usage)

The experiments will run on graphs of varying sizes and densities in order to observe how algorithm behavior scales.

3. Preliminary Results

Initial implementations confirm the expected theoretical behavior of the traversal algorithms.

BFS explores nodes level by level and tends to maintain a large frontier (queue), which can lead to higher auxiliary memory usage.

DFS explores nodes along deep paths and therefore maintains a smaller frontier (stack), resulting in lower memory usage.

These observations support the hypothesis that BFS favors time efficiency in discovering shallow nodes, while DFS favors space efficiency during exploration.

4. Difficulties Encountered and Proposed Solutions

The main challenge encountered so far concerns ensuring fair comparisons between algorithms and representations.

Different graph representations may introduce constant-factor differences in runtime and memory access patterns.
To address this issue, the project uses a consistent Graph ADT so that traversal algorithms interact with the graph through the same interface.

Another challenge involves isolating algorithmic effects from language-specific implementation details.
To mitigate this, a minimal C++ implementation will be developed to validate that the observed trends are not specific to Python.

5. Next Steps

The remaining work will focus on completing the experimental study and producing the final report.
The next steps include:

Finalizing the Python implementations of BFS and DFS.

Generating test graphs with varying sizes and densities.

Running systematic experiments to measure runtime and memory usage.

Implementing minimal BFS and DFS versions in C++ for cross-language validation.

Collecting results and producing visualizations of the space–time trade-offs.

Writing the final report summarizing the experimental findings.

Conclusion

The project is progressing according to plan.
The core graph abstraction and traversal framework have been designed, and the next phase will focus on empirical analysis and validation of the theoretical space–time trade-offs between BFS and DFS.