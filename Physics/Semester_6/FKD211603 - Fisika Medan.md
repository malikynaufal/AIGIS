---
code: FKD211603
name: Fisika Medan
SKS: 3
semester: 6
department: Fisika
tags: [physics, field-theory, gauge-theory, advanced-electrodynamics, standard-model]
created: 2026-07-27
---

# FKD211603 — Fisika Medan

## Course Overview

Classical and quantum field theories — the mathematical framework underlying all modern fundamental physics. This course develops the Lagrangian field theory approach, gauge symmetries, and introduces the conceptual foundation for the Standard Model of particle physics and general relativity as field theories.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Klasik, Elektromagnetik, Fisika Inti dan Partikel
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Classical Field Theory (Weeks 1–4)

- **Fields as dynamical variables:** φ(x,t) replacing particle coordinates

- **Lagrangian density:** L = T - V = ½(∂φ/∂t)² - ½(∇φ)² - V(φ)

- **Euler-Lagrange equation for fields:**
  ```
  ∂_μ (∂L/∂(∂_μφ)) - ∂L/∂φ = 0
  ```

- **Wave equation:** Klein-Gordon equation: (∂_μ∂^μ + m²)φ = 0

- **Noether's theorem for fields:** conserved currents from symmetries
  - Example: global U(1) symmetry → conserved charge

- **Energy-momentum tensor:** T^μν = ∂L/∂(∂_μφ) ∂^νφ - g^μν L

### Unit 2: Electrodynamics as Gauge Theory (Weeks 5–8)

- **Electromagnetic four-potential:** A^μ = (V/c, A_x, A_y, A_z)

- **Field tensor:** F^μν = ∂^μA^ν - ∂^νA^μ

- **Maxwell's equations** in covariant form:
  ```
  ∂_μF^μν = μ₀J^ν  (inhomogeneous)
  ∂_[μF_νρ] = 0    (homogeneous)
  ```

- **Gauge invariance:** A^μ → A^μ + ∂^μΛ (U(1) gauge symmetry)

- **Minimal coupling:** ∂_μ → D_μ = ∂_μ + ieA_μ (introducing charge)

- **Lagrangian of QED:** L = -¼F_μνF^μν + ψ̄(iγ^μD_μ - m)ψ

### Unit 3: Non-Abelian Gauge Theories (Weeks 9–12)

- **Gauge symmetry generalization:** from U(1) to SU(2), SU(3)

- **Yang-Mills theory:** non-Abelian gauge fields with self-interaction
  ```
  D_μ = ∂_μ - igA_μ^a T^a  (T^a = generators of the gauge group)
  ```

- **Strong force (QCD):** SU(3)_color, 8 gluons, quarks carry color
  - **Color confinement:** gluons carry color charge → self-interaction → confinement
  - **Asymptotic freedom:** quarks are free at high energy (Gross, Wilczek, Politzer: Nobel 2004)

- **Electroweak theory:** SU(2)_L × U(1)_Y → U(1)_EM
  - Higgs mechanism: spontaneous symmetry breaking
  - Mass generation for W± and Z⁰ bosons

### Unit 4: Applications and Overview (Weeks 13–16)

- **Spontaneous symmetry breaking and the Higgs mechanism**
  ```
  φ = (1/√2)(v + h) exp(iθ/v) → Higgs field with VEV v ≈ 246 GeV
  ```

- **Anomalies** in field theories

- **Solitons** and topological defects (vortices, monopoles)

- **General relativity as a field theory:** Einstein-Hilbert action

- **Quantization** overview: path integrals, functional methods

- **Future directions:** string theory, loop quantum gravity (qualitative overview)

- **Connections to measurement:** how gauge theories underpin fundamental constants

---

## 🔬 Key Equations

```
Klein-Gordon:      (∂_μ∂^μ + m²)φ = 0
Dirac equation:    (iγ^μ∂_μ - m)ψ = 0
Maxwell (covariant): ∂_μF^μν = μ₀J^ν
Noether current:   j^μ = ∂L/∂(∂_μφ) δφ
Gauge transformation: A^μ → A^μ + ∂^μΛ
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Formulate classical field theories using Lagrangian densities
2. Understand electrodynamics as a U(1) gauge theory
3. Explain non-Abelian gauge theories and the Standard Model structure
4. Describe the Higgs mechanism and spontaneous symmetry breaking
5. Appreciate how field theories provide the language for fundamental physics
6. Connect gauge theory to fundamental constants and symmetries used in measurement

---

## 📚 References

1. Peskin, M.E. & Schroeder, D.V. (1995). *An Introduction to Quantum Field Theory*. Westview.
2. Greiner, W. (2000). *Field Quantization*. Springer.
3. Srednicki, M. (2007). *Quantum Field Theory*. Cambridge. (Free draft at web.physics.ucsb.edu)
4. Ryder, L.H. (1996). *Quantum Field Theory*, 2nd ed. Cambridge.
5. Schwartz, M.D. (2014). *Quantum Field Theory and the Standard Model*. Cambridge.
