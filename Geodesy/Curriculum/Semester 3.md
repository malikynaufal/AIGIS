---
tags: [geodesy, curriculum, semester-3]
aliases: [Semester 3 Curriculum]
created: 2026-07-13
updated: 2026-07-27
---

# 📋 Semester 3 — Geodesy Curriculum

> *"Core geodetic theory: coordinate systems, reference frames, and geodetic astronomy."*

---

## 1. Courses

| Code | Course | SKS | Focus |
|------|--------|-----|-------|
| TKD212301 | Geometri Diferensial | 3 | Differential geometry |
| TKD212302 | Oseanografi Fisis | 2 | Physical oceanography |
| TKD212303 | Sistem Referensi Geodesi | 3 | Geodetic reference systems |
| TKD212304 | Fotogrametri Dasar | 3 | Basic photogrammetry |
| TKD212305 | Praktikum Fotogrametri Dasar | 1 | Photogrammetry lab |
| TKD212306 | Sistem Informasi Geografis | 3 | GIS fundamentals |
| TKD212307 | Praktikum SIG | 1 | GIS lab |
| TKD212308 | Survei Terestris III | 3 | Advanced terrestrial surveying |
| TKD212309 | Praktikum Survei Terestris III | 1 | Surveying lab |
| TKD212310 | Analisis Statistika | 2 | Statistical analysis |

**Total: 21 SKS**

---

## 2. Key Concepts

### Geometri Diferensial
- Curves: curvature, torsion, Frenet-Serret formulas
- Surfaces: first/second fundamental forms, Gaussian curvature
- Geodesic curves on surfaces
- **Application:** Reference ellipsoid geometry

### Sistem Referensi Geodesi
- [[ITRF]], [[ITRS]] — International Terrestrial Reference Frame
- [[WGS84]] — GPS reference system
- [[GRS80]] — Reference ellipsoid
- [[Precession and Nutation]] — Earth orientation
- [[IERS]] conventions

### Fotogrametri
- Camera geometry, collinearity equations
- Stereo vision: y-parallax, x-parallax
- Aerotriangulation, bundle adjustment

### SIG
- Raster vs vector models
- Coordinate reference systems
- Spatial analysis: buffering, overlay, interpolation

---

## 3. Key Formulas

### Reference Ellipsoid — Meridian Curvature

$$ M = \frac{a(1-e^2)}{(1-e^2\sin^2\phi)^{3/2}}$$### Prime Vertical Curvature $$ N = \frac{a}{\sqrt{1-e^2\sin^2\phi}} $$### Geodetic to Cartesian (ECEF)$$ \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} (N+h)\cos\phi\cos\lambda \\ (N+h)\cos\phi\sin\lambda \\ (N(1-e^2)+h)\sin\phi \end{pmatrix}

$$

---

## 4. Learning Outcomes

By the end of Semester 3, students can:

1. Transform between coordinate reference systems
2. Compute coordinates on a reference ellipsoid
3. Perform basic photogrammetric measurements
4. Use GIS software for spatial analysis
5. Apply statistical methods to survey data
6. Understand Earth orientation parameters

---

## 5. Cross-links

- Previous: [[Semester_2/TKD211201 - Sistem Koordinat|Semester 2 — Coordinate Systems]]
- Next: [[Semester_4 Curriculum]]
- Related: [[ITRF]], [[WGS84]], [[Geodetic Coordinates]], [[Map Projection]], [[Least Squares Adjustment]]

*Page last updated: 2026-07-27 | AIGIS Content™*