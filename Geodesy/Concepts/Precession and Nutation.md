---
tags: [aigis, concept, geodesy, precession, nutation, earth-orientation, astronomy]
aliases: [Precession and Nutation, Earth Orientation]
created: 2026-07-27
updated: 2026-07-27
---

# Precession and Nutation

## Overview

**Precession** and **nutation** describe the long-term rotation and short-period oscillation of Earth's rotational axis in space. They define how the celestial coordinate system changes over time, which is critical for [[Geodetic Astronomy|geodetic astronomy]], GNSS satellite ephemeris computation, and precise coordinate transformations.

## Precession

Precession is the slow (~26,000-year) circular motion of Earth's rotational axis around the ecliptic pole due to gravitational torques from the Sun and Moon on Earth's equatorial bulge.

### Main Parameters

| Parameter | Rate | Period |
|-----------|------|--------|
| General precession in longitude | $\psi \approx 50.26"$ /yr | ~25,772 years |
| Obliquity of ecliptic | $\varepsilon \approx 23.44°$ | 41,000-year oscillation |
| Axial tilt change | $d\varepsilon/dt \approx -0.0047"$ /yr | — |

### Precession Matrix

The precession matrix $P$ transforms from the mean equator of date to the mean equator of J2000.0:$ $P = R_3(\zeta_A) \cdot R_2(\theta_A) \cdot R_3(-z_A)$\$$where:$ $\zeta_A = 2.5976176" + 0.0028469"t + 0.0000050"t^2
$$
$ $\theta_A = 20.043109" - 0.0085330"t - 0.0000934"t^2
$$
$ $ z_A = -2.5976176" + 0.0028469"t + 0.0000050"t^2
$$
$ $t = (JD_{date} - 2451545.0) / 36525 \quad \text{(Julian centuries from J2000.0)}
$$# ## Rotation Matrices$ $ R_3(\alpha) = \begin{pmatrix} \cos\alpha & \sin\alpha & 0 \\ -\sin\alpha & \cos\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
$ $ R_2(\alpha) = \begin{pmatrix} \cos\alpha & 0 & \sin\alpha \\ 0 & 1 & 0 \\ -\sin\alpha & 0 & \cos\alpha \end{pmatrix}
$$
# # Nutation

Nutation is the short-period wobble of Earth's axis superimposed on precession, caused by periodic changes in the Sun-Moon-Earth geometry (lunar nodal cycle: 18.6 years, solar semi-annual: 6 months).

### Nutation Parameters

| Parameter | Symbol | Value | Period |
|-----------|--------|-------|--------|
| Obliquity nutation | $\Delta\varepsilon$|$\pm 9.21"$| 18.6 years |
| Longitude nutation |$\Delta\psi $|$\pm 17.23"$ | 18.6 years |
| IAU 2000A terms | — | 678 terms | Various |

### Nutation Matrix$ $N = R_1(-\varepsilon_0) \cdot R_3(\Delta\psi) \cdot R_1(+\varepsilon_0 + \Delta\varepsilon)$\$$where $ \varepsilon_0 $ is the mean obliquity of the ecliptic.

### IAU 2000A Fundamental Arguments

| Argument | Period | Value at J2000.0 |
|----------|--------|-------------------|
| Mean anomaly of Sun $M$ | 1 yr | 357.51716° |
| Mean anomaly of Moon $M'$ | 27.32 days | 134.96340° |
| Argument of latitude $F$ | 27.32 days | 93.27209° |
| Elongation of Moon $D$ | 27.32 days | 297.85020° |
| Longitude of ascending node $\Omega$ | 18.6 years | 125.04452° |

## Combined: Precession-Nutation (IAU 2000A)$\$ $\mathbf{r}_{true} = N \cdot P \cdot \mathbf{r}_{J2000.0}
$$
$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}_{true} = N \cdot P \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix}_{J2000.0}
$$
# # Earth Rotation and EOP

| Parameter | Symbol | Range | IERS Publication |
|-----------|--------|-------|------------------|
| UT1-UTC | ΔUT1 | ±0.9 s | Bulletin A |
| Polar motion | $\(x_p, y_p)$\$ | ±0.4" | Bulletin A |
| Nutation corrections | $\Delta\varepsilon, \Delta\psi$ | ±0.01" | Bulletin B |
| LOD (Length of Day) | LOD | 86164 ± 0.001 s | Bulletin A |

### Polar Motion$ $x_{ITRF} = x_p + \text{tidal terms}$$
$ $y_{ITRF} = -y_p + \text{tidal terms}$$
# # In [[Geodesy]] Context

### Applications

| Application | Which Component | Required Accuracy |
|-------------|-----------------|-------------------|
| [[Geodetic Astronomy]] | Precession + nutation | ~0.01" |
| GNSS orbit computation | Precession + nutation | ~1 mas |
| [[ITRF]] transformation | All EOP | ~1 mm |
| [[Celestial Coordinates]] | Precession + nutation | ~1" |

### Julian Date Calculation$ $JD = 2451545.0 + 367Y - \text{int}(7(Y + \text{int}((M+9)/12))/4) + \text{int}(275M/9) + D + 1721013.5
$$
# # Study Problems

1. Compute the number of Julian centuries from J2000.0 for 2026-01-01.
2. Why does precession have a 26,000-year period?
3. Explain why IAU 2000A replaced the earlier IAU 1976 precession model.
4. Compute the precession matrix for 2026-07-01.

## Common Mistakes

1. **Ignoring precession in long-baseline surveys** — > 50 arcsec error over centuries
2. **Confusing precession with nutation** — precession is secular; nutation is periodic
3. **Using IAU 1976 instead of IAU 2000A** — IAU 2000A is 10× more accurate

## Related Concepts

- [[Celestial Coordinates]] — Uses precession-nutation
- [[Geodetic Astronomy]] — Application of EOP
- [[Time Systems]] — UT1 and Earth rotation
- [[ITRF]] — Terrestrial reference frame
- [[IERS]] — Publishes EOP data
- [[IGS]] — Determines GNSS orbits

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
