---
title: Semester 1 — Kalkulus I (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, calculus, semester-1, aigis, geodesy-applied]
---

# Semester 1 — Kalkulus I (Expanded)

**Course**: MGM211101 — Kalkulus I
**Credits**: 3 SKS
**Study time**: ~40 hours
**Prerequisites**: High school algebra, trigonometry

---

## Course Overview

Kalkulus I covers the fundamental concepts of single-variable calculus: limits, continuity, derivatives, and basic applications. This is the foundation for all advanced mathematics in the geodesy curriculum.

---

## Week-by-Week Syllabus

### Weeks 1-2: Functions and Limits

#### 1.1 Functions Review

- Domain, range, piecewise functions

- Transformations: shift, stretch, reflect

- Inverse functions

- Exponential and logarithmic functions

#### 1.2 Limits
**Definition**: $\lim_{x o a} f(x) = L $ means $ f(x) $ can be made arbitrarily close to $  L $ by taking $  x $ sufficiently close to $  a $.

**Properties**:

- $\lim [f+g] = \lim f + \lim g $-$\lim [f\cdot g] = (\lim f)(\lim g) $-$\lim [f/g] = (\lim f)/(\lim g) $ if $\lim g \neq 0 $**Techniques**:

- Direct substitution

- Factoring and canceling

- Rationalizing

- Squeeze theorem

- Limits at infinity

**Key Limits**

$ $\lim_{x o 0} \frac{\sin x}{x} = 1, \\quad \lim_{x o 0} \frac{e^x - 1}{x} = 1

$ $### # 1.3 Continuity $  f $ is continuous at $  a $ if:
1.$ f(a) $ exists
2.$\lim_{x o a} f(x) $ exists
3.$\lim_{x o a} f(x) = f(a) $**Intermediate Value Theorem**: If $  f $ is continuous on $ [a,b] $ and $ f(a) < N < f(b) $, then $\\exists c \in (a,b): f(c) = N $.

### Weeks 3-5: Derivatives

#### 2.1 Definition of Derivative

$ $ f'(x) = \lim_{h o 0} \frac{f(x+h) - f(x)}{h}$ $**Interpretations**:

- Slope of tangent line

- Instantaneous rate of change

#### 2.2 Differentiation Rules
| Rule | Formula |
|------|---------|
| Power | $ (x^n)' = nx^{n-1} $ |
| Constant | $ (c)' = 0 $ |
| Sum | $ (f+g)' = f'+g'$ |
| Product | $ (fg)' = f'g+fg'$ |
| Quotient | $ (f/g)' = (f'g-fg')/g^2 $ |
| Chain | $ (f\circ g)' = f'(g)\cdot g'$ |

#### 2.3 Derivatives of Transcendental Functions
| Function | Derivative |
| ------------ | ----------------- |
| $\sin x $|$\cos x $ |
| $\cos x $|$-\sin x $ |
| $ an x $|$\sec^2 x $ |
| $ e^x $ | $ e^x $ |
| $\ln x $|$ 1/x $ |
| $\\arcsin x $|$ 1/\sqrt{1-x^2} $ |
| $\\arctan x $|$ 1/(1+x^2) $ |

#### 2.4 Implicit Differentiation
Differentiate both sides of an equation treating $ y $ as function of $  x $.

**Example**: $ x^2 + y^2 = 25 $→$ 2x + 2yy' = 0 $→$ y' = -x/y $#### 2.5 Higher-Order Derivatives $ f''(x) $, $ f'''(x) $, $ f^{(n)}(x) $— used in Taylor series and concavity.

#### 2.6 Related Rates
1. Identify variables and given rates
2. Write equation relating them
3. Differentiate wrt time
4. Substitute known values

**Example**: Ladder sliding down wall

### Weeks 6-8: Applications of Derivatives

#### 3.1 Extrema

- **Fermat's Theorem**: If $ f $ has local extremum at $  c $ and $ f'(c) $ exists, then $ f'(c) = 0 $.

- **Critical numbers**: $ f'(c) = 0 $ or $ f'(c) $ DNE

#### 3.2 Mean Value Theorem
If $ f $ continuous on $ [a,b] $ and differentiable on $ (a,b) $:

$ $\\exists c \in (a,b): f'(c) = \frac{f(b)-f(a)}{b-a} $ $

### # 3.3 First Derivative Test
-$ f'$ changes $+$ to $-$→ local max
-$ f'$ changes $-$ to $+$→ local min

#### 3.4 Second Derivative Test
-$ f''(c) > 0 $ and $ f'(c)=0 $→ local min
-$ f''(c) < 0 $ and $ f'(c)=0 $→ local max

#### 3.5 Curve Sketching
1. Domain
2. Intercepts
3. Symmetry (even/odd/periodic)
4. Asymptotes
5. Intervals of increase/decrease
6. Local extrema
7. Concavity and inflection points
8. Sketch

#### 3.6 Optimization Problems

- Translate word problem to math

- Find objective function and constraints

- Use derivative to find extremum

- Check endpoints

#### 3.7 Newton's Metho
d

$ $ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ $

#### 3.8 L'Hôpital's Rule
For $\frac{0}{0} $ or $\frac{\infty}{\infty} $:

$ $\lim \frac{f}{g} = \lim \frac{f'}{g'} $ $

### Weeks 9-12: Integrals

#### 4.1 Antiderivatives $ F' = f $→$  F $ is antiderivative of $  f $.
General antiderivative: $ F(x) + C $#### 4.2 Indefinite Integral
s

$ $\int f(x)\,dx = F(x) + C

$ $

Basic formulas: $\int x^n = x^{n+1}/(n+1) $,$\int e^x = e^x $,$\int \sin x = -\cos x $, etc.

#### 4.3 Riemann Sums and Definite Integrals

$ $\int_a^b f(x)\,dx = \lim_{n o \infty} \sum_{i=1}^n f(x_i^*)\Delta x

$ $

### # 4.4 Fundamental Theorem of Calculus
**Part 1**: $\frac{d}{dx}\int_a^x f(t)\,dt = f(x) $**Part 2**: $\int_a^b f(x)\,dx = F(b) - F(a) $ where $ F' = f $#### 4.5 Substitution Rul
e

$ $\int f(g(x))g'(x)\,dx = \int f(u)\,du \\quad (u = g(x))

$ $

Weeks 13-14: Applications of Integrals

#### 5.1 Area Between Curve
s

$ $## Weeks 13-14: Applications of Integrals

#### 5.1 Area Between Curve
sA = \int_a^b |f(x) - g(x)|\,dx $ $

# ## Weeks 13-14: Applications of Integrals

#### 5.1 Area Between Curve
sA = \int_a^b |f(x) - g(x)|\,dx

#### 5.2 Volumes
**Disk**: $ V = i\int_a^b [R(x)]^2\,dx $**Washer**: $  V = i\int_a^b ([R(x)]^2 - [r(x)]^2)\,dx $**Shell**: $  V = 2i\int_a^b x\cdot f(x)\,dx $#### 5.3 Wor
k

$ $  W = \int_a^b F(x)\,dx $ $

---

## Worked Examples

### Example 1: Limit
Find $\lim_{x o 0} \frac{\sin 3x}{\sin 5x} $.

**Solution**:

$ $\lim_{x o 0} \frac{3x}{5x} \cdot \frac{\sin 3x}{3x} \cdot \frac{5x}{\sin 5x} = \frac{3}{5} \cdot 1 \cdot 1 = \frac{3}{5} $ $

### Example 2: Optimization
Find the dimensions of a cylinder with volume 1000 cm³ that minimizes surface area.

**Solution**: $ V = i r^2 h = 1000 $, so $  h = 1000/(i r^2) $
$ S = 2i r^2 + 2i r h = 2i r^2 + 2000/r $
$ S' = 4i r - 2000/r^2 = 0 $→$ r^3 = 500/i $→$  r \approx 5.42 $ cm $  h = 1000/(i r^2) \approx 10.84 $ cm

### Example 3: Definite Integral
Evaluate $\int_0^{i/2} \sin^3 x \cos^2 x\,dx $.

**Solution**:
$\int \sin^3 x \cos^2 x\,dx = \int \sin x (1-\cos^2 x) \cos^2 x\,dx $ Let $  u = \cos x $, $ du = -\sin x\,dx $
$= -\int (1-u^2)u^2\,du = -\int (u^2 - u^4)\,du = -\frac{u^3}{3} + \frac{u^5}{5} $
$= -\frac{\cos^3 x}{3} + \frac{\cos^5 x}{5} $ From 0 to $ i/2 $: $ [0] - [-\frac{1}{3} + \frac{1}{5}] = \frac{1}{3} - \frac{1}{5} = \frac{2}{15} $---

## Practice Problems

### Problem Set 1: Limits
1.$\lim_{x o 2} \frac{x^2-4}{x-2} $ 2.$\lim_{x o \infty} \frac{3x^2+2x+1}{5x^2-7} $ 3.$\lim_{x o 0} \frac{e^x - 1 - x}{x^2} $### Problem Set 2: Derivatives
1.$ y = x^2\sin x + e^x\ln x $ 2.$  y = \frac{an x}{1+x^2} $ 3.$  y = (\sin x)^x $ (logarithmic differentiation)

### Problem Set 3: Applications
1. Find absolute extrema of $ f(x) = x^3 - 3x^2 + 1 $ on $ [-1, 4] $ 2. A farmer has 2400 ft of fencing. What is the largest rectangular area that can be enclosed?
3. Find the maximum volume of a box made by cutting squares from a 12×12 sheet and folding.

### Problem Set 4: Integrals
1.$\int (3x^2 - 2/x + \sin x)\,dx $ 2.$\int x\cos(x^2)\,dx $ 3.$\int_0^1 x\sqrt{1-x^2}\,dx $---

## Key Formulas Summary

| Topic | Formula |
|-------|---------|
| Derivative def. | $ f'(x) = \lim_{ho0}(f(x+h)-f(x))/h $ |
| Chain rule | $ (f\circ g)' = f'(g)\cdot g'$ |
| Product rule | $ (uv)' = u'v + uv'$ |
| Quotient rule | $ (u/v)' = (u'v-uv')/v^2 $ |
| FTC | $\int_a^b f = F(b)-F(a) $ |
| Substitution | $\int f(g(x))g'(x)dx = \int f(u)du $ |
| MVT | $ f'(c) = (f(b)-f(a))/(b-a) $ |
| Newton | $ x_{n+1} = x_n - f(x_n)/f'(x_n)$ |

---

## Geodesy Connections

- **Limits**: Convergence of iterative solutions in least squares

- **Derivatives**: Jacobian matrix in adjustment (design matrix)

- **Optimization**: Minimizing sum of squared residuals

- **Integrals**: Area/volume computations from DTMs

---

## References

- OpenStax Calculus Vol. 1 (Chapters 1-5)

- MIT OCW 18.01: Single Variable Calculus

- Stewart, J. *Calculus: Early Transcendentals* (Chapters 1-6)

---

➡️ [[Mathematics MOC]] | ➡️ [[Kalkulus II]] | ➡️ [[Derivatives]] | ➡️ [[Integrals]]