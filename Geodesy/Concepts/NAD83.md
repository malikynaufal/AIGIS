---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [NAD83, North American Datum 1983, NAD83(2011)]
created: 2026-07-12
updated: 2026-07-27
---

# 📍 NAD83

**NAD83** (North American Datum 1983) is the modern horizontal [[Datum]] for North America, based on the [[GRS80]] ellipsoid from its inception but now effectively tied to [[ITRF]] through successive readjustments. It replaced [[NAD27]] across the United States, Canada, Mexico, and Central America.

## NAD83 Realizations

Unlike a single static datum, NAD83 has been updated multiple times:

| NAD83 Realization | Year | Ellipsoid | Relation to ITRF | Accuracy |
|-------------------|------|-----------|-------------------|----------|
| **NAD83(1986)** | 1986 | GRS80 | ≈ITRF89, but not explicitly tied | ±1–2 m |
| **NAD93(CORS)** | 1993 | GRS80 | ≈ITRF92 at epoch 1993.0 | ±0.01 m |
| **NAD83(HARN)** — 50 state readjustments | 1990–1999 | GRS80 | ≈ITRF94/97 per region | ±0.05 m |
| **NAD83(NSRS2007)** | 2007 | GRS80 | ≈ITRF2000 at epoch 2005.0 | ±0.01 m |
| **NAD83(2011)** | 2011 | GRS80 | ≈ITRF2008 at epoch 2010.0 | ±0.01 m |
| **NATRF2022** | 2022 (+ CORS) | GRS80 | ITRF2020 + plate model | ±0.01 m |

### NAD83(2011) — Current Standard in the US

- **Epoch:** 2010.0

- **Realization:** Positions/velocities from CORS network aligned to ITRF2008 via 14-parameter transformation.

- **CORS used:** ~1500 (including IGS stations)

- **Velocity model:** "HT_DH" (plate motion + post-glacial rebound + coasts)

- **Accuracy:** 0.01–0.03 m relative within network; < 0.1 m absolute vs WGS84 in CONUS.

### NAD83 HARN (High Accuracy Reference Network)

- **Dates:** 1990–1999, phased by state

- **Method:** Readjustment of all FGCS stations in a state using GPS baselines

- **Accuracy:** 0.01–0.05 m

- **Still used:** Many state DOTs still contract in NAD83(HARN) for legacy data

## Relationship to ITRF

NAD83 and ITRF diverge because NAD83 is fixed to the North American plate (≈WGS84-like global can't account for plate motion):

| Frame | Underlying origin plate motion | Relative Drift Rate (CONUS) |
|-------|-------------------------------|---------------------------|
| ITRF2020 | Global, no net plate rotation | 0 mm/yr (reference) |
| WGS84(G2139) | Tied to ITRF2014 | < 5 mm/yr |
| **NAD83(2011)** | Fixed to North American plate | **~3–4 cm/yr West** |

**Key consequence:** A point with NAD83(2011) coordinates in 2010 differs from the same point's ITRF2020 coordinates by up to 1.5 m in 2030 because NAD83 does NOT account for the ~3 cm/year drift of North America in ITRF.

### Transformation: NAD83(2011) ↔ ITRF2008

At epoch $t $:

$ $\mathbf{X}_{ITRF2008}(t) = \mathbf{T}(t) + (1+s)\,\mathbf{R}(t)\,\mathbf{X}_{NAD83}(t)

$$| Parameter | $ T_x $ | $ T_y $ | $ T_z $ | $  s $ | $ R_x $ | $ R_y $ | $ R_z $ |
|-----------|-------|-------|-------|-----|-------|-------|-------|
| Translation (m) | −0.993 | 1.907 | −0.514 | — | — | — | — |
| Scale (ppb) | — | — | — | 0.809 | — | — | — |
| Rotation (mas) | — | — | — | — | 25.677 | 8.412 | 11.331 |
| Rate (m/yr) | −0.001 | −0.001 | 0.003 | 0.000 | −0.07 | −0.05 | −0.02 |

Note: These parameters change over time (14-parameter model).

## NAD83 vs. WGS84

| Property | NAD83(2011) | WGS84(G2139) |
|----------|-------------|---------------|
| Ellipsoid | GRS80 | WGS84 (nearly same) |
| Origin | Geocentric (≈ITRF2008) | Geocentric (≈ITRF2014) |
| Plate | Fixed to North America | Fixed to global no-rotation |
| Max coordinate diff in CONUS | — | ~1.5 m (growing ~3 cm/yr) |
| Natural context | Mapping, civil engineering | Navigation, global |

## Conversion: NAD27 → NAD83

Converting from [[NAD27]] to NAD83 is not a simple 7-parameter Helmert. The recommended approach is:

### Grid-Based Transformation (US)

**NADCON** (National Ocean Service, NOAA):

- Input: NAD27 $ (\phi, \lambda) $- Output: NAD83 $ (\phi, \lambda) $- Method: Bilinear interpolation in a 30″ × 30″ grid of shift values

- Accuracy: ±0.15 m (CONUS), ±0.5 m (Alaska)

### Grid-Based Transformation (Canada)

**NTv2** (Natural Resources Canada):

- Input: NAD27 $ (\phi, \lambda) $- Output: NAD83 $ (\phi, \lambda) $- Grid resolution: 1′ × 1′

- Accuracy: ±0.10 m (southern Canada), ±0.50 m (northern)

### Approximate Helmert (NAD27→NAD83)

For quick checks only (±10 m accuracy):

$ $ T_x \approx −6\ \text{m}, T_y \approx 158\ \text{m}, T_z \approx −176\ \text{m}$$

# # Usage and EPSG Codes

| EPSG Code | Description |
|-----------|-------------|
| **4269** | NAD83 (lat/lon) |
| **4344** | NAD83 (lat/lon) — deprecated? |
| **6318** | NAD83(2011) (lat/lon) |
| **6325** | NAD83(HARN) |
| **6320** | NAD83(NSRS2007) |
| **26901–26922** | NAD83 / UTM zones (10–60N) |
| **32100–32161** | NAD83 / State Plane zones |
| **4911–4913** | NAD83 / ECEF (X/Y/Z) |

## References

- Schwarz, C. R. (1989). *North American Datum of 1983*. NOAA Professional Paper 2.

- Soler, T. & Marshall, J. (2003). *A note on the relationship between NAD83 and ITRF2000*. J. Surveying Eng., 129(4).

- NGS. *NAD83(2011) Realization*. www.ngs.noaa.gov/NAD83/

- NGS. *Geodesy Tool Platform: www.ngs.noaa.gov

## Related

- [[Datum]] · [[GRS80]] · [[NAD27]] · [[Horizontal Datum]] · [[ITRF]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
