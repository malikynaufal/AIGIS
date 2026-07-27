---
code: FKD211302
name: Elektromagnetik
SKS: 4
semester: 3
department: Fisika
tags: [physics, electrodynamics, maxwell, electromagnetic-waves]
created: 2026-07-27
---

# FKD211302 — Elektromagnetik

## Course Overview

Electromagnetism is arguably the most successful physical theory — Maxwell's equations unify electricity, magnetism, and light into a single framework. This course develops the full mathematical description of electromagnetic fields and waves, essential for understanding GNSS signal propagation, antenna design, and the structure of modern physics.

**Contact Hours:** 4 SKS (3 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Dasar II, Kalkulus II, Persamaan Diferensial
**Co-requisites:** Fisika Klasik

---

## 📋 Topics & Outline

### Unit 1: Vector Calculus for Electromagnetism (Weeks 1–3)

- **Gradient:** ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) — rate of change of scalar field

- **Divergence:** ∇·**E** = ∂E_x/∂x + ∂E_y/∂y + ∂E_z/∂z — source density

- **Curl:** ∇×**E** = determinant expression — rotation/circulation density

- **Integral theorems:**
  - Divergence theorem: ∫∫∫ (∇·**A**) dV = ∮∮ **A**·d**A**
  - Stokes' theorem: ∫∫ (∇×**A**)·d**A** = ∮ **A**·d**l**

### Unit 2: Electrostatics and Magnetostatics (Weeks 4–8)

- **Maxwell's equations in matter:** full vector calculus forms

- **Electrostatics:** Poisson's equation ∇²V = -ρ/ε₀

- **Magnetostatics:** ∇×**B** = μ₀**J** (Ampere's law, differential form)

- **Biot-Savart law** and **Ampere's circuital law** (revisited in full generality)

- **Boundary conditions** for E and B at interfaces between materials

- **Dielectrics and magnetic materials:** polarization, magnetization

- **Energy in fields:** u = ½(ε₀E² + B²/μ₀)

- Maxwell's displacement current and the inconsistency of static Ampere's law

### Unit 3: Electromagnetic Waves (Weeks 9–12)

- **Faraday's law:** ∇×**E** = -∂**B**/∂t

- **Maxwell's equations (complete, in vacuum):**
  ```
  ∇·E = 0         ∇×E = -∂B/∂t
  ∇·B = 0         ∇×B = μ₀ε₀ ∂E/∂t
  ```

- **Wave equation:** ∇²**E** = μ₀ε₀ ∂²**E**/∂t²

- **Plane wave solutions:** **E** = **E₀** cos(**k**·**r** - ωt)

- **Phase velocity:** c = 1/√(μ₀ε₀) = 2.998×10⁸ m/s

- **Poynting vector:** **S** = **E**×**B**/μ₀ (energy flux)

- **Reflection and transmission** at interfaces

- **Polarization:** linear, circular, elliptical

- **Dispersion** in materials: phase vs. group velocity

### Unit 4: Radiation and Antennas (Weeks 13–16)

- **Retarded potentials:** V and **A** depend on retarded time

- **Electric dipole radiation:** E ∝ 1/r · sinθ · d²p/dt²

- **Radiation from accelerating charges:** Larmor formula

- **Power radiated:** P = (μ₀/6πc) (|ä|)²  (Larmor)

- **Antenna basics:** dipole antenna, radiation pattern

- **Applications to geodesy:** GNSS signal propagation, ionospheric effects

---

## 🔬 Key Equations (Maxwell's Complete Set)

```
Maxwell I:     ∇·D = ρ_f         (Gauss)
Maxwell II:    ∇·B = 0            (No magnetic monopoles)
Maxwell III:   ∇×E = -∂B/∂t       (Faraday)
Maxwell IV:   ∇×H = J_f + ∂D/∂t  (Ampere-Maxwell)

Wave equation: ∇²E - μ₀ε₀∂²E/∂t² = 0
Phase velocity: c = 1/√(μ₀ε₀) ≈ 2.998×10⁸ m/s
Poynting vector: S = E×H
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Express Maxwell's equations in both integral and differential forms
2. Derive electromagnetic wave solutions from Maxwell's equations
3. Calculate wave propagation, reflection, and polarization properties
4. Apply the Poynting vector to compute energy transport
5. Understand radiation mechanisms from accelerating charges
6. Connect electromagnetic theory to GNSS signal propagation and ionospheric physics

---

## 📚 References

1. Griffiths, D.J. (2017). *Introduction to Electrodynamics*, 4th ed. Cambridge.
2. Purcell, E.M. (2013). *Electricity and Magnetism*, 3rd ed. Cambridge.
3. Jackson, J.D. (1998). *Classical Electrodynamics*, 3rd ed. Wiley. (Advanced reference)
4. Zangwill, A. (2013). *Modern Electrodynamics*. Cambridge.
5. MIT OCW 8.07 Electromagnetism II: https://ocw.mit.edu
