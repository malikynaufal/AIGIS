---
title: 11. Hypothesis Testing
type: concept
subject: Mathematics
tags: [mathematics, statistics, hypothesis-testing, p-value, t-test, z-test, anova, aigis, geodesy-applied]
---

# 11. Hypothesis Testing

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary
Hypothesis testing is a formal procedure for deciding whether sample data provides sufficient evidence to reject a null hypothesis. It is fundamental for statistical inference, quality control, and model validation in geodesy.

---

## 1. Framework (Kerangka Uji)

### 1.1 The Six Steps

| Step | Action | Example |
|------|--------|---------|
| 1. | State $H_0$(null hypothesis) | $\mu = 100 $m |
| 2. | State $H_a$(alternative hypothesis) | $\mu \neq 100 $m |
| 3. | Choose significance level $\alpha$ | $\alpha = 0.05$ |
| 4. | Compute test statistic | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} $ |
| 5. | Compute p-value or compare to critical value | $p = 0.023$ |
| 6. | Make decision | Reject $H_0 $if $p < \alpha$; otherwise fail to reject |

**Null hypothesis (Hipotesis nol):** The default assumption — no effect, no difference, no relationship.
**Alternative hypothesis (Hipotesis alternatif):** The claim being tested (two-sided: $\neq$; one-sided: $>$or$<$).

---

## 2. Error Types (Jenis Galat)

| | $H_0 $is True | $H_0 $is False |
|---|---|---|
| **Reject $H_0$** | Type I error ($\alpha$) — false positive | **Correct** (Power = $1-\beta$) |
| **Fail to reject $H_0$** | **Correct** | Type II error ($\beta$) — false negative |

- **$\alpha$(significance level):** Probability of rejecting a true $H_0$. Usually 0.05 or 0.01.

- **$\beta$:** Probability of failing to reject a false $H_0$.

- **Power ($1-\beta$):** Probability of detecting a real effect when it exists.

**Factors affecting power:**

- Larger $\alpha$→ higher power (but more Type I errors)

- Larger sample size $n$→ higher power

- Larger effect size → higher power

- Lower variability → higher power

---

## 3. Test Statistics

### 3.1 One-Sample Z-Test (Known Variance
)

$$Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} $$

-$Z \sim \mathcal{N}(0, 1) $under $H_0$- Use when $\sigma $is known (large sample or known population variance)

### 3.2 One-Sample t-Test (Unknown Variance
)

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} $$

-$t \sim t(n-1) $under $H_0$- Use when $\sigma $is estimated from the sample

### 3.3 Two-Sample t-Test

**Independent (unpaired):*
*

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2(1/n_1 + 1/n_2)}}, \quad s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2} $$

-$t \sim t(n_1 + n_2 - 2) $under $H_0$**Welch's t-test** (unequal variances, more general)
:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} $$

### 3.4 Paired t-Tes
t

$$t = \frac{\bar{d}}{s_d/\sqrt{n}}, \quad d_i = x_{1i} - x_{2i} $$

### 3.5 Z-Test for Proportion
s

$$Z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}} $$

---

## 4. p-Values (Nilai-p)

The **p-value** is the probability of obtaining a test statistic as extreme as (or more extreme than) the observed one, assuming $H_0 $is true
.

$$p = P(T > t_{\text{obs}} \mid H_0)$$

**Interpretation:**
-$p < 0.01$: strong evidence against $H_0$-$p < 0.05$: moderate evidence

- $p < 0.10$: weak evidence

- $p \geq 0.10$: insufficient evidence

**⚠️ Common mistakes:**

- p-value is **not** the probability that $H_0 $is true

- p-value is **not** the probability that the result occurred by chance

- Statistical significance ≠ practical importance (a very small effect can be "significant" with large $n$)

---

## 5. One-Tailed vs Two-Tailed Tests

| Type | $H_a$ | Critical Region | When |
|------|-------|-----------------|------|
| Two-tailed | $\mu \neq \mu_0$ | Both tails | No directional expectation |
| Right-tailed | $\mu > \mu_0$ | Upper tail | Test for increase |
| Left-tailed | $\mu < \mu_0$ | Lower tail | Test for decrease |

**Rule:** Use two-tailed unless there is a strong prior expectation of direction.

---

## 6. Chi-Square Tests

### 6.1 Goodness-of-Fit Test

$$H_0: \text{Data follows a specified distribution}\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} $$-$\chi^2 \sim \chi^2(k-1-m)$(where $m$= estimated parameters)

### 6.2 Test of Independenc
e

$$H_0: \text{Two categorical variables are independent} $$

Same test statistic, applied to contingency tables. Degrees of freedom =$(r-1)(c-1)$.

---

## 7. ANOVA — Analysis of Variance

**Purpose:** Compare means of three or more groups.

**One-way ANOVA model:**

$$y_{ij} = \mu + \alpha_j + \epsilon_{ij}, \quad \epsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$$**Hypotheses:**
-$H_0: \mu_1 = \mu_2 = \cdots = \mu_k$(all group means equal)
-$H_a$: at least one mean differs

**F-statistic:**

$$F = \frac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}} = \frac{\frac{1}{k-1}\sum n_j(\bar{x}_j - \bar{x})^2}{\frac{1}{N-k}\sum\sum (x_{ij} - \bar{x}_j)^2} $$-$F \sim F(k-1, N-k) $under $H_0$**ANOVA assumptions:** (1) Normality, (2) Homoscedasticity (equal variances), (3) Independence

**Post-hoc tests** (after ANOVA rejects $H_0$): Tukey HSD, Bonferroni correction.

---

## 8. Geodesy Applications

| Test | Geodetic Use |
|------|-------------|
| **t-test** | Testing whether a coordinate shift is significant between epochs |
| **$\chi^2 $test** | Global model test for LS adjustment quality |
| **F-test** | Testing whether adding parameters significantly improves the model |
| **Baarda w-test** | Outlier detection using standardized residuals |
| **ANOVA** | Comparing precision of different measurement techniques |

### Baarda Data Snooping (Detailed)

Test an individual observation for a gross error
:

$$w_i = \frac{v_i}{\sigma_0\sqrt{q_{v_i v_i}}} \sim \mathcal{N}(0, 1)$$

-$|w_i| > 3.29$($\alpha = 0.001$): reject $H_0$(observation likely has a gross error)

- Iterate: remove worst outlier, re-adjust, repeat

---

## Key Equations

| Equation | Test | Use |
|----------|------|-----|
| $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} $ | One-sample t-test | Mean comparison |
| $t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{1/n_1 + 1/n_2}} $ | Two-sample t-test | Comparing two groups |
| $\chi^2 = \sum (O_i - E_i)^2/E_i$ | Chi-square test | Distribution fit |
| $F = \text{MS}_{\text{between}}/\text{MS}_{\text{within}} $ | ANOVA | Multiple group means |
| $w_i = v_i/\hat{\sigma}_{v_i} $ | Baarda test | Outlier detection |

---

## Where geodesy uses this

- Data snooping in least-squares adjustment (Baarda, Tau-test)

- Evaluating whether coordinate changes between survey epochs are significant

- Testing whether residuals are normally distributed

- Model selection using F-test (adding more parameters)

## Linked vault notes

- [[Least Squares Adjustment]]

- [[Probability Foundations]]

- [[Error Propagation]]

- [[Descriptive Statistics]]

- [[Probability and Statistics for Geodesy]]

- [[Mathematics MOC]]

---

*Maintained by AIGIS.*
