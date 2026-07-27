---
tags: [aigis, geodesy, pilihan, remote-sensing-applied, satellite]
aliases: [Applied Remote Sensing, Penginderaan Jauh Terapan]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Penginderaan Jauh Terapan (Applied Remote Sensing)

**Kode:** TKD214707 | **SKS:** 3 (2-1) | **Semester:** 6–8

## Course Overview

Advanced applications of [[Remote Sensing]] data for environmental monitoring, resource management, and urban planning. Covers Sentinel-2/Landsat analysis, object-based image analysis (OBIA), time series analysis, and machine learning for image classification.

## Key Topics

### 1. Classification Methods

| Method | Type | Training Data | Accuracy |
|--------|------|---------------|----------|
| Maximum Likelihood | Pixel-based | Required | 80–85% |
| Random Forest | Pixel/object | Required | 85–95% |
| SVM | Object-based | Required | 90–95% |
| Deep Learning (CNN) | Object-based | Large required | 95%+ |

### 2. Time Series Analysis

**NDVI time series for phenology:**

$$

NDVI(t) = a + b \sin(2\pi t) + c \cos(2\pi t)

$ $

**Change detection:**

$$

\Delta NDVI = NDVI_{t2} - NDVI_{t1}

$$

### 3. Land Cover/Land Use

- Sentinel-2 10-class classification
- Forest cover change in Kalimantan
- Urban expansion in Jabodetabek

---
*Maintained by AIGIS — part of [[Geodesy MOC]]*
