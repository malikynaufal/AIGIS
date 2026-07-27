---
title: 10. Sampling & Estimation
type: concept
subject: Mathematics
tags: [mathematics, statistics, sampling, estimation, CLT, confidence-interval, sample-size, aigis, geodesy-applied]
---

# 10. Sampling & Estimation

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary
Sampling and estimation provide the tools to infer population parameters from a sample — the foundation of all statistical inference. This concept covers random sampling, the Central Limit Theorem, confidence intervals, and sample size determination.

---

## 1. Random Sampling (Pengambilan Sampel Acak)

### 1.1 Types of Samples

| Sample Type | Description | Bias Risk |
|-------------|-------------|-----------|
| **Simple random** | Every member has equal selection probability | Low |
| **Stratified** | Population divided into strata, each sampled proportionally | Low (if strata well-chosen) |
| **Cluster** | Groups (clusters) are randomly selected, then all in cluster sampled | Higher |
| **Systematic** | Every $k $ th member selected | Higher (periodicity) |
| **Convenience** | Readily available subjects | Very high — avoid |

### 1.2 Estimator Properties

Let $\hat{\theta} $ be an estimator of parameter $\theta $:

| Property | Definition | Meaning |
|----------|------------|---------|
| **Unbiased** | $ E[\hat{\theta}] = \theta $ | Correct on average |
| **Consistent** | $\hat{\theta} \xrightarrow{p} \theta $ as $  n \to \infty $ | Converges to truth |
| **Efficient** | $\text{Var}(\hat{\theta}) $ is minimal among unbiased estimators | Precise estimation |
| **Sufficient** | Uses all information about $\theta $ in the sample | No information loss |

**Mean Squared Error (MSE):*
*

$ $\text{MSE}(\hat{\theta}) = \text{Bias}(\hat{\theta})^2 + \text{Var}(\hat{\theta})

$$

---

## 2. Central Limit Theorem (Teorema Limit Pusat)

The most important theorem in statistics.

### 2.1 Statement

For any population with mean $\mu $ and finite variance $\sigma^2 $, the sample mean $\bar{X} $ of $  n $ independent observations has $ $\bar{X}_n \xrightarrow{d} \mathcal{N}\!\left(\mu,\;\frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty

$$

**Practical rule:**$ n \geq 30 $ is usually sufficient for the CLT to provide a good approximation, but this depends on the population distribution's skewness and kurtosis.

### 2.2 Standard Error of the Mea
n

$ $\text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}} \approx \frac{s}{\sqrt{n}} $$

This is the standard deviation of the sampling distribution of $\bar{x} $— it measures how precisely the sample mean estimates the population mean.

**Example:** If $ s = 10 $ mm for GNSS baseline measurements and $  n = 100 $:

$ $\text{SE}(\bar{x}) = \frac{10}{\sqrt{100}} = 1\text{ mm} $$

This means the estimated mean baseline length has std. dev. of 1 mm.

---

## 3. Point Estimation (Estimasi Titik)

### 3.1 Method of Moments

Equate sample moments to population moments and solve for parameters

$ $\frac{1}{n}\sum x_i^k = E[X^k] \quad \text{for } k = 1, 2, \ldots

$$

# ## 3.2 Maximum Likelihood Estimation (MLE
)

$ $\hat{\theta}_{\text{MLE}} = \arg\max_\theta \prod_{i=1}^n f(x_i|\theta)

$$

**Properties:** Consistent, asymptotically efficient, asymptotically normal.

### 3.3 Least Squares Estimation

Minimizes sum of squared errors (classical approach in geodesy)

$ $\hat{\theta}_{\text{LS}} = \arg\min_\theta \sum (y_i - f(x_i, \theta))^2

$$

For linear models, this is BLUE — Best Linear Unbiased Estimator.

---

## 4. Confidence Intervals (Interval Keyakinan)

### 4.1 For the Population Mean

**Large sample / known variance:*
*

$ $\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} $$

**Small sample / unknown variance:*
*

$ $\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}} $$

# ## 4.2 Common Critical Values

| Confidence Level | $ z_{\alpha/2} $ | $  z $ (one-sided) |
|-----------------|----------------|-----------------|
| 90% | 1.645 | 1.282 |
| 95% | 1.960 | 1.645 |
| 99% | 2.576 | 2.326 |

### 4.3 For the Population Varianc
e

$ $ (n-1)s^2 / \chi^2_{\alpha/2, n-1} \leq \sigma^2 \leq (n-1)s^2 / \chi^2_{1-\alpha/2, n-1} $$

# ## 4.4 For a Proportio
n

$ $ \hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} $$

# ## 4.5 Interpretation

**Frequentist interpretation:** If we repeated the sampling process many times and computed a CI each time,$ (1-\alpha) $ of these intervals would contain the true parameter.

**Not:** "There is a 95% probability that $\mu $ lies in this interval" —$\mu $ is fixed, not random.

---

## 5. Sample Size Determination

### 5.1 For Estimating a Mea
n

$ $  n = \left(\frac{z_{\alpha/2} \cdot \sigma}{\text{Margin of Error } E}\right)^2 $ $**Example:** Desired half-width $  E = \pm 2 $ mm,$\sigma \approx 10 $ mm, 95% confidence $ $  n = \left(\frac{1.96 \times 10}{2}\right)^2 = (9.8)^2 \approx 96 $$

# ## 5.2 For Estimating a Proportio
n

$ $  n = \frac{z_{\alpha/2}^2 \cdot \hat{p}(1-\hat{p})}{E^2}$$

# ## 5.3 Finite Population Correction (FPC)

When sample $ n $ is more than 5-10% of population $  N $:

$ $\text{FPC} = \sqrt{\frac{N-n}{N-1}} $$

Use this to reduce the standard error when sampling a large fraction of a finite population.

---

## 6. Sampling Distribution (Distribusi Sampling)

### 6.1 Distribution of $\bar{x} $ If $  X \sim \mathcal{N}(\mu, \sigma^2) $:

$ $\bar{x} \sim \mathcal{N}(\mu, \sigma^2/n)

$$

# ## 6.2 Distribution of $\hat{p} $ For large $  n $:

$ $\hat{p} \sim \mathcal{N}\!\left(p,\;\frac{p(1-p)}{n}\right)

$$

# ## 6.3 Distribution of $ (n-1)s^2/\sigma^2 $

$ $\frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1)

$$---

## 7. Practical Considerations

### 7.1 What if the Population is Not Normal?

- For $ n \geq 30 $: CLT ensures $\bar{x} $ is approximately normal

- For $ n < 30 $: if the population distribution is also non-normal, consider nonparametric methods (bootstrap, Mann-Whitney, etc.)

- **Bootstrap:** Resample with replacement from the data to estimate the sampling distribution without parametric assumptions

### 7.2 Outliers and Influential Points

- Outliers can significantly affect $\bar{x} $ (especially for small $  n $)

- The **median** is more robust than the mean as a point estimate under heavy-tailed distributions

- **Trimmed mean** discards $ k\%$ from each tail for robustness

---

## 8. Geodesy Examples

**Sampling applied:** GNSS data logged at 1 Hz over 30 minutes → 1800 epochs. Sample every 30th measurement →$ n = 60 $ independent observations (accounting for time correlation).

**Estimation applied:** Estimating the station coordinate from $ n $ GNSS observation epochs:
-$\hat{x} = \bar{x} $ (MLE under normal distribution)
-$\text{SE}(\hat{x}) = s/\sqrt{n} $- 95% CI: $\hat{x} \pm t_{0.025, n-1} \cdot s/\sqrt{n} $---

## Key Equations

| Equation | Use |
|----------|-----|
| $\text{SE}(\bar{x}) = s/\sqrt{n} $ | Standard error of mean |
| $\bar{x} \pm t_{\alpha/2, n-1} \cdot s/\sqrt{n} $ | CI for mean |
| $ n = (z_{\alpha/2}\sigma/E)^2 $ | Sample size for mean |
| $\text{MSE} = \text{Bias}^2 + \text{Var} $ | Estimator quality |

---

## Where geodesy uses this

- Determining required number of GNSS epochs for a given precision

- Computing confidence intervals for estimated coordinates

- Sample size planning for survey campaigns

- Bootstrap methods for deformation uncertainty estimation

## Linked vault notes

- [[Least Squares Adjustment]]

- [[Hypothesis Testing]]

- [[Probability Foundations]]

- [[Descriptive Statistics]]

- [[Error Propagation]]

- [[Mathematics MOC]]

---

*Maintained by AIGIS.*
