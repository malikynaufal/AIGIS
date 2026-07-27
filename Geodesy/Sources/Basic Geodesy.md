---
tags: [geodesy, source, aigis]
aliases: [Basic Geodesy primer]
source_file: geodesy_basics.pdf
created: 2026-07-12
---

# 📄 Basic Geodesy (source note)

Extracted from `geodesy_basics.pdf` (8.8 KB) by AIGIS. A short, practical English primer covering the essentials of geodesy.

## What it covers
1. **Shape of the Earth** — flattened sphere; reference ellipsoid defined by semimajor axis *a*, semiminor axis *b*, flattening *f*, eccentricities *e*, *e′*.
2. **Geoid** — the "true" equipotential surface ≈ mean sea level; [[Orthometric Height]] H measured above it.
3. **Datums** — horizontal reference frames: [[NAD27]], [[NAD83]], [[WGS84]], [[ETRS89]], GDA94/GDA2020.
4. **Coordinate systems** — [[Geodetic Coordinates]] (φ, λ, h), [[Geocentric Cartesian ECEF]] (X,Y,Z), [[Projected Coordinates]] (UTM, State Plane, Web Mercator), [[Local ENU NEU]].
5. **Heights & vertical datums** — h, N, H with **h = H + N**.
6. **Map projections** — conformal / equal-area / equidistant / azimuthal trade-offs.
7. **Common computations** — [[Vincenty Formula]], ECEF conversion, [[Datum Transformation]] (Helmert 7-param), UTM forward/inverse, geoid lookup, projection↔geographic.
8. **Tools** — [[PROJ]], [[GeographicLib]], GDAL/OGR, national agencies (NGS, etc.).

## Key constants (WGS84)

- a = 6378.137 km (equatorial radius)

- b = 6356.752 km (polar radius)

- f = 1/298.257

- e = 0.0818, e′ = 0.0821

## Further reading it cites

- Snyder, *Map Projections — A Working Manual* (USGS PP 1395)

- Torge & Müller, *Geodesy*, 5th ed.

- Vaníček & Krakiwsky, *Geodesy: The Concepts*

- NOAA NGS Manual NOS NGS 5

- IERS Conventions

➡️ Back to the hub: [[Geodesy MOC]]
