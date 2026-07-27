---
tags: [aigis, concept, geodesy, datum, transformation, wgs84, nad83, nad27, local-datums]
created: 2026-07-27
updated: 2026-07-27
---

# Datum Transformation

## For Geodesy & Coordinate Conversion

**Core Idea:** A datum is a reference framework for specifying positions on Earth's surface. Datum transformations convert coordinates between different reference frames. Understanding datum is essential because coordinates in WGS84 are NOT the same as coordinates in a local Indonesian datum — the difference can be hundreds of meters.

---

## Fundamental Concepts

### What is a Datum?

A geodetic datum specifies:
1. **The reference ellipsoid** (shape, size)
2. **The orientation and position** of that ellipsoid relative to Earth
3. **The origin point** (can be a single point, multiple points, or a best-fit over a region)

### Datum Types

| Type | Description | Examples |
|------|-------------|----------|
| **Global (geocentric)** | Origin at Earth's center of mass | WGS84, ITRF, GTRF |
| **Regional** | Best fit over a continent/region | NAD83, ETRS89, DGN95 |
| **Local** | Best fit over a small area | Local surveys, custom datums |

### WGS84 Detail

| Parameter | Value |
|-----------|-------|
| Ellipsoid | GRS80-based |
| Semi-major axis $a$| 6,378,137.0 m (exact) |
| Flattening$f$| 1/298.257223563 |
| Origin | Earth's center of mass (geocentric) |
| Z-axis | Conventional Terrestrial Pole (CTP) |
| X-axis | Intersection of CTP and Greenwich meridian |
| Y-axis | Completes right-handed system |

---

## Datum Transformation Methods

### 7-Parameter Helmert Transformation$$\begin{bmatrix} X_T \\ Y_T \\ Z_T \end{bmatrix} = \begin{bmatrix} 1 & -r_Z & r_Y \\ r_Z & 1 & -r_X \\ -r_Y & r_X & 1 + \delta\mu \end{bmatrix} \begin{bmatrix} X_s \\ Y_s \\ Z_s \end{bmatrix} + \begin{bmatrix} T_X \\ T_Y \\ T_Z \end{bmatrix}$$| Parameter | Meaning | Unit |
|-----------|----------|------|
|$T_X, T_Y, T_Z$| Translation | m |
|$r_X, r_Y, r_Z$| Rotation | arcseconds |
|$\delta\mu$| Scale change | ppm |

### Molodensky Transformation (Geodetic)

Works directly in geodetic coordinates$(\phi, \lambda, h)$without converting to ECEF. More practical for small-area transformations.

**Formulas** (simplified):$$\Delta\phi = \frac{1}{M}\left[-a_X\cos\phi\sin\lambda + a_Y\cos\phi\cos\lambda + a_Z\sin\phi\right]
$$

$$\Delta\lambda = \frac{1}{N\cos\phi}\left[-a_X\sin\lambda + a_Y\cos\lambda\right]$$

$$
\Delta h = -a_X\cos\phi\cos\lambda - a_Y\cos\phi\sin\lambda + a_Z\sin\phi + \text{scale terms}$$---

## Common Datums

### WGS84

- GPS reference frame

- Global, geocentric

- Updated regularly (WGS84 G1674, G1762, G2139)

- Tied to ITRF by convention

### NAD83 (North American Datum 1983)

- NAD83 is geocentric (GRS80 ellipsoid)

- Nearly identical to WGS84 (≤2 m difference)

- Used in North America

### NAD27 (North American Datum 1927)

- Based on the Clarke 1866 ellipsoid

- Origin at Meining, Kansas

- **Not geocentric** — WGS84 differences can be ~200 m

### Indonesia: DGN95 (Datum Geodetic Nasional 1995) — Indonesia's National Datum

- Based on ITRF94, tied to WGS84 with a specific epoch

- Origin: multiple points across Indonesia

- **Key transformation parameters (WGS84 → DGN95):**

| Parameter | Value |
|-----------|-------|
|$T_X, T_Y, T_Z$| ~0 m (nearly identical) |
|$r_X, r_Y, r_Z$| ~0–1 arcsec |
|$\delta\mu$| ~0 ppm |

In practice, for many applications, WGS84 ≈ DGN95 (difference < 0.1 m).

### ETRS89 (European Terrestrial Reference System 1989)

- European regional datum

- Fixed to European plate (no continental drift)

---

## Indonesia Local Datums and SIG

**SIG (Sistem Informasi Geografis)** — Indonesia's national geospatial infrastructure coordinates coordinate systems through the Indonesian Geospatial Information Agency (BIG/Badan Informasi Geospasial).

### BIG Datum Framework

| Datum | Reference | Use |
|-------|-----------|-----|
| WGS84 (G2139) | ITRF2014 epoch 2010 | GNSS survey |
| DGN95 | ITRF94, epoch 1994 | National mapping |
| ITRF (various epochs) | ITRF | Scientific precise work |

---

## Practical Considerations

### Transformation Quality

| Datum change | Typical accuracy |
|---|---|
| WGS84 (G1674) → WGS84 (G2139) | ≤ 5 cm |
| WGS84 → DGN95 | < 0.1 m (Indonesia) |
| WGS84 → NAD27 | ~200 m (continental US) |
| WGS84 → local datum (Jakarta) | ~0.5–3 m depending on datum |

### Best Practices

1. **Never transform blindly** — always check the source and target datums
2. **Use published transformation parameters** — not made-up values
3. **Document the transformation** — include transformation method, parameters, and accuracy in metadata
4. **Consider the magnitude** — if working at sub-meter level, datum matters a lot
5. **Use software (PROJ)** with EPSG codes for reliable transformations

### EPSG Codes for Indonesia

| EPSG | Description |
|------|-------------|
| 4326 | WGS84 geographic |
| 4613 | DGN95 geographic |
| 3001 | UTM Zone 48N (WGS84) — Sumatra |
| 3002 | UTM Zone 49N |
| 3101 | Proj. Sempurna |
| 4004 | MRT (Jakarta) — projected |
| 3821 | Mercator (Singapore) — used in Maluku area |
| 3824 | MTM zone (Meridian 123°E) |
| 23841 | UTM Zone 48N (DGN95-based) |

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
|$\mathbf{X}_T = \mathbf{R}\mathbf{X}_s + \mathbf{T}$| Helmert (7-param) | 3D coordinate conversion |
|$\Delta\phi = a_Z / M$| Molodensky | Geodetic coordinate shift |
| EPSG:xxxx | EPSG code | Unique datum/CRS identifier |

---

## Related Concepts

- [[WGS84]] — The global GNSS datum

- [[GRS80]] — Reference ellipsoid definition

- [[Geodetic Coordinates]] — Input/output of transformation

- [[Datum Transformation]] — Matrix form

- [[DGN95]] — Indonesia's national datum

- [[SIG]] — Indonesian geospatial infrastructure

- [[Helmert Transformation]] — The 7-parameter transform

---

## Study Problems

1. **Recall:** List three datums and compare their ellipsoid parameters.
2. **Application:** Given WGS84 coordinates$(\phi, \lambda, h)$ = (-6.2, 106.8, 25), transform to DGN95. What parameters from BIG or BIG's official document would you use?
3. **Derivation:** Starting from the 7-parameter Helmert transform, derive the transformation of geodetic coordinates to first order in rotations (small-angle approximation).
4. **Real-world:** You have coordinates in NAD27 and want to publish them in WGS84. What is the approximate error if you skip the datum transformation? What EPSG codes should you use?

---

## Common Mistakes

1. **Assuming WGS84 coordinates are the same everywhere** — WGS84 is a family of realizations, not one absolute frame.
2. **Confusing geoid (orthometric heights) with ellipsoid (ellipsoidal heights)** — datum defines both the reference shape AND the reference for heights.
3. **Using wrong transformation parameters** — always source from official national agency documents.
4. **Forgetting the epoch** — transformation parameters are epoch-specific.
5. **Mixing 2D and 3D transformations** — horizontal only vs. full 3D.

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*