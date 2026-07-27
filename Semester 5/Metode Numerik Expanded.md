---
title: Semester 5 — Metode Numerik (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, numerical-methods, semester-5, aigis, geodesy-applied]
---

# Semester 5 — Metode Numerik (Expanded)

**Course**: MGM211501 — Metode Numerik  
**Credits**: 3 SKS  
**Prerequisites**: [[Kalkulus I Expanded]], [[Kalkulus II Expanded]], [[Persamaan Diferensial]]

---

## Course Overview

Numerical methods are computational techniques to solve mathematical problems that cannot be solved analytically. This course focuses on practical algorithms used in scientific computing, with applications in geodesy, engineering, and data analysis.

---

## Syllabus

### Unit 1: Root-Finding Methods

- **Bisection method**: Reliable but linear convergence
  Algorithm: Divide interval in half, evaluate sign at midpoint
  Convergence: Error halves each iteration

- **Newton-Raphson method**: Quadratic convergence near roots
  Formula: $x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}$
  Applications: Finding roots of nonlinear equations

- **Secant method**: Derivative-free improvement over Newton
  Formula: $x_{n+1} = x_n - f(x_n)\\cdot\\frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}$
  Convergence: Superlinear (~1.618)

### Unit 2: Interpolation

- **Linear interpolation**: $f(x) \\approx \\frac{y_2-y_1}{x_2-x_1}(x-x_1) + y_1$ for $(x_1,y_1)$, $(x_2,y_2)$

- **Polynomial interpolation**: Lagrange form, Newton form
  Given $(x_i, y_i)$, $i=0..n$: $P_n(x) = \\sum_{i=0}^n y_i \\prod_{j\\neq i} \\frac{x-x_j}{x_i-x_j}$

- **Spline interpolation**: Piecewise polynomials with $C^1$ or $C^2$ continuity
  Cubic splines: Minimize bending energy

### Unit 3: Least Squares Approximation

- **Linear least squares**: $\\min_x \\sum (y_i - x^T z_i)^2$
  Solution: Normal equations $Z^T Z x = Z^T y$

- **Nonlinear least squares**: $\\min_x \\sum r_i(x)^2$
  Gauss-Newton: $x_{k+1} = x_k + (J^T J)^{-1} J^T r$
  Levenberg-Marquardt: $(J^T J + \\lambda I)\\delta x = -J^T r$

### Unit 4: Numerical Integration

- **Newton-Cotes formulas**: Trapezoidal rule, Simpson's rule
  Composite: Divide interval into subintervals

- **Gaussian quadrature**: Optimal weights and nodes
  Gauss-Legendre: $\\int_{-1}^1 f(x) dx \\approx \\sum_{i=1}^n w_i f(x_i)$

- **Adaptive integration**: Error-controlled subdivision
  Refine where error exceeds tolerance

### Unit 5: Numerical ODE Solvers

- **Initial value problems**: $y'(t) = f(t,y)$, $y(t_0) = y_0$

- **Explicit methods**:
  Euler: $y_{n+1} = y_n + hf(t_n,y_n)$
  Runge-Kutta (RK4): Weighted average of slopes

- **Implicit methods** (A-stable):
  Backward Euler: $y_{n+1} = y_n + hf(t_{n+1},y_{n+1})$
  Solve nonlinear system using Newton-Raphson

### Unit 6: Eigenvalue Problems

- **Power iteration**: Find dominant eigenvalue/vector
  $x_{k+1} = Ax_k / \\|Ax_k\\|$

- **Inverse iteration**: Find eigenvalue near shift $\\sigma$
  Solve $(A-\\sigma I)x = b$

- **QR algorithm**: Iterative QR factorization
  $A_k = Q_k R_k$, $A_{k+1} = R_k Q_k$

### Unit 7: Partial Differential Equations

- **Finite difference method**: Discretize derivatives
  Poisson's equation: $-u_{xx} - u_{yy} = f$
  Discretization: $\\frac{u_{i+1,j}-2u_{i,j}+u_{i-1,j}}{h^2} + \\frac{u_{i,j+1}-2u_{i,j}+u_{i,j-1}}{h^2} = -f_{ij}$

- **Method of lines**: Spatially discretize, then solve ODE system

---

## Geodesy Applications

- **Geodetic network adjustment**: Least squares optimization
- **Coordinate transformations**: Numerical solutions to nonlinear equations
- **Gravity field modeling**: Numerical integration of spherical harmonics
- **Least squares curves/surfaces**: Fitting geodetic networks
- **Trajectory computation**: Integration of kinematic equations

---

## References

- Burden, R.L. & Faires, J.D. (2020). *Numerical Analysis* (10th ed.)
- Press, W.H. & Teukolsky, S.A. (2007). *Numerical Recipes* (Chapters 7-9)

---

➡️ [[Mathematics MOC]] | ➡️ [[Numerical Methods]]