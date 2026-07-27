---
title: 8. Probability Distributions (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, probability, distributions, statistics, aigis, geodesy-applied]
---

# 8. Probability Distributions (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Probability distributions model the behaviour of random variables. They form the foundation of statistical inference, error modelling, and measurement uncertainty in geodesy.

## 1. Probability Fundamentals

### 1.1 Axioms (Kolmogorov)

- $0 \leq P(A) \leq 1$-$P(\Omega) = 1$- Additivity for disjoint events:$P(A \cup B) = P(A) + P(B)$### 1.2 Bayes' Theorem$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$## 2. Discrete Distributions

### 2.1 Binomial Distribution

**Setup**:$n$independent Bernoulli trials, each with success probability$p$.

PMF (probability mass function):
$$

P(X = k) = \binom{n}{k}p^k(1-p)^{n-k},\quad k = 0,1,\ldots,n$$Parameters:$E[X] = np$, $\text{Var}(X) = np(1-p)$**Example**: Fair coin flipped 10 times, probability of exactly 3 heads:$$P(X=3) = \binom{10}{3}(0.5)^{10} = \frac{120}{1024} \approx 0.117$$### 2.2 Poisson Distribution

Models rare events over a fixed interval (time, space, or count).$$P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!},\quad k = 0,1,2,\ldots$$Parameters:$E[X] = \lambda$, $\text{Var}(X) = \lambda$**Approximation**: Poisson is the limit of Binomial when$n \to \infty$, $p \to 0$, $np = \lambda$.

**Example**: On average 3 GPS errors per hour. Probability of exactly 5 errors:
$$

P(X=5) = \frac{e^{-3} \cdot 3^5}{120} \approx 0.1008$$### 2.3 Geometric Distribution

Number of trials until first success:$$P(X=k) = (1-p)^{k-1}p,\quad k = 1,2,\ldots
$$

$E[X] = \frac{1}{p}$### 2.4 Hypergeometric Distribution

Sampling without replacement from finite population:$$P(X=k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$## 3. Continuous Distributions

### 3.1 Normal Distribution$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$Parameters:$\mu$(mean),$\sigma^2$(variance)

**Standard normal**:$Z = \frac{X-\mu}{\sigma} \sim N(0,1)$**68-95-99.7 rule**:
-$\mu \pm \sigma$: ~68%

- $\mu \pm 2\sigma$: ~95%

- $\mu \pm 3\sigma$: ~99.7%

**Proof of the normal PDF integral equalling 1** (Gaussian integral):
$$I = \int_{-\infty}^{\infty} e^{-x^2/2}dx$$

$$I^2 = \int\int e^{-(x^2+y^2)/2}dx\,dy = \int_0^{2\pi}\int_0^{\infty} e^{-r^2/2}r\,dr\,d\theta$$

$$= 2\pi\left[-e^{-r^2/2}\right]_0^{\infty} = 2\pi(1) = 2\pi$$

$$
I = \sqrt{2\pi}$$### 3.2 Student t-Distribution

When estimated$\sigma$from sample:$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}$$Heavier tails than normal; key for small-sample inference.

**As$n \to \infty$, $t \to N(0,1)$**.

### 3.3 Chi-Square Distribution

If $Z_1, \ldots, Z_k$i.i.d.$N(0,1)$:
$$\chi^2_k = \sum_{i=1}^k Z_i^2 \sim \chi^2(k)$$

$E[\chi^2] = k$, $\text{Var}(\chi^2) = 2k$**Use**: Goodness-of-fit tests, variance estimation.

### 3.4 F-Distribution

If$U \sim \chi^2_{d_1}$, $V \sim \chi^2_{d_2}$independent:$$F = \frac{U/d_1}{V/d_2} \sim F(d_1, d_2)$$**Use**: Comparing variances, ANOVA, regression significance.

## 4. Distribution Functions

### 4.1 CDF (Cumulative Distribution Function)$$F_X(x) = P(X \leq x)$$### 4.2 PDF (Probability Density Function)$$f_X(x) = \frac{d}{dx}F_X(x)
$$

$P(a < X < b) = F(b) - F(a) = \int_a^b f(x)\,dx$### 4.3 Expected Value$$E[g(X)] = \begin{cases} \sum_x g(x)p(x) & \text{discrete} \\ \int_{-\infty}^{\infty} g(x)f(x)\,dx & \text{continuous} \end{cases}$$### 4.4 Variance$$\text{Var}(X) = E[(X-\mu)^2] = E[X^2] - \mu^2$$### 4.5 Moment Generating Function$$M_X(t) = E[e^{tX}]
$$

$M_X^{(n)}(0) = E[X^n]$## 5. Joint Distributions

### 5.1 Joint PDF/PMF$$f_{X,Y}(x,y)$$Marginal:$$f_X(x) = \int f_{X,Y}(x,y)\,dy$$### 5.2 Covariance and Correlation$$\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]
$$

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y}$$

$-1 \leq \rho \leq 1$## 6. Law of Large Numbers & Central Limit Theorem

### 6.1 Weak Law of Large Numbers

For i.i.d.$X_i$with mean$\mu$:
$$

\frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu \quad \text{as } n \to \infty$$### 6.2 Central Limit Theorem$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$$For large$n$, sample mean is approximately normal regardless of population distribution.

## 7. Practice Problems

### Problem 1
Let $X \sim \text{Binomial}(10, 0.4)$. Find $P(X = 4)$.

**Solution**:
$$

P(X=4) = \binom{10}{4}(0.4)^4(0.6)^6 = 210 \cdot 0.0256 \cdot 0.04666 \approx 0.2508$$### Problem 2
Let$X \sim N(5, 4)$. Find $P(X > 7)$.

**Solution**: $Z = \frac{7-5}{2} = 1$
$$

P(X > 7) = P(Z > 1) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587$$### Problem 3$X \sim \chi^2_{10}$, find $P(X \geq 18)$.

**Solution**: Using chi-square table or `scipy.stats.chi2.sf(18, 10) \approx 0.0535`

### Problem 4
Show that $E[X] = \lambda$for$X \sim \text{Poisson}(\lambda)$.

**Proof**:
$$E[X] = \sum_{k=0}^{\infty} k \frac{e^{-\lambda}\lambda^k}{k!} = \lambda e^{-\lambda}\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda}e^{\lambda} = \lambda \quad \blacksquare$$

## 8. Where Geodesy Uses This

- **Measurement uncertainty**: Gaussian errors dominate

- **Error ellipses**: 2D normal distribution for position estimates

- **Hypothesis testing**: Student-t for small adjustment datasets

- **Significance tests**: F-test for comparing models

- **Noise modelling**: Poisson for counting (satellite counts)

- **Bootstrap resampling**: empirical distribution from data

## 9. References

- OpenStax Introductory Statistics

- MIT OCW 18.05: Probability and Statistics

- Wackerly, Mendenhall, Scheaffer (2014). *Mathematical Statistics*

---

*Maintained by AIGIS.*
