---
code: FKD211301
name: Fisika Klasik (Classical Mechanics — Advanced)
SKS: 3
semester: 3
department: Fisika
tags: [physics, classical-mechanics, lagrangian, hamiltonian, variational]
created: 2026-07-27
---

# FKD211301 — Fisika Klasik: Analytical Mechanics

## Course Overview

Advanced classical mechanics using the Lagrangian and Hamiltonian formalisms — elegant reformulations of Newtonian mechanics that reveal deep connections between symmetry and conservation laws, and provide the direct bridge to quantum mechanics and field theory. This course is the gateway to modern theoretical physics.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Dasar I, Kalkulus II, Persamaan Diferensial
**Co-requisites:** Elektromagnetik

---

## 📋 Topics & Outline

### Unit 1: Lagrangian Mechanics (Weeks 1–5)
- **Variational principles:** the principle of least action
- **Generalized coordinates:** replacing Cartesian with generalized coordinates q_i
- **Generalized velocities:** q̇_i = dq_i/dt
- **Lagrangian:** L = T - V (kinetic minus potential energy)
- **Euler-Lagrange equation:**
  ```
  d/dt(∂L/∂q̇_i) - ∂L/∂q_i = 0
  ```
- Applications:
  - Simple pendulum (θ as generalized coordinate)
  - Double pendulum
  - Atwood machine
  - Sliding bead on a wire
- **Constraints:** holonomic vs. non-holonomic
- **Generalized momentum:** p_i = ∂L/∂q̇_i

### Unit 2: Symmetries and Conservation Laws (Weeks 6–8)
- **Noether's theorem:** Every continuous symmetry → conserved quantity
  - Translational symmetry → conservation of linear momentum
  - Rotational symmetry → conservation of angular momentum
  - Time-translation symmetry → conservation of energy
- **Cyclic coordinates:** when ∂L/∂q = 0, then p_q is conserved
- **Routhian** and reduction by cyclic coordinates
- Applications: central force problems in 2D

### Unit 3: Central Force Problems (Weeks 9–12)
- **Effective potential:** V_eff(r) = V(r) + L²/(2mr²)
- **Orbits in gravitational field:**
  - Conic sections: circles, ellipses, parabolas, hyperbolas
  - Kepler's laws as consequences of 1/r potential
- **Scattering:** Rutherford scattering formula
- **Binary stars** and reduced mass system
- **Laplace-Runge-Lenz vector** and its significance

### Unit 4: Hamiltonian Mechanics (Weeks 13–16)
- **Hamiltonian:** H = Σ p_i q̇_i - L
- **Hamilton's equations (canonical equations):**
  ```
  q̇_i = ∂H/∂p_i    ṗ_i = -∂H/∂q_i
  ```
- **Phase space** and the geometry of dynamics
- **Poisson brackets:** {A, B} = Σ (∂A/∂q_i ∂B/∂p_i - ∂A/∂p_i ∂B/∂q_i)
  - Canonical transformations preserve Poisson bracket structure
  - Liouville's theorem: phase space volume is conserved
- **Generating functions** for canonical transformations
- Introduction to **Hamilton-Jacobi theory** (overview)
- Bridge to quantum mechanics: Dirac's correspondence principle

---

## 🔬 Key Equations

```
Euler-Lagrange:     d/dt(∂L/∂q̇) - ∂L/∂q = 0
Lagrangian:         L = T - V
Noether:            Symmetry → Conserved Quantity
Hamiltonian:        H = T + V  (for natural systems)
Hamilton's Eq:      q̇ = ∂H/∂p,  ṗ = -∂H/∂q
Poisson Bracket:    {A, B} = ∂A/∂q ∂B/∂p - ∂A/∂p ∂B/∂q
Kepler's 3rd:       T² = (4π²/GM)a³
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Formulate and solve mechanics problems using the Lagrangian formalism
2. Apply Noether's theorem to identify conserved quantities from symmetries
3. Solve central force problems and derive Kepler's laws
4. Transition to the Hamiltonian formulation and interpret dynamics in phase space
5. Use canonical transformations and Poisson brackets as tools
6. Appreciate the Lagrangian/Hamiltonian framework as the foundation for modern physics

---

## 📚 References

1. Goldstein, H. (2001). *Classical Mechanics*, 3rd ed. Addison-Wesley. (The standard text)
2. Landau, L.D. & Lifshitz, E.M. (1976). *Mechanics*, 3rd ed. Butterworth-Heinemann.
3. Taylor, J.R. (2005). *Classical Mechanics*. University Science Books.
4. Marion, J.B. & Thornton, S.T. (1995). *Classical Dynamics*, 4th ed. Brooks/Cole.
5. MIT OCW 8.033 Relativity (classical foundation): https://ocw.mit.edu
