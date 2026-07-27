---
title: Topology
type: concept
subject: Mathematics
tags: [mathematics, topology, metric-spaces, continuity, manifolds]
created: 2026-07-27
updated: 2026-07-27
---

# Topology

> *"Topology is exactly the study of what doesn't change when you continuously deform things."* — John Baez
> Part of [[Mathematics MOC]]. Foundation for analysis, differential geometry, and data analysis (TDA).

## 1. Metric Spaces

A **metric space** $(X, d)$ has a distance function $d: X \times X \to [0, \infty)$ satisfying:
1. $d(x, y) = 0 \iff x = y$
2. $d(x, y) = d(y, x)$
3. Triangle inequality: $d(x, z) \leq d(x, y) + d(y, z)$

### Open and Closed Sets

- **Open ball:** $B(x, r) = \{y \in X : d(x, y) < r\}$
- **Open set:** $U \subseteq X$ is open if $\forall x \in U, \exists r > 0: B(x, r) \subseteq U$
- **Closed set:** Complement is open, or contains all its limit points
- **Closure:** $\overline{A} = A \cup A'$ (limit points)
- **Interior:** $A^\circ = $ largest open set $\subseteq A$
- **Boundary:** $\partial A = \overline{A} \setminus A^\circ$

### Convergence

$x_n \to x$ iff $\forall \varepsilon > 0, \exists N: n \geq N \implies d(x_n, x) < \varepsilon$.

**Cauchy sequence:** $\forall \varepsilon > 0, \exists N: m, n \geq N \implies d(x_m, x_n) < \varepsilon$.

A metric space is **complete** if every Cauchy sequence converges.

## 2. Topological Spaces

A **topology** on $X$ is a collection $\tau \subseteq \mathcal{P}(X)$ such that:
1. $\emptyset, X \in \tau$
2. Arbitrary unions of sets in $\tau$ are in $\tau$
3. Finite intersections of sets in $\tau$ are in $\tau$

A **topological space** is $(X, \tau)$. Elements of $\tau$ are **open sets**.

### Basis and Subbasis

A **basis** $\mathcal{B}$ generates $\tau$ if every open set is a union of basis elements.

Standard basis for $\mathbb{R}^n$: $\{B(x, r) : x \in \mathbb{R}^n, r > 0\}$.

### Continuous Maps

$f: X \to Y$ is **continuous** if $f^{-1}(U)$ is open in $X$ for every open $U \subseteq Y$.

**Equivalent:** $f$ preserves limits: $x_n \to x \implies f(x_n) \to f(x)$.

### Homeomorphisms

A **homeomorphism** is a bijection $f: X \to Y$ with $f$ and $f^{-1}$ continuous.

$X$ and $Y$ are **homeomorphic** ($X \cong Y$) — they have identical topological properties.

| Invariant under homeomorphism | Not invariant |
|------------------------------|---------------|
| Connectedness | Metric (distance) |
| Compactness | Boundedness |
| Hausdorff property | Curvature |
| Fundamental group | Specific shape |

## 3. Separation Axioms

| Axiom | Name | Meaning |
|-------|------|---------|
| $T_0$ | Kolmogorov | For any distinct $x, y$, one has a neighborhood not containing the other |
| $T_1$ | Fréchet | For any distinct $x, y$, each has a neighborhood not containing the other |
| $T_2$ | Hausdorff | Any distinct $x, y$ have disjoint neighborhoods |
| $T_3$ | Regular | $T_1$ + point and closed set can be separated |
| $T_4$ | Normal | $T_1$ + disjoint closed sets can be separated |

**Metric spaces are $T_4$ (normal Hausdorff).**

## 4. Connectedness

$X$ is **connected** if it cannot be written as $U \cup V$ with $U, V$ non-empty, open, disjoint.

$X$ is **path-connected** if $\forall x, y \in X, \exists$ continuous $f: [0,1] \to X$ with $f(0)=x, f(1)=y$.

Path-connected $\implies$ connected (converse false: topologist's sine curve).

## 5. Compactness

$K \subseteq X$ is **compact** if every open cover has a finite subcover.

**Heine-Borel Theorem:** In $\mathbb{R}^n$, compact $\iff$ closed and bounded.

**Key properties:**
- Continuous image of compact is compact
- Compact subsets of Hausdorff spaces are closed
- Continuous function on compact attains max/min (Extreme Value Theorem)

## 6. Product and Quotient Topologies

### Product Topology

For $\prod X_i$, basic open sets are $\prod U_i$ where $U_i \subseteq X_i$ open and $U_i = X_i$ for all but finitely many $i$.

### Quotient Topology

Given $f: X \to Y$ surjective, $U \subseteq Y$ is open iff $f^{-1}(U)$ is open in $X$.

**Example:** Identifying opposite edges of a square gives a torus.

## 7. Fundamental Group

The **fundamental group** $\pi_1(X, x_0)$ is the set of homotopy classes of loops based at $x_0$, with concatenation as operation.

| Space | $\pi_1$ |
|-------|----------|
| $\mathbb{R}^n$, ball | Trivial (simply connected) |
| $S^1$ (circle) | $\mathbb{Z}$ |
| Torus $T^2$ | $\mathbb{Z} \times \mathbb{Z}$ |
| Figure-eight | Free group $F_2$ |

```mermaid
graph TD
    Base[Topological Space X] --> CG[Connected?]
    CG -->|Yes| PG[π₁(X) = ?]
    CG -->|No| Components[Components]
    PG --> Simply[Simply connected if trivial]
    PG --> Z[ℤ for S¹]
    PG --> ZxZ[ℤ×ℤ for T²]
    PG --> Fn[Free group Fₙ]
```

## 8. Applications to Data Analysis (TDA)

**Topological Data Analysis** uses persistent homology to study shape of data.

- **Vietoris-Rips complex:** Build simplicial complexes at scale $\epsilon$
- **Persistence diagram:** Track birth/death of topological features
- **Betti numbers:** $\beta_0$ (components), $\beta_1$ (loops), $\beta_2$ (voids)

## Practice Problems

1. Prove that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
2. Show that $\mathbb{R}$ and $(0,1)$ are homeomorphic.
3. Prove that $[0,1]$ is compact but $(0,1)$ is not.
4. Compute the fundamental group of the figure-eight space.

## References

- Munkres, J.R. (2000). *Topology* (2nd ed.). Prentice Hall.
- Hatcher, A. (2002). *Algebraic Topology*. Cambridge (free online).
- Lee, J.M. (2011). *Introduction to Topological Manifolds*. Springer.

---
*See also: [[Metric Spaces]], [[Real Analysis]], [[Differential Geometry]], [[Manifolds]]*
