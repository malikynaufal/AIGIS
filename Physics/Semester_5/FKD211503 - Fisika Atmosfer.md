---
code: FKD211503
name: Fisika Atmosfer
SKS: 3
semester: 5
department: Fisika/Geodesi
tags: [physics, atmospheric-physics, meteorology, weather, climate]
created: 2026-07-27
---

# FKD211503 — Fisika Atmosfer

## Course Overview

Atmospheric physics applies thermodynamics, fluid dynamics, and radiation physics to understand Earth's atmosphere — from the boundary layer to the ionosphere. This course is essential for understanding electromagnetic wave propagation in GNSS signals, weather effects on surveying, and satellite orbit perturbations.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Termodinamika, Mekanika Fluida, Elektromagnetik
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Atmospheric Structure and Composition (Weeks 1–4)

- **Vertical structure:** temperature profile defines layers
 - **Troposphere** (0–12 km): temperature decreases ~6.5 K/km
 - **Stratosphere** (12–50 km): ozone absorption → temperature increase
 - **Mesosphere** (50–80 km): coldest layer
 - **Thermosphere** (80–700 km): temperature rises to ~1000 K
 - **Ionosphere** (50–1000 km): free electrons, radio wave reflection

- **Atmospheric composition:** N₂ (78%), O₂ (21%), Ar (1%), trace gases (CO₂, H₂O, O₃)

- **Hydrostatic balance:** dP/dz = -ρg

- **Standard atmosphere model:** pressure/exponential: P(z) = P₀ exp(-z/H)

- **Scale height:** H = kT/mg ≈ 8.5 km (Earth's troposphere)

### Unit 2: Atmospheric Thermodynamics (Weeks 5–8)

- **Equation of state for dry air:** P = ρR_d T

- **Potential temperature:** θ = T (P₀/P)^{R_d/c_p}

- **Dry adiabatic lapse rate:** Γ_d = g/c_p ≈ 9.8 K/km

- **Moist air processes:** saturation, condensation
 - Clausius-Clapeyron for water vapor: e_s(T) ∝ exp(-L_v/R_vT)

- **Moist adiabatic lapse rate:** Γ_m < Γ_d (latent heat release)

- **Stability:** Γ_environment < Γ_d → stable; Γ_environment > Γ_d → unstable

- **Cloud formation** and atmospheric convection

### Unit 3: Atmospheric Radiation and Dynamics (Weeks 9–12)

- **Solar radiation:** blackbody at ~5800 K, 1361 W/m² solar constant

- **Earth's radiation:** blackbody at ~255 K (effective temperature)

- **Greenhouse effect:** atmosphere absorbs outgoing longwave radiation

- **Radiative transfer equation:** dI_ν/dτ = -I_ν + S_ν

- **Optical depth:** τ — measure of atmosphere's transparency to radiation

- **Geostrophic balance:** horizontal pressure gradient ↔ Coriolis force
 - Wind direction parallel to isobars in mid-latitudes

- **Thermal wind:** wind shear related to horizontal temperature gradient

- **Rossby waves** and mid-latitude weather systems

### Unit 4: Atmospheric Effects on GNSS (Weeks 13–16)

- **Tropospheric delay:** refraction of GNSS signals by neutral atmosphere
 - Zenith hydrostatic delay (ZHD): ~2.3 m
 - Zenith wet delay (ZWD): ~0.3 m (variable)

- **Troposphere models:** Saastamoinen, Hopfield, GPT2w

- **Ionospheric delay:** dispersive medium → frequency-dependent delay
 ```
 ΔL_{ion} = 40.3/f² · TEC (TEC = Total Electron Content)
 ```

- **Ionospheric effects on GNSS:** signal delay, scintillation, cycle slips

- **Ionospheric correction:** dual-frequency (L1/L2) eliminates ~99% of delay

- **Mapping functions:** projecting zenith delay to slant delay

- **Practical applications:** GNSS meteorology (PWV estimation), ionospheric tomography

---

## 🔬 Key Equations

```
Hydrostatic: dP/dz = -ρg
Dry adiabatic: Γ_d = g/c_p ≈ 9.8 K/km
Scale height: H = kT/mg
Geostrophic wind: u_g = -(1/ρf) ∂P/∂y, v_g = (1/ρf) ∂P/∂x
Tropospheric delay: ΔL_trop = ZHD · mf_h + ZWD · mf_w
Ionospheric delay: ΔL_ion = 40.3/f² · TEC
Optical depth: τ = ∫ κ_λ ρ dz
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Identify and describe the vertical layers of the atmosphere
2. Apply thermodynamic principles (adiabatic lapse rates, stability) to the atmosphere
3. Understand radiative transfer and the greenhouse effect
4. Explain geostrophic balance and large-scale atmospheric circulation
5. Model atmospheric delays on GNSS signals (tropospheric and ionospheric)
6. Understand how GNSS can be used to map water vapor and ionospheric TEC

---

## 📚 References

1. Salby, M.L. (2012). *Fundamentals of Atmospheric Physics*. Academic Press.
2. Wallace, J.M. & Hobbs, P.V. (2006). *Atmospheric Science: An Introductory Survey*, 2nd ed. Elsevier.
3. Ahrens, C.D. (2014). *Meteorology Today*, 10th ed. Cengage.
4. Hofmann-Wellenhof, B. et al. (2008). *GNSS — Global Navigation Satellite Systems*. Springer.
5. Bohm, J. & Schuh, H. (2013). *Atmospheric Effects in Space Geodesy*. Springer.
