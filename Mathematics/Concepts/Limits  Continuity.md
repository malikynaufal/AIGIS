---
title: 4. Limits & Continuity
type: concept
subject: Mathematics
tags: [mathematics, calculus, statistics, aigis, geodesy-applied]
created: 2026-07-27
---

# 4. Limits & Continuity

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

The **limit** describes the value a function approaches as the input approaches some point. **Continuity** formalises the intuitive notion of "no jumps" — a function that is continuous everywhere can be drawn without lifting the pen. These two concepts are the foundation of calculus and are essential before studying derivatives and integrals; in geodesy, they underpin convergence proofs for least-squares iteration and numerical differentiation of observation functions.

$$\text{Limit: } \lim_{x \to a} f(x) = L \quad \Longleftrightarrow \quad \text{f(x) approaches L as x approaches a} $$## The Formal Definition of a Limit

### Intuitive Definition
As $x \to a$, the function $f(x) $approaches the value $L $written:

$$\lim_{x \to a} f(x) = L$$

### Epsilon-Delta Definition ($\varepsilon$–$\delta$)

The rigorous definition is:

$$\forall\, \varepsilon > 0,\; \exists\, \delta > 0 \text{ such that } 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$**Artinya** (meaning): For any desired "tolerance"$\varepsilon $around $L$(seberapun kecilnya), there exists a corresponding tolerance $\delta $around $a $such that whenever $x $is within $\delta $of $a$(but not equal to $a$),$f(x) $is within $\varepsilon $of $L$.

### One-Sided Limits (Limit Satu Sisi)

- **Left-hand limit**: $\lim_{x \to a^-} f(x) = L$— the value approached from the **left** (dari kiri).

- **Right-hand limit**:$\lim_{x \to a^+} f(x) = L$— the value approached from the **right** (dari kanan).

The two-sided limit exists **if and only if** both one-sided limits exist and are equal
:

$$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$$### Example: Epsilon-Delta Proof that $\lim_{x \to 3} (2x+1) = 7 $Let $\varepsilon > 0 $be given. We need $\delta > 0 $such that
:

$$0 < |x - 3| < \delta \implies |(2x+1) - 7| < \varepsilon$$

Observe:$|(2x+1)-7| = |2x-6| = 2|x-3| $.

Choose $\delta = \varepsilon/2$. Then:

$$|x-3| < \delta = \varepsilon/2 \implies 2|x-3| < \varepsilon \implies |(2x+1)-7| < \varepsilon \quad \checkmark$$## Continuity (Kekontinuan)

### Definition
A function $f $is **continuous at**$a$(kontinu pada $a$) if all three conditions are met:

1. $f(a) $is defined.
2.$\lim_{x \to a} f(x) $exists.
3.$\lim_{x \to a} f(x) = f(a)$.

$$\lim_{x \to a} f(x) = f(a)$$If any condition fails,$f $has a **discontinuity** (ketidakkontinuan) at $a$.

### Types of Discontinuities (Jenis Ketidakkontinuan)

| Type | Description | Example | Bahasa Indonesia |
|------|-------------|---------|------------------|
| **Removable** | Limit exists but $\neq f(a) $or $f(a) $undefined | $f(x) = \frac{x^2-1}{x-1} $at $x=1$ | Singularitas yang bisa dihilangkan |
| **Jump** | Left and right limits both exist but differ | Step function $u(t)$ | Lompatan |
| **Infinite** | Limit is $\pm\infty$ | $f(x) = 1/x $at $x=0$ | Tak hingga |
| **Oscillatory** | No limit — function oscillates infinitely | $f(x) = \sin(1/x) $near $x=0$ | Osilasi tak terhingga |

### Classes of Continuous Functions (Kelas Fungsi Kontinu)

All of the following are **continuous on their domains** (kontinu pada daerah definisinya):

- Polynomials

- Rational functions (kecuali di titik nol penyebut)

- Trigonometric functions ($\sin, \cos, \tan, \ldots$)

- Exponential and logarithmic functions

- Compositions, sums, products, quotients of continuous functions

### Intermediate Value Theorem (Teorema Nilai Antara / TVA)

If $f $is continuous on$[a, b] $and $N $is any value between $f(a) $and $f(b)$, then there exists at least one $c \in (a, b) $such that $f(c) = N$.

$$\text{Continuous on } [a,b],\; f(a) < N < f(b) \;\Longrightarrow\; \exists\, c \in (a,b): f(c) = N$$**Application: Root existence (keberadaan akar).** If $f(a) < 0 $and $f(b) > 0 $and $f $is continuous, then $\exists\, c \in (a,b) $with $f(c) = 0$. This justifies the **bisection method** (metode bagi dua) for root-finding — the fundamental convergence proof for numerical root-finders.

### Extreme Value Theorem (Teorema Nilai Ekstrim)

If $f $is continuous on a **closed interval**$[a, b]$, then $f $attains both an **absolute maximum** (nilai maksimum mutlak) and an **absolute minimum** (nilai minimum mutlak) on$[a, b]$. This justifies optimization problems over bounded domains — critical in constrained least-squares adjustment.

## L'Hôpital's Rule (Aturan L'Hôpital)

L'Hôpital's Rule evaluates limits of the indeterminate forms $\frac{0}{0} $(nol/nol) or $\frac{\infty}{\infty} $(tak hingga/tak hingga) by differentiating numerator and denominator separately:

$$\text{If } \lim_{x \to a} f(x) = 0 \text{ and } \lim_{x \to a} g(x) = 0 \;\; (\text{or both } \to \infty)$$$$

\text{and } \lim_{x \to a} \frac{f'(x)}{g'(x)} \text{ exists, then } \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} $$**Catatan penting** (important note): L'Hôpital's Rule applies **only** to indeterminate forms$0/0 $or $\infty/\infty$— applying it to a determinate form (misalnya$0/1$) gives the wrong answer.

### Examples (Contoh)

**Example 1:** $\lim_{x \to 0} \frac{\sin x}{x} = \frac{0}{0} $— apply L'Hôpital
:

$$\lim_{x \to 0} \frac{\cos x}{1} = 1$$

**Example 2:**$\lim_{x \to \infty} \frac{\ln x}{x} = \frac{\infty}{\infty} $— apply L'Hôpital
:

$$\lim_{x \to \infty} \frac{1/x}{1} = 0$$

**Example 3:** Multiple applications may be needed
:

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{0}{0} \xrightarrow{\text{L'Hôpital}} \frac{\sin x}{2x} = \frac{0}{0} \xrightarrow{\text{L'Hôpital}} \frac{\cos x}{2} = \frac{1}{2} $$

### Indeterminate Forms
Common indeterminate forms requiring manipulation before L'Hôpital can be applied (or requiring other techniques):

| Form | Strategy | Strategy | Bahasa Indonesia |
|------|---------|----------|------------------|
| $0 \cdot \infty$ | Rewrite as $\frac{0}{1/\infty} $or $\frac{\infty}{1/0} $ | Transform to$0/0 $or $\infty/\infty$ | Kalikan dengan kebalikan |
| $\infty - \infty$ | Common denominator / rationalization | Algebraic manipulation | Samakan penyebut |
| $0^0$, $1^\infty$, $\infty^0$ | Take logarithms:$\ln(f^g) = g \ln f$ | Logarithmic transformation | Eksponensiasi kembali |

**Aturan L'Hôpital** is also valid for one-sided limits and the $x \to \infty $case, provided the differentiability and limit existence conditions are satisfied.

## Where Geodesy Uses Limits & Continuity

| Application | Concept Used |
|-------------|-------------|
| Numerical differentiation of observation data | Limit definition of the derivative:$f'(x) \approx \frac{f(x+h)-f(x)}{h} $as $h \to 0$ |
| Convergence of least-squares iteration | Continuity of the objective function ensures iterative methods converge to the minimiser |
| Geoid height computation via spherical harmonics | The harmonic series converges as a limit (partial sum $\to $infinite series) |
| GPS baseline convergence criteria | Iterative solvers terminate when $\ |\mathbf{x}_{k+1} - \mathbf{x}_k\| < \varepsilon$— an $\varepsilon$-$\delta $idea in practice |
| Map projection scale at the pole limit | $\sec\phi \to \infty $as $\phi \to 90°$— studying asymptotic behaviour of the projection function |

**Konvergensi iterasi** least-squares adjustment (misalnya Gauss-Seidel, metode gradient descent) guarantees that if the objective function $S(\mathbf{x}) $is continuous and convex, the sequence $\{\mathbf{x}_k\} $produced by a gradient-based method converges to the unique minimiser $\hat{\mathbf{x}} $. This is a continuity argument at the core of computational geodesy.

## Formalising Convergence (Mengformalisasi Konvergensi)

A sequence $\{a_n\} $**converges** to $L $if
:

$$\forall\, \varepsilon > 0, \; \exists\, N \in \mathbb{N} \text{ such that } n > N \implies |a_n - L| < \varepsilon$$This is analogous in spirit to the epsilon-delta limit definition, but for sequences indexed by natural numbers rather than for inputs approaching a specific point. In geodesy, the iterates $\mathbf{x}_k $form a sequence; proving convergence means proving this $\varepsilon$ condition holds for the sequence of adjustments.

## Linked vault notes

- [[Least Squares Adjustment]]

- [[Mathematics MOC]]

---
*Maintained by AIGIS.*
