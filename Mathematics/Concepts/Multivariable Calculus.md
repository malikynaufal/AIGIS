---
tags: [aigis, concept, mathematics, calculus, multivariable, partial-derivatives, jacobian, gradient]
created: 2026-07-27
updated: 2026-07-27
---

# Multivariable Calculus

## For Geodesy & Physics Applications

**Core Idea:** Multivariable calculus extends single-variable differentiation and integration to functions of several variables. In geodesy, this underpins coordinate transformations (Jacobians), optimization (gradients), surface integrals (geoid computation), and potential theory (gravity field modeling).

---

## Fundamental Concepts

### Partial Derivatives

For $f(x_1, x_2, \dots, x_n) $:

$ $\frac{\partial f}{\partial x_i} = \lim_{\Delta x_i \to 0} \frac{f(x_1,\dots,x_i+\Delta x_i,\dots,x_n) - f(x_1,\dots,x_i,\dots,x_n)}{\Delta x_i} $$

All other variables held constant.

### The Gradien
t

$ $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)

$$

- Points in direction of steepest ascent

- Magnitude = rate of ascent

- Orthogonal to level curves/surfaces

### Directional Derivativ
e

$ $ D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = |\nabla f| \cos\theta $$

where $\mathbf{u} $ is a unit vector in the desired direction.

### Hessian Matri
x

$ $  H = \begin{bmatrix} f_{xx} & f_{xy} & f_{xz} \\ f_{yx} & f_{yy} & f_{yz} \\ f_{zx} & f_{zy} & f_{zz} \end{bmatrix}$$

**Second derivative test (2D):**

| $ f_{xx}f_{yy} - f_{xy}^2 $ | $ f_{xx} $ | Type |
|---|---|---|
| $> 0 $|$> 0 $ | Local minimum |
| $> 0 $|$< 0 $ | Local maximum |
| $< 0 $ | — | Saddle point |
| $= 0 $ | — | Inconclusive |

### The Jacobian Matrix

For $\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m $:

$ $  J = \begin{bmatrix} \frac{\partial F_1}{\partial x_1} & \cdots & \frac{\partial F_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial F_m}{\partial x_1} & \cdots & \frac{\partial F_m}{\partial x_n} \end{bmatrix}$$---

## In Geodesy Context

### Geodetic ↔ ECEF Jacobian

For the transformation $ (\phi, \lambda, h) \to (X, Y, Z) $:

$ $  J = \begin{bmatrix} -(N+h)\sin\phi\cos\lambda & -(N+h)\cos\phi\sin\lambda & \cos\phi\cos\lambda \\ -(N+h)\sin\phi\sin\lambda & (N+h)\cos\phi\cos\lambda & \cos\phi\sin\lambda \\ (N(1-e^2)+h)\cos\phi & 0 & \sin\phi \end{bmatrix}+ \text{ terms with } \partial N/\partial\phi $$

This Jacobian is essential for error propagation from geodetic to ECEF coordinates.

### Least-Squares in Matrix Form

The normal equations arise from setting the gradient of the least-squares criterion to zero

$ $\frac{\partial}{\partial \mathbf{x}} (\mathbf{r}^T \mathbf{P} \mathbf{r}) = 0 \implies \mathbf{J}^T \mathbf{P} \mathbf{J} \Delta\mathbf{x} = -\mathbf{J}^T \mathbf{P} \mathbf{r} $$

# ## Surface Integrals on the Ellipsoid

The total mass of a body: $ M = \iiint \rho\, dV $ The gravitational potential at a point outside

$ $

U(\mathbf{r}) = G \int \frac{\rho(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|}\, dV'$$

This requires multivariable integration — spherical harmonic decomposition simplifies it.

### Gradient in Optimization

To find the minimum of $\Phi(\mathbf{x}) = \mathbf{r}^T\mathbf{P}\mathbf{r} $, set $\nabla\Phi = 0 $:

$ $\nabla\Phi = 2\mathbf{J}^T\mathbf{P}\mathbf{r} = 0

$$

This gives the normal equations — the heart of least-squares estimation.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\nabla f = (\partial f/\partial x, \partial f/\partial y, \partial f/\partial z) $ | Gradient | Steepest ascent |
| $\nabla f \cdot \mathbf{u} $ | Directional derivative | Rate in direction |
| $ J = \partial(x,y,z)/\partial(\phi,\lambda,h) $ | Jacobian | Coordinate transform |
| $\nabla \cdot \mathbf{F} $ | Divergence | Source density |
| $\nabla \times \mathbf{F} $ | Curl | Irrotational flow |

---

## Related Concepts

- [[Derivatives]] — Single-variable basis

- [[Integrals]] — Multiple integrals for volumes

- [[Linear Algebra Fundamentals]] — Jacobians, gradients

- [[Least Squares Adjustment]] — Optimization on multivariable functions

- [[Error Propagation]] — Jacobian-based covariance transformation

- [[Differential Equations intro]] — Partial differential equations

---

## Study Problems

1. **Recall:** Compute $\nabla f $ for $ f(x,y,z) = x^2 + y^2 + z^2 $ at the point $ (1,2,3) $.
2. **Application:** Compute the Jacobian for the transformation $ (\phi, \lambda, h) \to (X,Y,Z) $ at $ (\phi = -6°, \lambda = 106°, h = 50\ \text{m}) $ on WGS84.
3. **Derivation:** Show that the gradient of the ellipsoidal potential $ U(\phi, \lambda, h) $ gives the gravity vector.
4. **Real-world:** In PPP, you minimize a weighted sum of squared residuals over 40 epochs with 13 parameters. What are the dimensions of $\mathbf{J} $, $\mathbf{P} $, and $\mathbf{N} $?

---

## Common Mistakes

1. **Evaluating the gradient in the wrong direction:** The gradient points in direction of increasing $ f $, not decreasing.
2. **Swapping rows and columns of the Jacobian:** The $ (i,j) $ element is $\partial F_i / \partial x_j $.
3. **Confusing $\partial $ with $  d $:** Partial derivatives hold other variables constant; total derivatives account for chain dependence.
4. **Ignoring the chain rule in multivariable contexts:** $ df/dt = \nabla f \cdot d\mathbf{r}/dt$.

---

*Concept maintained by AIGIS — part of [[Mathematics MOC]]*