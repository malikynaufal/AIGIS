---
title: "Sensor dan Aktuator"
subject: "Fisika Pilihan"
tags:
 - sensors
 - actuators
 - microcontrollers
 - calibration
 - SKS: 3
---

# FKD214706 — Sensor dan Aktuator
**Sensors and Actuators** | 3 SKS (Satuan Kredit Semester)

## Overview

Sensors (sensor) and actuators (aktuator) form the critical interface between physical phenomena and digital systems. This course covers the operating principles, performance characteristics, calibration procedures, and microcontroller interfacing of transducers used in geophysical instrumentation, environmental monitoring, and industrial automation. Students will learn to select, calibrate, and integrate sensors into embedded measurement systems, with emphasis on understanding noise, resolution, and uncertainty.

---

## 1. Fundamental Sensor Characteristics (Karakteristik Sensor)

### 1.1 Static Characteristics

The relationship between input (stimulus) $x $ and output (response) $ y$ is characterized by:

**Sensitivity** (sensitivitas): Rate of change of output with respect to input

$S = \frac{\partial y}{\partial x} \bigg|_{x_0} $ Example: A thermocouple with $  S = 41\;\mu\text{V/°C} $ produces 41 μV per degree change.

**Linearity** (linearitas): Maximum deviation from ideal linear response

$ $ \text{Linearity} = \frac{\max|y_i - (mx_i + b)|}{y_{\text{FS}}} \times 100\% $$

**Hysteresis** (histeresis): Difference in output for increasing vs. decreasing input $ $  H = \frac{\max|y_{\uparrow}(x) - y_{\downarrow}(x)|}{y_{\text{FS}}} \times 100\% $$

# ## 1.2 Dynamic Characteristics

A sensor's response to time-varying inputs is modeled as a differential equation. First-order sensor

$ $ \tau \frac{dy}{dt} + y = K \cdot x(t)

$ where $\tau $ is the time constant (konstanta waktu) and $  K $ is the steady-state gain. For a step input $ x(t) = u_0 \cdot u(t) $:

$ $ y(t) = K u_0 \left(1 - e^{-t/\tau}\right) $ $ A sensor reaches 99% of final value at $ $  t = 5\tau $.

Second-order sensor (model umum):

$$ \frac{1}{\omega_n^2}\ddot{y} + \frac{2\zeta}{\omega_n}\dot{y} + y = K \cdot x(t)

$ where $\omega_n $ is the natural frequency (frekuensi alami) and $\zeta$ is the damping ratio (rasio redaman).

---

## 2. Sensor Types (Jenis Sensor)

### 2.1 Overview Table

| Sensor Type | Principle (Prinsip) | Range | Resolution | Application |
|---|---|---|---|---|
| Thermocouple | Seebeck effect | −270 to 2300 °C | 0.1 °C | Volcanic monitoring |
| RTD (Pt100) | Resistance vs. temperature | −200 to 850 °C | 0.01 °C | Precision thermometry |
| LVDT | Mutual inductance | ±0.5 to ±250 mm | 0.1 μm | Displacement |
| Accelerometer (MEMS) | Capacitive/piezoelectric | ±2 to ±400 g | 1 mg | Vibration, seismic |
| Pressure sensor | Piezoresistive/capacitive | 0–1000 bar | 0.01% FS | Downhole, ocean |
| Flow meter (MASS) | Coriolis force | 0.1–5000 kg/h | 0.1% | Geothermal |
| GPS receiver | Code/carrier phase | Global | 2 mm (carrier) | Deformation |

### 2.2 Piezoelectric Sensors

The piezoelectric effect (efek piezoelektrik) generates charge $q $ proportional to applied force $  F $:

$ q = d \cdot F $ where $  d $ is the piezoelectric constant (typically 2–500 pC/N). The open-circuit voltage $  V = \frac{q}{C_p} = \frac{d \cdot F}{C_p} $ where $ C_p $ is the sensor capacitance. Piezoelectric sensors cannot measure DC signals due to charge leakage through $ R_p $:

$ $ V(t) = V_0 e^{-t/(R_p C_p)} $$

The low-frequency cutoff: $ $ f_{\text{low}} = 1/(2\pi R_p C_p) $. For seismic sensors, charge amplifiers extend this to very low frequencies.

### 2.3 MEMS Accelerometers

MEMS (Micro-Electro-Mechanical Systems) accelerometers use a suspended proof mass with capacitive sensing:

$$ \Delta C = C_0 \frac{\Delta x}{d_0
}

$ Sensitivity depends on mass-spring design: $ $ \Delta x = \frac{ma}{k} = \frac{a}{\omega_n^2}

$$

Modern MEMS accelerometers (e.g., Analog Devices ADXL355) achieve:

- Noise density: $ 25\;\mu g/\sqrt{\text{Hz}} $- Bias stability: $ 0.25\;\text{mg} $ over temperature

- Bandwidth: DC to 1.5 kHz

---

## 3. Noise in Sensors (Noise pada Sensor)

### 3.1 Fundamental Noise Sources

**Thermal (Johnson–Nyquist) noise**

$V_n = \sqrt{4 k_B T R \Delta f} $ where $ k_B = 1.38 \times 10^{-23} $ J/K, $  T $ is temperature (K), $  R $ is resistance (Ω), and $\Delta f $ is bandwidth (Hz).

**Shot noise** (noise tembakan)

$i_n = \sqrt{2 e I \Delta f} $ where $  e = 1.6 \times 10^{-19} $ C and $  I $ is the average current.

**1/$ f $ (flicker) noise** (noise kedip)

$ V_{1/f}^2 = \frac{K_f}{f^n} \Delta f, \quad n \approx 1 $ $

### 3.2 Signal-to-Noise Rati
o

$$ \text{SNR} = 10\log_{10}\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right) \;\text{dB} $ $

### 3.3 Noise Figure and Equivalent Input Noise

The noise figure (NF) quantifies degradation by a signal chain

$$ \text{NF} = 10\log_{10}(F), \quad F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} $ $

For cascaded stages, the Friis formula $$ F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots $ $

This shows the first stage dominates the system noise — the rationale for low-noise amplifiers (LNA) as the front end.

---

## 4. Calibration (Kalibrasi)

### 4.1 Calibration Methods

**Comparison method**: Compare sensor output against a reference standard under controlled conditions
.

$y = a_0 + a_1 x + a_2 x^2 + \cdots + \epsilon $ Calibration coefficients $ a_i $ determined by least-squares regression.

**Substitution method**: Replace the DUT (device under test) with a calibrated standard and compare readings.

**Null method**: Adjust a known reference until the output reads zero — used in bridge circuits and potentiometers.

### 4.2 Calibration Uncertainty

The combined standard uncertainty from calibration

$u_c = \sqrt{u_{\text{ref}}^2 + u_{\text{repeatability}}^2 + u_{\text{hysteresis}}^2 + u_{\text{environment}}^2} $ Expanded uncertainty at 95% confidence: $  U = k \cdot u_c $ where $  k = 2 $ for normal distribution.

---

## 5. Microcontroller Interfacing (Antarmuka Mikrokontroler)

### 5.1 ADC Considerations

The ADC resolution (resolusi ADC) determines the minimum detectable signal change

$ $ \text{LSB} = \frac{V_{\text{ref}}}{2^n} $$

For a 12-bit ADC with $ V_{\text{ref}} = 3.3 $ V: LSB = 0.81 mV.

| Microcontroller | ADC Bits | Sample Rate | Interface |
|---|---|---|---|
| Arduino Uno (ATmega328) | 10-bit | 15 ksps | I²C, SPI, UART |
| STM32F407 | 12-bit | 2.4 Msps | SPI, I²C, CAN |
| ESP32 | 12-bit | 100 ksps | I²C, SPI, Wi-Fi |
| Teensy 4.1 (NXP i.MX RT1062) | 12-bit | 1 Msps | SPI, I²C, USB |

### 5.2 Case Study: Volcano Tiltmeter Network

A tiltmeter (inklinometer) network on Mount Merapi uses MEMS accelerometers (Analog Devices ADXL345,$ \pm 3 $  g range, 13-bit resolution) interfaced with ESP32 microcontrollers. Each station:

- Samples at 10 Hz with 12-bit oversampling (effective 16-bit)

- Transmits via LoRa (Long Range) radio at 900 MHz

- Battery life: >6 months with solar panel recharge

- Accuracy: 1 μrad tilt change detection

- Cost per station: <$ 200 (vs.$ 5,000+ for commercial systems)

The network provides real-time tilt data to BPPTKG (Pusat Vulkanologi dan Mitigasi Bencana Geologi) for Merapi eruption early warning.

---

## References

1. Fraden, J. (2016). *Handbook of Modern Sensors: Physics, Designs, and Applications*, 5th ed. Springer.
2. Webster, J. G. (2014). *The Measurement, Instrumentation and Sensors Handbook*, 2nd ed. CRC Press.
3. Bolton, W. (2015). *Mechatronics: Electronic Control Systems in Mechanical and Electrical Engineering*, 7th ed. Pearson.
4. Kotz, S., Llewellyn-Jones, D., & Zorn, P. (2002). *Sensor and Transducers*, 3rd ed. Newnes.
5. Yurish, S. Y. (2014). *MEMS-Based Smart Sensors and Smart Sensor Networks*. IFSA.
6. BPPTKG (2022). "Monitoring System Design for Merapi Volcano." Technical Report, Yogyakarta.
