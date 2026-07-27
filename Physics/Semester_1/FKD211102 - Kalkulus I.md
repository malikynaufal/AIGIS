---
code: FKD211102
name: Kalkulus I
SKS: 4
semester: 1
department: Matematika
tags: [mathematics, calculus, limits, derivatives, integrals]
created: 2026-07-27
---

# FKD211102 — Kalkulus I

## Course Overview

Calculus I provides the mathematical foundation essential for all physics courses. This course develops fluency in limits, differentiation, and integration — the tools that make physics quantitative. Every law of physics from Newton's F=ma to Maxwell's equations requires calculus for its expression and application.

**Contact Hours:** 4 SKS (3 hours lecture + 1 hour tutorial per week)
**Prerequisites:** None
**Co-requisites:** Fisika Dasar I, Aljabar Linear

---

## 📋 Topics & Outline

### Unit 1: Foundations and Limits (Weeks 1–4)

- Real number system, inequalities, absolute value

- Functions: domain, range, composition, inverse functions

- **Limits:** intuitive concept, one-sided limits, limit laws

- ε-δ definition of a limit (introductory)

- Limits involving infinity: horizontal and vertical asymptotes

- **Continuity:** definition, types of discontinuity, Intermediate Value Theorem

### Unit 2: Differentiation (Weeks 5–9)

- Definition of the derivative: `f'(x) = lim[Δx→0] (f(x+Δx) - f(x))/Δx`

- Geometric interpretation: slope of tangent line, velocity

- **Differentiation rules:**
  - Power rule: d/dx[xⁿ] = nxⁿ⁻¹
  - Product rule: d/dx[fg] = f'g + fg'
  - Quotient rule: d/dx[f/g] = (f'g - fg')/g²
  - **Chain rule:** d/dx[f(g(x))] = f'(g(x))·g'(x)

- Derivatives of trigonometric, exponential, and logarithmic functions

- **Implicit differentiation**

- **Related rates** problems

- L'Hôpital's Rule for indeterminate forms

- Mean Value Theorem and Rolle's Theorem

### Unit 3: Applications of Derivatives (Weeks 10–12)

- **Optimization:** max/min problems, critical points, second derivative test

- Curve sketching: concavity, inflection points, asymptotes

- Linearization and differentials: f(x+Δx) ≈ f(x) + f'(x)Δx

- Newton's method for root finding: x_{n+1} = x_n - f(x_n)/f'(x_n)

- Applications to physics: velocity from position, acceleration from velocity

### Unit 4: Integration (Weeks 13–18)

- Antiderivatives and indefinite integrals

- **Riemann sums** and area under a curve

- **Fundamental Theorem of Calculus:**
  - Part I: d/dx[∫ₐˣ f(t)dt] = f(x)
  - Part II: ∫ₐᵇ f(x)dx = F(b) - F(a)

- Integration techniques: substitution, integration by parts, partial fractions

- Improper integrals and convergence

- Applications: area, volume (disk/washer/shell methods), arc length

- Applications to physics: work done by variable forces, center of mass

---

## 🔬 Key Formulas

```
Power Rule:         d/dx[xⁿ] = nxⁿ⁻¹
Chain Rule:         d/dx[f(g(x))] = f'(g(x))·g'(x)
Product Rule:       d/dx[fg] = f'g + fg'
Integration:        ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C  (n ≠ -1)
                    ∫ (1/x) dx = ln|x| + C
                    ∫ eˣ dx = eˣ + C
                    ∫ sin(x) dx = -cos(x) + C
                    ∫ cos(x) dx = sin(x) + C
Fundamental Thm:    ∫ₐᵇ f(x)dx = F(b) - F(a)
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Compute limits and determine continuity of functions
2. Differentiate functions using standard rules and techniques
3. Apply derivatives to solve optimization and related rates problems
4. Evaluate definite and indefinite integrals using multiple techniques
5. Apply integration to compute areas, volumes, and physical quantities
6. Connect calculus operations to their physical interpretations (velocity, work, etc.)

---

## 📚 References

1. Stewart, J. (2015). *Calculus: Early Transcendentals*, 8th ed. Cengage.
2. Thomas, G.B. et al. (2014). *Thomas' Calculus*, 14th ed. Pearson.
3. Spivak, M. (2008). *Calculus*, 4th ed. Publish or Perish. (Rigorous/proof-based)
4. MIT OCW 18.01 Single Variable Calculus: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
5. Paul's Online Math Notes: https://tutorial.math.lamar.edu/
