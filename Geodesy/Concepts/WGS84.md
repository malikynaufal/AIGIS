---
tags: [aigis, concept, geodesy, reference-frame, wgs84, ellipsoid, coordinate-system]
aliases: [World Geodetic System 1984]
created: 2026-07-27
updated: 2026-07-27
---

# WGS84 — World Geodetic System 1984

## Overview

**WGS84** is the global terrestrial reference system maintained by the U.S. Department of Defense (DoD). It defines the Earth's shape as an ellipsoid and provides the standard coordinate frame for GPS/GNSS positioning. WGS84 is functionally equivalent to [[ITRF]] for most practical purposes (sub-centimeter agreement as of WGS84 G2139).

## Fundamental Parameters

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Semi-major axis | $a $ | 6 378 137.0 | m |
| Inverse flattening | $ 1/f $ | 298.257223563 | — |
| Flattening | $ f $ | 1/298.257223563 = 3.3528106647474805e-3 | — |
| Semi-minor axis | $ b $ | 6 356 752.314245 | m |
| First eccentricity² | $ e^2 $ | 0.00669437999014 | — |
| Second eccentricity² | $ {e'}^2 $ | 0.00673949674228 | — |
| Equatorial gravity | $\gamma_a $ | 9.7803253359 | m/s² |
| Polar gravity | $\gamma_p $ | 9.8321849378 | m/s² |
| Mean angular velocity | $\omega $ | 7.2921151467e-5 | rad/s |
| GM (Earth + atmosphere) | $ GM $ | 3.986004418e14 | m³/s² |

## Derived Quantities

$ $ b = a(1 - f) = 6{,}356{,}752.314245 \text{ m}$$

$ $ e^2 = \frac{a^2 - b^2}{a^2} = 2f - f^2 $$

$ ${e'}^2 = \frac{a^2 - b^2}{b^2} = \frac{e^2}{1 - e^2}$$

### Radius of Curvature

| Quantity | Formula | Value at equator | Value at pole |
|----------|---------|-------------------|---------------|
| Meridian radius $ M $ | $\frac{a(1-e^2)}{(1-e^2\sin^2\varphi)^{3/2}} $ | 6 335 439 m | 6 399 594 m |
| Prime vertical radius $ N $ | $\frac{a}{(1-e^2\sin^2\varphi)^{1/2}} $ | 6 378 137 m | 6 399 594 m |
| Mean radius $ R $ | $\sqrt{MN} $ | — | — |

### Normal Gravity (Somigliana Formula)

$ $\gamma_0(\varphi) = \frac{\gamma_a (1 + k\sin^2\varphi)}{\sqrt{1 - e^2\sin^2\varphi}}

$$

where:$ $ k = \frac{b\gamma_p - a\gamma_a}{a\gamma_a} = 0.00193185138639 $$

## WGS84 Evolution

| Version | Year | Key Change | Alignment |
|---------|------|------------|-----------|
| WGS84 (original) | 1987 | Adopted GRS80 parameters | NWL-9D |
| WGS84 G730 | 1997 | Aligned with ITRF94 | ITRF94 (cm-level) |
| WGS84 G873 | 2001 | Aligned with ITRF97 | ITRF97 (cm-level) |
| WGS84 G1150 | 2002 | Aligned with ITRF2000 | ITRF2000 (mm-level) |
| WGS84 G1674 | 2011 | Aligned with ITRF2008 | ITRF2008 (mm-level) |
| WGS84 G1762 | 2014 | Aligned with ITRF2008 | ITRF2008 (mm-level) |
| WGS84 G2139 | 2023 | Aligned with ITRF2014 | ITRF2014 (mm-level) |

## WGS84 vs GRS80

The WGS84 ellipsoid is defined with the **same** $ a $ and $ 1/f $ as [[GRS80]], but WGS84 uses the full normal gravity formula while GRS80 defines only the geometry. For geodetic computations the two are interchangeable.

| Property | WGS84 | GRS80 |
|----------|-------|-------|
| $ a $ (m) | 6 378 137.0 | 6 378 137.0 |
| $ 1/f $ | 298.257223563 | 298.257222101 |
| Purpose | Full system (coord + gravity) | Reference ellipsoid only |
| GM | ✅ Defined | ✅ Defined |
| Normal gravity | ✅ Somigliana | Not specified |

## In [[Geodesy]] Context

### ECEF → Geodetic (Bowring Iteration)

Given $ (X, Y, Z) $ in [[Geocentric Cartesian ECEF]]:

$ $ p = \sqrt{X^2 + Y^2} $$

$ $ \lambda = \arctan2(Y, X)

$$

$ $\varphi^{(0)} = \arctan\left(\frac{Z}{p(1-e^2)}\right)

$$

Iterate:$ $ N^{(i)} = \frac{a}{\sqrt{1 - e^2\sin^2\varphi^{(i)}}} $$

$ $ \varphi^{(i+1)} = \arctan\left(\frac{Z + e^2 N^{(i)}\sin\varphi^{(i)}}{p}\right)

$$

Converges in 3–4 iterations to $< 1 $ mm.

### Height Relationship

$ $ h = \frac{p}{\cos\varphi} - N \quad \text{or} \quad h = \frac{Z}{\sin\varphi} + e^2 N $$

where $ h $ is [[Ellipsoidal Height]].

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ e^2 = 2f - f^2 $ | Eccentricity | All ellipsoidal math |
| $ N = a/\sqrt{1-e^2\sin^2\varphi} $ | Prime vertical radius | Geodetic ↔ ECEF |
| $\gamma_0 = \frac{\gamma_a(1+k\sin^2\varphi)}{\sqrt{1-e^2\sin^2\varphi}} $ | Normal gravity | Physical geodesy |
| $ h = H + N $ | Height relationship | GPS heighting |

## Applications in Indonesian Surveying

- **Horizontal control:** All BPN (Badan Pertanahan Nasional) surveys use WGS84 as the reference
- **GNSS networks:** CORS Indonesia (BIG) uses ITRF2014/WGS84
- **Topographic mapping:** Rupabumi map series uses UTM on WGS84
- **Cadastral surveys:** WGS84 mandatory for new land boundary surveys since 2014

## Study Problems

1. Compute the meridian radius of curvature at latitude $\varphi = -6°$ (Jakarta).
2. Given ECEF coordinates $ (X, Y, Z) = (−5{,}242{,}000, \ldots) $, convert to geodetic.
3. Explain why WGS84 G2139 is essentially identical to [[ITRF]]2014.
4. Compute normal gravity at the equator and pole; what is the difference?

## Common Mistakes

1. **Confusing $ a $ and $ b $** — $ a $ is always semi-major (equatorial), $ b $ is semi-minor (polar).
2. **Using wrong sign for flattening** — $ f > 0 $, not negative.
3. **Treating WGS84 as static** — it was updated 7 times; always specify the realization.
4. **Mixing WGS84 and GRS80** — they differ in $ 1/f $ by 0.0000000001; negligible for surveying but matters for precise orbits.

## Related Concepts

- [[GRS80]] — Nearly identical ellipsoid
- [[ITRF]] — Current realization standard
- [[Reference Ellipsoid]] — Theoretical basis
- [[Geodetic Coordinates]] — $ (\varphi, \lambda, h) $ on WGS84
- [[Geocentric Cartesian ECEF]] — $ (X, Y, Z)$
- [[Datum]] — The broader reference system
- [[GPS]] — Primary user of WGS84

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
