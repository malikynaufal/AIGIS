---
tags: [aigis, concept, geodesy, deformation-monitoring, insar, gps-monitoring, structural]
aliases: [Deformation Monitoring, Structural Monitoring, Crustal Monitoring]
created: 2026-07-27
updated: 2026-07-27
---

# Deformation Monitoring

## Overview

**Deformation monitoring** (Survei Deformasi) measures changes in the shape or position of objects over time — from buildings and dams to tectonic plates. It uses repeated surveys, [[GPS|GNSS]], [[InSAR|InSAR]], and [[Levenslijn]] leveling to detect displacements with millimeter precision.

## Monitoring Techniques

### GNSS Deformation Monitoring

| Method | Accuracy | Temporal Resolution | Spatial Coverage |
|--------|----------|---------------------|------------------|
| Continuous GNSS | 1–3 mm (H), 3–5 mm (V) | Real-time | Point-based |
| Campaign GNSS | 2–5 mm (H), 5–10 mm (V) | Monthly–yearly | Network |
| [[RTK]] monitoring | 5–10 mm | Minutes | Local area |

### InSAR (Interferometric SAR)

| Technique | Accuracy | Temporal Resolution | Spatial Coverage |
|-----------|----------|---------------------|------------------|
| PS-InSAR | 1–5 mm | Days–weeks | Regional |
| SBAS-InSAR | 2–10 mm | Weeks–months | Regional |
| D-InSAR | 5–10 mm | Days | Regional |

### Levelling

| Method | Accuracy | Application |
|--------|----------|-------------|
| Precise levelling | ±0.3 mm/km | Dam, bridge, building |
| Digital levelling | ±0.5 mm/km | Road, railway |
| Trigonometric levelling | ±5–10 mm | Rough terrain |

## Mathematical Models

### Linear Displacement Model

$$\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v} \cdot t

$ $### Seasonal + Linear Model $$\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v} \cdot t + \mathbf{A}_1 \sin(2\pi t) + \mathbf{A}_2 \cos(2\pi t)

$ $### Reference Frame for Deformation $$\Delta \mathbf{r} = \mathbf{r}_{target}(t) - \mathbf{r}_{ref}(t) - \mathbf{T}_{plate}(t)

$ $

where $\mathbf{r}_{ref} $ are stable reference stations and $\mathbf{T}_{plate} $ is the tectonic model.

## In [[Geodesy]] Context

### Indonesian Deformation Applications

| Application | Method | Area |
|-------------|--------|------|
| Jakarta subsidence | [[PPP]], PS-InSAR | Jakarta |
| Volcanic monitoring | GNSS + InSAR | Merapi, Rinjani |
| Earthquake hazard | GNSS network | Sunda subduction |
| Dam monitoring | Levelling + GNSS | Jatiluhur, Saguling |
| Land subsidence | InSAR | Semarang, Surabaya |
| [[Survei Geodinamika|Geodynamic survey]] | GNSS + InSAR | All regions |

### Critical Zone: Jakarta Subsidence

| Area | Subsidence Rate | Cause |
|------|-----------------|-------|
| North Jakarta | 5–25 cm/yr | Groundwater extraction |
| Central Jakarta | 1–5 cm/yr | Mixed |
| South Jakarta | 0.5–2 cm/yr | Mixed |
| East Jakarta | 2–10 cm/yr | Groundwater |

## Statistical Analysis

### Velocity Estimation

$ $\hat{v} = \frac{\sum_{i=1}^{n} (t_i - \bar{t})(r_i - \bar{r})}{\sum_{i=1}^{n} (t_i - \bar{t})^2}

$$

# ## Confidence Interval $ $\hat{v} \pm t_{\alpha/2, n-2} \cdot \frac{s_v}{\sqrt{n}}

$$

where $ s_v$ is the standard error of the velocity.

## Study Problems

1. Explain why reference stations must be stable for deformation monitoring.
2. Compute the subsidence rate given annual measurements over 5 years.
3. Why is PS-InSAR preferred over D-InSAR for long-term monitoring?

## Related Concepts

- [[Crustal Deformation]] — Tectonic deformation
- [[Survei Deformasi]] — Course on deformation survey
- [[Survei Geodinamika]] — Geodynamic monitoring
- [[InSAR|Satellite deformation]]
- [[GPS]] — GNSS monitoring
- [[Levenslijn|Leveling]] — Precise height monitoring

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*
