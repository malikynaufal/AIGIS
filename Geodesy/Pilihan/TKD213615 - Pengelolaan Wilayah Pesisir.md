---
tags: [aigis, geodesy, pilihan, coastal-management, gis, environment]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Pengelolaan Wilayah Pesisir (Coastal Zone Management)

**Kode:** TKD213615 | **SKS:** 3 (2-1) | **Semester:** 5–7

## Course Overview

Coastal Zone Management integrates [[GIS]], [[Remote Sensing]], and [[Survei Hidrografi]] techniques for the sustainable management of coastal areas. Covers shoreline mapping, coastal zoning, mangrove monitoring, and spatial planning for coastal resources.

## Key Topics

### 1. Coastal Survey Techniques

| Method | Application | Accuracy |
|--------|-------------|----------|
| RTK-GNSS | Shoreline mapping | 2–5 cm |
| Hydrographic | Bathymetry | 5–20 cm |
| Aerial photography | Land cover | 10–50 cm |
| Satellite remote sensing | Large-scale changes | 30 m (Landsat) |
| UAV/drone survey | High-resolution coastal | 2–10 cm |

### 2. Shoreline Change Analysis

**End Point Rate (EPR):**

$$

R_{EPR} = \frac{x_2 - x_1}{t_2 - t_1}

$ $

**Linear Regression Rate (LRR):**

$$ R_{LRR} = \text{slope of shoreline position vs. time}

$ $

### 3. Coastal Vulnerability Index (CVI)

$$

CVI = \frac{\sqrt{\prod_{i=1}^n r_i}}{n}

$ $

where $ r_i$ are ranked factors (geomorphology, slope, sea-level rise, wave height, tide range)

### 4. Mangrove Monitoring

**Vegetation Indices for Mangroves:**
- **MVI (Mangrove Vegetation Index):**

 $ $ MVI = \frac{NIR - SWIR}{Green - SWIR}$$

- **NDVI:** Standard vegetation density

### 5. Coastal Zoning in Indonesia

| Zone | Designation | Buffer |
|------|------------|--------|
| Sempadan Pantai | Protected shoreline | 100 m from MHWL |
| WiP | Public access | Variable |
| KPA | Conservation area | Full protection |

## Assignment
Map shoreline change for a 20 km coastal segment using Landsat time series (5 epochs over 20 years). Compute EPR and LRR rates.

## Related Concepts

- [[Survei Hidrografi I]] — Hydrographic survey
- [[Survei Rekayasa Laut]] — Marine engineering
- [[Remote Sensing]] — Satellite monitoring
- [[Sistem Informasi Geografis Terapan]] — GIS application
- [[Mitigasi dan Manajemen Bencana]] — Disaster management

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
