---
tags: [geodesy, concept, heights, aigis]
aliases: [Orthometric Height, Tinggi Ortometrik, H, Height Above Geoid]
created: 2026-07-12
updated: 2026-07-27
---

# 📉 Orthometric Height (H)

**Orthometric height** $H $ is the height above the [[Geoid]] measured along the local plumb line (the direction of gravity). This is the "real" height used in mapping, civil engineering, cadastre, and topographic maps — the one that makes water flow downhill.

## Definition

The orthometric height of a point $ P $ is

$ $ H = \frac{\overline{W}_0 - \overline{W}_P}{\overline{g}}$$

where $\overline{W}_0 $ is the geoid potential,$\overline{W}_P $ is the actual gravity potential at $ P $, and $\overline{g} $ is the mean gravity along the plumb line between geoid and point.

In practice

$ $ H = h - N $$

where $ h $ is the [[Ellipsoidal Height]] from [[GNSS]] and $ N $ is the [[Geoid Undulation]] from a geoid model.

## Determination Methods

### Spirit Leveling (Direct Measurement)

The most accurate method for local orthometric height:

1. **Geometric leveling:** Survey teams set up an optical or digital level at a reference benchmark, take measurements at a forward rod (read height differences), and carry the vertical difference from the benchmark.
2. **Accuracy:** ±0.2–0.5 mm/km (1st order leveling); ±0.1 mm/km (with high-precision digital level and invar rod
)

$ $\Delta H_{AB} = \sum \Delta h_i

$$

where $\Delta h_i $ are the leveling increments from A to B.

**Challenge:** Leveling measures **potential difference**, not geometric height. It is path-dependent on Earth's gravity field (tidal corrections, orthometric correction).

### GNSS + Geoid Model

The indirect method used today in most surveys:

1. Measure $ h $ via GPS/GNSS (cm-level with RTK or PPP).
2. Obtain $ N $ from EGM2008 or national geoid model (e.g., GEOID18, EGG2008).
3. Compute $ H = h - N $.

**Accuracy drivers:**

- GNSS vertical accuracy: 1–3 cm (RTK), 2–5 cm (PPP)

- Geoid model accuracy: 1–3 cm (USA GEOID18), 5–15 cm (global EGM2008)

- Combined: 3–10 cm for $ H $### Precise Gravimetric Method (Helmert Orthometric Height)

The most rigorous definition accounts for the actual gravity field

$ $ H = \frac{C}{\overline{g}}, \quad C = W_0 - W_P = \int_{0}^{H} g\,dH $$

where $ C $ is the **geopotential number** and $\overline{g} $ is the mean gravity along the plumb line. This is the approach used in the International Height Reference System (IHRS).

## Relationship Between Height
s

$ $ h = H + N $$

| Symbol | Name | Reference Surface |
|--------|------|-------------------|
| $ h $ | Ellipsoidal height | Reference Ellipsoid |
| $ H $ | Orthometric height | Geoid (mean sea level) |
| $ N $ | Geoid undulation | Geoid − Ellipsoid |
| $\zeta $ | Height anomaly | Quasi-geoid − Ellipsoid |

## Common Heights Summary

| Height Type | Reference | Use Case |
|-------------|-----------|----------|
| **Orthometric**$ H $ | Geoid | Topo maps, engineering, cadastre |
| **Normal-orthometric**$ H_N $ | Quasi-geoid | Some European countries |
| **Normal**$ H_N $ | Ellipsoid + normal gravity | Molodensky system |
| **Dynamic**$ H_D $ | Geoid (potential) | Hydrological works |

## Accuracy Considerations

| Application | Required Orthometric Accuracy | Method |
|-------------|-------------------------------|--------|
| Engineering construction | ±1–2 cm | 1st-order leveling |
| Topographic mapping | ±10 cm | RTK GNSS + geoid |
| 3D city models | ±5 cm | RTK + GEOID18 |
| Sea level monitoring | ±0.5 mm/yr | Tide gauge + precise leveling |
| Flood risk mapping | ±5–15 cm | RTK GNSS + global geoid |

## Worked Example

**Problem:** A GNSS survey at a building site gives ellipsoidal height $ h = 243.176 $ m. Using the national geoid model, the geoid undulation at the site is $ N = 41.528 $ m. What is the orthometric height for construction plans?

**Solution:*
*

$ $ H = h - N = 243.176 - 41.528 = 201.648\ \text{m}$$

This 201.65 m is the value to put on engineering drawings. If the construction crew uses a level (spirit leveling), they will measure 201.65 m from the site benchmark, consistent with the GNSS result.

## The Orthometric Height Dilemma in GNSS

GNSS gives $ h $ but engineers need $ H $. The conversion requires a geoid model. Key points:

1. **If the geoid model is wrong by 10 cm**, $ H $ is wrong by 10 cm — even with perfect GNSS.
2. **Local benchmarks** (tide gauge connections) anchor the geoid model.
3. **National geoid models** (GEOID24 in US, EGG2008 in Europe) provide $ N $ at geoid models with 2–3 cm accuracy.
4. **In Indonesia**, the geoid model (GeoidINDO or EGM2008) provides $ N$ at 5–15 cm accuracy over land.

## References

- Hofmann-Wellenhof, B. & Moritz, H. (2006). *Physical Geodesy*, 2nd ed. Springer.

- Heiskanen, W. A. & Moritz, H. (1967). *Physical Geodesy*. Freeman.

- NGS. *Orthometric Heights and NAVD88*. www.ngs.noaa.gov

- BIG. *Geoid Model Indonesia*. www.big.go.id

## Related

- [[Geoid]] · [[Ellipsoidal Height]] · [[Geoid Undulation]] · [[Physical Geodesy]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
