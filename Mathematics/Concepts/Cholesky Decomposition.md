---
tags: [math, linear-algebra, numerical-methods, matrix-factorization, spd]
aliases: [Cholesky Factorization]
created: 2026-07-13
updated: 2026-07-27
---

# Cholesky Decomposition

> *"The elegant square-root factorization for symmetric positive definite matrices — twice as fast as LU."*

---

## 1. Definition

For a **symmetric positive definite (SPD)** matrix $A \in \mathbb{R}^{n \times n} $:

$ $  A = LL^T $$

where $ L $ is lower triangular with **positive** diagonal entries ( $ l_{ii} > 0 $).

### Equivalent Forms

| Form | Expression | Notes |
|------|------------|-------|
| Lower Cholesky | $ A = LL^T $ | Standard |
| Upper Cholesky | $ A = R^T R $ | $  R = L^T $ |
| LDLᵀ | $ A = LDL^T $ | $  D $ diagonal, $  L $ unit lower triangular |

---

## 2. Algorithm (Cholesky-Banachiewicz)

```
For j = 1 to n:
 l_jj = sqrt(a_jj - sum_{k=1}^{j-1} l_jk^2)
 For i = j+1 to n:
 l_ij = (a_ij - sum_{k=1}^{j-1} l_ik * l_jk) / l_jj
```

### Example

$ $  A = \begin{pmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{pmatrix}$$

$ l_{11} = \sqrt{4} = 2 $

$ l_{21} = 12/2 = 6 $, $ l_{31} = -16/2 = -8 $

$ l_{22} = \sqrt{37 - 6^2} = \sqrt{1} = 1 $

$ l_{32} = (-43 - (-8)(6))/1 = -43 + 48 = 5 $

$ l_{33} = \sqrt{98 - (-8)^2 - 5^2} = \sqrt{98 - 64 - 25} = \sqrt{9} = 3 $

$ $  L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{pmatrix}$$

Verification: $ LL^T = A $ ✓

---

## 3. Properties

| Property | Value |
|----------|-------|
| Cost | $\frac{1}{3}n^3 $ flops (vs $\frac{2}{3}n^3 $ for LU) |
| Storage | $\frac{n(n+1)}{2} $ elements (half matrix) |
| Stability | Unconditionally stable for SPD matrices |
| Uniqueness | Unique if diagonal entries $> 0 $ |

---

## 4. Testing for Positive Definiteness

Cholesky **fails** if $ A $ is not SPD:

- If $ a_{jj} - \sum l_{jk}^2 \leq 0 $ at any step → $\sqrt{\text{negative}} $ → **not SPD**
- This provides a practical test for positive definiteness

---

## 5. Applications

### Solving $ Ax = b $

1. Forward substitution: $ Ly = b $
2. Back substitution: $ L^T x = y $

### Computing Determinant

$ $\det(A) = \det(L)\det(L^T) = \left(\prod_{i=1}^n l_{ii}\right)^2

$$

# ## Monte Carlo / Sampling

To sample $ x \sim \mathcal{N}(0, A) $:
1. Compute $ A = LL^T $
2. Sample $ z \sim \mathcal{N}(0, I) $
3. $ x = Lz $ has covariance $ LL^T = A $

---

## 6. Banded / Sparse Cholesky

For sparse SPD matrices (e.g., geodetic normal equations):
- **Fill-in** occurs during factorization
- **Ordering** (AMD, Cuthill-McKee) minimizes fill-in
- **Symbolic factorization** before numeric factorization

---

## 7. Geodesy Connection

The **normal matrix $ N $** in least squares adjustment is SPD:

$ $  N = A^T P A $$

Cholesky factorization $ N = LL^T $ is the standard way to solve the normal equations: $ $ N\hat{x} = w \implies LL^T \hat{x} = w $$

1.$ Ly = w $ (forward)
2. $ L^T \hat{x} = y $ (backward)

This is the **workhorse** of geodetic computation.

---

## 8. Comparison Table

| Method | Flops | Storage | Stability | Use Case |
|--------|-------|---------|-----------|----------|
| Cholesky | $ n^3/3 $ | $ n^2/2 $ | Perfect for SPD | SPD systems, least squares normal eq |
| LU | $ 2n^3/3 $ | $ n^2 $ | Needs pivoting | General square |
| QR | $ 2mn^2 $ | $ mn $ | Always stable | Least squares, rectangular |
| SVD | $ 2mn^2 + 2n^3 $ | $ mn$ | Ultimate stability | Rank-deficient, ill-posed |

---

## 9. References

- Golub, G. H. & Van Loan, C. F. (2013). *Matrix Computations*. 4th ed. Johns Hopkins.
- Strang, G. (2006). *Linear Algebra and Its Applications*. Thomson.

See also: [[LU Decomposition]], [[QR Factorization]], [[Least Squares Adjustment]], [[Linear Algebra Fundamentals]]