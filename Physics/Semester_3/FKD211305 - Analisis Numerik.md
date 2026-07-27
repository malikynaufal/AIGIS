---
code: FKD211305
name: Analisis Numerik
SKS: 3
semester: 3
department: Matematika/Fisika
tags: [numerical-analysis, algorithms, computation, physics-methods]
created: 2026-07-27
---

# FKD211305 — Analisis Numerik

## Course Overview

Numerical analysis provides the mathematical framework for solving problems that cannot be solved analytically — which describes most real-world physics problems. This course covers the theory and implementation of algorithms for root finding, interpolation, numerical differentiation/integration, ODE solving, and linear algebra, with emphasis on error analysis and convergence.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour lab per week)
**Prerequisites:** Kalkulus II, Persamaan Diferensial, Pemrograman Lanjutan
**Co-requisites:** Fisika Klasik

---

## 📋 Topics & Outline

### Unit 1: Foundations and Error Analysis (Weeks 1–3)

- **Sources of error:** truncation error, round-off error, catastrophic cancellation

- **Floating-point representation** and machine epsilon

- **Condition number** — sensitivity of a problem to input perturbations

- **Stability** — does error amplify through algorithm steps?

- IEEE 754 double precision: ~16 significant decimal digits

### Unit 2: Root Finding (Weeks 4–7)

- **Bisection method:** guaranteed convergence, but linear
 - Error bound: |b_n - a_n| = 2^{-n}(b-a)

- **Newton-Raphson method:**
 - x_{n+1} = x_n - f(x_n)/f'(x_n)
 - Quadratic convergence near simple roots
 - Pitfalls: zero derivative, cycling, divergence

- **Secant method:** derivative-free, superlinear convergence (order ~1.618)

- **Fixed-point iteration:** x = g(x), convergence condition |g'| < 1

- **Comparison of methods** and when to use each

### Unit 3: Numerical Interpolation and Integration (Weeks 8–12)

- **Polynomial interpolation:**
 - Lagrange interpolation formula
 - Newton's divided differences
 - Runge's phenomenon — equidistant nodes can diverge!
 - **Chebyshev nodes** for stable interpolation

- **Splines:** cubic splines for smooth interpolation

- **Numerical differentiation:**
 - Forward difference: f'(x) = (f(x+h)-f(x))/h + O(h)
 - Central difference: f'(x) = (f(x+h)-f(x-h))/(2h) + O(h²)

- **Numerical integration (quadrature):**
 - Trapezoidal rule: ∫f dx ≈ (h/2)[f₀ + 2f₁ + ... + f_N]
 - **Simpson's 1/3 rule:** ∫f dx ≈ (h/3)[f₀ + 4f₁ + 2f₂ + 4f₃ + ... + f_N]
 - **Gaussian quadrature:** optimal node placement for polynomials up to degree 2N-1

### Unit 4: ODE Solving and Matrix Methods (Weeks 13–16)

- **ODE initial value problems:**
 - Euler method (first-order)
 - **Runge-Kutta methods** (2nd and 4th order)
 - **Multistep methods:** Adams-Bashforth, Adams-Moulton
 - **Stiff equations** and implicit methods (brief treatment)

- **Boundary value problems:** shooting method, finite differences

- **Numerical linear algebra:**
 - LU decomposition for solving Ax = b
 - **Iterative methods:** Jacobi, Gauss-Seidel for large sparse systems
 - Eigenvalue algorithms: power method, QR algorithm (overview)

- **Applications:** solving the Schrödinger equation numerically, N-body problem

---

## 🔬 Key Algorithms

```
Bisection: e_{n+1} = (1/2)e_n (linear convergence)
Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n) (quadratic)
Trapezoidal: Error = O(h²) (global)
Simpson's: Error = O(h⁴) (global)
RK4: Local error = O(h⁵), global error = O(h⁴)
Gaussian Quad: Exact for polynomials up to degree 2N-1
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Analyze sources of numerical error and their impact on computed results
2. Implement and compare root-finding algorithms (bisection, Newton, secant)
3. Apply interpolation and quadrature methods with error estimates
4. Solve ODEs numerically using Euler and Runge-Kutta methods
5. Perform numerical linear algebra operations (LU, eigenvalues)
6. Select appropriate numerical methods for specific physics problems

---

## 📚 References

1. Burden, R.L. & Faires, J.D. (2011). *Numerical Analysis*, 9th ed. Cengage.
2. Press, W.H. et al. (2007). *Numerical Recipes*, 3rd ed. Cambridge.
3. Heath, M.T. (2018). *Scientific Computing*, 3rd ed. McGraw-Hill.
4. Quarteroni, A. & Saleri, F. (2006). *Scientific Computing with MATLAB and Octave*, 2nd ed. Springer.
5. Trefethen, L.N. (2011). *Numerical Linear Algebra*. SIAM.
