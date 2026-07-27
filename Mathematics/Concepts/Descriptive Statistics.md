---
title: 7. Descriptive Statistics
type: concept
subject: Mathematics
tags: [mathematics, statistics, descriptive-statistics, central-tendency, dispersion, skewness, kurtosis, aigis, geodesy-applied]
---

# 7. Descriptive Statistics

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary
Descriptive statistics summarise and describe the main features of a dataset — its centre, spread, and shape — through numerical measures and visualisation.

---

## Measures of Central Tendency (Ukuran Pemusatan)

These describe the "typical" value in a dataset.

| Measure | Formula | When to Use |
|---------|---------|-------------|
| **Mean** (Rata-rata) | $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ | Symmetric data without outliers |
| **Median** (Median) | Middle value when data is sorted | Skewed data, ordinal data, outliers present |
| **Mode** (Modus) | Most frequently occurring value | Categorical data, multimodal distributions |

**Example:** For data $\{2, 3, 3, 5, 7, 8, 100\} $:

- Mean = 18.3 (pulled right by the outlier 100)

- Median = 5 (robust to outliers)

- Mode = 3 (most frequent)

**Trimmed mean:** Discard top/bottom $k\%$before averaging — a compromise between mean and median robustness.

---

## Measures of Dispersion (Ukuran Persebaran)

These describe how spread out the data is.

| Measure | Formula | Notes |
|---------|---------|-------|
| **Range** | $\max(x_i) - \min(x_i)$ | Simple but sensitive to outliers |
| **Interquartile Range (IQR)** | $Q_3 - Q_1$ | Robust to outliers |
| **Variance** | $s^2 = \frac{1}{n-1}\sum(x_i - \bar{x})^2$ | Sample variance (unbiased) |
| **Std Deviation** | $s = \sqrt{s^2} $ | Same units as data |
| **CV (Koefisien Variasi)** | $CV = s/\bar{x} $ | Dimensionless relative spread |

**Degrees of freedom:**$n-1 $in sample variance corrects for the bias of estimating the mean from the same data.

**Geodesy application:** The standard deviation of GNSS height residuals tells how precisely height observations cluster around the estimated surface.

---

## Percentiles and Quartiles

- **Quartiles:**$Q_1$(25th percentile),$Q_2$(median),$Q_3$(75th percentile)

- **IQR** =$Q_3 - Q_1$— the middle 50% of the data

- **Box plot:** Visualisation using min,$Q_1$, median, $Q_3$, max (with outlier detection)

- **Outlier rule:** Data point is an outlier if it lies beyond $Q_1 - 1.5\times\text{IQR} $or $Q_3 + 1.5\times\text{IQR} $---

## Measures of Shape (Ukuran Bentuk)

### Skewness (Kemiringan)

Measures asymmetry of the distribution
:

$$\gamma_1 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^3$$

| Value | Shape | Example |
|-------|-------|---------|
| $\gamma_1 = 0$ | Symmetric (perfectly balanced) | Normal distribution |
| $\gamma_1 > 0$ | Right-skewed (positif) | Income, GNSS multipath errors |
| $\gamma_1 < 0$ | Left-skewed (negatif) | Exam scores (easy test) |

**Interpretation:** The tail is longer on the skewed side; the mean is pulled toward the tail.

### Kurtosis (Keruncingan)

Measures tail heaviness and peakedness (excess kurtosis)
:

$$\gamma_2 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^4 - 3$$

| Value | Type | Interpretation |
|-------|------|----------------|
| $\gamma_2 = 0$ | Mesokurtic | Normal distribution tails |
| $\gamma_2 > 0$ | Leptokurtic | Heavy tails, more outliers |
| $\gamma_2 < 0$ | Platykurtic | Light tails, fewer outliers |

**Geodesy application:** Residuals from LS adjustment with heavy tails (leptokurtic) suggest that the normal error assumption is violated — may indicate systematic errors or unmodeled effects.

---

## Covariance and Correlation (Kovarian dan Korelasi)

**Covariance:** measures how two variables vary together
:

$$\text{Cov}(X, Y) = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})$$

- Positive: variables increase together

- Negative: one increases as the other decreases

- Covariance magnitude depends on scales (hard to interpret directly)

**Correlation coefficient** (Pearson's $r$):

$$r = \frac{\text{Cov}(X, Y)}{s_X s_Y}, \quad -1 \leq r \leq 1$$-$r = \pm 1$: perfect linear relationship

- $r = 0$: no linear relationship

- $r > 0.7$: strong positive correlation

**Geodesy application:** Correlation between East and North coordinate estimates from GNSS reveals network geometry quality.

---

## Summary Statistics Table

| Category | Measure | Robust to Outliers? |
|----------|---------|-------------------|
| Centre | Mean | No |
| Centre | Median | Yes |
| Spread | Standard deviation | No |
| Spread | IQR | Yes |
| Shape | Skewness | No |
| Shape | Kurtosis | No |
| Association | Correlation | No |

---

## Visualisation

| Plot | Shows |
|------|-------|
| **Histogram** | Frequency distribution shape |
| **Box plot** | Median, IQR, outliers |
| **Scatter plot** | Bivariate relationship |
| **QQ-plot** | Normality assessment |

---

## Key Equations

| Equation | Name | Purpose |
|----------|------|---------|
| $\bar{x} = \frac{1}{n}\sum x_i$ | Sample mean | Centre |
| $s^2 = \frac{1}{n-1}\sum(x_i-\bar{x})^2$ | Sample variance | Spread |
| $\gamma_1 = \frac{1}{n}\sum((x_i-\bar{x})/s)^3$ | Skewness | Asymmetry |
| $\gamma_2 = \frac{1}{n}\sum((x_i-\bar{x})/s)^4 - 3$ | Excess kurtosis | Tail weight |
| $r = \text{Cov}(X,Y)/(s_X s_Y)$ | Correlation | Association |

---

## Where geodesy uses this

- Analysing measurement residuals for systematic effects (skewness ≠ 0)

- Network reliability assessment (variance-covariance matrices)

- Outlier detection using IQR-based methods

- Assessing whether observations meet precision specifications

## Linked vault notes

- [[Least Squares Adjustment]]

- [[Hypothesis Testing]]

- [[Error Propagation]]

- [[Probability Foundations]]

- [[Mathematics MOC]]

---

*Maintained by AIGIS.*
