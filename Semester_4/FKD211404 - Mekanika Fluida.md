---
code: FKD211404
name: Mekanika Fluida
SKS: 3
semester: 4
department: Fisika
tags: [physics, fluid-mechanics, fluid-dynamics, navier-stokes, turbulence]
created: 2026-07-27
---

# FKD211404 — Mekanika Fluida

## Course Overview

Fluid mechanics describes the behavior of liquids and gases — from oceanic currents and atmospheric dynamics to blood flow and microfluidic devices. This course covers fluid statics, the equations of motion, potential flow, viscous flow, and an introduction to turbulence, with direct applications to geophysical and environmental systems.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Dasar I, Kalkulus II, Persamaan Diferensial
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Fluid Statics (Weeks 1–3)
- **Density and pressure:** hydrostatic equation dP/dz = -ρg
- **Pascal's principle:** pressure applied to confined fluid transmitted undiminished
- **Buoyancy:** Archimedes' principle — F_b = ρ_fluid × V_displaced × g
- **Atmospheric pressure variation:** P(z) = P₀ exp(-z/H) (isothermal atmosphere)
- **Manometers and barometers** — pressure measurement

### Unit 2: Fluid Kinematics (Weeks 4–7)
- **Flow field description:** Lagrangian (particle paths) vs. Eulerian (field variables)
- **Pathlines, streamlines, streaklines**
- **Stream function:** ψ represents flow; constant ψ = streamline
- **Reynolds transport theorem** — rate of change of extensive properties in a control volume
- **Material derivative:** D/Dt = ∂/∂t + (v·∇)
- **Continuity equation:** ∂ρ/∂t + ∇·(ρv) = 0 (mass conservation)
  - For incompressible flow: ∇·v = 0 (divergence-free velocity)
- **Acceleration field:** a = Dv/Dt = ∂v/∂t + (v·∇)v

### Unit 3: Fluid Dynamics: Euler and Navier-Stokes (Weeks 8–12)
- **Euler's equation** (inviscid flow): ρ Dv/Dt = -∇P + ρg
- **Bernoulli's equation** (for steady, inviscid, along streamline):
  - P + ½ρv² + ρgz = constant
  - Applications: Venturi meter, Pitot tube, lift on wings
- **Vorticity:** ω = ∇×v
  - Kelvin's circulation theorem: for inviscid flow, circulation is conserved
- **Potential flow:** φ such that v = ∇φ, ∇²φ = 0
- **Boundary layer concept** — Prandtl's great insight
- **Navier-Stokes equation (viscous flow):**
  ```
  ρ(∂v/∂t + (v·∇)v) = -∇P + μ∇²v + ρg
  ```
  - One of the most important/famous PDEs in all of physics
- **Reynolds number:** Re = ρUL/μ — laminar (Re < ~2000) vs. turbulent flow

### Unit 4: Applications (Weeks 13–16)
- **Poiseuille flow:** pipe flow — v(r) = (ΔP/4μL)(R² - r²), Q = πΔPR⁴/(8μL)
- **Stokes flow:** creeping flow at low Re (Re << 1)
- **Drag force:** F_d = ½ρv²·C_d·A, Stokes' law: F_d = 6πμRv
- **Lift generation:** circulation around airfoils (Kutta-Joukowski theorem)
- **Waves in fluids:** gravity waves, shallow water waves
- **Turbulence:** (intro): energy cascade (Kolmogorov), dissipation
- **Geophysical fluid dynamics:**
  - Coriolis effect and Rossby number
  - Ocean currents, atmospheric circulation
  - Tidal dynamics

---

## 🔬 Key Equations

```
Continuity:         ∂ρ/∂t + ∇·(ρv) = 0
Bernoulli:          P + ½ρv² + ρgz = const
Euler:              ρ Dv/Dt = -∇P + ρg
Navier-Stokes:      ρ Dv/Dt = -∇P + μ∇²v + ρg
Poiseuille:         Q = πΔPR⁴/(8μL)
Reynolds number:    Re = ρUL/μ
Drag:               F_d = ½ρC_dAv²
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Apply hydrostatic principles to calculate pressure distributions
2. Use Bernoulli's equation to analyze steady flow in engineering applications
3. Solve for velocity and pressure fields using the Navier-Stokes equations for simple cases
4. Predict flow regime (laminar vs. turbulent) using the Reynolds number
5. Understand drag, lift, and boundary layer effects
6. Apply fluid mechanics to geophysical problems (atmospheric and ocean currents)

---

## 📚 References

1. Batchelor, G.K. (2000). *An Introduction to Fluid Dynamics*. Cambridge. (The classic reference)
2. Kundu, P.K. et al. (2015). *Fluid Mechanics*, 6th ed. Academic Press.
3. Fox, R.W. et al. (2016). *Introduction to Fluid Mechanics*, 9th ed. Wiley.
4. White, F.M. (2015). *Fluid Mechanics*, 8th ed. McGraw-Hill.
5. Vallis, G.K. (2017). *Atmospheric and Oceanic Fluid Dynamics*, 2nd ed. Cambridge.
