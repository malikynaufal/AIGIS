---
tags: [aigis, concept, mathematics, numerical-methods, iterative, algorithms, GNSS]
created: 2026-07-27
updated: 2026-07-27
---

# Numerical Methods

## For Geodesy & Computational Science

**Core Idea:** Numerical methods approximate mathematical operations (integration, differentiation, root-finding) using discrete computations. In geodesy, everything is numerical — from GNSS orbit integration to least-squares adjustment, from coordinate transformations to geoid modeling.

---

## Fundamental Concepts

### Sources of Numerical Error

| Error Type | Source | Example |
|-----------|--------|---------|
| **Round-off** | Finite precision of floating-point | $1/3 = 0.333...$ truncated |
| **Truncation** | Approximating infinite series | Taylor series $\sum_{n=0}^{N-1} \to \sum_{n=0}^\infty$ |
| **Discretization** | Approximating continuous with discrete | Finite differences instead of derivatives |
| **Cancellation** | Subtracting nearly equal numbers | $\sqrt{1+\varepsilon} - 1$ for small $\varepsilon$ |

**Double precision:** 15–16 significant decimal digits; condition number determines loss of digits.

### Root-Finding

| Method | Formula | Convergence | Use |
|--------|---------|-------------|-----|
| **Bisection** | $x_{n+1} = (a+b)/2$ | Linear | Guaranteed convergence |
| **Newton-Raphson** | $x_{n+1} = x_n - f(x_n)/f'(x_n)$ | Quadratic | Fast, needs derivative |
| **Secant** | $x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}$ | Superlinear | No derivative needed |
| **Regula Falsi** | Like secant but bounded | Linear | Guaranteed |

### Interpolation

| Method | Formula | Degree | Use |
|--------|---------|--------|-----|
| **Lagrange** | $P(x) = \sum_{i=0}^n y_i \prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ | ≤ $n$ | Exact fit to $n+1$ points |
| **Newton** | $P(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \cdots$ | ≤ $n$ | Easy to add points |
| **Spline** | Piecewise cubic, $C^2$ continuous | Local | Smooth interpolation |

### Numerical Integration (Quadrature)

| Method | Formula | Error | Order |
|--------|---------|-------|-------|
| **Trapezoidal** | $\int_a^b f \approx \frac{h}{2}[f_0 + 2f_1 + \cdots + f_n]$ | $O(h^2)$ | 2 |
| **Simpson's 1/3** | $\int_a^b f \approx \frac{h}{3}[f_0 + 4f_1 + 2f_2 + \cdots + f_n]$ | $O(h^4)$ | 4 |
| **Gauss quadrature** | $\int_{-1}^{1} f \approx \sum_{i=1}^n w_i f(x_i)$ | $O(h^{2n})$ | Variable |
| **Adaptive** | Refine intervals where $f$ varies rapidly | Error-controlled | Application |

### Numerical Differentiation

**Forward difference:**
$$f'(x) \approx \frac{f(x+h) - f(x)}{h} \quad \text{error } O(h)$$

**Central difference (better):**
$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} \quad \text{error } O(h^2)$$

**Second derivative:**
$$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} \quad \text{error } O(h^2)$$

---

## In Geodesy Context

### Satellite Orbit Integration

The equations of motion:
$$\ddot{\mathbf{r}} = -\frac{GM}{r^3}\mathbf{r} + \mathbf{a}_{\text{perturbations}}$$

**Numerical integration methods:**
- **Runge-Kutta 4 (RK4):** Standard 4th-order method, good accuracy
- **Adams-Bashforth/Moulton:** Multi-step, more efficient for smooth orbits
- **Cowell's method:** Direct numerical integration of position and velocity

**Step size:** Typically ~60–300 seconds for precise orbit determination.

### Newton-Raphson in GNSS

The Gauss-Newton iteration for nonlinear least-squares:

$$\mathbf{x}_{k+1} = \mathbf{x}_k - (J^T P J)^{-1} J^T P \mathbf{r}_k$$

This is a multidimensional Newton-Raphson with special structure exploiting the least-squares form.

### Coordinate Conversion

**ECEF → Geodetic:** Requires solving a nonlinear equation (Bowring's method = Newton-Raphson). Converges in 2–3 iterations for most points, but near the poles may need more.

**Inverse projections:** Newton-Raphson for complex projections (LCC, stereographic).

### Geoid Computation (Remove-Compute-Restore)

The Stokes integral is discretized numerically:
$$N_p = \frac{R}{4\pi\gamma} \sum_{i=1}^{n} \Delta g_i \cdot S(\psi_i) \cdot \Delta\sigma_i$$

This is essentially a Gauss quadrature on the sphere.

### Error Analysis

**Condition number:** $\kappa(A) = \frac{\sigma_{max}}{\sigma_{min}}$ of the normal matrix $A = H^T P H$.

| $\kappa$ | Interpretation |
|-----------|---------------|
| $\kappa < 10^3$ | Well-conditioned |
| $10^3 < \kappa < 10^8$ | Moderately ill-conditioned |
| $\kappa > 10^8$ | Ill-conditioned (solution unreliable) |

**GNSS condition number** is typically $10^3$–$10^5$ depending on geometry.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $x_{n+1} = x_n - f(x_n)/f'(x_n)$ | Newton-Raphson | Root-finding |
| $f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$ | Central difference | Derivative |
| $\int \approx \frac{h}{3}[f_0+4f_1+2f_2+...] $ | Simpson's rule | Quadrature |
| $\kappa(A) = \sigma_{max}/\sigma_{min}$ | Condition number | Numerical stability |

---

## Related Concepts

- [[Least Squares Adjustment]] — Core numerical problem
- [[Integrals]] — Analytic basis for quadrature
- [[Derivatives]] — Analytic basis for differentiation
- [[Linear Algebra Fundamentals]] — Solving linear systems
- [[GNSS]] — Practical numerical processing

---

## Study Problems

1. **Recall:** Use Newton-Raphson to find $\sqrt{2}$ (root of $x^2 - 2 = 0$), starting from $x_0 = 1.5$.
2. **Application:** Compute $\int_0^1 e^{-x^2}dx$ numerically using Simpson's rule with $n = 4$ intervals.
3. **Derivation:** Derive the central difference formula for $f'(x)$ from Taylor expansions of $f(x+h)$ and $f(x-h)$.
4. **Real-world:** In GNSS processing, the normal matrix is often nearly singular. Suggest two strategies to handle ill-conditioning.

---

## Common Mistakes

1. **Using too small a step size in numerical differentiation:** Round-off dominates, result is worse.
2. **Applying Newton-Raphson with a poor initial guess:** May diverge or converge to wrong root.
3. **Ignoring condition number:** A high condition number means the solution is unreliable.
4. **Using Simpson's rule for an odd number of intervals:** Must be even (even number of sub-intervals).
5. **Confusing absolute and relative error:** Relative error matters more when the answer is large.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*