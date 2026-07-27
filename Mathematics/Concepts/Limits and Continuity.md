---
tags: [math, calculus, derivatives, limits, analysis, continuity]
aliases: [Limits and Continuity, epsilon-delta]
created: 2026-7-13
updated: 2026-07-27
---

# Limits and Continuity

> *"The rigorous foundation of calculus that bridges algebraic intuition with analytical precision."*

---

## 1. Definition of Limit (ε-δ Definition)

For functions of a real variable, the limit describes behavior as the input approaches a value:

$$\lim_{x \to c} f(x) = L

$ $**Formal ε-δ definition:** For every $\varepsilon > 0 $, there exists $\delta > 0 $ such that: $ $|x - c| < \delta \implies |f(x) - L| < \varepsilon

$$

# ## Visual Interpretation

- As $ x $ gets closer to $  c $ (within $\delta $),
- $ f(x) $ gets closer to $  L $ (within $\varepsilon $)
- Both $\varepsilon $ and $\delta $ are positive real numbers

---

## 2. Key Limit Properties

| Property | Formula | Note |
|----------|---------|------|
| Sum/Difference | $\lim_{x \to c} [f(x) \pm g(x)] = \lim f \pm \lim g $ | Requires both limits exist |
| Scalar multiplication | $\lim_{x \to c} [k f(x)] = k \lim f(x) $| $  k $ constant |
| Product | $\lim_{x \to c} [f(x) \cdot g(x)] = \lim f \cdot \lim g $ |
| Quotient | $\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim f}{\lim g} $| $ g(x) \neq 0 $ |
| Power | $\lim_{x \to c} [f(x)]^n = [\lim f(x)]^n $| $  n $ integer |

---

## 3. Classic Limits

### 3.1 Polynomial and Rational Functions

$ $\lim_{x \to c} f(x) = f(c) \quad (\text{continuity at } c)

$$

# ## 3.2 Trigonometric Limits $ $\lim_{x \to 0} \frac{\sin x}{x} = 1

$$

$ $\lim_{x \to 0} \frac{\tan x}{x} = 1

$$

$ $\lim_{x \to 0} \frac{\sin kx}{x} = k

$$

# ## 3.3 Exponential and Logarithmic $ $\lim_{x \to 0} \frac{e^x - 1}{x} = 1

$$

$ $\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1

$$

---

## 4. Continuity

A function $ f $ is **continuous at $  c $** if:

1. $ f(c) $ is defined
2. $\lim_{x \to c} f(x) $ exists
3. $\lim_{x \to c} f(x) = f(c) $

### Continuity Properties

| Property | Explanation |
|----------|-------------|
| Sum/Composition | Continuous functions remain continuous |
| Inverse | Continuous and strictly monotonic → invertible continuous |
| Extreme Value Theorem | Continuous on $ [a,b] $ → has max/min |
| Intermediate Value Theorem | Continuous on $ [a,b] $, $ f(a) \cdot f(b) < 0 $ → has root |

---

## 5. Important Theorems

### 5.1 Intermediate Value Theorem (IVT)

If $ f $ is continuous on $ [a,b] $ and $  y $ lies between $ f(a) $ and $ f(b) $, then there exists $  c \in (a,b) $ such that $ f(c) = y $.

### 5.2 Mean Value Theorem (MVT)

If $ f $ is continuous on $ [a,b] $ and differentiable on $ (a,b) $, then there exists $  c \in (a,b) $ such that:

$ $ f'(c) = \frac{f(b) - f(a)}{b - a}$$

# ## 5.3 L'Hôpital's Rule

For $\frac{0}{0} $ or $\frac{\infty}{\infty} $ indeterminate forms: $ $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}

$$

*Provided the right-hand limit exists.*

---

## 6. One-Sided Limits

### 6.1 Definition

- **Left-hand:** $\lim_{x \to c^-} f(x) $ (approach from values $  x < c $)
- **Right-hand:** $\lim_{x \to c^+} f(x) $ (approach from values $  x > c $)

### 6.2 Existence Conditions

$ $\lim_{x \to c} f(x) \text{ exists } \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L

$$

---

## 7. Infinite Limits and Asymptotes

### 7.1 Vertical Asymptotes

$ $\lim_{x \to c} f(x) = \pm\infty \iff x = c \text{ is a vertical asymptote}

$$

# ## 7.2 Horizontal Asymptotes $ $\lim_{x \to \pm\infty} f(x) = L \iff y = L \text{ is a horizontal asymptote}

$$

# ## 7.3 Slant (Oblique) Asymptotes

For rational functions where degree numerator = degree denominator + 1:

$ $  y = mx + b \text{ where } m = \frac{\text{leading coeff. numerator}}{\text{leading coeff. denominator}}$$

---

## 8. Sequences and Their Limits

### 8.1 Sequence Definition

A sequence $ a_n $ converges to $  L $ if:

$ $\lim_{n \to \infty} a_n = L

$$

# ## 8.2 Monotone Convergence Theorem

- If $ a_n $ is bounded and monotonic ( $ a_{n+1} \geq a_n $), then it converges
- If $ a_n $ is bounded above but decreasing, or bounded below but increasing, limit exists

### 8.3 Squeeze (Sandwich) Theorem

If $ g(n) \leq f(n) \leq h(n) $ and $\lim g(n) = \lim h(n) = L $, then $\lim f(n) = L $.

---

## 9. Derivatives and First Principles

The derivative connects limits with rates of change:

$ $ f'(c) = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h}$$

This limit must exist for the derivative to exist.

---

## 10. Why This Matters in Engineering

| Application | Limit/Continuity Role |
|-------------|----------------------|
| Signal Processing | Sampling theorem and reconstruction |
| Control Systems | Stability analysis and pole locations |
| Numerical Methods | Convergence of iterative algorithms |
| Optimization | Gradient-based methods require differentiability |
| Error Analysis | Understanding how small changes affect systems |

---

## 11. Mathematical Tools

### 11.1 Taylor Series Expansion

Continuity allows approximation by polynomials:

$ $ f(x) = f(c) + f'(c)(x-c) + \frac{f''(c)}{2!}(x-c)^2 + \cdots $$

# ## 11.2 Practical Epsilon-Delta

For practical engineering tolerances:

- Choose $\delta $ based on required precision $\varepsilon $- Use Lipschitz continuity: $|f(x) - f(y)| \leq L|x - y|$

---

## 12. Cross-References

- See also: [[Derivatives]], [[Continuity of Functions]], [[Fourier Analysis]]
- Geodesy context: [[Coordinate System Transformations]], [[Error Propagation]]

---

## 13. References

- Bartle, R. G. & Sherbert, D. R. (2011). *Introduction to Real Analysis*. Wiley.
- Rudin, W. (1976). *Principles of Mathematical Analysis*. McGraw-Hill.
- Spivak, M. (1994). *Calculus on Manifolds*. Addison-Wesley.

Page last updated: 2026-07-27 | AIGIS Content™
