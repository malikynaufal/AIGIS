---
title: MGM211401 - Kalkulus Numerik
type: course
semester: 4
sks: 3
tags: [mathematics, numerical-methods, semester-4, geodesy-applied]
created: 2026-07-27
---

# MGM211401 - Kalkulus Numerik (Numerical Methods)

> *"In numerical analysis, we trade exactness for feasibility."* — Part of [[Mathematics MOC]]
> **SKS:** 3 | **Semester:** 4 | **Prerequisite:** [[Derivatives]], [[Integrals]], [[Linear Algebra Fundamentals]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Error Analysis | Round-off, truncation, propagation |
| 2 | Root Finding | Bisection, Newton-Raphson, secant |
| 3 | Interpolation | Lagrange, Newton, splines |
| 4 | Numerical Differentiation | Finite differences, Richardson extrapolation |
| 5 | Numerical Integration | Trapezoidal, Simpson, Gaussian quadrature |
| 6 | Linear Systems | Gaussian elimination, LU decomposition |
| 7 | Iterative Methods | Jacobi, Gauss-Seidel, SOR |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Eigenvalues | Power method, QR algorithm |
| 10 | Least Squares | Normal equations, orthogonal polynomials |
| 11 | Optimization | Gradient descent, Newton's method |
| 12 | ODE Solving | Euler, Runge-Kutta methods |
| 13 | PDE Solving | Finite difference methods |
| 14 | Monte Carlo | Random sampling methods |
| 15 | Final Review | Integration project |

## 📚 Core Theorems

### 1. Taylor's Theorem (with Remainder)

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x)$$

**Lagrange remainder:** $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$

### 2. Error Propagation

If $z = f(x, y)$ and $x, y$ have errors $\delta x, \delta y$:

$$\delta z \approx \left|\frac{\partial f}{\partial x}\right| \delta x + \left|\frac{\partial f}{\partial y}\right| \delta y$$

For independent errors:

$$\sigma_z^2 = \left(\frac{\partial f}{\partial x}\right)^2 \sigma_x^2 + \left(\frac{\partial f}{\partial y}\right)^2 \sigma_y^2$$

### 3. Convergence of Iterative Methods

An iterative method $x_{n+1} = g(x_n)$ converges to fixed point $p$ if:
1. $g(p) = p$ (fixed point)
2. $|g'(p)| < 1$ (local convergence)

**Rate of convergence:**
- **Linear:** $|e_{n+1}| \leq C|e_n|$, $C < 1$
- **Quadratic:** $|e_{n+1}| \leq C|e_n|^2$
- **Superlinear:** $\lim \frac{|e_{n+1}|}{|e_n|} = 0$

## 🔧 Root-Finding Methods

### Bisection Method
- **Interval:** $[a, b]$ with $f(a)f(b) < 0$
- **Guaranteed convergence** (continuous $f$)
- **Rate:** Linear, $\approx 0.693/n$ bits per iteration
- **Formula:** $c = \frac{a+b}{2}$

### Newton-Raphson Method

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

- **Rate:** Quadratic (if $f'(p) \neq 0$)
- **Requires:** $f$ differentiable, good initial guess
- **Failure modes:** $f'(x_n) = 0$, oscillation, divergence

### Secant Method

$$x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

- **Rate:** Superlinear ($\approx 1.618$, golden ratio)
- **Advantage:** No derivative needed

## 📈 Interpolation

### Lagrange Interpolation

$$P(x) = \sum_{i=0}^{n} f(x_i) \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$$

### Newton's Divided Differences

$$P(x) = f[x_0] + f[x_0,x_1](x-x_0) + \cdots + f[x_0,\dots,x_n] \prod_{i=0}^{n-1}(x-x_i)$$

### Cubic Splines
Piecewise cubic polynomials with continuous first and second derivatives.

## 🧮 Numerical Integration

### Trapezoidal Rule

$$\int_a^b f(x)\,dx \approx \frac{h}{2}[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)]$$

**Error:** $O(h^2)$, exact for polynomials of degree $\leq 1$.

### Simpson's Rule

$$\int_a^b f(x)\,dx \approx \frac{h}{3}[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + f_n]$$

**Error:** $O(h^4)$, exact for polynomials of degree $\leq 3$.

### Gaussian Quadrature

$$\int_{-1}^{1} f(x)\,dx \approx \sum_{i=1}^{n} w_i f(x_i)$$

where $x_i$ are roots of Legendre polynomial $P_n(x)$.

## 💡 Solved Example: Newton-Raphson

**Problem:** Find $\sqrt{2}$ using Newton-Raphson.

**Solution:**

$$f(x) = x^2 - 2, \quad f'(x) = 2x$$

$$x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{x_n + 2/x_n}{2}$$

Starting with $x_0 = 1$:
- $x_1 = 1.5$
- $x_2 = 1.4167$
- $x_3 = 1.4142$

Converges quadratically to $\sqrt{2} \approx 1.41421356...$

## 📐 Geodesy Application: GNSS Position

The pseudorange equation:

$$\rho_i = \|r_{sat,i} - r_{rx}\| + c \cdot dt + \varepsilon_i$$

Linearized via Taylor expansion:

$$\Delta\rho = H \cdot \Delta x$$

Solved using least squares (see [[Least Squares Adjustment]]).

## 🎯 Practice Problems

1. **Error Analysis:** If $x = 1.23 \pm 0.01$ and $y = 0.45 \pm 0.02$, find $z = x/y$ and its uncertainty.
2. **Root Finding:** Use Newton-Raphson to find the root of $f(x) = x^3 - 2x - 5$ near $x = 2$.
3. **Interpolation:** Given data points $(0,1), (1,2), (2,0)$, find the quadratic interpolant.
4. **Integration:** Compute $\int_0^1 e^{-x^2} dx$ using Simpson's rule with $n=4$.
5. **ODE:** Solve $y' = -2y + 1, y(0) = 0$ using RK4 with $h=0.1$ for 5 steps.

## 📖 References

- Burden, R.L. & Faires, J.D. (2010). *Numerical Analysis* (9th ed.). Brooks/Cole.
- Chapra, S.C. & Canale, R.P. (2014). *Numerical Methods for Engineers*. McGraw-Hill.
- Heath, M.T. (2018). *Scientific Computing*. McGraw-Hill.

---
*See also: [[Numerical Methods]], [[Bisection Method]], [[Newton-Raphson Method]], [[LU Decomposition]], [[QR Factorization]], [[Least Squares Adjustment]]*
