---
tags: [geodesy, study-pack, ITRF, reference-frames, GNSS, frame-transformation, multi-GNSS]
aliases: [Geodetic Reference Frames, Frame Referensi Geodesi]
created: 2026-07-27
---

# Geodetic Reference Frames (Frame Referensi Geodesi)

> **Comprehensive Study Pack** — ITRF realizations, regional densification, frame rotation/translation, and combining GPS/Galileo/GLONASS/BeiDou in modern geodesy.

---

## 📋 Overview

A **geodetic reference frame** is a set of precisely determined coordinates of control points that physically realize a geodetic reference system. The **International Terrestrial Reference Frame (ITRF)** is the global realization of the **International Terrestrial Reference System (ITRS)**, maintained by the IERS.

**Key Indonesian Context**: Indonesia's reference frame is defined through **InaCORS** (Indonesian Continuously Operating Reference Stations) and the national realizations of ITRF, using GNSS densification of the national control network.

---

## 🌐 International Terrestrial Reference System (ITRS) & Frame (ITRF)

### Conceptual Hierarchy
| Level | Name | Definition |
|-------|------|-----------|
| **Terrestrial Reference System (TRS)** | ITRS | Theoretical system: origin at Earth's center of mass (CM), axes fixed to Earth, no rotation relative to distant objects |
| **Terrestrial Reference Frame (TRF)** | **ITRF** | **Realization** of ITRS: precise coordinates + velocities of sites (GNSS stations, SLR stations, VLBI antennas, DORIS beacons) |
| **Frame Realizations** | ITRF2020, ITRF2014, ITRF2008, ... | Specific epoch + set of coordinates/velocities |

### Properties of ITRS
| Property | Definition |
|----------|------------|
| **Origin** | Geocenter (Earth's center of mass, CM) |
| **Scale** | Consistent with relativistic theory (light deflection, time dilation) |
| **Axes** | Co-rotating with Earth; no global rotation relative to celestial frame (no-net-rotation condition) |
| **Orientation** | Constrained by minimal residual rotations relative to ICRF (celestial frame) |
| **Realization** | Coordinates + velocities at a set of fundamental stations |

---

## 📊 ITRF Realizations: Evolution

| Realization | Epoch | Stations | Reference | Key Improvements |
|-------------|-------|----------|-----------|------------------|
| **ITRF88** | 1988 | 150 | VLBI+SLR | First ITRF |
| **ITRF89** | 1989 | 200 | VLBI+SLR+LLR | Improved |
| **ITRF90** | 1990 | 250 | + DORIS | More stations |
| **ITRF91** | 1991 | 300 | + GPS | + GPS technique |
| **ITRF92** | 1992 | 400 | + GPS | Improved GPS |
| **ITRF93** | 1993 | 400 | | Added satellite data |
| **ITRF94** | 1994 | 450 | | Improved models |
| **ITRF96** | 1996 | 500 | | Better error models |
| **ITRF97** | 1997 | 550 | | Improved velocities |
| **ITRF2000** | 2000 | 600 | | Absolute antenna phase centers (IGS00) |
| **ITRF2005** | 2005 | 800 | | Network improvement, local ties |
| **ITRF2008** | 2008 | 900 | | FNEQ approach, better error |
| **ITRF2014** | 2014 | 1000 | | Non-linear motion, co-seismic |
| **ITRF2020** | 2020 | 1100+ | GNSS+SLR+VLBI+DORIS | Improved station coordinates & velocities; co-seismic/post-seismic; better scale & origin |

### ITRF2020 Key Parameters (Epoch 2015.0)

$$\mathbf{X}(t) = \mathbf{X}(t_0) + \dot{\mathbf{X}} \cdot (t - t_0) + \sum_i \mathbf{c}_i H(t_i, t)

$ $

where:
-$\mathbf{X}(t_0) $= coordinates at reference epoch $ t_0 = 2015.0 $-$\dot{\mathbf{X}} $= site velocity (mm/year)
-$\mathbf{c}_i H(t_i, t) $= co-seismic/post-seismic displacement terms (Heaviside functions)

**ITRF2020 vs ITRF2014**:

- ITRF2020: improved scale & origin realization

- ITRF2020: $ a_T = 1.1 \text{ mm} $, $\dot{a}_T = 0.07 \text{ mm/yr} $ (translation drift)

- ITRF2020: $ a_S = 0.07 \text{ ppb} $ (scale bias)

- ITRF2020: $ a_R = 0.10 \text{ mas} $ (rotation drift)

---

## 🔄 Frame Transformation: Helmert / Similarity / Bursa-Wolf

### 14-Parameter Helmert (Seven Parameters + Rates)

Given two ITRF realizations (A → B)

$ $\mathbf{X}_B(t) = \mathbf{X}_A(t) + \mathbf{T} + (1+s)\mathbf{R}\mathbf{X}_A(t) + \dot{\mathbf{T}} \cdot \Delta t + \dot{s} \cdot \Delta t \cdot \mathbf{X}_A(t) + \dot{\mathbf{R}} \cdot \Delta t \cdot \mathbf{X}_A(t)

$$**Parameters** (at reference epoch $ t_0 $):

| Parameter | Symbol | Meaning |
|-----------|--------|---------|
| Translation | $\mathbf{T} = (T_x, T_y, T_z) $ | Origin shift |
| Rotation | $\mathbf{R} = (R_x, R_y, R_z) $ | Axis orientation |
| Scale | $ s $ | Scale factor |
| Translation rates | $\dot{\mathbf{T}} = (\dot{T}_x, \dot{T}_y, \dot{T}_z) $ | Origin drift |
| Rotation rates | $\dot{\mathbf{R}} = (\dot{R}_x, \dot{R}_y, \dot{R}_z) $ | Axis rotation drift |
| Scale rate | $\dot{s} $ | Scale drift |

**14 parameters** = 7 (translation + rotation + scale) + 7 (rates)

### Compact 7-Parameter Form (Bursa-Wolf
)

$ $\begin{pmatrix} X_B \\ Y_B \\ Z_B \end{pmatrix} = \begin{pmatrix} T_x \\ T_y \\ T_z \end{pmatrix} + (1+s) \begin{pmatrix} 1 & -R_z & R_y \\ R_z & 1 & -R_x \\ -R_y & R_x & 1 \end{pmatrix} \begin{pmatrix} X_A \\ Y_A \\ Z_A \end{pmatrix} $$

### ITRF Combination Formula (IERS Standard)
For transformation from ITRF2014 → ITRF2020 (example values from IERS):

| Parameter | Value (mm, ppb, mas) | Rate (mm/yr, ppb/yr, mas/yr) |
|-----------|---------------------|-------------------------------|
| $ T_x $ | $-2.0 $|$-0.1 $ |
| $ T_y $ | $-1.0 $|$ 0.0 $ |
| $ T_z $ | $-3.3 $|$ 0.3 $ |
| $ D $ (scale) | $-0.39 $ ppb |$ 0.07 $ ppb/yr |
| $ R_x $ |$ 0.00 $ mas | $ 0.10 $ mas/yr |
| $ R_y $ |$ 0.00 $ mas | $-0.20 $ mas/yr |
| $ R_z $ |$ 0.00 $ mas | $ 0.00 $ mas/yr |

*(Actual values vary by ITRF pair; check IERS ITRF2020 documentation for exact numbers)*

---

## 🌏 Regional Densification of Reference Frames

### Why Regional Densification?

- ITRF stations are sparse (especially in developing countries)

- Dense local networks (GNSS CORS, geodetic control) needed for surveying

- Regional densification realizes a **regional reference frame** that is consistent with ITRF

### Regional Reference Frames
| Region | Frame | Maintaining Agency | ITRF Basis |
|--------|-------|-------------------|------------|
| **Eropa** | ETRS89 | EUREF | ITRF (frozen, co-moves with Eurafrican plate) |
| **Amerika Utara** | NAD83 (2011, 2012) | NGS | ITRF + plate motion |
| **Amerika Selatan** | SIRGAS | SIRGAS Committee | ITRF |
| **Afrika** | AFREF | AFCET/IERS | ITRF |
| **Australia** | GDA2020 | Geoscience Australia | ITRF2014 |
| **Asia (Kawasan)** | AGRS95 | IAG Regional | ITRF |
| **Indonesia** | **ITRF realization via InaCORS** | **BIG (Badan Informasi Geospasial)** | **ITRF2014/2020** |

### Indonesia: InaCORS Network
| Network | Coverage | Status |
|---------|----------|--------|
| **InaCORS-RTK** | 70+ stations (as of 2024) | Operational |
| **InaCORS-PPP** | Multi-station PPP processing | Operational |
| **IGS (International GNSS Service)** | 1 global station in Indonesia (e.g., NTUS, NTU2) | Operational |
| **National GNSS Control** | ITRF-based densification via PPP & network adjustment | Ongoing |

### Regional Densification Method
1. **Choose ITRF realization** (e.g., ITRF2020)
2. **Determine coordinates** of CORS stations in ITRF via PPP
3. **Densify** with static GNSS (fast static / rapid-static)
4. **Adjust** in ITRF frame using IGS orbits
5. **Transform** to regional system if needed (e.g., TSSGI, local datum)
6. **Monitor** velocity field for secular motion

---

## 🔢 Frame Rotation & Translation (Helmert Transformation in Practice)

### ITRF2014 → ITRF2020 (General Formula
)

$ $\mathbf{X}_{2020}(t) = \mathbf{X}_{2014}(t) + \mathbf{T} + (1+s)\mathbf{R}\mathbf{X}_{2014}(t) + \Delta t\cdot(\dot{\mathbf{T}} + (1+\dot{s})\mathbf{R}\mathbf{X}_{2014}(t) + (1+s)\dot{\mathbf{R}}\mathbf{X}_{2014}(t))

$$

**Practical steps**:
1. Obtain $\mathbf{X}(t_0) $ and $\dot{\mathbf{X}} $ from ITRF2014 solution
2. Apply Helmert 14-parameter transformation
3. Propagate to epoch $ t $ using velocity field

### Scale & Origin Differences (Typical)
| ITRF Pair | Scale Bias (ppb) | Origin Shift (mm) | Rate (mm/yr) |
|-----------|------------------|-------------------|--------------|
| ITRF2008 → ITRF2014 | 0.94 | ~1–2 | ~0.1–0.3 |
| ITRF2014 → ITRF2020 | 0.07 | ~1–3 | ~0.1 |
| WGS84 → ITRF2020 | $< 1 \text{ cm} $|$< 1 \text{ cm} $|$< 1 \text{ mm/yr} $ |

### Practical Implications

- For mm-level surveys: **always use latest ITRF realization**

- For cm-level surveys: WGS84 ≈ ITRF2020 suffices

- For local surveys (mm accuracy): Apply full Helmert transformation

- Always propagate coordinates to survey epoch: $\mathbf{X}(t) = \mathbf{X}(t_0) + \dot{\mathbf{X}}\Delta t $---

## 📡 Multi-GNSS Integration (GPS + Galileo + GLONASS + BeiDou)

### Constellation Comparison

| Constellation | Agency | Satellites | Signal Frequency | Orbit | Ground Track Repeat |
|---------------|--------|------------|------------------|-------|---------------------|
| **GPS (USA)** | USAF/DoD | 31 | L1/L2/L5 | 20,200 km, 55° | ~1 day |
| **GLONASS (Russia)** | VKS/Roscosmos | 24 | L1/L2 (FDMA+CDMA) | 19,100 km, 64.8° | ~8 days |
| **Galileo (EU)** | ESA/EU | 28+ | E1/E5/E6 | 23,222 km, 56° | ~17 days |
| **BeiDou (China)** | CNSA | 35+ (BDS-3) | B1/B2/B3 | MEO+GEO+IGSO | Varies |

### Multi-GNSS Benefits
| Benefit | Explanation |
|---------|-------------|
| **More satellites visible** | $\sim $ 30+ satellites simultaneously (vs. 8–12 GPS only) |
| **Improved geometry (lower DOP)** | Better satellite geometry → lower DOP values |
| **Faster convergence (PPP)** | PPP convergence from 30 min (GPS only) to 10–15 min (multi-GNSS) |
| **Better reliability** | Redundancy for outlier detection |
| **Improved accuracy** | 10–30% improvement in position accuracy |
| **Urban/canyon environments** | More visible satellites in obstructed environments |

### Multi-GNSS Observation Equations

For satellite system $ s $ (GPS, Galileo, GLONASS, BeiDou):

**Pseudorange**

$ $ P^s = \rho^s + c(\delta t_r - \delta t^{s}) + I^s + T^s + \epsilon_P^s $$**Carrier Phase**$ $\Phi^s = \rho^s + c(\delta t_r - \delta t^{s}) - I^s + T^s + \lambda N^s + \epsilon_\Phi^s

$$

**System-specific considerations**:

- **Inter-system bias (ISB)**: $\delta t_r^{\text{GPS}} \neq \delta t_r^{\text{GAL}} \neq \delta t_r^{\text{GLO}} $— must estimate ISB parameters

- **Inter-frequency bias (IFB)**: GLONASS FDMA has different code biases per frequency

- **Antenna phase center variations (PCV)**: Different antenna models (igs14.atx / igs20.atx)

- **Observation weighting**: Weight GPS : Galileo : GLONASS : BeiDou = 1 : 1 : 0.5 : 0.75 (typical)

### PPP Processing with Multi-GNS
S

$ $\text{PPP observation model:} \quad \mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{l} + \epsilon

$$

where $\mathbf{x} $ includes:

- Station coordinates $ (X, Y, Z) $- Zenith wet delay (ZWD)

- Inter-system biases (ISB)

- Ambiguity parameters (integer if ambiguity resolution applied)

### Integer Ambiguity Resolution (AR) in Multi-GNSS

$ $ N_{\text{wide-lane}} = \frac{f_1 N_1 - f_2 N_2}{f_1 - f_2}N_{\text{narrow-lane}} = N_1 + N_{\text{wide-lane}} $$

Modern PPP-AR enables cm-level accuracy with multi-GNSS.

---

## 🇮🇩 Indonesia Reference Frame Implementation

### Current State (2024)
| Component | Status |
|-----------|--------|
| **Primary Frame** | ITRF2014 / ITRF2020 (realized through InaCORS) |
| **InaCORS Stations** | 70+ CORS operated by BIG |
| **PPP Processing Service** | InaCORS-PPP (BIG) — kinematic and static PPP |
| **RTK Service** | InaCORS-RTK — real-time corrections |
| **Network Adjustment** | Jaring Kontrol Geodesi (JKG) — horizontal (SNI 8067) |
| **Geoid Model** | TSSGI Geoid 2020 (for vertical datum) |
| **Coordinate Systems** | ITRF (primary), plus local systems (historical datum, TM3°, UTM) |

### InaCORS Coordinate Processing Workflow
1. **Receive GNSS data** from InaCORS stations (RINEX)
2. **Download precise orbits** (IGS, IGS Final)
3. **PPP processing** (GAMIT/GLOBK, Bernese, or InaCORS-PPP service)
4. **Network adjustment** (if densifying from InaCORS)
5. **Apply ITRF transformation** (to desired realization + epoch)
6. **Apply geoid model** for vertical (TSSGI Geoid 2020)
7. **Output** coordinates in ITRF2020 at epoch of survey

### From ITRF to Local Surveys (Indonesia)

$ $ \mathbf{X}_{\text{ITRF2020}}(t) = \mathbf{X}_{\text{ITRF2014}}(t_0) + \dot{\mathbf{X}}(t - t_0) + \Delta_{\text{Helmert}}H_{\text{TSSGI}} = h_{\text{ITRF2020}} - N_{\text{TSSGI}} $$---

## 📐 Practical Formulas Summary

| Task | Formula/Method |
|------|----------------|
| **ITRF velocity propagation** | $\mathbf{X}(t) = \mathbf{X}(t_0) + \dot{\mathbf{X}} \cdot (t - t_0) $ |
| **Helmert 7-param (Bursa-Wolf)** | $\mathbf{X}_B = \mathbf{T} + (1+s)\mathbf{R}\mathbf{X}_A $ |
| **Helmert 14-param (ITRF)** | Add rates: $\dot{\mathbf{T}}, \dot{s}, \dot{\mathbf{R}} $ |
| **DOP (Geometric)** | $ DOP = \sqrt{tr((\mathbf{A}^T\mathbf{A})^{-1})} $ |
| **PPP position** | $\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{P}\mathbf{A})^{-1}\mathbf{A}^T\mathbf{P}\mathbf{l} $ |
| **Ambiguity resolution** | $ N_{WL} = \frac{f_1 N_1 - f_2 N_2}{f_1 - f_2} $ |
| **Co-seismic displacement** | Heaviside function $ H(t_i, t) $ at earthquake epoch $ t_i$ |

---

## 🛠️ Practical Applications

| Application | How Reference Frames are Used |
|-------------|-------------------------------|
| **Precise GNSS Surveying** | ITRF coordinates → base line vectors → adjusted coordinates |
| **PPP Surveying** | Precise orbits + ITRF → mm-cm positions |
| **RTK Surveying** | ITRF-based reference station network → RTK corrections |
| **Plate Tectonics Monitoring** | ITRF velocity field → plate motion vectors |
| **Coseismic Deformation** | ITRF coordinates before/after earthquake → displacement |
| **Sea Level Monitoring** | ITRF-referenced altimetry → geocentric sea level |
| **Satellite Orbit Determination** | ITRF stations as tracking network |
| **Construction / Monitoring** | ITRF → local frame → deformation reference |
| **Boundary Delineation** | National boundaries in ITRF/TM3/UTM |
| **Cadastral Surveying** | ITRF → local coordinate transformation |

---

## 🔗 Related Notes

- [[ITRF]] — Core concept of terrestrial reference frames

- [[ITRF2020]] — Latest ITRF realization

- [[WGS84]] — GPS system frame (≈ ITRF2020)

- [[ETRS89]] — European regional frame

- [[NAD83]] — North American frame

- [[Datum Transformation]] — General datum transformation theory

- [[Helmert Transformation]] — Mathematical frame transformation

- [[GNSS]] — GNSS positioning and reference frames

- [[PPP]] — Precise Point Positioning in ITRF

- [[RTK]] — Real-Time Kinematic in reference frame context

- [[Indonesia]] — InaCORS, TSSGI, national reference

- [[Vertical Datum]] — TSSGI, height reference

---

## 📚 References

### ITRF / Reference Frames
1. **Altamimi, Z. et al.**, *ITRF2020: A new realization of the International Terrestrial Reference Frame*, Journal of Geodesy, 97, 117, 2023.
2. **Altamimi, Z. et al.**, *ITRF2014: A new release of the International Terrestrial Reference Frame*, J. Geod., 90, 613–629, 2016.
3. **IERS**, *ITRF2020 Reference Frame Information*, IERS Technical Notes, 2023.
4. **IERS**, *Conventions (2010/2024)*, IERS Technical Notes, Ch. 4.
5. **Boucher, C. & Altamimi, Z.**, *Memo: Specifications for reference frame fixing in the analysis of a EUREF GPS campaign*, EUREF, 2010.

### Multi-GNSS
6. **Montenbruck, J., Steigenberger, P. et al.**, *Multi-GNSS Processing*, various publications.
7. **Rizos, C. & Montenbruck, O.**, *Introduction to GNSS: Multi-constellation positioning*, J. Geod., 2019.
8. **Li, X. et al.**, *Multi-GNSS precise point positioning*, J. Geod., 2015.
9. **Teunissen, P.J.G. & Montenbruck, O.** (eds.), *Springer Handbook of GNSS*, Springer, 2017.

### PPP & IGS
10. **Kouba, J. & Héroux, P.**, *GPS Precise Point Positioning using IGS orbit products*, GPS Solutions, 2001.
11. **Zumberge, J. et al.**, *Precise point positioning for the efficient and robust analysis of GPS data from large networks*, J. Geophys. Res., 1997.
12. **IGS**, *IGS Technical Reports* — IGS08, IGS14, IGS20 antenna phase center models.
13. **Ghoddousi-Fard, R. & Langley, R.B.**, *Multi-GNSS data processing*, GPS Solutions, 2020.

### Indonesia
14. **BIG**, *Pedoman Teknis Jaring Kontrol Geodesi (JKG)*, SNI 8067:2014.
15. **BIG**, *InaCORS Network Status and Processing Guidelines*.
16. **Suhartadi et al.**, *Indonesian CORS network for geodetic reference*, various.
17. **Prijatna et al.**, *Implementation of ITRF in Indonesian geodetic surveys*, various.

---

#study-pack #geodetic-reference-frames #ITRF #reference-frame #multi-GNSS #regional-densification #frame-transformation #Indonesia #InaCORS