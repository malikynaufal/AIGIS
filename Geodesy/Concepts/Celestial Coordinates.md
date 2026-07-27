---
tags: [aigis, concept, geodesy, celestial-coordinates, astronomy, coordinate-systems]
aliases: [Celestial Coordinates, Astronomical Coordinates]
created: 2026-07-27
updated: 2026-07-27
---

# Celestial Coordinates

## Overview

**Celestial coordinates** describe positions on the celestial sphere as seen from Earth. They form the basis of [[Geodetic Astronomy]], which uses stellar observations to determine precise directions and positions. Celestial coordinates connect to terrestrial coordinates through [[Precession and Nutation]] and Earth rotation models.

## Celestial Coordinate Systems

### Equatorial System

| Quantity | Symbol | Range | Reference |
|----------|--------|-------|-----------|
| Right Ascension | $\alpha$ | 0°–360° (or 0h–24h) | Vernal equinox |
| Declination | $\delta$| -90° to +90° | Celestial equator |$ $x = r \cos\delta \cos\alpha, \quad y = r \cos\delta \sin\alpha, \quad z = r \sin\delta $$# ## Horizontal System (Observer-Local)

| Quantity | Symbol | Range | Reference |
|----------|--------|-------|-----------|
| Azimuth | $A$ | 0°–360° | North, clockwise |
| Altitude | $h$ | -90° to +90° | Horizon |
| Zenith angle | $z$| 0°–180° | Zenith |$ $h = 90° - z, \quad A = \arctan\left(\frac{\sin\alpha}{\cos\alpha \sin\varphi - \tan\delta \cos\varphi}\right) $ $### Conversion: Equatorial ↔ Horizontal$ $ \sin h = \sin\varphi \sin\delta + \cos\varphi \cos\delta \cos H
$$
$ $\cos A \sin h = \cos\delta \sin H$$
$ $\sin A \sin h = \cos\varphi \sin\delta - \sin\varphi \cos\delta \cos H
$$where$ H = \theta - \alpha $ is the [[Geodetic Astronomy|hour angle]], and $\theta$ is Greenwich Apparent Sidereal Time.

## Epoch Transformations

### Precession (J2000.0 → Epoch)

The precession matrix $P$ transforms from J2000.0 equatorial to mean equator at epoch $t$:$$
\begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} = P \begin{pmatrix} x \\ y \\ z \end{pmatrix}_{J2000}
$$
# ## Nutation (Mean → True Equator)

The nutation matrix $N$ accounts for short-period oscillations:$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}_{true} = N \cdot P \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix}_{J2000}
$$
See [[Precession and Nutation]] for detailed formulas.

## Star Catalogs

| Catalog | Epoch | Stars | Accuracy |
|---------|-------|-------|----------|
| Hipparcos | J1991.25 | 118,000 | ~1 mas |
| Tycho-2 | J1991.5 | 2,539,951 | ~25 mas |
| Gaia DR3 | J2016.0 | ~1.8 billion | ~10 μas |

## In [[Geodesy]] Context

### Geodetic Astronomy Applications
- **Azimuth determination:** Measure azimuth to stars for [[Jaring Kontrol Geodesi|control networks]]
- **Deflection of the vertical:** Compare astronomical and geodetic coordinates
- **Latitude/longitude:** Classical method before [[GPS]]

### Azimuth from Stellar Observations$ $\alpha_{az} = \sum_{i=1}^{N} w_i \cdot \alpha_{i,obs}
$$where$ w_i $ weights each observation by altitude, zenith distance, and atmospheric conditions.

## Study Problems

1. Convert star coordinates $(\alpha, \delta) = (6h, 23°)$ to local $(A, h)$ for an observer at $\varphi = -7°$ at LST = 10h.
2. Compute the hour angle for a star with $\alpha = 15h$ when GST = 20h.
3. Explain the difference between precession and nutation.

## Related Concepts

- [[Geodetic Astronomy]] — Practical applications
- [[Precession and Nutation]] — Earth orientation models
- [[Time Systems]] — Time-dependent coordinates
- [[Celestial Coordinates#Geodetic Astronomy|Deflection of the Vertical]]
- [[Gravity Field]] — Related to vertical
- [[ITRF]] — Terrestrial counterpart

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
