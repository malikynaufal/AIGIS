---
code: FKD211604
name: Instrumentasi
SKS: 3
semester: 6
department: Fisika
tags: [physics, instrumentation, sensors, detectors, electronics]
created: 2026-07-27
---

# FKD211604 — Instrumentasi

## Course Overview

Instrumentation — the practical physics of measuring the world. This course covers sensors, transducers, signal conditioning, data acquisition systems, and precision measurement techniques. Students learn how physics enables the instruments that enable physics (and geodesy).

**Contact Hours:** 3 SKS (1 hour lecture + 2 hours lab per week)
**Prerequisites:** Fisika Dasar II, Analisis Numerik
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Measurement Fundamentals (Weeks 1–4)

- **Measurement process:** physical quantity → transducer → signal conditioning → output

- **Measurement characteristics:**
 - Range, sensitivity, resolution, linearity
 - Accuracy vs. precision: systematic vs. random error
 - **Static characteristics:** calibration curves, zero offset, span
 - **Dynamic characteristics:** rise time, settling time, bandwidth

- **Instrument error sources:** noise, drift, hysteresis, nonlinearity

- **Calibration** procedures: using reference standards

- **International System of Units (SI)** and metrology

### Unit 2: Transducers and Sensors (Weeks 5–8)

- **Resistive sensors:**
 - Strain gauges: ΔR/R = Gε (gauge factor)
 - Thermistors: R(T) = R₀ exp[B(1/T - 1/T₀)] (NTC/PTC)
 - RTD (resistance temperature detectors): Pt100

- **Capacitive sensors:** displacement, humidity

- **Piezoelectric sensors:** charge generation under stress
 - q = d·F (charge proportional to force)

- **Inductive sensors:** LVDT (linear variable differential transformer)

- **Optical sensors:**
 - Photodiodes, photomultipliers
 - Fiber optic sensors

- **Hall effect sensors:** magnetic field measurement

- **Accelerometers:** MEMS-based, piezoelectric, servo-accelerometers

- **GPS/GNSS receivers** as position sensors (overview)

### Unit 3: Signal Conditioning and Electronics (Weeks 9–12)

- **Operational amplifiers (op-amps):**
 - Ideal op-amp: infinite input impedance, zero output impedance
 - Inverting amplifier: V_out = -R_f/R_in · V_in
 - Non-inverting amplifier: V_out = (1 + R_f/R_in) · V_in
 - Summing amplifier, differential amplifier

- **Instrumentation amplifiers:** high CMRR, precision measurement

- **Active filters:**
 - Low-pass filter: f_c = 1/(2πRC)
 - Band-pass filter: for signal selection

- **Amplifier noise:**
 - Thermal (Johnson-Nyquist): V_n = √(4kTRΔf)
 - Shot noise: I_n = √(2qIΔf)
 - 1/f (flicker) noise

- **Analog-to-digital conversion (ADC):** resolution, sampling rate
 - Resolution: 1 LSB = V_range/2^n (n = bits)
 - Nyquist theorem: f_s > 2f_max

### Unit 4: Data Acquisition and Precision Measurement (Weeks 13–16)

- **Data acquisition systems (DAQ):** sensors → signal conditioning → ADC → computer

- **LabVIEW** or Python-based DAQ programming

- **Bridge circuits:**
 - Wheatstone bridge for precision resistance measurement
 - Strain gauge bridge configurations

- **Lock-in amplifiers:** detecting weak signals buried in noise
 - Using reference frequency to extract signal

- **Precision timekeeping:** atomic clocks (cesium, rubidium, hydrogen maser)

- **Distance measurement:** EDM, laser ranging (LIDAR, SLR)

- **Geodetic instrumentation** (overview): total station, gravimeter, tiltmeter

---

## 🔬 Key Equations

```
Thermal noise: V_n = √(4kTRΔf)
Op-amp gain: V_out = -R_f/R_in · V_in
ADC resolution: ΔV = V_range / 2^n
RC filter cutoff: f_c = 1/(2πRC)
Strain gauge: ΔR/R = G·ε
Piezoelectric: q = d·F (pC/N)
Sensitivity: S = d(output)/d(input)
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Select appropriate sensors and transducers for specific measurements
2. Design signal conditioning circuits (amplifiers, filters)
3. Understand noise sources and strategies to improve SNR
4. Set up data acquisition systems and acquire measurement data
5. Apply lock-in amplification for weak signal detection
6. Understand the principles behind geodetic instruments (GNSS receivers, gravimeters, EDM)

---

## 📚 References

1. Horowitz, P. & Hill, W. (2015). *The Art of Electronics*, 3rd ed. Cambridge.
2. Fraden, J. (2016). *Handbook of Modern Sensors*, 5th ed. Springer.
3. Bentley, J.P. (2004). *Principles of Measurement Systems*, 3rd ed. Prentice Hall.
4. Hartley, R. (2017). *Analog Circuit Design*. Springer.
5. UGM Geomatics Lab equipment manuals (campus-specific).
