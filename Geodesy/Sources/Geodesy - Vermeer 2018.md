---
title: Geodesy — Vermeer (2018)
author: Martin Vermeer
type: source
subject: Geodesy
pages: 534
tags: [source, geodesy, textbook, classical-geodesy, modern-geodesy, GNSS, least-squares, geoid]
---

# Geodesy — Vermeer (2018)

> **Source PDF:** `Geodesy - Vermeer 2018.pdf` (534 pp., Aalto University)
> Classical + modern geodesy textbook. Lineage: Torge (2001), Vaníček & Krakiwsky (1986),
> Heiskanen & Moritz (1967), Hofmann-Wellenhof et al. (2001).
> AIGIS mirrors this into `H:\My Drive\AIGIS - Geodesy\Sources\` daily; add that Drive
> folder as a source in the Geodesy NotebookLM notebook.

This book is the **primary long-term reference** for AIGIS tutoring Geodesy — not limited
to Semester 3 or the geoid. It spans history → instruments → GNSS → adjustment calculus →
gravity/geoid → space geodesy → geodynamics.

## How AIGIS uses this

- Treats each chapter as a tutoring unit; cross-links to atomic concept notes below.

- Pulls definitions/examples on request; can generate exercises/summaries per chapter.

- Connected to the [[Geodesy MOC]] and to Mathematics/Physics where a topic depends on them.

---

## Part I — Classical Geodesy (ch. 1–9)

### 1. The history and societal status of geodesy — p.1

- [[Geoid]] · [[Reference Ellipsoid]] · [[Horizontal Datum]] · [[Orthometric Height]]

- 1.1 Figure of the Earth, early conceptions

- 1.3 The mathematical figure of the Earth or geoid → [[Geoid]] · [[Geoid Undulation]]

- 1.6 Reference surfaces and reference systems → [[Datum]] · [[Horizontal Datum]]

### 2. Geodetic measurements and co-ordinates — p.21

- [[Geodetic Coordinates]] · [[Projected Coordinates]] · [[Geocentric Cartesian ECEF]]

- 2.3–2.4 Stochastic quantities, statistical distributions (→ Mathematics)

- 2.6 About co-ordinates · 2.8 3D location co-ordinates → [[Geocentric Cartesian ECEF]]

### 3. Map projections, datums and transformations — p.47

- [[Map Projection]] · [[Datum Transformation]] · [[Transverse Mercator]] · [[Mercator]] · [[UTM]]

- 3.5 Geodetic forward/inverse problem → [[Vincenty Formula]]

- 3.6 Similarity co-ordinate transformation · 3.7 Datums & datum transformations → [[Datum Transformation]]

- 3.8 Map projections and height systems → [[Orthometric Height]] · [[Ellipsoidal Height]]

### 4. Height measurement and the levelling instrument — p.79

- [[Orthometric Height]] · [[Geoid]] · [[Geoid Undulation]]

- 4.1 Height, geopotential and the geoid → [[Gravity Field]] · [[Physical Geodesy]]

### 5. The theodolite and angle measurement — p.107

- 5.2 Axes of a theodolite · 5.8 Horizontal angle measurement

### 6. Distance measurement — p.155

- 6.2 Electromagnetic radiation · 6.4 Electronic distance measurement (EDM)

### 7. Base network and detail survey measurement — p.177

- 7.5 Traverse measurement and computation · [[Local ENU NEU]]

### 8. Construction surveying — p.209

- 8.3 Straight lines, circular arcs, transfer curves

### 9. Digital terrain models and volume calculation — p.223

- 9.3 Surface areas · 9.4 Volume calculations

## Part II — Modern Geodesy (ch. 10–17)

### 10. Three-dimensional co-ordinate reference systems — p.237

- [[Geocentric Cartesian ECEF]] · [[ITRF]] · [[ETRS89]] · [[Helmert Transformation]]

- 10.3–10.5 3D transformations, ellipsoid-to-ellipsoid → [[Helmert Transformation]] · [[Datum Transformation]]

- 10.8 ED50 ↔ EUREF89 · 10.9 ITRF ↔ ETRF → [[ITRF]] · [[ETRS89]]

### 11. Global Positioning System (GPS) — p.255

- [[GPS]] · [[GNSS]] · [[IGS]] · [[PPP]] · [[RTK]]

- 11.6 Observables of GPS · 11.7–11.8 Measurement geometry / DOP · 11.9 Orbits → [[GPS]]

- 11.10 International GNSS Service → [[IGS]]

### 12. Processing GPS observations — p.299

- 12.2 Relative (static) GPS · 12.3 Fixing ambiguities · 12.4 Real-time positioning → [[RTK]]

- 12.5 SBAS · 12.6 Real-time support services

### 13. Adjustment calculus in geodesy — p.319

- [[Least Squares Adjustment]] · [[Helmert Transformation]] · [[Geocentric Cartesian ECEF]]

- 13.4 Theory of least-squares → [[Least Squares Adjustment]]

- 13.10 Helmert transformation in the plane → [[Helmert Transformation]]

### 14. Statistical methods in geodesy — p.351

- [[Least Squares Adjustment]]

- 14.3–14.5 Testing, overall validation, locating gross errors

- 14.8 Reliability · 14.9 Redundancy · 14.10 Deformation analysis

### 15. Gravity in geodesy — p.377

- [[Gravity Field]] · [[Physical Geodesy]] · [[Geoid]] · [[Geoid Undulation]] · [[Orthometric Height]]

- 15.4 The gravimetric geoid → [[Geoid Undulation]]

- 15.6 Bouguer anomalies · 15.7 Astronomical position determination

### 16. Space geodesy — p.405

- [[IERS]] · [[ITRF]] · [[GPS]]

- 16.1 Earth rotation, sidereal time · 16.4–16.5 Variations, precession & nutation → [[IERS]]

- 16.7 Satellite orbital motion · 16.9 Sun-synchronous orbit

### 17. Geodesy and geophysics — p.425

- 17.1 Geodynamics · 17.2 Gravity field from orbit · 17.3 Atmospheric research & GNSS → [[GNSS]]

- 17.5 Land-ice / climate · 17.6 Geodetic oceanography

## Appendices

- **A.** Properties of matrices (→ Mathematics)

- **B.** Short introduction to magnetohydrodynamics (Maxwell's equations)

- **C.** Kepler orbital elements for satellites → [[GPS]]

## Quick tutor entry points

- New to the field? Start at ch.1 → [[Geoid]] and [[Reference Ellipsoid]].

- GNSS deep-dive? ch.11–12 → [[GPS]] · [[RTK]] · [[PPP]] · [[IGS]].

- Adjustment/stats? ch.13–14 → [[Least Squares Adjustment]].

- Gravity/geoid? ch.15 → [[Physical Geodesy]] · [[Geoid Undulation]].

- Frames? ch.10 → [[ITRF]] · [[ETRS89]] · [[Helmert Transformation]].
