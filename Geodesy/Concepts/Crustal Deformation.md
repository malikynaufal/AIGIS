---
tags: [geodesy, concept, geodynamics, aigis]
aliases: [Crustal Deformation, Deformasi Kerak Bumi]
created: 2026-07-27
---

# 🌍 Crustal Deformation

**Crustal deformation** refers to the displacement and distortion of the Earth's lithosphere due to tectonic forces, volcanic processes, glacial loading/unloading, and anthropogenic activities. Measuring crustal deformation is a core application of geodesy — using GNSS, InSAR, and geodetic levelling to monitor plate motion, seismic hazards, and land subsidence.

> **Indonesian term:** *Deformasi Kerak Bumi*

---

## 1. Driving Mechanisms

| Mechanism | Timescale | Typical rate | Example |
|-----------|-----------|-------------|---------|
| **Plate tectonics** | 10⁶ – 10⁷ yr | 1–10 cm/yr | Pacific–Eurasian boundary |
| **Interseismic strain** | 10² – 10³ yr | mm/yr | Locked subduction zone |
| **Coseismic** | Minutes | 0.1–10 m | Great earthquakes |
| **Postseismic** | 10 – 10³ yr | mm/yr to cm/yr | Afterslip, viscoelastic relaxation |
| **Volcanic inflation/deflation** | 10⁻² – 10² yr | mm/yr to cm/yr | Mount Merapi |
| **Glacial isostatic adjustment** | 10³ – 10⁴ yr | mm/yr | Scandinavia, Canada |
| **Land subsidence** | 10⁻¹ – 10¹ yr | mm/yr to cm/yr | Jakarta, Semarang |
| **Anthropogenic** | 10⁰ – 10¹ yr | mm/yr to cm/yr | Groundwater extraction |

---

## 2. Tectonic Plate Motion

### 2.1. Plate motion in ITRF

Each plate moves as a rigid body on the sphere. The Euler pole (rotation vector) describes the motion:

$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r} $ $

where $\mathbf{v} $ is the velocity at a station on the surface,$\boldsymbol{\omega} $ is the angular velocity vector, and $\mathbf{r} $ is the position vector.

| Plate | Angular velocity $\omega $ (°/Myr) | Euler pole (°N, °E) |
|-------|-----------------------------------|----------------------|
| Eurasian | 0.96 | 50.6, −91.4 |
| Indo‑Australian | 0.68 | 33.9, 39.4 |
| Philippine Sea | 0.88 | −34.4, −34.2 |
| Pacific | 0.94 | −63.0, −77.4 |

**Indonesia** sits at the triple junction of Eurasian, Indo‑Australian, and Philippine Sea plates — making it one of the most tectonically active regions on Earth.

### 2.2. Interseismic deformation

At a locked subduction zone (e.g., Sunda Trench), the overriding plate is compressed and pushed upward

$ $ v_{\text{int}} = A \cdot e^{-x/\xi} + B $$

where $ x $ is distance from the trench, and $\xi $ is the locking depth parameter.

---

## 3. Coseismic and Postseismic Deformation

### 3.1. Coseismic displacement (Okada elastic half‑space model)

The displacement at a point $ (x,y) $ on the surface due to a rectangular dislocation (fault) is given by the **Okada (1985)** equations. Key parameters:

| Parameter | Symbol | Meaning |
|-----------|--------|---------|
| Length | $ L $ | Along‑strike extent of fault |
| Width | $ W $ | Down‑dip extent |
| Strike | $\phi $ | Azimuth of fault trace |
| Dip | $\delta $ | Inclination of fault plane |
| Rake | $\lambda $ | Direction of slip on fault |
| Slip | $ D $ | Amount of displacement |
| Depth | $ d$ | Depth to top of fault |

The 3D displacement field involves analytical solutions in terms of trigonometric and logarithmic functions (Okada 1985, 1992). The vertical displacement field is often the largest for shallow thrust events.

### 3.2. Postseismic deformation

Three main mechanisms:
1. **Afterslip** — continued creeping on the fault plane (dominant in first months).
2. **Viscoelastic relaxation** — mantle flow in response to stress change (dominant years to decades).
3. **Poroelastic rebound** — fluid redistribution in crust (short‑lived).

---

## 4. Geodetic Measurement Techniques

| Technique | Precision | Spatial coverage | Temporal sampling | Best for |
|-----------|-----------|------------------|-------------------|----------|
| **GNSS (continuous)** | 1–2 mm horiz, 3–5 mm vert | Point | Continuous | Plate motion, interseismic |
| **GNSS (campaign)** | 2–5 mm | Point | Seasonal/annual | Regional networks |
| **InSAR (SAR interferometry)** | 1–5 mm | Area (100s km) | Days–weeks | Subsidence, fault mapping |
| **Leveling** | 0.3–1 mm/km | Linear route | Episodic | Vertical deformation |
| **VLBI** | 1 mm | Global | Continuous | Earth rotation, frame |
| **Satellite laser ranging** | 1–2 mm | Global | Continuous | Geocentre, frame |

---

## 5. Worked Example – Measuring Plate Velocity with GNSS

**Given:** Continuous GNSS station CUTO (Jakarta) observed for 10 years (2014–2024).

| Component | Velocity (mm/yr) | Uncertainty (mm/yr) |
|-----------|------------------|----------------------|
| East | +21.3 | 0.4 |
| North | +38.7 | 0.3 |
| Up | −12.1 | 1.5 |

Interpretation:

- **Horizontal velocity** (+21.3, +38.7) mm/yr is consistent with the **Eurasian plate** motion (expected ~25 mm/yr east, ~40 mm/yr north relative to ITRF).

- **Vertical velocity** (−12.1 mm/yr) is dominated by **local land subsidence** in Jakarta due to groundwater extraction — one of the fastest subsiding cities in the world.

---

## 6. Indonesia Case Studies

| Area | Phenomenon | Rate | Reference |
|------|-----------|------|-----------|
| **Sunda Trench** | Interseismic coupling | 20–40 mm/yr convergence | Simons et al., 2007 |
| **Yogyakarta (2006)** | Coseismic slip (M6.4) | Up to 0.8 m slip | Savage et al., 2007 |
| **Mentawai Islands** | Interseismic strain accumulation | 20–30 mm/yr | Chlieh et al., 2008 |
| **Mount Merapi** | Volcanic inflation/deflation | 2–5 cm/yr | Surono et al., 2012 |
| **Jakarta** | Land subsidence | 5–25 cm/yr | Abidin et al., 2001–present |
| **Semarang** | Land subsidence | 1–5 cm/yr | Marfai et al., 2015 |

---

## 7. Diagram – Subduction Zone Deformation Cycle

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" width="700" height="300">
 <rect width="700" height="300" fill="#1a1a2e" rx="8"/>
 <text x="350" y="25" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle">Subduction Zone Deformation Cycle</text>
 <!-- Ocean plate -->
 <path d="M 50 200 Q 200 210, 300 220 L 300 280 L 50 280 Z" fill="#118ab2" opacity="0.7"/>
 <text x="150" y="260" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">Oceanic Plate (Indo‑Aus)</text>
 <!-- Overriding plate -->
 <path d="M 300 160 Q 450 150, 650 145 L 650 280 L 300 280 Z" fill="#06d6a0" opacity="0.6"/>
 <text x="480" y="250" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">Continental Plate (Eurasian)</text>
 <!-- Trench -->
 <path d="M 300 140 L 300 280" stroke="#f9c74f" stroke-width="2" stroke-dasharray="5,3"/>
 <text x="280" y="145" fill="#f9c74f" font-size="10" font-family="sans-serif" text-anchor="end">Trench</text>
 <!-- Arrows showing plate motion -->
 <g stroke="#4cc9f0" stroke-width="2" marker-end="url(#a4)">
 <line x1="100" y1="220" x2="250" y2="230"/>
 </g>
 <text x="170" y="215" fill="#4cc9f0" font-size="9" font-family="sans-serif">Subduction</text>
 <!-- Locking zone -->
 <path d="M 320 200 Q 360 190, 400 195" stroke="#f72585" stroke-width="3" fill="none"/>
 <text x="360" y="185" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">Locked zone</text>
 <!-- GPS station -->
 <circle cx="450" cy="155" r="6" fill="#ff9f1c"/>
 <text x="450" y="148" fill="#ff9f1c" font-size="9" font-family="sans-serif" text-anchor="middle">GPS</text>
 <!-- Deformed GPS vectors -->
 <g stroke="#ff9f1c" stroke-width="2" marker-end="url(#a5)">
 <line x1="450" y1="150" x2="430" y2="138"/>
 </g>
 <text x="435" y="133" fill="#ff9f1c" font-size="8" font-family="sans-serif">Interseismic</text>
 <text x="435" y="125" fill="#ff9f1c" font-size="8" font-family="sans-serif">velocity</text>
 <defs>
 <marker id="a4" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#4cc9f0"/></marker>
 <marker id="a5" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#ff9f1c"/></marker>
 </defs>
 <!-- Legend -->
 <text x="50" y="45" fill="#ccc" font-size="10" font-family="sans-serif">Coseismic: seconds to minutes (earthquake)</text>
 <text x="50" y="60" fill="#ccc" font-size="10" font-family="sans-serif">Interseismic: decades to centuries (strain build‑up)</text>
 <text x="50" y="75" fill="#ccc" font-size="10" font-family="sans-serif">Postseismic: years to decades (relaxation after quake)</text>
</svg>

---

## 8. Related

- [[Geodetic Astronomy]] – traditional deformation measurements.

- [[ITRF]] – provides the global reference frame for velocity fields.

- [[GNSS]] – the primary technique for measuring deformation.

- [[Tidal Theory]] – tidal loading is a deformation signal that must be removed.

- [[Geoid Undulation]] – the geoid changes with mass redistribution.

---

## 9. References

- Okada, Y., *Surface deformation due to shear and tensile faults in a half‑space*, Bull. Seismol. Soc. Am. 75(4), 1135‑1154, 1985.

- Simons, M. et al., *The 2004 Sumatra‑Andaman earthquake: Imaging the fault slip*, Nature 443, 288‑293, 2006.

- Chlieh, M. et al., *Coseismic slip and afterslip of the great Mw 9.15 Sumatra‑Andaman earthquake*, JGR 114, B01401, 2009.

- Abidin, H.Z. et al., *Land subsidence of Jakarta*, J. Geod. Soc. Japan, 2001–2020. (Multiple papers)

- Savage, J.C., *Postseismic deformation in Java after the 2006 Yogyakarta earthquake*, JGR 2007.

- SEG (Society of Economic Geophysics), *The OKADA Model (1985) – MATLAB implementation*, https://www.mathworks.com/matlabcentral/

- IERS Conventions (2010), Chapter 7. https://www.iers.org/

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]