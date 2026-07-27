---
title: MGM211503 - Optimisasi (Optimization)
type: course
semester: 5
sks: 3
tags: [mathematics, optimization, linear-programming, nonlinear, semester-5]
created: 2026-07-27
---

# MGM211503 - Optimisasi (Optimization)

> *"The art of doing mathematics consists in finding that special case which contains all the germs of generality."* — Hilbert
> **SKS:** 3 | **Semester:** 5 | **Prerequisite:** [[Linear Algebra Fundamentals]], [[Multivariable Calculus]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Optimization Overview | Classification, convexity |
| 2 | Convex Sets | Separation, supporting hyperplane |
| 3 | Convex Functions | Properties, sublevel sets |
| 4 | Unconstrained Optimization | First/second order conditions |
| 5 | Gradient Descent | Line search, convergence rates |
| 6 | Newton's Method | Quasi-Newton, BFGS |
| 7 | Constrained: Equality | Lagrange multipliers |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | KKT Conditions | Inequality constraints |
| 10 | Duality | Weak/strong duality, Slater's condition |
| 11 | Linear Programming | Simplex method, duality |
| 12 | Integer Programming | Branch and bound |
| 13 | Semidefinite Programming | Matrix inequalities |
| 14 | Applications | Least squares, ML optimization |
| 15 | Final Review | Integration project |

## 📚 Core Theory

### Unconstrained Optimization

For $\min f(x) $:
- **1st order:** $\nabla f(x^*) = 0 $ (necessary)
- **2nd order:** $\nabla^2 f(x^*) \succeq 0 $ (necessary),$\nabla^2 f(x^*) \succ 0 $ (sufficient)

### Lagrange Multipliers

For $\min f(x) $ subject to $ h(x) = 0 $:

$ $\mathcal{L}(x, \lambda) = f(x) + \lambda^T h(x)

$$

### KKT Conditions

For inequality constraints:
1. Stationarity: $\nabla f + \sum \lambda_i \nabla g_i = 0 $ 2. Primal feasibility: $ g_i(x) \leq 0 $ 3. Dual feasibility: $\lambda_i \geq 0 $ 4. Complementary slackness: $\lambda_i g_i(x) = 0 $

## 💡 Solved Example: Least Squares

**Problem:** Solve $\min_x \|Ax - b\|^2 $ for overdetermined system.

**Solution:**

$ $\nabla_x \|Ax - b\|^2 = 2A^T(Ax - b) = 0

$$

$ $

A^T A x = A^T b $$

$ $\hat{x} = (A^T A)^{-1} A^T b

$$

This is the normal equation — foundation of [[Least Squares Adjustment]].

## 📐 Geodesy Application: Survey Network Optimization

**Problem:** Optimize survey network design subject to accuracy and cost constraints.

$ $\begin{aligned}
ext{minimize} \quad & ext{tr}(Q_{xx}) \quad ext{(maximize precision)} \\
ext{subject to} \quad & \sum c_i l_i \leq B \quad ext{(budget)} \\
& \sigma_{xx} \leq \sigma_{max} \quad ext{(accuracy)} \\
& l_i \geq 0 \quad ext{(non-negative baselines)}
\end{aligned}

$$

## 🎯 Practice Problems

1. Solve $\min x^2 + y^2 $ subject to $ x + y = 1 $.
2. Apply gradient descent to $ f(x,y) = x^2 + 4y^2 - 8x - 16y + 10 $.
3. Derive KKT conditions for $\min x^2 + y^2 $ s.t.$ x + 2y \geq 5$.
4. Solve a small LP using the simplex method.
5. Implement Newton's method for Rosenbrock function.

## 📖 References

- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge.
- Nocedal, J. & Wright, S.J. (2006). *Numerical Optimization*. Springer.
- Bazaraa, M.S. et al. (2013). *Nonlinear Programming*. Wiley.

---
*See also: [[Optimization Theory]], [[Numerical Methods]], [[Least Squares Adjustment]]*
