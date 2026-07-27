---
tags: [aigis, concept, computer-science, algorithms]
created: 2026-07-27
---

# Algorithms

## Overview

Algorithms are step-by-step procedures for calculations, data processing, and automated reasoning. In geomatics and geodesy, algorithms underpin GIS spatial analysis, least-squares adjustment (penyesuaian kuadrat terkecil), signal processing of GNSS data, and triangulation networks.

The study of algorithms is fundamentally about **efficiency**: given a problem, how much time and memory does the best known method require, and how do we improve it?

## Algorithmic Complexity & Big-O Notation

**Big-O notation** ( $O(\cdot) $) describes the upper bound of an algorithm's growth rate as the input size $  n $ grows. Formally,$ f(n) = O(g(n)) $ means there exist positive constants $  c $ and $ n_0 $ such that $ 0 \le f(n) \le c \cdot g(n) $ for all $  n \ge n_0 $.

### Common complexity classes (Kelas kompleksitas umum)

| Notation | Name | Example | Bahasa Indonesia |
|----------|------|---------|------------------|
| $ O(1) $ | Constant | Array index access | Waktu konstan |
| $ O(\log n) $ | Logarithmic | Binary search | Pencarian biner |
| $ O(n) $ | Linear | Linear scan through array | Waktu linear |
| $ O(n \log n) $ | Linearithmic | Merge sort, quicksort (average) | Pengurutan gabungan |
| $ O(n^{2}) $ | Quadratic | Bubble sort, naive matrix multiply | Waktu kuadratik |
| $ O(n^{3}) $ | Cubic | Floyd-Warshall (all-pairs shortest path) | Waktu kubik |
| $ O(2^{n}) $ | Exponential | Brute-force TSP (traveling salesman) | Waktu eksponensial |
| $ O(n!) $ | Factorial | Permutation enumeration | Waktu faktorial |

**Notasi Omega** ( $\Omega $) gives the lower bound; **Theta** ( $\Theta $) gives a tight bound. For instance:

- Merge sort is $\Theta(n \log n) $— always this efficient.

- Quicksort is $ O(n \log n) $ on average but $ O(n^2) $ in the worst case (pivot terburuk).

**Kompleksitas ruang** (space complexity) measures the additional memory required beyond the input. An in-place sort is $ O(1) $ space; merge sort is $ O(n) $ space (membutuhkan memori tambahan).

## Sorting Algorithms (Pengurutan)

### 1. Quicksort (Urcepat)
**Average**$ O(n \log n) $, **worst** $ O(n^{2}) $, **space** $ O(\log n) $ stack depth.

Divide-and-conquer: choose a **pivot**, partition into elements $<$ pivot and $>$ pivot, recurse on each partition. Kinerja sangat bergantung pada pemilihan pivot (pemilihan pivot).

```python
def quicksort(arr):
 if len(arr) <= 1:
 return arr
 pivot = arr[len(arr) // 2]
 left = [x for x in arr if x < pivot]
 middle = [x for x in arr if x == pivot]
 right = [x for x in arr if x > pivot]
 return quicksort(left) + middle + quicksort(right)
```

### 2. Merge Sort (Gabungan)
**Always**$ O(n \log n) $, **space** $ O(n) $.

Stable sort; splits array in half, recursively sorts, merges. Cocok untuk data yang tersimpan di linked list maupun eksternal storage (penyimpanan eksternal).

### 3. Timsort (Hybrid)
Python's built-in sorting algorithm is Timsort — a hybrid of merge sort and insertion sort optimised for real-world data that often has pre-existing "runs" (urutan). $ O(n \log n) $ worst case,$ O(n) $ best case (jika data sudah sebagian terurut).

## Searching (Pencarian)

### Binary Search (Pencarian Biner) —$ O(\log n) $ Requires sorted input (input harus terurut). Repeatedly halves the search interval

$ $\text{mid} = \left\lfloor \frac{\text{low} + \text{high}}{2} \right\rfloor

$$

```python
def binary_search(arr, target):
 lo, hi = 0, len(arr) - 1
 while lo <= hi:
 mid = (lo + hi) // 2
 if arr[mid] == target:
 return mid
 elif arr[mid] < target:
 lo = mid + 1
 else:
 hi = mid - 1
 return -1 # not found (tidak ditemukan)
```

### Hash-based search —$ O(1) $ average
Using a hash table (tabel hash), lookup is constant time on average. Hash collisions handled by chaining (rantai) or open addressing (alamat terbuka).

## Numerical Algorithms (Algoritma Numerik)

Numerical algorithms are essential in computational geodesy and geomatics — closed-form solutions often don't exist for real-world geodetic problems.

### Newton-Raphson Method (Mencari akar / root-finding)
For solving $ f(x) = 0 $:

$ $ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Converges **quadratically** (cepat) when $ f'(x) \neq 0 $ near the root — quadratic convergence berarti galat dikuadratkan setiap iterasi.

### Least-Squares Adjustment (Penyesuaian Kuadrat Terkecil)
Given observations $\mathbf{L} $ and model $\mathbf{A}\,\mathbf{x} = \mathbf{L} $, the least-squares solution minimises the sum of squared residuals:

$ $\hat{\mathbf{x}} = (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T \mathbf{L} $$

This is the workhorse of geodetic network adjustment — used in GPS baseline processing, traverse adjustment, and geoid modelling.

### Gauss-Seidel Iteration (Penyelesaian sistem linear)
For solving $\mathbf{A}\mathbf{x} = \mathbf{b} $ iteratively $ $ x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right)$$

Converges if $\mathbf{A} $ is strictly diagonally dominant (dominan diagonal).

### QR Decomposition untuk Least Squares
Numerically more stable than normal equations

$ $\mathbf{A} = \mathbf{Q}\mathbf{R} \implies \hat{\mathbf{x}} = \mathbf{R}^{-1}\mathbf{Q}^T\mathbf{L} $$

# # Spatial / Geospatial Algorithms (Algoritma Spasial)

| Algorithm | Complexity | Use case | Bahasa Indonesia |
|-----------|-----------|----------|------------------|
| R-tree indexing | $ O(\log n) $ query | Spatial database queries (kueri basis data spasial) | Pengindeksan spasial |
| Delaunay triangulation | $ O(n \log n) $ | TIN construction, mesh generation | Triangulasi Delaunay |
| Convex hull (Graham scan) | $ O(n \log n) $ | Boundary computation | Cembung (convex hull) |
| Dijkstra / A* | $ O((V+E)\log V) $ | Shortest path routing | Rute terpendek |
| Sutherland-Hodgman | $ O(n)$ per clip | Polygon clipping (pemotongan poligon) | Penggeseran poligon |

## Python Implementation Example

A minimal numerical algorithm — solving a system of equations via Gauss-Seidel in Python:

```python
import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
 n = len(b)
 x = x0.copy() if x0 is not None else np.zeros(n)
 for k in range(max_iter):
 x_new = x.copy()
 for i in range(n):
 s1 = np.dot(A[i, :i], x_new[:i])
 s2 = np.dot(A[i, i+1:], x[i+1:])
 x_new[i] = (b[i] - s1 - s2) / A[i, i]
 if np.linalg.norm(x_new - x) < tol:
 return x_new, k + 1
 x = x_new
 return x, max_iter
```

Similarly, a binary search in pure Python:

```python
def binary_search(sorted_arr, target):
 lo, hi = 0, len(sorted_arr) - 1
 while lo <= hi:
 mid = (lo + hi) // 2
 if sorted_arr[mid] == target:
 return mid
 elif sorted_arr[mid] < target:
 lo = mid + 1
 else:
 hi = mid - 1
 return None # tidak ditemukan
```

## Related

- [[Algorithms]] · [[Algorithms]] · [[Mathematics MOC]]

---
*Concept maintained by AIGIS — part of [[Mathematics MOC]]*
