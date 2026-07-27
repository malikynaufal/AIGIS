---
title: Semester 3 — Probabilitas (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, probability, semester-3, aigis, geodesy-applied]
---

# Semester 3 — Probabilitas (Expanded)

**Course**: MGM211303 — Probabilitas
**Credits**: 3 SKS
**Prerequisites**: [[Kalkulus I Expanded]], [[Multivariable Calculus]]

---

## Course Overview

This course introduces the axioms of probability, random variables, and fundamental distributions. It provides the mathematical foundation for statistical inference and measurement error theory in geodesy.

---

## Syllabus

### Unit 1: Foundations

- **Axioms of probability** (Kolmogorov):
 1. $0 \leq P(A) \leq 1 $ 2.$ P(\Omega) = 1 $ 3. Countable additivity: $ P(\cup_i A_i) = \sum_i P(A_i) $ for disjoint events

- **Set operations**: Union, intersection, complement

- **Conditional probability**: $ P(A|B) = P(A\cap B)/P(B) $- **Bayes' theorem**: $ P(A|B) = P(B|A)P(A)/P(B) $- **Independence**: $ P(A\cap B) = P(A)P(B) $### Unit 2: Random Variables

- **Discrete RVs**: PMF, support, examples (Bernoulli, Binomial, Poisson)

- **Continuous RVs**: PDF, CDF, support

- **Mixed distributions**: Discrete + continuous components

- **Random vector**: Joint PMF/PDF, marginal distributions

### Unit 3: Expectation and Variance

- **Expected value**: $ E[X] = \sum x_i p_i $ or $\int xf(x)dx $- **Variance**: $ ext{Var}(X) = E[X^2]-(E[X])^2 $- **Covariance and correlation**: $ ext{Cov}(X,Y) $, $\rho_{XY} $

- **Properties**: Linearity, independence → zero covariance

### Unit 4: Important Distributions

**Discrete**:

- Bernoulli($ p $): $ P(1)=p $, $ E=p $, $ ext{Var}=p(1-p) $

- Binomial($ n,p $): $\binom{n}{k}p^k(1-p)^{n-k} $

- Poisson($\lambda $): $ e^{-\lambda}\lambda^k/k!$, $ E=\lambda $, $ ext{Var}=\lambda $

- Geometric($ p $): $ (1-p)^{k-1}p $, $ E=1/p $

**Continuous**:

- Uniform($ a,b $): $ f(x)=1/(b-a) $, $ E=(a+b)/2 $

- Normal($\mu,\sigma^2 $): $ f(x) = \frac{1}{\sigma\sqrt{2i}}e^{-(x-\mu)^2/(2\sigma^2)} $

- Exponential($\lambda $): $\lambda e^{-\lambda x} $, $ E=1/\lambda $, $ ext{Var}=1/\lambda^2 $

- Chi-square($ n $): $\sum Z_i^2 $### Unit 5: Limit Theorems

- **Law of Large Numbers** (weak and strong): $\bar{X}_n o \mu $- **Central Limit Theorem**: $\frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \\xrightarrow{d} N(0,1) $### Unit 6: Joint Distributions

- **Joint PMF/PDF**: $ p(x,y) $ or $ f(x,y) $- **Marginals**: $ p_X(x) = \sum_y p(x,y) $ or $ f_X(x) = \int f(x,y)dy $- **Independence**: $ f(x,y) = f_X(x)f_Y(y) $- **Covariance matrix**: $\Sigma = \begin{bmatrix}\sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2\end{bmatrix} $---

## Worked Example: Bayes' Theorem in GPS

A GPS station has 90% probability of correct signal. Signal noise test is 80% sensitive. What's the probability of a clean signal given a positive noise test?$ P(ext{clean}) = 0.9 $, $ P(ext{positive}|ext{clean}) = 0.8 $
$ P(ext{positive}|ext{noisy}) = 0.3 $

$ $ P(ext{clean}|+) = \frac{0.8 imes 0.9}{0.8imes 0.9 + 0.3imes 0.1} = \frac{0.72}{0.75} = 0.96 $ $---

## Geodesy Applications

- **Normal distribution**: Measurement errors assumed Gaussian

- **CLT**: Justifies why the mean of $ n$ measurements is approximately normal

- **Bayes' theorem**: GPS signal quality assessment, outlier detection

- **Covariance matrices**: Uncertainty of coordinate estimates

- **Independence**: Assumption for adjustment weights

---

## References

- Ross, S. (2019). *A First Course in Probability*

- OpenStax Introductory Statistics (Chapters 3-5)

- MIT OCW 18.05: Probability and Statistics

---

➡️ [[Mathematics MOC]] | ➡️ [[Probability Distributions]]