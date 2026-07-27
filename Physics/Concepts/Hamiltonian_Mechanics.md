---
tags: [physics, concept, aigis]
aliases: [Hamiltonian Mechanics]
created: 2026-07-27
---

# Hamiltonian Mechanics (Mekanika Hamiltonian)

> Hamilton's equations, phase space, canonical transformations, Poisson brackets, Liouville's theorem

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Hamiltonian mechanics reformulates classical mechanics in phase space $(q, p)$, where the Hamiltonian function $H(q, p, t)$ generates equations of motion via partial derivatives — providing a symmetric and powerful framework for canonical transformations, perturbation theory, and quantum mechanics.

> **Geodesy Connection:** Phase space analysis for orbital mechanics, perturbation theory in satellite orbits, symplectic integrators for long-term orbit propagation, and Hamiltonian structure of geophysical fluid dynamics.

---

## 🧮 Key Equations

### Hamiltonian Definition

The Hamiltonian is obtained from the Lagrangian via a Legendre transformation (Transformasi Legendre):

$$
H(q, p, t) = \sum_i p_i \dot{q}_i - \mathcal{L}(q, \dot{q}, t)
$$

where $p_i = \frac{\partial \mathcal{L}}{\partial \dot{q}_i}$ are the canonical momenta. For natural systems where the Lagrangian does not explicitly depend on time and the potential is velocity-independent, $H$ equals the total energy:

$$
H = T + V
$$

### Hamilton's Canonical Equations (Persamaan Kanonik Hamilton)

Hamilton's equations are a system of first-order ODEs in phase space:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

These replace the second-order Lagrangian equations with an equivalent but more symmetric first-order system. The $2n$ phase space coordinates $(q_1, \ldots, q_n, p_1, \ldots, p_n)$ fully specify the state.

### Poisson Brackets (Kurung Poisson)

The Poisson bracket of two functions $f(q, p, t)$ and $g(q, p, t)$ is:

$$
\{f, g\} = \sum_i \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)
$$

Key properties:

$$
\{q_i, q_j\} = 0, \quad \{p_i, p_j\} = 0, \quad \{q_i, p_j\} = \delta_{ij}
$$

Time evolution of any observable $f$ is given by:

$$
\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}
$$

### Hamilton's Equations in Poisson Bracket Form

$$
\dot{q}_i = \{q_i, H\}, \quad \dot{p}_i = \{p_i, H\}
$$

### Canonical Transformations (Transformasi Kanonik)

A transformation $(q, p) \to (Q, P)$ is canonical if it preserves the Poisson bracket structure:

$$
\{Q_i, Q_j\} = 0, \quad \{P_i, P_j\} = 0, \quad \{Q_i, P_j\} = \delta_{ij}
$$

A transformation is canonical if and only if there exists a generating function $F$ such that:

$$
p_i = \frac{\partial F}{\partial q_i}, \quad Q_i = \frac{\partial F}{\partial P_i}
$$

### Generating Functions

| Type | Generator | Relations |
|------|-----------|-----------|
| $F_1(q, Q, t)$ | $p_i = \partial F_1 / \partial q_i$ | $P_i = -\partial F_1 / \partial Q_i$ |
| $F_2(q, P, t)$ | $p_i = \partial F_2 / \partial q_i$ | $Q_i = \partial F_2 / \partial P_i$ |
| $F_3(p, Q, t)$ | $q_i = -\partial F_3 / \partial p_i$ | $P_i = -\partial F_3 / \partial Q_i$ |
| $F_4(p, P, t)$ | $q_i = -\partial F_4 / \partial p_i$ | $Q_i = \partial F_4 / \partial P_i$ |

### Liouville's Theorem (Teorema Liouville)

The phase space volume is preserved under Hamiltonian flow:

$$
\frac{d\rho}{dt} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0
$$

This means the phase space "fluid" is incompressible — a fundamental result for statistical mechanics.

### Action-Angle Variables (Variabel Aksi-Sudut)

For integrable systems with action variables $J_i$ and angle variables $w_i$:

$$
J_i = \frac{1}{2\pi} \oint p_i \, dq_i
$$

$$
\dot{J}_i = 0, \quad \dot{w}_i = \omega_i = \frac{\partial H}{\partial J_i}
$$

These variables are particularly useful in celestial mechanics and perturbation theory.

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** Think of phase space as a "state map" — each point $(q, p)$ is a unique snapshot of the system. Hamiltonian flow traces paths through this map like wind currents on a globe.

> **Key insight:** Hamilton's equations reveal a deep symmetry between coordinates and momenta — they play identical roles. This symmetry is the foundation of canonical quantization, where $q$ and $p$ become operators.

> **Geodesy intuition:** Satellite orbits in perturbed Keplerian motion can be described using Hamiltonian formalism, where the perturbation is a small modification to the Keplerian Hamiltonian. Symplectic integrators preserve the Hamiltonian structure, making them ideal for long-term orbit propagation.

---

## 🧪 Worked Examples

### Example 1: Hamiltonian for a Simple Pendulum

**Problem:** Derive the Hamiltonian and Hamilton's equations for a simple pendulum of mass $m$ and length $l$.

**Solution:**

The Lagrangian in terms of angle $\theta$ is:

$$
\mathcal{L} = \frac{1}{2}ml^2\dot{\theta}^2 + mgl\cos\theta
$$

The canonical momentum is:

$$
p_\theta = \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = ml^2\dot{\theta}
$$

The Hamiltonian is:

$$
H = p_\theta \dot{\theta} - \mathcal{L} = \frac{p_\theta^2}{2ml^2} - mgl\cos\theta
$$

Hamilton's equations give:

$$
\dot{\theta} = \frac{\partial H}{\partial p_\theta} = \frac{p_\theta}{ml^2}
$$

$$
\dot{p}_\theta = -\frac{\partial H}{\partial \theta} = -mgl\sin\theta
$$

Substituting the first into the second recovers $\ddot{\theta} + \frac{g}{l}\sin\theta = 0$.

---

### Example 2: Canonical Transformation to Action-Angle Variables

**Problem:** Find a canonical transformation that converts the 1D harmonic oscillator Hamiltonian $H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 q^2$ into action-angle variables.

**Solution:**

The action variable is computed from one complete cycle:

$$
J = \frac{1}{2\pi} \oint p \, dq = \frac{1}{2\pi} \oint \sqrt{2m\left(H - \frac{1}{2}m\omega^2 q^2\right)} \, dq
$$

The orbit in phase space is an ellipse: $\frac{p^2}{2mH} + \frac{m\omega^2 q^2}{2H} = 1$. The area of this ellipse is $\pi \cdot \sqrt{2mH} \cdot \sqrt{2H/(m\omega^2)} = 2\pi H/\omega$.

Therefore:

$$
J = \frac{H}{\omega} \quad \Longrightarrow \quad H = \omega J
$$

Hamilton's equations become trivial:

$$
\dot{J} = 0, \quad \dot{w} = \omega
$$

The motion is simply $w(t) = \omega t + w_0$, showing that action-angle variables reveal the periodicity of the system.

---

## 📚 References

| Source | Topic | URL |
|--------|-------|-----|
| MIT OCW 8.033 (Classical Mechanics) | Hamiltonian formalism, canonical transformations | https://ocw.mit.edu/courses/8-033-classical-mechanics-fall-2017/ |
| OpenStax Classical Mechanics | Hamiltonian mechanics, phase space | https://openstax.org/details/books/classical-mechanics |
| Goldstein, Classical Mechanics (arXiv:math-ph/0511064) | Ch. 9: Hamiltonian mechanics, canonical transformations | https://arxiv.org/abs/math-ph/0511064 |
| HyperPhysics — Phase Space | Hamiltonian, Liouville theorem | http://hyperphysics.phy-astr.gsu.edu/hbase/classm/hamton.html |
| Cambridge DAMTP Lecture Notes | Action-angle variables, perturbation theory | https://www.damtp.cam.ac.uk/user/tong/dynamics.html |

---

## 🔗 Links

- **Related:** [[Newtonian_Mechanics]] · [[Lagrangian_Mechanics]]
- **Geodesy:** [[Orbital_Mechanics]] · [[Gravitational_Potential_Theory]]
- **Study Pack:** [[_Study Packs/]]

*Created by AIGIS Physics Specialist · Part of the AIGIS Knowledge Machine*
*Last updated: 2026-07-27*
