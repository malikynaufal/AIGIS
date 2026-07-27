---
title: Semester 5 — Optimisasi (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, optimization, semester-5, aigis, geodesy-applied]
---

# Semester 5 — Optimisasi (Expanded)

**Course**: MGM211503 — Optimisasi  
**Credits**: 3 SKS  
**Prerequisites**: [[Kalkulus I Expanded]], [[Kalkulus II Expanded]], [[Aljabar Linear Lanjut Expanded]]

---

## Course Overview

This course introduces optimization theory and algorithms: unconstrained and constrained methods. Essential for parameter estimation, network design, and decision-making in geodesy and engineering.

---

## Syllabus

### Unit 1: Foundations

- **Optimization problem**: $\\min f(\\mathbf{x})$subject to$\\mathbf{g}(\\mathbf{x})=0$, $\\mathbf{h}(\\mathbf{x})\\leq 0$- **Local vs. global optima**

- **Convexity**: Local = global for convex functions

- **Level sets, gradient, Hessian**

### Unit 2: Unconstrained Optimization

- **Gradient descent**:$\\mathbf{x}_{k+1} = \\mathbf{x}_k - \\alpha_k\\nabla f$- **Newton's method**:$\\mathbf{x}_{k+1} = \\mathbf{x}_k - H^{-1}\\nabla f$- **Line search**: Exact and backtracking

- **Convergence rates**: Linear, superlinear, quadratic

### Unit 3: Constrained Optimization

- **Lagrange multipliers**:$\\nabla f + \\sum \\lambda_i\\nabla g_i = 0$- **KKT conditions**: Necessary and sufficient conditions

- **Convex optimization**: LP, QP, SOCP, SDP

- **Duality**: Weak and strong duality

### Unit 4: Linear Programming

- **Standard form**:$\\min c^Tx$s.t.$Ax=b$, $x\\geq 0$

- **Simplex method**: Moves along vertices

- **Duality theorem**: Strong duality holds for LP

- **Sensitivity analysis**: Shadow prices, ranges

### Unit 5: Numerical Optimization

- **BFGS quasi-Newton method**: Approximate Hessian updates

- **Levenberg-Marquardt**: For nonlinear least squares

- **Trust region methods**: Step size control

- **Stochastic gradient descent**: For large-scale problems

---

## Geodesy Applications

- **Least squares adjustment**: Quadratic optimization

- **Datum definition**: Constraint optimization for datum parameters

- **Network design**: Optimizing observation strategies

- **Outlier detection**: Robust estimation (M-estimators)

---

## References

- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*

- Nocedal, J. & Wright, S. (2006). *Numerical Optimization*

- Luenberger, D. & Ye, Y. (2008). *Linear and Nonlinear Programming*

---

➡️ [[Mathematics MOC]] | ➡️ [[Numerical Methods]]