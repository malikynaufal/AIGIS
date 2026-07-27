---
tags: [aigis, concept, mathematics, least-squares, adjustment, geodesy, estimation]
created: 2026-07-27
updated: 2026-07-27
---

# Least Squares Adjustment

## For Geodesy & Measurement Science

**Core Idea:** Least squares finds the parameter values that minimize the sum of squared residuals, providing the best estimate in the sense of maximum likelihood (for Gaussian errors). It is THE fundamental mathematical tool in geodesy — used in every survey adjustment, GNSS processing, gravity field modeling, and coordinate transformation.

---

## Fundamental Concepts

### The Gauss-Markov Model

$$\mathbf{y} = \mathbf{f}(\mathbf{x}) + \boldsymbol{\varepsilon} $$ | Symbol | Type | Meaning |
|--------|------|---------|
| $\mathbf{y} $ | Observation vector ($n \times 1$) | Measured quantities |
| $\mathbf{x} $ | Parameter vector ($u \times 1$) | Unknowns to estimate |
| $\mathbf{f}(\mathbf{x}) $ | Functional model | Theory relating observations to parameters |
| $\boldsymbol{\varepsilon} $ | Residual vector ($n \times 1$) | Errors $E[\boldsymbol{\varepsilon}] = 0$ |

**Stochastic model:**$E[\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^T] = \sigma_0^2 \mathbf{P}^{-1}$where $\mathbf{P} $is the weight matrix and $\sigma_0^2 $ is the prior variance factor.

### Linear Model

If $\mathbf{f}(\mathbf{x}) = \mathbf{H}\mathbf{x} $:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \boldsymbol{\varepsilon
}

$$**Normal equations:** $$

\mathbf{H}^T\mathbf{P}\mathbf{H}\hat{\mathbf{x}} = \mathbf{H}^T\mathbf{P}\mathbf{y
}

$$ **Solution:**$$\hat{\mathbf{x}} = (\mathbf{H}^T\mathbf{P}\mathbf{H})^{-1}\mathbf{H}^T\mathbf{P}\mathbf{y}

$$

### Nonlinear Model (Gauss-Newton Iteration)

For $\mathbf{f}(\mathbf{x}) $nonlinear, linearize around current estimate $\mathbf{x}_k $:

$$\mathbf{y} \approx \mathbf{f}(\mathbf{x}_k) + \mathbf{J}_k \Delta\mathbf{x}\Delta\mathbf{x}_k = (\mathbf{J}_k^T\mathbf{P}\mathbf{J}_k)^{-1}\mathbf{J}_k^T\mathbf{P}\mathbf{r}_k

$$ where $\mathbf{J}_k = \partial\mathbf{f}/\partial\mathbf{x}|_{\mathbf{x}_k} $and $\mathbf{r}_k = \mathbf{y} - \mathbf{f}(\mathbf{x}_k) $.

Iterate until $\ |\Delta\mathbf{x}\| < \epsilon $.

### Least Squares with Constraints

**Equality constraints** (Helmert): $\mathbf{C}\mathbf{x} = \mathbf{w} $Via Lagrange multipliers $$\hat{\mathbf{x}}_{con} = \hat{\mathbf{x}} + \mathbf{N}^{-1}\mathbf{C}^T(\mathbf{C}\mathbf{N}^{-1}\mathbf{C}^T)^{-1}(\mathbf{w} - \mathbf{C}\hat{\mathbf{x}})

$$

---

## Variance-Covariance of Estimate
s

$$ C_{\hat{\mathbf{x}}} = \sigma_0^2 \mathbf{N}^{-1}$$ where $\mathbf{N} = \mathbf{H}^T\mathbf{P}\mathbf{H} $ (normal matrix).

**A posteriori variance factor:*
*

$$\hat{\sigma}_0^2 = \frac{\mathbf{v}^T\mathbf{P}\mathbf{v}}{n - u} $$ where $\mathbf{v} = \mathbf{y} - \mathbf{H}\hat{\mathbf{x}} $ are the residuals.

---

## In Geodesy Context

### Weight Matrix Construction

For observations with known standard deviations $\sigma_i $:

$$\mathbf{P} = \text{diag}\left(\frac{1}{\sigma_1^2}, \frac{1}{\sigma_2^2}, \dots, \frac{1}{\sigma_n^2}\right)

$$ If $\mathbf{P} = \mathbf{C}^{-1} $ (inverse covariance), the solution is the **BLUE** (Best Linear Unbiased Estimate).

### Block Diagonal Structure in GNSS

For $m $receivers and $n $satellites observed over $T$ epochs:

The normal matrix has a **block diagonal + coupling** structure

$$\mathbf{N} = \begin{bmatrix} \mathbf{N}_{11} & \mathbf{N}_{12} \\ \mathbf{N}_{21} & \mathbf{N}_{22} \end{bmatrix} $$

-$\mathbf{N}_{11} $: receiver positions (dense)

- $\mathbf{N}_{22} $: ambiguity block (sparse, integer-valued)

- $\mathbf{N}_{12}, \mathbf{N}_{21} $: coupling (position–ambiguity)

This structure enables efficient solvers (Cholesky factorization, partitioning).

### Precision Dilution of Precision (DOP)

$$\mathbf{Q}_{xx} = (\mathbf{H}^T\mathbf{H})^{-1} $$ | DOP | Formula | Interpretation |
|-----|---------|---------------|
| GDOP | $\sqrt{\text{tr}(\mathbf{Q}_{xx})} $ | Geometry quality |
| PDOP | $\sqrt{Q_{xx} + Q_{yy} + Q_{zz}} $ | 3D position quality |
| HDOP | $\sqrt{Q_{xx} + Q_{yy}} $ | Horizontal quality |
| VDOP | $\sqrt{Q_{zz}} $ | Vertical quality |
| TDOP | $\sqrt{Q_{tt}} $ | Time/clock quality |

### Robust Estimation (M-estimation)

Replace least squares with a robust criterion to handle outliers

$$\min \sum \rho(v_i)

$$| Method |$\rho(v) $ | Property |
|--------|----------|----------|
| LS | $v^2$ | Sensitive to outliers |
| Huber | $v^2 $if $|v|<k $; $2k|v|-k^2 $otherwise | Compromise |
| L₁-norm | $|v| $ | Very robust |
| Danish | $v^2 e^{-v^2/2c^2}$ | Downweights outliers exponentially |

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\hat{\mathbf{x}} = (\mathbf{H}^T\mathbf{P}\mathbf{H})^{-1}\mathbf{H}^T\mathbf{P}\mathbf{y} $ | BLUE | Linear least squares |
| $\mathbf{v}^T\mathbf{P}\mathbf{v} = \min $ | Least squares criterion | Minimize residuals |
| $C_{\hat{x}} = \sigma_0^2 \mathbf{N}^{-1}$ | Covariance of estimates | Precision |
| $\hat{\sigma}_0^2 = \mathbf{v}^T\mathbf{P}\mathbf{v}/(n-u) $ | Variance of unit weight | Fit quality |
| $\Delta\mathbf{x} = (\mathbf{J}^T\mathbf{P}\mathbf{J})^{-1}\mathbf{J}^T\mathbf{P}\mathbf{r} $ | Gauss-Newton | Nonlinear LS |
| GDOP =$\sqrt{\text{tr}(\mathbf{N}^{-1})} $ | Dilution of precision | GNSS geometry |

---

## Related Concepts

- [[Linear Algebra Fundamentals]] — Matrix theory for normal equations

- [[Probability Foundations]] — Statistical justification

- [[Regression & Least Squares]] — Statistical curve fitting

- [[Error Propagation]] —$C_{\hat{x}} = \sigma_0^2 \mathbf{N}^{-1}$- [[GNSS]] — Practical GNSS adjustment

- [[RTK]] — Real-time least squares for positioning

- [[PPP]] — Precise point positioning

---

## Study Problems

1. **Recall:** Given 4 distance observations to 2 unknowns, write the design matrix $\mathbf{H} $, normal matrix $\mathbf{N} = \mathbf{H}^T\mathbf{H} $, and solve for $\hat{\mathbf{x}} $.
2. **Application:** In GNSS PPP, you have 40 observations (4 satellites × 10 epochs) and 13 parameters (4 positions × 10 epochs + 10 ambiguities + 1 clock bias). Compute degrees of freedom.
3. **Derivation:** Show that the least squares estimator is equivalent to the MLE under Gaussian errors.
4. **Real-world:** After a network adjustment, $\hat{\sigma}_0 = 2.3 $ (much greater than 1). What does this indicate? List possible causes and solutions.

---

## Common Mistakes

1. **Forgetting to check degrees of freedom:**$n - u$ must be positive and sufficient.
2. **Assuming $\hat{\sigma}_0^2 = 1 $ always:** It should be close to 1; values >> 1 indicate model misspecification or under-estimated observation noise.
3. **Ignoring correlations:** Off-diagonal terms in $\mathbf{P}^{-1} $ are critical for satellite-based systems.
4. **Not checking residuals after adjustment:** Large residuals signal outliers or model errors.
5. **Confusing a priori and a posteriori variance factors:** Before adjustment $\sigma_0^2$ is assumed (usually 1); after it's estimated.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*