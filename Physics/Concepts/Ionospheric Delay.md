---
tags: [aigis, concept, physics, electromagnetism, gnss, ionosphere]
created: 2026-07-26
updated: 2026-07-27
---

# Ionospheric Delay

## The Physics of EM Wave Propagation in the Ionosphere

**Core Idea:** The ionosphere (60–1000 km) is a dispersive, ionized plasma that affects GNSS signals. The frequency-dependent delay is the largest single error source for single-frequency positioning — and understanding its models is essential for high-precision geodesy.

---

## 1. Ionospheric Physics

### Structure of the Ionosphere
| Layer | Altitude (km) | Max $N_e $ (m⁻³) | Ionizing Source |
|-------|---------------|------------------|-----------------|
| D | 60–90 | $ 10^8 $–$ 10^{10} $ | X-ray absorption |
| E | 90–150 | $ 10^{11} $ | EUV, particle precipitation |
| F₁ | 150–200 | $ 10^{11} $–$ 10^{12} $ | EUV |
| F₂ | 200–400 | $ 5\times 10^{11} $–$ 2\times 10^{12} $ | EUV (dominant F layer) |

### Plasma Frequency (Critical Frequency
)

$ f_p = \frac{1}{2\pi}\sqrt{\frac{N_e e^2}{m_e \epsilon_0}} = 9\sqrt{N_e} \text{ Hz} $ where $ N_e $ is electron density in m⁻³.

- At $ N_e = 10^{12} $ m⁻³: $ f_p \approx 9 $ MHz

- GNSS signals (L-band) at ~1.5 GHz pass through without reflection, but are delayed.

### Key Parameter: Total Electron Content (TEC
)

$ $ \text{TEC} = \int_{\text{path}} N_e(s) \, ds \quad [\text{electrons/m}^2]

$$

- 1 TECU =$ 10^{16} $ electrons/m²

- Typical values: 1–300 TECU (depends on solar cycle, latitude, local time)

---

## 2. Dispersion Relation — Cold Plasma Model

Starting from the equation of motion for electrons in the ionosphere (ignoring collisions, ion motion):

**Electron equation of motion:*
*

$ m_e \frac{d\vec{v}}{dt} = -e\vec{E} - e\vec{v}\times\vec{B} $$$

**Applying Maxwell's equations:*
*

$ $ \nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}, \quad \nabla\times\vec{B} = \mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t} + \mu_0\vec{J} $$

**Resulting dispersion relation (Appleton-Hartree):*
*

$ $ n^2 = 1 - \frac{X}{1 - \frac{Y_T}{2} \pm \sqrt{Y_T^2/4 + X^2}} $$

where:
- $ X = \left(\frac{f_p}{f}\right)^2 = \frac{\omega_p^2}{\omega^2} = \frac{N_e e^2}{m_e \epsilon_0 \omega^2} $- $  Y = \frac{f_c}{f} = \frac{eB_0}{m_e \omega} $- $ f_c $ = cyclotron frequency ≈ 1.4 MHz at Earth's surface (varies with $  B $)

- $+$ for R-wave (right-hand),$-$ for L-wave (left-hand)

### Limiting Case: $ B = 0 $ (No Magnetic Field)

$ $ n^2 = 1 - \frac{f_p^2}{f^2} $$

This is the **cold plasma approximation** used for first-order GNSS calculations.

---

## 3. Refractive Index and Phase/Group Velocity

### First-Order Refractive Index ( $ B=0 $)

$ $ 

n = \sqrt{1 - \frac{f_p^2}{f^2}} \approx 1 - \frac{f_p^2}{2f^2} \quad \text{(for } f \gg f_p\text{)
}

**### Phase Velocity vs Group Velocity **

v_p = \frac{c}{n} > c \quad \text{(phase leads — superluminal)}v_g = c \cdot n < c \quad \text{(group — signals travel at this speed)
}

**Inverse relationship:**

v_p \cdot v_g = c^2 $$

# ## Why Code Is Delayed But Phase Is Advanced

- The **carrier phase** propagates at $ v_p = c/n $; since $  n < 1 $, the phase front moves faster than $  c $→ carrier phase is **advanced** relative to vacuum.

- The **modulation/code** travels at $ v_g = cn $; since $  n < 1 $, code information lags → code pseudorange is **delayed** relative to vacuum.

- Both effects stem from the same plasma, but one gives "advance" and the other "delay."

---

## 4. First-Order Ionospheric Delay

### Code (Pseudorange) Delay
The first-order ionospheric range delay:

$ $ \Delta_{\text{ion}} = \frac{40.3}{f^2} \cdot \text{TEC} \quad [\text{meters}]

$$

where:
-$ f $ = signal frequency in Hz

- TEC = Total Electron Content along slant path, in electrons/m² (divide by $ 10^{16} $ to get TECU, then multiply by $ 40.3 \times 10^{16} $ TECU⁻¹ m³/s²)

**Detailed derivation:**

The excess phase path is

$ $ \Delta\phi = \omega\left(\frac{1}{v_g} - \frac{1}{c}\right) \cdot \text{path} = -\omega(1-n) \int \frac{ds}{c} $$

Converting to range $ $  I = -\lambda \frac{\Delta\phi}{2\pi} = \frac{40.3}{f^2} \int N_e \, ds = \frac{40.3}{f^2}\text{TEC} $$

# ## Delay Per TECU at GNSS Frequencies

| Frequency | Band | Wavelength | Delay per TECU |
|-----------|------|------------|----------------|
| 1575.42 MHz | L1 | 19.05 cm | 0.162 m |
| 1227.60 MHz | L2 | 24.42 cm | 0.267 m |
| 1176.45 MHz | L5 | 25.48 cm | 0.291 m |
| 1207.14 MHz | E5a | 24.85 cm | 0.277 m |
| 1191.795 MHz | E5b | 25.17 cm | 0.287 m |

### Frequency Dependence
The delay scales as $ 1/f^2 $:

$ $ \frac{I_{\text{L1}}}{I_{\text{L2}}} = \left(\frac{f_2}{f_1}\right)^2 \approx \left(\frac{1228}{1575}\right)^2 \approx 0.606

$$

This means L1 delay is ~1.65× the L2 delay for the same TEC.

---

## 5. Dual-Frequency Ionosphere-Free Combination

Using two frequencies, the ionospheric delay cancels:

### Code Combinatio
n

$ P_{\text{IF}} = \frac{f_1^2 P_1 - f_2^2 P_2}{f_1^2 - f_2^2} $$$

# ## Phase Combinatio
n

$ $ \phi_{\text{IF}} = \frac{f_1^2 \phi_1 - f_2^2 \phi_2}{f_1^2 - f_2^2} $$

# ## Residual Error

- Higher-order terms: ~1–2% of TEC

- Ray bending: neglected in first-order; ~1 mm at low elevation angles

- Typical residual: **0.5–1 cm** for dual-frequency processing (after first-order removal)

### Derivation of TEC from Dual-Frequency Observations
From code measurements at L1 and L2

$ $ P_1 = \rho + \frac{40.3}{f_1^2}\text{TEC} + \varepsilon_1, \quad P_2 = \rho + \frac{40.3}{f_2^2}\text{TEC} + \varepsilon_
2

$ Taking the combination: $$$

P_2 - P_1 = 40.3 \cdot \text{TEC}\cdot\frac{f_1^2 - f_2^2}{f_1^2 f_2^2}\text{TEC} = \frac{f_1^2 f_2^2}{40.3(f_1^2 - f_2^2)}(P_2 - P_1
)

$ Or in normalized form: $ $ \text{TEC} = \frac{\lambda_1^2\lambda_2^2}{40.3\times 4\pi^2}(\phi_1 - \phi_2) \quad \text{(from phase, noisier)} $

$$ ---

## 6. Higher-Order Ionospheric Effects

### Magnetic Field: $ f_p $ vs $ f_c $
When the Earth's magnetic field ( $ B_0 \approx 50 \,\mu $ T) is included:

$ n_{\pm}^2 = 1 - X \pm \frac{XY}{2} $ where $  Y = f_c/f $. The $+ $ and $-$ correspond to left- and right-hand circular polarization. The difference between the two polarizations is the **Faraday rotation**.

### Second-Order Correction (Geomagnetic
)

$ $ \Delta_{\text{ion}}^{(2)} \approx -\frac{7527}{f^3} \int N_e B_{\parallel} \, ds

$$

**Magnitude (GPS L1):**

- Mid-latitudes: 1–2 cm RMS

- Low latitudes (equatorial anomaly): up to 5 cm

- Nighttime: negligible

### Third-Orde
r

$ $ \Delta_{\text{ion}}^{(3)} \propto \frac{1}{f^4} $$

Negligible (<1 mm for all GNSS applications).

### Faraday Rotation

$ $ \Omega_F = \frac{e^3}{2\epsilon_0 m_e^2 c^2}\int N_e B_{\parallel} \frac{ds}{f^2} $$

- Significant for L-band at low elevation angles

- Affects polarization-sensitive receivers (L-band antennas)

- For standard GNSS: usually not a first-order concern

### Ray Bending
The signal path is not straight in a refracting medium. Lateral gradient of TEC causes ray bending. Magnitude:

- Zenith: 0 (straight)

- Low elevation (< 5°): cm-scale position offset

- Handled in precise processing (ray-tracing through ionospheric model)

---

## 7. Ionospheric Models

### Broadcast Models (Real-Time)
| Model | Agency | Parameters | Accuracy | Notes |
|-------|--------|-----------|----------|-------|
| **Klobuchar** (GPS) | US Space Force | 8 coefficients | ~50% removal → 2–10 m residual | In NAV message |
| **NeQuick 2** (Galileo) | ESA/ASGS | 5 parameters | ~60% removal → 1–5 m residual | In navigation message |
| **Klobuchar GIM** | Multi-GNSS | 8 Coefficients | ~50% | Used by BeiDou/GLONASS as well |

### Ionospheric Maps (Real-Time, IGS)
| Product | Provider | Resolution | Latency | TEC Accuracy |
|---------|----------|------------|---------|-------------|
| **IGS GIM** | IGS Center | 5°×2.5°/2 h | ~8 days (rapid) | 1–3 mm in range |
| **CODE GIM** | CODE, Bern | 5°×2.5°/2 h | Real-time/rapid | 2–5 TECU |
| **IGS Ultra-Rapid GIM** | Various | 5°×2.5°/15 min | ~4 h | Real-time |

### Empirical Models (Climatological)

**International Reference Ionosphere (IRI)**

- Empirical, based on decades of measurements

- Covers 100–2000 km altitude

- Inputs: latitude, longitude, day-of-year, UT, solar activity ( $ F_{10.7} $)

- Outputs: $ N_e(h) $ profile, TEC, $ f_oF2 $, $ M(3000)F2 $, foF2 etc.

**International Reference Ionosphere Model (IRI)**

$ N_e(h) = \sum_i A_i(h) \exp\left[ -\frac{(h-h_{mi})^2}{2\Delta h_i^2}\right] $$$

Peaks at D, E, and F layer altitudes.

### Physics-Based Models

**International Ionospheric Model (TIEGCM)**

- First-principles thermosphere-ionosphere model

- Driven by solar EUV flux, geomagnetic indices, meteorological data

- Resolves dynamics, composition, electrodynamics

- Computationally expensive; not real-time

### Regional Models

- **BKG (Germany)**: European ionosphere map

- **UNSW (Australia)**: Regional for Asia-Pacific

- **CODG (CODE Bern)**: Global

- **RTG (JPL)**: Real-Time Global Ionosphere Map

---

## 8. Practical Implications for Geodesy

### Single-Frequency (L1-Only)

- Klobuchar correction removes ~50% of ionospheric delay

- Residual: **5–15 m** typical, up to **30+ m** at equator during geomagnetic storms

- Not acceptable for cm-level surveying

- Used in single-frequency consumer equipment only

### Dual-Frequency (L1/L2 or L1/L5)

- Ionosphere-free combination removes first-order (→ residual <1% of TEC)

- Standard for RTK, PPK, PPP

- Baseline length limit (RTK): ~10–15 km (common-mode decorrelation)

### PPP (Precise Point Positioning)

- Ionosphere-free combination required for single-receiver processing

- Requires external ionospheric products for convergence speed

- With IGS GIM: convergence in ~30 min → 1 cm (horizontal)

- Without: convergence slower (hours)

### RTK (Real-Time Kinematic)

- Base-rover differencing at short baselines (<10 km) cancels first-order ionosphere

- **Extended Kalman filter/RTK solver must handle ambiguity resolution** after ionosphere removal

- Network RTK (VRS, FKP, MAC) — ionospheric gradients modeled via reference network

### Ionospheric Storm Effects
During major geomagnetic storms:

- TEC can vary by ±50% in hours

- Spatial gradients increase (scintillation)

- Klobuchar model fails (designed for quiet conditions)

- **Solution:** Use dual-frequency + external ionosphere products (GIM), avoid single-frequency during storms

---

## 9. Ionospheric Scintillation

### What is Scintillation?
Rapid fluctuations in signal amplitude and phase caused by small-scale irregularities in electron density ( $\delta N_e/N_e \sim 0.1 $–1 at scales ~100 m).

### Occurrence

- Primarily along magnetic equator (equatorial ionization anomaly, EIA)

- Post-sunset, L-band scintillation peaks between 21:00–03:00 local time

- High-Latitude (auroral oval) also affected, especially geomagnetic storms

### Impact on GNSS

- Loss of lock: receiver loses carrier tracking

- Cycle slips in phase measurements

- Increased noise in code and phase observables

- Can corrupt PPP and RTK solutions

---

## 10. Key Formulas to Memorize

| Formula | Description |
|---------|-------------|
| $ \Delta_{\text{ion}} = \frac{40.3}{f^2}\text{TEC} $ | First-order delay (code) |
| $ n^2 = 1 - \frac{f_p^2}{f^2} $ | Cold plasma refractive index |
| $ v_g = cn $, $ v_p = c/n $ | Group and phase velocities |
| $ P_{\text{IF}} = \frac{f_1^2 P_1 - f_2^2 P_2}{f_1^2 - f_2^2} $ | Iono-free code combination |
| $ \text{TEC} = \frac{f_1^2 f_2^2}{40.3(f_1^2 - f_2^2)}(P_2 - P_1) $ | TEC from dual-frequency |
| $ \Delta_{\text{ion}}^{(2)} \propto \frac{1}{f^3}\int N_e B_\parallel\,ds $ | Second-order (geomagnetic) |
| $ \Omega_F \propto \frac{1}{f^2}\int N_e B_\parallel\,ds $ | Faraday rotation |

---

## 11. Typical TEC and Delay Values

| Condition | TEC (TECU) | L1 Delay (m) | L2 Delay (m) | L1-L2 Delay (m) |
|-----------|------------|---------------|---------------|------------------|
| Night mid-lat | 2–10 | 0.3–1.6 | 0.5–2.6 | 0.2–1.0 |
| Day mid-lat | 10–50 | 1.6–8 | 2.6–13 | 1.0–5.4 |
| Day equatorial | 50–150 | 8–24 | 13–39 | 5.4–13.5 |
| Solar max peak | 150–200 | 24–32 | 39–52 | 14–20 |
| Solar min | 10–30% less | — | — | — |

---

## Problems
1. Compute the first-order ionospheric delay at L1 for TEC = 100 TECU at the equator.
2. Derive the ionosphere-free combination from $ P_1 $, $ P_2 $, $ f_1 $, $ f_2 $ (first principles).
3. Calculate TEC from $ P_1 = 21,500,000 $ m, $ P_2 = 21,503,000 $  m at L1/L2.
4. Explain why phase advances while code is delayed — trace the physics from plasma frequency.
5. Estimate the second-order correction for L1 at mid-latitudes (assume $ B_\parallel = 40 \,\mu $ T, $ N_e = 10^{12}$ m⁻³, path 350 km).
6. Compare Klobuchar vs. IGS GIM performance: explain the 50% removal limitation of Klobuchar.
7. Describe the physical origin of equatorial scintillation and its impact on PPP convergence.

---

*Concept maintained by AIGIS — part of [[Physics MOC]] → [[Geodesi Satelit / GNSS]]*