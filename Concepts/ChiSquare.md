---
tags: [aigis, concept, mathematics, statistics, chi-square]
created: 2026-07-27
---

# Chi-Square ($\chi^2$) Distribution

## Definition
If $Z_1, \dots, Z_k \sim \mathcal{N}(0,1)$, then:
$$X = \sum_{i=1}^k Z_i^2 \sim \chi^2(k)$$

## Properties
| Property | Value |
|----------|-------|
| Mean | $k$ |
| Variance | $2k$ |
| PDF | $f(x) = \frac{x^{k/2-1}e^{-x/2}}{2^{k/2}\Gamma(k/2)}$ |

## In Geodesy
1. **Least squares goodness-of-fit:** $\hat{\sigma}_0^2 \cdot (n-u) \sim \chi^2(n-u)$
2. **Variance component estimation:** Test if $\hat{\sigma}_0^2$ is statistically 1
3. **GNSS ambiguity resolution:** $\chi^2$ test on residuals validates fix

## Related
- [[Probability Foundations]]
- [[Least Squares Adjustment]]
- [[Hypothesis Testing]]

---
*Part of [[Probability Foundations]] → [[Least Squares Adjustment]]*