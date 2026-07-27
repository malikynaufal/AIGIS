---
tags: [aigis, curriculum, geodesy, semester-5, ugm]
created: 2026-07-27
updated: 2026-07-27
---

# Semester 5 — Advanced Geodesy and GNSS

## Overview

Semester 5 is the most technically demanding semester, covering physical geodesy (the gravity field and geoid), Digital Terrain Models (DTM), land administration, spatial programming, GNSS surveying, and hydrography. These are the key specialization areas for geodetic engineers.

## Required Courses (11 mata kuliah, total ~30 SKS)

| Code | Course | SKS | Type |
|------|--------|-----|------|
| TKD213501 | Geodesi Fisis | 3 | Core |
| TKD213502 | Model Terrain Digital | 3 | Core |
| TKD213503 | Administrasi Pertanahan | 3 | Core |
| TKD213504 | Pemrograman Spasial | 3 | Core |
| TKD213505 | Survei GNSS | 3 | Core |
| TKD213506 | Praktikum Survei GNSS | 2 | Lab |
| TKD213507 | Survei Hidrografi I | 3 | Core |
| TKD213508 | Praktikum Survei Hidrografi I | 1 | Lab |
| TKD213509 | Survei Kadastral | 3 | Core |
| TKD213510 | Praktikum Survei Kadastral | 2 | Lab |
| TKD213511 | Kemah Kerja | 1 | Field |

## Key Topics

### TKD213501 — Geodesi Fisis (Physical Geodesy)
- Potential theory fundamentals
- Gravity field: Poisson's equation

$$\nabla^2 W = -4\pi G\rho$$

- Normal gravity ([[GRS80]] Somigliana formula)
- [[Geoid]] determination methods:
  - Stokes' integral: $N = \frac{R}{4\pi\gamma}\int\Delta g \cdot S(\psi)\,d\sigma$
  - Remove-Compute-Restore
  - Molodensky's method
  - OSGEM (Orthometric Surface Geoid Estimation from Gravimetry)
- See [[Physical Geodesy]] for full derivation

### TKD213505 — Survei GNSS (GNSS Surveying)
- GPS principles and signal structure
- Carrier-phase observation equation
- [[Ambiguity Resolution]] — the key challenge
- Differential GNSS: [[RTK]] and [[PPP]]
- Network design and [[Jaring Kontrol Geodesi]]
- See [[GNSS Signal Processing]] study pack

### TKD213506 — Hidrografi I (Hydrographic Surveying)
- Sound physics in water
- SBES and MBES operation
- [[Hydrographic Surveying]] fundamentals
- Tidal correction algorithms
- Tidal datum determination

### TKD213509 — Survei Kadastral (Cadastral Survey)
- Legal boundary definition (UU No. 5/1960)
- [[Cadastral Surveying]] procedures
- Indonesia land registration system
- GNSS cadastral techniques
- Area computation (Shoelace formula)

## Semester 5 Study Pack
➡️ [[_Study Packs/Satellite Positioning and Clock Corrections|Semester 5 Study Pack]] — consolidating [[GNSS]], geophysical concepts, land administration

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
