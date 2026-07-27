---
title: Semester 2 — Aljabar Linear Lanjut (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, linear-algebra, semester-2, aigis, geodesy-applied]
---

# Semester 2 — Aljabar Linear Lanjut (Expanded)

**Course**: MGM211203 — Aljabar Linear Lanjut 
**Credits**: 3 SKS 
**Prerequisites**: [[Kalkulus I Expanded]]

---

## Course Overview

Advanced Linear Algebra extends basic matrix algebra to inner product spaces, spectral theory, and applications. This is the most important mathematics course for geodesy — least squares adjustment is built entirely on linear algebra.

---

## Syllabus

### Weeks 1-2: Vector Spaces

#### 1.1 Abstract Vector Spaces
**Definition**: Set $V $with addition$+$and scalar multiplication $\cdot $satisfying 8 axioms (commutativity, associativity, distributivity, identity, inverse, etc.).

**Examples**:$\mathbb{R}^n$, $\mathbb{C}^n$, $\mathcal{C}[a,b]$, $\mathcal{P}_n$(polynomials of degree $\leq n$).

#### 1.2 Subspaces
$W \subseteq V $is a subspace if:
1.$0 \in W$2.$u, v \in W$→$u+v \in W$3.$v \in W$, $c \in F$→$cv \in W$**Span**:$\text{span}\\{v_1,\ldots,v_k\\} = \\{\sum c_i v_i : c_i \in F\\} $#### 1.3 Linear Independence $\\{v_1,\ldots,v_k\\} $is linearly independent if $\sum c_i v_i = 0$→$c_1 = \cdots = c_k = 0$.

#### 1.4 Basis and Dimension
Basis = linearly independent spanning set. All bases of a vector space have same cardinality = dimension.

**Example**: $\\{1, x, x^2, \ldots, x^n\\} $is the standard basis for $\mathcal{P}_n$, $\dim = n+1$.

### Weeks 3-4: Linear Transformations

#### 2.1 Definition
$T: V \to W $is linear if $T(u+v)=T(u)+T(v) $and $T(cv)=cT(v)$.

#### 2.2 Kernel and Image

- $\text{Ker}(T) = \\{v: Tv=0\\} $-$\text{Im}(T) = \\{Tv: v \in V\\} $- **Rank-Nullity**:$\dim(\text{Ker}(T)) + \dim(\text{Im}(T)) = \dim(V)$#### 2.3 Matrix Representation

Every linear $T: V \to W $with bases $B, C $has matrix$[T]_{C\leftarrow B} $.

$[T(v)]_C = [T]_{C\leftarrow B}[v]_B$#### 2.4 Change of Basis $P_{B\leftarrow C} $= transition matrix from basis $C $to basis $B$.

$[v]_B = P_{B\leftarrow C}[v]_C$### Weeks 5-6: Inner Product Spaces

#### 3.1 Inner Product

$$\langle u, v \rangle$$

**Properties**: Symmetry, linearity in first argument, positive definiteness ($\langle v,v\rangle \geq 0$, $=0 $iff $v=0$).

**Standard**: $\langle u,v\rangle = u^T v $in $\mathbb{R}^n$, $\langle f,g\rangle = \int_a^b f(x)g(x)\,dx $in $L^2$.

#### 3.2 Norm and Distance

$$\\|v\\| = \sqrt{\langle v,v\rangle}d(u,v) = \\|u-v\\| $$#### 3.3 Orthogonality

**Cauchy-Schwarz**:$|\langle u,v\rangle| \leq \\|u\\|\\|v\\| $**Pythagorean**: If $u \\perp v$, $\\|u+v\\|^2 = \\|u\\|^2 + \\|v\\|^2$#### 3.4 Gram-Schmidt Process
Given $\\{v_1,\ldots,v_k\\} $, produce orthonormal $\\{u_1,\ldots,u_k\\} $:

$$u_1 = \frac{v_1}{\\|v_1\\|}w_k = v_k - \sum_{i=1}^{k-1} \langle v_k,u_i\rangle u_i, \\quad u_k = \frac{w_k}{\\|w_k\\|} $$#### 3.5 Orthogonal Complement $W^\\perp = \\{v: \langle v,w\rangle = 0 \, \\forall w \in W\\} $

$\dim(W) + \dim(W^\\perp) = \dim(V)$### Weeks 7-8: Least Squares

#### 4.1 Best Approximation
**Best approximation theorem**: Unique vector $\hat{y} \in W $minimizing $\\|y-\hat{y}\\| $.

$\hat{y} = \text{proj}_W(y)$(orthogonal projection onto $W$)

#### 4.2 Normal Equations

For $A\hat{x} \approx b$: $A^TA\hat{x} = A^Tb $When $A $has full column rank:$\hat{x} = (A^TA)^{-1}A^Tb$#### 4.3 Orthogonal Projection Matrix $P_W = A(A^TA)^{-1}A^T$(projects onto $\text{Col}(A)$)

Properties: $P_W = P_W^T$, $P_W^2 = P_W$, $\hat{y} = P_W y$.

### Weeks 9-10: Eigenvalues and Diagonalization

#### 5.1 Characteristic Polynomial

$p(\lambda) = \det(A-\lambda I)$#### 5.2 Diagonalization $A = PDP^{-1} $where $D $is diagonal and $P $contains eigenvectors.$A $is diagonalizable $\\iff$ $A $has $n $independent eigenvectors.

**Criterion**: Distinct eigenvalues → diagonalizable.

#### 5.3 Spectral Decomposition

For symmetric $A$: $A = Q\Lambda Q^T $with $Q $orthogonal.$A = \sum_{i=1}^n \lambda_i q_i q_i^T$#### 5.4 Quadratic Forms $Q(x) = x^TAx$— sign determined by eigenvalues.

### Weeks 11-12: Applications

#### 6.1 Singular Value Decomposition $A = U\Sigma V^T $Used for: pseudoinverse, low-rank approximation, condition number.

#### 6.2 QR Decomposition $A = QR$, with $Q $orthogonal,$R $upper triangular.

Used for: stable least squares, Gram-Schmidt computation.

#### 6.3 LU Decomposition $A = LU$— Gaussian elimination factorization.

---

## Practice Problems

1. Find the orthogonal projection of$(1,2,3) $onto the span of$(1,2,-1) $and$(2,1,1)$.
2. Diagonalize $A = \begin{bmatrix}3&1\\\\1&3\end{bmatrix} $.
3. Find the SVD of $A = \begin{bmatrix}2&1\\\\1&2\end{bmatrix} $.
4. Solve $\hat{x} $in the least squares sense:$\begin{bmatrix}1&1\\\\1&2\\\\1&3\end{bmatrix}x = \begin{bmatrix}1\\\\3\\\\5\end{bmatrix} $.

---

## Geodesy Connections

- **Orthogonal projection**: Residual vectors in least squares

- **Spectral decomposition**: Error ellipses (eigenvectors = axes directions)

- **SVD**: Rank-deficient normal equations (datum ambiguity)

- **Inner products**: Weighted least squares $\langle l_1,l_2\rangle = l_1^T P l_2$

---

## References

- Strang, G. *Linear Algebra and Its Applications* (Chapters 4-6)

- MIT OCW 18.06: Linear Algebra

- Lay, D. (2020). *Linear Algebra*

---

➡️ [[Mathematics MOC]] | ➡️ [[Linear Algebra Fundamentals]]