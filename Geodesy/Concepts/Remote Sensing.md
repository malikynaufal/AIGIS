---
tags: [aigis, concept, geodesy, remote-sensing, satellite-imaging, spectral-analysis]
aliases: [Remote Sensing, Penginderaan Jauh]
created: 2026-07-27
updated: 2026-07-27
---

# Remote Sensing

## Overview

**Remote sensing** (Penginderaan Jauh) is the acquisition of information about the Earth's surface without physical contact, using sensors on satellites, aircraft, or UAVs. It covers both **passive** (solar-reflective) and **active** (radar/LiDAR) systems. In geodesy, remote sensing provides data for land cover mapping, environmental monitoring, and deformation analysis via [[InSAR]].

## Electromagnetic Spectrum

| Region | Wavelength | Frequency | Sensor Type | Application |
|--------|------------|-----------|-------------|-------------|
| Ultraviolet | 0.01–0.38 μm | 8e14–3e15 Hz | UV sensor | Atmosphere |
| Visible blue | 0.45–0.52 μm | 5.8–6.7e14 Hz | Optical | Water quality |
| Visible green | 0.52–0.60 μm | 5.0–5.8e14 Hz | Optical | Vegetation |
| Visible red | 0.63–0.69 μm | 4.3–4.8e14 Hz | Optical | Vegetation |
| Near infrared | 0.76–0.90 μm | 3.3–3.9e14 Hz | Optical | Vegetation stress |
| Shortwave IR | 1.55–2.35 μm | 1.3–1.9e14 Hz | Optical | Minerals, moisture |
| Thermal IR | 3.7–14 μm | 2.1–8.1e13 Hz | Thermal | Heat mapping |
| Microwave | 1 mm–1 m | 300 MHz–300 GHz | Radar (SAR) | All-weather |

## Spectral Indices

### NDVI — Normalized Difference Vegetation Index
$$NDVI = \frac{NIR - Red}{NIR + Red}$ $| NDVI Value | Land Cover |
|------------|------------|
| < 0.1 | Water, bare soil |
| 0.1–0.3 | Sparse vegetation |
| 0.3–0.5 | Moderate vegetation |
| 0.5–0.7 | Dense vegetation |
| > 0.7 | Very dense (forest) |

### NDWI — Normalized Difference Water Index
$$NDWI = \frac{Green - NIR}{Green + NIR}$ $### Other Indices

| Index | Formula | Use |
|-------|---------|-----|
| SAVI | $\frac{NIR-Red}{NIR+Red+L}(1+L)$, $L=0.5$ | Soil-adjusted vegetation |
| MNDWI | $\frac{Green-SWIR}{Green+SWIR}$| Modified water index |
| BSI | $\frac{(SWIR+Red)-(NIR+Blue)}{(SWIR+Red)+(NIR+Blue)} $ | Bare soil index |

## Sensor Platforms

### Satellite Sensors

| Sensor | Resolution (m) | Bands | Revisit | Provider |
|--------|----------------|-------|---------|----------|
| Sentinel-2 | 10–60 | 13 | 5 days | ESA |
| Landsat 8/9 | 15–100 | 11 | 16 days | NASA/USGS |
| WorldView-3 | 0.31 (pan) | 29 | 1–3 days | Maxar |
| ALOS-2 PALSAR | 1–100 | L-band | 14 days | JAXA |
| SPOT-7 | 1.5 (pan) | 5 | 1 day | Airbus |
| Planet Labs | 3–5 | 4 | Daily | Planet |

### Platform Comparison

| Platform | Altitude | Resolution | Coverage | Cost |
|----------|----------|------------|----------|------|
| Satellite | 400–800 km | 0.3–30 m | Continental | Low per km² |
| Manned aircraft | 1–10 km | 0.05–1 m | Regional | Medium |
| UAV/drone | 50–300 m | 1–10 cm | Local | Low |
| Kite balloon | 5–50 m | 1–5 cm | Very local | Very low |

## Active Remote Sensing

### SAR (Synthetic Aperture Radar)$ $\text{Resolution}_{range} = \frac{c}{2B} = \frac{c}{2f_{chirp}}
$$
$ $\text{Resolution}_{azimuth} = \frac{D_{antenna}}{2}
$$
| SAR Band | Wavelength | Penetration | Use |
|----------|------------|-------------|-----|
| X-band | 3 cm | Vegetation canopy | Urban, snow |
| C-band | 5 cm | Light vegetation | General, [[Crustal Deformation#InSAR|InSAR]] |
| L-band | 23 cm | Dense vegetation | Forest, agriculture |
| P-band | 70 cm | Full canopy | Subsurface |

### LiDAR (Light Detection and Ranging)$ $\text{Range} = \frac{c \cdot \Delta t}{2}
$$
| LiDAR Type | Range | Points/sec | Application |
|------------|-------|------------|-------------|
| Airborne | 500–3000 m | 100k–2M | Topographic mapping |
| Terrestrial | 1–300 m | 100k–2M | [[Survei Rekayasa|Engineering survey]] |
| UAV-mounted | 10–500 m | 50k–500k | Local mapping |
| Bathymetric | 0–50 m | 10k–100k | [[Survei Hidrografi|Hydrographic survey]] |

## In [[Geodesy]] Context

### Indonesian Applications
- **Land cover mapping:** KLHK (Ministry of Forestry) uses Sentinel-2
- **Deforestation monitoring:** Destructive logging detection
- **Urban expansion:** Jakarta land subsidence monitoring
- **Cadastral mapping:** UAV photogrammetry for land parcels
- **Disaster response:** Earthquake/tsunami damage assessment
- **Coastal monitoring:** [[Pengelolaan Wilayah Pesisir|Shoreline change analysis]]

### [[Penginderaan Jauh Terapan|Applied Remote Sensing]] in Indonesia
- PALAPA-1 satellite program
- LAPAN-BRIN constellation
- InSAR deformation studies (Lembaga Aeronautika dan Antariksa Nasional)

## Study Problems

1. Compute NDVI given $NIR = 0.35$ and $Red = 0.08$.
2. Explain the difference between multispectral and hyperspectral sensors.
3. Why is L-band SAR better than X-band for forest monitoring?
4. Calculate the range resolution of a SAR with bandwidth 150 MHz.

## Related Concepts

- [[Penginderaan Jauh Sensor Aktif|Active Sensors (SAR)]]
- [[Penginderaan Jauh Terapan|Applied Remote Sensing]]
- [[Analisis Citra Penginderaan Jauh|Image Analysis]]
- [[Model Terrain Digital|DEM from remote sensing]]
- [[SIG]] — GIS for remote sensing data
- [[Crustal Deformation]] — InSAR applications
- [[Photogrammetry]] — Related discipline

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
