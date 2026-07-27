---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [GRS80, Geodetic Reference System 1980]
created: 2026-07-12
updated: 2026-07-27
---

# 📏 GRS80

**GRS80** (Geodetic Reference System 1980) is a complete geodetic datum adopted by the [[IERS]] and used as the reference ellipsoid for [[NAD83]], [[ETRS89]], and the Australian reference frames (GDA94/GDA2020). It is nearly identical to [[WGS84]] but differs in its flattening by $1$part in$298{,}257$— about 0.1 mm over the Earth's radius.

## GRS80 Parameters

| Parameter | Symbol | Value (GRS80) | Unit |
|-----------|--------|---------------|------|
| Semimajor axis |$a$| 6,378,137 | m |
| Gravitational constant |$GM$| 3,986,005 × 10⁸ | m³/s² |
| Angular velocity |$\omega$| 7,292,115 × 10⁻¹¹ | rad/s |
| Semiminor axis |$b$| 6,356,752.3141 | m |
| 1st flattening |$f$| 1/298.257222101 | — |
| 2nd flattening |$f'$| 1/297.9886736 | — |
| 3rd flattening |$n$| 1/596.1453779 | — |
| 1st eccentricity² |$e^2$| 0.0066943800229 | — |
| 2nd eccentricity² |$e'^2$| 0.0067394967755 | — |
| Polar radius |$b$ | 6,356,752.3141 | m |

### Derived Quantities

The three fundamental parameters ($a$, $GM$, $\omega$) generate all others through the equilibrium theory of a rotating fluid Earth:

**From the equilibrium flattening equation:**
$$

\frac{a^3 \omega^2}{GM} = \frac{2f - f^2}{(1 - f)^2} \left(1 - \frac{3}{2}m\right), \quad m = \frac{\omega^2 a^3}{GM}$$Solving iteratively for$f$with$a$, $GM$, $\omega$known yields GRS80's flattening.

**Normal gravity formula (Somigliana):**$$g_0(\phi) = \frac{GM}{a b} \cdot \frac{1 + k\sin^2\phi}{\sqrt{1 - e^2\sin^2\phi}}$$where:$$k = \frac{b\,\omega^2\,a}{GM} - \frac{3}{2}J_2\left(\frac{a\,\omega^2\,a}{GM}\right)$$## Comparison: GRS80 vs. WGS84

| Parameter | GRS80 | WGS84 (WGS84.G2139) | Difference |
|-----------|-------|----------------------|------------|
|$a$(m) | 6,378,137 | 6,378,137.0 | **Exact same** |
|$1/f$| 298.257222101 | 298.257223563 |$\Delta f \approx 1.4 \times 10^{-11}$|
|$e^2$| 0.0066943800229 | 0.0066943799901 |$3.3 \times 10^{-10}$|
|$GM$(m³/s²) | 3.986005 × 10¹⁴ | 3.986004418 × 10¹⁴ |$0.1 \times 10^{8}$ (≈$4.2 \times 10^{6}$m³/s²) |
|$\omega$(rad/s) | 7.292115 × 10⁻⁵ | 7.2921151467 × 10⁻⁵ |$1.5 \times 10^{-11}$|

### Physical Consequences of the Difference

The maximum difference in computed coordinates between GRS80 and WGS84:

| Quantity | Max Difference |
|----------|---------------|
| Latitude (same$X,Y,Z$) | ~0.11″ ≈ 3.3 m at equator |
| Longitude (same $X,Y,Z$) | ~0.02″ ≈ 0.6 m at equator |
| Radius of curvature | < 0.1 m |
| Geodesic distance (1000 km) | < 1 mm |
| ECEF coordinates (same geodetic) | < 0.1 mm |

These differences are negligible for most applications but matter for geodetic work at the sub-centimeter level.

## Which Geodetic Systems Use GRS80?

| Geodetic System | Region | Status |
|----------------|--------|--------|
| **NAD83** (original 1987) | North America | Replaced by HARN/CSRS/NATRF2022 |
| **NAD83(2011)** | US | Current realization (EPSG:6318) |
| **ETRS89** | Europe | Official EU datum (EPSG:4258) |
| **GDA94** | Australia | Replaced by GDA2020 |
| **GDA2020** | Australia | Current (EPSG:7844) |
| **REFRAME** | New Zealand | Used with NZGD2000 |
| **JGD2011** | Japan | National CRS |

### Why GRS80 Was Chosen Over WGS84

1. GRS80 is derived from fundamental geodetic constants (self-consistent), while WGS84 was fitted to a best surface through the best available data at the time.
2. GRS80's $GM$and$\omega$ are **theoretical geodetic constants** (for a reference Earth), while WGS84's are measured quantities.
3. International adoption by IAU/IERS gave GRS80 broad consensus.

## Usage in Practice

### PROJ / PyPROJ

```python
import pyproj

# GRS80 ellipsoid directly
crs_nad83 = pyproj.CRS("EPSG:4269")  # GRS80-based NAD83
print(crs_nad83.ellipsoid)  # GRS 1980
```

### EPSG Codes Based on GRS80

| EPSG Code | Description |
|-----------|-------------|
| 4269 | NAD83 (lat/lon) |
| 4283 | GDA94 (lat/lon) |
| 4258 | ETRS89 (lat/lon) |
| 6318 | NAD83(2011) (lat/lon) |
| 7844 | GDA2020 (lat/lon) |

## References

- Moritz, H. (1980). *Geodetic Reference System 1980*. Bulletin Géodésique, 54, 395–405.

- Moritz, H. (2000). *Geodetic Reference System 1980*. Journal of Geodesy, 74, 128–162.

- NGA (2014). *WGS84 Technical Report*.

- IERS Conventions (2010/2023).

## Related

- [[Reference Ellipsoid]] · [[NAD83]] · [[ETRS89]] · [[WGS84]] · [[Flattening]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]]
