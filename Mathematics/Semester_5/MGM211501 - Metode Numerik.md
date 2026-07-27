---
title: MGM211501 - Metode Numerik (Numerical Methods Advanced)
type: course
semester: 5
sks: 3
tags: [mathematics, numerical-methods, optimization, interpolation, semester-5]
created: 2026-07-27
---

# MGM211501 - Metode Numerik (Numerical Methods)

> *"The purpose of computing is insight, not numbers."* — Richard Hamming
> **SKS:** 3 | **Semester:** 5 | **Prerequisite:** [[Numerical Methods]], [[Linear Algebra Fundamentals]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Numerical ODE | Runge-Kutta, multistep methods |
| 2 | Stiff Equations | Implicit methods, stability regions |
| 3 | BVP Methods | Shooting, finite differences |
| 4 | PDE Intro | Classification (hyperbolic, parabolic, elliptic) |
| 5 | Finite Difference | Stability, convergence, CFL condition |
| 6 | Optimization Intro | Unconstrained methods |
| 7 | Constrained Optimization | KKT conditions, penalty methods |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | SVD & PCA | Singular value decomposition |
| 10 | Iterative Methods | Krylov methods, CG, GMRES |
| 11 | Sparse Systems | Structure exploitation |
| 12 | Monte Carlo | Sampling, variance reduction |
| 13 | Numerical Integration | Adaptive quadrature |
| 14 | Case Studies | Real geodetic computation |
| 15 | Final Review | Integration project |

## 📚 Core Methods

### Runge-Kutta Methods

For $y' = f(t, y) $, $ y(t_0) = y_0 $:

**RK4:**

$ $\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f(t_n + h/2, y_n + h k_1/2) \\
k_3 &= f(t_n + h/2, y_n + h k_2/2) \\
k_4 &= f(t_n + h, y_n + h k_3) \\
y_{n+1} &= y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}

$ $**Accuracy:**$ O(h^4) $ local error,$ O(h^4) $ global error.

### SVD (Singular Value Decomposition)

Any $ m imes n $ matrix $  A $:

$ $  A = U \Sigma V^T $ $

where $ U \in \mathbb{R}^{m imes m} $, $\Sigma = ext{diag}(\sigma_1, \dots, \sigma_p) $, $  V \in \mathbb{R}^{n imes n} $.

**Applications:**
- Least squares: $ x = V \Sigma^+ U^T b $
- PCA: $\sigma_i^2 $= variance explained by $  i $-th component
- Numerical rank: count $\sigma_i > \varepsilon $

## 📐 Geodesy Application: GNSS Ambiguity Resolution

The **LAMBDA method** for integer ambiguity resolution:
1. Float solution via least squares
2. Integer search in ambiguity lattice
3. Z-transform decorrelation (reduce correlation)
4. Search for best integer vectors

$ $\hat{N} = \arg\min_{N \in \mathbb{Z}^n} \|N - \hat{N}_{float}\|_{Q_N}^2

$ $

## 🎯 Practice Problems

1. Solve $ y' = -2y + t, y(0) = 1 $ using RK4 with $ h=0.1 $.
2. Implement GMRES for a sparse system $ Ax = b $ from surveying data.
3. Apply Monte Carlo integration to estimate $ i$ and compare with Simpson's rule.
4. Perform SVD on a design matrix and identify ill-conditioning.
5. Implement interior-point method for a linear programming problem.

## 📖 References

- Burden, R.L. & Faires, J.D. (2010). *Numerical Analysis*. Brooks/Cole.
- Trefethen, L.N. & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.
- Quarteroni, A. et al. (2007). *Numerical Mathematics*. Springer.

---
*See also: [[Numerical Methods]], [[Optimization Theory]], [[Linear Algebra Fundamentals]], [[QR Factorization]]*
