---
tags: [geodesy, concept, heights, aigis]
aliases: [Geoid Undulation, Undulasi Geoid, N, Geoid Height]
created: 2026-07-12
updated: 2026-07-27
---

# 🌊 Geoid Undulation (N)

**Geoid undulation** $N $ is the separation (distance along the ellipsoidal normal) between the [[Geoid]] (equipotential surface approximating mean sea level) and the [[Reference Ellipsoid]] at a given point. It is the critical conversion factor in the height relationship $h = H + N $.

## Global Values and Behavior

$ N $ varies globally by hundreds of meters:

| Region | Typical $ N $ (m) | Dominant Factor |
|--------|------------------|-----------------|
| North Atlantic | $-100 $ to $+10 $ | Low-density mantle beneath |
| Western Europe | $-40 $ to $-30 $ | Subducted slab effects |
| Indian Ocean | $-100 $ to $-15 $ | Mid-ocean ridge dynamics |
| Himalayas | $+50 $ to $+100 $ | Massive topography, deep root |
| Antarctica | $-60 $ to $-50 $ | Ice sheet mass + long-wavelength |
| New Zealand | $-30 $ to $+10 $ | Subduction + tectonics |

The undulation reflects the distribution of mass anomalies in the Earth's interior. Mountains create positive anomalies (mass excess), ocean trenches create negative anomalies.

## Models (Global Grid Files)

Each major model provides $ N $ on a global grid at specific resolution:

| Model | Year | Resolution | Max $ N $ Error | Grid Cell Size | Max Degree |
|-------|------|------------|---------------|----------------|------------|
| **EGM84** (GPM) | 1984 | 5′ × 5′ | ±2 m | ~5′ | N=30 |
| **EGM96** | 1996 | 2.5′ × 2.5′ | ±0.1 m (global) | ~2-Arcmin | N=360 |
| **EGM2008** (latest standard) | 2008 | 2.5′ × 2.5′ | ±0.07 m (global) | ~2-Arcmin | N=2190 |
| **GEOID18** (US only) | 2018 | 2′ × 2′ | ±0.04 m (contiguous US) | ~2′ | N=2160 |
| **GEOID18** | 2019 | 2′ × 2′ | ±0.03 m | ~2′ | N=2190 |
| **GEOID24** | 2024 | 30″ × 30″ | Under 5 cm (US) | 30″ | N=10080 |
| **G2022** | 2022 | 30″ | 1-2 cm (US) | 30″ | N=10080 |
| **GEOID12B** (US NOAA) | 2012 | 2′ × 2′ | ±0.05 m (US) | ~2′ | N=240 |

### EGM96 Details

EGM96 (Earth Gravity Model 1996) was developed from satellite altimetry, terrestrial gravity measurements, and satellite geodesy (GPS). It represents the gravitational potential using spherical harmonics up to degree and order $ N = 360 $:

$ $ V(r,\phi,\lambda) = \frac{GM}{r}\sum_{n=0}^{360}\sum_{m=0}^{n} \left(\frac{a}{r}\right)^n \left[C_{nm}\cos m\lambda + S_{nm}\sin m\lambda\right] P_{nm}(\cos\phi)$$- Grid spacing: 2.5 arcminutes

- File format: ASCII or binary grid (~14 MB)

- Publicly available from NGA (National Geospatial-Intelligence Agency)

- Accuracy: ±0.1 m over oceans, ±0.5 m over land (pre-EGM2008)

### EGM2008 Details

EGM2008 is the most widely used high-resolution global geoid model:

- Degree/order: N = 2190 (grid resolution improved by ~3× over EGM96)

- Gravity anomaly data: satellite-only (GOCE) + terrestrial + airborne + airborne altimetry

- Accuracy:
 - Global ocean (no data): ±0.10 m (1-sigma)
 - Global land (with gravity data): ±0.05 m
 - US (NGA GEOID models): ±0.03–0.04 m

- Grid: 2.5 arcminutes per cell

- File: Binary or ASCII format (~45 MB for the full grid)

## Computation Methods

### Bilinear Interpolation from Grid

The standard way to compute $ N(\phi, \lambda) $ at an arbitrary point:

1. Locate the four grid points surrounding $ (\phi, \lambda) $.
2. Use bilinear interpolation weights based on fractional distance.
3. $ N = N_{00}(1-t)(1-u) + N_{01}(1-t)u + N_{10}t(1-u) + N_{11}tu $ where $ t = (\phi - \phi_0)/\Delta\phi $ and $ u = (\lambda - \lambda_0)/\Delta\lambda $.

### Spherical Harmonic Synthesis

From the model coefficients and point coordinates:

$ $ N(\phi,\lambda) = \frac{1}{\gamma}\sum_{n=2}^{N_{max}}\sum_{m=0}^{n} \left(\frac{a}{r}\right)^n \left[C_{nm}\cos m\lambda + S_{nm}\sin m\lambda\right] P_{nm}(\cos\phi)$$

where $\gamma = GM/(a(1-f)) $ is normal gravity on the ellipsoid.

### Height Anomaly Approach

The **height anomaly**$\zeta $ (related to but not identical to undulation) can be computed from gravity data via $ $\zeta(\phi,\lambda) = \frac{1}{4\pi\gamma_0}\iint_\sigma \Delta g(\phi',\lambda') \, S(\psi) \, d\sigma'$$

Stokes' integral with the Stokes function $ S(\psi) $. In practice, this uses the Molodensky approach (computing the quasi-geoid from surface gravity anomalies).

## Relationship to Other Height Systems

$ $ h = H + NH = h - N $$

In regions with poor geoid models (oceans, deserts), EGM2008 gives $ N $ accurate to 10–100 m. This means:

- Over the ocean: $ N $ is accurate enough for oceanographic leveling but **not** for engineering.

- Over land with dense gravity data: $ N $ can be sub-meter.

- Over the USA with GEOID models: $ N $ is sub-centimeter accurate.

## Worked Example

**Problem:** A GNSS survey at a point gives ellipsoidal height $ h = 152.345 $ m. Using EGM2008, the geoid undulation at that point is $ N = 42.678 $ m. What is the orthometric height?

**Solution:**

$ $ H = h - N = 152.345 - 42.678 = 109.667\ \text{m}$$

This orthometric height is what you would use on a construction site or topographic map.

## References

- Pavlis, N. K., Holmes, S. A., Kenyon, S. C., & Factor, J. K. (2012). *The Development and Evaluation of the Earth Gravitational Model 2008 (EGM2008)*. J. Geophys. Res., 117, B04406.

- NOAA/NGS. *Geoid Models Overview* — www.ngs.noaa.gov/geoids

- NGA GEODAS: *EGM2008 Grid Download* — https://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008/egm08_w.html

## Related

- [[Geoid]] · [[Orthometric Height]] · [[Ellipsoidal Height]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
