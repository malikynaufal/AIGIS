---
code: FKD211206
name: Pemrograman Lanjutan
SKS: 3
semester: 2
department: Informatika
tags: [programming, scientific-computing, algorithms, data-structures]
created: 2026-07-27
---

# FKD211206 — Pemrograman Lanjutan (Scientific Computing)

## Course Overview

Advanced programming for scientific computing — extending Python skills with data structures, algorithms, numerical methods, and scientific library design. This course equips students with tools to tackle large-scale physics computations, simulations, and data analysis pipelines.

**Contact Hours:** 3 SKS (1 hour lecture + 2 hours lab per week)
**Prerequisites:** Pengantar Pemrograman (FKD211105), Kalkulus I, Kalkulus II
**Co-requisites:** Fisika Dasar II

---

## 📋 Topics & Outline

### Unit 1: Advanced Python (Weeks 1–4)

- **Object-Oriented Programming:**
  - Classes, `__init__`, `self`, inheritance, polymorphism
  - Encapsulation, abstraction, and composition
  - Example: `class Particle: def __init__(self, x, y, z, mass): ...`

- **Decorators and generators**
  - `@timer`, `@cached` decorators
  - Generator functions with `yield`

- **File I/O:** binary files, JSON serialization, CSV writing

- **Exception handling** — custom exception classes

- **Testing:** `pytest` fundamentals, unit tests for physics functions

- **Virtual environments** and package management (`pip`, `requirements.txt`)

### Unit 2: Data Structures and Algorithms (Weeks 5–9)

- **Algorithm complexity:** Big-O notation — O(1), O(n), O(n log n), O(n²)

- **Sorting:** quicksort, mergesort, bisect for sorted lists

- **Searching:** binary search, hash tables for fast lookup

- **Trees and graphs** (introductory): tree traversal, BFS/DFS

- **Numerical data structures:** NumPy ndarray operations, memory layout

- **Performance profiling:** `%timeit`, `cProfile`, identifying bottlenecks

- **Vectorization:** replacing Python loops with NumPy array operations

### Unit 3: Numerical Methods (Weeks 10–14)

- **Numerical integration:**
  - Trapezoidal rule, Simpson's rule
  - Monte Carlo integration (random sampling)

- **Root finding:**
  - Bisection method
  - Newton-Raphson method: x_{n+1} = x_n - f(x_n)/f'(x_n)
  - Secant method (derivative-free)

- **Numerical differentiation:**
  - Forward difference: f'(x) ≈ (f(x+h) - f(x))/h
  - Central difference (more accurate): f'(x) ≈ (f(x+h) - f(x-h))/(2h)

- **Numerical ODE solvers:**
  - Euler method: y_{n+1} = y_n + h·f(x_n, y_n)
  - **Runge-Kutta 4th order (RK4):**
    ```python
    k1 = h*f(x_n, y_n)
    k2 = h*f(x_n + h/2, y_n + k1/2)
    k3 = h*f(x_n + h/2, y_n + k2/2)
    k4 = h*f(x_n + h, y_n + k3)
    y_{n+1} = y_n + (k1 + 2k2 + 2k3 + k4)/6
    ```

- **Linear algebra** with NumPy/SciPy: `np.linalg.solve(A, b)`, eigenvalues

### Unit 4: Scientific Visualization and Projects (Weeks 15–18)

- **3D plotting** with Matplotlib and Mayavi

- **Animation** with Matplotlib FuncAnimation

- **Data pipelines:** reading raw experimental data → processing → plotting → saving

- **Reproducible research:** Jupyter notebooks, version control with Git

- **Final project:** build a physics simulation (e.g., N-body, EM field solver) with full documentation

---

## 🔬 Key Algorithms

```
Bisection:           bracket root, halve interval each step
Newton-Raphson:      x_{n+1} = x_n - f(x_n)/f'(x_n)  (quadratic convergence)
Euler (ODE):         y_{n+1} = y_n + h·f(x_n, y_n)  (first-order)
RK4 (ODE):           see formulas above (fourth-order, O(h⁴) local error)
Trapezoidal:         ∫f dx ≈ Δx/2 · (f₀ + 2f₁ + 2f₂ + ... + f_N)
Simpson:             ∫f dx ≈ Δx/3 · (f₀ + 4f₁ + 2f₂ + 4f₃ + ... + f_N)
Monte Carlo:         I ≈ (b-a)/N · Σ f(x_i), x_i ~ Uniform(a,b)
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Design and implement object-oriented code for physics simulations
2. Analyze algorithm complexity and choose efficient data structures
3. Implement numerical methods (integration, root-finding, ODE solving) in Python
4. Apply vectorization and profiling to optimize scientific code
5. Build reproducible data analysis pipelines with Jupyter notebooks
6. Create a complete physics simulation project from specification to documentation

---

## 📚 References

1. Downey, A.B. (2015). *Think Python*, 2nd ed. O'Reilly.
2. Langtangen, H.P. (2016). *Scientific Computing with Python 3*, 2nd ed. Springer.
3. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.
4. Press, W.H. et al. (2007). *Numerical Recipes*, 3rd ed. Cambridge.
5. SciPy Lecture Notes: https://scipy-lectures.org/
6. NumPy Documentation: https://numpy.org/doc/
