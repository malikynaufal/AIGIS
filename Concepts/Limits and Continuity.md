---
tags: [aigis, concept, mathematics, calculus, limits, continuity]
created: 2026-07-27
updated: 2026-07-27
---

# Limits and Continuity

## For Geodesy & Physics Applications

**Core Idea:** Limits formalize the intuitive notion of "approaching" a value. Continuity ensures functions behave predictably — no sudden jumps. These are the bedrock of calculus, essential for modeling smooth physical phenomena (orbits, gravity fields, signal processing) and numerical methods (GNSS positioning, least-squares adjustment).

---

## Fundamental Concepts

### The ε–δ Definition of a Limit

Let $f$ be a function defined near $a$ (except possibly at $a$). We say:

$$\lim_{x \to a} f(x) = L$$

if for every $\varepsilon > 0$, there exists a $\delta > 0$ such that:

$$0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$

| Symbol | Meaning |
|--------|---------|
| $\varepsilon$ | Tolerance on output (how close $f(x)$ must be to $L$) |
| $\delta$ | Tolerance on input (how close $x$ must be to $a$) |
| $L$ | The limiting value |
| $a$ | The approach point |

**Geometric interpretation:** No matter how tight a horizontal band ($\pm \varepsilon$) around $L$ we draw, we can find a vertical band ($\pm \delta$) around $a$ such that the graph stays inside the horizontal band.

### One-Sided Limits

$$\lim_{x \to a^-} f(x) = L^- \quad \text{(left-hand limit)}$$
$$\lim_{x \to a^+} f(x) = L^+ \quad \text{(right-hand limit)}$$

The two-sided limit exists **iff** $L^- = L^+$.

### Limits at Infinity & Infinite Limits

| Type | Notation | Meaning |
|------|----------|---------|
| Limit at infinity | $\lim_{x \to \infty} f(x) = L$ | $f(x)$ approaches $L$ as $x$ grows |
| Infinite limit | $\lim_{x \to a} f(x) = \infty$ | $f(x)$ grows without bound near $a$ |

---

## Continuity

### Definition

A function $f$ is **continuous at $a$** iff:

1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists
3. $\lim_{x \to a} f(x) = f(a)$

### Types of Discontinuities

| Type | Condition | Example |
|------|-----------|---------|
| **Removable** | $\lim_{x \to a} f(x)$ exists but $\neq f(a)$ or $f(a)$ undefined | $f(x) = \frac{\sin x}{x}$ at $x=0$ |
| **Jump** | Left and right limits exist but are unequal | $f(x) = \lfloor x \rfloor$ at integers |
| **Infinite/Essential** | Limit is $\pm \infty$ or doesn't exist | $f(x) = \frac{1}{x}$ at $x=0$ |

### Continuity on Intervals

- **Continuous on $(a,b)$:** continuous at every point in the open interval
- **Continuous on $[a,b]$:** continuous on $(a,b)$ + right-continuous at $a$ + left-continuous at $b$

---

## In Geodesy & Physics Context

| Application | Formula/Method | When Used |
|-------------|----------------|-----------|
| **GNSS Positioning** | Taylor expansion of nonlinear range equations around approximate position | Linearize $|| \mathbf{x} - \mathbf{s}_i || = \rho_i$ for least-squares |
| **Gravity Field Modeling** | Spherical harmonic series convergence analysis | Ensuring series for geoid/potential converges uniformly |
| **Numerical Differentiation** | Finite difference limits: $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ | Computing gradients in adjustment |
| **Signal Processing** | Fourier series convergence (Dirichlet conditions) | Decomposing periodic geodetic signals |
| **Coordinate Transformations** | Continuity of projection mappings (e.g., UTM, Mercator) | Ensuring no tears in map projections |

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\lim_{x \to 0} \frac{\sin x}{x} = 1$ | Fundamental trig limit | Derivatives of trig functions |
| $\lim_{x \to 0} \frac{e^x - 1}{x} = 1$ | Exponential limit | Derivative of $e^x$ |
| $\lim_{x \to \infty} (1 + \frac{1}{x})^x = e$ | Definition of $e$ | Continuous compounding, growth models |
| $\lim_{x \to a} \frac{f(x)-f(a)}{x-a} = f'(a)$ | Derivative definition | Instantaneous rate of change |
| $\lim_{h \to 0} \frac{f(x+h)-2f(x)+f(x-h)}{h^2} = f''(x)$ | Second difference | Numerical second derivative |

---

## Key Theorems

### Intermediate Value Theorem (IVT)
If $f$ is continuous on $[a,b]$ and $N$ is between $f(a)$ and $f(b)$, then $\exists c \in (a,b)$ such that $f(c) = N$.

**Geodesy use:** Root-finding for nonlinear equations (e.g., solving Kepler's equation for eccentric anomaly).

### Extreme Value Theorem (EVT)
If $f$ is continuous on $[a,b]$, then $f$ attains absolute max and min on $[a,b]$.

**Geodesy use:** Optimization in least-squares adjustment (covariance analysis).

### Mean Value Theorem (MVT)
If $f$ continuous on $[a,b]$ and differentiable on $(a,b)$, then $\exists c \in (a,b)$ with $f'(c) = \frac{f(b)-f(a)}{b-a}$.

**Geodesy use:** Error bounds in numerical integration (quadrature for area on ellipsoid).

---

## Related Concepts

- [[Derivatives]] — Limits define the derivative
- [[Sequences and Series]] — Limits of sequences generalize function limits
- [[Multivariable Calculus]] — Limits in $\mathbb{R}^n$: $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L$
- [[Numerical Methods]] — Finite differences approximate limits
- [[Error Propagation]] — Continuity ensures small input errors → small output errors

---

## Study Problems

1. **Recall:** State the ε–δ definition of $\lim_{x \to 2} (3x - 1) = 5$. Find $\delta$ for $\varepsilon = 0.01$.
2. **Application:** Prove $\lim_{x \to 0} x \sin(1/x) = 0$ using the Squeeze Theorem.
3. **Derivation:** Use the limit definition to find $f'(x)$ for $f(x) = \sqrt{x}$.
4. **Real-world:** A GNSS receiver computes position via $\mathbf{x}_{k+1} = \mathbf{x}_k - (J^T J)^{-1} J^T \mathbf{r}(\mathbf{x}_k)$. Why does continuity of $\mathbf{r}(\mathbf{x})$ matter for convergence?

---

## Common Mistakes

1. **Confusing limit with function value:** $\lim_{x \to a} f(x) \neq f(a)$ in general (only if continuous).
2. **Assuming one-sided limits equal the two-sided limit:** Must check both sides.
3. **Treating $\infty$ as a number:** $\infty - \infty$, $0 \cdot \infty$, $\frac{\infty}{\infty}$ are indeterminate forms — not arithmetic.
4. **Ignoring domain issues:** $\lim_{x \to 0} \sqrt{x}$ only exists as right-hand limit.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*