---
title: "Standar dan Kalibrasi"
subject: "Fisika Pilihan"
tags:
 - standards
 - calibration
 - ISO
 - metrology
 - SKS: 3
---

# FKD214714 — Standar dan Kalibrasi
**Standards and Calibration** | 3 SKS (Satuan Kredit Semester)

## Overview
Standards and calibration (standar dan kalibrasi) form the backbone of measurement quality assurance (jaminan mutu pengukuran) in physics, engineering, and geodesy. This course covers the international standards framework (ISO, IEC), measurement traceability (jejak pengukuran), calibration laboratory procedures, uncertainty budgets, and quality management systems. Students will learn to implement calibration programs that satisfy ISO/IEC 17025 requirements, ensuring that measurements performed in Indonesian laboratories and field operations are accurate, traceable, and internationally recognized.

---

## 1. The International Standards Framework

### 1.1 SI Units and the Metrological Hierarchy
The International System of Units (SI, Sistem Internasional) defines seven base units:

| Base Unit | Symbol | SI Definition (2019) |
|---|---|---|
| Length (panjang) | m | Speed of light $c = 299\,792\,458 $m/s |
| Mass (massa) | kg | Planck constant $h = 6.626\,070\,15 \times 10^{-34}$J·s |
| Time (waktu) | s | Cesium-133 hyperfine transition: 9,192,631,770 Hz |
| Electric current | A | Elementary charge $e = 1.602\,176\,634 \times 10^{-19}$C |
| Temperature (suhu) | K | Boltzmann constant $k = 1.380\,649 \times 10^{-23}$J/K |
| Amount of substance | mol | Avogadro constant $N_A = 6.022\,140\,76 \times 10^{23}$mol⁻¹ |
| Luminous intensity | cd | Fixed luminous efficacy $K_{cd} = 683 $lm/W |

### 1.2 Traceability Chain (Rantai Jejak)

Measurement traceability (jejak pengukuran) is an unbroken chain of calibrations, each with stated uncertainties:

```
SI Definition (BIPM, France)
 ↓ (key comparison)
National Standard (BPN-RI, Indonesia)
 ↓ (calibration)
Working Standard (Regional lab)
 ↓ (calibration)
Reference Standard (Company lab)
 ↓ (calibration)
Device Under Test (Field instrument)
```

Each link must have a calibration certificate with:

- Measurand (quantity being measured)

- Measured value with uncertainty ($U$, $k = 2$)

- Calibration method used

- Environmental conditions

- Traceability statement

### 1.3 Key Standards Documents

| Standard | Title | Scope (Cakupan) |
|---|---|---|
| ISO/IEC 17025:2017 | General requirements for lab competence | Calibration & testing labs |
| ISO 10012:2003 | Measurement management systems | Organizational measurement |
| ISO/IEC Guide 98-3 (GUM) | Uncertainty in measurement | Uncertainty evaluation |
| ISO 17020:2012 | Conformity assessment — Inspectors | Inspection bodies |
| ISO 17034:2016 | Reference material producers | RM producers |
| VIM (JCGM 200:2012) | International Vocabulary of Metrology | Definitions and terms |

---

## 2. ISO/IEC 17025 — Laboratory Competence

### 2.1 Structure of the Standard
ISO/IEC 17025:2017 organizes requirements into two models:

**General requirements** (persyaratan umum):

- Impartiality (ketidakberpihakan)

- Confidentiality (kerahasiaan)

**Structural requirements** (persyaratan struktural):

- Legal entity, management system, personnel roles

**Resource requirements** (persyaratan sumber daya):

- Personnel competence, facilities, equipment, metrological traceability

**Process requirements** (persyaratan proses):

- Review of requests, selection/validation of methods, sampling, handling of items, technical records, evaluation of measurement uncertainty, reporting, complaints, nonconforming work, data control

**Management system requirements**:

- Document control, internal audits, management reviews

### 2.2 Calibration vs. Testing

| Aspect (Aspek) | Calibration | Testing (Pengujian) |
|---|---|---|
| Purpose (Tujuan) | Determine measurement values | Determine conformity to specifications |
| Output | Measured value + uncertainty | Pass/fail or compliance statement |
| Traceability | Mandatory (to SI) | May or may not require traceability |
| Method | Often defined by standard | May be standard or laboratory-developed |
| Certificate | Calibration certificate | Test report |

### 2.3 Measurement Uncertainty Requirements

17025 requires laboratories to evaluate measurement uncertainty for all calibrations:

**Step-by-step uncertainty evaluation**:

1. **Define the measurand** (quantitas yang diukur)
2. **Identify all input quantities** $x_i$.
3. **Evaluate standard uncertainty** $u(x_i) $for each input (Type A or Type B)
4. **Determine the sensitivity coefficient** $c_i = \partial f / \partial x_i$.
5. **Calculate combined uncertainty** $u_c = \sqrt{\sum c_i^2 u^2(x_i)}$.
6. **Determine expanded uncertainty** $U = k \cdot u_c$.
7. **Report** the result: $y \pm U$ (with $k$ and confidence level)

---

## 3. Calibration Procedures (Prosedur Kalibrasi)

### 3.1 Temperature Calibration

A reference thermometer (termometer referensi) and the DUT (device under test) are compared in a temperature bath (bak suhu) at set points:

**Example**: Calibrating a Pt100 RTD against a standard Pt100

| Set Point (°C) | Reference ($\Omega$) | DUT ($\Omega$) | Deviation (°C) |
|---|---|---|---|
| 0.00 | 100.000 | 100.012 | +0.031 |
| 50.00 | 119.400 | 119.408 | +0.020 |
| 100.00 | 138.505 | 138.510 | +0.013 |
| 150.00 | 157.320 | 157.322 | +0.005 |
| 200.00 | 175.840 | 175.835 | −0.013 |

**Polynomial fit** for correction:

$T_{\text{corrected}} = T_{\text{read}} + a_0 + a_1 T_{\text{read}} + a_2 T_{\text{read}}^2 $Fitting the data:$a_0 = 0.031$, $a_1 = -5.8 \times 10^{-5}$, $a_2 = -2.6 \times 10^{-7}$

**Uncertainty budget** for the 100 °C calibration point:

| Source | Value | Distribution | $u$ (°C) |
|---|---|---|---|
| Reference thermometer | 0.02 °C | Normal ($k=2$) | 0.010 |
| Bath uniformity | 0.03 °C | Rectangular | 0.017 |
| Readout resolution | 0.001 °C | Rectangular | 0.0006 |
| DUT repeatability | 0.005 °C | Type A (N=6) | 0.002 |
| **Combined** | — | — | ** $u_c = 0.020$** |
| **Expanded** ($k=2$) | — | — | ** $U = 0.040$** |

Result: $T = 100.013 \pm 0.040$ °C ($k=2$, 95% confidence)

### 3.2 Length and Distance Calibration

For EDM (Electronic Distance Measurement) instruments, calibration baselines (garis ukur) of known length are used:

| Baseline Length | Calibration Method | Achievable Uncertainty |
|---|---|---|
| 10–100 m | Invar tape comparison | 0.1 mm |
| 100 m – 1 km | Two-color EDM + baseline | 0.5 mm + 0.1 ppm |
| 1–10 km | Trilateration network | 1 mm + 0.5 ppm |
| >10 km | GNSS-controlled network | 2 mm + 1 ppm |

Indonesia's national baseline at the Sentul Calibration Field (Bogor) provides primary standards for EDM calibration, maintained by BPN (Badan Pertanahan Nasional).

### 3.3 Mass Calibration

Mass standards follow a hierarchy:

$$ \text{kg (SI)} \rightarrow \text{E2 weights} \rightarrow \text{F1 weights} \rightarrow \text{F2 weights} \rightarrow \text{Working weights}

$$

| Weight Class | Uncertainty (mg) | Typical Use |
|---|---|---|
| E2 | 0.05–1.0 | Reference standards |
| F1 | 0.15–3.0 | Calibration of M1/F2 weights |
| F2 | 0.5–10 | Calibration of working weights |
| M1 | 5–50 | Industrial calibration |

---

## 4. Quality Assurance in Measurement (Jaminan Mutu Pengukuran)

### 4.1 Quality Control Tools

| Tool (Alat) | Purpose | Application |
|---|---|---|
| Control charts (kartu kendali) | Monitor measurement stability | Daily calibration checks |
| Proficiency testing (uji profisiensi) | Compare with other labs | Annual participation |
| Inter-laboratory comparison | Verify equivalence | Between partner labs |
| Internal audits (audit internal) | Check compliance | Semi-annual |
| Management review | Strategic assessment | Annual |

### 4.2 Control Charts

The $ \bar{x}$ and $R$ charts monitor measurement process stability:

**Center line:** $ \bar{\bar{x}} = \frac{1}{m}\sum_{j=1}^{m}\bar{x}_j$**Upper/Lower control limits:** $$ \text{UCL} = \bar{\bar{x}} + A_2 \bar{R}, \quad \text{LCL} = \bar{\bar{x}} - A_2 \bar{R}

$For subgroup size $n = 5$: $A_2 = 0.577$.$

**Out-of-control signals** (sinyal di luar kendali):

- One point beyond$ \pm 3\sigma$

- 7 consecutive points on one side of center

- 7 consecutive increasing or decreasing points

- Any non-random pattern

### 4.3 Case Study: BPN Geodetic Instrument Calibration Program

Indonesia's BPN (Badan Pertanahan Nasional) operates a calibration program for >5,000 EDM instruments and >2,000 GNSS receivers used in land surveying:

**Program structure**:
1. **Annual calibration**: All instruments calibrated at Sentul baseline or regional calibrators
2. **Traceability**: Linked to BPN primary standards, which are traceable to BIPM via APLMF (Asia Pacific Legal Metrology Forum)
3. **Certificate validity**: 12 months
4. **Non-compliance**: Instrument flagged in SIPTNR database; cannot be used for official surveys
5. **Cost**: Subsidized by government; ~IDR 500,000 (≈35 USD) per EDM calibration

**Impact**: This program ensures that >10 million land parcels (sertifikat tanah) are surveyed with instruments of known accuracy, supporting Indonesia's land registration reform (reformasi agraria).

---

## References

1. ISO/IEC 17025:2017. "General requirements for the competence of testing and calibration laboratories."
2. JCGM 100:2008 (GUM). "Evaluation of measurement data — Guide to the expression of uncertainty in measurement."
3. JCGM 200:2012 (VIM). "International Vocabulary of Metrology — Basic and general concepts."
4. Bell, S. (2007). "A Beginner's Guide to Uncertainty of Measurement." NPL Guide CG-2, UK.
5. BIPM (2019). "The International System of Units (SI)," 9th ed. Bureau International des Poids et Mesures.
6. BPN-RI (2022). "Standar Operasional Prosedur Kalibrasi Instrumen Geodetik." Badan Pertanahan Nasional, Jakarta.