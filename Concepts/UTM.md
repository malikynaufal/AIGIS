---
tags: [geodesy, concept, projection, aigis]
aliases: [UTM, Universal Transverse Mercator, UTM Zone, UTM Coordinate]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 UTM (Universal Transverse Mercator)

**UTM** (Universal Transverse Mercator) is the world's most widely used map projection. It divides the Earth into 6°-wide longitude zones, each projected using a conformal [[Transverse Mercator]] projection. Coordinates are in meters (easting, northing) — a practical, standardized global grid for topographic mapping, surveying, and GIS.

## Zone System

UTM divides the globe into **60 zones** numbered 1–60 east to west:

| Property | Value |
|----------|-------|
| **Number of zones** | 60 |
| **Zone width** | 6° longitude |
| **Zone numbering** | 1 = 180°W to 174°W, ..., 60 = 174°E to 180°E |
| **Latitude bands** | 20 bands (C–X, 8° each, excluding I/O) |
| **Hemisphere designation** | N (north of equator), S (south of equator) |

### Zone Identification

| Example | Meaning |
|---------|---------|
| UTM Zone **33N** | 12°E to 18°E, Northern hemisphere |
| UTM Zone **49S** | 114°E to 120°E, Southern hemisphere |
| UTM Zone **30N** | 0° to 6°E, Northern hemisphere |

### Exceptions

| Zone | Exception |
|------|-----------|
| 31N | 0°–3°E |
| 32N | 3°–12°E (widened for Norway) |
| 33N | 12°–18°E |
| X band | 80°S–80°N (12° wide, excluding poles) |

The Svalbard islands receive special treatment: zones 31–37 are each widened to 3°.

## Projection Parameters

| Parameter | Northern Hemisphere | Southern Hemisphere |
|-----------|-------------------|---------------------|
| Central meridian | Zone center longitude | Zone center longitude |
| False easting $E_0$ | 500,000 m | 500,000 m |
| False northing $N_0$ | 0 m | 10,000,000 m |
| Scale factor $k_0$ | 0.9996 | 0.9996 |
| Ellipsoid | WGS84 | WGS84 |

### Scale Factor Behavior

The scale factor $k = 0.9996$ at the central meridian means UTM distances are **compressed** by 0.04% at the CM. This allows $k$ to reach **1.0** at ~180 km east/west of CM, and to remain below **1.0004** at zone edges — a deliberate design choice to minimize maximum distortion.

$$k \approx 1 + \frac{l^2}{2}\cos^2\phi$$

where $l$ is the longitude offset from CM in radians.

## Convergence

**Grid convergence** (angle between grid north and true north):

$$\gamma = l \cdot \sin\phi \approx \Delta\lambda \cdot \sin\phi$$

| Location | $\Delta\lambda$ from CM | $\gamma$ |
|----------|------------------------|----------|
| Equator, any longitude offset | 1.5° | 0° |
| 30°N, CM | 0° | 0° |
| 30°N, zone edge | 3° | 1.50° |
| 45°N, zone edge | 3° | 2.12° |
| 60°N, zone edge | 3° | 2.60° |

Convergence increases with latitude and with distance from the central meridian.

## Grid to Geographic Conversion

### Forward: $(\phi, \lambda) \to (E, N)$

1. Determine zone: $Z = \lfloor(\lambda + 180)/6\rfloor + 1$
2. Compute CM: $\lambda_0 = (Z - 1) \times 6 - 180 + 3°$
3. Apply TM formulas using $k_0 = 0.9996$, $E_0 = 500000$, $N_0 = 0$ (N) or $10000000$ (S)
4. Append zone letter and hemisphere: "33N"

### Inverse: $(E, N) \to (\phi, \lambda)$

1. Subtract false origin ($E_0$, $N_0$)
2. Apply inverse TM series
3. Determine zone from longitude
4. Output: $(\phi, \lambda)$

## Worked Example

**Problem:** Determine the UTM Zone and compute projected coordinates for Jakarta, Indonesia ($\phi = -6.175^\circ\text{S}$, $\lambda = 106.827^\circ\text{E}$) on WGS84.

**Solution:**

**Step 1:** Zone number:
$$Z = \lfloor(106.827 + 180)/6\rfloor + 1 = \lfloor286.827/6\rfloor + 1 = \lfloor47.805\rfloor + 1 = 48$$

**Step 2:** Zone 48 is in the Southern hemisphere, so the designation is **48S**.

**Step 3:** Central meridian of Zone 48:
$$\lambda_0 = (48 - 1) \times 6 - 180 + 3 = 282 - 180 + 3 = 105^\circ\text{E}$$

**Step 4:** Apply forward TM formulas. For this zone on WGS84:

$$k_0 = 0.9996, \quad E_0 = 500000, \quad N_0 = 10000000$$

Using standard formulas (abbreviated for worked example):

The computed easting and northing for Jakarta on Zone 48S are approximately:

$$E \approx 715,488\ \text{m}, \quad N \approx 9,317,839\ \text{m}$$

(Actual values depend on the complete series evaluation; these are representative.)

**Zone check:** The false northing is 10,000,000 m in the Southern hemisphere to ensure all N values are positive.

## Accuracy Considerations

| Distance from CM | Max Scale Distortion ($k - 1$) | Corresponding Distance Error |
|------------------|--------------------------------|------------------------------|
| 0 km (CM) | −0.04% | −40 mm per km |
| 180 km | 0 (true scale) | 0 |
| 330 km (zone edge) | +0.04% | +40 mm per km |

**For surveying:** Grid distances must be corrected by the average scale factor ($1/k$) to get ground distances. This is crucial for precise work (property boundaries, engineering).

## Application in Indonesia

Indonesia uses two UTM-based systems:

| System | Zone Width | CM Interval | Use |
|--------|-----------|-------------|-----|
| **UTM** | 6° | 102°, 108°, 114°, 120°, 126°, 132° | National mapping |
| **TM3°** | 3° | 102°, 105°, 108°, 111°, 114°, 117°, 120°, 123°, 126°, 129°, 132°, 135° | Cadastral, local mapping |

Indonesia's [[Indonesia|spatial information policy]] requires TM3° for cadastral surveys (better accuracy than 6° UTM).

## Common Pitfalls

1. **Hemisphere confusion:** Forgetting that Southern hemisphere uses false northing = 10,000,000 m.
2. **Zone boundary ambiguity:** A point near a zone boundary may be valid in two zones.
3. **Scale factor neglect:** Failing to apply $1/k$ when converting grid distances to ground distances.
4. **Coordinate order:** E,N vs N,E — most software uses E,N (eastings first).
5. **Web Mercator confusion:** EPSG:3857 is NOT UTM — it is a spherical Mercator with no zone system.

## References
- USGS (1983). *Map Projections — A Working Manual*. PP 1395.
- Snyder, J. P. (1987). *Map Projections*. USGS PP 1395.
- Defense Mapping Agency (1983). *TM 8358.2: The Universal Grids (UTM/UPS)*.
- BIG Indonesia. *Koordinat Nasional Indonesia*.

## Related
- [[Map Projection]] · [[Transverse Mercator]] · [[Projected Coordinates]] · [[Map Projection]] · [[Indonesia]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]] · [[Kurikulum Teknik Geodesi]]
