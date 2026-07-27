---
tags: [physics, study-pack, aigis, quantum-mechanics]
aliases: [Quantum Mechanics Intro, QM Study Pack]
created: 2026-07-27
updated: 2026-07-27
---

# 📚 Study Pack — Quantum Mechanics Introduction
_Wave Function, Uncertainty Principle, Particle in a Box

---

## 1. The Birth of Quantum Theory

### Blackbody Radiation (Planck, 1900)
Energy comes in discrete packets (quanta):
$$E = nh\nu \quad (n = 0, 1, 2, \dots)$$
where $h = 6.626 \times 10^{-34}$ J·s (Planck's constant).

Planck distribution:
$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT} - 1}$$

### Photoelectric Effect (Einstein, 1905)
Light acts as particles (photons) with $E = h\nu$.

$$K_{\max} = h\nu - \phi$$

where $\phi$ = work function of metal.

### Compton Scattering (1923)
$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta)$$

Confirmed light's momentum: $p = h/\lambda = \hbar k$.

---

## 2. The Wave Function

### Born Interpretation
The wave function $\Psi(\vec{r}, t)$ contains all information:
$$P(\vec{r}, t) = |\Psi(\vec{r}, t)|^2 d^3r$$

is the probability of finding the particle in volume $d^3r$.

### Normalization
$$\int_{-\infty}^{\infty} |\Psi(\vec{r}, t)|^2 d^3r = 1$$

### Time-Dependent Schrödinger Equation
$$i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$$

### Time-Independent Schrödinger Equation
For stationary states $\Psi(\vec{r},t) = \psi(\vec{r})e^{-iEt/\hbar}$:
$$-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$$

This is an eigenvalue equation: energy eigenvalues and eigenfunctions.

---

## 3. Heisenberg Uncertainty Principle

$$\sigma_x \sigma_p \geq \frac{\hbar}{2}$$

This is not about measurement limitations — it's a fundamental property of quantum states.

### Other Uncertainty Relations
$$\sigma_E \sigma_t \geq \frac{\hbar}{2}$$
$$\sigma_\theta \sigma_\ell \geq \frac{\hbar}{2}$$

### Example: Electron in Atom
Electron confined to $\sigma_x \approx 10^{-10}$ m (Bohr radius):
$$\sigma_p \geq \frac{\hbar}{2\sigma_x} \approx 5.3 \times 10^{-25} \text{ kg·m/s}$$
$$K = \frac{\sigma_p^2}{2m_e} \approx 1.5 \text{ eV}$$

---

## 4. Particle in a Box (Infinite Square Well)

### Setup
$$V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & \text{elsewhere}\end{cases}$$

### Solutions
Wave functions (boundary conditions: $\psi(0) = \psi(L) = 0$):
$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \dots$$

### Energy Eigenvalues
$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}$$

### Key Properties
- **Zero-point energy:** $E_1 = \pi^2\hbar^2/(2mL^2) > 0$
- **Energy spacing:** $E_{n+1} - E_n = (2n+1)E_1$
- **Nodes:** $\psi_n$ has $n-1$ nodes
- **Orthogonality:** $\int_0^L \psi_m \psi_n dx = \delta_{mn}$

### 2D Box
$$E_{n_x,n_y} = \frac{\pi^2\hbar^2}{2m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right)$$

### 3D Box
$$E_{n_x,n_y,n_z} = \frac{\pi^2\hbar^2}{2m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right)$$

---

## 5. Quantum Harmonic Oscillator

### Potential
$$V(x) = \frac{1}{2}m\omega^2 x^2$$

### Energy Levels
$$E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \dots$$

- Zero-point energy: $E_0 = \frac{1}{2}\hbar\omega$
- Evenly spaced: $\Delta E = \hbar\omega$

### Ladder Operators
$$\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right), \quad \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)$$

$$[\hat{a}, \hat{a}^\dagger] = 1$$
$$\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right) = \hbar\omega\left(\hat{N} + \frac{1}{2}\right)$$

**Ground state:** $\hat{a}|0\rangle = 0 \implies \psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/(2\hbar)}$

---

## 6. Operators and Commutators

### Position and Momentum Operators
$$\hat{x} = x, \quad \hat{p} = -i\hbar\frac{\partial}{\partial x}$$

### Canonical Commutation Relation
$$[\hat{x}, \hat{p}] = \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar$$

### Measurement Outcomes
- Measuring $\hat{A}$ on state $|\psi\rangle$ yields eigenvalue $a_n$ with $|\psi_n\rangle$
- After measurement: system collapses to $|\psi_n\rangle$
- Average (expectation): $\langle A \rangle = \langle\psi|\hat{A}|\psi\rangle$

---

## 7. Applications in Physics and Geodesy

### Atomic Spectra
Energy level transitions give emission/absorption lines:
$$\Delta E = h\nu = E_n - E_m$$

### GNSS Atomic Clocks
Caesium/Rubidium clocks use atomic transition frequencies as time standards:
$$\nu_{Cs} = 9,192,631,770 \text{ Hz (exact, defines the second)}$$

### Quantum Metrology
Entanglement and squeezed states can improve precision beyond standard quantum limit.

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $i\hbar\partial_t\Psi = H\Psi$ | TDSE | Time evolution |
| $-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$ | TISE | Energy eigenvalues |
| $\sigma_x\sigma_p \geq \hbar/2$ | Uncertainty principle | Quantum limits |
| $E_n = n^2\pi^2\hbar^2/(2mL^2)$ | Particle-in-box | Confined particles |
| $E_n = \hbar\omega(n+1/2)$ | Harmonic oscillator | Vibrational spectra |
| $\hat{H} = \hbar\omega(\hat{N}+1/2)$ | QHO Hamiltonian | Ladder operator approach |

---

## Problems
1. An electron is confined to a box of width 0.1 nm. Calculate the energy levels $E_1$ through $E_4$ in eV.
2. Find the probability of finding a particle in a 1D box between $x = L/4$ and $x = 3L/4$ for the ground state.
3. Show that $[\hat{a}, \hat{a}^\dagger] = 1$ using $[\hat{x}, \hat{p}] = i\hbar$.
4. A quantum dot is modeled as a 3D box of side 5 nm. Find the ground state energy.
5. Using the uncertainty principle, estimate the ground state energy of hydrogen.

---

## References
- Griffiths, "Introduction to Quantum Mechanics" (Ch. 1-4)
- Feynman Lectures Vol. III (Ch. 1-10)
- MIT OCW 8.04: Quantum Physics I
- OpenStax University Physics Vol. 3 (Ch. 5-6)

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
