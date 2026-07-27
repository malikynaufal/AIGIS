---
title: Metric Spaces
type: concept
subject: Mathematics
tags: [mathematics, metric-spaces, analysis, convergence, completeness]
created: 2026-07-27
updated: 2026-07-27
---

# Metric Spaces

> *"The notion of distance is the first geometric idea."* — Part of [[Mathematics MOC]]. Foundation for analysis, topology, and numerical methods.

## 1. Definition

A **metric space** is $(X, d) $ where $ d: X \times X \to [0, \infty) $ satisfies:

| Axiom | Condition |
|-------|-----------|
| **Positivity** | $ d(x, y) = 0 \iff x = y $ |
| **Symmetry** | $ d(x, y) = d(y, x) $ |
| **Triangle Inequality** | $ d(x, z) \leq d(x, y) + d(y, z) $ |

### Examples

| Space | Metric | Use |
|-------|--------|-----|
| $\mathbb{R}^n $ (Euclidean) | $ d(x,y) = \|x-y\|_2 = \sqrt{\sum (x_i-y_i)^2} $ | Geometry |
| $\mathbb{R}^n $ (Manhattan) |$ d_1(x,y) = \sum |x_i-y_i|$ | Taxicab geometry |
| $\mathbb{R}^n $ (Sup-norm) |$ d_\infty(x,y) = \max |x_i-y_i|$ | Uniform convergence |
| $ C[a,b] $ (continuous) | $ d(f,g) = \sup_{x} |f(x)-g(x)|$ | Function spaces |
| $\ell^p $| $ d(x,y) = (\sum |x_i-y_i|^p)^{1/p} $ | Sequence spaces |
| $ L^p[0,1] $ | $ d(f,g) = (\int_0^1 |f-g|^p)^{1/p} $ | Integrable functions |

## 2. Open and Closed Sets

- **Open ball:** $ B(x, r) = \{y \in X : d(x, y) < r\} $
- **Closed ball:** $\overline{B}(x, r) = \{y \in X : d(x, y) \leq r\} $
- **Open set:** Union of open balls
- **Closed set:** Complement is open
- **Interior:** $ A^\circ = \bigcup \{U \subseteq A : U \text{ open}\} $
- **Closure:** $\overline{A} = A \cup \{x : \forall r > 0, B(x,r) \cap A \neq \emptyset\} $

## 3. Convergence and Continuity

### Convergence

$ x_n \to x $ in $ (X, d) $ iff $ d(x_n, x) \to 0 $ as $ n \to \infty $.

**Uniqueness of limits** holds in all metric spaces.

### Cauchy Sequences

$ (x_n) $ is **Cauchy** iff $\forall \varepsilon > 0, \exists N: m,n \geq N \implies d(x_m, x_n) < \varepsilon $.

Convergent $\implies $ Cauchy (always). Cauchy $\implies $ convergent iff $ X $ is **complete**.

### Continuity

$ f: X \to Y $ is continuous at $ x $ iff $ x_n \to x \implies f(x_n) \to f(x) $.

Equivalently: $\forall \varepsilon > 0, \exists \delta > 0: d(x, x') < \delta \implies d(f(x), f(x')) < \varepsilon $.

## 4. Completeness

A metric space is **complete** if every Cauchy sequence converges.

| Complete | Not Complete |
|----------|--------------|
| $\mathbb{R}^n $|$\mathbb{Q} $ |
| $ C[a,b] $ with sup-norm | $ C[0,1] $ with $ L^1 $ norm |
| $\ell^\infty $| $ c_{00} $ (finite sequences) |

**Banach Space:** Complete normed vector space.

### Banach Fixed Point Theorem

If $ (X, d) $ is complete and $ T: X \to X $ is a **contraction** ($ d(Tx, Ty) \leq q \cdot d(x,y) $, $ q < 1 $), then $ T $ has a unique fixed point $ x^*$ and:$ $ d(x_n, x^*) \leq \frac{q}{1-q} d(x_0, Tx_0)$$

**Applications:** Existence and uniqueness for ODEs (Picard-Lindelöf), convergence of iterative methods.

## 5. Compactness

### Sequential Compactness

Every sequence has a convergent subsequence. In metric spaces, this is equivalent to compactness.

**Arzelà-Ascoli Theorem:** A subset $\mathcal{F} \subseteq C[a,b] $ is relatively compact iff it is uniformly bounded and equicontinuous.

## 6. Normed Spaces

A **norm** $\|\cdot\| $ on a vector space $ V $ satisfies:
1. $\|x\| = 0 \iff x = 0 $ 2.$\|\alpha x\| = |\alpha| \|x\|$ 3.$\|x + y\| \leq \|x\| + \|y\| $ The metric is $ d(x,y) = \|x - y\|$.

| Norm | Formula | Space |
|------|---------|-------|
| $\|x\|_1 $|$\sum |x_i|$|$\ell^1 $ |
| $\|x\|_2 $|$\sqrt{\sum x_i^2} $|$\ell^2 $ (Hilbert) |
| $\|x\|_\infty $|$\max |x_i|$|$\ell^\infty $ |

## 7. Inner Product Spaces

An **inner product** satisfies $\langle x, x \rangle \geq 0 $, $\langle x, y \rangle = \overline{\langle y, x\rangle} $, and linearity.

$\|x\| = \sqrt{\langle x, x \rangle} $ gives a norm.

**Hilbert Space:** Complete inner product space.

**Key examples:** $\ell^2 $, $ L^2[0,1] $.

**Orthogonality:** $\langle x, y \rangle = 0 \implies \|x + y\|^2 = \|x\|^2 + \|y\|^2 $ (Pythagorean theorem).

## 8. Applications

| Field | Application |
|-------|-------------|
| **Numerical Analysis** | Convergence of iterative methods (Banach theorem) |
| **PDEs** | Sobolev spaces, weak solutions |
| **Geodesy** | Weighted least squares in Hilbert space $ L^2(W) $ |
| **Quantum Mechanics** | Hilbert space of quantum states |
| **Machine Learning** | Kernel methods in feature spaces |

## Practice Problems

1. Prove that $ (\mathbb{R}, d) $ with $ d(x,y) = |x-y|$ is a complete metric space.
2. Show that $\ell^2 $ is a Hilbert space.
3. Apply Banach fixed point theorem to prove Picard's theorem for ODEs.
4. Show that the $ L^p $ spaces are Banach spaces for $ 1 \leq p \leq \infty$.

## References

- Kreyszig, E. (1978). *Introductory Functional Analysis with Applications*. Wiley.
- Carothers, N.L. (2000). *Real Analysis*. Cambridge.
- Rudin, W. (1991). *Functional Analysis* (2nd ed.). McGraw-Hill.

---
*See also: [[Topology]], [[Real Analysis]], [[Linear Algebra Fundamentals]], [[Optimization Theory]]*
