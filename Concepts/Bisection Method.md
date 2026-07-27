---
tags: [aigis, concept, mathematics, numerical-methods, root-finding]
created: 2026-07-27
---

# Bisection Method

**Core Idea:** The bisection method is a root-finding algorithm that repeatedly bisects an interval and selects the subinterval where the function changes sign. Guaranteed to converge for continuous functions.

## Algorithm
1. Choose $[a,b]$ such that $f(a) \cdot f(b) < 0$
2. Compute midpoint $c = \frac{a+b}{2}$
3. If $f(c) = 0$ (or $|b-a| < \varepsilon$), stop
4. If $f(a) \cdot f(c) < 0$, set $b = c$; else set $a = c$
5. Repeat

## Convergence
- **Rate:** Linear ($O(n)$ iterations for $\varepsilon$ precision)
- **Required iterations:** $n \geq \log_2\left(\frac{b-a}{\varepsilon}\right)$

## In Geodesy
Used for solving Kepler's equation $M = E - e\sin E$ and coordinate conversions.

---
*Part of [[Numerical Methods]]*