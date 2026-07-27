---
code: FKD211401
name: Mekanika Kuantum
SKS: 3
semester: 4
department: Fisika
tags: [physics, quantum-mechanics, schrodinger, wavefunction, probability]
created: 2026-07-27
---

# FKD211401 — Mekanika Kuantum

## Course Overview

Quantum mechanics — the most successful physical theory ever devised. This course introduces the wave-function description of microscopic systems, the Schrödinger equation, and the probabilistic interpretation that revolutionized physics. From atomic spectra to quantum sensors, QM underlies every modern physics technology.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Klasik, Fisika Dasar II, Persamaan Diferensial
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Foundations of Quantum Mechanics (Weeks 1–4)
- **Historical crisis:** blackbody radiation (Planck), photoelectric effect (Einstein), atomic spectra
- **Wave-particle duality:** photons and electrons exhibit both wave and particle behavior
- **Double-slit experiment:** the central mystery of QM
- **Heisenberg uncertainty principle:** Δx·Δp ≥ ℏ/2
- **De Broglie wavelength:** λ = h/p, matter waves
- **Wave function** ψ(x,t): probabilistic interpretation (Born rule)
- **Probability density:** P(x) = |ψ(x)|²
- **Normalization:** ∫|ψ|²dx = 1

### Unit 2: The Schrödinger Equation (Weeks 5–9)
- **Time-dependent Schrödinger equation (TDSE):**
  ```
  iℏ ∂ψ/∂t = -ℏ²/(2m) ∂²ψ/∂x² + Vψ
  ```
- **Time-independent Schrödinger equation (TISE):**
  ```
  -ℏ²/(2m) d²ψ/dx² + Vψ = Eψ
  ```
- **Infinite square well (particle in a box):**
  ```
  ψ_n(x) = √(2/L) sin(nπx/L)
  E_n = n²π²ℏ²/(2mL²)
  ```
- **Finite potential well:** tunneling solutions
- **Harmonic oscillator:**
  ```
  ψ_n(x) = H_n(x) exp(-mωx²/(2ℏ))
  E_n = (n+½)ℏω
  ```
- **Step potentials** and scattering/reflection

### Unit 3: Quantum Mechanics in 3D (Weeks 10–13)
- **Schrödinger equation in 3D:** ∇²ψ + 2m(E-V)/ℏ² ψ = 0
- **Hydrogen atom** (spherical symmetry):
  - Separation: ψ(r,θ,φ) = R_nl(r) Y_{lm}(θ,φ)
  - Radial equation → discrete energy levels
  - **Bohr:** E_n = -13.6 eV/n² (hydrogen)
  - Spherical harmonics Y_{lm} → shapes of orbitals
- **Angular momentum:** **L** = **r**×**p** as operator
  - L² and L_z eigenvalues: l(l+1)ℏ², mℏ
- **Spin:** magnetic moment, Stern-Gerlach experiment
- **Pauli matrices** and two-component spinors

### Unit 4: Quantum Formalism and Applications (Weeks 14–16)
- **Observables as operators:** position, momentum, energy
- **Eigenstates and eigenvalues:** Aψ = aψ
- **Commutation relations:** [x, p] = iℏ
- **Dirac notation:** |ψ⟩ ⟨φ|
- **Entanglement** and superposition (Bell's theorem overview)
- **Quantum tunneling:** scanning tunneling microscope (STM)
- **Sensors based on quantum phenomena:**
  - Atomic clocks (GPS timing!)
  - Quantum gravimeters
  - SQUIDs for magnetic field measurement
  - NV-diamond magnetometers

---

## 🔬 Key Equations

```
Schrödinger (time-dependent):   iℏ∂ψ/∂t = Ĥψ
Schrödinger (time-independent): Ĥψ = Eψ
Uncertainty:                    Δx·Δp ≥ ℏ/2
de Broglie:                     λ = h/p
Harmonic oscillator:            E_n = (n+½)ℏω
Hydrogen atom:                  E_n = -13.6 eV / n²
Angular momentum:               L² = l(l+1)ℏ²
Commutator:                     [x, p] = iℏ
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Write and interpret the Schrödinger equation for simple systems
2. Solve for energy levels and wavefunctions of infinite wells, harmonic oscillators, and hydrogen
3. Calculate probabilities of measurement outcomes from wavefunctions
4. Understand uncertainty principles and their physical implications
5. Explain how quantum phenomena are exploited in precise sensors
6. Understand the role of quantum mechanics in GPS atomic clocks

---

## 📚 References

1. Griffiths, D.J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge.
2. Liboff, R. (2003). *Introductory Quantum Mechanics*, 4th ed. Addison-Wesley.
3. Shankar, R. (2012). *Principles of Quantum Mechanics*, 2nd ed. Springer.
4. Feynman, R.P. (1965). *Feynman Lectures on Physics, Vol. III* (Intuitive overview)
5. MIT OCW 8.04 Quantum Physics I: https://ocw.mit.edu
