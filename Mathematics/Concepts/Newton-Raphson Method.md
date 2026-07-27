---
tags: [aigis, concept, mathematics, numerical-methods, root-finding]
created: 2026-07-27
---

# Newton-Raphson Method

**Core Idea:** Newton-Raphson finds roots using iterative linearization. Quadratic convergence makes it the go-to method for smooth functions.
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

## Convergence

- **Rate:** Quadratic ($O(\log \log n)$iterations)

- **Condition:**$f'(x) \neq 0$near root; initial guess must be close

## In Geodesy

- **ECEF → Geodetic:** Bowring's method is a specialized Newton-Raphson

- **Nonlinear least squares:** Gauss-Newton extends this to systems

- **Kepler's equation:** Solve$M = E - e\sin E$for$E$

## Related

- [[Bisection Method]] (guaranteed but slower)

- [[Newton-Raphson Method]] (no derivative needed)

- [[Least Squares Adjustment]] (Gauss-Newton extension)

---
*Part of [[Numerical Methods]]*