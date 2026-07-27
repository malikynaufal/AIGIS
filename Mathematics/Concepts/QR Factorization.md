---
tags: [math, linear-algebra, numerical-methods, matrix-factorization]
aliases: [QR Decomposition, Gram-Schmidt QR]
created: 2026-07-13
updated: 2026-07-27
---

# QR Factorization

> *"Decompose a matrix into an orthogonal matrix and an upper triangular matrix — the gold standard for least squares."*

---

## 1. Definition

For any matrix $A \in \mathbb{R}^{m \times n} $ ($ m \geq n $):

$ $ A = Q \cdot R $$

where:
- $ Q \in \mathbb{R}^{m \times m} $ is **orthogonal**: $ Q^T Q = I $
- $ R \in \mathbb{R}^{m \times n} $ is **upper triangular**

For the **thin (reduced) QR**: $ Q \in \mathbb{R}^{m \times n} $ with orthonormal columns, $ R \in \mathbb{R}^{n \times n} $ upper triangular.

---

## 2. Three Algorithms

### 2.1 Classical Gram-Schmidt

```
For j = 1 to n:
 v_j = a_j
 For i = 1 to j-1:
 r_ij = q_i^T * a_j
 v_j = v_j - r_ij * q_i
 r_jj = ||v_j||
 q_j = v_j / r_jj
```

**Problem:** Numerically unstable for ill-conditioned columns (loss of orthogonality).

### 2.2 Modified Gram-Schmidt (MGS)

```
For j = 1 to n:
 v_j = a_j
 For i = 1 to j-1:
 r_ij = q_i^T * v_j ← uses updated v_j
 v_j = v_j - r_ij * q_i
 r_jj = ||v_j||
 q_j = v_j / r_jj
```

MGS is numerically stable and equivalent to Householder in exact arithmetic.

### 2.3 Householder Reflections (Preferred)

A Householder reflector:

$ $ H = I - 2uu^T, \quad \|u\| = 1 $$

reflects $ x $ to $\pm \|x\| e_1 $. Apply $ n $ reflectors to zero out subdiagonal entries:

$ $ H_n H_{n-1} \cdots H_1 A = R $$

$ $ Q = H_1 H_2 \cdots H_n = Q^T \quad (\text{since } H^T = H)$$

---

## 3. Worked Example (Householder)

Given $ A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 0 \end{pmatrix} $

**Step 1:** Reflect column 1:

$ $\|a_1\| = \sqrt{2}, \quad u = \frac{a_1 - \|a_1\|e_1}{\|a_1 - \|a_1\|e_1\|} = \frac{1}{\sqrt{2-\sqrt{2}}} \begin{pmatrix} 1-\sqrt{2} \\ 1 \\ 0 \end{pmatrix}

$$

Apply $ H_1 $ to get:$ $ R = \begin{pmatrix} -\sqrt{2} & 0 \\ 0 & \sqrt{2} \\ 0 & 0 \end{pmatrix}, \quad Q = \begin{pmatrix} -1/\sqrt{2} & 1/\sqrt{2} \\ -1/\sqrt{2} & -1/\sqrt{2} \\ 0 & 0 \end{pmatrix}$$

---

## 4. Applications

### Solving Least Squares: $ A\hat{x} \approx b $

$ $ A = QR \implies QR\hat{x} = b \implies R\hat{x} = Q^T b $$

Back-substitute the $ n \times n $ triangular system. Cost: $ O(2mn^2 - \frac{2n^3}{3}) $.

### Computing the QR Factorization of the Normal Equations

$ $ A^T A = R^T R \quad (\text{no formation of } A^T A \text{ needed})$$

This avoids the squaring of the condition number that plagues normal equations.

### Eigenvalue Algorithms

The **QR algorithm** iterates $ A_k = Q_k R_k $, $ A_{k+1} = R_k Q_k $ to converge to the Schur form.

---

## 5. Comparison with LU

| Property | LU | QR |
|----------|----|----|
| Square systems | ✓ Best | ✓ Overkill |
| Rectangular ($ m > n $) | ✗ | ✓ Best |
| Least squares | Indirect | Direct |
| Numerical stability | Needs pivoting | Always stable |
| SPD systems | Cholesky wins | Works but slower |

---

## 6. Complexity

| Algorithm | Flops |
|-----------|-------|
| Classical GS | $ 2mn^2 $ |
| Modified GS | $ 2mn^2 $ |
| Householder | $ 2mn^2 - \frac{2n^3}{3} $ |
| Givens rotations | $ 3mn^2 - n^3$ |

---

## 7. Geodesy Application

QR factorization is critical in:
- **Geodetic least squares adjustment** (numerically stable alternative to normal equations)
- **GNSS ambiguity resolution** (LAMBDA method uses QR preprocessing)
- **Kriging and covariance matrix factorization** in gravity field modeling

---

## 8. References

- Trefethen, L. N. & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.
- Björck, Å. (1996). *Numerical Methods for Least Squares Problems*. SIAM.

See also: [[LU Decomposition]], [[Cholesky Decomposition]], [[Least Squares Adjustment]], [[Linear Algebra Fundamentals]]
