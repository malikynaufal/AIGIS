---
tags: [geodesy, concept, coordinate-system, aigis]
aliases: [Projected Coordinates, Koordinat Proyeksi, Easting, Northing]
created: 2026-07-12
updated: 2026-07-27
---

# 🗺️ Projected Coordinates

**Projected coordinates** (e.g., [[UTM]], State Plane, Web Mercator) are a 2D representation in meters on a flat plane — the result of a [[Map Projection]] applied to geodetic coordinates $(\phi, \lambda)$. They enable flat-Earth calculations (distances, areas, angles) over regional extents where ellipsoid curvature can be treated as distortion.

## Why We Need Them

- **Maps, CAD, and surveying** all work in flat coordinates (x, y); the Earth is curved.
- **Area and distance** computations on a projection plane can be accurate to millimeters over small regions.
- **Always** declare the input/output CRS (via [[PROJ]] or EPSG codes) to ensure reproducibility.

## Common Projection Types

| Projection | Character | Use Cases | Examples |
|------------|-----------|-----------|----------|
| **UTM** ([[Universal Transverse Mercator]]) | Conformal | Topographic mapping, surveying | Global 6° zones |
| **Transverse Mercator (TM)** | Conformal | National/cadastral grids | Indonesia TM3°, State Plane |
| **Lambert Conformal Conic (LCC)** | Conformal | Middle-latitude mapping | France, US State Plane |
| **Lambert Azimuthal Equal Area** | Equal-area | Statistical/thematic mapping | National atlas pages |
| **Albers Equal-Area Conic** | Equal-area | Large-area thematic maps | USGS thematic, EU maps |
| **Mercator** | Conformal | Navigation, web mapping | EPSG:3857 (Web Mercator) |
| **Stereographic** | Conformal | Polar maps | Antarctica, Arctic |
| **Oblique Mercator** | Conformal | Elongated regions | Panama Canal zone |

## Forward and Inverse Problems

### Forward: $(\phi, \lambda) \to (E, N)$

Given geodetic coordinates, apply the projection formulas to get easting (E) and northing (N):

$$E = E_0 + k_0 \cdot f_1(\phi, \lambda)$$
$$N = N_0 + k_0 \cdot f_2(\phi, \lambda)$$

where $E_0, N_0$ are false easting/northing, $k_0$ is the scale factor.

### Inverse: $(E, N) \to (\phi, \lambda)$

Solve the inverse formulas (often iterative for TM projections).

## Key Parameters of Any Projection

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Central meridian | $\lambda_0$ | Reference longitude |
| Standard parallel(s) | $\phi_{SP}$ | Lines of true scale (no distortion) |
| False easting | $E_0$ | Shift x origin to avoid negative numbers |
| False northing | $N_0$ | Shift y origin (often for southern hemisphere) |
| Scale factor at origin | $k_0$ | Scales all projected distances |
| Ellipsoid | — | WGS84, GRS80, etc. |

## Comparison of Popular CRS

| CRS | EPSG | Zone System | Origin | False Easting | Scale Factor | Coverage |
|-----|------|-------------|--------|---------------|--------------|----------|
| **WGS84 / UTM Zone 33N** | 32633 | 6° bands | 15°E | 500,000 | 0.9996 | Northern hemisphere |
| **WGS84 / TM3** | — | 3° strips | Per zone | 500,000 | 0.9995 | Indonesia, Brazil |
| **State Plane (NAD83)** | 26901+ | Varies by state | State-dependent | 500,000+ | Varies | US per-state |
| **EPSG:4326** | 4326 | — (geographic) | Equator/Prime Meridian | — | 1.0 | Global |
| **Web Mercator** | 3857 | — | Equator/Prime Meridian | 0 | 1.0 | Web map tiles |

## Grid Distortion and Scale Factor

Projection introduces **distortion**. Conformal projections (UTM, TM) preserve angles but distort area/distance according to the scale factor:

| Property | UTM ($k_0 = 0.9996$) | TM3 ($k_0 = 0.9995$) |
|----------|----------------------|-----------------------|
| True scale at | 180 km east/west of CM | 370 km east/west of CM |
| Maximum $k$ on zone | ~1.00040 (at zone edge) | ~1.00016 (at ±1.5°) |
| Area distortion | ~0.04% at edges | ~0.05% at edges |

The scale factor $k_0 < 1$ means projections are **slightly smaller** than the ellipsoid at the central meridian, and **grow to exactly 1** at the standard parallels, then **exceed 1** toward zone edges.

## Worked Example: Projected Distance

**Problem:** Two points in UTM Zone 33N have projected coordinates:
$A: (290312.3,\ 5712982.2)$
$B: (340500.1,\ 5740120.5)$

Compute the grid distance.

**Solution:**
$$\Delta E = 340500.1 - 290312.3 = 50187.8\ \text{m}$$
$$\Delta N = 5740120.5 - 5712982.2 = 27138.3\ \text{m}$$

$$d_{\text{grid}} = \sqrt{50187.8^2 + 27138.3^2} = \sqrt{2518816563 + 736488307} = 57134.6\ \text{m}$$

**To get the true ground distance**, multiply by the average scale factor at the midpoint. If $k_{\text{mid}} = 1.0002$, then:
$$d_{\text{true}} = 57134.6 / 1.0002 = 57123.2\ \text{m}$$

(Difference: 11.4 m over 57 km — due to 0.02% average distortion.)

## Accuracy Budget for Surveying

| Error Source | Typical Magnitude | Notes |
|--------------|-------------------|-------|
| Scale factor uncertainty | 1–5 mm/km | Depends on $k_0$ and position |
| Projection distortion | 0–50 mm/km | Depends on zone width vs. distance from CM |
| Elevation factor | 1–5 mm/km | Height reduction to sea level |
| Combined ground distance error | 1–10 mm/km | For precise surveys |

## Key Rule

> **Never use projected coordinates for long-distance (inter-continental) computations.** Always use [[Geodetic Coordinates]] or [[Geocentric Cartesian ECEF]] for global geodetic work. Use projected coordinates only within their designed zone (typically ±3° of the central meridian).

## References
- Snyder, J. P. (1987). *Map Projections — A Working Manual*. USGS Professional Paper 1395.
- Bugayevski, L. A. & Snyder, J. P. (1995). *Map Projections: A Reference Manual*. Taylor & Francis.
- Burtch, R. & Hirt, C. (2009). *Reducing distortion in projected coordinates*. Journal of Geodesy.

## Related
- [[Map Projection]] · [[UTM]] · [[Transverse Mercator]] · [[Geodetic Coordinates]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
