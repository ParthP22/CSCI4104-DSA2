# CSCI 4104 — Data Structures & Algorithms II

Coursework archive for **CSCI 4104: Data Structures & Algorithms II**, Stockton
University, Fall 2023.

This repository collects the complete set of work from the course: five
programming assignments, six problem sets, and one supplementary utility written
to support a written problem. The programming assignments are written in
**Python 3**; the supplementary utility is written in **Java**.

Each assignment builds on graph and algorithm fundamentals — sorting, minimum
spanning trees, shortest paths, all-pairs shortest paths, and parallel
simulation — with an emphasis on implementing algorithms from the CLRS textbook
against a provided interface and then analyzing their empirical performance.

## Repository Structure

```
.
├── FloydWarshallAlgorithm/     Java utility supporting Problem Set 3
├── Problem Sets/               Written problem sets 1–6
├── Programming Assignment 1/   Sorting algorithms
├── Programming Assignment 2/   Graph file parsing and minimum spanning trees
├── Programming Assignment 3/   Dijkstra's algorithm and performance analysis
├── Programming Assignment 4/   Floyd–Warshall on adjacency matrices
├── Programming Assignment 5/   Parallel Monte Carlo simulation
└── README.md
```

## Programming Assignments

### Assignment 1 — Sorting

Implementation of two classic sorting algorithms along with supporting
utilities, written against a provided function interface.

- Insertion sort and heap sort, with the heap sort helpers (`_build_max_heap`,
  `_max_heapify`, `_left`, `_right`) implemented from the textbook pseudocode.
- `is_sorted` and `random_list` utilities used to verify correctness.

### Assignment 2 — Graph Parsing and Minimum Spanning Trees

Parsing of real-world highway graph data into a weighted graph representation,
then running minimum spanning tree algorithms over it.

- `graphfileparser.py` — parses TMG-format highway graph files into a
  `WeightedGraph`, computing edge weights from latitude/longitude pairs via the
  **haversine formula** for great-circle distance.
- Supporting data structures: `Graph`, `WeightedGraph`, and `Digraph`
  (`graphshw.py`), a binary min-heap and array-based priority queue (`intpq.py`),
  and a disjoint-set forest with union by rank and path compression
  (`disjointset.py`).
- MSTs computed with both **Kruskal's** and **Prim's** algorithms.
- Includes the TMG datasets used for testing (Albuquerque area, Andorra region,
  and Africa continent) plus captured program output.

### Assignment 3 — Dijkstra's Algorithm and Empirical Analysis

Implementation of Dijkstra's single-source shortest path algorithm, backed by
two interchangeable priority queue implementations, followed by a timing study
comparing them.

- `_dijkstra` implemented once against a priority queue interface, then driven by
  both a **binary min-heap** (`dijkstra_binheap`) and a **simple array**
  (`dijkstra_array`) backend.
- `shortestpathscomparison.py` — generates random weighted graphs across a range
  of sizes and densities and times both variants.
- `table.txt` — timing results for sparse and dense graphs from 32 to 2048
  vertices.
- `Question5Answer.txt` — written analysis reconciling the measured runtimes
  against the asymptotic bounds of O(E lg V) and O(V²), including discussion of
  where the empirical results diverge from theory.
- `extracredit.py` — extra credit; runs Dijkstra over a highway graph file
  supplied as a command line argument.

### Assignment 4 — Floyd–Warshall on Adjacency Matrices

All-pairs shortest paths over a matrix-based graph representation.

- `WeightedAdjacencyMatrix` and `WeightedDirectedAdjacencyMatrix` classes.
- `floyd_warshall` — computes all-pairs shortest path distances alongside a
  predecessor matrix for path reconstruction.
- `pair_shortest_path` — reconstructs the actual vertex sequence between any
  source and target from the predecessor matrix.
- `parse_highway_graph_matrix` and `haversine` — extra credit; loads highway
  graph data into the matrix representation.

### Assignment 5 — Parallel Monte Carlo Simulation

Estimation of π by Monte Carlo simulation, in sequential and parallel form.

- `pi_monte_carlo` — sequential estimation.
- `pi_parallel_monte_carlo` — parallel estimation across `p` processes using
  Python's `multiprocessing.Pool`.
- `generate_table` and `time` — produce convergence and timing tables comparing
  the sequential implementation against 1–4 worker processes.
- `output.txt.txt` — captured output showing estimates converging toward π as the
  sample count grows.

## Problem Sets

Six written problem sets covering the theoretical portion of the course,
submitted as PDFs. Problem Set 3 additionally includes a typed Word document
covering the applied portion, plus a revised PDF in which the first two problems
were rewritten more coherently for readability.

## Supplementary Code

`FloydWarshallAlgorithm/` is a small standalone Java program written to work
through problem 23.2-1 on Problem Set 3. It runs the Floyd–Warshall algorithm on
a fixed 6×6 weight matrix and prints the distance matrix after each iteration of
the outer loop, so that every intermediate step could be checked by hand. It was
not a required part of any assignment.

## A Note on Commit History

This coursework was completed in 2023 and committed to version control
retroactively. Each commit is dated to the last modification time of the work it
contains, so the history reflects the order and timing in which the assignments
were originally completed and submitted. Two commits note the use of the
course's late-submission waivers.

IDE configuration (`.idea/`) and build output (`__pycache__/`, `out/`) have been
retained as they existed at submission time.
