# Survei GNSS (*GNSS Surveying*)

**Kode:** TKD213505
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Geodesi Satelit, Matematika Geodesi

---

## 1. Overview

GNSS (Global Navigation Satellite System) surveying is the process of using satellite positioning systems to determine the coordinates of points on the Earth's surface with high accuracy. The primary GNSS constellations are:

| System | Country | Satellites (Full) | Frequencies | First Operational |
|--------|---------|-------------------|-------------|-------------------|
| **GPS** | USA | 31 | L1, L2, L5 | 1993 |
| **GLONASS** | Russia | 24 | G1, G2, G3 | 2010 |
| **Galileo** | EU | 26 (planned 30) | E1, E5, E6 | 2016 |
| **BeiDou** | China | 44 (BDS-3) | B1, B2, B3 | 2020 |
| **QZSS** | Japan | 4 (regional) | L1, L2, L5, L6 | 2018 |

---

## 2. GNSS Frequencies and Signals

### 2.1 GPS Frequencies

| Band | Center Frequency | Wavelength | Civilian |
|------|-----------------|------------|----------|
| **L1** | 1575.42 MHz | 19.0 cm | C/A code (+ L1C) |
| **L2** | 1227.60 MHz | 24.4 cm | L2C |
| **L5** | 1176.45 MHz | 25.5 cm | L5 (safety-of-life) |

### 2.2 Ionosphere-Free Linear Combination

The ionosphere-free (IF) combination removes first-order ionospheric delay:

$$\Phi_{IF} = \frac{f_1^2 \cdot \Phi_1 - f_2^2 \cdot \Phi_2}{f_1^2 - f_2^2} $ $

where $ f_1 = 1575.42 $ MHz (L1) and $ f_2 = 1227.60 $ MHz (L2).

### 2.3 Carrier Phase Observable

The carrier phase measurement is

$ $\Phi_i = \rho + c(dt - dT) + \lambda_i N_i - I_i + T_i + \epsilon_i

$ $

where:
-$\rho $= geometric range (distance satellite–receiver)
-$ c $= speed of light
-$ dt $= satellite clock error
-$ dT $= receiver clock error
-$\lambda_i $= wavelength of frequency $ i $-$ N_i $= integer ambiguity
-$ I_i $= ionospheric delay (negative for phase)
-$ T_i $= tropospheric delay
-$\epsilon_i $= multipath and noise

---

## 3. Observation Planning

### 3.1 Factors Affecting GNSS Observations

| Factor | Impact | Mitigation |
|--------|--------|------------|
| **PDOP** (Position Dilution of Precision) | Affects geometry quality | PDOP < 4 recommended |
| **Elevation mask** | Low-elevation signals more noisy | 10°–15° mask |
| **Atmospheric conditions** | Ionosphere and troposphere delays | Dual-frequency, model correction |
| **Multipath** | Signal reflection | Careful site selection |
| **Obstructions** | Building, tree canopy | Site selection, extended observations |
| **Satellite visibility** | Minimum 4 needed (5–8 recommended) | Check almanac |

### 3.2 Observation Planning Tools

- **RTKLIB** — OBS-plan function

- **GAMIT/GLOBK** — Planning module

- **Trimble Planning** — Free web tool

- **HxGN SmartNet** — Commercial planning

### 3.3 Optimal Observation Window

For double-differenced baseline processing:

- **Minimum:** 15 minutes (2.5 km base–rover)

- **Optimal:** 30–60 minutes (10–50 km baseline)

- **Long baseline (>50 km):** 2+ hours

For RTK: typically ≤ 5 minutes per point

### 3.4 Dilution of Precision (DOP)

$ $ ext{PDOP} = \sqrt{\sigma_x^2 + \sigma_y^2 + \sigma_z^2} \; / \; \sigma_0ext{HDOP} = \sqrt{\sigma_x^2 + \sigma_y^2} \; / \; \sigma_0ext{VDOP} = \sigma_z \; / \; \sigma_0ext{TDOP} = \sigma_t \; / \; \sigma_0

$ $

where $\sigma_0 $ is the standard deviation of the unit-weight pseudorange.

---

## 4. Field Procedures

### 4.1 Base Station Setup

#### Monumentation

- **Height:** Above any obstructions

- **Stability:** Concrete pillar or stable tripod with forced centering

- **Clear horizon:** Minimum 10° elevation mask

- **Multipath avoidance:** No reflective surfaces within 50 m

#### Equipment

- Geodetic-grade receiver (dual- or triple-frequency)

- GNSS antenna with ground plane

- Tribrach and tripod

- Tape measure (antenna height, ±1 mm)

- Length measurement to ARP (Antenna Reference Point)

#### Observation

- **Session duration:** 8–24 hours for absolute positioning; 1–2 hours for RTN base

- **Data rate:** 1–30 seconds

- **Elevation mask:** 10°–15°

- **PDOP mask:** < 6

### 4.2 Rover Station Setup

#### Rapid Static

- **Duration:** 15–30 minutes (baseline < 50 km)

- **Post-processing required**

- **Conversion from base:** via differential post-processing

#### Stop-and-Go

- **Static on base:** 10–30 minutes

- **Traverse between points:** 1–5 minutes per point

- **Re-initialization at known point** every 30 minutes

#### RTK (Real-Time Kinematic)

- **Base broadcasts corrections** via radio or NTRIP (RTCM 3.x)

- **Rover receives corrections** in real time

- **Accuracy:** 1–3 cm + 1 ppm

- **Range:** Up to 30 km (UHF radio), unlimited (NTRIP via internet)

#### RTN (Real-Time Network)

- **Network of permanent reference stations**

- **VRS (Virtual Reference Station)** — generates corrections at rover location

- **FKP (Flächenkorrekturparameter)** — area correction parameters

- **MAC (Master-Auxiliary Concept)** — individual station corrections

### 4.3 Observation Log

A proper field log should record:
1. **Station ID** — unique identifier
2. **Date and time** — UTC/local with offset
3. **Receiver/antenna type and serial numbers**
4. **Antenna height** (slant, vertical, or vertical to ARP)
5. **Method** (static, RTK, inverse)
6. **PDOP / # of satellites** during observation
7. **Weather conditions** (temperature, humidity, pressure)
8. **Obstructions** — sky plot sketch
9. **Photos** — 4 cardinal directions (N, S, E, W)

---

## 5. Data Collection

### 5.1 Data Output Formats

| Format | Use |
|--------|-----|
| **RINEX 2.xx / 3.xx** | Standard exchange format for post-processing |
| **RTCM 3.2–3.3** | Real-time correction standard |
| **NMEA 0183** | Low-accuracy navigation output |
| **Receiver native** | Trimble DAT, Leica MDB, Topcon TPS |

### 5.2 RINEX File Components

```
Base: base_20260601_120000.obs (observations)
 base_20260601_120000.nav (navigation)
 base_20260601_120000.gnav (GLONASS almanac)

Rover: rover_20260601_120000.obs
 rover_20260601_120000.nav
```

### 5.3 Data Quality Metrics

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| **Multipath L1** | < 0.25 m | 0.25–0.50 m | > 0.50 m |
| **Multipath L2** | < 0.35 m | 0.35–0.75 m | > 0.75 m |
| **Cycle slip ratio** | > 90% | 80–90% | < 80% |
| **Observation completeness** | > 95% | 85–95% | < 85% |
| **PDOP** | < 3 | 3–5 | > 5 |

Tools: **TEQC (Trimble)** or **gpsqc (RTKLIB)** for quality checks.

---

## 6. Base-Rover Setup Workflow

### 6.1 Differential GNSS (DGNSS)

For pseudorange-based differential positioning

$ $\Delta \rho_{BR} = \rho_B - \rho_R = \Delta X_{BR} + c \cdot \Delta dt + \Delta T + \Delta I + \epsilon

$ $

The common errors (satellite clock, ephemeris, ionosphere, troposphere) are eliminated or strongly reduced when the base–rover baseline is short (< 10 km).

### 6.2 Double-Differenced Solution

The double-difference observation eliminates both receiver and satellite clock errors

$ $\nabla \Delta \Phi_{12}^{ij} = \nabla \Delta \rho_{12}^{ij} + \lambda \cdot \nabla \Delta N_{12}^{ij} + \nabla \Delta \epsilon_{12}^{ij} $ $

where:
-$\nabla \Delta \Phi_{12}^{ij} $= double-differenced phase
-$\nabla \Delta \rho_{12}^{ij} $= double-differenced geometric range
-$\nabla \Delta N_{12}^{ij} $= double-differenced integer ambiguity
-$\nabla \Delta \epsilon_{12}^{ij} $= double-differenced residual error

### 6.3 Ambiguity Resolutio
n

$ $\hat{N} = \frac{\Phi - \rho}{\lambda} $ $

- **Float solution:**$ N $ estimated as real numbers

- **Fixed solution:**$ N $ fixed to integers (LAMBDA method)

- **Ratio test:**$\frac{ext{best}}{ext{2nd best}} > 3.0 $ for reliable fixing

#### LAMBDA Method (Least-squares AMBiguity Decorrelation Adjustment)

The LAMBDA method transforms the ambiguity space to improve search efficiency

$ $\hat{Z} = Z \cdot \hat{N}, \quad Q_{\hat{Z}} = Z \cdot Q_{\hat{N}} \cdot Z^T

$ $

where $ Z $ is an integer-decorrelating transformation matrix.

---

## 7. Post-Processing Software

| Software | Type | Platform |
|----------|------|----------|
| **GAMIT/GLOBK** | Scientific | UNIX/Linux |
| **RTKLib** | Open source | Windows/Linux |
| **Bernese GNSS Software** | Scientific | UNIX/Linux |
| **Trimble Business Center** | Commercial | Windows |
| **Leica Infinity** | Commercial | Windows |
| **Topcon Magnet** | Commercial | Windows |

---

## 8. Indonesian GNSS Infrastructure

### 8.1 BIG's Continuously Operating Reference Station (CORS)

- **INACORS** (Indonesia CORS)

- **Stations:** 150+ across Indonesia

- **Data format:** RTCM 3.2, RINEX 3.03

- **Access:** Free for public use (some restrictions)

- **Coverage:** Most densely populated regions

### 8.2 Nasional Jaring Kontrol Geodesi (SKRGI)

The National Geodetic Control Network (SKRGI = *Seksi Kerangka Referensi Geodesi Indonesia*) provides:

- **Zero-order network:** ~4 stations (Bakosurtanal stations)

- **First-order network:** ~30 stations

- **Second-order network:** ~200 stations

### 8.3 INACORS Access

1. Register at https://inacors.big.go.id
2. Download RINEX data or connect via NTRIP
3. CORS coordinates referenced to ITRF 2014, epoch 2013.0
4. Vertical datum: Geoid model Geoid_Besar_Indonesia

---

## 9. Error Budget

| Error Source | Magnitude (Standalone GPS) | Differential (Short Baseline) |
|-------------|---------------------------|------|
| Satellite orbit | 2–5 m | < 0.01 m |
| Satellite clock | 2–5 m | < 0.01 m |
| Ionosphere | 5–20 m | < 0.05 m |
| Troposphere | 2–5 m | < 0.05 m |
| Multipath | 1–5 m | < 0.5 m |
| Receiver noise | 0.3–1.0 m | < 0.3 m |
| **Total (RMS)** | **5–15 m** | **< 0.05 m** |

---

## 10. Safety Procedures

1. **Sun protection** — use sun hat, SPF 50+, reflective vest
2. **Tripping hazards** — cables should be marked and covered
3. **Lightning** — stop observations during electrical storms
4. **Traffic** — use warning signs when near roads
5. **Hydration** — bring adequate water supply
6. **Communication** — use radio/phone for coordination between base and rover teams

---

## 11. Key Formulas Summary

| Formula | Description |
|---------|-------------|
| $\Phi_i = \rho + c(dt - dT) + \lambda_i N_i - I_i + T_i + \epsilon_i $ | Phase observation equation |
| $\Phi_{IF} = \frac{f_1^2 \Phi_1 - f_2^2 \Phi_2}{f_1^2 - f_2^2} $ | Ionosphere-free combination |
| $\nabla \Delta \Phi_{12}^{ij} = \nabla \Delta \rho_{12}^{ij} + \lambda \nabla \Delta N_{12}^{ij} $ | Double-differenced phase |
| $ h = H + N $ | Height equation |
| $ ext{PDOP} = \sqrt{\frac{\sigma_x^2 + \sigma_y^2 + \sigma_z^2}{\sigma_0^2}} $ | Position DOP |

---

## References

1. Hofmann-Wellenhof, B., Lichtenegger, H. & Wasle, E. (2008). *GNSS — Global Navigation Satellite Systems*. Springer.
2. Leick, A. et al. (2015). *GPS Satellite Surveying*, 4th ed. Wiley.
3. Parkinson, B.W. & Spilker, J.J. (1996). *Global Positioning System: Theory and Applications*. AIAA.
4. BIG (2021). *Pedoman Survei GNSS untuk Jaring Kontrol Geodesi*.
5. Takasu, T. & Yasuda, A. (2009). "RTKLIB: Open Source Program Package for GNSS Positioning." *ION GNSS*.
6. Teunissen, P.J.G. (1995). "The Least-Squares Ambiguity Decorrelation Adjustment." *J. Geodesy*, 70.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*
