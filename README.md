# Graph Traversal Benchmarking Framework

### Space–Time Trade-offs in Graph Traversal  
*An Empirical Study of BFS, DFS, and Graph Representations*

---

## 🧠 Overview

This project builds a **controlled experimental framework** to analyze the **practical time–space trade-offs** of graph traversal algorithms.

We focus on:

- Algorithms: **BFS / DFS**
- Representations: **Adjacency List / Adjacency Matrix**
- Runtime environments: **Python vs C++**

The goal is to understand how **algorithm choice, data structure, and execution environment** jointly affect performance.

---

## 🎯 Objectives

- Design a **Graph ADT abstraction layer**
- Decouple:
  - traversal logic  
  - graph representation  
- Build a **reproducible benchmarking pipeline**
- Measure:
  - runtime  
  - visited nodes  
  - peak frontier (exploration scale)
- Compare results across **Python and C++**

---

## 🧩 Project Structure
``` txt
        graph-tradeoff/
        ├── analysis/ # notebook + exported report ⭐⭐⭐
        │ ├── analysis.ipynb
        │ └── analysis.html
        │
        ├── cpp/ # C++ implementation
        │ ├── include/
        │ ├── src/
        │ ├── build/
        │ └── CMakeLists.txt
        │
        ├── src/graph_tradeoff/ # Python core package
        │ ├── core/ # graph abstraction & data model
        │ ├── execution/ # traversal execution layer
        │ ├── experiment/ # experiment runner
        │ ├── metrics/ # metrics + plotting
        │ ├── benchmark/ # benchmark orchestration
        │ ├── data/ # graph generation / loading
        │ ├── config.py # experiment configuration ⭐
        │ └── main.py # entry point
        │
        ├── datasets/ # generated graph data
        ├── outputs/ # intermediate outputs
        ├── results/ # final results
        ├── reports/ # exported reports
        └── tests/
```


---

## ⚙️ Configuration (Very Important)

All experiment settings are controlled via:

Key parameters:

```python
BASE_DIR = Path(__file__).parent.parent.parent
CPP_EXE_DIR = BASE_DIR / "cpp"
DATASETS_DIR = BASE_DIR / "datasets"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

```
---
## ⚡ C++ Implementation

The project includes a C++ version to validate performance trends.

▶ Build (CMake)
```script
cd cpp
mkdir build
cd build
cmake ..
cmake --build . --config release
```

💡 Notes
C++ version is used for performance comparison
Python is used for experimentation & analysis
Results should be consistent in trend across both

---

## 🧪 Experimental Design

To ensure fairness:

Same graph instance across runs
- Fixed random seed
- Controlled variables:
- number of nodes (n)
- edge density (p)
- representation
- algorithm

---

## 📊 Metrics

We collect:

- Runtime (execution time)
- Visited nodes
- Peak frontier size

⚠️ Note:

Peak frontier reflects exploration scale, not exact memory usage.

---

## 🧠 Key Insights
- BFS and DFS show similar runtime (O(V + E))
- Representation is the dominant performance factor
- Adjacency list outperforms matrix in sparse graphs
- Graph density strongly affects exploration scale
- Python vs C++ mainly differs in constant factors
  
---

## 🧭 Future Work
Cache behavior analysis
Parallel traversal
Real-world graph datasets
Visualization UI

---
## 👤 Author

Qiyun Ge
Montreal, Canada
grantnj.ge@gmail.com