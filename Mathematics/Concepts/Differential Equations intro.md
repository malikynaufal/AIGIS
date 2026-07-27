---
tags: [aigis, concept, mathematics, calculus, differential-equations, physics]
created: 2026-07-27
updated: 2026-07-27
---

# Differential Equations Introduction

## For Geodesy & Physics Applications

**Core Idea:** Differential equations (DEs) describe how quantities change over time or space. They are the language of physics (Newton's laws, heat conduction, wave motion) and geodesy (reference frame dynamics, satellite orbit propagation). In geodesy, DEs govern least-squares iteration and Kalman filter dynamics.

---

## Fundamental Concepts

### What is a Differential Equation?

A DE relates a function to its derivatives:

$$ F(x, y, y', y'', \dots, y^{(n)}) = 0 $ $- **Order** = highest derivative present

- **Degree** = power of the highest derivative (if polynomial in derivatives)

- **Linear** = dependent variable and all derivatives appear to the first power, no products

| Type | General Form | Example |
|------|-------------|---------|
| ODE (1st order, linear) | $ y' + P(x)y = Q(x) $ | Exponential decay |
| ODE (2nd order, linear) | $ ay'' + by' + cy = f(x) $ | Harmonic oscillator |
| PDE | $ u_t = \alpha u_{xx} $ | Heat/diffusion equation |
| Separable | $ M(x)\,dx + N(y)\,dy = 0 $ | Population growth |
| Exact | $ M\,dx + N\,dy = 0 $ with $\partial M/\partial y = \partial N/\partial x $ | Conservative force |

### First-Order ODEs

**Separable:*
*

$ $\frac{dy}{dx} = g(x)h(y) \implies \int \frac{dy}{h(y)} = \int g(x)\,d
x

$$**Linear (integrating factor):** $ $ y' + P(x)y = Q(x)\mu(x) = e^{\int P(x)\,dx}y = \frac{1}{\mu(x)} \left[\int \mu(x)Q(x)\,dx + C\right
]

$$ ### Second-Order Linear ODEs $ $

ay'' + by' + cy = f(x)$$

**Homogeneous** ($ f = 0 $) — characteristic equation:

$ $ ar^2 + br + c = 0 \implies r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$ | Discriminant | Roots | General Solution |
|-------------|-------|-----------------|
| $ b^2 - 4ac > 0 $ | Two real $ r_1, r_2 $ | $ y = c_1 e^{r_1 x} + c_2 e^{r_2 x} $ |
| $ b^2 - 4ac = 0 $ | One repeated $ r $ | $ y = (c_1 + c_2 x)e^{rx} $ |
| $ b^2 - 4ac < 0 $ | Complex $\alpha \pm \beta i $| $ y = e^{\alpha x}(c_1 \cos\beta x + c_2 \sin\beta x) $ |

---

## Systems of ODEs

A system $\mathbf{y}' = A\mathbf{y} $ has solution $ $\mathbf{y}(t) = e^{At}\mathbf{y}(0)

$$

where $ e^{At} $ is the matrix exponential.

**For diagonalizable $ A = PDP^{-1} $:**

$ $ e^{At} = Pe^{Dt}P^{-1} = P\,\text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t})\,P^{-1} $$---

## In Geodesy & Physics Context

### Satellite Orbit (Kepler Problem)

The two-body equation in polar coordinates:

$ $ \ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2}r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0

$$

From the second, angular momentum $ h = r^2\dot{\theta} $ is conserved. Substituting into the first gives the orbit equation $ $ r(t) = \frac{a(1-e^2)}{1 + e\cos\theta}$$

where $ a $= semi-major axis,$ e $ = eccentricity — an ellipse!

### Deformation Time Series Analysis

Geodetic monitoring stations measure position over time. A simple model

$ $\frac{d^2\mathbf{x}}{dt^2} + 2\lambda\frac{d\mathbf{x}}{dt} + \omega_0^2\mathbf{x} = \mathbf{f}(t)

$$

- Overshoots from tectonic events → impulse response

- Slow subsidence → particular solution

- Damping parameter $\lambda $ from viscoelastic Earth models

### Least-Squares Iteration (Newton-like)

Nonlinear least squares solves $\min \|\mathbf{r}(\mathbf{x})\|^2 $, giving the Gauss-Newton iteration:

$ $\mathbf{x}_{k+1} = \mathbf{x}_k - (J^T J)^{-1} J^T \mathbf{r} $$

This is a system of PDEs in vector form — a fixed-point DE iteration.

### Kalman Filter (State-Space)

Continuous-time Kalman filter equations:

$ $\dot{\mathbf{x}} = F\mathbf{x} + G\mathbf{w}\dot{P} = FP + PF^T + Q

$$

where $ F $= dynamics matrix,$ Q $ = process noise,$ P $ = state covariance.

These form a matrix differential equation for the covariance — fundamental to real-time GNSS navigation.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ y' + Py = Q $ | First-order linear | Exponential decay model |
| $ y = (c_1 + c_2 x)e^{rx} $ | Repeated root | Critically damped oscillator |
| $ y = e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x) $ | Complex roots | Underdamped oscillations |
| $ r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0 $ | Angular momentum conservation | Kepler orbit |
| $ r = \frac{a(1-e^2)}{1+e\cos\theta} $ | Conic orbit | Ellipse (bound orbit) |
| $\mathbf{x}_{k+1} = \mathbf{x}_k - (J^T J)^{-1} J^T \mathbf{r} $ | Gauss-Newton | GNSS positioning |
| $\dot{P} = FP + PF^T + Q $ | Riccati equation | Kalman covariance |

---

## Related Concepts

- [[Integrals]] — Solving DEs requires integration

- [[Sequences and Series]] — Power series solutions for DEs near ordinary points

- [[Multivariable Calculus]] — Partial DEs (PDEs)

- [[Numerical Methods]] — Numerical DE solvers (Euler, Runge-Kutta)

- [[Least Squares Adjustment]] — DE form of Gauss-Newton iteration

---

## Study Problems

1. **Recall:** Solve $ y' + 2xy = 0 $ with $ y(0) = 3 $. (Hint: integrating factor or separable.)
2. **Application:** A GNSS receiver uses Kalman tracking. Given $ F = \begin{bmatrix} 0 & 1 \\ -\omega_0^2 & -2\lambda \end{bmatrix} $, write the state equations and compute the natural frequency $\omega_0 $ from $ f_0 = 1/Hz $.
3. **Derivation:** Starting from Newton's law of gravitation, derive the Keplerian orbit equation from the two-body DE (use $ u = 1/r $, $ h = r^2\dot{\theta} $).
4. **Real-world:** Earth's mantle behaves like a Maxwell viscoelastic body. Write the DE that describes post-glacial rebound: $\ddot{h} + \frac{E}{\eta}\dot{h} + \frac{E}{\tau_R^2}h = \frac{L}{\eta} $ where $ E $= elastic modulus,$\eta $= viscosity. Identify the relaxation time constant.

---

## Common Mistakes

1. **Dropping constants of integration** — they determine the particular solution.
2. **Swapping order of integration in exact DEs** — check $\partial M/\partial y = \partial N/\partial x $ before concluding.
3. **Forgetting the negative sign** in spring equation: $ F = -kx $ not $ F = kx$.
4. **Treating ODE and PDE interchangeably** — they have different solution methods.
5. **Misinterpreting the characteristic equation** — the sign of the discriminant determines solution form.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*