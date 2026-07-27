---
tags: [aigis, geodesy, pilihan, geosensor, sensors, electronics]
aliases: [Dasar Geosensor, Geo-sensor Fundamentals]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Dasar Geosensor (Geo-sensor Fundamentals)

**Kode:** TKD214704 | **SKS:** 3 (2-1) | **Semester:** 6–8

## Course Overview

Fundamentals of geo-sensors used in geodetic instruments — electronic theodolites, total stations, GNSS receivers, inertial sensors, and environmental sensors. Focus on signal processing, calibration, and error analysis.

## Key Topics

### 1. Types of Geo-sensors

| Sensor | Measurand | Application |
|--------|-----------|-------------|
| CCD/CMOS | Light intensity | [[Photogrammetry]] cameras |
| Accelerometer | Acceleration | IMU, INS |
| Gyroscope | Angular rate | IMU, INS |
| Magnetometer | Magnetic field | Compass, orientation |
| Photodiode | Optical signal | EDM |
| Barometer | Pressure | Height measurement |

### 2. Sensor Error Models

**Linear sensor model:**
$$y = a + b \cdot x + \epsilon$ $where$a$= bias, $b$= scale factor, $\epsilon $ = noise.

**Allan variance for noise characterization:**$ $\sigma^2(\tau) = \frac{1}{2(N-1)} \sum_{i=1}^{N-1} (y_{i+1}(\tau) - y_i(\tau))^2
$$
# ## 3. IMU / INS Principles

**Strapdown INS mechanization:**
$$
\begin{pmatrix}
\dot{\phi} \\ \dot{\lambda} \\ \dot{h}
\end{pmatrix} = f(\mathbf{f}^n, \boldsymbol{\omega}^n, \mathbf{R}_b^n)$\$$
# ## 4. Calibration

- Scale factor and bias estimation for GNSS receivers
- EDM offset/scale calibration
- Camera calibration (intrinsic parameters)

---
*Maintained by AIGIS — part of [[Geodesy MOC]]*
