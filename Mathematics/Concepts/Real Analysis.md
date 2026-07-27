---
title: Real Analysis
type: concept
subject: Mathematics
tags: [mathematics, real-analysis, measure-theory, sequences, continuity]
created: 2026-07-27
updated: 2026-07-27
---

# Real Analysis

> *"Analysis is the branch of mathematics most closely related to calculus."* — Rudin
> Part of [[Mathematics MOC]]. Provides the rigorous foundation for calculus, measure theory, and probability.

## 1. The Real Numbers

### Axioms of $\mathbb{R} $

$\mathbb{R} $ is a **complete ordered field**:
1. **Field axioms:** Addition, multiplication, distributivity
2. **Order axioms:** Total order compatible with field operations
3. **Completeness:** Every non-empty bounded-above set has a supremum

### The Completeness Axiom

**Least Upper Bound (LUB) Property:** If $ S \subseteq \mathbb{R} $ is non-empty and bounded above, then $\sup S $ exists.

This is equivalent to:
- **Monotone Convergence Theorem**
- **Nested Interval Property**
- **Heine-Borel Theorem**
- **Cauchy Completeness**

## 2. Sequences and Limits

### Convergence

$ (a_n) $ **converges** to $ L $ if $\forall \varepsilon > 0, \exists N \in \mathbb{N}: n \geq N \implies |a_n - L| < \varepsilon $.

**Cauchy sequence:** $\forall \varepsilon > 0, \exists N: m, n \geq N \implies |a_m - a_n| < \varepsilon $.

In $\mathbb{R} $: Convergent $\iff $ Cauchy (completeness).

### Key Theorems

| Theorem | Statement |
|---------|-----------|
| **Bolzano-Weierstrass** | Every bounded sequence has a convergent subsequence |
| **Squeeze Theorem** | $ a_n \leq b_n \leq c_n $, $ a_n, c_n \to L \implies b_n \to L $ |
| **Monotone Convergence** | Every bounded monotone sequence converges |

### Limits Superior and Inferior

$ $\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \sup_{k \geq n} a_k

$$

Every sequence satisfies: $\liminf a_n \leq \limsup a_n $, with equality iff $\lim a_n $ exists.

## 3. Series

### Convergence Tests

| Test | Condition | Type |
|------|-----------|------|
| **Comparison** | $ 0 \leq a_n \leq b_n $, $\sum b_n $ converges $\implies \sum a_n $ converges | Positive terms |
| **Ratio** | $\lim |a_{n+1}/a_n| = L $| $ L < 1 $: converges, $ L > 1 $: diverges |
| **Root** | $\lim \sqrt[n]{|a_n|} = L $ | Same as ratio test |
| **Integral** | $\int_1^\infty f(x)dx $ converges $\iff $ $\sum f(n) $ converges | Positive, decreasing |
| **Dirichlet** | Partial sums of $\sum b_n $ bounded,$ a_n \to 0 $ monotonically | Alternating-like |
| **Abel** | $\sum a_n $ converges,$ b_n $ monotone bounded | General |

### Power Series

$ $\sum_{n=0}^{\infty} c_n (x-a)^n

$$**Radius of convergence:**$ R = 1/\limsup |c_n|^{1/n} $- Converges absolutely for $|x-a| < R $- Diverges for $|x-a| > R $### Uniform Convergence $ f_n \to f $**uniformly** on $ S $ if $\sup_{x \in S} |f_n(x) - f(x)| \to 0 $.

**Key property:** Uniform limit of continuous functions is continuous.

## 4. Continuity (Rigorous)

$ f: \mathbb{R} \to \mathbb{R} $ is **continuous at $ a $** if:

$ $\forall \varepsilon > 0, \exists \delta > 0: |x - a| < \delta \implies |f(x) - f(a)| < \varepsilon

$$### Heine Definition $ f $ is continuous at $ a $ $\iff $ for every sequence $ x_n \to a $, we have $ f(x_n) \to f(a) $.

### Properties

| Theorem | Statement |
|---------|-----------|
| **Extreme Value** | Continuous on $ [a,b] $ $\implies $ attains max and min |
| **Intermediate Value** | $ f $ continuous, $ f(a) < c < f(b) $ $\implies $ $\exists x: f(x) = c $ |
| **Uniform Continuity** | Continuous on $ [a,b] $ $\implies $ uniformly continuous |

## 5. Differentiability

### Mean Value Theorem

If $ f $ is continuous on $ [a,b] $ and differentiable on $ (a,b) $:

$ $\exists c \in (a,b): f'(c) = \frac{f(b) - f(a)}{b - a}

$$**Taylor's Theorem with Remainder:**$ $ f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x)$$

Lagrange remainder: $ R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1} $

## 6. Integration

### Riemann Integral

$\int_a^b f(x) \, dx = \lim_{\|P\| \to 0} \sum_{i=1}^{n} f(c_i)(x_i - x_{i-1}) $**Integrability:**$ f $ is Riemann integrable $\iff $ it is bounded and continuous almost everywhere.

### Fundamental Theorem of Calculus

1. $\frac{d}{dx} \int_a^x f(t) \, dt = f(x) $ 2.$\int_a^b f(x) \, dx = F(b) - F(a) $ where $ F' = f $

## 7. Measure Theory (Preview)

### Lebesgue Measure

The **Lebesgue measure** $ m(E) $ extends length to irregular sets.

- $ m([a,b]) = b - a $
- $ m(\mathbb{Q}) = 0 $ (rationals are countable, thus measure zero)
- Countable additivity: $ m(\cup E_i) = \sum m(E_i) $ (disjoint)

### Lebesgue Integral

$ $\int f \, dm = \sup \left\{ \int s \, dm : 0 \leq s \leq f, \; s \text{ simple} \right\}

$$

### Lebesgue's Dominated Convergence Theorem

If $ f_n \to f $ pointwise and $|f_n| \leq g $ with $\int g < \infty $, then:

$ $\lim_{n \to \infty} \int f_n = \int f

$$

## 8. Metric Space Topology

### Important Properties

| Property | Definition |
|----------|-----------|
| **Separable** | Contains a countable dense subset |
| **Compact** | Every open cover has a finite subcover |
| **Connected** | Not a union of two disjoint non-empty open sets |

**Compactness in $\mathbb{R}^n $:** $ K $ is compact $\iff $ closed and bounded (Heine-Borel).

## Practice Problems

1. Prove that $\sqrt{2} $ is irrational using the least upper bound property.
2. Prove the Bolzano-Weierstrass theorem.
3. Show that $ f_n(x) = x^n $ on $ [0,1] $ converges pointwise but not uniformly.
4. Evaluate $\int_0^1 x^2 \, dx$ using the definition of Riemann integral.

## References

- Rudin, W. (1976). *Principles of Mathematical Analysis* (3rd ed.). McGraw-Hill.
- Abbott, S. (2015). *Understanding Analysis* (2nd ed.). Springer.
- Tao, T. (2016). *Analysis I* (3rd ed.). Hindustan Book Agency.

---
*See also: [[Limits Continuity]], [[Sequences and Series]], [[Measure Theory]], [[Topology]]*
