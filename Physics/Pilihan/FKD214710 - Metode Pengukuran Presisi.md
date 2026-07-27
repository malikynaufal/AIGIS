---
title: "Metode Pengukuran Presisi"
subject: "Fisika Pilihan"
tags:
 - precision-measurement
 - interferometry
 - calibration
 - uncertainty
 - SKS: 3
---

# FKD214710 — Metode Pengukuran Presisi
**Precision Measurement Methods** | 3 SKS (Satuan Kredit Semester)

## Overview

Precision measurement methods (metode pengukuran presisi) provide the foundation for high-accuracy measurements in physics, engineering, and geodesy. This course covers interferometry (interferometri), calibration techniques (teknik kalibrasi), error analysis (analisis galat), and uncertainty quantification (kuantifikasi ketidakpastian) following the GUM (Guide to the Expression of Uncertainty in Measurement) framework. Students will learn to design measurement experiments, propagate uncertainties, and report results with proper confidence levels.

---

## 1. Interferometry (Interferometri)

### 1.1 Basic Principle

An interferometer splits a coherent beam (e.g., laser) into two paths and recombines them. The interference pattern depends on the optical path difference (OPD, selisih lintasan optik):

$I = I_0 \left[1 + V\cos\left(\frac{2\pi \cdot \text{OPD}}{\lambda}\right)\right] $ where $  V $ is the visibility (visibilitas) of the fringes and $\lambda$ is the wavelength.

### 1.2 Michelson Interferometer

The Michelson interferometer splits a beam at a 50/50 beam splitter. Moving one mirror by distance $d $ produces a path change of $ 2d $:

$ $ \text{OPD} = 2d\cos\thet
a

$ The number of fringes passing a detector point: $  N = \frac{2d}{\lambda} $ $

For a HeNe laser ( $\lambda = 632.8 $ nm), each fringe corresponds to 316.4 nm of mirror displacement.

### 1.3 Applications in Metrology

| Application | Technique | Resolution |
|---|---|---|
| Length standard | Laser interferometry | $ \lambda/1000 \approx 0.6 $ nm |
| Surface profiling | Fizeau interferometer | $ \lambda/20 \approx 30 $ nm |
| Gravitational waves | LIGO (km-scale) | $10^{-19}$  m |
| Geodetic ranging | Two-color EDM | 1 mm + 0.1 ppm |
| Strain measurement | Fiber Bragg grating | $10^{-6}$ strain |

### 1.4 Laser Wavelength Stabilization

Precision interferometry requires a frequency-stabilized laser. The iodine-stabilized HeNe laser serves as a primary length standard

$ $ \lambda_{\text{I}_2} = 632.99121258\;\text{nm} $$

Relative uncertainty: $ \Delta\lambda/\lambda \approx 10^{-11} $.

---

## 2. Error Analysis (Analisis Galat)

### 2.1 Types of Errors

| Error Type (Tipe Galat) | Source (Sumber) | Characterization | Minimization |
|---|---|---|---|
| Systematic (sistematis) | Instrument bias, environment | Known direction | Calibration, correction |
| Random (acak) | Thermal noise, quantization | Gaussian-like | Averaging, longer integration |
| Blunders (kesalahan kasar) | Human error, gross outliers | Large, sporadic | Redundant measurements, checks |

### 2.2 Error Propagation

For a computed quantity $f(x_1, x_2, \ldots, x_n) $ with independent measured variables

$ $ \sigma_f^2 = \sum_{i=1}^{n} \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2

$$

**Example**: Measuring the area of a rectangle $ A = l \cdot w $ with $\sigma_l = 0.1 $ mm and $\sigma_w = 0.2 $ mm $ $

 \frac{\sigma_A}{A} = \sqrt{\left(\frac{\sigma_l}{l}\right)^2 + \left(\frac{\sigma_w}{w}\right)^2} $For $  l = 100.0 $ mm and $  w = 50.0 $ mm $$$

 \sigma_A = A\sqrt{\left(\frac{0.1}{100}\right)^2 + \left(\frac{0.2}{50}\right)^2} = 5000 \times 4.47 \times 10^{-3} = 22.4\;\text{mm}^2

$ $

### 2.3 Outlier Detection

**Grubbs' test**: For a dataset with mean $ \bar{x}$ and standard deviation $  s $:

$ G = \frac{|x_{\text{suspect}} - \bar{x}|}{s} $ Reject if $  G > G_{\alpha, N} $ at significance level $ \alpha $ with $  N $ observations.

**Chauvenet's criterion**: Reject if probability of obtaining the deviation is $< 1/(2N) $.

---

## 3. Calibration Procedures (Prosedur Kalibrasi)

### 3.1 Calibration Chain (Rantai Kalibrasi)

Measurement traceability (jejak pengukuran) requires an unbroken chain of calibrations, each with stated uncertainty, linking to SI units:

$ $ \text{SI unit} \rightarrow \text{National standard (BPN)} \rightarrow \text{Working standard} \rightarrow \text{DUT (device under test)} $$

# ## 3.2 Calibration Methods

**Six Calibration Approaches**:

| Method | When to Use | Uncertainty Budget |
|---|---|---|
| Comparison (perbandingan) | Reference standard available | Reference + repeatability |
| Substitution (substitusi) | High accuracy needed | Reference + switching error |
| Transfer (transfer) | Field calibration | Transfer standard stability |
| Self-calibration (kalibrasi diri) | Interferometers | Internal geometry constraints |
| Ratio (perbandingan) | Ratios of similar quantities | Common-mode rejection |
| Null (nol) | Bridge circuits, balance | Sensitivity limit |

### 3.3 Calibration Interval

The optimal calibration interval $T_c $ balances cost against measurement risk. Methods include:

- **Fixed interval**: Based on historical drift rates

- **Decision-theoretic**: Minimize total cost $C(T) = C_{\text{cal}}/T + C_{\text{risk}} \cdot P(\text{fail by } T) $- **Adaptive**: Adjust interval based on latest calibration results

---

## 4. Uncertainty Quantification (Kuantifikasi Ketidakpastian)

### 4.1 GUM Framework

The GUM (Guide to the Expression of Uncertainty in Measurement, ISO/IEC Guide 98-3) provides a systematic approach:

**Type A evaluation** (from statistical analysis)

$ $

u_A = \frac{s}{\sqrt{N}} = \sqrt{\frac{1}{N(N-1)}\sum_{i=1}^{N}(x_i - \bar{x})^2
}

$$ **Type B evaluation** (from other information):

$ u_B = \frac{a}{\sqrt{3}} \quad \text{(rectangular distribution)}u_B = \frac{a}{\sqrt{6}} \quad \text{(triangular distribution)}u_B = \frac{a}{3} \quad \text{(normal distribution, } k=3\text{)} $$$

# ## 4.2 Combined and Expanded Uncertainty

**Combined standard uncertainty**

$ u_c(y) = \sqrt{\sum_{i} \left(\frac{\partial y}{\partial x_i}\right)^2 u^2(x_i) + 2\sum_{i<j}\frac{\partial y}{\partial x_i}\frac{\partial y}{\partial x_j}u(x_i,x_j)} $ $ **Expanded uncertainty** (95% confidence) $ $ U = k \cdot u_c $ $

where $ k = 2 $ (normal distribution, 95.45% confidence).$

### 4.3 Effective Degrees of Freedom

The Welch–Satterthwaite formula gives the effective degrees of freedom

$ $ \nu_{\text{eff}} = \frac{u_c^4}{\sum_{i} \frac{u_i^4}{\nu_i}} $$

If $ \nu_{\text{eff}} < 30 $, use the Student $  t $-distribution with $  k = t_{0.025, \nu_{\text{eff}}}$.

---

## 5. Worked Example: EDM Calibration

**Problem**: Calibrate an electronic distance measurement (EDM) instrument using a baseline of known length $L_0 = 2000.000 \pm 0.002 $ m.

**Measurements** (10 observations at constant temperature):

| Trial | Measured Distance (m) |
|---|---|
| 1–10 | 2000.0034, 2000.0028, 2000.0041, 2000.0033, 2000.0037 |
| | 2000.0030, 2000.0042, 2000.0035, 2000.0031, 2000.0038 |

**Analysis**:

- Mean: $ \bar{x} = 2000.00349 $  m

- Standard deviation: $s = 0.00044 $  m

- Type A uncertainty: $u_A = s/\sqrt{10} = 0.00014 $  m

- Type B (EDM spec ±1 mm): $u_B = 0.001/\sqrt{3} = 0.00058 $  m

- Combined: $u_c = \sqrt{u_A^2 + u_B^2} = 0.00060 $  m

- Expanded ( $k=2 $): $  U = 0.0012 $ m

- **Bias**: $ \Delta = \bar{x} - L_0 = +3.49 $ mm (statistically significant: $ |\Delta| > U $)

- **Correction needed**: Add $-3.5 \pm 1.2 $ mm to future measurements

---

## References

1. ISO/IEC (2008). *Guide to the Expression of Uncertainty in Measurement* (GUM), JCGM 100:2008.
2. Taylor, B. N., & Kuyatt, C. E. (1994). "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results." NIST Technical Note 1297.
3. Saleh, B. E. A., & Teich, M. C. (2019). *Fundamentals of Photonics*, 3rd ed. Wiley.
4. Rüeger, J. M. (2012). *Electronic Distance Measurement*, 4th ed. Springer.
5. Maul, G. A. (2006). *Introduction to Time Series Analysis and Forecasting*. Springer.
6. BPN-RI (2021). "Standar Nasional Pengukuran: Jejak Metrologi." Badan Pengawasan Mutu Barang, Jakarta.
