---
tags: [aigis, geodesy, pilihan, remote-sensing, sar, active-sensor, radar]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Penginderaan Jauh Sensor Aktif (Active Remote Sensing — SAR)

**Kode:** TKD213613 | **SKS:** 3 (2-1) | **Semester:** 5–6

## Course Overview

Active Remote Sensing focuses on Synthetic Aperture Radar (SAR) and LiDAR systems. Covers SAR principles, polarimetry, InSAR (Interferometric SAR) for deformation mapping, and LiDAR for terrain and vegetation modeling.

## Key Topics

### 1. SAR Principles

$$

\text{Range resolution: } \Delta r = \frac{c}{2B}, \quad \text{Azimuth resolution: } \Delta a = \frac{\lambda R}{2L_{SAR}}

$ $

- **Backscatter:** $\sigma^0 = \frac{P_r (4\pi)^3 R^4}{P_t G^2 \lambda^2 A}$
- **Penetration by band:** X (< 2 cm), C (< 5 cm), L (< 25 cm), P (< 70 cm)

### 2. SAR Interferometry (InSAR)

**Phase difference:**

$ $

\Delta\phi = \frac{4\pi}{\lambda} \Delta r + \phi_{atm} + \phi_{noise}

$$

**DEM generation:** $ z = h - \frac{\lambda R \sin\theta}{4\pi B_\perp} \Delta\phi $

**Deformation mapping:**

$ $

d = \frac{\lambda}{4\pi} \cdot \Delta\phi_{def}

$$

| Technique | Accuracy | Application |
|-----------|----------|-------------|
| D-InSAR | 5–10 mm | Coseismic deformation |
| PS-InSAR | 1–3 mm | Subsidence monitoring |
| SBAS | 2–5 mm | Time series deformation |
| PolInSAR | 2–5 mm | Forest height estimation |

### 3. LiDAR Principles

$ $

\text{Range: } R = \frac{c \Delta t}{2}

$$

| LiDAR Type | Penetration | Application |
|------------|-------------|-------------|
| Discrete return | 1–5 returns | DTM, buildings |
| Full-waveform | Continuous | Forest structure |
| Bathymetric | Up to 50 m water | Seafloor mapping |

## Practical Work
- SAR image processing using SNAP (ESA)
- InSAR interferogram generation
- LiDAR point cloud classification

## Related Concepts

- [[Remote Sensing]] — Passive remote sensing
- [[Penginderaan Jauh Terapan]] — Applied remote sensing
- [[Crustal Deformation]] — InSAR monitoring
- [[Deformation Monitoring]] — Structural monitoring
- [[Survei Deformasi]] — Deformation surveys

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
