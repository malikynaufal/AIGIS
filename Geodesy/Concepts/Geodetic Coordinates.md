---
tags: [geodesy, concept, coordinate-system, aigis]
aliases: [Geodetic Coordinates, φ, λ, Lintang Bujur, Geographic Coordinates]
created: 2026-07-12
updated: 2026-07-27
---

# 🌐 Geodetic Coordinates

**Geodetic coordinates** $(\phi, \lambda, h)$define a point's position **on the [[Reference Ellipsoid]]** (or its extension via height). They are the most natural coordinate system for geodesy, mapping, and GNSS positioning.

## Components

| Component | Symbol | Range | Physical Meaning |
|-----------|--------|-------|------------------|
| **Geodetic latitude** |$\phi$|$-90^\circ$to$+90^\circ$| Angle between ellipsoidal normal and equatorial plane |
| **Longitude** |$\lambda$|$-180^\circ$to$+180^\circ$| Angle east of prime meridian |
| **Ellipsoidal height** |$h$|$-\infty$to$+\infty$| Distance above ellipsoid along normal |

### Key Distinction: Geodetic vs. Geocentric Latitude

- **Geodetic latitude**$\phi$: angle between normal to ellipsoid and equatorial plane. This is the standard.

- **Geocentric latitude** $\theta$: angle between line from Earth's center to point and equatorial plane. Related by:
$$

\tan\theta = (1 - e^2)\tan\phi$$The difference is small (maximum ~11.5′ at 45°) but critical for satellite calculations and the [[Helmert Transformation]].

## Coordinate Systems Summary

| System | Coordinates | Use Case |
|--------|-------------|----------|
| Geodetic |$(\phi, \lambda, h)$| GNSS, mapping, geodesy |
| ECEF |$(X, Y, Z)$| Datum transforms, orbits |
| Local ENU |$(E, N, U)$| Relative surveying |
| Projected |$(E, N)$meters | Maps, cadastral |

## Conversion: Geodetic → ECEF (Forward)

Given$(\phi, \lambda, h)$, compute:

**Step 1:** Compute the radius of curvature in the prime vertical:
$$

N = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}$$**Step 2:** Compute ECEF coordinates:$$X = (N + h)\cos\phi \cos\lambda
$$

$$Y = (N + h)\cos\phi \sin\lambda$$

$$
Z = \left(N(1 - e^2) + h\right)\sin\phi$$## Conversion: ECEF → Geodetic (Inverse)

**Step 1:** Longitude (exact):$$\lambda = \arctan\left(\frac{Y}{X}\right)$$**Step 2:** Reduced circumference (Bowring's iteration, recommended for numerical stability):

Start with:$$p = \sqrt{X^2 + Y^2}
$$

$$e'^2 = \frac{a^2}{b^2} - 1 = \frac{2f - f^2}{(1-f)^2}$$

$$
\phi_1 = \arctan\left(\frac{Z}{p(1 - e^2) + 0}\right) \approx \arctan\left(\frac{Z}{p(1 - e^2)}\right)$$Iterate until convergence (typically 3–5 iterations):$$N_i = \frac{a}{\sqrt{1 - e^2\sin^2\phi_i}}
$$

$$
\phi_{i+1} = \arctan\left(\frac{Z + N_i e^2 \sin\phi_i}{p}\right)$$**Step 3:** Height:$$h = \frac{p}{\cos\phi} - N$$### Bowring's Iterative Method (1976)

A single-iteration approximation with sub-millimeter accuracy for most ellipsoids:$$\phi = \arctan\left(\frac{Z + b\,\varepsilon^2 \sin^3\theta}{p - a\,e^2 \cos^3\theta}\right)$$where$\theta = \arctan\left(\frac{a}{b} \cdot \frac{Z}{p}\right)$, $\varepsilon^2 = \frac{a^2 - b^2}{b^2}$, and the $e'^2 = \frac{a^2 - b^2}{b^2}$.

## Worked Example: Geodetic → ECEF

**Problem:** Convert WGS84 coordinates $(\phi, \lambda, h) = (51.477^\circ\text{N}, 0.001^\circ\text{W}, 100\ \text{m})$to ECEF.

**Solution:**

1. WGS84 parameters:$a = 6378137.0$m,$f = 1/298.257223563$2.$e^2 = 2f - f^2 = 0.006694379990$3. Convert$\phi = 51.477^\circ = 0.89865$rad,$\lambda = -0.001^\circ = -0.00001745$rad

4. Compute$N$:
$$N = \frac{6378137}{\sqrt{1 - 0.00669438 \times \sin^2(51.477^\circ)}}$$

$$\sin(51.477^\circ) = 0.78246, \quad \sin^2 = 0.61224$$

$$
N = \frac{6378137}{\sqrt{1 - 0.0040937}} = \frac{6378137}{\sqrt{0.995906}} = \frac{6378137}{0.997951} = 6391250\ \text{m}$$5. Compute XYZ:$$X = (6391250 + 100) \times \cos(51.477^\circ) \times \cos(-0.001^\circ)
$$

$$= 6391350 \times 0.62315 \times 0.999999985 = 3,982,718\ \text{m}$$

$$Y = 6391350 \times 0.62315 \times \sin(-0.001^\circ) = 6391350 \times 0.62315 \times (-0.0000175) = -69.1\ \text{m}$$

$$
Z = (6391250 \times 0.993306 + 100) \times 0.78246 = (6348522 + 100) \times 0.78246 = 4,966,175\ \text{m}$$**Result:**$(X, Y, Z) \approx (3,982,718, -69.1, 4,966,175)$m

## Worked Example: ECEF → Geodetic (Bowring)

**Problem:** Convert ECEF coords to geodetic using the same WGS84 ellipsoid.$(X, Y, Z) = (3.98\times10^6, -69, 4.97\times10^6)$m from above.

1.$p = \sqrt{X^2 + Y^2} = \sqrt{3982718^2 + 69^2} \approx 3,982,718$m (Y contribution negligible)

2.$\theta = \arctan\left(\frac{a}{b} \cdot \frac{Z}{p}\right)$, with $a/b = 1.0033528$
$$

\theta = \arctan\left(1.00335 \times \frac{4966175}{3982718}\right) = \arctan(1.00335 \times 1.2468) = \arctan(1.2511) = 51.356^\circ$$3.$e'^2 = \frac{a^2 - b^2}{b^2} = 0.0067395$4. Single iteration:$$\phi = \arctan\left(\frac{Z + b \cdot e'^2 \cdot \sin^3\theta}{p - a \cdot e^2 \cdot \cos^3\theta}\right)
$$

$$
= \arctan\left(\frac{4966175 + 6356752 \times 0.0067395 \times 0.1287}{3982718 - 6378137 \times 0.0066944 \times 0.648}\right)$$Numerator$\approx 4966175 + 5480 = 4971655$Denominator$\approx 3982718 - 28110 = 3954608$
$$

\phi = \arctan(4971655 / 3954608) = \arctan(1.2571) = 51.477^\circ$$5.$h$: With $\phi \approx 51.477^\circ$, $N = 6391250$m$$h = \frac{3982718}{\cos(51.477^\circ)} - 6391250 = \frac{3982718}{0.62315} - 6391250 = 6391250 - 6391250 + 100 \approx 100\ \text{m}$$**Recovery:** Original$h = 100$m — error < 0.1 mm after one iteration.

## Importance of Geodetic Coordinates

- **GNSS receivers** output$(\phi, \lambda, h)$in their configured datum (usually WGS84).

- **Datum transformations** convert between local datums (NAD83, ETRS89, etc.) using$7$- or $14$-parameter Helmert transforms in ECEF.

- **Map projections** (UTM, Transverse Mercator) take $(\phi, \lambda)$ as input.

- **Network adjustment** works in ECEF; results converted back to geodetic.

## References

- Torge, W. & Müller, J. (2012). *Geodesy*. de Gruyter, §4.1–4.5.

- Hofmann-Wellenhof, B. et al. (2008). *GNSS*. Springer, §3.1.3.

- Karney, C. F. F. (2011). *Transverse Mercator with an accuracy of a few nanometers*. Journal of Geodesy.

## Related

- [[Geocentric Cartesian ECEF]] · [[Local ENU NEU]] · [[Projected Coordinates]] · [[Reference Ellipsoid]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
