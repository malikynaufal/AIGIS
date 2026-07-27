---
tags: [aigis, concept, mathematics, linear-algebra, factorization]
created: 2026-07-27
---

# LU Decomposition
$$

A = LU$$where$L$= lower triangular,$U$= upper triangular.

## Use
Solve$Ax = b$:
1. Forward substitution: $Ly = b$2. Backward substitution:$Ux = y$## In Geodesy
Solving normal equations$(H^T P H)\hat{x} = H^T P y$efficiently. For large networks, LU is faster than computing the full inverse.

## Related

- [[Cholesky Decomposition]] (for symmetric positive definite$A$)

- [[QR Factorization]] (more stable for ill-conditioned systems)

---
*Part of [[Linear Algebra Fundamentals]] → [[Numerical Methods]]*