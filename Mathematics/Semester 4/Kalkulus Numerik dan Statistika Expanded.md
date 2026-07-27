---
title: Semester 4 — Kalkulus Numerik dan Statistika (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, numerical, statistics, semester-4, aigis, geodesy-applied]
---

# Semester 4 — Kalkulus Numerik dan Statistika (Expanded)

**Course**: MGM211204 — Kalkulus Numerik dan Statistika 
**Credits**: 3 SKS 
**Prerequisites**: [[Kalkulus II Expanded]], [[Persamaan Diferensial]]

---

## Course Overview

This course introduces numerical methods for solving mathematical problems that cannot be solved analytically, and covers statistical methods for data analysis. It focuses on practical computational techniques used in scientific computing and geodesy.

---

## Syllabus

### Unit 1: Numerical Methods

#### 1.1 Root-Finding Methods

- **Bisection**: Reliable but slow convergence

- **Newton-Raphson**: Quadratic convergence, requires derivative

- **Secant method**: Bisection-like, does not require derivative

- **Fixed-point iteration**: $x = g(x) $conversion

**Example**: Find $\sqrt{2} $using Newton:$x_{n+1} = \frac{1}{2}(x_n + \frac{2}{x_n})$#### 1.2 Interpolation and Approximation

- **Linear interpolation**: Connecting data points

- **Polynomial interpolation**: Lagrange/Neville interpolation

- **Spline functions**: Cubic splines for smooth interpolation

- **Least squares approximation**: Fitting models to data

#### 1.3 Numerical Integration

- **Trapezoidal rule**:$\int_a^b f(x)dx \approx \frac{h}{2}[f(a)+2\sum f(x_i)+f(b)]$- **Simpson's rule**:$\int_a^b f(x)dx \approx \frac{h}{3}[f(a)+4\sum f(\text{odd})+2\sum f(\text{even})+f(b)]$

- **Gaussian quadrature**: Weighted sums with optimal nodes

- **Adaptive integration**: Error-controlled integration

#### 1.4 Ordinary Differential Equations

- **Euler method**: Simple but low accuracy

- **Runge-Kutta methods**: Higher-order methods (RK4 most common)

- **Multi-step methods**: Adams-Bashforth, Adams-Moulton

- **Stiff ODEs**: Implicit methods (backward Euler)

### Unit 2: Statistical Methods

#### 2.1 Descriptive Statistics

- **Measures of central tendency**: Mean, median, mode

- **Measures of dispersion**: Variance, standard deviation, range

- **Data visualization**: Histograms, box plots, scatter plots

#### 2.2 Probability Distributions

- Extension of probability theory for statistical inference

- Common continuous distributions: Normal, Chi-square, t, F-distributions

#### 2.3 Statistical Inference

- **Point estimation**: Methods (MLE, method of moments)

- **Interval estimation**: Confidence intervals, bootstrap

- **Hypothesis testing**: Concept of null/alternative hypotheses

- **Regression analysis**: Least squares estimation

#### 2.4 Analysis of Variance (ANOVA)

- **One-way ANOVA**: Comparing means of multiple groups

- **Two-way ANOVA**: Factorial designs

### Unit 3: Computational Techniques

#### 3.1 Matrix Computations

- **Matrix multiplication**: Algorithms and complexity

- **LU decomposition**: Factorization for solving linear systems

- **QR decomposition**: Orthogonal factorization

- **Eigenvalue problems**: Power method, QR algorithm

#### 3.2 Optimization Algorithms

- **Gradient descent**: Steepest descent methods

- **Newton's method**: Second-order optimization

- **Conjugate gradient**: Efficient for symmetric positive definite matrices

- **Linear programming**: Simplex method, interior point methods

#### 3.3 Monte Carlo Methods

- **Random number generation**: Pseudo-random number generators

- **Importance sampling**: Efficient estimation techniques

- **Markov Chain Monte Carlo**: Bayesian inference

- **Applications**: Numerical integration, optimization

### Unit 4: Software Tools and Implementation

#### 4.1 Programming Implementation

- **MATLAB**: Built-in numerical solvers

- **Python**: NumPy, SciPy, SciPy ODE solvers

- **R**: Statistical computing

- **Julia**: High-performance numerical computing

#### 4.2 Error Analysis and Precision

- **Floating point arithmetic**: IEEE 754 standard

- **Round-off error**: Sources and control

- **Truncation error**: Discretization effects

- **Stability analysis**: Numerical stability of algorithms

#### 4.3 Performance and Scalability

- **Time complexity**: Big-O notation

- **Memory requirements**: Matrix storage schemes

- **Parallel computing**: Vectorization, multi-threading

---

## Geodesy Applications

- **Numerical integration**: Computing areas from DTMs

- **Root-finding**: Solving nonlinear adjustment equations

- **ODE solvers**: orbit propagation, inertial navigation

- **Optimization**: constraint satisfaction for network design

- **Statistical tests**: hypothesis testing for observation quality

- **Linear algebra**: solving large sparse systems for least squares

- **Regression**: trend analysis in time series data

---

## References

- Burden, R.L. & Faires, J.D. (2020). *Numerical Analysis* (10th ed.)

- Strang, G. & Borre, T. (2021). *Linear Algebra for Optimization and Numerical Analysis*

- OpenStax Numerical Methods

---

➡️ [[Mathematics MOC]] | ➡️ [[Numerical Methods]]