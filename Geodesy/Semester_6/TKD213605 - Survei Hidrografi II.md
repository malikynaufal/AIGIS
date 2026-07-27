# Survei Hidrografi II (*Hydrographic Survey II*)

**Kode:** TKD213605
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Survei Hidrografi I

---

## 1. Overview

Advanced hydrographic surveying expands upon the fundamentals of hydrography I (single-beam echo sounding) to cover **multibeam systems**, **side-scan sonar**, **tidal analysis**, and **autonomous chart production**. This course addresses the modern tools and techniques for comprehensive seafloor mapping, with specific relevance to the Indonesian archipelago's maritime domain.

---

## 2. Multibeam Echosounder (MBES)

### 2.1 Operating Principles

A multibeam echosounder (MBES) transmits a扇面 (fan-shaped) beam pattern across the seabed, creating a swath of depth soundings:

**Beam geometry:**

$$\alpha_n = -\alpha_{\max} + n \cdot \Delta\alpha\theta_n = \alpha_n + \phi$$where:
-$\alpha_n$= angle from nadir (swath perpendicular)
-$\Delta\alpha$= beam width (typically 0.5°–1°)
-$\phi$= roll angle
-$n$= beam number (0 = nadir)

**Swath width:*
*

$$W = 2 d \cdot \tan(\alpha_{\max})$$

**Number of beams:*
*

$$N_{\text{beams}} = \frac{2\alpha_{\max}}{\Delta\alpha} + 1$$For a typical MBES with $\alpha_{\max} = 60°$and $\Delta\alpha = 1°$:

$$N = 121 \text{ beams per swath} $$### 2.2 MBES Frequency vs. Depth Range

| Frequency | Depth Range | Beam Angle | Resolution |
|-----------|-------------|------------|------------|
| 200 kHz | 10–200 m | 1° | 0.1–0.5 m |
| 400 kHz | 10–100 m | 1° | 0.1 m |
| 70 kHz | 100–1000 m | 1° | 0.5–1 m |

### 2.3 Motion Compensation

The MBES measures along the acoustic beam, requiring compensation for vessel motion
:

$$\vec{r}_{\text{corrected}} = \vec{r}_{\text{raw}} - R_z(\psi) \cdot R_y(\theta) \cdot R_x(\phi) \cdot \vec{r}_{\text{transducer}} $$Where $R_x(\phi), R_y(\theta), R_z(\psi) $are rotation matrices for **roll, pitch, yaw** angles compensated by the **MRU (Motion Reference Unit)**.

### 2.4 Patch Test

A vessel patch test calibrates 6 parameters:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Roll error | $\delta\phi$ | MRU roll bias |
| Pitch error | $\delta\theta$ | MRU pitch bias |
| Yaw error | $\delta\psi$ | MRU heading bias |
| Delay | $\delta t$ | Time lag (transducer to MRU) |
| X-offset | $\delta x$ | Transducer horizontal position |
| Z-offset | $\delta z$ | Transducer vertical position |

Patch test procedure:
1. Sail in straight lines (N-S, E-W)
2. Sail in circles (~3-5 revolutions)
3. Analyze cross-track and along-track errors
4. Optimize 6 parameters iteratively

---

## 3. Side-Scan Sonar (*Sonar Samping*)

### 3.1 Operating Principle

Side-scan sonar (SSS) maps the **acoustic seafloor reflectivity** (backscatter), providing imagery of the seabed that complements bathymetric data
:

$$R = \frac{P_r}{P_t} \cdot \left(\frac{c}{2}\right)^{2\cdot r} $$where $R$is reflectivity,$P_r$= received power,$P_t$= transmitted power,$r$= slant range.

### 3.2 System Configuration

| Parameter | Typical Value |
|-----------|---------------|
| Frequency | 200 kHz – 1 MHz |
| Swath width | 2–15× water depth |
| Ground range | 10–200 m |
| Sonar image resolution (GSD) | 2.5–10 cm |

### 3.3 Applications

| Application | Description |
|-------------|-------------|
| **Target detection** | Wrecks, debris, mines |
| **Seabed classification** | Sand, mud, rock |
| **Pipeline/ cable inspection** | Buried/obstructed infrastructure |
| **Fishing** | Fish habitat mapping |
| **Geological mapping** | Sediment texture |

### 3.4 Interpreting Backscatter

| Seabed Type | Backscatter | Acoustic Appearance |
|-------------|-------------|---------------------|
| Gravel/sand | High (bright) | White/gray |
| Mud/silt | Low (dark) | Dark gray/black |
| Coral/rock | Very high (bright) | White |
| Seagrass | Medium (textured) | Gray with texture |
| Shipwreck | Very high (echo) | Bright spot |

---

## 4. Tidal Analysis (*Analisis Pasang Surut*)

### 4.1 Harmonic Analysis

Tides can be decomposed into harmonic constituents
:

$$\eta(t) = Z_0 + \sum_{i=1}^{N} R_i \cos(\omega_i t - \phi_i) + \epsilon(t)$$

where:
-$\eta(t)$= water surface elevation at time $t$-$Z_0$= mean water level
-$R_i$= amplitude of constituent $i$-$\omega_i$= angular frequency of constituent $i$-$\phi_i$= phase lag
-$\epsilon(t)$= residual

### 4.2 Major Tidal Constituents

| Constituent | Period | Amplitude | Description |
|-------------|--------|-----------|-------------|
| $M_2$ | ~12.42 h | Largest | Lunar semidiurnal |
| $S_2$ | ~12.00 h | ~0.5 ×$M_2$ | Solar semidiurnal |
| $N_2$ | ~12.66 h | Reduced | Lunar elliptic |
| $K_1$ | ~23.93 h | Diurnal | Lunar-solar |
| $O_1$ | ~25.82 h | Diurnal | Lunar diurnal |

### 4.3 Tide Prediction

For a given epoch $t$:

$$\eta(t) = Z_0 + \sum_{i=1}^{N} R_i \cos(\omega_i t - \phi_i)$$**Chart datum** typically corresponds to **Lowest Astronomical Tide (LAT)** — the lowest predictable tidal level.

### 4.4 Indonesian Tidal Regimes

| Region | Type | Characteristics |
|--------|------|-----------------|
| Java Sea | Mixed semidiurnal | Two highs, two lows per day |
| Nusa Tenggara | Diurnal | One high, one low |
| Maluku | Semidiurnal | Equal two highs |
| Arafura Sea | Mixed | Complex |

### 4.5 Tide Correction for Sounding
s

$$d_{CD} = d_{\text{observed}} - (\text{HT} - \text{RT})$$

where:

- HT = Heel Tide (correction for vessel movement)

- RT = Tidal reduction (observed - CD)

---

## 5. Chart Datum (*Dasar Peta*)

### 5.1 Chart Datum vs. Tide Gauge Datum

| Datum Type | Description |
|------------|-------------|
| **Chart Datum (CD)** | Depths referenced lowest predictable tide |
| **Mean Low Water (MLW)** | Average of low waters |
| **Mean Sea Level (MSL)** | Average of all tide readings |
| **Highest Astronomical Tide (HAT)** | Highest predictable astronomical level |
| **Lowest Astronomical Tide (LAT)** | Lowest predictable astronomical level |

### 5.2 IHO Standards

- **IHO S-4** (now S-23) defines standard chart datum practices

- **Squat** effect for vessel depth correction
:

$$\Delta d = \frac{v^2}{2g}(C_B - C_B^2)$$where $v$= vessel speed,$g$= gravity,$C_B$= block coefficient.

---

## 6. Advanced Data Processing

### 6.1 Tidal Correction Pipeline

```
Raw depth (time stamp → UTC)
 ↓
1. Tide prediction → Predicted tide at time of sounding
2. Tidal correction → Observed depth - predicted tide + CD
3. Heel correction → Sound velocity ray-bending for vessel tilt
4. Sound velocity correction → CTD-based refraction
5. SVP interpolation → Depth-dependent sound speed
6. Quality control → SDE check, outlier detection
```

### 6.2 Gridding Methods for Bathymetry

| Method | Algorithm | Use |
|--------|-----------|-----|
| **Natural Neighbor** | Voronoi-based | Irregular data |
| **Kriging** | Geostatistical | Optimal interpolation |
| **Minimum Curvature** | Biharmonic splines | Smooth surfaces |
| **Inverse Distance** | IDW | Quick visualization |
| **B-spline** | Polynomial basis | High-res MBES |
| **EMD** (Empirical Mode Decomposition) | Adaptive | Complex terrain |

### 6.3 Quality Indicators

**Standard Deviation of Depth Error (SDE):*
*

$$\text{SDE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (z_{obs,i} - z_{grid,i})^2} $$

**IHO S-44 requirements:**
| Order | SDE |
|-------|-----|
| Order 1 | ≤ 0.25 m |
| Order 2 | ≤ 0.5 m |
| Order 3 | ≤ 0.5 m |

---

## 7. Digital Bathymetric Chart Production

### 7.1 IHO S-57 to S-100

**S-57** (Transfer Standard) → **S-100** (Universal Hydrographic Data Model)

Migration reasons:

- S-57 is ISO 19100 based; S-100 is ISO 19100 family-based

- S-100 supports 3D data, temporal data

- S-100 is extensible — any data type can be represented

### 7.2 Chart Features

| Feature Type | S-57 Object | Description |
|-------------|-------------|-------------|
| **Depth sounding** | SO Undredged / SO Dredged | Bottom depth |
| **Bank/shoal** | SO Submerged Bank | Shallow hazard |
| **Wreck** | SO Wreck | Hazard object |
| **Rock** | SO Rock (Awash) | Submerged hazard |
| **Buoys** | SO Small-Craft Fairway Buoy | Navigation aid |
| **Seabed composition** | SO Seabed (Mud/Sand/Clay) | SSS classification |

---

## 8. Indonesian Maritime Context

### 8.1 National Hydrographic Office

**HO** (Hydro-Oceanographic Office) of TNI AL conducts:

- **National bathymetric survey** program

- **Nautical chart production** (S-57 compliant)

- **Dredging support**

- **Marine infrastructure surveys** (ports, harbors)

### 8.2 Strategic Waterways

| Waterway | Significance |
|----------|-------------|
| **Selat Sunda** | Java-Sumatra passage |
| **Selat Malaka** | World's busiest shipping lane |
| **Selat Makassar** | Kalimantan-Sulawesi route |
| **Laut Flores** | East Indonesia connectivity |
| **Teluk Cenderawasih** | Papua development route |

### 8.3 Current Survey Equipment

The Indonesian hydrographic fleet uses:

- **MBES:** Kongsberg EM712, R2Sonic 2024

- **SSS:** EdgeTech 2205, Klein 5000

- **Positioning:** RTK GNSS (Trimble, Topcon)

- **Motion sensors:** Applanix POS MV (Inertial + GNSS)

- **Tide gauges:** Valeport MiniSVS, OTT

---

## 9. Emerging Technology

### 9.1 Autonomous Surface Vessels (ASV)

- Uncrewed survey vessels for dangerous/shallow areas

- **Advantages:** Lower cost, 24/7 operation, safer

- **Equipment:** Compact MBES, SSS, GNSS

- **Challenges:** Communication, legal status in Indonesian waters

### 9.2 Satellite Bathymetry

- **Satellite-derived bathymetry (SDB):*
*

$$d \approx f(\lambda_{green}, \lambda_{near\text{-}IR})$$

Green light penetrates water to ~30 m depth; near-IR reflects from surface.

- **Satellite data:** Sentinel-2 (10 m), WorldView (3.7 m)

- **Maximum depth:** 50–80 m (turbidity dependent)

- **Spatial resolution:** 3.7–30 m

- **Application:** Preliminary reconnaissance surveys, coastal mapping

### 9.3 LiDAR Bathymetry (LIDAR/LIDARB)

Airborne LiDAR with green laser penetrates water surface
:

$$z_{bottom} = z_{surface} - \frac{c}{2} \cdot t_{water} $$

- **Depth penetration:** 0–50 m (clear water)

- **Accuracy:** ±15–30 cm

- **Data density:** 1–10 pts/m²

- **Advantages:** Simultaneous land/sea mapping

---

## 10. Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Swath width | $W = 2d \cdot \tan(\alpha_{\max})$ |
| Number of beams | $N = \frac{2\alpha_{\max}}{\Delta\alpha} + 1$ |
| Tide prediction | $\eta(t) = Z_0 + \sum R_i \cos(\omega_i t - \phi_i)$ |
| Heel correction | $d_{corr} = d / \cos\theta$ |
| SDE | $\text{SDE} = \sqrt{\frac{1}{n}\sum(z_{obs}-z_{grid})^2} $ |
| Backscatter (relative) | $R = \frac{P_r}{P_t} \cdot \left(\frac{c}{2}\right)^{2r} $ |

---

## References

1. IHO (2008). *Standards for Hydrographic Surveys*, 6th ed. (S-44).
2. IHO (2021). *S-100 Universal Hydrographic Data Model*.
3. Stow, D.A. (2017). *Hydrographic Surveying*. Springer.
4. Liddell, B.H. (1987). *Hydrographic Surveying*. US Naval Institute Press.
5. Kongsberg Maritime (2022). *EM-Series MBES User Manual*.
6. Lee, K. & Liu, P. (2008). "Satellite-Derived Bathymetry." *ISPRS Journal*.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*
