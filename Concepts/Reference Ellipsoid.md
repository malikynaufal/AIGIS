---
tags: [aigis, concept, geodesy, ellipsoid, wgs84, grs80, geodetic-coordinates]
created: 2026-07-27
updated: 2026-07-27
---

# Reference Ellipsoid

## For Geodesy & Coordinate Systems

**Core Idea:** The reference ellipsoid is a mathematically defined oblate spheroid that approximates Earth's shape. It serves as the geometric reference for all geodetic coordinates, satellite orbits, and map projections. Understanding its geometry is fundamental to converting between geodetic coordinates (latitude, longitude, height) and Cartesian ECEF coordinates.

---

## Fundamental Concepts

### The Ellipsoid as Reference Surface

An ellipsoid of revolution (oblate spheroid) is defined by:
- **Semi-major axis** $a$ (equatorial radius)
- **Semi-minor axis** $b$ (polar radius)
- **Flattening** $f = (a-b)/a$
- **First eccentricity** $e = \sqrt{(a^2-b^2)/a^2}$
- **Second eccentricity** $e' = \sqrt{(a^2-b^2)/b^2}$

### Relationships Between Parameters

$$b = a(1-f) = \frac{a}{\sqrt{1+e'^2}}$$
$$a = b\sqrt{1+e'^2} = \frac{b}{\sqrt{1-e^2}}$$
$$e^2 = 2f - f^2 = \frac{a^2-b^2}{a^2}$$
$$e'^2 = \frac{f(2-f)}{(1-f)^2} = \frac{a^2-b^2}{b^2}$$
$$f = 1 - \frac{b}{a} = 1 - \sqrt{1-e^2}$$

### Standard Reference Ellipsoids

| Ellipsoid | $a$ (m) | $f^{-1}$ | $b$ (m) | Use |
|-----------|---------|-----------|---------|-----|
| **WGS84** | 6,378,137.0 | 298.257223563 | 6,356,752.3142 | GPS, GNSS |
| **GRS80** | 6,378,137.0 | 298.257222101 | 6,356,752.31414 | IERS, ITRF |
| **Hayford 1924** | 6,378,388.0 | 297.0 | 6,356,911.9 | Historical |
| **Bessel 1841** | 6,377,397.155 | 299.1528128 | 6,356,078.963 | Indonesia (DGN95) |
| **Krassovsky 1940** | 6,378,245.0 | 298.3 | 6,356,863.0 | GLONASS |
| **IERS 2003** | 6,378,136.6 | 298.25642 | 6,356,751.9 | ITRF2014 |

**WGS84 vs GRS80:** Nearly identical; the difference is in the dynamic form factor $J_2$ and the derived flattening. For most applications, $a$ and $f$ are indistinguishable.

---

## Geodetic Coordinates

A point on or near Earth is specified by $(\phi, \lambda, h)$:

- $\phi$ = geodetic latitude (angle between equatorial plane and normal to ellipsoid)
- $\lambda$ = geodetic longitude (angle from prime meridian)
- $h$ = ellipsoidal height (distance from ellipsoid surface along normal)

**IMPORTANT:** Geodetic latitude is NOT the same as geocentric latitude (except at equator and poles).

### Ellipsoid Radius of Curvature

**Prime vertical radius of curvature:**
$$N(\phi) = \frac{a}{\sqrt{1 - e^2\sin^2\phi}}$$

**Meridian radius of curvature:**
$$M(\phi) = \frac{a(1-e^2)}{(1-e^2\sin^2\phi)^{3/2}}$$

**Ratio of curvatures:**
$$\eta^2 = \frac{N(\phi)}{M(\phi)}$$

| Latitude | $N$ (m) | $M$ (m) | $N/M$ |
|----------|---------|---------|-------|
| 0° (equator) | 6,378,137 | 6,335,439 | 1.00674 |
| 45° | 6,388,848 | 6,367,343 | 1.00332 |
| 90° (pole) | 6,399,594 | 6,399,594 | 1.00000 |

---

## Coordinate Transformations

### Geodetic → ECEF (Cartesian)

$$X = (N + h)\cos\phi\cos\lambda$$
$$Y = (N + h)\cos\phi\sin\lambda$$
$$Z = \left[N(1-e^2) + h\right]\sin\phi$$

### ECEF → Geodetic (Iterative)

**Bowring's method** (converges in 2–3 iterations):

$$\lambda = \arctan(Y/X)$$
$$p = \sqrt{X^2 + Y^2}$$
$$\phi_0 = \arctan\left(\frac{Z}{p(1-e^2)}\right)$$

Iterate:
$$N_i = \frac{a}{\sqrt{1-e^2\sin^2\phi_i}}$$
$$\phi_{i+1} = \arctan\left(\frac{Z + e^2 N_i \sin\phi_i}{p}\right)$$

Converge when $|\phi_{i+1} - \phi_i| < \epsilon$:
$$h = \frac{p}{\cos\phi} - N$$

### Exact Closed-Form (Vermeille/Borkowski)

$$X = (\nu + h)\cos\phi\cos\lambda$$
$$Y = (\nu + h)\cos\phi\sin\lambda$$
$$Z = \left[\nu(1-e^2) + h\right]\sin\phi$$

where:
$$p = \sqrt{X^2+Y^2}, \quad \nu = \frac{a^2}{\sqrt{a^2\cos^2\phi + b^2\sin^2\phi}}$$
$$\phi = \arctan\left(\frac{Z + e'^2 b\sin^3\theta}{p - e^2 a\cos^3\theta}\right)$$
where $\theta = \arctan(Za / pb)$

---

## Arc Lengths on the Ellipsoid

### Meridional Arc (Latitude $\phi_1$ to $\phi_2$)

$$s = a(1-e^2)\int_{\phi_1}^{\phi_2} \frac{d\phi}{(1-e^2\sin^2\phi)^{3/2}}$$

This integral must be evaluated numerically or by series expansion.

**Series expansion (to 4th order in $e^2$):**
$$s = a\left[A\phi - B\sin 2\phi + C\sin 4\phi - D\sin 6\phi\right]$$

where:
$$A = 1 - \frac{e^2}{4} - \frac{3e^4}{64} - \frac{5e^6}{256}$$
$$B = \frac{3e^2}{8} + \frac{3e^4}{32} + \frac{45e^6}{1024}$$
$$C = \frac{15e^4}{256} + \frac{45e^6}{1024}$$
$$D = \frac{35e^6}{3072}$$

### Geodesic Length on Ellipsoid

The shortest path between two points on the ellipsoid is a geodesic, not a great circle. Given $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$:

**Vincenty's formula** (iterative):
$$\sin U_1 = (1-f)\sin\phi_1, \quad \cos U_1 = \cos\phi_1$$
$$\sin U_2 = (1-f)\sin\phi_2, \quad \cos U_2 = \cos\phi_2$$
$$\lambda = L = \lambda_2 - \lambda_1$$

Iterate:
$$\sin\sigma = \sqrt{(\cos U_2\sin\lambda)^2 + (\cos U_1\sin U_2 - \sin U_1\cos U_2\cos\lambda)^2}$$
$$\cos\sigma = \sin U_1\sin U_2 + \cos U_1\cos U_2\cos\lambda$$
$$\sigma = \arctan(\sin\sigma/\cos\sigma)$$

Distance: $s = b \cdot A \cdot (\sigma + \Delta\sigma)$

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $N = a/\sqrt{1-e^2\sin^2\phi}$ | Prime vertical radius | Coordinate conversion |
| $X = (N+h)\cos\phi\cos\lambda$ | Geodetic → ECEF | Position conversion |
| $e^2 = 2f - f^2$ | Eccentricity from flattening | Parameter relations |
| $M = a(1-e^2)/(1-e^2\sin^2\phi)^{3/2}$ | Meridian radius | Arc length |
| $s = \int_{\phi_1}^{\phi_2} M\,d\phi$ | Meridional arc | Distance on ellipsoid |

---

## Related Concepts

- [[Geodetic Coordinates]] — Latitude, longitude, height
- [[Geocentric Cartesian ECEF]] — X, Y, Z coordinates
- [[Flattening]] — Ellipsoid shape parameter
- [[Eccentricity]] — Ellipsoid eccentricity
- [[GRS80]] — Standard reference ellipsoid
- [[WGS84]] — GPS reference system
- [[Map Projection]] — Ellipsoid → flat map
- [[Vincenty Formula]] — Geodesic distance

---

## Study Problems

1. **Recall:** Given WGS84 ($a = 6378137$, $f = 1/298.257223563$), compute $b$, $e^2$, and $e'^2$ to 10 significant figures.
2. **Application:** Compute the geodetic latitude $\phi$ for a point at ECEF $(X, Y, Z) = (4000000, 3000000, 4000000)$ m. Verify $\phi$ by converting back.
3. **Derivation:** Derive the relationship $e^2 = 2f - f^2$ from the definitions of $f = (a-b)/a$ and $e^2 = (a^2-b^2)/a^2$.
4. **Real-world:** Compute the meridional arc length from $\phi = -8°$ (Jakarta, Indonesia) to $\phi = 0°$ (equator) on WGS84. This is the north-south extent of western Java.

---

## Common Mistakes

1. **Confusing geodetic and geocentric latitude:** They differ by up to 11.5 arcminutes at 45° latitude.
2. **Using spherical geometry on an ellipsoid:** Earth is NOT a sphere — the difference matters for precision.
3. **Forgetting that $h$ is measured from the ellipsoid, not mean sea level:** The geoid undulation $N = h - H$ connects them.
4. **Wrong sign in coordinate conversions:** $(1-e^2)$ multiplies $N$ only in the $Z$ component.
5. **Ignoring convergence issues in Bowring's method:** Near the poles, more iterations may be needed.

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*