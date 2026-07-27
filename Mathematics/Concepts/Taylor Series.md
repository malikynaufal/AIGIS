---
tags: [aigis, concept, mathematics, taylor-series, series]
created: 2026-07-27
---

# Taylor Series

## Overview
The Taylor series expresses a function as an infinite sum of terms calculated from its derivatives at a single point:
$$

f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$$**Maclaurin series:**$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n$## Convergence Radius
If$f$is entire (analytic everywhere), radius =$\infty$. Otherwise, use ratio/root tests to find interval of convergence.

## In Geodesy

- **Linearization:** $\rho(x) \approx \rho(x_0) + \nabla\rho|_{x_0} \cdot (x-x_0) + \frac{1}{2}(x-x_0)^T H \nabla\rho|_{x_0} (x-x_0) + \cdots$

- **Bessel's inequality:** Bessel functions for ellipsoid coordinates

## Related

- [[Sequences and Series]]

- [[Numerical Methods]]

---
*Part of [[Numerical Methods]]*