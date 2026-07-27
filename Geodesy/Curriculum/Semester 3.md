---
tags: [aigis, curriculum, geodesy, semester-3, ugm]
created: 2026-07-27
updated: 2026-07-27
---

# Semester 3 — Core Geodesy

## Overview

Semester 3 is the pivotal year where students master the core geodesic disciplines: differential geometry of the curved Earth surface, reference systems (including ITRF/WGS84), physical geodesy, photogrammetry foundations, GIS systems, and advanced survey techniques.

## Courses (10 mata kuliah, total ~26 SKS)

| Code | Course | SKS | Type |
|------|--------|-----|------|
| TKD212301 | Geometri Diferensial | 3 | Core |
| TKD212302 | Oseanografi Fisis | 3 | Sci |
| TKD212303 | Sistem Referensi Geodesi | 3 | Core |
| TKD212304 | Fotogrametri Dasar | 3 | Core |
| TKD212305 | Praktikum Fotogrametri Dasar | 1 | Lab |
| TKD212306 | Sistem Informasi Geografis | 3 | IT |
| TKD212307 | Praktikum Sistem Informasi Geografis | 1 | Lab |
| TKD212308 | Survei Terestris III | 3 | Core |
| TKD212309 | Praktikum Survei Terestris III | 3 | Lab |
| TKD212310 | Analisis Statistika | 3 | Math |

## Key Topics

### TKD212301 — Geometri Diferensial (Differential Geometry)
- Curves on an ellipsoid: curvature and torsion
- Geodesic lines (geodesics): shortest paths
- Euler equation for geodesic:
  
  $$\frac{d^2 u}{ds^2} + \Gamma_{ij}^{k} \frac{du^i}{ds} \frac{du^j}{ds} = 0$$
  
- Christoffel symbols on ellipsoid
- Vincenty's direct and inverse problems (see [[Vincenty Formula]])

### TKD212303 — Sistem Referensi Geodesi (Reference Systems)
- ITRF: definition, realizations, transformation between epochs
- WGS84 evolution (G1150 through G2139)
- [[GRS80]] and other reference ellipsoids
- ETRS89: European system
- Datum transformations (Helmert, Molodensky)
- [[Datum Transformation]] in detail
- [[Helmert Transformation]] formulas

### TKD212304 — Fotogrametri Dasar
- Collinearity condition (see [[Photogrammetry]])
- Exterior orientation elements
- Aerial triangulation
- Digital photogrammetry basics

### TKD212306 — Sistem Informasi Geografis (GIS)
- Vector vs raster data models
- Data structures, topology
- Spatial queries and analysis
- [[SIG]] for Indonesian land management

## Key Formulas (Preview)

- Geodesic arc length: $s = a(1-e^2)\int_0^\varphi \frac{d\varphi}{(1-e^2\sin^2\varphi)^{3/2}}$
- Helmert 7-parameter: $\mathbf{X}_{B} = T + (1+c)R\mathbf{X}_{A}$
- Vincenty inverse: iterative solution for $(\lambda, \alpha)$

## Study Pack
➡️ Study pack for Semester 3 consolidating: [[Geometri Diferensial]], [[Reference Frame]], [[Helmert Transformation]], [[Vincenty Formula]]

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
