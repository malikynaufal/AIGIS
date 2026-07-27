---
code: FKD211202
name: Kalkulus II
SKS: 3
semester: 2
department: Matematika
tags: [mathematics, calculus, series, multivariable]
created: 2026-07-27
---

# FKD211202 — Kalkulus II

## Course Overview

Kalkulus II extends single-variable calculus into infinite series, parametric curves, and an introduction to multivariable calculus — essential tools for describing electromagnetic fields, oscillatory motion, and statistical distributions in physics.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Kalkulus I, Fisika Dasar I
**Co-requisites:** Fisika Dasar II

---

## 📋 Topics & Outline

### Unit 1: Sequences and Limits (Weeks 1–4)

- Sequences: convergence, divergence, monotonic sequences

- **Limit of a sequence:** lim_{n→∞} a_n = L

- Squeeze theorem for sequences

- **Infinite sequences:** a_n = n/(n+1), a_n = (1+1/n)ⁿ → e

- **Monotone Convergence Theorem** and the number e

### Unit 2: Infinite Series (Weeks 5–9)

- **Series notation:** Σ_{n=1}∞ a_n, partial sums S_N = Σ_{n=1}^{N} a_n

- **Convergence tests:**
 - Divergence test (nth term test)
 - Integral test
 - Comparison test and Limit comparison test
 - Ratio test: lim |a_{n+1}/a_n| = L
 - Root test: lim (|a_n|)^{1/n} = L

- **Absolutely vs. conditionally convergent** series

- **Alternating series:** Leibniz alternating series test

- **Absolute convergence implies convergence**

### Unit 3: Power Series and Taylor Series (Weeks 10–13)

- **Power series:** Σ c_n (x-a)ⁿ, radius of convergence

- **Ratio test for radius of convergence**

- **Taylor series:** f(x) = Σ f^(n)(a)/n! · (x-a)ⁿ

- **Maclaurin series:** Taylor series at a = 0

- Key Maclaurin expansions:
 ```
 eˣ = Σ xⁿ/n! (all x)
 sin(x) = Σ (-1)ⁿ x^{2n+1}/(2n+1)! (all x)
 cos(x) = Σ (-1)ⁿ x^{2n}/(2n)! (all x)
 1/(1-x) = Σ xⁿ (|x| < 1)
 ```

- **Term-by-term differentiation and integration** of power series

- Approximation and error bounds using Taylor remainder

### Unit 4: Introduction to Multivariable Calculus (Weeks 14–18)

- Functions of several variables: f(x,y), f(x,y,z)

- **Level curves and surfaces** (contour maps)

- **Limits and continuity** in R², R³

- **Partial derivatives:** ∂f/∂x, ∂f/∂y

- **Gradient:** ∇f = (∂f/∂x, ∂f/∂y) — direction of steepest ascent

- **Chain rule** for multivariable functions

- **Directional derivative:** D_u f = ∇f · u

- **Tangent planes** and linear approximation

- **Double and triple integrals** as volume/summation

- **Change of variables:** polar, cylindrical, spherical coordinates

---

## 🔬 Key Series Expansions

```
eˣ = 1 + x + x²/2! + x³/3! + ...
sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ... (|x| < 1)
1/(1-x) = Σ_{n=0}∞ xⁿ (|x| < 1)
arctan(x) = x - x³/3 + x⁵/5 - ...
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Determine convergence/divergence of infinite series using standard tests
2. Construct and manipulate Taylor and Maclaurin series expansions
3. Use series for approximation and error estimation
4. Compute partial derivatives, gradients, and directional derivatives
5. Set up and evaluate double/triple integrals in various coordinate systems
6. Apply multivariable calculus to physics problems (fields, flux, charge distributions)

---

## 📚 References

1. Stewart, J. (2015). *Calculus: Early Transcendentals*, 8th ed. Cengage. (Chapters 11–16)
2. Thomas, G.B. et al. (2014). *Thomas' Calculus*, 14th ed. Pearson.
3. MIT OCW 18.01 and 18.02 (Multivariable Calculus): https://ocw.mit.edu
4. Paul's Online Math Notes: https://tutorial.math.lamar.edu/Classes/CalcII/CalcII.aspx
""