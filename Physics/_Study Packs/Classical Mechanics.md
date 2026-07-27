---
tags: [physics, study-pack, aigis, mechanics, classical]
aliases: [Classical Mechanics, Classical Mechanics Pack]
created: 2026-07-12
updated: 2026-07-27
---

# 📚 Study Pack — Classical Mechanics
_Expanded: Lagrangian/Hamiltonian Formalisms

---

## 1. Newtonian Mechanics (Review)

Newton's three laws provide the foundation for classical mechanics. In inertial frames:

$$ \vec{F}_{\text{net}} = m\vec{a} = \frac{d\vec{p}}{dt} $ $

**Limitations:**

- Cannot handle rotating or non-inertial frames easily (fictitious forces needed)

- Constrained systems require solving for constraint forces

- Coordinate dependence (not manifestly covariant)

---

## 2. Lagrangian Mechanics

### Derivation of the Lagrangian
Start with **D'Alembert's Principle**: The sum of virtual work done by applied forces plus inertial forces is zero for any virtual displacement $ \delta \vec{r}_i $:

$ $ \sum_i (\vec{F}_i - m_i\vec{a}_i) \cdot \delta\vec{r}_i = 0

$$

### Generalized Coordinates
Let $ q_1, q_2, \dots, q_n $ be independent generalized coordinates. Virtual displacements

$ $ \delta \vec{r}_i = \sum_j \frac{\partial \vec{r}_i}{\partial q_j} \delta q_j

$$

### The Lagrangian
Define the scalar function

$ $ L(q, \\dot{q}, t) = T - V $$

where $ T $ is kinetic energy (all terms) and $ V $ is potential energy (conservative forces only).

### Euler-Lagrange Equation
s

$ $ \frac{d}{dt}\frac{\partial L}{\partial \\dot{q}_j} - \frac{\partial L}{\partial q_j} = 0 \\quad (j = 1, 2, \dots, n)

$$ **Proof sketch:** Substitute generalized coordinates into D'Alembert's principle, swap summation order, apply chain rule, and use the definition $ \partial\\dot{r}_i/\partial\\dot{q}_j = \partial r_i/\partial q_j $.

### Example: Simple Pendulum

- Generalized coordinate: $ \theta $ (angle from vertical)
- $ T = \frac{1}{2}m l^2 \\dot{\theta}^2 $- $ V = -mgl\cos\theta $- $ L = \frac{1}{2}m l^2 \\dot{\theta}^2 + mgl\cos\theta $ Euler-Lagrange:

$ $ \frac{d}{dt}(m l^2 \\dot{\theta}) + mgl\sin\theta = 0ml^2\ddot{\theta} + mgl\sin\theta = 0\ddot{\theta} + \frac{g}{l}\sin\theta = 0

$$

For small angles ($ \sin\theta \approx \theta $): $ \ddot{\theta} + (g/l)\theta = 0 $. Natural freq. $ \omega_0 = \sqrt{g/l} $.

### Example: Central Force Problem (Orbits)
Use polar coordinates $ (r, \theta) $:

- $ T = \frac{1}{2}m(\\dot{r}^2 + r^2\\dot{\theta}^2) $- $ V = V(r) $: gravitational, Coulomb, etc.

For gravity: $ V = -GMm/r $.

Lagrangian: $ L = \frac{1}{2}m(\\dot{r}^2 + r^2\\dot{\theta}^2) + GMm/r $**Euler-Lagrange for $ \theta $:** $ \frac{d}{dt}(mr^2\\dot{\theta}) = 0 \\implies \\ell = mr^2\\dot{\theta} = \text{const} $ (angular momentum conservation)

**Euler-Lagrange for $ r $:** $ m\ddot{r} - mr\\dot{\theta}^2 = -GMm/r^2 $

$ $ m\ddot{r} = \frac{\\ell^2}{mr^3} - \frac{GMm}{r^2} $$

---

## 3. Hamiltonian Mechanics

### Legendre Transform
Define generalized momenta

$ p_j = \frac{\partial L}{\partial \\dot{q}_j} $ The **Hamiltonian** is $ $

H(q, p, t) = \sum_j p_j \\dot{q}_j -
L

**### Hamilton's Equations **

\\dot{q}_j = \frac{\partial H}{\partial p_j}\\dot{p}_j = -\frac{\partial H}{\partial q_j}

$ These are $ 2n $ first-order ODEs (vs.$ n $ second-order from Lagrangian).

### Example: 1D Harmonic Oscillator $ L = \frac{1}{2}m\\dot{x}^2 - \frac{1}{2}kx^2 $

$ p = m\\dot{x} \\implies \\dot{x} = p/m $

$ H = p\\dot{x} - L = \frac{p^2}{m} - (\frac{1}{2}m\frac{p^2}{m^2} - \frac{1}{2}kx^2) = \frac{p^2}{2m} + \frac{1}{2}kx^2 $Hamilton's equations:

$ $ \\dot{x} = \frac{\partial H}{\partial p} = \frac{p}{m}-\\dot{p} = \frac{\partial H}{\partial x} = kx

$ Which gives the familiar: $ m\ddot{x} + kx = 0 $.

### Poisson Brackets

$ $ \{A, B\\} = \sum_j \left[\frac{\partial A}{\partial q_j}\frac{\partial B}{\partial p_j} - \frac{\partial A}{\partial p_j}\frac{\partial B}{\partial q_j}\right]

$$

Key identities:
-$\\{q_i, p_j\\} = \delta_{ij} $-$\\{q_i, q_j\\} = 0 = \\{p_i, p_j\\} $- Hamilton's equations: $\\dot{A} = \\{A, H\\} + \partial_t A $ If $\\{A, H\\} = 0 $, then $ A $ is a **constant of motion**.

---

## 4. Symmetries and Conservation Laws (Noether's Theorem)

| Symmetry | Conserved Quantity |
|----------|-------------------|
| Time translation | Energy ($ H $) |
| Spatial translation | Linear momentum ($ \vec{p} $) |
| Rotation | Angular momentum ($ \vec{L} $) |
| Galilean boost | Center-of-mass position |

---

## 5. Applications in Geodesy

### Satellite Motion

- The Kepler problem (inverted potential) is exactly solvable via Lagrangian methods

- $ J_2 $ perturbation can be treated as a correction to the Keplerian Lagrangian

- Perturbation theory via canonical transformations (Lie transforms)

### Inertial Navigation
The Hamiltonian formulation leads to elegant state-space representations needed for Kalman filtering.

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $ L = T - V $ | Lagrangian | All generalized coords |
| $ \frac{d}{dt}\frac{\partial L}{\partial \\dot{q}} - \frac{\partial L}{\partial q} = 0 $ | Euler-Lagrange | Equations of motion |
| $ H = \sum p\\dot{q} - L $ | Hamiltonian | Energy function |
| $\\dot{q} = \partial H/\partial p $ | Hamilton's eq | Phase-space dynamics |
| $\\dot{p} = -\partial H/\partial q $ | Hamilton's eq | Force in generalized coords |

---

## Problems
1. Derive the equation of motion for a double pendulum using the Lagrangian method.
2. Find the Hamiltonian for a charged particle in an electromagnetic field.
3. Show that angular momentum is conserved for central force motion using Poisson brackets.
4. Use Lagrange multipliers to derive the frictionless Atwood machine.
5. A bead slides on a rotating hoop (constant $\omega$). Write the Lagrangian and find equilibrium positions.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
