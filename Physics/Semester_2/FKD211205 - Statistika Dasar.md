---
code: FKD211205
name: Statistika Dasar
SKS: 2
semester: 2
department: Matematika/Fisika
tags: [statistics, data-analysis, probability, physics-methods]
created: 2026-07-27
---

# FKD211205 — Statistika Dasar

## Course Overview

Statistics is the essential tool for analyzing experimental data in physics. This course covers probability theory, statistical distributions, error analysis, and hypothesis testing — all applied to the measurement contexts encountered in physics laboratories and research.

**Contact Hours:** 2 SKS (2 hours lecture per week)
**Prerequisites:** Fisika Dasar I, Kalkulus I
**Co-requisites:** Statistika Lanjutan (Semester 3)

---

## 📋 Topics & Outline

### Unit 1: Probability Theory (Weeks 1–5)

- **Sample space, events, probability axioms** — Kolmogorov axioms

- **Conditional probability:** P(A|B) = P(A∩B)/P(B)

- **Bayes' theorem:** P(A|B) = P(B|A)P(A)/P(B)

- **Independence:** P(A∩B) = P(A)P(B)

- **Discrete random variables:**
 - Probability mass function (PMF)
 - Expected value: E[X] = Σ x·P(x)
 - Variance: Var(X) = E[X²] - (E[X])²

- **Continuous random variables:**
 - Probability density function (PDF)
 - Cumulative distribution function (CDF): F(x) = P(X≤x)
 - E[X] = ∫ x·f(x)dx, Var(X) = ∫ (x-μ)²f(x)dx

### Unit 2: Important Distributions (Weeks 6–9)

- **Binomial distribution:** P(k; n,p) = C(n,k)p^k(1-p)^{n-k}
 - Mean = np, Variance = np(1-p)

- **Poisson distribution:** P(k; λ) = λ^k e^{-λ}/k!
 - Mean = λ, Variance = λ
 - Approximation of binomial for large n, small p

- **Normal (Gaussian) distribution:**
 ```
 f(x) = (1/σ√(2π)) exp(-(x-μ)²/(2σ²))
 ```
 - 68-95-99.7 rule (±1σ, ±2σ, ±3σ)
 - Central Limit Theorem: sums of i.i.d. variables → Gaussian

- **Exponential distribution:** f(x) = λe^{-λx}, for decay processes

- **Chi-squared (χ²), Student's t, and F distributions** — introduced for later lab use

### Unit 3: Data Analysis and Error (Weeks 10–13)

- **Measurement uncertainty:**
 - Random vs. systematic error
 - Standard deviation of the mean: σ̄ = σ/√N
 - Propagation of uncertainty: if z = f(x,y), then
 σ_z = √[(∂f/∂x)²σ_x² + (∂f/∂y)²σ_y²]

- **Significant figures** and rounding rules

- **Graphical analysis:** linearization, log-log and semi-log plots

- **Least-squares linear regression:**
 - Finding best-fit line y = mx + b
 - Slope uncertainty and correlation coefficient r
 - χ² minimization for nonlinear fits

### Unit 4: Hypothesis Testing and Inference (Weeks 14–16)

- **Null hypothesis (H₀) and alternative hypothesis (H₁)**

- **p-value:** probability of observing data as extreme if H₀ is true

- **Confidence intervals:** 95% CI = x̄ ± t·σ/√N

- **Chi-squared goodness-of-fit test:** χ² = Σ (O_i - E_i)²/E_i

- **t-test** for comparing means

- **Statistical significance** vs. practical significance

- Common misconceptions (p-hacking, base rate fallacy)

- Software tools for statistics: Python `scipy.stats`, R

---

## 🔬 Key Formulas

```
Mean: μ = Σx_i/N (population) x̄ = Σx_i/n (sample)
Variance: σ² = Σ(x_i - μ)²/N
Gaussian: f(x) = (1/σ√(2π)) exp(-(x-μ)²/(2σ²))
Uncertainty propagation: σ_z² = (∂f/∂x)²σ_x² + (∂f/∂y)²σ_y²
Regression slope: m = Σ(x_i-x̄)(y_i-ȳ) / Σ(x_i-x̄)²
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Compute probabilities using basic rules, Bayes' theorem, and distributions
2. Apply the normal distribution and Central Limit Theorem to measurement data
3. Perform uncertainty propagation for derived quantities
4. Conduct least-squares fits and interpret goodness-of-fit
5. Formulate and test hypotheses using p-values and confidence intervals
6. Apply statistical methods to physics experimental data responsibly

---

## 📚 References

1. Taylor, J.R. (1997). *An Introduction to Error Analysis*, 2nd ed. University Science Books.
2. Bevington, P.R. & Robinson, D.K. (2003). *Data Reduction and Error Analysis*, 3rd ed. McGraw-Hill.
3. Leon-Garcia, A. (2008). *Probability and Statistics for Engineers and the Sciences*, 8th ed. Cengage.
4. MIT OCW Introduction to Probability: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/
5. Python libraries: `numpy.random`, `scipy.stats`, `matplotlib.pyplot.errorbar`
