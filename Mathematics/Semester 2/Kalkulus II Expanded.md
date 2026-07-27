---
title: Semester 2 — Kalkulus II (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, calculus, semester-2, aigis, geodesy-applied]
---

# Semester 2 — Kalkulus II (Expanded)

**Course**: MGM211201 — Kalkulus II
**Credits**: 3 SKS
**Study time**: ~40 hours
**Prerequisites**: Kalkulus I

---

## Course Overview

Kalkulus II extends single-variable calculus to integration techniques, sequences/series, and applications. Students master methods of integration and learn to approximate functions using Taylor and power series.

---

## Syllabus

### Weeks 1-3: Advanced Integration Techniques

#### 1.1 Integration by Parts

$$\int u\,dv = uv - \int v\,du

$ $**LIATE Priority**: Logarithms > Inverse trig > Algebraic > Trig > Exponential

**Example**: $\int x e^x\,dx $: $ u=x $, $ dv=e^x dx $→$ xe^x - e^x + C $**Reduction formulas**

$ $\int \sin^n x\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int \sin^{n-2}x\,dx

$$

#### 1.2 Trigonometric Integrals

| Form | Strategy |
|------|----------|
| $\int \sin^m x\cos^n x\,dx $| If $ m $ odd: save one $\sin $, $\sin^2 = 1-\cos^2 $ |
| | If $ n $odd: save one $\cos $, $\cos^2 = 1-\sin^2 $ |
| | If both even: half-angle identities |
| $\int an^m x\sec^n x\,dx $| If $ n $ even: save $\sec^2 x $ |
| | If $ m $odd: save $\sec xan x $ |

#### 1.3 Trigonometric Substitution

| Radial expression | Substitution | Identity |
|-------------------|-------------|---------|
| $\sqrt{a^2-x^2} $|$ x = a\sinheta $|$ 1-\sin^2heta = \cos^2heta $ |
| $\sqrt{a^2+x^2} $|$ x = aanheta $|$ 1+an^2heta = \sec^2heta $ |
| $\sqrt{x^2-a^2} $|$ x = a\secheta $|$\sec^2heta-1 = an^2heta $ |

**Example**: $\int \frac{dx}{x^2\sqrt{4+x^2}} $

$ x = 2anheta $, $ dx = 2\sec^2heta\,dheta $, $\sqrt{4+x^2} = 2\secheta $

$ $\int \frac{2\sec^2heta\,dheta}{4an^2heta \cdot 2\secheta} = \int \frac{\secheta\,dheta}{4an^2heta} = \frac{1}{4}\int \frac{\cosheta}{\sin^2heta}\,dheta = -\frac{1}{4\sinheta}+C = -\frac{\sqrt{4+x^2}}{4x}+C

$$

### # 1.4 Partial Fractions

For $\frac{P(x)}{Q(x)} $ with $\deg P < \deg Q $:

1. Linear factors: $\frac{1}{(x-a)(x-b)} = \frac{A}{x-a}+\frac{B}{x-b} $ 2. Repeated linear: $\frac{1}{(x-a)^2} = \frac{A}{x-a}+\frac{B}{(x-a)^2} $ 3. Irreducible quadratic: $\frac{Ax+B}{x^2+bx+c} $**Example**: $\int \frac{x+1}{x^2(x-1)}\,dx $

$ $\frac{x+1}{x^2(x-1)} = \frac{A}{x}+\frac{B}{x^2}+\frac{C}{x-1} $$

$ x+1 = Ax(x-1)+B(x-1)+Cx^2 $-$ x=0 $: $ 1 = B(-1) $→$ B=-1 $-$ x=1 $: $ 2 = C $→$ C=2 $-$ x^2 $coeff: $ A+C=0 $→$ A=-2 $

$ $= -2\ln|x| + \frac{1}{x} + 2\ln|x-1| + C

$$

Weeks 4-5: Improper Integrals

#### 2.1 Infinite Integral
s

$ $## Weeks 4-5: Improper Integrals

#### 2.1 Infinite Integral
s\int_1^{\infty} \frac{1}{x^p}\,dx = \begin{cases} \frac{1}{p-1} & p>1 \\ ext{diverges} & p\leq 1 \end{cases}$$

# ## Weeks 4-5: Improper Integrals

#### 2.1 Infinite Integral
s\int_1^{\infty} \frac{1}{x^p}\,dx = \begin{cases} \frac{1}{p-1} & p>1 \\ ext{diverges} & p\leq 1 \end{cases}**Comparison test**: If $ 0 \leq f(x) \leq g(x) $ and $\int g $ converges →$\int f $ converges.

#### 2.2 Discontinuous Integrands

$ $\int_0^1 \frac{1}{\sqrt{x}}\,dx = [2\sqrt{x}]_0^1 = 2

$$(convergent)$ $\int_0^1 \frac{1}{x}\,dx = [\ln|x|]_0^1 = \infty

$$

(divergent)

### Weeks 6-8: Sequences and Series

#### 3.1 Sequences

A sequence $\\{a_n\\} $**converges** if $\lim_{no\infty} a_n = L $ exists.

**Monotone Convergence Theorem**: Bounded monotone sequences converge.

#### 3.2 Serie
s

$ $\sum_{n=1}^{\infty} a_n = \lim_{No\infty} S_N, \\quad S_N = \sum_{n=1}^N a_n

$$**Nth term test**: If $\lim a_n \neq 0 $, the series diverges.

#### 3.3 Geometric Series

$ $\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r} \\quad (|r|<1)

$$**Diverges** when $|r| \geq 1 $.

#### 3.4 Telescoping Series

$ $\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}\right) =
1

$$3.5 p-Series$ $

# 3.5 p-Series

### # 3.5 p-Series\sum_{n=1}^{\infty} \frac{1}{n^p} \begin{cases} ext{converges} & p>1 \\ ext{diverges} & p\leq 1 \end{cases}

$$

### # 3.6 Comparison Tests

**Direct**: If $ 0 \leq a_n \leq b_n $and $\sum b_n $ converges →$\sum a_n $ converges

**Limit**: $\lim \frac{a_n}{b_n} = L $, $ 0 < L < \infty $→ same convergence

### Weeks 9-10: Convergence Tests

#### 4.1 Integral Test

If $ f $is positive, continuous, decreasing with $ f(n)=a_n $:

$ $\sum a_n ext{ and } \int_1^{\infty} f(x)\,dx ext{ both converge or both diverge
}

$$4.2 Ratio Test$ $

# 4.2 Ratio Test

### # 4.2 Ratio Test\rho = \lim_{no\infty} \frac{a_{n+1}}{a_n}

$$-$\rho < 1 $: converges

- $\rho > 1 $: diverges

- $\rho = 1 $: inconclusive

**Best for**: factorials, exponentials.

#### 4.3 Root Test

$ $\rho = \lim_{no\infty} |a_n|^{1/n} $$

Same rules as ratio test.

#### 4.4 Alternating Series Test $\sum (-1)^{n+1}b_n $ converges if:
1.$ b_{n+1} \leq b_n $for all $ n $ 2.$\lim b_n = 0 $**Error bound**: $|S-S_N| \leq b_{N+1} $#### 4.5 Absolute vs Conditional Convergence

-$\sum |a_n| $ converges →$\sum a_n $**absolutely** convergent (converges!)
-$\sum a_n $ converges but $\sum |a_n| $ diverges → **conditionally** convergent

**Riemann rearrangement theorem**: Conditionally convergent series can be rearranged to converge to ANY value.

### Weeks 11-12: Power Series and Taylor Series

#### 5.1 Power Serie
s

$ $\sum_{n=0}^{\infty} c_n(x-a)^n

$$**Radius of convergence**: $ R = 1/\lim|c_{n+1}/c_n|$ (ratio test)

Converges absolutely on $ (a-R, a+R) $, needs checking at endpoints.

#### 5.2 Taylor Series

$ $f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n $$

### # 5.3 Common Taylor Series

| $ f(x) $ | Expansion | Radius |
|---------|-----------|--------|
| $ e^x $ | $ 1+x+x^2/2!+x^3/3!+\cdots $ | $\infty $ |
| $\sin x $|$ x-x^3/3!+x^5/5!-\cdots $|$\infty $ |
| $\cos x $|$ 1-x^2/2!+x^4/4!-\cdots $|$\infty $ |
| $\ln(1+x) $|$ x-x^2/2+x^3/3-\cdots $ | 1 |
| $\frac{1}{1-x} $|$ 1+x+x^2+x^3+\cdots $ | 1 |
| $\\arctan x $|$ x-x^3/3+x^5/5-\cdots $ | 1 |

#### 5.4 Taylor's Theorem with Remainde
r

$ $f(x) = T_n(x) + R_n(x)$$

where $ T_n $ is the $n $ th degree Taylor polynomial and:$ $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

for some $ c $ between $a $ and $x $.

### Week 13: Applications of Series

#### 6.1 Approximation
**Example**: $ e^{0.1} \approx 1 + 0.1 + 0.01/2 + 0.001/6 \approx 1.10517 $**Error**: $|R_3| \leq \frac{e^{0.1}}{24}(0.1)^4 < 10^{-5} $#### 6.2 Indeterminate Forms and L'Hôpital
Using series to evaluate limits

$ $\lim_{xo 0}\frac{e^x-1-x}{x^2} = \lim_{xo 0}\frac{(1+x+x^2/2+\cdots)-1-x}{x^2} = \lim_{xo 0}\frac{x^2/2+\cdots}{x^2} = \frac{1}{2}

$$6.3 Definite Integral
s$ $

# 6.3 Definite Integral
s

### # 6.3 Definite Integral
s\int e^{-x^2}\,dx = \int\left(1-x^2+\frac{x^4}{2!}-\cdots\right)dx = x - \frac{x^3}{3}+\frac{x^5}{10}-\cdots

$$

---

## Worked Examples

### Example 1: Partial Fractions
Evaluate $\int \frac{2x+3}{x^2+2x-3}\,dx $.

$ x^2+2x-3=(x+3)(x-1) $

$\frac{2x+3}{(x+3)(x-1)} = \frac{A}{x+3}+\frac{B}{x-1} $

$ 2x+3=A(x-1)+B(x+3) $

$ x=1 $: $ 5=4B $→$ B=5/4 $

$ x=-3 $: $-3=-4A $→$ A=3/4 $

$ $= \frac{3}{4}\ln|x+3|+\frac{5}{4}\ln|x-1|+C

$$

### Example 2: Alternating Series Error
Estimate $\sum_{n=0}^{\infty} \frac{(-1)^n}{n!} $ to within 0.001.$ S = e^{-1} \approx 0.3679 $

$ S \approx 1 - 1 + 1/2 - 1/6 + 1/24 - 1/120 + 1/720 $Error $\leq |a_7| = 1/5040 \approx 0.000198 < 0.001 $✓

### Example 3: Radius of Convergence
Find the radius of convergence of $\sum_{n=1}^{\infty} \frac{n^n}{n!}x^n $.

$\rho = \lim \frac{(n+1)^{n+1}/(n+1)!}{n^n/n!} \cdot |x| = \lim \frac{(n+1)^n}{n^n}|x| = e|x| $ Converges when $e |x| < 1 $→$ R = 1/e $.

---

## Practice Problems

### Integration
1. $\int x^2 e^x\,dx $ 2.$\int \sin^4 x\,dx $ 3.$\int \frac{x}{(x-1)(x-2)(x-3)}\,dx $ 4.$\int_0^{\infty} xe^{-x}\,dx $### Series
1.$\sum_{n=1}^{\infty} \frac{n^2}{3^n} $ (ratio test)
2.$\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}} $ (AST)
3.$\sum_{n=1}^{\infty} \frac{n!}{n^n} $ (ratio test)
4.$\sum_{n=1}^{\infty} \frac{(-1)^n n^3}{n^4+1} $ (conditional?)

### Taylor Series
1. Write $ e^{-x^2} $as a Taylor series at $ x=0 $2. Find the first 4 nonzero terms of $\cos(x^2) $ 3. Approximate $\int_0^1 e^{-x^2}\,dx$ using series

---

## Geodesy Connections

- **Power series**: Approximating functions in geodetic computations

- **Taylor linearization**: Nonlinear adjustment models

- **Error bounds**: Series truncation errors

---

## References

- OpenStax Calculus Vol. 2 (Chapters 1-5)

- MIT OCW 18.01: Single Variable Calculus (Lecture 25+)

- Stewart, J. *Calculus: Early Transcendentals* (Chapters 7-11)

---

➡️ [[Mathematics MOC]] | ➡️ [[Kalkulus I Expanded]] | ➡️ [[Differential Equations intro]]