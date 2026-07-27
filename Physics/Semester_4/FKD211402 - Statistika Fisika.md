---
code: FKD211402
name: Statistika Fisika (Statistical Physics)
SKS: 3
semester: 4
department: Fisika
tags: [physics, statistical-mechanics, boltzmann, phase-transitions, ensembles]
created: 2026-07-27
---

# FKD211402 — Statistika Fisika

## Course Overview

Statistical physics bridges the microscopic world of atoms and molecules with macroscopic observables like temperature and pressure. This course develops the statistical foundations of thermodynamics and explores the behavior of many-particle systems, phase transitions, and fluctuations — essential knowledge for any physicist.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Termodinamika, Statistika Dasar, Kimia Dasar
**Co-requisites:** Mekanika Kuantum

---

## 📋 Topics & Outline

### Unit 1: Statistical Foundations (Weeks 1–5)

- **Macrostate vs. microstate:** macroscopic parameters (T, P, V) vs. microscopic configurations

- **Fundamental postulate:** all accessible microstates are equally likely

- **Boltzmann entropy:** S = k_B ln Ω

- **Configurations and multiplicity:** binomial distribution for two-state systems

- **Stirling's approximation:** ln N! ≈ N ln N - N

- **The Einstein solid:** N oscillators, q quanta
 ```
 Ω(N,q) = (q+N-1)!/(q!(N-1)!)
 S = k_B [(N+q)ln(N+q) - N ln N - q ln q]
 ```

- **Temperature as a statistical concept:** 1/T = ∂S/∂U

### Unit 2: Statistical Ensembles (Weeks 6–10)

- **Microcanonical ensemble:** fixed U, V, N — the most fundamental

- **Canonical ensemble:** fixed T, V, N (Boltzmann distribution)
 - **Partition function:** Z = Σ_i e^{-βE_i}
 - **Boltzmann factor:** P_i = e^{-βE_i}/Z
 - **Connection to thermodynamics:**
 - F = -k_B T ln Z (Helmholtz free energy)
 - U = ⟨E⟩ = -∂ ln Z/∂β
 - S = k_B(ln Z + β⟨E⟩)

- **Grand canonical ensemble:** fixed μ, V, T (variable particle number)
 - Grand partition function: Ξ = Σ_N Σ_i e^{-β(E_i - μN)}
 - Fluctuations in particle number

### Unit 3: Statistical Thermodynamics (Weeks 11–14)

- Equipartition theorem: each quadratic degree of freedom gets ½k_B T of energy

- **Ideal gases:**
 - Maxwell-Boltzmann distribution of speeds:
 f(v) = 4π (m/2πkT)^{3/2} v² exp(-mv²/(2kT))
 - Sackur-Tetrode equation for monatomic ideal gas entropy

- **Photon gas (blackbody radiation):** Planck distribution, Stefan-Boltzmann law

- **Phonons in solids:** Debye model T³ law at low temperatures

- **Fermi-Dirac statistics** (fermions, Pauli exclusion principle)
 - f(E) = 1/(e^{(E-μ)/kT} + 1)
 - Fermi energy, electron gas in metals

- **Bose-Einstein statistics** (bosons)
 - f(E) = 1/(e^{(E-μ)/kT} - 1)
 - Bose-Einstein condensation

### Unit 4: Phase Transitions (Weeks 15–16)

- **Phase transitions** as singularities in thermodynamic potentials

- **First-order transitions:** latent heat, volume change (Clausius-Clapeyron)

- **Second-order transitions:** continuous (e.g., ferromagnetic/paramagnetic)

- **Order parameters:** magnetization for ferromagnet, density for liquid-gas

- **Landau theory** of phase transitions:
 - Free energy expansion in powers of order parameter
 - Critical exponents and universality

- **Ising model** and exact solution in 1D (brief)

---

## 🔬 Key Formulas

```
Boltzmann: S = k_B ln Ω
Partition fn: Z = Σ e^{-βE_i}
Free energy: F = -k_B T ln Z
Equipartition: ⟨E⟩ = ½k_B T per quadratic DOF
Maxwell-Boltzmann: f(v) = 4π(m/2πkT)^{3/2} v² e^{-mv²/(2kT)}
Fermi-Dirac: f(E) = 1/(e^{(E-μ)/kT} + 1)
Bose-Einstein: f(E) = 1/(e^{(E-μ)/kT} - 1)
Planck: u(ω) = (ℏω³/π²c³)/(e^{ℏω/kT} - 1)
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Connect microscopic statistics to macroscopic thermodynamics via partition functions
2. Apply the three statistical ensembles (microcanonical, canonical, grand canonical)
3. Compute thermodynamic quantities from partition functions
4. Distinguish between Maxwell-Boltzmann, Fermi-Dirac, and Bose-Einstein statistics
5. Analyze phase transitions using order parameters and Landau theory
6. Understand the statistical interpretation of entropy and the Second Law

---

## 📚 References

1. Kittel, C. & Kroemer, H. (1980). *Thermal Physics*, 2nd ed. W.H. Freeman.
2. Pathria, R.K. & Beale, P.D. (2011). *Statistical Mechanics*, 3rd ed. Elsevier.
3. Reif, F. (2009). *Fundamentals of Statistical and Thermal Physics*. Waveland Press.
4. Landau, L.D. & Lifshitz, E.M. (1980). *Statistical Physics, Part I*, 3rd ed. Butterworth-Heinemann.
5. MIT OCW 8.044 Statistical Physics I: https://ocw.mit.edu
