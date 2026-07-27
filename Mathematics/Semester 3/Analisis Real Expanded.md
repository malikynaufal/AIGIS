---
title: Semester 3 — Analisis Real (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, real-analysis, semester-3, aigis, geodesy-applied]
---

# Semester 3 — Analisis Real (Expanded)

**Course**: MGM211302 — Analisis Real
**Credits**: 3 SKS
**Prerequisites**: [[Kalkulus I Expanded]], [[Kalkulus II Expanded]]

---

## Course Overview

Real analysis provides the rigorous foundation of calculus. This course covers sequences, series, topological properties, continuity, differentiability, and metric space theory. Essential for understanding convergence of numerical methods and approximations.

---

## Syllabus

### Unit 1: Numbers and Sets

- **Real numbers**: Completeness, Archimedean property

- **Countable vs. uncountable**: $\mathbb{Q} $ countable,$\mathbb{R} $ uncountable

- **Cantor's diagonal argument**: $\mathbb{R} $ uncountable

- **Interrelations of sets**: Unions, intersections, De Morgan's laws

- **Cantor's theorem**: $|\mathcal{P}(A)| > |A| $### Unit 2: Sequences and Series

- **Convergent sequences**: Definition and properties

- **Subsequences and completeness**: In $\mathbb{R} $, every Cauchy sequence converges

- **Bolzano-Weierstrass**: Every bounded sequence has convergent subsequence

- **Series convergence tests**: Ratio, root, comparison, integral

- **Absolute vs. conditional convergence**: Riemann rearrangement theorem

- **Power series**: Radius of convergence, termwise differentiation/integration

### Unit 3: Topological Concepts

- **Open sets**: Definition and properties

- **Closed sets**: Definition and properties

- **Compact sets**: Heine-Borel theorem in $\mathbb{R}^n $- **Connectedness**: In $\mathbb{R} $ and $\mathbb{R}^n $- **Separation properties**: Hausdorff spaces

### Unit 4: Continuity

- **Continuous functions**: $\lim_{xo a} f(x) = f(a) $- **Characterization**: Continuous function maps connected sets to connected sets

- **Intermediate Value Theorem**: For continuous $ f $ on $ [a,b] $- **Extreme Value Theorem**: Continuous $ f $ on compact set attains max/min

### Unit 5: Differentiability and Integration

- **$ C^1 $ and $ C^2 $ functions**: Continuously differentiable

- **Mean Value Theorem**: $ f(b)-f(a) = f'(c)(b-a) $ for some $ c\in(a,b) $- **L'Hôpital's rule**: $ 0/0 $ and $\infty/\infty $ limits

- **Taylor's theorem**: With remainder $ R_n $- **Riemann integrals**: Definition and properties

- **Improper integrals**: Infinite limits and discontinuities

### Unit 6: Sequences of Functions

- **Uniform convergence**: Pointwise vs. uniform convergence

- **Weierstrass M-test**: Uniform convergence of series

- **Uniform continuity**: Bounded functions on compact metric spaces

- **Interchange of operations**: limit, integration, differentiation

### Unit 7: Metric Spaces

- **Metric space axioms**: Distance function properties

- **Compact metric spaces**: Sequential compactness

- **Completeness**: Cauchy sequences converge

- **Contraction mapping**: Banach fixed-point theorem

---

## Key Theorems

1. **Heine-Borel**: $ S \subset \mathbb{R}^n $ is compact $\\iff $ S closed and bounded
2. **Bolzano-Weierstrass**: Every bounded sequence in $\mathbb{R}^n $ has convergent subsequence
3. **Intermediate Value**: Continuous $ f $ on $ [a,b] $ hits all intermediate values
4. **Extreme Value**: Continuous $ f $ on compact $ K $ attains max/min
5. **Mean Value**: $ f(b)-f(a) = f'(c)(b-a) $ 6. **Weierstrass Approximation**: Polynomials are dense in $ C[a,b]$
7. **Contraction Mapping**: Unique fixed point for contraction on complete metric space

---

## Geodesy Applications

- **Proof of existence**: Justifies convergence of least-squares iterations

- **Uniform convergence**: Ensures numerical methods converge uniformly

- **Completeness**: Guarantees stability of numerical systems

- **Compactness**: Critical for proving optimal solutions exist

---

## References

- Rudin, W. *Principles of Mathematical Analysis* (Chapters 1-4)

- Bartle, R.G. & Sherbert, D.R. *Introduction to Real Analysis* (Chapters 1-4)

- Abbott, S. *Understanding Analysis* (Chapters 1-4)

---

➡️ [[Mathematics MOC]] | ➡️ [[Differential Equations intro]]