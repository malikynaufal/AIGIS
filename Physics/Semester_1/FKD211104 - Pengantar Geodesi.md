---
code: FKD211104
name: Pengantar Geodesi
SKS: 2
semester: 1
department: Geodesi
tags: [geodesy, introduction, earth-shape, gravity, coordinate-systems]
created: 2026-07-27
---

# FKD211104 — Pengantar Geodesi

## Course Overview

An introductory survey of geodesy — the science of measuring and understanding Earth's shape, orientation in space, and gravity field. This course situates physics within the broader geodetic context, introducing students to the reference frames, coordinate systems, and measurement principles that underpin all subsequent coursework.

**Contact Hours:** 2 SKS (2 hours lecture per week)
**Prerequisites:** None
**Co-requisites:** Fisika Dasar I, Aljabar Linear

---

## 📋 Topics & Outline

### Unit 1: What is Geodesy? (Weeks 1–4)

- Definition: *"Geodesy is the Earth science of measurement and mapping"*

- Historical development: from Eratosthenes (240 BC) to satellite geodesy

- Three branches:
 - **Geometric geodesy:** shape and size of Earth
 - **Physical geodesy:** Earth's gravity field
 - **Dynamic geodesy:** Earth's rotation and orientation

- Geodesy vs. cartography vs. surveying vs. GIS

- Why geodesy matters: infrastructure, navigation, climate monitoring

### Unit 2: The Shape of the Earth (Weeks 5–8)

- Earth as an ellipsoid: semi-major axis a, semi-minor axis b

- **Reference ellipsoid:** WGS84 (a = 6,378,137 m, f = 1/298.257223563)

- Geometric relationships: latitude (geodetic, geocentric), longitude, height

- **Coordinate systems:**
 - Geodetic (φ, λ, h)
 - Cartesian ECEF (X, Y, Z)
 - Local tangent plane (E, N, U)

- **Transformations** between coordinate systems

- The geoid: equipotential surface ≈ mean sea level

- Quasigeoid and height systems: orthometric, normal, ellipsoidal heights

### Unit 3: Earth's Gravity Field (Weeks 9–12)

- Newton's law of gravitation: F = GMm/r²

- Gravitational potential: V = GM/r

- Normal gravity and the normal gravity formula

- Gravity anomalies: free-air, Bouguer, isostatic

- Gravity measurement: absolute vs. relative gravimeters

- **Applications:** geoid determination, mineral exploration, tectonic monitoring

### Unit 4: Positioning and Measurement (Weeks 13–16)

- Traditional methods: triangulation, trilateration, leveling

- **GNSS principles:** GPS, GLONASS, Galileo, BeiDou

- Signal propagation and error sources

- Time systems: UTC, TAI, GPS time, Earth rotation

- Introduction to reference frames: ITRF, WGS84, local datums

- Future of geodesy: SLR, VLBI, DORIS, altimetry

---

## 🔬 Key Formulas

```
Ellipsoid: x²/a² + y²/a² + z²/b² = 1
Normal gravity: γ = γ₀(1 + β sin²φ - β₁ sin²2φ)
Free-air anomaly: Δg_FA = g_obs - γ₀ + 0.3086·h
Bouguer anomaly: Δg_B = Δg_FA - 2πGρh
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Define geodesy and distinguish its major branches
2. Describe Earth's shape using ellipsoidal models and reference systems
3. Convert between geodetic, Cartesian, and local coordinate systems
4. Explain the concept of the geoid and its relationship to gravity
5. Understand the principles of GNSS positioning
6. Appreciate the role of physics in all geodetic measurement

---

## 📚 References

1. Torge, W. & Müller, J. (2012). *Geodesy*, 4th ed. de Gruyter.
2. Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS — Global Navigation Satellite Systems*. Springer.
3. Vanicek, P. & Krakiwsky, E. (1986). *Geodesy: The Concepts*, 2nd ed. Elsevier.
4. IAG Services: https://www.iag-aig.org/
5. NOAA NGS: https://www.ngs.noaa.gov/
