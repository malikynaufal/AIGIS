---
title: 12. Regression & Least Squares (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, regression, least-squares, statistics, aigis, geodesy-applied]
---

# 12. Regression & Least Squares (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Regression and least squares fitting estimate model parameters from noisy observations. This is THE central technique in geodesy — used for adjustments, datum transformations, and parameter estimation.

## 1. Linear Regression

### 1.1 Simple Linear Regression

Model: $y = \beta_0 + \beta_1 x + \varepsilon $ where $\varepsilon \sim N(0, \sigma^2) $ is noise.

### 1.2 Ordinary Least Squares (OLS)

Minimise $\sum_{i=1}^n (y_i - \hat{y}_i)^2 $:

$ $\hat{\beta}_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}}\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x
}

$$

# ## 1.3 Coefficient of Determination $ $ R^2 = 1 - \frac{\text{SSE}}{\text{SST}} = 1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}$$

$ R^2 = 1 $ means perfect fit;$ R^2 = 0 $ means model explains none of the variance.

## 2. Matrix Form of Least Squares

### 2.1 General Linear Mode
l

$ $\mathbf{l} = A\mathbf{x} + \mathbf{v} $$

where:
-$\mathbf{l} $: $  n \times 1 $ observation vector
-$ A $: $  n \times u $ design matrix
-$\mathbf{x} $: $  u \times 1 $ parameter vector
-$\mathbf{v} $: $  n \times 1 $ residual vector

### 2.2 Normal Equations

Minimise $\mathbf{v}^TP\mathbf{v} $ where $  P $ is weight matrix: $ $ A^TPA\hat{\mathbf{x}} = A^TPl\hat{\mathbf{x}} = (A^TPA)^{-1}A^TPl $$

# ## 2.3 Solution Properties

-$ E[\hat{\mathbf{x}}] = \mathbf{x} $ (unbiased)
-$ C_{\hat{x}} = \sigma_0^2(A^TPA)^{-1} $ (covariance)

- Residuals: $\mathbf{v} = A\hat{\mathbf{x}} - \mathbf{l} $-$\mathbf{v}^TP\mathbf{v} $ is $\chi^2 $-distributed

### 2.4 A Priori vs A Posteriori Variance

**A priori**: $\sigma_0^2 $ known before adjustment

**A posteriori**: Estimated from residual
s

$ $\hat{\sigma}_0^2 = \frac{\mathbf{v}^TP\mathbf{v}}{n-u} $$

where $ n-u $= degrees of freedom.

## 3. Multiple Regression

Model: $ y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_kx_k + \varepsilon $

$ $\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y} $ $### 3.1 Adjusted $ R^2 $

$ $ R^2_{\text{adj}} = 1 - \frac{\text{SSE}/(n-p)}{\text{SST}/(n-1)}$$

Accounts for number of predictors $ p $.

## 4. Weighted Least Squares

When observations have different precision:

$ $\text{Weight matrix: } P = \Sigma^{-1} $$

where $\Sigma $ is covariance matrix of observations.

- Higher weight = more reliable observation

- Equal weights = OLS special case

### 4.1 Cholesky Approac
h

$ $  P = L^TL $$

Transform: $\tilde{A} = LA $,$\tilde{l} = Ll $ Solve $\tilde{A}^T\tilde{A}\hat{\mathbf{x}} = \tilde{A}^T\tilde{l} $## 5. Nonlinear Least Squares

### 5.1 Gauss-Newton Iteration

For nonlinear model $\mathbf{l} = \mathbf{f}(\mathbf{x}) + \mathbf{v} $:

Linearize: $\mathbf{f}(\mathbf{x} + \delta\mathbf{x}) \approx \mathbf{f}(\mathbf{x}) + J\delta\mathbf{x} $ Iterate: $ $ J^TJ\delta\hat{\mathbf{x}} = J^T(\mathbf{l} - \mathbf{f}(\mathbf{x}))\mathbf{x}_{k+1} = \mathbf{x}_k + \delta\hat{\mathbf{x}}$$

# ## 5.2 Levenberg-Marquardt

Adds damping parameter $\lambda $:

$ $ (J^TJ + \lambda I)\delta\hat{\mathbf{x}} = J^T(\mathbf{l} - \mathbf{f})$ $-$\lambda $ large: gradient descent (stable)
-$\lambda $ small: Gauss-Newton (fast convergence)

## 6. Hypothesis Testing in Regression

### 6.1 t-Test for Individual Coefficient
s

$ $  t = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)} \sim t_{n-p}$$

# ## 6.2 F-Test for Model Significanc
e

$ $  F = \frac{\text{SSR}/p}{\text{SSE}/(n-p-1)} \sim F(p, n-p-1) $$

# ## 6.3 Confidence Interval
s

$ $ \hat{\beta}_j \pm t_{\alpha/2, n-p} \cdot \text{SE}(\hat{\beta}_j)

$$

# # 7. Residual Diagnostics

### 7.1 Assumptions

1. **Linearity**: $ E[\varepsilon] = 0 $ 2. **Homoscedasticity**: $\text{Var}(\varepsilon) = \sigma^2 $ 3. **Independence**: $\text{Cov}(\varepsilon_i, \varepsilon_j) = 0 $ 4. **Normality**: $\varepsilon \sim N(0, \sigma^2) $### 7.2 Diagnostic Tools

- **Residual plots**: $\hat{v}_i $ vs $\hat{y}_i $ or $ x_i $- **Normal Q-Q plot**: Check normality

- **Cook's distance**: Influential observations

- **Durbin-Watson**: Autocorrelation in residuals

## 8. Regularization

### 8.1 Ridge Regression (L2
)

$ $\hat{\mathbf{x}} = (A^TA + \alpha I)^{-1}A^T\mathbf{l} $$

Penalises large coefficients; improves stability for ill-conditioned $ A $.

### 8.2 LASSO (L1)

$ $\hat{\mathbf{x}} = \arg\min \|A\mathbf{x}-\mathbf{l}\|^2 + \alpha\|\mathbf{x}\|_1

$$

Promotes sparsity (feature selection).

## 9. Practice Problems

### Problem 1
Given data $ (1,2), (2,3), (3,5), (4,4), (5,6) $. Fit $  y = \beta_0 + \beta_1 x $.

**Solution**:
$\bar{x} = 3 $, $\bar{y} = 4 $
$ S_{xx} = \sum(x_i-3)^2 = 10 $
$ S_{xy} = \sum(x_i-3)(y_i-4) = 10 $

$\hat{\beta}_1 = 10/10 = 1 $, $\hat{\beta}_0 = 4 - 3 = 1 $

$\hat{y} = 1 + x $, $ R^2 = 0.92 $### Problem 2
Solve the normal equations for

$ $\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\mathbf{x} = \begin{bmatrix} 3 \\ 4 \end{bmatrix
}

$$**Solution**:

$ $\mathbf{x} = \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}\begin{bmatrix} 3 \\ 4 \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 2 \\ 5 \end{bmatrix}

$$

# # 10. Where Geodesy Uses This

- **ALL adjustments** — GPS, levelling, traverse, datum transform

- **Datum definition**: rank-deficient normal equations

- **Network adjustment**: large sparse systems

- **Quality control**: residuals, standard deviations

- **Prediction**: surface fitting, height interpolation

- **Error propagation**: covariance propagation

## 11. References

- OpenStax Introductory Statistics

- MIT OCW 18.650: Statistics for Applications

- Ghilani, C. (2017). *Adjustment Computations*

---

*Maintained by AIGIS.*
