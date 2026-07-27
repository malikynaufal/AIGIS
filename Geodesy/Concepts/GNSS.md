---
tags: [aigis, concept, geodesy, gnss, gps, glonass, galileo, positioning, satellite-navigation]
created: 2026-07-27
updated: 2026-07-27
---

# GNSS — Global Navigation Satellite Systems

## For Geodesy & Positioning Science

**Core Idea:** GNSS uses satellite radio signals to determine position, velocity, and time anywhere on Earth. Multiple constellations (GPS, GLONASS, Galileo, BeiDou) provide global coverage with centimeter-to-meter accuracy. GNSS is the primary positioning technology for modern geodesy, surveying, navigation, and timing.

---

## System Overview

### Major Constellations

| System | Country | Satellites (approx.) | Frequencies | Started |
|--------|---------|---------------------|-------------|---------|
| **GPS** | USA | 31 (nominal 24) | L1 (1575.42 MHz), L2 (1227.60), L5 (1176.45) | 1978 (FOC 1995) |
| **GLONASS** | Russia | 24 | L1 (1602.0 ± n×0.5625 MHz), L2, L3 | 1996 (FOC 2011) |
| **Galileo** | EU | 26 (full 30) | E1 (1575.42), E5a/E5b, E6 | 2016 (FOC 2022) |
| **BeiDou** | China | 35 (full) | B1 (1561.098), B2, B3 | 2020 (FOC) |
| **IRNSS/NavIC** | India | 7 (+4 backup) | L5 (1176.45), S (2492.028) | 2018 |

### GPS Segments

| Segment | Description |
|---------|-------------|
| **Space** | Constellation of ~31 satellites in 6 orbital planes, ~20,200 km altitude, 55° inclination, ~12h period |
| **Control** | Master Control Station at Schriever AFB plus monitor stations worldwide |
| **User** | Receivers — from survey-grade to mass-market phones |

---

## GNSS Positioning Principles

### Basic Pseudorange

$$\rho = c \cdot (t_{rx} - t_{tx}) = ||\mathbf{r}_{sat}(t) - \mathbf{r}_{rx}|| + c\Delta t$$**Resolving for 4 unknowns**$(x, y, z, \delta t) $requires ≥ 4 satellites
:

$$\begin{bmatrix} \rho_1 \\ \rho_2 \\ \rho_3 \\ \rho_4 \end{bmatrix} \xrightarrow{\text{least squares}} \begin{bmatrix} x_{rx} \\ y_{rx} \\ z_{rx} \\ \delta t_{rx} \end{bmatrix} $$

### Observation Equations

**Code (pseudorange):*
*

$$P_i = \rho + c(dt_r - dt_s) + d_{iono} + d_{trop} + \varepsilon_P$$

**Carrier phase:*
*

$$\Phi_i = \frac{\rho}{\lambda} + N_i + \frac{c}{\lambda}(dt_r - dt_s) - \frac{d_{iono}}{\lambda} + \frac{d_{trop}}{\lambda} + \varepsilon_\Phi$$where $\rho = ||\mathbf{r}_r - \mathbf{r}_s|| $= geometric range,$N$= integer ambiguity.

### Error Sources

| Error Source | Magnitude (standard GPS) | Mitigation |
|-------------|------------------------|------------|
| **Satellite clock** | 2–3 m | Broadcast corrections, differencing |
| **Satellite orbit** | 1–2 m | Precise ephemeris (IGS) |
| **Ionosphere** | 5–15 m (peak) | Dual-frequency, model |
| **Troposphere** | 2.5 m (zenith) | Model, estimation |
| **Multipath** | 0.5–5 m | Antenna design, filtering |
| **Receiver noise** | 0.1–0.5 m (code); 1–2 mm (phase) | SNR-based weighting |

---

## Positioning Modes

### SPP (Standard Point Positioning)

- Single C/A-code receiver

- Broadcast ephemeris and clocks

- **Accuracy:** 3–5 m horizontal, 5–10 m vertical

### PPP (Precise Point Positioning)

- Dual-frequency ionosphere-free combination

- Precise satellite orbits and clocks (IGS final: ~2.5 cm)

- **Accuracy:** 2–5 cm (static), 5–10 cm (kinematic)

### DGNSS (Differential GNSS)

Base station transmits corrections to rover
:

$$\rho_{corr} = \rho_{rover} + \Delta\rho_{base} $$

**Accuracy:** 0.5–3 m (sub-meter with carrier smoothing)

### RTK (Real-Time Kinematic)

Float solution: estimate $N \in \mathbb{R} $Fixed solution: resolve $N \in \mathbb{Z} $(LAMBDA method
)

$$\hat{N}_{float} \xrightarrow{\text{LAMBDA}} \hat{N}_{fixed} $$

**Accuracy:** 1–2 cm + 2 ppm (horizontal)

### Network RTK (CORS)

Multiple reference stations model spatially-correlated errors:

| Method | Description |
|--------|-------------|
| **VRS** | Virtual Reference Station — closest real station |
| **FKP** | Area correction parameters |
| **MAC** | Master-Auxiliary Concept — full network |

---

## GNSS Observables

### Linear Combinations

| Combination | Formula | Purpose |
|-------------|---------|---------|
| **Ionosphere-free (L3)** | $\frac{f_1^2 P_1 - f_2^2 P_2}{f_1^2 - f_2^2} $ | Eliminates ~99.9% ionosphere |
| **Geometry-free (L4)** | $P_1 - P_2$ | Ionosphere measurement |
| **Wide-lane (WL)** | $\frac{f_1 \Phi_1 - f_2 \Phi_2}{f_1 - f_2} $ | Widens ambiguity resolution |
| **Narrow-lane (NL)** | $\frac{f_1 \Phi_1 + f_2 \Phi_2}{f_1 + f_2} $ | Reduces noise |

### Single, Double, Triple Differences

| Difference | Form | Value |
|------------|------|-------|
| Single-diff (receivers) | $\Delta\Phi_{ij} = \Phi_i - \Phi_j$ | Removes satellite clock |
| Double-diff (receivers & sats) | $\nabla\Delta\Phi_{ij}^{pq} = \Phi_i^p - \Phi_j^p - \Phi_i^q + \Phi_j^q$ | Removes receiver clocks |
| Triple-diff (epochs) | $\delta\nabla\Delta\Phi_{ij}^{pq} = \nabla\Delta\Phi(t_2) - \nabla\Delta\Phi(t_1)$ | Removes ambiguities (detects cycle slips) |

---

## GPS Signals

### C/A Code (L1)

- Chipping rate: 1.023 MHz

- Code length: 1023 chips → 1 ms period

- Each satellite has unique PRN sequence

### P(Y) Code (L1, L2)

- Chipping rate: 10.23 MHz

- Seven-day-long sequence

- Encrypted for authorized users

### Modernized Signals (Block IIR-M onward)

- **L2C** (L2, 1227.60 MHz): Improved civilian code

- **L5** (1176.45 MHz): Safety-of-life, higher power

- **L1C** (L1, 1575.42 MHz): Interoperability with Galileo

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\rho = ||\mathbf{r}_r - \mathbf{r}_s|| + c\Delta t$ | Pseudorange | Basic ranging |
| $P = \rho + cdt + d_{iono} + d_{trop} + \varepsilon$ | Code equation | Observation model |
| $\Phi = \rho/\lambda + N + \dots$ | Phase equation | Precision positioning |
| $P_{IF} = (f_1^2 P_1 - f_2^2 P_2)/(f_1^2 - f_2^2)$ | Ionosphere-free | PPP processing |
| $\nabla\Delta\Phi_{12}^{34} $ | Double difference | RTK processing |
| $\rho = c \cdot \Delta t$ | Time-of-flight | Range from timing |

---

## Related Concepts

- [[GPS]] — Specific GPS constellation details

- [[GNSS]] — GLONASS specificities

- [[GNSS]] — Galileo constellation

- [[PPP]] — Precise Point Positioning

- [[RTK]] — Real-Time Kinematic

- [[Least Squares Adjustment]] — Estimation method

- [[Electromagnetism & Signal Propagation]] — Signal physics

- [[WGS84]] — Reference frame for GNSS

---

## Study Problems

1. **Recall:** Why must ≥ 4 satellites be visible for 3D positioning? (Hint: count unknowns.)
2. **Application:** A GPS-SPP receiver gets $\rho_1 = 20589423.5 $m,$\rho_2 = 21045987.2 $m,$\rho_3 = 20765432.1 $m,$\rho_4 = 21234567.8 $m. The satellite positions (ECEF) are given. Form the design matrix and compute the receiver position (simplified: skip clock term for this problem).
3. **Derivation:** Show that in double-differencing, the receiver clock term cancels.
4. **Real-world:** In CORS network, a rover is 50 km from the nearest reference station. Estimate the residual ionospheric and tropospheric errors after differential correction.

---

## Common Mistakes

1. **Forgetting the integer nature of ambiguities:**$N$ is integer — rounding the float solution is NOT the same as LAMBDA.
2. **Ignoring satellite geometry:** PDOP of 20 is very different from PDOP of 2.
3. **Confusing code and phase:** Code = meters, phase = cycles (needs conversion).
4. **Not accounting for antenna phase center variations:** They change with elevation and azimuth.
5. **Applying wrong Earth rotation correction:** Earth rotates during signal travel (Sagnac effect: ~30 m at equator).

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*