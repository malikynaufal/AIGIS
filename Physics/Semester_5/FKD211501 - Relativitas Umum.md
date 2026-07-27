---
code: FKD211501
name: Relativitas Umum
SKS: 3
semester: 5
department: Fisika
tags: [physics, general-relativity, spacetime, black-holes, cosmology]
created: 2026-07-27
---

# FKD211501 — Relativitas Umum

## Course Overview

General relativity — Einstein's geometric theory of gravity describing spacetime as a dynamical entity curved by mass and energy. This course covers tensor calculus, the Einstein field equations, Schwarzschild solution, and astrophysical applications (black holes, gravitational waves) with special attention to GPS relativistic corrections.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Klasik, Elektromagnetik, Persamaan Diferensial, Aljabar Linear
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Special Relativity (Weeks 1–3)

- **Lorentz transformations:** x′ = γ(x - vt), t′ = γ(t - vx/c²)
 - γ = 1/√(1 - v²/c²)

- **Spacetime interval:** (Δs)² = (cΔt)² - (Δx)² - (Δy)² - (Δz)²
 - Timelike (Δt² > Δx² + Δy² + Δz²): causally connected
 - Spacelike: not causally connected

- **Four-vectors:** 4-position (ct, x, y, z), 4-momentum (E/c, p_x, p_y, p_z)

- **Energy-momentum relation:** E² = (pc)² + (mc²)²

- **GPS clocks:** special relativistic correction due to orbital speed (~7 μs/day)

### Unit 2: Curved Spacetime and Tensor Calculus (Weeks 4–8)

- **Equivalence principle:** locally, gravity is indistinguishable from acceleration

- **Metric tensor g_μν:** fundamental object encoding geometry
 - For flat spacetime (Minkowski): ds² = -c²dt² + dx² + dy² + dz²

- **Covariant vs. contravariant** vectors and tensors

- **Christoffel symbols** Γ^ρ_μν — connection coefficients
 - Measure how basis vectors change from point to point

- **Geodesic equation:** d²x^μ/dτ² + Γ^μ_νρ dx^ν/dτ dx^ρ/dτ = 0
 - Free-fall paths = geodesics in curved spacetime

- **Riemann curvature tensor** R^ρ_σμν — measure of curvature
 - If R = 0 everywhere, spacetime is flat

### Unit 3: Einstein Field Equations (Weeks 9–12)

- **The Einstein Field Equations (EFE):**
 ```
 G_μν = R_μν - ½g_μνR = (8πG/c⁴) T_μν
 ```
 - G_μν = Einstein tensor (geometry)
 - T_μν = Stress-energy tensor (matter/energy content)
 - G_μν is automatically divergenceless (Bianchi identity)

- **Newtonian limit:** EFE reduces to Poisson's equation ∇²Φ = 4πGρ for weak fields

- **Schwarzschild solution** (static, spherically symmetric mass):
 ```
 ds² = -(1-2GM/rc²)c²dt² + (1-2GM/rc²)⁻¹dr² + r²dΩ²
 ```
 - Event horizon at r_s = 2GM/c² (Schwarzschild radius)
 - Gravitational time dilation: τ = t√(1-2GM/rc²)

### Unit 4: Applications (Weeks 13–16)

- **Black holes:**
 - Schwarzschild black hole: singularity + event horizon
 - Kerr (rotating) black hole: ergosphere, frame-dragging

- **Gravitational redshift:** light loses energy escaping a gravitational well
 - GPS correction: ~45 μs/day from GR (combined with SR: total ~38 μs/day)

- **Perihelion precession** of Mercury (43 arcseconds/century)

- **Gravitational lensing:** deflection of light by massive objects

- **Gravitational waves:** predicted by Einstein 1916, detected by LIGO 2015

- **Cosmology** (intro): FRW metric, expanding universe, ΛCDM model

---

## 🔬 Key Equations

```
Interval: ds² = -(c²)dt² + dx² + dy² + dz² (flat)
Geodesic eqn: d²x^μ/dτ² + Γ^μ_νρ (dx^ν/dτ)(dx^ρ/dτ) = 0
Einstein field: G_μν + Λg_μν = (8πG/c⁴)T_μν
Schwarzschild: r_s = 2GM/c²
GR time dilation: τ = t·√(1 - r_s/r)
GPS corrections: SR: -7 μs/day, GR: +45 μs/day, Net: +38 μs/day
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Apply four-vectors and Lorentz transformations in special relativity
2. Understand the metric description of curved spacetime
3. Calculate relativistic corrections (time dilation, Doppler shift)
4. Explain the Schwarzschild solution and black hole properties
5. Understand the physical meaning of the gravitational time dilation correction in GPS
6. Connect general relativity to precision geodetic measurements (reference frames, clock modeling)

---

## 📚 References

1. Schutz, B. (2009). *A First Course in General Relativity*, 2nd ed. Cambridge.
2. Hartle, J.B. (2003). *Gravity: An Introduction to Einstein's General Relativity*. Addison-Wesley.
3. Carroll, S. (2019). *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge.
4. Hobson, M.P. et al. (2006). *General Relativity: An Introduction for Physicists*. Cambridge.
5. Ashby, N. (2003). *Relativity in the Global Positioning System*. Living Rev. Relativity.