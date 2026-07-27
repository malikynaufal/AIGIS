---
tags: [math, numerical-methods, series-expansion, approximations, taylor-series]
aliases: [Taylor Series Expansion]
created: 2026-07-13
updated: 2026-07-27
---

# Taylor Series

> *"Represent any smooth function as an infinite polynomial."*

---

## 1. Definition

For a function $f(x) $ that is infinitely differentiable at $ x = a $:

$ $ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n $$

$ $= f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots

$$

### Maclaurin Series

Special case when $ a = 0 $:

$ $ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n $$

---

## 2. Remainder (Error) Terms

### 2.1 Lagrange Remainder

$ $ R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

where $\xi $ is between $ a $ and $ x $.

### 2.2 Peano Remainder

$ $ R_n(x) = o((x-a)^n) \quad \text{as } x \to a $$

### 2.3 Convergence Criterion

Taylor series converges to $ f(x) $ if $ R_n(x) \to 0 $ as $ n \to \infty $.

---

## 3. Important Taylor Series

| Function | Expansion | Valid When |
|----------|-----------|------------|
| $ e^x $ | $\sum \frac{x^n}{n!} $| All $ x $ |
| $\sin x $| $ x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots $| All $ x $ |
| $\cos x $|$ 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots $| All $ x $ |
| $\ln(1+x) $| $ x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots $|$-1 < x \leq 1 $ |
| $\frac{1}{1-x} $|$\sum x^n $|$|x| < 1 $ |
| $ (1+x)^\alpha $ | $\sum \binom{\alpha}{n} x^n $|$|x| \leq 1 $ |

### Visual Summary

```mermaid
graph LR
 A[f(x)] --> B[f(a)]
 A --> C[f'(a)(x-a)]
 A --> D[f''(a)(x-a)²/2!]
 A --> E[f'''(a)(x-a)³/3!]
 A --> F["∞ terms → exact"]
```

---

## 4. Convergence Visualization

For $\sin x $ approximation:

| Terms | $ n=0 $ | $ n=1 $ | $ n=3 $ | $ n=5 $ | $ n=7 $ | $ n=9 $ |
|-------|-------|-------|-------|-------|-------|-------|
| Error at $ x=\pi/4 $ | $ 1.000 $ | $ 0.215 $ | $ 0.004 $ | $ 5.0 \times 10^{-7} $ | $ 7.1 \times 10^{-12} $ | $\approx 0 $ |

Each pair of terms adds roughly 2 more correct decimal digits.

---

## 5. Practical Applications

### 5.1 Derivation of Numerical Methods

- **Finite differences** for derivatives
- **Newton's method** convergence proof
- **Integration** quadrature rules (Trapezoid, Simpson's)
- **ODE solvers** (Runge-Kutta)

### 5.2 Small Angle Approximation

For $\theta \ll 1 $ radians:$ $\sin\theta \approx \theta - \frac{\theta^3}{6} \approx \theta

$$

$ $\cos\theta \approx 1 - \frac{\theta^2}{2}

$$

Used in geodesy for small deformation calculations.

### 5.3 Geodesy: Ellipsoidal-to-Cartesian Approximation

Taylor expansion of coordinate transformation near a point gives linearized approximation used in Gauss-Markov models.

---

## 6. Taylor Series in Optimization

Second-order Taylor expansion of $ f(x) $ around $ x_0 $:

$ $ f(x) \approx f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2}(x-x_0)^2 $$

Minimizing: $ f'(x_0) + f''(x_0)(x-x_0) = 0 $ gives:$ $ x = x_0 - \frac{f'(x_0)}{f''(x_0)}$$

This is Newton's method for optimization.

---

## 7. Multivariate Taylor Expansion

For $ f(\mathbf{x}) $ where $\mathbf{x} \in \mathbb{R}^n $:

$ $ f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f^T \Delta\mathbf{x} + \frac{1}{2} \Delta\mathbf{x}^T H \Delta\mathbf{x}$$

where $ H $ is the Hessian matrix.

---

## 8. Common Errors in Taylor Approximations

| Error Type | Source | Mitigation |
|------------|--------|------------|
| Truncation | Finite terms | More terms |
| Roundoff | Finite precision | Higher precision |
| Divergence | $ x $ far from $ a$ | Use better center point |
| Non-convergence | Non-analytic function | Use alternative method |

---

## 9. Geodesy Connection

| Application | Taylor Use |
|-------------|------------|
| Deformation analysis | Linearized displacement model |
| Ellipsoid parameters | Series expansion of elliptic integrals |
| Map projection formulas | Perturbation expansions |
| Time system conversions | Polynomial approximations of rotation |

---

## 10. References

- Apostol, T. M. (1967). *Calculus*. Vol. 1 & 2. Wiley.
- Kline, M. (1972). *Mathematical Thought from Ancient to Modern Times*. Oxford.

See also: [[Limits and Continuity]], [[Derivatives]], [[Numerical Methods]], [[Error Propagation]]