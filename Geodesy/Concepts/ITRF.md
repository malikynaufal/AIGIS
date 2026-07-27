---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [ITRF, International Terrestrial Reference Frame, ITRF2014, ITRF2020]
created: 2026-07-12
updated: 2026-07-27
---

# 🌐 ITRF

**ITRF** (International Terrestrial Reference Frame) is the high-precision global reference frame maintained by the [[IERS]]. Each ITRF realization (e.g., ITRF2008, ITRF2014, ITRF2020) provides coordinates and velocities for a global network of ~1000 stations measured by the four space-geodetic techniques: VLBI, SLR, GNSS, and DORIS.

## ITRF Characteristics

| Property | Definition |
|----------|------------|
| **Origin** | Earth's center of mass (geocenter), as sampled by SLR and GNSS |
| **Scale** | Defined by SLR + VLBI, consistent with geophysical models |
| **Orientation** | No-net rotation (NNR) with respect to horizontal tectonic plate motion |
| **Time dependence** | Stations have positions + velocities (linear or piecewise) |

## Realizations Over Time

Every ~5 years a new realization replaces its predecessor, improving station coordinates and expanding the network:

| ITRF | Publication Year | Stations | Epoch | Accuracy (mm) |
|------|-----------------|----------|-------|---------------|
| **ITRF88** | 1989 | ~200 | 1988.0 | ~100 mm |
| **ITRF89** | 1990 | ~300 | 1988.0 | ~50 mm |
| **ITRF90** | 1991 | ~400 | 1988.0 | ~20 mm |
| **ITRF91** | 1992 | ~500 | 1988.0 | ~10 mm |
| **ITRF92** | 1993 | ~600 | 1988.0 | ~5 mm |
| **ITRF93** | 1993 | ~600 | 1993.0 | ~5 mm |
| **ITRF94** | 1995 | ~600 | 1993.0 | ~3 mm |
| **ITRF96** | 1997 | ~600 | 1996.0 | ~3 mm |
| **ITRF97** | 1998 | ~600 | 1997.0 | ~2 mm |
| **ITRF2000** | 2001 | ~750 | 1997.0 | 1–2 mm |
| **ITRF2005** | 2007 | ~850 | 2000.0 | < 1 mm |
| **ITRF2008** | 2011 | ~950 | 2005.0 | < 1 mm |
| **ITRF2014** | 2016 | ~1000 | 2010.0 | ~0.5 mm |
| **ITRF2020** | 2022 | ~1200 | 2015.0 | ~0.3 mm |

## Realization Details for ITRF2020

| Component | Value |
|-----------|-------|
| **Epoch** | 2015.0 (reference) |
| **Stations** | ~1200 stations, including ~150 core stations with VLBI/SLR/GNSS/DORIS |
| **Techniques** | GNSS (~600), SLR (~100), VLBI (~200), DORIS (~100) |
| **Combination** | Daily time series → weekly → semiannual → final ITRF |
| **Time span** | Data 2000–2020 |
| **Mean repeatability** | < 1 mm horizontal, < 2 mm vertical |

### ITRF2020 Station Velocity Models

ITRF2020 includes a **post-seismic deformation (PSD)** model for stations affected by major earthquakes. Stations affected by large earthquakes (Sumatra 2004, Japan 2011, Chile 2010, etc.) have time-dependent rather than linear velocities.

## Transformation Between Realizations

Moving between ITRF realizations uses a **14-parameter Helmert transformation** (translation, rotation, scale, plus their time derivatives) valid at a given epoch:
$$

\mathbf{X}_{ITRF_{new}} = \mathbf{T}(t) + (1+s(t))\,\mathbf{R}(t)\,\mathbf{X}_{ITRF_{old}}$$where:
-$\mathbf{T}(t) = \mathbf{T}_0 + \dot{\mathbf{T}}\cdot(t - t_0)$-$\mathbf{R}(t) = \mathbf{R}_0 + \dot{\mathbf{R}}\cdot(t - t_0)$-$s(t) = s_0 + \dot{s}\cdot(t - t_0)$### Transformation: ITRF2014 → ITRF2020 (at epoch 2015.0)

| Parameter | Value | Unit |
|-----------|-------|------|
|$T_x$| 1.4 ± 0.3 | mm |
|$T_y$| −1.3 ± 0.3 | mm |
|$T_z$| −1.5 ± 0.3 | mm |
|$s$| −0.21 ± 0.06 | ppb (≈ −1.3 ± 0.4 mm) |
|$R_x$| 0.41 ± 0.10 | µas (mas in origin?) |
|$R_y$| −1.25 ± 0.10 | µas |
|$R_z$| −0.37 ± 0.10 | µas |
|$\dot{T}_x$| −0.3 ± 0.3 | mm/yr |
|$\dot{T}_y$| −0.3 ± 0.3 | mm/yr |
|$\dot{T}_z$| 0.2 ± 0.3 | mm/yr |
|$\dot{s}$ | 0.1 ± 0.1 | ppb/yr |

## Combination Methodology

The ITRF combination uses a rigorous least-squares approach:

1. **Technique-specific solutions** are computed independently by each analysis center:
   - **VLBI**: ITRF scale + Earth rotation (UT1, nutation)
   - **SLR**: ITRF origin + scale (centroid of SLR network)
   - **GNSS**: Dense global coverage, relative frame tie
   - **DORIS**: Global coverage, polar motion tie

2. **Daily time series** from all techniques are collected (~15 years for ITRF2020).

3. **Ties at co-located sites** (stations where multiple techniques operate) provide the constraints linking the techniques.

4. **Least-squares combination** solves for positions + velocities + Helmert transformation parameters between techniques.

### Colocation Sites

A key challenge: only ~40 stations globally have 2+ techniques. This limits the accuracy of frame ties. The ITRF2020 identified 175 colocation sites:

| Colocation | Number of Sites |
|------------|-----------------|
| VLBI + SLR | ~15 |
| VLBI + GNSS | ~60 |
| SLR + GNSS | ~40 |
| DORIS + GNSS | ~25 |
| VLBI + SLR + GNSS | ~10 |

## Relationship to Other Systems

| System | Relationship to ITRF |
|--------|---------------------|
| **WGS84 (G1762)** | Aligned to ITRF2008 at cm level |
| **WGS84 (G2139)** | Aligned to ITRF2014 at mm level |
| **ETRS89** | Fixed to ITRF1989.0, then rotated with Eurasian plate |
| **NAD83** | Realized through ITRF2008 + plate model |
| **NAD83(2011)** | Tied to ITRF2008 at epoch 2010.0 |
| **NATRF2022** | Tied to ITRF2020 |

## References

- Altamimi, Z., Rebischung, P., Métivier, L., & Collilieux, X. (2016). *ITRF2014: A new release of the International Terrestrial Reference Frame modeling nonlinear station motions*. J. Geophys. Res. Solid Earth, 121(8), 6109–6131.

- Petit, G. & Luzum, B. (2010). *IERS Conventions (2010)*. IERS TN 36.

- Altamimi, Z. (2003). *ITRF combination*. Adv. Space Res., 31(8), 1781–1792.

## Related

- [[IERS]] · [[Helmert Transformation]] · [[WGS84]] · [[ETRS89]] · [[NAD83]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]]
