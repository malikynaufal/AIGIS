---
tags: [physics, concept, aigis]
aliases: [Quantum Foundations]
created: 2026-07-27
---

# Quantum Foundations (Dasar-Dasar Kuantum)

> Wave-particle duality, Schrödinger equation, operators, uncertainty principle, measurement problem, Hilbert space

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Quantum mechanics describes nature at the smallest scales through states in Hilbert space, where observables are Hermitian operators, measurements are probabilistic, and the wavefunction evolves via the Schrödinger equation.

> **Geodesy Connection:** Atomic clock physics for GNSS satellites; quantum gravimeters; fundamental limits on measurement precision; Heisenberg uncertainty in precision metrology.

---

## 🧮 Key Equations

### Postulates of Quantum Mechanics (Postulat Mekanika Kuantum)

**Postulate 1 — State Vector:** The state of a quantum system is completely described by a state vector $|\Psi\rangle$ in a Hilbert space $\mathcal{H}$.

**Postulate 2 — Observables:** Every measurable physical quantity is represented by a Hermitian (self-adjoint) operator $\hat{A}$ acting on $\mathcal{H}$, satisfying $\hat{A} = \hat{A}^\dagger$.

**Postulate 3 — Measurement:** The possible outcomes of measuring $\hat{A}$ are the eigenvalues $a_n$ of $\hat{A}$:

$$
\hat{A}|a_n\rangle = a_n|a_n\rangle
$$

The probability of obtaining outcome $a_n$ when the system is in state $|\Psi\rangle$ is:

$$
P(a_n) = |\langle a_n | \Psi \rangle|^2
$$

**Postulate 4 — Collapse:** Upon measurement yielding $a_n$, the state collapses to $|a_n\rangle$.

**Postulate 5 — Time Evolution:** The time evolution of an isolated quantum system is governed by the Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}|\Psi(t)\rangle = \hat{H}|\Psi(t)\rangle
$$

### Hilbert Space (Ruang Hilbert)

A Hilbert space is a complete inner product space. The inner product (produk dalam) is:

$$
\langle \phi | \psi \rangle = \int \phi^*(x)\psi(x) \, dx
$$

The normalization condition requires:

$$
\langle \Psi | \Psi \rangle = \int |\Psi(x)|^2 \, dx = 1
$$

An orthonormal basis $\{|e_n\rangle\}$ satisfies:

$$
\langle e_m | e_n \rangle = \delta_{mn}, \quad \sum_n |e_n\rangle\langle e_n| = \hat{1}
$$

### Time-Dependent Schrödinger Equation

$$
i\hbar\frac{\partial \Psi(x,t)}{\partial t} = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)\right]\Psi(x,t)
$$

### Time-Independent Schrödinger Equation

For time-separable solutions $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$:

$$
\hat{H}\psi(x) = E\psi(x)
$$

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi
$$

### Position and Momentum Operators

$$
\hat{x}\psi(x) = x\psi(x)
$$

$$
\hat{p}\psi(x) = -i\hbar\frac{\partial\psi}{\partial x}
$$

These satisfy the canonical commutation relation:

$$
[\hat{x}, \hat{p}] = i\hbar
$$

### Generalized Uncertainty Principle (Prinsip Ketidakpastian)

For any two observables $\hat{A}$ and $\hat{B}$:

$$
\Delta A \cdot \Delta B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|
$$

For position and momentum:

$$
\Delta x \cdot \Delta p \geq \frac{\hbar}{2}
$$

For energy and time:

$$
\Delta E \cdot \Delta t \geq \frac{\hbar}{2}
$$

### Expectation Values and Observables

$$
\langle \hat{A} \rangle = \langle \Psi | \hat{A} | \Psi \rangle = \int \Psi^* \hat{A} \Psi \, dx
$$

$$
\langle x \rangle = \int \Psi^* x \Psi \, dx
$$

$$
\langle p \rangle = \int \Psi^* \left(-i\hbar\frac{\partial}{\partial x}\right) \Psi \, dx
$$

The variance (varians) is:

$$
(\Delta A)^2 = \langle \hat{A}^2 \rangle - \langle \hat{A} \rangle^2
$$

### Ehrenfest's Theorem (Teorema Ehrenfest)

Quantum expectation values obey classical equations of motion:

$$
m\frac{d\langle x\rangle}{dt} = \langle p\rangle, \quad \frac{d\langle p\rangle}{dt} = -\left\langle\frac{\partial V}{\partial x}\right\rangle
$$

This bridges quantum and classical mechanics in the correspondence limit.

### Density Matrix (Matriks Densitas)

For a general state (possibly mixed):

$$
\hat{\rho} = \sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

Time evolution: $i\hbar\frac{d\hat{\rho}}{dt} = [\hat{H}, \hat{\rho}]$ (von Neumann equation).

Expectation values: $\langle \hat{A} \rangle = \text{Tr}(\hat{\rho}\hat{A})$.

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** A quantum state is like a musical chord — it contains multiple notes (eigenstates) simultaneously. Measurement is like listening and hearing only one note — you've gained information but lost the chord.

> **Key insight:** The uncertainty principle is not about measurement disturbance — it's a fundamental property of quantum states. A particle cannot simultaneously have precise position and momentum because these are conjugate variables linked by the Fourier transform of the wavefunction.

> **Geodesy intuition:** The Heisenberg limit $\Delta E \Delta t \geq \hbar/2$ sets the ultimate precision for atomic clocks. Current cesium clocks achieve fractional frequency stability of $\sim 10^{-16}$, limited by quantum noise. Quantum-enhanced sensors could improve geodetic measurements beyond classical limits.

---

## 🧪 Worked Examples

### Example 1: Particle in a Box — Energy Quantization

**Problem:** A particle of mass $m$ is confined to a 1D box of width $L$ with infinite walls. Find the energy eigenvalues and the probability of finding the particle in the left half of the box for the ground state.

**Solution:**

Inside the box ($0 < x < L$), the time-independent Schrödinger equation is:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
$$

With boundary conditions $\psi(0) = \psi(L) = 0$, the solutions are:

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}
$$

For the ground state ($n=1$), the probability of finding the particle in $0 < x < L/2$:

$$
P = \int_0^{L/2} |\psi_1(x)|^2 \, dx = \frac{2}{L}\int_0^{L/2} \sin^2\left(\frac{\pi x}{L}\right) dx = \frac{1}{2}
$$

This makes sense by symmetry — the ground state probability density is symmetric about $x = L/2$.

---

### Example 2: Commutator and Uncertainty Relation

**Problem:** Verify the commutation relation $[\hat{x}, \hat{p}] = i\hbar$ and use it to derive the position-momentum uncertainty relation.

**Solution:**

Acting on an arbitrary test function $\psi(x)$:

$$
[\hat{x}, \hat{p}]\psi = \hat{x}(\hat{p}\psi) - \hat{p}(\hat{x}\psi) = x\left(-i\hbar\frac{\partial\psi}{\partial x}\right) - \left(-i\hbar\frac{\partial}{\partial x}\right)(x\psi)
$$

$$
= -i\hbar x\frac{\partial\psi}{\partial x} + i\hbar\left(\psi + x\frac{\partial\psi}{\partial x}\right) = i\hbar\psi
$$

Therefore $[\hat{x}, \hat{p}] = i\hbar$.

For the general uncertainty relation, let $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}$:

$$
\Delta x \cdot \Delta p \geq \frac{1}{2}|\langle[\hat{x}, \hat{p}]\rangle| = \frac{1}{2}|i\hbar| = \frac{\hbar}{2}
$$

This is the Heisenberg uncertainty principle — a fundamental bound on simultaneous knowledge of position and momentum.

---

## 📚 References

| Source | Topic | URL |
|--------|-------|-----|
| MIT OCW 8.04 (Quantum Physics I) | Postulates, Hilbert space, Schrödinger equation | https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/ |
| OpenStax University Physics Vol. 3 | Wave-particle duality, uncertainty principle | https://openstax.org/books/university-physics-volume-3/ |
| HyperPhysics — Quantum Mechanical Model | Schrödinger equation, wavefunctions | http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/qm.html |
| Sakurai, Modern Quantum Mechanics (arXiv:1503.07657) | Postulates of QM, Hilbert space formalism | https://arxiv.org/abs/1503.07657 |
| Griffiths, Introduction to QM (arXiv:1805.09907) | Ch. 1-3: Foundations, formalism | https://arxiv.org/abs/1805.09907 |

---

## 🔗 Links

- **Related:** [[Quantum_Systems]] · [[Quantum_Applications]]
- **Geodesy:** [[Atomic_Clocks]] · [[GNSS_Positioning]]
- **Study Pack:** [[_Study Packs/]]

*Created by AIGIS Physics Specialist · Part of the AIGIS Knowledge Machine*
*Last updated: 2026-07-27*
