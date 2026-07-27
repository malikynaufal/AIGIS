---
tags: [aigis, concept, mathematics, linear-algebra, matrices, vectors]
created: 2026-07-27
updated: 2026-07-27
---

# Linear Algebra Fundamentals

## For Geodesy & Physics Applications

**Core Idea:** Linear algebra provides the language and tools for solving systems of equations, transforming coordinates, and representing physical quantities as vectors and matrices. In geodesy, matrices encode GNSS geometry, datum transformations, and least-squares adjustment. In physics, they describe rotations, quantum states, and tensor operations.

---

## Fundamental Concepts

### Vectors in ℝⁿ

A vector $\mathbf{v} \in \mathbb{R}^n $is an ordered $n$-tuple:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = (v_1, v_2, \dots, v_n)$$**Operations:**

| Operation | Formula |
|-----------|---------|
| Addition | $\mathbf{u} + \mathbf{v} = (u_1+v_1, u_2+v_2, \dots, u_n+v_n)$ |
| Scalar multiplication | $c\mathbf{v} = (cv_1, cv_2, \dots, cv_n)$ |
| Dot (inner) product | $\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$ |
| Cross product (ℝ³) | $\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} $ |
| Norm (length) | $\ |\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_2^2} $ |

**Key properties:**
-$\mathbf{u} \cdot \mathbf{v} = 0 \implies \mathbf{u} \perp \mathbf{v} $(orthogonal)
-$\ |\mathbf{v}\|^2 = \mathbf{v} \cdot \mathbf{v} $- Cauchy-Schwarz:$|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\|\,\|\mathbf{v}\| $### Matrices

A matrix $A \in \mathbb{R}^{m \times n} $has $m $rows and $n $columns
:

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} $$

**Special matrices:**

| Type | Definition | Symbol |
|------|-------------|--------|
| Square | $m = n$ | $A_{n \times n} $ |
| Diagonal | $a_{ij} = 0 $for $i \neq j$ | $\text{diag}(d_1, \dots, d_n)$ |
| Identity | $I_n = \text{diag}(1, 1, \dots, 1)$ | $I_n$ |
| Zero | All entries 0 | $0_{m \times n} $ |
| Symmetric | $A = A^T$ | $A^T = A$ |
| Skew-symmetric | $A^T = -A$ | $A^T = -A$ |
| Orthogonal | $A^T A = I$ | $A^T = A^{-1} $ |
| Positive definite | $\mathbf{x}^T A \mathbf{x} > 0 $for $\mathbf{x} \neq 0$ | $A \succ 0$ |

### Matrix Operations

| Operation | Formula |
|-----------|---------|
| Addition | $(A + B)_{ij} = A_{ij} + B_{ij} $ |
| Scalar mult | $(cA)_{ij} = c \cdot A_{ij} $ |
| Multiplication | $(AB)_{ij} = \sum_{k=1}^n A_{ik} B_{kj} $ |
| Transpose | $(A^T)_{ij} = A_{ji} $ |
| Determinant | $\det(A)$, volume scaling factor |
| Inverse | $A^{-1} $such that $AA^{-1} = I$ |
| Trace | $\text{tr}(A) = \sum_{i=1}^n A_{ii} $ |

---

## Key Theorems

### Determinant Properties

$$\det(AB) = \det(A)\det(B)\det(A^T) = \det(A)\det(A^{-1}) = \frac{1}{\det(A)}\det(cA) = c^n \det(A) \quad (A \in \mathbb{R}^{n \times n}
)

$$### Matrix Inversion Lemma (Woodbury)$$

(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1} $$**Use in geodesy:** Efficient inversion of augmented covariance matrices.

### Eigenvalue Decomposition

For a square matrix $A \in \mathbb{R}^{n \times n} $:

$$A\mathbf{v} = \lambda \mathbf{v} $$-$\lambda$= eigenvalue
-$\mathbf{v} $= eigenvector

**Properties:**
-$\det(A) = \prod_{i=1}^n \lambda_i$-$\text{tr}(A) = \sum_{i=1}^n \lambda_i$-$A $diagonalizable if $n $independent eigenvectors exist

### Singular Value Decomposition (SVD
)

$$A = U\Sigma V^T$$

-$U \in \mathbb{R}^{m \times m} $(orthogonal)
-$\Sigma \in \mathbb{R}^{m \times n} $(diagonal singular values $\sigma_1 \geq \sigma_2 \geq \dots \geq 0$)

- $V \in \mathbb{R}^{n \times n} $(orthogonal)

**Geodesy use:** Rank-deficient least-squares, principal component analysis of coordinate time series.

---

## In Geodesy & Physics Context

### GNSS Positioning as Linear System

The linearized GNSS observation equation
:

$$\mathbf{y} = H\mathbf{x} + \mathbf{e} $$

where:
-$\mathbf{y} $= observation vector (pseudoranges, phases)
-$H$= design matrix (geometry matrix)
-$\mathbf{x} $= unknown parameters (position, clock bias)
-$\mathbf{e} $= error vector

Least-squares solution
:

$$\hat{\mathbf{x}} = (H^T H)^{-1} H^T \mathbf{y} $$

### Covariance Propagation

If $\mathbf{x} $has covariance $C_x$, then $y = Ax + b $has
:

$$C_y = A C_x A^T$$

### Helmert Transformation (7-parameter
)

$$\begin{bmatrix} X \\ Y \\ Z \end{bmatrix}_{\text{new}} = \begin{bmatrix} 1 & -\varepsilon_Z & \varepsilon_Y \\ \varepsilon_Z & 1 & -\varepsilon_X \\ -\varepsilon_Y & \varepsilon_X & 1 \end{bmatrix} \begin{bmatrix} X \\ Y \\ Z \end{bmatrix}_{\text{old}} + \begin{bmatrix} T_X \\ T_Y \\ T_Z \end{bmatrix} $$

- 3 translations$(T_X, T_Y, T_Z)$- 3 rotations$(\varepsilon_X, \varepsilon_Y, \varepsilon_Z)$- 1 scale factor $s = 1 + \delta\mu$### Rotation Matrices

**Rotation about Z-axis (yaw):*
*

$$R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

**Rotation about Y-axis (pitch):*
*

$$R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix} $$

**Rotation about X-axis (roll):*
*

$$R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix} $$

Combined:$R = R_z R_y R_x$---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$ | Dot product | Angle between vectors |
| $\hat{\mathbf{x}} = (H^T H)^{-1} H^T \mathbf{y} $ | LS solution | GNSS/deformation |
| $C_y = A C_x A^T$ | Error propagation | Covariance |
| $A = U\Sigma V^T$ | SVD | Rank, pseudoinverse |
| $\det(A) = \prod \lambda_i$ | Determinant | Volume/singularity |
| $A\mathbf{v} = \lambda\mathbf{v} $ | Eigenvalue eq | Vibrations, stability |

---

## Related Concepts

- [[Least Squares Adjustment]] — Linear algebra for parameter estimation

- [[Reference Ellipsoid]] — Parametric surfaces via linear algebra

- [[Helmert Transformation]] — 7-parameter coordinate conversion

- [[Derivatives]] — Matrix derivatives (gradient, Jacobian)

- [[Error Propagation]] — Covariance propagation

- [[RTK]] — Real-time kinematics via linearized models

---

## Study Problems

1. **Recall:** Compute the eigenvalues and eigenvectors of $A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} $.
2. **Application:** Given GNSS satellite positions in ECEF and design matrix $H$, derive the PDOP (Position Dilution of Precision) from $(H^T H)^{-1} $.
3. **Derivation:** Show that for an orthogonal matrix $Q$, $\ |Q\mathbf{x}\| = \|\mathbf{x}\| $for any vector $\mathbf{x} $.
4. **Real-world:** In Helmert transformation from WGS84 to DGN95 (Indonesia local datum), if the rotation parameters are $\varepsilon_X = 0.5''$, $\varepsilon_Y = -0.3''$, $\varepsilon_Z = 0.8''$, convert these to radians and form the rotation matrix. What physical interpretation do these small angles have?

---

## Common Mistakes

1. **Matrix multiplication order:** $AB \neq BA $in general — order matters.
2. **Confusing transpose with inverse:**$(AB)^T = B^T A^T$, but $(AB)^{-1} = B^{-1} A^{-1} $.
3. **Dimension mismatch:** Cannot multiply $(m \times n)(p \times q) $unless $n = p$.
4. **Forgetting that inverse only exists for square, full-rank matrices.**
5. **Using the wrong norm:** $\ell_1$, $\ell_2$, $\ell_\infty$ give different results.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*