---
tags: [aigis, concept, geodesy, utm, map-projection, transverse-mercator]
aliases: [Universal Transverse Mercator]
created: 2026-07-27
updated: 2026-07-27
---

# UTM — Universal Transverse Mercator

## Overview

**UTM** (Universal Transverse Mercator) is a conformal [[Map Projection]] system that divides the world into 60 zones of $6°$ longitude each, with a central meridian for each zone. It uses the [[Transverse Mercator]] projection with two standard parallels at $\pm 80°$ latitude. UTM is the primary coordinate system for topographic mapping worldwide, including Indonesia's Rupabumi map series.

## Zone Structure

| Property | Value |
|----------|-------|
| Number of zones | 60 (001°E to 360°E) |
| Zone width | $6°$ longitude |
| Central meridian |$\lambda_0 = 6°(Z - 1) - 180° + 3°$for zone$Z$ |
| Latitude bands | C to X (80°S to 84°N) |
| False easting | 500 000 m (at central meridian) |
| False northing | 0 m (equator) for northern hemisphere; 10 000 000 m for southern |
| Scale factor at CM | $k_0 = 0.9996$ |
| Latitude of origin | Equator (0°) |

## Zone Numbering

The zone number $Z$ is computed as:$ $Z = \text{floor}\left(\frac{\lambda + 180°}{6°}\right) + 1 $$# ## Indonesia's UTM Zones

| Zone | Longitude Range | Central Meridian | Region |
|------|----------------|-------------------|--------|
| 46 | 84°E – 90°E | 87°E | Western Sumatra |
| 47 | 90°E – 96°E | 93°E | Central Sumatra |
| 48 | 96°E – 102°E | 99°E | Eastern Sumatra, Jakarta |
| 49 | 102°E – 108°E | 105°E | West Java, Bali |
| 50 | 108°E – 114°E | 111°E | East Java, Lombok |
| 51 | 114°E – 120°E | 117°E | Kalimantan, Sulawesi |
| 52 | 120°E – 126°E | 123°E | Maluku, Papua (west) |
| 53 | 126°E – 132°E | 129°E | Papua (east) |
| 54 | 132°E – 138°E | 135°E | Papua (far east) |

## Forward Projection Formulas

Given geodetic coordinates $\(\varphi, \lambda)$\$ on [[WGS84]]:$ $n = \frac{a - b}{a + b} = \frac{f}{2 - f}$$$ $A = \frac{a}{1+n}\left(1 + n^2/4 + n^4/64 + \ldots\right)$\$$$ $t = \sinh(\tanh^{-1}(\sin\varphi)) - 2n\cdot\text{atanh}(n\sin\varphi)$\$$$ $ \lambda' = \lambda - \lambda_0 \quad \text{(reduced longitude)}
$$
$ $\xi' = \frac{1}{2}\ln\frac{1+t}{1-t} \quad \text{(isometric latitude)}
$$
$ $x = A \cdot \ln\frac{1+\sin\xi'\cos\lambda'}{1-\sin\xi'\cos\lambda'} \quad \text{(meridional arc)}$$The final UTM coordinates:$ $E = k_0 \cdot N(\varphi) \cdot \cos\varphi \cdot \lambda' + \ldots + 500\,000 \text{ m}$$$ $N = k_0 \cdot \text{meridional arc} + 0 \text{ m (northern hemisphere)}$$# ## Simplified Transverse Mercator Series

For direct computation (Bowring & Romer):$ $E = E_0 + k_0 N \cos\varphi \left[\lambda' + \frac{(1-T+C)\lambda'^3}{6} + \frac{(5-18T+T^2+72C-58e'^2)\lambda'^5}{120} + \ldots\right]$$$ $N = N_0 + k_0 \left[M(\varphi) - M(\varphi_0) + N\tan\varphi\left(\frac{\lambda'^2}{2} + \frac{(5-T+9C+4C^2)\lambda'^4}{24} + \frac{(61-58T+T^2+600C-330e'^2)\lambda'^6}{720}\right)\right]$$where:
-$T = \tan^2\varphi $-$ C = e'^2\cos^2\varphi = \frac{e^2}{1-e^2}\cos^2\varphi $-$ N = a/\sqrt{1-e^2\sin^2\varphi} $\([[GRS80#Radius of Curvature|prime vertical radius]])
- $E_0 = 500\,000$ m

## Scale Factor

The scale factor of UTM at the central meridian is:$ $k_0 = 0.9996$$This means distances on the map are$0.04\%$ shorter than true distances at the CM. At the zone boundaries ( $3°$ from CM):$ $k_{boundary} \approx 1.0004$ $**True scale line** occurs where$ k = 1.0000 $, at approximately$ \pm 1°56'$ from the CM.

## Distortion Analysis

| Distance from CM | Scale Factor | Distortion |
|-------------------|-------------|------------|
| 0° (CM) | 0.99960 | -40 cm/km |
| 1° | 0.99969 | -31 cm/km |
| 2° | 0.99990 | -10 cm/km |
| 2.5° | 1.00000 | 0 (true scale) |
| 3° (boundary) | 1.00040 | +40 cm/km |

### Maximum Angular Distortion
UTM preserves angles (conformal) but has scale distortion. Maximum scale error is about $0.04\%$ at the central meridian.

## In [[Geodesy]] Context

### UTM Zone Overlap
Indonesia spans zones 46–54. For surveys spanning zone boundaries:$ $ E_{zoneB} = (E_{zoneA} - 500\,000) \times \frac{k_{CM_A}}{k_{CM_B}} + 500\,000 $$# ## Indonesia's National Mapping (Rupabumi)
- Uses UTM on [[WGS84]]
- Sheet scales: 1:25,000, 1:50,000, 1:100,000, 1:250,000
- Grid ticks every 1 km (on 1:25,000)
- Printed on the Transverse Mercator projection

### Practical Conventions
| Convention | Value | Purpose |
|------------|-------|---------|
| False Easting | 500 000 m | Avoid negative coordinates |
| False Northing (S) | 10 000 000 m | Distinguish from N hemisphere |
| Scale factor | 0.9996 | Minimize zone-width distortion |
| CM spacing | $6°$ | Balance between accuracy and zone count |

## Study Problems

1. Determine the UTM zone for Yogyakarta ( $\varphi = -7.8°$, $\lambda = 110.4°$).
2. Calculate the scale factor at$2°$ from the central meridian.
3. Convert UTM coordinates $\(E, N) = (567\,000, 9\,123\,456)$\$ to geographic.
4. Explain why UTM uses $k_0 = 0.9996$ instead of $k_0 = 1.0$.

## Related Concepts

- [[Transverse Mercator]] — Underlying projection
- [[Map Projection]] — Broader category
- [[Mercator]] — Similar but cylindrical (not transverse)
- [[Projected Coordinates]] — $\(E, N)$\$ on any projection
- [[WGS84]] — Reference ellipsoid
- [[UTM#Indonesia|Indonesia]] — National mapping standard
- [[GRS80]] — Ellipsoid used

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
