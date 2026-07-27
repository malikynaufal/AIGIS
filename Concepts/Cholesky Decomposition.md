---
tags: [aigis, concept, mathematics, linear-algebra, factorization]
created: 2026-07-27
---

# Cholesky Decomposition

$$A = G G^T$$

where $G$ = lower triangular, $A$ = symmetric positive definite.

## Advantages
- **2× faster** than LU for symmetric PD matrices
- **Numerically stable** — no pivoting needed
- **Memory efficient** — stores only one triangular matrix

## In Geodesy
The normal matrix $N = H^T P H$ is always symmetric positive definite. Cholesky decomposition is the standard method for solving:

$$N\hat{x} = b \quad \rightarrow \quad \hat{x} = G^{-T}G^{-1}b$$

## Related
- [[LU Decomposition]] (general matrices)
- [[Least Squares Adjustment]] (normal equations)

---
*Part of [[Numerical Methods]]*