---
tags: [geodesy, concept, geometric-geodesy, aigis]
aliases: [Flattening, Kepipihan, First Flattening, Second Flattening, Reciprocal Flattening]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 Flattening (f, f′)

**Flattening** (also called *ellipticity* or *oblateness*) quantifies how much an ellipsoid deviates from a sphere. It is one of the two defining parameters (along with semimajor axis $a$) of any [[Reference Ellipsoid]].

## First Flattening (f)

The first flattening (or simply *flattening*) $f $is
:

$$f = \frac{a - b}{a} $$where $a$= equatorial radius (semimajor axis),$b$= polar radius (semiminor axis).

Earth's flattening is small:$f \approx 1/298.26$, meaning the polar radius is about 21 km shorter than the equatorial radius.

## Second Flattening (f′)

The second flattening $f'$(also called the *second ellipticity*) is
:

$$f' = \frac{a - b}{b} $$

It relates to the first flattening by
:

$$f' = \frac{f}{1 - f} $$

## Third Flattening (n) — Third Eccentricity Squared

The third flattening $n$(used in series expansions for geodesics) is
:

$$n = \frac{a - b}{a + b} = \frac{f}{2 - f} $$

For WGS84:$n \approx 0.001679220394$

## Reciprocal Flattening ($1/f$)

It is conventional to quote the **reciprocal flattening** rather than $f $itself:

| Ellipsoid | $a$(m) | $b$(m) | $f$ | $1/f$ |
|-----------|---------|---------|-----|-------|
| **WGS84** | 6,378,137.0 | 6,356,752.3142 | 0.00335281066475 | 298.257223563 |
| **GRS80** | 6,378,137.0 | 6,356,752.3141 | 0.00335281068118 | 298.257222101 |
| **Clarke 1866** | 6,378,206.4 | 6,356,583.8 | 0.003390075 | 294.978698 |
| **Airy 1830** | 6,377,563.4 | 6,356,256.9 | 0.003340850 | 299.324964 |
| **Bessel 1841** | 6,377,397.2 | 6,356,079.0 | 0.003342860 | 299.152812 |
| **International (Hayford 1909)** | 6,378,388.0 | 6,356,911.9 | 0.003367003 | 297.0 |
| **IUGG 1967** | 6,378,160.0 | 6,356,774.5 | 0.003352923 | 298.247 |

## Relationship to Eccentricity

Flattening and [[Eccentricity]] are mathematically linked:

$$e^2 = 2f - f^2e'^2 = \frac{2f - f^2}{(1 - f)^2}f = 1 - \sqrt{1 - e^2} $$### Taylor Series Expansion (for small f)

Since $f \approx 0.00335$(very small), series expansions converge quickly:

$$e^2 = 2f - f^2 = 2f\left(1 - \frac{f}{2}\right)e = \sqrt{2f}\left(1 - \frac{f}{4} - \frac{f^2}{32} - \cdots\right)e'^2 = 2f + 3f^2 + 4f^3 + \cdots$$## Parameter Relationships Summary

Given any two of $\{a, b, f, e\} $, all others are determined:

| Known | Formulas |
|-------|----------|
| $a, f$ | $b = a(1-f)$, $e^2 = 2f - f^2$ |
| $a, b$ | $f = (a-b)/a$, $e^2 = 1 - b^2/a^2$ |
| $a, e$ | $b = a\sqrt{1 - e^2} $, $f = 1 - \sqrt{1 - e^2} $ |

## Physical Origin

Earth's flattening is a direct consequence of its rotation
:

$$\Omega^2 a^3 \approx 2f GM$$where $\Omega$= angular velocity,$GM$= gravitational constant × mass. The centrifugal force at the equator creates a bulge; the theoretical hydrostatic flattening for a fluid Earth in equilibrium is approximately $f \approx 1/299$.

## Worked Example

**Problem:** An ellipsoid has $a = 6378137 $m and $b = 6356752.314 $m. Compute $f$, $1/f$, $f'$, and $n$.

**Solution:**
1. $f = \frac{a-b}{a} = \frac{6378137 - 6356752.314}{6378137} = \frac{21384.686}{6378137} = 0.00335281066$2.$1/f = 298.25722356$3.$f' = \frac{a-b}{b} = \frac{21384.686}{6356752.314} = 0.00336404567$4.$n = \frac{a-b}{a+b} = \frac{21384.686}{12734889.314} = 0.00167922039$

## References

- Torge, W. (2012). *Geodesy*. de Gruyter.

- Moritz, H. (2000). *Geodetic Reference System 1980*. Journal of Geodesy.

- NGA Technical Report TR8350.2 (3rd ed., 2014).

## Related

- [[Eccentricity]] · [[Reference Ellipsoid]] · [[GRS80]] · [[WGS84]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
