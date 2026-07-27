---
title: Semester 5 — Teori Graf (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, graph-theory, semester-5, aigis, geodesy-applied]
---

# Semester 5 — Teori Graf (Expanded)

**Course**: MGM211502 — Teori Graf  
**Credits**: 3 SKS  
**Prerequisites**: [[Aljabar Linear Lanjut Expanded]]

---

## Course Overview

Graph theory studies discrete structures composed of vertices (nodes) and edges (connections). It is the mathematical foundation for network analysis, optimization, and modeling relationships in geodetic networks.

---

## Syllabus

### Unit 1: Basic Definitions

- **Graph**: $G = (V, E)$with vertex set$V$and edge set$E$- **Types**: Simple, multigraph, directed, weighted, bipartite, planar

- **Degree**:$\\deg(v)$= number of incident edges

- **Handshaking Lemma**:$\\sum_{v \\in V} \\deg(v) = 2|E|$### Unit 2: Connectivity

- **Paths, cycles, trails**: Sequences of adjacent vertices

- **Connected graphs**: Every pair of vertices has a path between them

- **Components**: Maximal connected subgraphs

- **Cut vertices/edges**: Removal increases number of components

- **Blocks**: Maximal 2-connected subgraphs

### Unit 3: Trees

- **Tree**: Connected, acyclic graph

- **Properties**:$|E| = |V| - 1$, unique path between any two vertices

- **Spanning trees**: Tree containing all vertices of $G$- **Minimum spanning tree**: Kruskal's algorithm, Prim's algorithm

- **Cayley's formula**:$n^{n-2}$spanning trees of$K_n$### Unit 4: Eulerian and Hamiltonian Graphs

- **Eulerian trail**: Uses each edge exactly once
  -$G$has Eulerian circuit$\\iff$all vertices have even degree
  -$G$has Eulerian path$\\iff$exactly 0 or 2 vertices have odd degree

- **Hamiltonian cycle**: Visits each vertex exactly once
  - Dirac's theorem: If$\\deg(v) \\geq n/2$for all$v$, then $G$is Hamiltonian
  - Finding Hamiltonian cycles is NP-complete

### Unit 5: Graph Coloring

- **Vertex coloring**: Adjacent vertices get different colors

- **Chromatic number**$\\chi(G)$: Minimum number of colors needed

- **Four Color Theorem**: Planar graphs have $\\chi \\leq 4$- **Edge coloring**: Vizing's theorem:$\\Delta \\leq \\chi' \\leq \\Delta+1$### Unit 6: Planar Graphs

- **Planarity**: Can be drawn without edge crossings

- **Kuratowski's theorem**: Non-planar$\\iff$contains subdivision of$K_5$or$K_{3,3}$- **Euler's formula**: For connected planar graph:$|V| - |E| + |F| = 2$

### Unit 7: Network Flows

- **Flow network**: Directed graph with capacity on edges

- **Max flow**: Maximum s-t flow equals minimum s-t cut capacity

- **Ford-Fulkerson**: Augmenting path algorithm

- **Applications**: Network design, routing

### Unit 8: Graph Algorithms

- **BFS/DFS**: Traversal algorithms

- **Shortest paths**: Dijkstra's algorithm, Bellman-Ford

- **All-pairs shortest paths**: Floyd-Warshall

- **Topological sorting**: For directed acyclic graphs

---

## Geodesy Applications

- **Geodetic networks**: Vertices = stations, edges = observations

- **Network design**: Optimal placement of stations (spanning trees)

- **Adjustment quality**: Graph connectivity indicates redundancy

- **Deformation monitoring**: Detect changes in network structure

- **Routing**: Optimizing field survey routes (traveling salesman)

---

## References

- Diestel, R. (2017). *Graph Theory* (5th ed.)

- Bondy, J.A. & Murty, U.S.R. (2008). *Graph Theory*

---

➡️ [[Mathematics MOC]]