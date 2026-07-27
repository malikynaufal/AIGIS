---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [WGS84, World Geodetic System 1984]
created: 2026-07-12
updated: 2026-07-27
---

# 🛰️ WGS84

**WGS84** (World Geodetic System 1984) is the global datumbasis for GPS and most mapping, aviation, and navigation worldwide. It couples the **WGS84 ellipsoid** (essentially GRS80) with an Earth-centered origin consistent with the [[ITRF]]. Each WGS84 realization (WGS84 G1150, G1674, G1762, G2139, G2296) is aligned to a specific ITRF realization.

## WGS84 Ellipsoid Parameters

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Semimajor axis | $a$| 6,378,137 | m |
| Semiminor axis |$b$| 6,356,752.31424 | m |
| First flattening |$f$| 1/298.257223563 | — |
| Reciprocal flattening |$1/f$| 298.257223563 | — |
| 1st eccentricity² |$e^2$| 0.006694379990 | — |
| 2nd eccentricity² |$e'^2$| 0.0067394967423 | — |
| Gravitational constant |$GM$| 3,986,004.418 × 10⁸ | m³/s² |
| Angular velocity |$\omega$| 7.292115 × 10⁻⁵ | rad/s |

### Derived Quantity — Normal Gravity (Somigliana)$$g_0(\phi) = \frac{GM}{a\,b}\cdot\frac{1 + \frac{a^2\omega^2}{GM}\sin^2\phi}{\sqrt{1 - e^2\sin^2\phi}}$$At the equator:$g_0 \approx 9.780325$m/s². At the pole:$g_0 \approx 9.832186$m/s².

## WGS84 Realizations and ITRF Alignment

WGS84 is not a fixed frame — it is periodically realigned to the latest ITRF:

| WGS84 Realization | ITRF Realization Aligned To | Alignment Accuracy |
|-------------------|------------------------------|---------------------|
| WGS84 G1150 | ITRF89 + ITRF91 | ~10 cm |
| WGS84 G1274 | ITRF2000 | ~1 cm |
| WGS84 G1674 | ITRF2008 | < 5 cm |
| WGS84 G1762 | ITRF2008 | < 1 cm |
| **WGS84 G2139** | **ITRF2014** | **< 0.5 cm** |
| WGS84 G2296 | ITRF2020 | < 0.3 cm |

### How Alignment Is Done

1. A 7-parameter Helmert transformation is determined from overlapping stations (ITRF stations vs. WGS84 stations).
2. Parameters are published by NGA in the WGS84 Technical Report.
3. Modern receivers use the latest WGS84 (G2296), which is essentially consistent with ITRF2020 at the mm level.

## Relationship to ITRF

The key relationships:$$\mathbf{X}_{WGS84}(t) = \mathbf{X}_{ITRF2020}(t) + \mathbf{T}_{\text{WGS→ITRF}}(t)$$where$\mathbf{T}$is a time-dependent translation of order ~10 cm that changes with each realization.

### WGS84 vs. Other Datums

| Datum | Same origin? | Same ellipsoid? | Max coord. difference (continental US) |
|-------|--------------|------------------|----------------------------|
| **WGS84** | Yes (geocentric) | GRS80 (≈, not identical) | Reference |
| **ITRF2020** | Yes (cm-level) | GRS80 | < 0.05 m |
| **ETRS89** | No | GRS80 | ~0.3 m (fixed to Eurasia) |
| **NAD83(2011)** | No (plate-fixed) | GRS80 | ~1.5 m (growing) |
| **NAD27** | No | Clarke 1866 | 50–200 m |
| **WGS72** | No | GRS67-derived | Up to 1 m globally |

## Significance for GNSS

- **GPS receivers** output WGS84 coordinates by default.

- **The navigation message** encodes satellite orbit and clock information in WGS84.

- **The IGV (Initial Guess Value)** for GNSS precise processing starts from WGS84.

- **All consumer and scientific GNSS** positioning is ultimately WGS84-based, tied to ITRF through the latest WGS realization.

## Worked Example: ETRS89-to-WGS84 Alignment

**Problem:** Show how roughly ETRS89 and WGS84 differ at a European station.

**Solution:**

- Take a European station with known ETRS89 coordinates:$\phi = 50^\circ, \lambda = 8^\circ, h = 100$m

- Convert to ECEF using ETRS89 (GRS80 ellipsoid) →$(X, Y, Z)$- Apply the Helmert 14-param transformation (epoch-dependent) to convert to WGS84 ITRF-aligned ECEF

- Convert back to geodetic → the difference is$d\phi \sim 0.01$″, $d\lambda \sim 0.03$″, $dh \sim 0.1$ m

- For practical GNSS, this difference is negligible; for scientific geodesy (mm work), the time-dependent transform matters.

## References

- NGA (2014). *WGS84 Technical Report TR8350.2*, 3rd edition.

- NGA (2024). *WGS84 G2296 Realization*.

- NGS (2014). *NAD83 and WGS84 Connection*. NGS GeodeticGlossary.

## Related

- [[Datum]] · [[GPS]] · [[GRS80]] · [[ITRF]] · [[Helmert Transformation]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
