---
tags: [physics, concept, aigis]
aliases: [Lagrangian Mechanics]
created: 2026-07-27
---

# Lagrangian Mechanics (Mekanika Lagrangean)

> Lagrangian, Euler-Lagrange equations, generalized coordinates, symmetries, Noether's theorem, constraints

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Lagrangian mechanics reformulates classical mechanics using the principle of stationary action, focusing on the scalar Lagrangian $\mathcal{L} = T - V$ rather than vector forces — automatically handling constraints through generalized coordinates.

> **Geodesy Connection:** Essential for complex geophysical systems, orbital perturbation modeling, and deriving the equations of motion for deformable rotating bodies.

---

## 🧮 Key Equations

### The Lagrangian (Fungsi Lagrangean)

$$
\mathcal{L}(q_i, \dot{q}_i, t) = T - V
$$

where $T$ is kinetic energy, $V$ is potential energy, $q_i$ are generalized coordinates, and $\dot{q}_i$ are generalized velocities.

### Euler-Lagrange Equations (Persamaan Euler-Lagrange)

For each generalized coordinate $q_i$:

$$
\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} = 0
$$

The quantity $p_i = \frac{\partial \mathcal{L}}{\partial \dot{q}_i}$ is the generalized momentum conjugate to $q_i$.

### Principle of Stationary Action (Prinsip Stasioner Aksi)

The action is defined as:

$$
S[q] = \int_{t_1}^{t_2} \mathcal{L}(q_i, \dot{q}_i, t) \, dt
$$

The true path is the one for which $\delta S = 0$ — the action is stationary (a minimum, maximum, or saddle point).

### Generalized Momentum (Momentum Tergeneralisasi)

$$
p_i = \frac{\partial \mathcal{L}}{\partial \dot{q}_i}
$$

For a particle in Cartesian coordinates, this reduces to the usual linear momentum. In angular coordinates, it gives angular momentum.

### Generalized Force

The generalized force $Q_i$ corresponding to coordinate $q_i$ is:

$$
Q_i = \sum_j F_j \frac{\partial x_j}{\partial q_i}
$$

### Constraints (Batasan/Kendala)

**Holonomic constraints** (kendala holonomic) can be written as:

$$
f(q_1, q_2, \ldots, q_n, t) = 0
$$

These reduce the number of independent coordinates. For example, a pendulum is constrained to move on a circle: $x^2 + y^2 = \ell^2$.

**Non-holonomic constraints** cannot be integrated into position-only form, such as rolling without slipping:

$$
dx - R\, d\theta = 0
$$

### Lagrange Multipliers (Perkalian Lagrange)

For systems with constraints $\lambda_k f_k(q_i, t) = 0$, the modified equations are:

$$
\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} = \sum_k \lambda_k \frac{\partial f_k}{\partial q_i}
$$

The multipliers $\lambda_k$ represent constraint forces.

### Noether's Theorem (Teorema Noether)

Every continuous symmetry of the Lagrangian corresponds to a conserved quantity:

| Symmetry | Conserved Quantity |
|----------|-------------------|
| Time translation: $\mathcal{L}$ independent of $t$ | Energy: $E = \sum_i \dot{q}_i \frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \mathcal{L}$ |
| Spatial translation: $\mathcal{L}$ independent of $q_i$ | Momentum: $p_i = \partial \mathcal{L}/\partial \dot{q}_i$ |
| Rotational symmetry: $\mathcal{L}$ independent of $\phi$ | Angular momentum: $L_z = \partial \mathcal{L}/\partial \dot{\phi}$ |

### Routhian (Fungsi Routh)

For cyclic coordinates, the Routhian eliminates them:

$$
\mathcal{R}(q, \dot{q}, p_{\text{cyclic}}) = \mathcal{L} - \sum_{\text{cyclic}} p_k \dot{q}_k
$$

### Velocity-Dependent Potentials

When forces cannot be derived from a scalar potential, use the generalized potential:

$$
\mathcal{L} = T - V(q, \dot{q}, t)
$$

For the Lorentz force on a charged particle:

$$
\mathcal{L} = \frac{1}{2}mv^2 - q\phi + q\mathbf{v} \cdot \mathbf{A}
$$

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** Nature follows the path of least resistance (action). A ball rolling downhill takes the path that minimizes the integral of kinetic minus potential energy — just as light follows Fermat's principle of least time.

> **Key insight:** By using generalized coordinates, we automatically account for system constraints without solving for constraint forces. A double pendulum in Lagrangian mechanics needs only two coordinates instead of four.

> **Geodesy intuition:** The Lagrangian approach is fundamental to geophysical fluid dynamics (geostrophic equations), satellite orbit perturbation theory ( disturbing function ), and the rotation of deformable Earth models.

---

## 🧪 Worked Examples

### Example 1: Double Pendulum

**Problem:** Derive the equations of motion for a double pendulum with masses $m_1, m_2$ and lengths $\ell_1, \ell_2$ using generalized coordinates $\theta_1, \theta_2$.

**Solution:**

The positions of the masses are:

$$
x_1 = \ell_1\sin\theta_1, \quad y_1 = -\ell_1\cos\theta_1
$$

$$
x_2 = \ell_1\sin\theta_1 + \ell_2\sin\theta_2, \quad y_2 = -\ell_1\cos\theta_1 - \ell_2\cos\theta_2
$$

The kinetic energy is:

$$
T = \frac{1}{2}(m_1 + m_2)\ell_1^2\dot{\theta}_1^2 + \frac{1}{2}m_2\ell_2^2\dot{\theta}_2^2 + m_2\ell_1\ell_2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)
$$

The potential energy is:

$$
V = -(m_1 + m_2)g\ell_1\cos\theta_1 - m_2 g\ell_2\cos\theta_2
$$

The Euler-Lagrange equations for $\theta_1$:

$$
(m_1 + m_2)\ell_1^2\ddot{\theta}_1 + m_2\ell_1\ell_2\ddot{\theta}_2\cos(\theta_1 - \theta_2) + m_2\ell_1\ell_2\dot{\theta}_2^2\sin(\theta_1 - \theta_2) + (m_1 + m_2)g\ell_1\sin\theta_1 = 0
$$

This coupled nonlinear system exhibits chaotic behavior — a hallmark of Lagrangian mechanics applied to multi-body problems.

---

### Example 2: Bead on a Rotating Wire — Noether's Theorem

**Problem:** A bead slides on a frictionless wire rotating at constant angular velocity $\omega$. Using the Lagrangian, find the equation of motion and identify any conserved quantities.

**Solution:**

The bead's position is $r$ (distance along the wire from the rotation axis). In the rotating frame, the kinetic energy is:

$$
T = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}mr^2\omega^2
$$

Since the wire is frictionless and horizontal, $V = 0$. The Lagrangian is:

$$
\mathcal{L} = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}mr^2\omega^2
$$

The Euler-Lagrange equation:

$$
m\ddot{r} - mr\omega^2 = 0 \quad \Longrightarrow \quad \ddot{r} = r\omega^2
$$

This describes exponential radial motion: $r(t) = r_0 \cosh(\omega t)$ if the bead starts at rest.

The Lagrangian does not depend on time explicitly, so the energy $E = \frac{1}{2}m\dot{r}^2 - \frac{1}{2}mr^2\omega^2$ (note the minus sign — this is the Jacobi integral in the rotating frame) is conserved. This is not ordinary energy because the rotating frame is non-inertial.

---

## 📚 References

| Source | Topic | URL |
|--------|-------|-----|
| MIT OCW 8.01 (Classical Mechanics) | Lagrangian mechanics, generalized coordinates | https://ocw.mit.edu/courses/8-01-classical-mechanics-fall-2016/ |
| OpenStax Classical Mechanics | Lagrangian formulation, action principle | https://openstax.org/details/books/classical-mechanics |
| Goldstein, Classical Mechanics (arXiv:math-ph/0511064) | Ch. 1-2: Lagrangian mechanics, variational principles | https://arxiv.org/abs/math-ph/0511064 |
| HyperPhysics — Lagrangian | Principle of least action, Euler-Lagrange | http://hyperphysics.phy-astr.gsu.edu/hbase/classm/lagrange.html |
| Lanczos, The Variational Principles of Mechanics (arXiv:1605.08795) | Historical and mathematical foundations | https://arxiv.org/abs/1605.08795 |

---

## 🔗 Links

- **Related:** [[Newtonian_Mechanics]] · [[Hamiltonian_Mechanics]]
- **Geodesy:** [[Orbital_Mechanics]] · [[Gravitational_Potential_Theory]]
- **Study Pack:** [[_Study Packs/]]

*Created by AIGIS Physics Specialist · Part of the AIGIS Knowledge Machine*
*Last updated: 2026-07-27*
