---
tags: [aigis, concept, geodesy, surveying, edm, distance-measurement]
aliases: [EDM, Electronic Distance Measurement]
created: 2026-07-27
---

# Electronic Distance Measurement (EDM)

**Core Idea:** EDM instruments measure distances by timing the travel of electromagnetic waves (light, infrared, or microwave) between two points. Accuracy ranges from ±1 mm (geodetic) to ±1 cm (construction).

## How it Works
$$

D = \frac{c \cdot \Delta t}{2n}$$where$c$= speed of light,$n$= refractive index,$\Delta t$= round-trip time.

## Types

| Type | Range | Accuracy | Carrier |
|------|-------|----------|---------|
| **Infrared** | 0.5–5 km | ±5 mm | IR LED |
| **Short-range laser** | 0.05–3 km | ±1 mm | Visible laser |
| **Geodetic** | 0.1–30 km | ±0.5 mm | Modulated IR/laser |
| **Microwave** | 0.2–150 km | ±5 mm | Microwave carrier |

## Atmospheric Correction$$\Delta D_{atm} = D \cdot (n_0 - 1) \cdot \frac{P}{1013.25} \cdot \frac{283.15}{273.15 + T} \cdot 10^{-6}
$$

## Related

- [[Survei Terestris II]] — Total station practice

- [[Electromagnetism & Signal Propagation]] — EM theory

- [[Error Propagation]] — Distance accuracy analysis

---
*Part of [[Geodesy MOC]]*