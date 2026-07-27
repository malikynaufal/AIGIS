# Jaring Kontrol Geodesi (*Geodetic Control Network*)

**Kode:** TKD213604
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Geodesi Dasar, Survei GNSS

---

## 1. Overview

A geodetic control network (*jaring kontrol geodesi*) is a framework of precisely determined points that serves as the reference for all surveying and mapping activities. In Indonesia, the national geodetic network is designated **SKRGI** (*Seksi Kerangka Referensi Geodesi Indonesia*), managed by **BIG** (*Badan Informasi Geospasial*).

---

## 2. Network Design

### 2.1 Network Types

| Type | Purpose | Accuracy |
|------|---------|----------|
| **Zero-order** | National reference frame | ~1 cm |
| **First-order** | Regional control | ~5 cm |
| **Second-order** | Local control | ~10 cm |
| **Third-order** | Detailed/topographic | ~20 cm |
| **Forth-order** | Cadastral/local detail | ±10 cm |

### 2.2 Network Geometry

The design of a geodetic network must balance:

- **Strength of figure** — geometry of triangles

- **Redundancy** — number of redundant observations

- **Economy** — efficient use of resources

- **Accessibility** — practicality of field observations

#### Strength of Figure

For a triangle network, the **strength ratio** $R $determines error propagation
:

$$R = \frac{\text{product of non-adjusted sides}}{\text{product of adjusted sides}} $$A smaller $R$indicates better geometric strength. For first-order networks,$R < 1.5 \times 10^{-4} $.

### 2.3 Geometric Criteria

| Criterion | First Order | Second Order |
|-----------|-------------|--------------|
| Triangle side length | 20–150 km | 10–40 km |
| Minimum angle | 30° | 30° |
| Maximum angle | 120° | 120° |
| Side length ratio | > 1:3 | > 1:4 |
| Maximum closure | 0.15 m | 0.3 m |
| Number of observations per point | ≥ 3 | ≥ 3 |

### 2.4 Redundancy

The **redundancy** $r $of a network
:

$$r = n - u$$where $n$is the number of observations and $u $is the number of unknowns.

For a 2D network with $p $points
:

$$u = 2p - 2 \quad \text{(fixing 2 degrees of freedom)} $$

---

## 3. Observation Methods

### 3.1 Triangulation (*Triangulasi*)

Measurement of **horizontal angles** from network stations:

| Type | Method | Application |
|------|--------|-------------|
| **Helmert** | 24 observations (12 FL + 12 FR) per triangle | First-order |
| **Dreyer** | 12 observations (6 FL + 6 FR) | Second-order |
| **Schumacher** | 8 observations (4 FL + 4 FR) | Third-order |

**Angular accuracy requirements:*
*

$$m_{\text{angle}} = \frac{1.5}{\sqrt{2}} \cdot c \; \text{for first-order} $$where $c$is the micrometer reading accuracy of the theodolite (typically 0.01").

### 3.2 Trilateration (*Trilaterasi*)

Direct measurement of **distances** between stations using EDM (Electronic Distance Measurement)
:

$$\sigma = \sqrt{(a)^2 + (b \cdot d)^2} $$

where:
-$a$= constant error (mm)
-$b$= proportional error (ppm)
-$d$= distance (km)

For a Leica TDM6000:$\sigma = \pm(1 \text{ mm} + 0.5 \text{ ppm})$### 3.3 Combined Method

Modern geodetic surveys combine:

- **GNSS observations** for position

- **EDM** for distance verification

- **Astronomical observations** for azimuth

### 3.4 GNSS-Based Control

#### Static Method

- **Duration:** 1–4 hours per session

- **Accuracy:** ±2–5 mm + 0.5 ppm

- **Application:** Zero- and first-order control

#### Rapid Static

- **Duration:** 15–30 minutes

- **Accuracy:** ±5–10 mm + 1 ppm

- **Application:** Second-order control

#### Continuous Operating Reference Stations (CORS)

- Permanent GNSS receivers with data logging

- Real-time correction service for surveying

- INACORS network: 150+ stations

---

## 4. Survey Methods

### 4.1 Triangulation Survey

```
1. Reconnaissance (pemetaan awal)
 - Identify stations and intervisibility
 - Plan observation schedules
 ↓
2. Monumentation (penentuan tonggak)
 - Establish permanent marks
 - Include identification plates
 ↓
3. Station observation (pengamatan stasiun)
 - Angular measurements (face left, face right)
 - Multiple rounds of observations
 ↓
4. Baseline measurement
 - Measure baseline with EDM
 - Apply atmospheric corrections
 ↓
5. Data processing
 - Preliminary adjustment
 - Error analysis
 ↓
6. Final adjustment
 - Least squares adjustment
 - Quality indicators
```

### 4.2 GNSS Survey

```
1. Reconnaissance (pemetaan)
 ↓
2. Monumentation (penentuan tonggak)
 ↓
3. Observation (pengamatan)
 - Static sessions
 - Field logging
 ↓
4. Data processing
 - RINEX → baseline vectors
 - Ambiguity resolution
 ↓
5. Network adjustment
 - Least squares
 - Quality checks
 ↓
6. Coordinate transformation
 - UTM projection
 - Height transformation
```

---

## 5. Least Squares Adjustment

### 5.1 Fundamental Equation

For a system of $n $observations and $u $unknowns, the least squares solution
:

$$\hat{x} = (A^T P A)^{-1} A^T P l$$

where:
-$\hat{x} $= vector of unknown parameters
-$A$= design matrix (partial derivatives of observations w.r.t. parameters)
-$P$ = weight matrix ($P = \sigma_0^2 \Sigma^{-1} $, where $\Sigma $is covariance matrix)
-$l$= observation vector (observed minus computed values)

### 5.2 Residuals and Quality

**Residual vector:*
*

$$v = A\hat{x} - l$$

**Standard error of unit weight:*
*

$$\sigma_0 = \sqrt{\frac{v^T P v}{n - u}} $$

**Standard error of parameters:*
*

$$\Sigma_{\hat{x}} = \sigma_0^2 (A^T P A)^{-1} $$

### 5.3 Chi-Square Tes
t

$$\chi^2 = \frac{v^T P v}{\sigma_0^2} \sim \chi^2(n - u)$$If $\chi^2 > \chi^2_{0.95}(n-u)$, the model may be inadequate or outliers may exist.

### 5.4 Network Types and Unknowns

**Horizontal 2D network:**

- Unknowns: coordinates $(x_i, y_i) $of $p $points

- If 2 points fixed:$u = 2(p-2)$**3D network:**

- Unknowns:$(x_i, y_i, z_i)$- If 2 points fixed (6 DOF):$u = 3(p-2)$---

## 6. Monumentation (*Penentuan Tonggak*)

### 6.1 Monument Types

| Type | Material | Use | Depth |
|------|----------|-----|-------|
| **Beton bertulang** | Reinforced concrete | Permanent | 1–2 m |
| **Tiang besi** | Iron rod | Semi-permanent | 0.5 m |
| **Bakar batu** | Iron stone, baked | Traditional | Surface |
| **Tiang pancang** | Steel pile | Coastal, soft ground | 3–10 m |

### 6.2 Monument Features

- **Identification plate** — engraved with name, number, date

- **Center mark** — cross or dot for precise centering

- **Reference points** — nearby points for reconstruction

- **Photographic documentation** — 4 cardinal views

### 6.3 INACORS Station Specifications

| Parameter | Requirement |
|-----------|-------------|
| Pillar height | 1.5–2 m above ground |
| Antenna height | Known to ±1 mm |
| Power supply | Uninterruptible (UPS + battery) |
| Communication | 3G/4G data link |
| Enclosure | Weatherproof, lockable |
| Monumentation | Deep foundation (2–3 m) |

---

## 7. Indonesia's SKRGI (National Geodetic Control Network)

### 7.1 Network Description

**SKRGI** (*Seksi Kerangka Referensi Geodesi Indonesia*) — Indonesia's national reference network:

| Level | Stations | Distribution | Accuracy |
|-------|----------|--------------|----------|
| **Zero-order** | 4 | Java, Sumatra, Kalimantan, Sulawesi | ±1–2 cm |
| **First-order** | ~30 | Major islands | ±5 cm |
| **Second-order** | ~200 | Provincial capitals | ±10 cm |
| **Third-order** | ~1000+ | Districts | ±20 cm |

### 7.2 Reference Frame

| Parameter | Current Value |
|-----------|--------------|
| **Coordinate system** | DGN95 (Datum Geodesi Nasional 1995) |
| **Realization** | Based on ITRF 1994, epoch 2000.0 |
| **Projection** | UTM (Universal Transverse Mercator) |
| **UTM zones** | 48S–51S (main archipelago) |
| **Vertical datum** | Geoid Besar Indonesia |
| **Geoid model** | Geoid Besar Indonesia 2013 |

### 7.3 DGN95 (Datum Geodesi Nasional 1995)

- **Origin:** Geocentric datum tied to ITRF 1994

- **Reference ellipsoid:** WGS84/GRS80

- **Transformation from WGS84:** minimal (< 0.1 m in Indonesia)

- **Bakosurtanal origin stations** as reference

### 7.4 Key Stations

| Station | Location | Level |
|---------|----------|-------|
| **Bakosurtanal** | Cibinong | Zero |
| **Gajah Mada** | Bandung | Zero |
| **Sanjaya** | Jakarta | Zero |
| **Ijen** | Jember | Zero |

---

## 8. Software for Network Adjustment

| Software | Type | Features |
|----------|------|----------|
| **GAMIT/GLOBK** | Open source | GPS-only, scientific |
| **Bernese** | Academic | Multi-GNSS, scientific |
| **Trimble Business Center** | Commercial | Industry standard |
| **Gnss-Process** | Open source | Multi-GNSS |
| **Adjustment Compute** | Open source | Classical adjustment |

---

## 9. Quality Assurance

### 9.1 Blunder Detection

- **Baarda data snooping** test for outlier detectio
n

$$|v_i| > k_{\alpha} \cdot \sigma_{v_i} $$

- **Chi-square test** for global model adequacy

### 9.2 Error Propagatio
n

$$\Sigma_{f} = B \cdot \Sigma_{\hat{x}} \cdot B^T$$where $B$is the Jacobian of the function $f(\hat{x}) $with respect to the adjusted parameters.

### 9.3 Reliability

**Internal reliability:** Ability to detect blunders within the observation set
**External reliability:** Impact of undetected blunders on the solutio
n

$$\text{Detectability} \geq \Delta_0 \cdot \sigma_{\text{observation}} $$

---

## 10. Key Formulas Summary

| Formula | Application |
|---------|-------------|
| $\hat{x} = (A^TPA)^{-1}A^TPl$ | Least squares |
| $\sigma_0 = \sqrt{\frac{v^T P v}{n-u}} $ | Unit weight error |
| $\Sigma_{\hat{x}} = \sigma_0^2 (A^TPA)^{-1} $ | Covariance matrix |
| $d = c \cdot t/2$ | EDM distance |
| $m = \sqrt{a^2 + (b \cdot d)^2} $ | EDM error budget |

---

## References

1. Torge, W. & Müller, J. (2012). *Geodesy*, 4th ed. de Gruyter.
2. BIG (2021). *Pedoman Kerangka Referensi Geodesi Indonesia*.
3. Ghilani, C.D. (2017). *Elementary Surveying*, 15th ed. Pearson.
4. Hofmann-Wellenhof, B. et al. (2012). *GNSS: GPS, GLONASS, Galileo*. Springer.
5. Guochang, X. (2011). *Science of Geodesy*. Springer.
6. BIG (2013). *Geoid Besar Indonesia — Documentation*.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait matakuliah ini.*
