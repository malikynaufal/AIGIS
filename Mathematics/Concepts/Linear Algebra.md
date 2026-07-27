---
title: 7. Linear Algebra (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, linear-algebra, eigenvalues, matrices, aigis, geodesy-applied]
---

# 7. Linear Algebra (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Linear algebra studies vectors, matrices, and linear transformations. It is the mathematical language of least squares adjustment, coordinate transformations, and data analysis.

## 1. Vector Spaces

### 1.1 Definition

A vector space $V $over field $F $satisfies:
1. Closure under addition:$\mathbf{u} + \mathbf{v} \in V$2. Closure under scalar multiplication:$c\mathbf{u} \in V$3. Associativity, commutativity of addition
4. Existence of zero vector and inverses
5. Distributive laws, compatibility

### 1.2 Subspace $W \subseteq V $is a subspace if it contains $\mathbf{0} $and is closed under addition and scalar multiplication.

### 1.3 Basis and Dimension

- **Linearly independent**:$c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \implies c_1 = \cdots = c_n = 0$- **Span**: All linear combinations of $\{\mathbf{v}_1, \ldots, \mathbf{v}_n\} $- **Basis**: Linearly independent spanning set

- **Dimension**: Number of vectors in a basis

## 2. Matrices

### 2.1 Matrix Operations

| Operation | Definition |
|-----------|-----------|
| Addition | $(A+B)_{ij} = a_{ij} + b_{ij} $ |
| Scalar multiplication | $(cA)_{ij} = ca_{ij} $ |
| Matrix product | $(AB)_{ij} = \sum_k a_{ik}b_{kj} $ |
| Transpose | $(A^T)_{ij} = a_{ji} $ |
| Inverse | $AA^{-1} = I$ |

### 2.2 Matrix Properties

-$AB \neq BA $in general
-$(AB)^T = B^TA^T$-$(AB)^{-1} = B^{-1}A^{-1} $-$\det(AB) = \det(A)\det(B)$## 3. Determinants

### 3.1 Definition (2×2
)

$$\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

### 3.2 Cofactor Expansio
n

$$\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij}M_{ij} $$where $M_{ij} $is the$(n-1)\times(n-1) $minor.

### 3.3 Properties

-$\det(A^T) = \det(A)$-$\det(cA) = c^n\det(A)$-$A $invertible $\iff \det(A) \neq 0$### 3.4 Geometric Interpretation$|\det(A)| $= factor by which $A $scales $n$-dimensional volume.

## 4. Eigenvalues and Eigenvectors

### 4.1 Definition

For square matrix $A$, if $A\mathbf{v} = \lambda\mathbf{v} $for $\mathbf{v} \neq \mathbf{0} $:

- $\lambda$= eigenvalue
-$\mathbf{v} $= eigenvector

### 4.2 Finding Eigenvalues

Solve **characteristic equation**:$\det(A - \lambda I) = 0$### 4.3 Finding Eigenvectors

For each $\lambda$, solve $(A - \lambda I)\mathbf{v} = \mathbf{0} $### 4.4 Properties

-$\text{tr}(A) = \sum \lambda_i$(trace = sum of eigenvalues)
-$\det(A) = \prod \lambda_i$- Distinct eigenvalues → independent eigenvectors
-$A $diagonalizable $\iff $algebraic multiplicity = geometric multiplicity for all $\lambda$### 4.5 Spectral Decomposition

If $A $is symmetric with eigenvalues $\lambda_i $and orthonormal eigenvectors $\mathbf{q}_i$:

$$A = Q\Lambda Q^T = \sum_{i=1}^n \lambda_i \mathbf{q}_i\mathbf{q}_i^T$$## 5. Matrix Decompositions

### 5.1 LU Decompositio
n

$$A = LU$$where $L$is lower triangular,$U $is upper triangular.

**Use**: Solving $A\mathbf{x} = \mathbf{b} $efficiently.

**Algorithm**: Gaussian elimination stores row operations in $L$.

### 5.2 QR Decomposition

$$A = QR$$where $Q $is orthogonal ($Q^TQ = I$),$R $is upper triangular.

**Construction**: Gram-Schmidt process or Householder reflections.

**Use**: Least squares problems, solving overdetermined systems.

### 5.3 Singular Value Decomposition (SVD
)

$$A = U\Sigma V^T$$

where:
-$U$: $m \times m $orthogonal matrix (left singular vectors)
-$\Sigma$: $m \times n $diagonal (singular values $\sigma_1 \geq \sigma_2 \geq \cdots$)

- $V$: $n \times n $orthogonal matrix (right singular vectors)

**Properties**:
-$\sigma_i = \sqrt{\lambda_i(A^TA)} $-$A^TA = V\Sigma^TU^TV\Sigma V^T = V(\Sigma^T\Sigma)V^T$- Rank = number of nonzero singular values

- Condition number $\kappa = \sigma_{\max}/\sigma_{\min} $**Applications**: Pseudoinverse, data compression, noise filtering

### 5.4 Cholesky Decomposition

For symmetric positive definite $A$:

$$A = LL^T$$where $L $is lower triangular.

## 6. Least Squares and Pseudoinverse

### 6.1 Normal Equations

For overdetermined system $A\mathbf{x} \approx \mathbf{b} $:

$$A^TA\hat{\mathbf{x}} = A^T\mathbf{b
}

$$### 6.2 Moore-Penrose Pseudoinverse$$

A^+ = V\Sigma^+U^T$$where $\Sigma^+$has reciprocals of nonzero singular values
.

$$\hat{\mathbf{x}} = A^+\mathbf{b} $$

## 7. Practice Problems

### Problem 1
Find eigenvalues of $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} $**Solution**:

$$\det(A-\lambda I) = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3) = 0$$

$\lambda_1 = 1$, $\lambda_2 = 3 $Eigenvectors:$\mathbf{v}_1 = (-1,1)^T$, $\mathbf{v}_2 = (1,1)^T$### Problem 2
Compute LU decomposition of $A = \begin{bmatrix} 2 & 1 \\ 6 & 4 \end{bmatrix} $**Solution**:$R_2 \to R_2 - 3R_1$: $U = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix} $, $L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix} $Check:$LU = \begin{bmatrix} 2 & 1 \\ 6 & 4 \end{bmatrix} $✓

### Problem 3
Find the SVD of $A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} $**Solution**: Already diagonal, so $U = I$, $\Sigma = A$, $V = I$

$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} $## 8. Where Geodesy Uses This

- **Least squares adjustment**: Normal equations $A^TPA\hat{x} = A^TPl$

- **Datum definition**: rank-deficient matrices, SVD for pseudoinverse

- **Coordinate transformations**: rotation matrices, Helmert

- **Eigenvalue problems**: error ellipses (covariance eigen-decomposition)

- **Condition number**: numerical stability of solutions

- **GPS ambiguity resolution**: integer least squares

## 9. References

- Strang, G. (2016). *Introduction to Linear Algebra*

- MIT OCW 18.06: Linear Algebra

- Lay, D. (2020). *Linear Algebra and Its Applications*

---

*Maintained by AIGIS.*
