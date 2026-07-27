---
tags: [geodesy, concept, coordinate-system, aigis]
aliases: [ECEF, Geocentric Cartesian, Earth-Centered Earth-Fixed, XYZ]
created: 2026-07-12
updated: 2026-07-27
---

# 📦 Geocentric Cartesian (ECEF)

**Earth-Centered, Earth-Fixed (ECEF)** coordinates $(X, Y, Z)$ place the origin at Earth's center of mass, with $Z$ along the rotation axis (pointing toward the Conventional Terrestrial Pole), $X$ toward the prime meridian (Greenwich), and $Y$ completing the right-handed system. All values are in meters.

## Definition

$$(0,0,0) = \text{Earth's center of mass}$$
$$Z\text{-axis} = \text{Conventional Terrestrial Pole (CTP)}$$
$$X\text{-axis} = \text{Intersection of CTP equator and Greenwich meridian}$$
$$Y\text{-axis} = \text{Perpendicular to $X$ and $Z$ (right-handed)}$$

ECEF rotates with Earth — hence "Earth-fixed" — making coordinates of stationary ground points constant over time (ignoring plate tectonics).

## Conversion: Geodetic ($\phi, \lambda, h$) → ECEF ($X, Y, Z$)

The forward transformation is direct and closed-form:

$$N = \frac{a}{\sqrt{1 - e^2\sin^2\phi}}$$

$$X = (N + h)\cos\phi\cos\lambda$$
$$Y = (N + h)\cos\phi\sin\lambda$$
$$Z = \left(N(1 - e^2) + h\right)\sin\phi$$

where:
- $a$ = semimajor axis (e.g., 6,378,137.0 m for WGS84)
- $e^2 = 2f - f^2$ = first eccentricity squared
- $N$ = radius of curvature in the prime vertical

## Conversion: ECEF ($X, Y, Z$) → Geodetic ($\phi, \lambda, h$)

The inverse conversion requires **iteration** (or a closed-form solution). Longitude is exact:

$$\lambda = \arctan\left(\frac{Y}{X}\right)$$

For latitude, the classic iterative approach:

Start with:
$$p = \sqrt{X^2 + Y^2}$$
$$\phi_0 = \arctan\left(\frac{Z}{p(1 - e^2)}\right)$$

Iterate:
$$N_i = \frac{a}{\sqrt{1 - e^2\sin^2\phi_i}}$$
$$\phi_{i+1} = \arctan\left(\frac{Z + N_i e^2 \sin\phi_i}{p}\right)$$

Converges in 3–5 iterations to double-precision accuracy. Then:

$$h = \frac{p}{\cos\phi} - N$$

### Bowring's Algorithm (Non-Iterative)

A fast single-step method with ~μm accuracy:

$$\tau = \frac{Z}{p}\frac{a}{b}$$
$$\phi = \arctan\left(\frac{Z + b\,e'^2\sin^3\theta}{p - a\,e^2\cos^3\theta}\right), \quad \theta = \arctan(\tau)$$

## Worked Example

**Problem:** Convert geodetic coordinates $\phi = 40^\circ\text{N}$, $\lambda = 105^\circ\text{W}$, $h = 500$ m on WGS84 to ECEF.

**Solution (WGS84: $a = 6378137$ m, $e^2 = 0.0066943799901$):**

1. Convert to radians: $\phi = 40^\circ = 0.6981317$ rad, $\lambda = -105^\circ = -1.8325957$ rad

2. Compute $N$:
$$N = \frac{6378137}{\sqrt{1 - 0.0066943799901 \times \sin^2(0.6981317)}}$$
$$\sin\phi = 0.6427876, \quad \sin^2\phi = 0.4131759$$
$$N = \frac{6378137}{\sqrt{1 - 0.00669438 \times 0.4131759}} = \frac{6378137}{\sqrt{0.997234}} = \frac{6378137}{0.998616} = 6387070.6\ \text{m}$$

3. Compute $X, Y, Z$:
$$X = (6387070.6 + 500) \times \cos(40^\circ) \times \cos(-105^\circ)$$
$$\cos(40^\circ) = 0.7660444$$
$$\cos(-105^\circ) = \cos(105^\circ) = -0.2588190$$
$$X = 6387570.6 \times 0.7660444 \times (-0.2588190) = -1266785.3\ \text{m}$$

$$Y = 6387570.6 \times 0.7660444 \times \sin(-105^\circ)$$
$$\sin(-105^\circ) = -\sin(105^\circ) = -0.9659258$$
$$Y = 6387570.6 \times 0.7660444 \times (-0.9659258) = -4728779.7\ \text{m}$$

$$Z = (6387070.6 \times (1 - 0.00669438) + 500) \times 0.6427876$$
$$Z = (6387070.6 \times 0.99330562 + 500) \times 0.6427876$$
$$Z = (6343977.5 + 500) \times 0.6427876 = 4078756.2\ \text{m}$$

**Result:** $X = -1,266,785$ m, $Y = -4,728,780$ m, $Z = 4,078,756$ m

## Why ECEF Matters

- **The natural bridge** for [[Datum Transformation]] and satellite orbit mechanics.
- **Required input** to apply a [[Helmert Transformation]] (7-parameter similarity): convert geodetic → ECEF → transform → back to geodetic.
- **Output of [[GNSS]] precise processing** (PPP, network adjustment) before conversion to projected coordinates.
- **Used in satellite dynamics** (Keplerian orbital mechanics, GPS ephemeris computation).

## Datum Transformations in ECEF

The 7-parameter Helmert (similarity) transformation operates directly on ECEF coordinates:

$$\begin{pmatrix} X' \\ Y' \\ Z' \end{pmatrix} = \mathbf{T} + (1 + s)\mathbf{R} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}$$

where $\mathbf{T}$ = translation vector, $s$ = scale factor, $\mathbf{R}$ = rotation matrix.

## Accuracy Notes

- Consumer GNSS: meter-level ECEF
- RTK GNSS: cm-level ECEF
- IGS precise products: mm-level ECEF
- The ITRF ECEF coordinates of a point change ~2–3 cm/year due to plate tectonics.

## References
- Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS*. Springer.
- Bowring, B. R. (1976). *Transformation from spatial to geographical coordinates*. Survey Review.
- NGA (2014). *WGS84 Technical Report TR8350.2*.

## Related
- [[Geodetic Coordinates]] · [[Datum Transformation]] · [[Helmert Transformation]] · [[Local ENU NEU]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
