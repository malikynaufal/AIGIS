---
tags: [aigis, concept, mathematics, statistics, error-propagation, covariance, jacobian, geodesy]
created: 2026-07-27
updated: 2026-07-27
---

# Error Propagation

## For Geodesy & Measurement Science

**Core Idea:** Error propagation predicts the uncertainty of a computed quantity from the uncertainties of its measurements. In geodesy, error propagation is THE tool for designing surveys, assessing coordinate quality, and understanding how errors propagate from observations to final results.

---

## 1. Fundamental Principles

### 1.1 General Law of Error Propagation

For a function $y = f(x_1, x_2, \dots, x_n) $, the variance of $ y $ is:

$ $\sigma_y^2 = \sum_{i=1}^n \sum_{j=1}^n \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} \text{Cov}(x_i, x_j)

$$

**For independent observations** ($\text{Cov}(x_i, x_j) = 0 $ when $ i \neq j $):

$ $\sigma_y^2 = \sum_{i=1}^n \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2

$$

### 1.2 Matrix Form (General)

For a vector transformation $\mathbf{y} = \mathbf{f}(\mathbf{x}) $:

$ $\mathbf{C}_y = \mathbf{J} \, \mathbf{C}_x \, \mathbf{J}^T

$$

where:
-$\mathbf{C}_y $= covariance matrix of $\mathbf{y} $-$\mathbf{C}_x $= covariance matrix of $\mathbf{x} $-$\mathbf{J} $= Jacobian matrix $\partial \mathbf{f}/\partial \mathbf{x} $ This is the **most general and powerful form** — it handles correlations, multiple outputs, and nonlinear transformations via linearisation.

### 1.3 Derivation (Quick)

Using first-order Taylor expansion around $\mathbf{x}_0 $:

$ $\mathbf{f}(\mathbf{x}) \approx \mathbf{f}(\mathbf{x}_0) + \mathbf{J}(\mathbf{x} - \mathbf{x}_0
)

$$

Taking variance of both sides:$ $\text{Var}[\mathbf{f}(\mathbf{x})] = \text{Var}[\mathbf{J}\mathbf{\delta}] = \mathbf{J}\,\text{Var}[\mathbf{\delta}]\,\mathbf{J}^T = \mathbf{J}\mathbf{C}_x\mathbf{J}^T

$$

---

## 2. Common Propagation Rules

| Operation | Error ($\sigma_y $) | Notes |
|-----------|-------------------|-------|
| $ y = a + b $ | $\sigma_y^2 = \sigma_a^2 + \sigma_b^2 + 2\sigma_{ab} $ | Add variances + 2×covariance |
| $ y = a - b $ | $\sigma_y^2 = \sigma_a^2 + \sigma_b^2 - 2\sigma_{ab} $ | Difference: covariance subtracts |
| $ y = a \cdot b $ | $\left(\frac{\sigma_y}{y}\right)^2 = \left(\frac{\sigma_a}{a}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 + \frac{2\sigma_{ab}}{ab} $ | Relative error form |
| $ y = a / b $ | $\left(\frac{\sigma_y}{y}\right)^2 = \left(\frac{\sigma_a}{a}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 - \frac{2\sigma_{ab}}{ab} $ | |
| $ y = a^n $ | $\frac{\sigma_y}{|y|} = |n|\frac{\sigma_a}{|a|} $ | Power: multiply relative error by exponent |
| $ y = \ln a $ | $\sigma_y = \frac{\sigma_a}{a} $ | Logarithm uncertainty |
| $ y = e^a $ | $\frac{\sigma_y}{y} = \sigma_a $ | Exponential uncertainty |
| $ y = \sin a $ | $\sigma_y = |\cos a|\,\sigma_a $ | Trig: derivative magnitude |
| $ y = \cos a $ | $\sigma_y = |\sin a|\,\sigma_a $ | |
| $ y = \sqrt{a} $ | $\frac{\sigma_y}{y} = \frac{1}{2}\frac{\sigma_a}{a} $ | Square root: half relative error |

**For uncorrelated variables** ($\sigma_{ab} = 0 $): the additive rule becomes $\sigma_y^2 = \sigma_a^2 + \sigma_b^2 $, and the product/quotient relative rules simplify to:

$ $\frac{\sigma_y}{|y|} = \sqrt{\left(\frac{\sigma_a}{a}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2
}

$$**Named in geodesy:** "**Law of Propagation of Variances**" or "**Variance-Covariance Propagation**"$ $\mathbf{Q}_{yy} = \mathbf{J} \mathbf{Q}_{xx} \mathbf{J}^T

$$

Where $\mathbf{Q} = \sigma_0^{-2} \cdot \mathbf{C} $ is the **cofactor matrix** (without unit-weight scale).

---

## 3. Advanced Topics

### 3.1 Propagation Through Least Squares

For the LS estimate $\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1}\mathbf{A}^T\mathbf{P}\mathbf{l} $:

$ $\mathbf{C}_{\hat{x}\hat{x}} = \hat{\sigma}_0^2 (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1
}

$$**Propagation to derived quantities** (e.g., distance between two adjusted points):

$ $ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\sigma_d^2 = \mathbf{J}\mathbf{C}_{\hat{x}\hat{x}}\mathbf{J}^T $$

where $\mathbf{J} $ contains partial derivatives $\partial d/\partial x_1, \partial d/\partial y_1, \partial d/\partial x_2, \partial d/\partial y_2 $.

### 3.2 Sequential Error Propagation

When observations flow through multiple processing stages:

1. **Raw observation** → $\sigma_\text{raw} $ 2. **Instrument correction** →$\sigma_\text{inst}^2 = \sigma_\text{raw}^2 + \sigma_\text{cal}^2 $ 3. **Atmospheric correction** →$\sigma_\text{corr}^2 = \sigma_\text{inst}^2 + \sigma_\text{atmo}^2 $ 4. **Parameter estimation** →$\mathbf{C}_{\hat{x}\hat{x}} = (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1} $ At each stage, the covariance propagates forward via the Jacobian of the applied transformation.

### 3.3 Nonlinear Error Propagation (Monte Carlo)

When nonlinearity is severe (large $\sigma $ relative to curvature), first-order linearisation may be inaccurate. Use **Monte Carlo simulation**:

1. Draw $ N $ samples from $\mathbf{x} \sim \mathcal{N}(\mathbf{\mu}_x, \mathbf{C}_x) $ 2. Compute $\mathbf{y}^{(i)} = \mathbf{f}(\mathbf{x}^{(i)}) $ for each sample
3. Estimate $\mathbf{C}_y $ from the sample covariance of $\{\mathbf{y}^{(i)}\} $ This is the "gold standard" for validating first-order propagation.

---

## 4. Geodetic Applications

### 4.1 Co-factor Matrix from GNS
S

$ $\mathbf{Q}_{xx} = (\mathbf{H}^T\mathbf{H})^{-1} $$

Position standard deviations $ $\sigma_X = \sigma_\rho\sqrt{q_{XX}}, \quad \sigma_Y = \sigma_\rho\sqrt{q_{YY}}, \quad \sigma_Z = \sigma_\rho\sqrt{q_{ZZ}} $$

**PDOP:**$\sqrt{\text{tr}(\mathbf{Q}_{xx}[1:3,1:3])} $— relationship between geometry and precision.

### 4.2 Geodetic → ECEF Error Propagation

Given coordinate covariance $\mathbf{C}_{\phi\lambda h} $:

$ $\mathbf{C}_{XYZ} = \mathbf{J} \, \mathbf{C}_{\phi\lambda h} \, \mathbf{J}^
T

$$

Jacobian: $ $

\mathbf{J} = \begin{bmatrix}
-(M+h)\sin\phi\cos\lambda & -(N+h)\cos\phi\sin\lambda & \cos\phi\cos\lambda \\
-(M+h)\sin\phi\sin\lambda & (N+h)\cos\phi\cos\lambda & \cos\phi\sin\lambda \\
(M+h)\cos\phi & 0 & \sin\phi
\end{bmatrix
}

$$ ### 4.3 Leveling Error Propagation $ $\sigma_H = \sigma \sqrt{n} = \epsilon \sqrt{L}

$$

where $\sigma $= standard deviation per setup,$ n $ = number of setups,$\epsilon $= standard deviation per km,$ L $ = line length in km.

**Classic rule of thumb:**$\epsilon \approx 1.5 $ mm/$\sqrt{\text{km}} $ for precision leveling,$\approx 3 $ mm/$\sqrt{\text{km}} $ for technical leveling.

### 4.4 Distance Measurement Erro
r

$ $ D = ct/2 \implies \sigma_D^2 = \left(\frac{c}{2}\sigma_t\right)^2 + \left(\frac{t}{2}\sigma_c\right)^2 $$| Source | Typical $\sigma $ | Contribution |
|--------|-----------------|-------------|
| Time-of-flight | 100 ps | 15 mm |
| Refractive index | 1 ppm | 1 mm/km |
| Instrument offset | 1 mm | 1 mm (constant) |

---

## 5. Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\sigma_y^2 = \sum (\partial f/\partial x_i)^2 \sigma_{x_i}^2 $ | Independent propagation | Simple uncorrelated |
| $\mathbf{C}_y = \mathbf{J} \mathbf{C}_x \mathbf{J}^T $ | Matrix propagation | General form |
| $\sigma_H = \sigma\sqrt{n} $ | Leveling propagation | Survey design |
| $\sigma_{\text{sum}} = \sqrt{\sum \sigma_i^2} $ | Sum of independent errors | RSS |
| $\sigma_y/|y| = \sqrt{\sum(n_i\sigma_{x_i}/x_i)^2} $ | Relative propagation | Products and powers |

---

## 6. Common Mistakes

1. **Assuming errors always add linearly:** For independent errors, use RSS ($\sqrt{\sum\sigma_i^2} $), not direct sum.
2. **Ignoring covariance:** When inputs are correlated, $\sigma_y^2 = \sum\sigma_i^2 + 2\sum\sigma_{ij} $— the covariance term can double or cancel the variance.
3. **Wrong Jacobian:** The chain rule applies; verify each $\partial f/\partial x_i $ is correct for your specific function.
4. **Neglecting nonlinearity:** For large $\sigma $, first-order propagation under/over-estimates. Check with Monte Carlo.
5. **Mixing cofactor and covariance:** $\mathbf{C} = \sigma_0^2 \mathbf{Q} $— don't forget the variance of unit weight scaling.

---

## Related Concepts

- [[Probability Foundations]] — Foundation

- [[Least Squares Adjustment]] — Variance-covariance of estimates

- [[Linear Algebra Fundamentals]] — Matrix propagation

- [[Descriptive Statistics]] — Standard deviation, variance

- [[Hypothesis Testing]] — Testing propagated errors

---

## Study Problems

1. **Recall:** A distance of 100 m is measured with $\sigma = 2 $ mm. What is the propagated error in $ y = 2.5 \times \text{distance} $?
2. **Application:** A GNSS survey reports $\sigma_X = 5 $ mm,$\sigma_Y = 5 $ mm,$\sigma_Z = 15 $ mm, all uncorrelated. What is the propagated horizontal position error? Vertical error?
3. **Derivation:** Show that an angle $\theta = \arctan(Y/X) $ has error $\sigma_\theta = \sqrt{\sigma_X^2 + \sigma_Y^2}/D $.
4. **Real-world:** Design a leveling line 2 km long with required accuracy 2 mm (95% confidence). Assuming $\sigma = 0.3 $ mm per setup, how many setups total and per km?

---

## Common Mistakes

1. **Assuming errors are always additive:** For products, use relative errors.
2. **Ignoring covariance:** Independent errors $\to $ sum of squares; correlated $\to $ includes covariance terms.
3. **Using the wrong Jacobian:** Always verify the transformation function.
4. **Hardware vs. propagated error:** Instrument precision $\neq$ actual field error (atmosphere, setup, etc. add to field error).

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*
