---
title: MGM211402 - Statistika Matematika
type: course
semester: 4
sks: 3
tags: [mathematics, statistics, probability, inference, semester-4]
created: 2026-07-27
---

# MGM211402 - Statistika Matematika (Mathematical Statistics)

> *"Statistics is the grammar of science."* — Karl Pearson
> **SKS:** 3 | **Semester:** 4 | **Prerequisite:** [[Probability Foundations]], [[Probability Distributions]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Random Variables | PDF, CDF, transformations |
| 2 | Expectation | Mean, variance, moments, MGF |
| 3 | Common Distributions | Normal, gamma, beta, chi-square |
| 4 | Joint Distributions | Marginal, conditional, covariance |
| 5 | Limit Theorems | LLN, CLT, convergence types |
| 6 | Estimation Theory | MLE, method of moments, bias |
| 7 | Properties of Estimators | Consistency, efficiency, sufficiency |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Confidence Intervals | Construction, interpretation |
| 10 | Hypothesis Testing | Neyman-Pearson, p-values |
| 11 | Likelihood Ratio Tests | Composite hypotheses |
| 12 | Nonparametric Tests | Sign test, Wilcoxon, Kolmogorov-Smirnov |
| 13 | Bayesian Inference | Prior, posterior, conjugate families |
| 14 | Two-Sample Tests | t-test, F-test, Mann-Whitney |
| 15 | Final Review | Integration project |

## 📚 Core Theorems

### 1. Law of Large Numbers (LLN)

If $X_1, X_2, \dots $ are i.i.d. with $ E[X_i] = \mu $:

$ $\frac{1}{n}\sum_{i=1}^{n} X_i \xrightarrow{p} \mu \quad ext{(Weak LLN)}

$ $

$ $\frac{1}{n}\sum_{i=1}^{n} X_i \xrightarrow{a.s.} \mu \quad ext{(Strong LLN)}

$ $

### 2. Central Limit Theorem (CLT)

If $ X_1, \dots, X_n $ are i.i.d. with $ E[X_i] = \mu $, $ ext{Var}(X_i) = \sigma^2 $:

$ $\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} N(0, 1)

$ $

More generally: $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2) $.

### 3. Cramér-Rao Inequality

For any unbiased estimator $\hat{heta} $ of $ heta $:

$ $ ext{Var}(\hat{heta}) \geq \frac{1}{nI(heta)}

$ $

where $ I(heta) = E\left[\left(\frac{artial}{artial heta} \log f(X;heta)\right)^2\right] $ is the **Fisher information**.

### 4. Neyman-Pearson Lemma

The most powerful test for $ H_0: heta = heta_0 $ vs $ H_1: heta = heta_1 $ rejects $ H_0 $ when:

$ $\frac{L(heta_1)}{L(heta_0)} > k

$ $

where $ L $ is the likelihood function and $  k $ is chosen to achieve significance level $\alpha $.

## 🎯 Point Estimation

### Maximum Likelihood Estimation (MLE)

Given data $ x_1, \dots, x_n $:

$ $\hat{heta}_{MLE} = \arg\max_{heta} L(heta) = \arg\max_{heta} rod_{i=1}^n f(x_i; heta)

$ $**Log-likelihood:**$\ell(heta) = \sum_{i=1}^n \log f(x_i; heta) $**Score equation:**$\frac{artial \ell}{artial heta} = 0 $

### Method of Moments (MOM)

Set sample moments equal to population moments:

$ $ E[X^k] = \frac{1}{n}\sum_{i=1}^n X_i^k $ $

### Properties of Estimators

| Property | Definition |
|----------|-----------|
| **Bias** | $ ext{Bias}(\hat{heta}) = E[\hat{heta}] - heta $ |
| **Consistency** | $\hat{heta} \xrightarrow{p} heta $ |
| **Efficiency** | $ ext{Var}(\hat{heta}) $ achieves Cramér-Rao bound |
| **Sufficiency** | $ T(X) $ contains all info about $ heta $ (Factorization Theorem) |

## 🧪 Hypothesis Testing

### Framework

1. **Null hypothesis** $ H_0 $
2. **Alternative hypothesis** $ H_1 $
3. **Test statistic** $ T(X) $
4. **Rejection region** $ R $
5. **p-value:** $ P(ext{Type I error}) $

### Types of Errors

| Error Type | Description | Probability |
|-----------|-------------|-------------|
| **Type I** | Reject $ H_0 $ when true | $\alpha $ (significance level) |
| **Type II** | Fail to reject $ H_0 $ when false | $\beta $ (power =$ 1-\beta $) |

### Common Tests

| Test | Distribution | Use Case |
|------|-------------|----------|
| **Z-test** | $ N(0,1) $ | Known variance, large sample |
| **t-test** | $ t_{n-1} $ | Unknown variance, small sample |
| **Chi-square** | $\chi^2_{n-1} $ | Variance, goodness-of-fit |
| **F-test** | $ F_{n_1-1,n_2-1} $ | Comparing variances |
| **Wilcoxon** | Non-parametric | Non-normal data |

## 📊 Confidence Intervals

### General Form

$ $\hat{heta} m z_{\alpha/2} \cdot ext{SE}(\hat{heta})

$ $

### Examples

**Normal mean (known $\sigma $):**

$ $\bar{x} m z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}

$ $**Normal mean (unknown $\sigma $):**

$ $\bar{x} m t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}

$ $**Variance:**$ $\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}} < \sigma^2 < \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}

$ $# 🔄 Bayesian Inference $ $

# # 🔄 Bayesian Inferenceext{Posterior} ropto ext{Likelihood} imes ext{Prior}

$ $

$ $

p(heta | x) = \frac{p(x | heta) p(heta)}{p(x)}$ $

**Conjugate priors:** Posterior is in same family as prior.

| Likelihood | Conjugate Prior | Posterior |
|-----------|----------------|-----------|
| Binomial | Beta | Beta |
| Poisson | Gamma | Gamma |
| Normal | Normal | Normal |

## 💡 Solved Example: MLE for Normal Distribution

**Problem:** Find MLE of $\mu $ and $\sigma^2 $ for $  X \sim N(\mu, \sigma^2) $.

**Solution:**

$ $\ell(\mu, \sigma^2) = -\frac{n}{2}\log(2i) - \frac{n}{2}\log(\sigma^2) - \frac{1}{2\sigma^2}\sum(x_i - \mu)^2

$ $

Taking derivatives and setting to zero: $ $\frac{artial \ell}{artial \mu} = \frac{1}{\sigma^2}\sum(x_i - \mu) = 0 \implies \hat{\mu} = \bar{x}

$ $

$ $\frac{artial \ell}{artial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2}\sum(x_i - \mu)^2 = 0 \implies \hat{\sigma}^2 = \frac{1}{n}\sum(x_i - \bar{x})^2

$ $

## 📐 Geodesy Application: Error Ellipses

For 2D position estimates $ (X, Y) $ with covariance matrix:

$ $\Sigma = \begin{bmatrix} \sigma_X^2 & \sigma_{XY} \\ \sigma_{XY} & \sigma_Y^2 \end{bmatrix}

$ $

The error ellipse at confidence level $ P $ has semi-axes: $ $ a, b = \sqrt{\lambda_{1,2} \cdot \chi^2_{2,P}}$ $

where $\lambda_1, \lambda_2 $ are eigenvalues of $\Sigma $.

## 🎯 Practice Problems

1. **MLE:** Find the MLE of $\lambda $ for exponential distribution.
2. **CLT:** Approximate $ P(\sum_{i=1}^{100} X_i > 55) $ where $ X_i \sim ext{Exp}(1) $.
3. **Hypothesis Test:** Test $ H_0: \mu = 100 $ vs $ H_1: \mu > 100 $ with $ n=25, \bar{x}=103, s=8 $.
4. **Confidence Interval:** Construct a 95% CI for the mean given $ n=30, \bar{x}=50, s=12 $.
5. **Bayesian:** With prior $ heta \sim ext{Beta}(2,3)$ and data 7 successes out of 20, find the posterior.

## 📖 References

- Casella, G. & Berger, R.L. (2002). *Statistical Inference* (2nd ed.). Duxbury.
- Hogg, R.V. & Craig, A.T. (2018). *Introduction to Mathematical Statistics*. Pearson.
- Casella, G. & Berger, R.L. (2002). *Statistical Inference* (2nd ed.). Duxbury.

---
*See also: [[Probability Foundations]], [[Probability Distributions]], [[Hypothesis Testing]], [[Descriptive Statistics]], [[Sampling Estimation]]*
