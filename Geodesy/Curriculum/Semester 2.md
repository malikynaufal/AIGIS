---
tags: [aigis, curriculum, geodesy, semester-2, ugm]
created: 2026-07-27
updated: 2026-07-27
---

# Semester 2 — Computation & Analysis

## Overview

Semester 2 focuses on computational methods for geodesy: coordinate systems, least squares adjustment (the core mathematical tool), and database management. Students build the analytical skills needed for Semester 3–4 advanced topics.

## Courses (10 mata kuliah, total ~26 SKS)

| Code | Course | SKS | Type |
|------|--------|-----|------|
| TKD211201 | Sistem Koordinat | 3 | Core |
| TKD211202 | Geometri Analitik | 3 | Math |
| TKD211203 | Hitung Perataan | 3 | Core |
| TKD211204 | Dasar-dasar Geofisika dan Astronomi | 3 | Sci |
| TKD211205 | Sistem Basisdata | 3 | IT |
| TKD211206 | Praktikum Sistem Basisdata | 1 | Lab |
| TKD211207 | Pemrograman Komputer | 3 | IT |
| TKD211208 | Praktikum Pemrograman Komputer | 1 | Lab |
| TKD211209 | Survei Terestris II | 3 | Core |
| TKD211210 | Praktikum Survei Terestris II | 3 | Lab |

## Key Topics

### TKD211201 — Sistem Koordinat
- Geographic, projected, and local coordinate systems
- Datum concept and transformation basics
- EPSG codes and coordinate reference systems (CRS)
- Introduction to geoid undulation

### TKD211203 — Hitung Perataan (Least Squares Adjustment)
The most important course in geodesy:
- Observation equations: $\mathbf{y} = f(\mathbf{x}) + \mathbf{v} $- Linearization: $\mathbf{v} = \mathbf{A}\hat{\mathbf{x}} + \mathbf{l} $- Normal equations: $\mathbf{A}^T\mathbf{P}\mathbf{A}\hat{\mathbf{x}} = \mathbf{A}^T\mathbf{P}\mathbf{l} $
- Covariance propagation
- Weight matrices and reliability

### TKD211204 — Geofisika & Astronomi
- Gravity potential and normal gravity
- Celestial coordinates and time systems
- Astronomical latitude/longitude determination
- [[Precession and Nutation]] concepts

## Key Formulas (Preview)

- Weighted least squares: $\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1}\mathbf{A}^T\mathbf{P}\mathbf{l} $- Covariance of adjusted parameters: $\mathbf{Q}_{\hat{x}\hat{x}} = (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1}$
- Coordinate transform: 7-parameter Helmert transform (see [[Helmert Transformation]])

## Study Advice
1. Master least squares — it underpins all geodesy
2. Implement Gauss-Jordan elimination in Python
3. Review [[Least Squares Adjustment]] concept note
4. Practice database design for spatial data

## Study Pack
➡️ [[_Study Packs/Satellite Positioning and Clock Corrections|Semester 2 Study Pack]] — consolidating [[Least Squares Adjustment]] and coordinate system concepts

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
