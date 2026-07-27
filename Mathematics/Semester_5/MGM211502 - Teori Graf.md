---
title: MGM211502 - Teori Graf (Graph Theory)
type: course
semester: 5
sks: 3
tags: [mathematics, graph-theory, combinatorics, algorithms, semester-5]
created: 2026-07-27
---

# MGM211502 - Teori Graf (Graph Theory)

> *"A graph is a mathematical structure modeling relations between objects."*
> **SKS:** 3 | **Semester:** 5 | **Prerequisite:** [[Algorithms]], [[Linear Algebra Fundamentals]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Basic Definitions | Vertices, edges, types, degree |
| 2 | Paths and Cycles | Walks, trails, Eulerian paths |
| 3 | Trees | Properties, spanning trees, counting |
| 4 | Connectivity | Components, Menger's theorem |
| 5 | Planar Graphs | Euler's formula, Kuratowski |
| 6 | Graph Coloring | Chromatic number, four-color theorem |
| 7 | Matchings | Hall's theorem, König's theorem |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Digraphs | Tournaments, strongly connected |
| 10 | Network Flow | Max-flow min-cut theorem |
| 11 | Spectral Graph Theory | Adjacency matrix, eigenvalues |
| 12 | Random Graphs | Erdős-Rényi model |
| 13 | Graph Algorithms | DFS, BFS, applications |
| 14 | Applications | Network design, scheduling |
| 15 | Final Review | Integration project |

## 📚 Core Theorems

### 1. Handshaking Lemma

$$\sum_{v \in V} \deg(v) = 2|E|$ $

### 2. Euler's Formula
For connected planar graphs: $ V - E + F = 2 $

### 3. Kuratowski's Theorem
$ G $ is planar $\iff $ contains no subdivision of $ K_5 $ or $ K_{3,3} $.

### 4. Max-Flow Min-Cut

$ $\max_{f} |f| = \min_{(S,T)} c(S,T)

$$

### 5. Menger's Theorem
The maximum number of vertex-disjoint $ s $-$ t $ paths equals the minimum size of an $ s $-$ t $ vertex cut.

## 📊 Spectral Graph Theory

The **adjacency matrix** $ A $ of a graph:
- $\lambda_1 $ (largest eigenvalue): $\lambda_1 \geq \bar{d} $ (average degree)
- **Spectral gap** $\lambda_1 - \lambda_2 $: measures connectivity/expansion
- **Algebraic connectivity** $\lambda_2 $ of Laplacian $ L = D - A $: positive $\iff $ connected

### Laplacian Matrix

$ L = D - A $ where $ D = ext{deg}(v_i) $.

Properties:
- $\lambda_1 = 0 $ (always)
- $\lambda_2 > 0 \iff $ connected
- Number of zero eigenvalues = number of connected components

## 💡 Solved Example: Network Flow

**Problem:** Find the maximum flow from $ s $ to $ t $ in:

```
s --(3)-- A --(2)-- t
s --(4)-- B --(3)-- t
A --(2)-- B
```

**Solution using Ford-Fulkerson:**
1. Augment $ s o A o t $ (flow 2): residual $ s o A(1) $, $ A o t(0) $
2. Augment $ s o B o t $ (flow 3): residual $ s o B(1) $, $ B o t(0) $
3. Augment $ s o A o B o t $: path blocked ($ B o t $ saturated)
4. Min-cut: $\{s\} $ vs $\{A, B, t\} $, capacity $ 3 + 4 = 7 $
5. **Maximum flow = 7**

## 📐 Applications to Geodesy

| Concept | Application |
|---------|-------------|
| **MST** | Survey network design |
| **Shortest Path** | GNSS baseline network |
| **Network Flow** | Data routing optimization |
| **Graph Coloring** | Frequency assignment |
| **Spectral Analysis** | Network connectivity quality |

## 🎯 Practice Problems

1. Prove every tree with $ n $ vertices has exactly $ n-1$ edges.
2. Apply Dijkstra's algorithm to find shortest paths in a GNSS network.
3. Find a maximum matching in a bipartite survey network.
4. Compute spectral gap of a random geometric graph.
5. Design a survey network that is 2-connected (redundant).

## 📖 References

- West, D.B. (2001). *Introduction to Graph Theory*. Prentice Hall.
- Diestel, R. (2017). *Graph Theory* (5th ed.). Springer.
- Biggs, N.L. (1993). *Algebraic Graph Theory*. Cambridge.

---
*See also: [[Graph Theory]], [[Algorithms]], [[Linear Algebra Fundamentals]], [[Optimization Theory]]*
