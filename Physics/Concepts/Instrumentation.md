---
tags: [aigis, concept, physics, instrumentation, sensors, measurement, uncertainty]
created: 2026-07-27
updated: 2026-07-27
---

# Instrumentation

## Sensors, Transducers, Signal Conditioning, Calibration, and Measurement Uncertainty

**Core Idea:** All physics measurements begin with a transducer converting a physical quantity into an electrical signal, followed by signal conditioning, digitization, and calibration. Understanding the complete measurement chain and its uncertainties is essential for rigorous science and precision geodesy.

---

## 1. Measurement Chain Overview
$$

\text{Physical Quantity} \xrightarrow{\text{Sensor}} \text{Analog Signal} \xrightarrow{\text{Conditioning}} \text{Digital Signal} \xrightarrow{\text{Processing}} \text{Result}$$### Key Blocks
1. **Sensor / Transducer:** Converts physical quantity to electrical signal
2. **Signal Conditioning:** Amplification, filtering, linearization
3. **Analog-to-Digital Conversion (ADC):** Analog → digital quantization
4. **Data Acquisition (DAQ):** Sampling, buffering, timestamping
5. **Calibration / Correction:** Apply model to convert raw reading to physical value
6. **Uncertainty Analysis:** Combine all error sources

---

## 2. Sensors and Transducers

### Transducer Basics$$\text{Sensitivity } S = \frac{\Delta V_{\text{out}}}{\Delta Q_{\text{in}}} \quad [\text{V/unit of quantity}]$$### Sensor Types and Examples

| Type | Principle | Examples | Typical Range |
|------|-----------|----------|---------------|
| **Resistive** | Resistance change with measured quantity | RTD (Pt100), strain gauge | -200°C to 850°C, strain$10^{-6}$|
| **Capacitive** | Capacitance change | Pressure sensor, displacement | 0–100 kHz bandwidth |
| **Inductive** | Inductance change | LVDT displacement | ±1 mm, 0–100 Hz |
| **Piezoelectric** | Charge from mechanical stress | Accelerometer, force transducer | High frequency (>1 kHz) |
| **Optical** | Light intensity/phase change | GNSS antenna, interferometer | GHz bandwidth |
| **Thermocouple** | Seebeck effect | Type K, Type N thermocouple | 0–1300°C |
| **Semiconductor** | Integrated sensing element | MEMS accelerometer, IC temperature | -55 to +150°C |

### Static Characteristics

- **Linearity:** Output proportional to input (deviation = non-linearity error)

- **Hysteresis:** Output depends on history (loading vs unloading)

- **Repeatability:** Same output for repeated identical inputs

- **Resolution:** Smallest detectable change

- **Threshold:** Minimum input for detectable output change

- **Drift:** Slow output change with time at constant input

### Dynamic Characteristics
**First-order sensor:**$$\tau\frac{dy}{dt} + y = K x(t)$$-$\tau$= time constant (response speed)
-$K$= static sensitivity

- Amplitude ratio:$\frac{|Y|}{|X|} = \frac{1}{\sqrt{1+(\omega\tau)^2}}$- Phase lag:$\phi = -\arctan(\omega\tau)$**Second-order sensor:**$$\ddot{y} + 2\zeta\omega_n\dot{y} + \omega_n^2 y = \omega_n^2 K x(t)$$-$\omega_n$= natural frequency
-$\zeta$= damping ratio

---

## 3. Signal Conditioning

### Amplification$$V_{\text{out}} = G \cdot V_{\text{in}}$$- **Instrumentation amplifier:** High CMRR, low drift
  - CMRR = Common-Mode Rejection Ratio
  - Ideal CMRR → ∞ (rejects any signal common to both inputs)
  - Real: 80–120 dB

### Filtering

#### Low-Pass Filter (1st order, RC)$$H(f) = \frac{1}{1 + j(f/f_c)}$$-$f_c = 1/(2\pi RC)$= cutoff frequency

- Attenuation:$-20$dB/decade above$f_c$- **Phase delay:**$\phi = -\arctan(f/f_c)$#### Band-Pass Filter
Series combination of low-pass and high-pass filters.

#### Anti-Aliasing Filter
Must be placed **before** ADC:$$f_{\text{cutoff}} < \frac{f_s}{2}$$where$f_s$= sampling frequency.

### Analog-to-Digital Conversion (ADC)
**Quantization:**$$V_{\text{out}} = \frac{V_{\text{ref}}}{2^N} \cdot \text{code}$$where$N$= number of bits.

**Quantization error:**$\pm \frac{1}{2}$LSB =$\pm \frac{V_{\text{ref}}}{2^{N+1}}$**Quantization noise power:**$$\sigma_q^2 = \frac{\Delta^2}{12}, \quad \Delta = \frac{2V_{\text{ref}}}{2^N}$$| ADC Resolution | LSB (for 0–5 V) | Quantization Noise RMS |
|----------------|------------------|--------------------------|
| 8-bit | 19.5 mV | 5.5 mV |
| 12-bit | 1.22 mV | 0.35 mV |
| 16-bit | 76 μV | 22 μV |
| 24-bit | 2.98 μV | 0.87 μV |

### Multiplexing and Sampling
**Nyquist-Shannon Sampling Theorem:**$$f_s \geq 2 f_{\text{max}}$$If$f_s < 2f_{\text{max}}$: **aliasing** — frequencies fold back into the recorded band.

**Oversampling:** Sampling at $f_s = n \cdot f_{\text{Nyquist}}$improves SNR by$(10/2)\log_{10} n$dB and allows simpler analog filter design.

---

## 4. Calibration

### Calibration Model (Polynomial)$$y_{\text{true}} = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots$$where:
-$x$= raw measurement value
-$y$= calibrated (physical) value
-$c_i$= calibration coefficients

### Two-Point Calibration$$y = (x - x_0) \cdot \frac{y_1 - y_0}{x_1 - x_0} + y_0$$### Multi-Point Calibration

- Measure at known values (calibration standards)

- Fit polynomial via least squares

- Residuals indicate non-linearity

### Calibration Standards
| Standard | Uncertainty | Application |
|----------|-------------|-------------|
| Primary | National metrology institute | kg, m, s realization |
| Secondary | Calibrated from primary | Lab reference |
| Working | Transfer standard | Field calibration |
| Check standard | Monitors drift | Routine checks |

### Traceability
Every measurement should be traceable to SI units through an unbroken chain of calibrations:$$\text{Instrument} \leftarrow \text{Calibration} \leftarrow \text{Primary Standard} \leftarrow \text{Kibble Balance / Atomic Standards}$$### Key Calibration Parameters

- **Span adjustment:** Sensitivity (slope) correction

- **Zero adjustment:** Offset correction

- **Linearity correction:** Polynomial coefficients

- **Temperature compensation:** Correct for sensor drift with ambient temperature

---

## 5. Measurement Uncertainty

### Types of Uncertainty

| Type | Source | Evaluation |
|------|--------|------------|
| **A** (Type 1) | Random, statistical | Standard deviation of repeated measurements |
| **B** (Type 2) | Systematic (calibration, model) | Based on manufacturer specs, published uncertainty budgets |

### Standard Uncertainty
**Type A** (standard deviation of mean):$$u_A = \frac{s}{\sqrt{n}} = \frac{1}{\sqrt{n(n-1)}}\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2}$$**Type B** (estimated bounds):$$u_B = \frac{a}{\sqrt{3}} \quad \text{(uniform distribution)}
$$

$$
u_B = \frac{a}{2} \quad \text{(triangular distribution)}$$where$a$= half-width of bounds.

### Combined Standard Uncertainty$$u_c = \sqrt{\sum_{i=1}^{N} \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)}$$where$f(x_1, \ldots, x_N)$= measurement function.

This is the **law of propagation of uncertainty** (also called GUM — Guide to the Expression of Uncertainty in Measurement).

### Expanded Uncertainty$$U = k \cdot u_c$$where$k$= coverage factor (typically$k = 2$for ~95% confidence level).

### Error Budget Example (GNSS Baseline Measurement)

| Source | Distribution | Magnitude | Contribution |
|--------|-------------|-----------|-------------|
| Satellite clock | Normal | 0.5 ns | ~0.15 m |
| Ephemeris error | Normal | 1 cm | 0.01 m |
| Troposphere (zenith mapping) | Normal | 1 cm | 0.01 m |
| Ionosphere (residual) | Normal | 1 cm | 0.01 m |
| Phase measurement noise | Normal | 0.5 mm | 0.0005 m |
| Multipath | Rectangular | 1 mm | 0.0005 m |
| Baseline geometry | Normal | 0.1 mm | 0.0001 m |
| **Total (combined)** | | | **~0.15 m** |

### Relative Uncertainty$$\text{Relative uncertainty} = \frac{u}{|x|} \times 100\%$$### Resolution-Limited Uncertainty
Instrument resolution$\Delta$contributes:$$u_{\text{res}} = \frac{\Delta}{\sqrt{12}}$$For a digital scale with resolution 1 g:$u_{\text{res}} = 0.29$g

---

## 6. GNSS Instrumentation Specifics

### GNSS Receiver Architecture
1. **Antenna:** Receive satellite signals at L1/L2/L5
2. **RF Front-end:** LNA → Filter → Down-conversion
3. **Correlator:** Code phase tracking, carrier phase measurement
4. **Tracker loops (PLL, DLL):** Phase-locked loop for carrier, delay-locked loop for code
5. **Navigation processor:** Solve for receiver position and time (least squares / Kalman filter)
6. **Output:** Position, velocity, time (PVT solution)

### Key Receiver Specs
| Parameter | Typical Value | Unit |
|-----------|---------------|------|
| Code phase accuracy | 1–2 | m |
| Carrier phase accuracy | 1–2 | mm |
| Horizontal position (static) | 1–3 | mm (post-processed) |
| Vertical position (static) | 2–5 | mm |
| Time accuracy (UTC offset) | 5–50 | ns |
| Sampling rate | 10 Hz – 1 sec | Hz |

### Measurement Noise Models

**Code (pseudorange) measurement noise:**$$\sigma_{P} = \sqrt{\sigma_{\text{iono}}^2 + \sigma_{\text{tropo}}^2 + \sigma_{\text{receiver}}^2}$$**Carrier phase measurement noise:**$$\sigma_{\phi} = \sqrt{\sigma_{\text{thermal}}^2 + \sigma_{\text{noise}}^2}$$Typically:$\sigma_P \approx 1$m (code),$\sigma_\phi \approx 1$mm (phase) for survey-grade receivers.

### Integer Ambiguity Resolution
Carrier phase:$\phi = \frac{\rho}{\lambda} + N + \varepsilon$where$N$= integer number of wavelengths (ambiguity). Resolving$N$correctly → mm accuracy.

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
|$V_{\text{out}} = G \cdot V_{\text{in}}$| Amplification | Signal conditioning |
|$f_s \geq 2f_{\text{max}}$| Nyquist theorem | Sampling rate |
|$\sigma = V_{\text{ref}}/(2^N)$| Quantization step | ADC resolution |
|$u_c = \sqrt{\sum(\partial f/\partial x_i)^2 u^2(x_i)}$| Propagation of uncertainty | Combined uncertainty |
|$U = k \cdot u_c$| Expanded uncertainty | Coverage interval |
|$\tau\frac{dy}{dt} + y = K x$| First-order sensor model | Dynamic response |

---

## Problems
1. A Pt100 RTD has sensitivity 0.385 Ω/°C, measuring 200°C with 0.1°C resolution — what resistance change? What ADC bits needed across 100 Ω range?
2. Design a two-point calibration for a pressure sensor: at 0 Pa → 0 V, at 100 kPa → 4.875 V. What is calibrated voltage for 50 kPa?
3. Compute the Nyquist rate for a GNSS L1 signal (1.575 GHz carrier, 2 MHz bandwidth).
4. A GNSS receiver has code noise 1 m RMS, tropospheric 1 cm, ionospheric residual 1 cm. What is the combined uncertainty?
5. Estimate the standard uncertainty of a digital scale with resolution 0.1 g and rectangular distribution.
6. Derive the uncertainty propagation for$f = \sqrt{x^2 + y^2}$given independent uncertainties$u_x$and$u_y$.
7. Design an anti-aliasing filter for 10 Hz data acquisition: what cutoff frequency? 

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*