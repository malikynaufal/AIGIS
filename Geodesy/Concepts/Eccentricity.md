---
tags: [geodesy, concept, geometric-geodesy, aigis]
aliases: [Eccentricity, Eksentrisitas, First Eccentricity, Second Eccentricity]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 Eccentricity (e, e′)

In geodesy, **eccentricity** measures how far an ellipse deviates from a circle. It is a fundamental parameter that appears in nearly every ellipsoidal computation — from meridian arc length to [[Geodetic Coordinates]] conversion and [[Map Projection]] formulas.

## First Eccentricity (e)

The **first eccentricity** $e$relates the semimajor axis$a$and semiminor axis$b$:
$$

e = \sqrt{1 - \frac{b^2}{a^2}}$$For Earth-like ellipsoids,$e \approx 0.08$, indicating a near-circular but distinctly oblate shape.

## Second Eccentricity (e′)

The **second eccentricity** $e'$is used in some geodetic formulas (particularly for auxiliary latitudes and the [[Transverse Mercator]] projection):$$e' = \sqrt{\frac{a^2}{b^2} - 1}$$It is related to the first eccentricity by:$$e' = \frac{e}{\sqrt{1 - e^2}}$$## Linear Eccentricity (c)

The linear eccentricity (distance from center to focus) is:$$c = \sqrt{a^2 - b^2} = a e$$## Numerical Values for Common Ellipsoids

| Ellipsoid |$a$(m) |$b$(m) |$e$|$e^2$|$e'$|$e'^2$|
|-----------|---------|---------|-----|-------|------|--------|
| **WGS84** | 6,378,137.0 | 6,356,752.3142 | 0.0818191908426 | 0.0066943799901 | 0.0820944379497 | 0.0067394967423 |
| **GRS80** | 6,378,137.0 | 6,356,752.3141 | 0.0818191910428 | 0.0066943800229 | 0.0820944381517 | 0.0067394967755 |
| **Clarke 1866** | 6,378,206.4 | 6,356,583.8 | 0.0822718542230 | 0.0067686580 | 0.0825456977 | 0.0068147850 |
| **Airy 1830** | 6,377,563.4 | 6,356,256.9 | 0.0816733741 | 0.0066705400 | 0.0819724598 | 0.0067194900 |
| **Bessel 1841** | 6,377,397.2 | 6,356,079.0 | 0.0816968312 | 0.0066743720 | 0.0819969334 | 0.0067237000 |
| **IUGG 1967** | 6,378,160.0 | 6,356,774.5 | 0.0818201520 | 0.0066945370 | 0.0820959412 | 0.0067397187 |
| **Hayford 1909** | 6,378,388.0 | 6,356,911.9 | 0.0819918899 | 0.0067226700 | 0.0822688893 | 0.0067681700 |

## Relationship to Flattening

The first eccentricity$e$and [[Flattening]]$f$are mathematically linked:$$e^2 = 2f - f^2
$$

$$
f = 1 - \sqrt{1 - e^2}$$This relationship means an ellipsoid can be defined equivalently by$(a, f)$or$(a, e)$. For small flattening ($f \approx 0.00335$for Earth), a useful approximation is:$$e^2 \approx 2f$$## Eccentricity in Geodetic Formulas

| Application | Where$e$Appears |
|-------------|-------------------|
| Meridian arc radius |$M = \frac{a(1-e^2)}{(1 - e^2\sin^2\phi)^{3/2}}$|
| Prime vertical radius |$N = \frac{a}{\sqrt{1 - e^2\sin^2\phi}}$|
| Lat ↔ ECEF conversion | Parametric latitude$\psi$: $\tan\psi = \sqrt{1 - e^2}\tan\phi$|
| [[Vincenty Formula]] | Reduced latitude:$\tan u = \sqrt{1 - e^2}\tan\phi$|
| Geodesic length | Elliptic integrals of the second kind in$e$|

## Geodetic Latitude vs. Eccentricity

The relationship between geodetic latitude$\phi$, geocentric latitude $\theta$, and reduced latitude $\beta$all depend on eccentricity:$$\tan\theta = (1 - e^2)\tan\phi
$$

$$\tan\beta = \sqrt{1 - e^2}\tan\phi$$

## Worked Example

**Problem:** For the WGS84 ellipsoid ($a = 6378137.0$m,$f = 1/298.257223563$), compute $e$, $e^2$, and $e'$.

**Solution:**
1. $f = 1/298.257223563 = 0.00335281066475$2.$e^2 = 2f - f^2 = 2(0.0033528) - (0.0033528)^2 = 0.0066943799901$3.$e = \sqrt{0.0066943799901} = 0.0818191908426$4.$e' = \frac{e}{\sqrt{1 - e^2}} = \frac{0.08181919}{\sqrt{0.99330562}} = 0.0820944379497$

## References

- Torge, W., & Müller, J. (2012). *Geodesy*. de Gruyter.

- Hofmann-Wellenhof, B., & Moritz, H. (2006). *Physical Geodesy*. Springer.

- NGA (2014). *World Geodetic System 1984: Its Definition and Relationships with Local Geodetic Systems*.

## Related

- [[Flattening]] · [[Reference Ellipsoid]] · [[Vincenty Formula]] · [[Geodetic Coordinates]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
