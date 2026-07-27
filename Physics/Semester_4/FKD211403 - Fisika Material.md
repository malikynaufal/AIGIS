---
code: FKD211403
name: Fisika Material
SKS: 3
semester: 4
department: Fisika
tags: [physics, materials, crystal-structure, solid-state, properties]
created: 2026-07-27
---

# FKD211403 — Fisika Material

## Course Overview

The physics of materials — exploring how atomic and electronic structure determines macroscopic properties. This course covers crystal lattices, band theory, semiconductor physics, and material characterization, forming the basis for understanding sensor materials used in modern geodetic instruments.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Kimia Dasar, Fisika Dasar II
**Co-requisites:** Mekanika Kuantum (may be taken simultaneously)

---

## 📋 Topics & Outline

### Unit 1: Crystal Structure (Weeks 1–4)

- **Bravais lattices:** 14 lattice types in 3D

- **Primitive and unit cells:** simple cubic (SC), body-centered cubic (BCC), face-centered cubic (FCC), hexagonal close-packed (HCP)

- **Crystal directions and planes:** Miller indices (hkl)

- **Reciprocal lattice:** connection to diffraction

- **X-ray diffraction:** Bragg's law nλ = 2d sin θ

- **X-ray diffraction patterns** — powder diffraction for crystal identification

### Unit 2: Lattice Dynamics and Thermal Properties (Weeks 5–8)

- **Lattice vibrations:** monatomic vs. diatomic chains

- **Phonon dispersion:** ω vs. k relation, acoustic vs. optical branches

- **Phonon heat capacity:** Einstein vs. Debye models
  - Debye model: C_v = 9Nk_B(T/θ_D)³ ∫₀^{θ_D/T} x⁴eˣ/(eˣ-1)² dx
  - Low T limit: C_v ∝ T³

- **Thermal expansion** and lattice anharmonicity

- **Thermal conductivity** — phonon scattering mechanisms (Umklapp, impurities)

### Unit 3: Electronic Properties of Solids (Weeks 9–12)

- **Bloch's theorem:** ψ_k(r) = u_k(r)e^{ik·r}

- **Nearly free electron model:** band gaps at Brillouin zone boundaries

- **Band structure:** valence band, conduction band, band gap E_g

- **Classification:** metals (no gap), semiconductors (small gap), insulators (large gap)

- **Semiconductor physics:**
  - Intrinsic: n = p = N_c exp(-E_g/2kT)
  - Extrinsic (doped): n-type (donors), p-type (acceptors)
  - Carrier mobility and conductivity: σ = nᵧqμ

- **Hall effect:** R_H = 1/(nq) — measuring carrier type and concentration

### Unit 4: Functional Materials and Applications (Weeks 13–16)

- **Piezoelectricity:** stress → voltage (sensors, actuators)

- **Ferroelectricity** and spontaneous polarization

- **Magnetic materials:** dia-, para-, ferro-, antiferro-, ferrimagnetic
  - Curie temperature: ferromagnetic → paramagnetic transition

- **Optical materials:** direct vs. indirect band gap, photodetectors, LEDs

- **Material science for geodetic instruments:**
  - Semiconductor-based sensors (accelerometers in IMUs)
  - Piezoelectric sensors in gravimeters
  - Optical materials in laser interferometers
  - Temperature-stable materials for precision metrology

---

## 🔬 Key Concepts

```
Bragg:              2d sin θ = nλ
Debye heat capacity: C_v ∝ T³ (low T)
Band gap:           E_g (eV) — material classification
Hall effect:        R_H = 1/nq
Conductivity:       σ = nqμ
Doping:             n-type (group V), p-type (group III)
Resistivity:        ρ(T) = ρ₀ + aT + bT²
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Identify crystal systems and compute Miller indices for planes and directions
2. Understand phonon dispersion and thermal properties of materials
3. Explain band theory and distinguish metals, semiconductors, and insulators
4. Analyze the Hall effect to determine carrier type and concentration
5. Explain the physical principles behind functional materials (piezoelectric, magnetic, optical)
6. Connect material properties to the design of geodetic instruments

---

## 📚 References

1. Kittel, C. (2005). *Introduction to Solid State Physics*, 8th ed. Wiley.
2. Ashcroft, N.W. & Mermin, N.D. (1976). *Solid State Physics*. Cengage.
3. Hook, J.R. & Hall, H.E. (1991). *Solid State Physics*, 2nd ed. Wiley.
4. Streetman, B.G. & Banerjee, S.K. (2015). *Solid State Electronic Devices*, 7th ed. Pearson.
5. Callister, W.D. & Rethwisch, D.G. (2018). *Materials Science and Engineering*, 10th ed. Wiley.
