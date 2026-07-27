---
tags: [aigis, concept, geodesy, grs80, reference-ellipsoid, iers]
aliases: [Geodetic Reference System 1980]
created: 2026-07-27
updated: 2026-07-27
---

# GRS80 — Geodetic Reference System 1980

## Overview

**GRS80** is the reference ellipsoid adopted by the [[IERS]] (International Earth Rotation and Reference Systems Service) and used as the basis for [[ITRF]], [[ETRS89]], and many national [[Datum|datums]]. It defines only the geometric ellipsoid and gravitational constant — not a full gravity formula (unlike [[WGS84]]).

## Defining Constants (Exact)

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Geocentric gravitational constant | $GM$ | 3.986 005 × 10¹⁴ | m³/s² |
| Angular velocity | $\omega$ | 7.292 115 × 10⁻⁵ | rad/s |
| Semi-major axis | $a$ | 6 378 137 | m (exact) |

## Derived Geometric Parameters

| Parameter | Formula | Value |
|-----------|---------|-------|
| Flattening $f$ | $f = \frac{a-b}{a}$ | 1/298.257 222 101 |
| Semi-minor axis $b$ | $b = a(1-f)$ | 6 356 752.314 140 m |
| First eccentricity² $e^2$ | $e^2 = 2f - f^2$ | 0.006 694 380 022 90 |
| Second eccentricity² ${e'}^2$ | ${e'}^2 = e^2/(1-e^2)$ | 0.006 739 496 775 48 |

## Derivation of $e^2$

Starting from $f$:

$$

e^2 = 2f - f^2 = 2 \times \frac{1}{298.257222101} - \left(\frac{1}{298.257222101}\right)^2

$$

$$

= 6.705\,516\,586 \times 10^{-3} - 1.126\,412\,239 \times 10^{-5}

$$

$$

= 6.694\,380\,022\,90 \times 10^{-3}

$$

## GRS80 vs WGS84

| Property | GRS80 | [[WGS84]] |
|----------|-------|-----------|
| $a$ (m) | 6 378 137.0 | 6 378 137.0 |
| $1/f$ | 298.257222101 | 298.257223563 |
| Difference in $f$ | — | $\Delta f = 1.6 \times 10^{-11}$ |
| $GM$ | 3.986 005 × 10¹⁴ | 3.986 004 418 × 10¹⁴ |
| $\omega$ | 7.292 115 × 10⁻⁵ | 7.292 115 146 7 × 10⁻⁵ |
| Gravity formula | Not specified | Somigliana |

The $1/f$ difference produces a maximum surface separation of:

$$

\Delta h_{max} = a \cdot \Delta f \approx 6.378 \times 10^6 \times 1.6 \times 10^{-11} \approx 0.1 \text{ mm}

$$

**Conclusion:** The two ellipsoids are geometrically indistinguishable for all surveying purposes.

## Radius of Curvature (on GRS80)

### Meridian Radius

$$

M(\varphi) = \frac{a(1 - e^2)}{(1 - e^2 \sin^2\varphi)^{3/2}}

$$

### Prime Vertical Radius

$$

N(\varphi) = \frac{a}{(1 - e^2 \sin^2\varphi)^{1/2}}

$$

### Gaussian Curvature Radius

$$

K(\varphi) = \frac{MN}{a^2} = \frac{a}{(1 - e^2\sin^2\varphi)}

$$

## Values at Key Latitudes

| Latitude | $M$ (m) | $N$ (m) | $1°$ meridian (km) | $1°$ parallel (km) |
|----------|---------|---------|---------------------|---------------------|
| 0° (equator) | 6 335 439 | 6 378 137 | 110.574 | 111.320 |
| 30° | 6 367 389 | 6 388 851 | 110.852 | 96.486 |
| 45° | 6 388 851 | 6 388 851 | 111.132 | 78.847 |
| 60° | 6 399 594 | 6 378 137 | 111.414 | 55.800 |
| 90° (pole) | 6 399 594 | 6 367 443 | 111.694 | 0 |

### Length of 1° Arc

**Meridian:**

$$

\Delta s_M \approx M(\varphi) \times \frac{\pi}{180}

$$

**Parallel:**

$$

\Delta s_P \approx N(\varphi) \cos\varphi \times \frac{\pi}{180}

$$

## Geodetic Reference System of 1980 (Resolution IAG 1979)

The full GRS80 system specifies:

1. **Gravity formula:** International Gravity Formula (IGF 1980)

   $$

   \gamma_0(\varphi) = 9.780327(1 + 0.0053024\sin^2\varphi - 0.0000058\sin^2 2\varphi) \text{ m/s}^2

   $$

2. **Reference potential:** $W_0 = 62\,636\,856.8 \text{ m}^2/\text{s}^2$ (geoid potential)
3. **Normal gravity at equator:** $\gamma_a = 9.780327$ m/s²
4. **Normal gravity at pole:** $\gamma_p = 9.832186$ m/s²

## In [[Geodesy]] Context

### Used By
- [[ITRF]] — All realizations use GRS80
- [[ETRS89]] — European realization of ITRF on GRS80
- [[GRS80#Australian datum|GDA94/GDA2020]] — Australian datum
- [[NAD83]] — North American Datum (based on GRS80, not WGS84)

### NOT Used By
- [[WGS84]] — Uses slightly different $1/f$
- [[NAD27]] — Uses Clarke 1866 ellipsoid
- Indonesian [[Datum|Datum Q]] — Uses WGS84 (BIG)

## Study Problems

1. Compute the meridian radius $M$ at Jakarta ($\varphi = -6°12'$).
2. Show that $e^2 = 2f - f^2$ algebraically.
3. Calculate the surface distance between two points at the equator separated by $1°$ longitude.
4. Explain why GRS80 was chosen over WGS84 for ITRF.

## Related Concepts

- [[WGS84]] — Nearly identical ellipsoid
- [[Reference Ellipsoid]] — Mathematical surface
- [[ITRF]] — Uses GRS80 as basis
- [[Eccentricity]] — Derived parameter
- [[Flattening]] — Derived parameter
- [[Gravity Field]] — GRS80 defines normal gravity
- [[Geodetic Coordinates]] — Coordinates on GRS80

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
