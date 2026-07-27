---
title: 4. Integrals (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, calculus, integrals, aigis, geodesy-applied]
---

# 4. Integrals (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Integration is the process of finding antiderivatives and computing areas, volumes, and other accumulations. It is the inverse operation of differentiation and essential for physics, engineering, and statistics.

## 1. Core Definitions

### 1.1 Indefinite Integral

The antiderivative (indefinite integral) of $f(x)$is:$$\int f(x)\,dx = F(x) + C$$where$F'(x) = f(x)$and$C$is the constant of integration.

### 1.2 Definite Integral

The definite integral from$a$to$b$is:$$\int_a^b f(x)\,dx = F(b) - F(a)$$This represents the signed area under$f(x)$from$x = a$to$x = b$.

## 2. Fundamental Theorem of Calculus (FTC)

### Part 1

If $f$is continuous on$[a,b]$and$F(x) = \int_a^x f(t)\,dt$, then:
$$

\frac{d}{dx}\left(\int_a^x f(t)\,dt\right) = f(x)$$### Part 2$$\int_a^b f(x)\,dx = F(b) - F(a)$$**Proof of FTC Part 1**: Let$F(x) = \int_a^x f(t)\,dt$. Then:
$$

F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h} = \lim_{h \to 0} \frac{1}{h}\int_x^{x+h} f(t)\,dt$$By Mean Value Theorem for Integrals,$\int_x^{x+h} f(t)\,dt = f(c) \cdot h$for some$c \in [x, x+h]$.
$$

F'(x) = \lim_{h \to 0} f(c) = f(x) \quad \blacksquare$$## 3. Basic Integration Formulas

| Function                 | Integral                  |     |     |
| ------------------------ | ------------------------- | --- | --- |
|$x^n$ ($n \neq -1$)      | $\frac{x^{n+1}}{n+1} + C$|     |     |
|$\frac{1}{x}$|$ln+ C$|     |     |
|$e^x$|$e^x + C$|     |     |
|$\sin x$|$-\cos x + C$|     |     |
|$\cos x$|$\sin x + C$|     |     |
|$\sec^2 x$|$\tan x + C$|     |     |
|$\csc^2 x$|$-\cot x + C$|     |     |
|$\sec x \tan x$|$\sec x + C$|     |     |
|$\frac{1}{\sqrt{1-x^2}}$|$\arcsin x + C$|     |     |
|$\frac{1}{1+x^2}$|$\arctan x + C$|     |     |
|$\sinh x$|$\cosh x + C$|     |     |
|$\cosh x$|$\sinh x + C$|     |     |

## 4. Integration Techniques

### 4.1$u$-Substitution

If $\int f(g(x))g'(x)\,dx$, let $u = g(x)$:
$$

\int f(g(x))g'(x)\,dx = \int f(u)\,du$$**Example**: Evaluate$\int x\cos(x^2)\,dx$Let$u = x^2$, $du = 2x\,dx$, so $x\,dx = \frac{du}{2}$
$$

\int x\cos(x^2)\,dx = \frac{1}{2}\int \cos u\,du = \frac{1}{2}\sin(x^2) + C$$### 4.2 Integration by Parts$$\int u\,dv = uv - \int v\,du$$**Strategy**: Choose$u$using LIATE (Logs, Inverse trig, Algebraic, Trig, Exponential).

**Example**: Evaluate$\int x e^x\,dx$Let$u = x$, $dv = e^x dx$, so $du = dx$, $v = e^x$
$$

\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1) + C$$### 4.3 Partial Fractions

For rational functions$\frac{P(x)}{Q(x)}$where$\deg P < \deg Q$:

1. Factor $Q(x)$completely
2. Decompose based on factors
3. Integrate term by term

**Example**: Evaluate$\int \frac{2x+3}{x^2+x-2}\,dx$Factor:$x^2 + x - 2 = (x+2)(x-1)$
$$

\frac{2x+3}{(x+2)(x-1)} = \frac{A}{x+2} + \frac{B}{x-1}$$Solving:$2x+3 = A(x-1) + B(x+2)$-$x = -2$: $1 = A(-3)$→$A = -\frac{1}{3}$-$x = 1$: $5 = 3B$→$B = \frac{5}{3}$
$$

\int = -\frac{1}{3}\ln|x+2| + \frac{5}{3}\ln|x-1| + C$$### 4.4 Trigonometric Integrals

**Form$\int \sin^m x \cos^n x\,dx$:**

- If $m$odd: save one$\sin$, convert rest to $\cos$- If$n$odd: save one$\cos$, convert rest to $\sin$- If both even: use half-angle identities

**Form$\int \tan^m x \sec^n x\,dx$:**

- If $n$even: save$\sec^2$, convert rest to $\tan$- If$m$odd: save$\sec x \tan x$, convert rest to $\sec$### 4.5 Trigonometric Substitution

| Form | Substitution |
|------|-------------|
|$\sqrt{a^2 - x^2}$|$x = a\sin\theta$|
|$\sqrt{a^2 + x^2}$|$x = a\tan\theta$|
|$\sqrt{x^2 - a^2}$|$x = a\sec\theta$|

**Example**:$\int \frac{dx}{\sqrt{4 - x^2}}$Let$x = 2\sin\theta$, $dx = 2\cos\theta\,d\theta$
$$

\int \frac{2\cos\theta\,d\theta}{\sqrt{4-4\sin^2\theta}} = \int \frac{2\cos\theta\,d\theta}{2\cos\theta} = \int d\theta = \theta + C = \arcsin\left(\frac{x}{2}\right) + C$$## 5. Improper Integrals

### Type 1: Infinite Limits$$\int_a^{\infty} f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx$$**Example**:$\int_1^{\infty} \frac{1}{x^2}\,dx = \lim_{b \to \infty} \left[-\frac{1}{x}\right]_1^b = \lim_{b \to \infty}\left(-\frac{1}{b} + 1\right) = 1$(converges)

### Type 2: Discontinuous Integrand$$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{a \to 0^+} \int_a^1 x^{-1/2}\,dx = \lim_{a \to 0^+} [2\sqrt{x}]_a^1 = 2$$## 6. Applications

### 6.1 Area Between Curves$$A = \int_a^b |f(x) - g(x)|\,dx$$### 6.2 Volume of Revolution

**Disk Method**:$V = \pi \int_a^b [R(x)]^2\,dx$**Washer Method**:$V = \pi \int_a^b ([R(x)]^2 - [r(x)]^2)\,dx$**Shell Method**:$V = 2\pi \int_a^b x \cdot f(x)\,dx$### 6.3 Arc Length$$L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$$### 6.4 Surface Area of Revolution$$S = 2\pi \int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx$$### 6.5 Work$$W = \int_a^b F(x)\,dx$$### 6.6 Average Value$$f_{\text{avg}} = \frac{1}{b-a}\int_a^b f(x)\,dx$$## 7. Practice Problems

### Problem 1
Evaluate$\int x\sqrt{1+x^2}\,dx$**Solution**: Let$u = 1+x^2$, $du = 2x\,dx$
$$

\int x\sqrt{1+x^2}\,dx = \frac{1}{2}\int u^{1/2}\,du = \frac{1}{2}\cdot\frac{2}{3}u^{3/2}+C = \frac{1}{3}(1+x^2)^{3/2}+C$$### Problem 2
Evaluate$\int \ln x\,dx$**Solution**: Integration by parts,$u = \ln x$, $dv = dx$
$$

\int \ln x\,dx = x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - x + C$$### Problem 3
Find the volume of the solid formed by rotating$y = x^2$around the$x$-axis from $x=0$to$x=2$.

**Solution**: Disk method
$$

V = \pi\int_0^2 (x^2)^2\,dx = \pi\int_0^2 x^4\,dx = \pi\left[\frac{x^5}{5}\right]_0^2 = \frac{32\pi}{5}$$### Problem 4
Evaluate$\int_0^1 \frac{x}{\sqrt{1+x^2}}\,dx$**Solution**:$u = 1+x^2$, $du = 2x\,dx$
$$

\int = \frac{1}{2}\int_1^2 u^{-1/2}\,du = [\sqrt{u}]_1^2 = \sqrt{2} - 1$$## 8. Where Geodesy Uses This

- **Computing areas** from DTM data

- **Probability** from density functions:$P(a < X < b) = \int_a^b f(x)\,dx$

- **Volume calculations** for earth segments

- **Signal processing** via Fourier transforms

- **Error propagation** through integration of variances

## 9. References

- OpenStax Calculus Vol. 1, Chapter 4-7

- MIT OCW 18.01: Single Variable Calculus

- Stewart, J. (2015). *Calculus: Early Transcendentals*

---

*Maintained by AIGIS.*
