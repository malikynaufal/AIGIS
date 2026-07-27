---
tags: [math, linear-algebra, numerical-methods, matrix-factorization]
aliases: [LU Factorization, LU Decomposition]
created: 2026-07-13
updated: 2026-07-27
---

# LU Decomposition

> *"Factorize a matrix into lower and upper triangular components for efficient computation."*

---

## 1. Definition

Given a square matrix $A \in \mathbb{R}^{n \times n} $, the **LU Decomposition** factors $  A $ into:

$ $  A = L \cdot U $$

where:
- $ L $ is a **lower triangular** matrix with ones on the diagonal ( $ l_{ii} = 1 $)
- $ U $ is an **upper triangular** matrix

This is essentially Gaussian elimination captured in matrix form.

---

## 2. Existence & Uniqueness

| Condition | Result |
|-----------|--------|
| $ A $ is nonsingular | LU decomposition exists |
| All leading minors $\det(A_k) \neq 0 $ | LU exists and is unique |
| $ A $ is symmetric positive definite | **Cholesky** factorization exists: $  A = LL^T $ |
| $ A $ requires row pivoting | **PLU** decomposition: $ PA = LU $ where $  P $ is a permutation matrix |

---

## 3. The Algorithm (Doolittle)

```
For k = 1 to n:
 For i = k+1 to n:
 l_ik = a_ik / a_kk
 For j = k to n:
 a_ij = a_ij - l_ik * a_kj
```

### Step-by-step Example

Given:

$ $  A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$ $**Step 1:** Eliminate below $ a_{11} $:

$ $ L_1 = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 0 & 1 \end{pmatrix}, \quad U_1 = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{pmatrix}$ $**Step 2:** Eliminate below $ a_{22} $:

$ $  L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ $**Verification:**$  L \cdot U = A $ ✓

---

## 4. Applications

### Solving Linear Systems $ Ax = b $

Instead of inverting $ A $, solve two triangular systems:

1. **Forward substitution:** $ Ly = b $ — solve for $  y $
2. **Back substitution:** $ Ux = y $ — solve for $  x $

Cost: $ O(n^2) $ instead of $ O(n^3) $ per additional right-hand side.

### Computing the Determinant

$ $\det(A) = \det(L) \cdot \det(U) = 1 \cdot \prod_{i=1}^{n} u_{ii}

$$

# ## Computing the Inverse

Solve $ AX = I $ column by column using LU.

---

## 5. Pivoting — PLU Decomposition

If $ a_{kk} = 0 $ during elimination, we must swap rows. This yields:

$ $ PA = LU $$

where $ P $ is a **permutation matrix** recording row swaps.

### Algorithm (Partial Pivoting)

At each step $ k $:
1. Find $ i \geq k $ such that $|a_{ik}| = \max_{j \geq k} |a_{jk}|$ 2. Swap rows $  k $ and $  i $
3. Proceed with standard LU elimination

---

## 6. Complexity

| Operation | Cost |
|-----------|------|
| LU Factorization | $ O\left(\frac{2n^3}{3}\right) $ |
| Forward Substitution | $ O(n^2) $ |
| Back Substitution | $ O(n^2) $ |
| Total for $ Ax = b $ | $ O\left(\frac{2n^3}{3} + 2n^2\right) $ |

---

## 7. Numerical Stability

- **Without pivoting:** Unstable if small pivots arise
- **Partial pivoting:** Sufficient for most practical problems; growth factor bounded by $ 2^{n-1} $
- **Complete pivoting:** Selects largest element in remaining submatrix; rarely needed

### Error Bound

$ $\frac{\|\delta x\|}{\|x\|} \leq \kappa(A) \cdot \left(\epsilon_{\text{machine}} + O\left(\frac{\rho}{\text{min}|u_{ii}|}\right)\right)

$$

where $\rho $ is the growth factor and $\kappa(A) $ is the condition number.

---

## 8. Connection to Other Decompositions

| Decomposition | Form | Use Case |
|---------------|------|----------|
| LU | $ A = LU $ | General square systems |
| PLU | $ PA = LU $ | General + stability |
| Cholesky | $ A = LL^T $ | SPD matrices (2× faster) |
| QR | $ A = QR $ | Overdetermined / least squares |
| LDU | $ A = LDU^T $ | Symmetric indefinite |

---

## 9. Geodesy Application

In **least squares adjustment**, the normal equations $ N\hat{x} = w $ are solved using Cholesky (a special LU for SPD matrices):

$ $  N = LL^T, \quad L y = w, \quad L^T \hat{x} = y $$

This is the computational backbone of [[Least Squares Adjustment]].

---

## 10. References

- Strang, G. (2006). *Linear Algebra and Its Applications*. Thomson.
- Golub, G. H. & Van Loan, C. F. (2013). *Matrix Computations*. Johns Hopkins.
- Trefethen, L. N. & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.

See also: [[QR Factorization]], [[Cholesky Decomposition]], [[Linear Algebra Fundamentals]], [[Least Squares Adjustment]]
