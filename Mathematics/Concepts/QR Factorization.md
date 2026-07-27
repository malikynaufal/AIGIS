---
tags: [aigis, concept, mathematics, linear-algebra]
created: 2026-07-27
---

# QR Factorization
$$

A = QR$$where$Q$ = orthogonal ($Q^T Q = I$), $R$= upper triangular.

## Advantages

- **Highly stable** for least squares

- Avoids forming$A^T A$(reduces condition number)

- Used in eigenvalue algorithms (QR algorithm)

## In Geodesy
The least squares problem$Ax \approx b$can be solved via QR factorization:$$Rx = Q^T b$$This avoids squaring the condition number$\kappa(A^T A) = [\kappa(A)]^2$.

## Related

- [[LU Decomposition]]

- [[Cholesky Decomposition]]

- [[Least Squares Adjustment]]

---
*Part of [[Linear Algebra Fundamentals]] → [[Numerical Methods]]*