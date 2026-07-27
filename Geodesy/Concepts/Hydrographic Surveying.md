---
tags: [aigis, concept, geodesy, hydrographic-survey, bathymetry, marine, sounding]
aliases: [Hydrographic Surveying, Survei Hidrografi, Bathymetric Survey]
created: 2026-07-27
updated: 2026-07-27
---

# Hydrographic Surveying

## Overview

**Hydrographic surveying** (Survei Hidrografi) measures and describes the physical features of water bodies — ocean floors, coastlines, and water levels. It supports nautical charting, port engineering, offshore resource exploration, and environmental monitoring. In Indonesia, hydrographic surveys are conducted by Bakosurtanal (BIG), TNI-AL (Navy), and private survey companies.

## Measurement Technologies

### Single-Beam Echo Sounder (SBES)

$$ d = \frac{c \cdot t}{2}$ $

where $ c $ = sound velocity in water ($\approx 1500 $ m/s),$ t $ = two-way travel time.

### Multi-Beam Echo Sounder (MBES)

| Parameter | Value |
|-----------|-------|
| Swath width | 120°–190° |
| Beams | 128–512 |
| Resolution | 1°–2° beam width |
| Frequency | 200 kHz–400 kHz |
| Depth range | 0.5–6000 m |

### Side-Scan Sonar (SSS)

$ $\text{Range} = \frac{c \cdot t}{2}

$$

$ $\text{Resolution} = \frac{c}{2 \cdot \text{bandwidth}}

$$## Sound Velocity Profile

$ $ c = 1449.2 + 4.6T - 0.055T^2 + 1.34(S - 35) + 0.018D $$

where $ T $= temperature (°C),$ S $ = salinity (‰),$ D $ = depth (m).

### Sound Velocity Table

| Depth (m) | Temperature (°C) | Salinity (‰) | Sound Velocity (m/s) |
|-----------|-------------------|---------------|----------------------|
| 0 | 28 | 34.5 | 1521 |
| 50 | 18 | 34.8 | 1518 |
| 200 | 12 | 35.0 | 1513 |
| 500 | 8 | 35.0 | 1510 |
| 1000 | 4 | 35.0 | 1506 |
| 4000 | 2 | 35.0 | 1504 |

## Tidal Corrections

### Tidal Model

$ $ h_{corrected} = h_{measured} + h_{tide}(t) - h_{chart}$$

where $ h_{tide}(t) $ is the tide level at measurement time and $ h_{chart}$ is the chart datum.

### Tidal Constituents

| Constituent | Period | Amplitude (Indonesia) |
|-------------|--------|----------------------|
| M2 | 12.42 h | 0.3–1.5 m |
| S2 | 12.00 h | 0.1–0.5 m |
| K1 | 23.93 h | 0.1–0.8 m |
| O1 | 25.82 h | 0.05–0.3 m |

## Chart Datum

In Indonesia, chart datum is typically:
- **Lowest Astronomical Tide (LAT)** for most waters
- **Mean Lowest Low Water (MLLW)** for some areas
- Referenced to the [[Vertical Datum]] of the national system

## In [[Geodesy]] Context

### Positioning for Hydrographic Survey

| Method | Horizontal Accuracy | Vertical Accuracy | Use |
|--------|-------------------|-------------------|-----|
| [[RTK]] GNSS | 2–5 cm | 3–8 cm | Coastal, ports |
| [[PPP]] | 5–10 cm | 10–20 cm | Open ocean |
| DGPS | 1–3 m | 2–5 m | General navigation |
| USBL | 0.1–1% of range | 0.5–2% of range | Underwater vehicles |

### Indonesian Hydrographic Surveys

| Project | Area | Purpose |
|---------|------|---------|
| NAS-12 | Natuna Sea | Oil/gas exploration |
| Bakosurtanal surveys | All waters | Nautical charts |
| Port surveys | Major ports | Dredging, navigation |
| Coral reef mapping | Raja Ampat, etc. | Conservation |

## IHO Standards

| Standard | Description |
|----------|-------------|
| S-44 | Bathymetric survey standards |
| S-57 | Nautical chart data format |
| S-100 | Universal hydrographic data model |
| S-102 | Bathymetric surface |
| S-111 | Surface currents |

## Study Problems

1. Compute the depth for a two-way travel time of 0.4 s in 28°C water.
2. Explain why sound velocity profiling is essential for MBES surveys.
3. Calculate the tidal correction if tide is +1.2 m above chart datum.
4. Why is chart datum set at LAT rather than MSL?

## Related Concepts

- [[Survei Hidrografi I]] — Hydrographic survey course
- [[Survei Hidrografi II]] — Advanced hydrography
- [[Sea Surface Height]] — Tides and currents
- [[Vertical Datum]] — Height reference
- [[Tidal Theory]] — Tidal mechanics
- [[Survei Rekayasa Laut]] — Offshore engineering survey
- [[GPS]] — Positioning for hydrography

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
