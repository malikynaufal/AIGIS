---
tags: [aigis, concept, mathematics, series, sequences, convergence]
aliases: [Sequences and Series, SeriesConvergence]
created: 2026-07-27
updated: 2026-07-27
---

# Sequences and Series

## For Geodesy & Physics

**Core Idea:** Sequences are ordered lists of numbers; series are sums of sequences. In geodesy, series expansions (Taylor, Fourier, spherical harmonics) are essential tools. Spherical harmonic series describe Earth's gravity field; Taylor series linearize GNSS equations; Fourier series analyze tidal signals.

---

## Fundamental Concepts

### Sequences

A sequence $\{a_n\}$ converges to $L$ if $\forall \varepsilon > 0, \exists N: n > N \implies |a_n - L| < \varepsilon$.

### Series Convergence Tests

| Test | Condition | Use |
|------|-----------|-----|
| **Geometric series** | $\sum ar^n$ converges iff $|r| < 1$, sum $= a/(1-r)$ | Exponential models |
| **p-series** | $\sum 1/n^p$ converges iff $p > 1$ | Integrals, sums |
| **Ratio test** | $L = \lim |a_{n+1}/a_n|$: converge if $< 1$ | Factorials, powers |
| **Root test** | $L = \lim |a_n|^{1/n}$: converge if $< 1$ | Power series |
| **Comparison** | Compare with known series | Direct comparison |
| **Integral test** | $\int_1^\infty f(x)dx$ converges $\iff$ series converges | Continuous functions |
| **Alternating series** | $\sum (-1)^n a_n$ converges if $a_n \downarrow 0$ | Alternating signs |

### Power Series

$$\sum_{n=0}^{\infty} c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

**Radius of convergence:** $R = 1/\limsup |c_n|^{1/n}$

**Common Taylor series:**

| Function | Series | Radius |
|----------|--------|--------|
| $e^x$ | $\sum_{n=0}^\infty \frac{x^n}{n!}$ | $\infty$ |
| $\sin x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty \frac{(-1)^{n+1} x^n}{n}$ | $(-1,1]$ |
| $1/(1-x)$ | $\sum_{n=0}^\infty x^n$ | $(-1,1)$ |

---

## In Geodesy Context

### Spherical Harmonic Series

The gravitational potential:
$$V(r,\theta,\lambda) = \frac{GM}{r}\sum_{n=0}^{N}\sum_{m=0}^{n}\left(\frac{a}{r}\right)^n[\bar{C}_{nm}\cos m\lambda + \bar{S}_{nm}\sin m\lambda]\bar{P}_{nm}(\cos\theta)$$

**Convergence:** The series converges for $r > a$ (outside the source radius).

**Truncation:** EGM2008 uses $N_{max} = 2190$ (~9 km resolution), requiring ~4.8 million coefficients.

### Legendre Functions

**Associated Legendre functions** (orthogonal basis on the sphere):
$$\bar{P}_{nm}(\cos\theta) = \text{(normalized)}$$

**Recurrence relation** (used in computation):
$$(n-m+1)\bar{P}_{n+1,m} = (2n+1)\cos\theta\,\bar{P}_{nm} - (n+m)\bar{P}_{n-1,m}$$

### Taylor Series for Linearization

The pseudorange equation is nonlinear. Taylor series around approximate position:

$$\rho(\mathbf{x}) \approx \rho(\mathbf{x}_0) + \nabla\rho|_0 \cdot \Delta\mathbf{x} + \frac{1}{2}\Delta\mathbf{x}^T H \Delta\mathbf{x} + \cdots$$

Truncating after the first derivative → linearization → least squares.

### Fourier Series for Tidal Analysis

Tidal signals decompose into harmonic constituents:
$$y(t) = \sum_k [A_k \cos(\omega_k t) + B_k \sin(\omega_k t)]$$

Each $\omega_k$ corresponds to a known astronomical frequency (M₂, S₂, K₁, O₁, etc.).

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\sum ar^n = a/(1-r)$ | Geometric series sum | When $\|r\|<1$ |
| $e^x = \sum x^n/n!$ | Exponential series | Linearization |
| $R = 1/\lim\|c_n\|^{1/n}$ | Radius of convergence | Power series domain |
| $\sum \frac{x^n}{n!}$, $\sum \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | Taylor series | sin, cos |

---

## Related Concepts

- [[Limits and Continuity]] — Foundation for series convergence
- [[Derivatives]] — Taylor series built from derivatives
- [[Integrals]] — Series evaluation by integration
- [[Physical Geodesy]] — Spherical harmonic series

---

## Study Problems

1. **Recall:** Determine if $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges and find its sum ($\pi^2/6$).
2. **Application:** Compute $e^{-0.01}$ using the first 4 terms of its Taylor series. What is the relative error vs. the exact value?
3. **Derivation:** Derive the Taylor expansion of $\sin x$ up to $x^5$.
4. **Real-world:** EGM2008 uses spherical harmonics up to degree 2190. How many coefficients are there (approximately)? How does truncation at degree 180 limit resolution?

---

## Common Mistakes

1. **Confusing absolute and conditional convergence:** A series can converge but not absolutely.
2. **Forgetting the radius of convergence:** Taylor series may diverge for $|x| > R$.
3. **Truncating series too aggressively:** The remainder term $R_N$ must be small enough for the application.
4. **Mixing up Fourier series and Fourier transform:** Series for periodic functions; transform for non-periodic.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*