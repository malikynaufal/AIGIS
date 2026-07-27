---
title: "Teknologi GNSS Lanjutan"
subject: "Fisika Pilihan"
tags:
  - GNSS
  - GPS
  - PPP
  - RTK
  - positioning
  - SKS: 3
---

# FKD214704 — Teknologi GNSS Lanjutan
**Advanced GNSS Technology** | 3 SKS (Satuan Kredit Semester)

## Overview

Advanced GNSS technology (teknologi GNSS lanjutan) builds on fundamental satellite positioning concepts to explore multi-frequency, multi-constellation processing, precise point positioning (PPP), real-time kinematic (RTK) techniques, integer ambiguity resolution, and tropospheric modeling. Students will gain practical skills in processing GNSS data for geodetic, surveying, and geophysical applications using the latest satellite constellations: GPS (USA), GLONASS (Russia), Galileo (EU), and BeiDou (China).

---

## 1. Multi-Frequency, Multi-Constellation GNSS

### 1.1 Signal Structure

Each GNSS satellite broadcasts on multiple carrier frequencies. The observables (pengamatan) for a receiver at epoch $t$include:

**Carrier phase (fase pembawa):**$$\Phi_{L_i}(t) = \rho(t) + c\left[\delta t_r(t) - \delta t^s(t)\right] + \lambda_i N_i - I_{L_i}(t) + T(t) + \epsilon_{\Phi,i}$$**Pseudorange (semua jarak):**$$P_{L_i}(t) = \rho(t) + c\left[\delta t_r(t) - \delta t^s(t)\right] + I_{L_i}(t) + T(t) + \epsilon_{P,i}
$$

| Constellation (Sistem) | Frequencies | Signals |
|---|---|---|
| GPS | L1 (1575.42 MHz), L2 (1227.60 MHz), L5 (1176.45 MHz) | C/A, P(Y), M, C |
| GLONASS | G1 (1602 MHz), G2 (1246 MHz) | CDMA + FDMA |
| Galileo | E1 (1575.42 MHz), E5a, E5b, E6 | BOC(1,1), BPSK |
| BeiDou | B1I, B1C, B2a, B2b, B3I | D-BOC, MBOC |

### 1.2 Ionosphere-Free Linear Combination

The first-order ionospheric delay is frequency-dependent ($I \propto f^{-2}$). The ionosphere-free combination eliminates >99.9% of the ionospheric error:
$$

\Phi_{IF} = \frac{f_1^2 \Phi_1 - f_2^2 \Phi_2}{f_1^2 - f_2^2}$$This combination is standard for precise orbit determination and PPP, but amplifies measurement noise by a factor$\approx 2.98$ for GPS L1/L2.

### 1.3 Wide-Lane and Narrow-Lane Combinations

**Wide-lane** ($\lambda_{WL} \approx 86.2$cm for GPS):$$\Phi_{WL} = \Phi_1 - \Phi_2, \quad \lambda_{WL} = \frac{c}{f_1 - f_2}
$$

**Narrow-lane** ($\lambda_{NL} \approx 10.7$cm):$$\Phi_{NL} = \frac{f_1 \Phi_1 + f_2 \Phi_2}{f_1 + f_2}, \quad \lambda_{NL} = \frac{c}{f_1 + f_2}$$The wide-lane ambiguity$N_{WL} = N_1 - N_2$is easier to resolve due to its long wavelength and is often solved first in the ambiguity resolution cascade.

---

## 2. Precise Point Positioning (PPP)

### 2.1 PPP Observation Model

PPP uses a single receiver with precise satellite orbit and clock products (from IGS) to achieve cm-level positioning. The undifferenced phase observation:$$\Phi = \rho + c(\delta t_r - \delta t^s) + T - I + N\lambda + \text{tides} + \text{PCO/PCV} + \epsilon$$Key corrections (koreksi) applied:

| Correction (Koreksi) | Source | Magnitude |
|---|---|---|
| Satellite clock | IGS rapid products | ~1 ns (30 cm) |
| Satellite orbit | IGS final orbits | ~2.5 cm |
| Phase wind-up | Computed | Up to ~2 dm |
| Tidal displacements | IERS conventions | Up to ~30 cm |
| Phase center offsets | ANTEX files | ~cm level |
| Solid Earth tide | IERS | Up to ~0.3 m |

### 2.2 Convergence Behavior

PPP requires a convergence period (waktu konvergensi) for integer ambiguities and tropospheric estimates to stabilize. Typical convergence:

- **Kinematic PPP**: 15–30 min for cm-level (3D RMS)

- **Static PPP**: 1–2 hours for mm-level horizontal, cm-level vertical

- **PPP-AR (ambiguity resolution)**: Convergence reduced to 5–15 min using integer ambiguity resolution with satellite fractional biases

### 2.3 Case Study: PPP for Sea-Level Monitoring

A permanent GNSS station at Jakarta coast (BIG站 CUTO) is processed in PPP mode using the CSRS-PPP service (Natural Resources Canada). Over 5 years of daily PPP solutions:

- Horizontal velocity:$v_E = 32.4 \pm 1.2$mm/yr,$v_N = -5.1 \pm 1.5$mm/yr

- Vertical velocity:$v_U = -4.8 \pm 2.1$mm/yr (including subsidence)

- Corrected relative sea-level rise: ~7 mm/yr (combining land subsidence + eustatic rise)

---

## 3. Real-Time Kinematic (RTK)

### 3.1 Differential Observation Equations

RTK uses a base station (stasiun base) and rover separated by$<40$km. Single-differenced (antenna-to-antenna) observations eliminate satellite clock errors:$$\Delta\Phi_{ij}^k = \Delta\rho_{ij}^k + T_{ij}^k - I_{ij}^k + \lambda N_{ij}^k + \epsilon$$Double-differencing (satellite-to-satellite) also eliminates receiver clock:$$\nabla\Delta\Phi = \nabla\Delta\rho + \nabla\Delta T - \nabla\Delta I + \lambda \nabla\Delta N + \epsilon$$### 3.2 RTK Positioning Precision

| Baseline Length | Horizontal Precision | Convergence Time |
|---|---|---|
| <10 km | 5–10 mm | <30 s |
| 10–30 km | 10–20 mm | 1–2 min |
| 30–50 km | 20–50 mm | 2–5 min |
| >50 km | 50+ mm | Unreliable |

### 3.3 Network RTK (VRS/FKP)

Network RTK interpolates atmospheric corrections from a CORS network (jaringan CORS) over a region. Virtual Reference Station (VRS) generates a virtual observation stream at the rover's location, effectively reducing the baseline to near-zero.

---

## 4. Integer Ambiguity Resolution (Resolusi Ambiguitas Intejer)

### 4.1 LAMBDA Method

The most widely used method for integer ambiguity resolution (IAR) is the Least-squares AMBiguity Decorrelation Adjustment (LAMBDA):

1. **Float solution**: Solve$\hat{a}_f$and$\Sigma_{\hat{a}}$in the real domain
2. **Decorrelation**: Transform$\hat{z} = U^{-1}\hat{a}_f$using Z-transform to decorrelate ambiguities
3. **Integer search**: Search integer grid points near$\hat{z}$within an ellipsoidal confidence region:$$\chi^2 = (\hat{z} - z)^T Q_{\hat{z}}^{-1}(\hat{z} - z) \leq \chi^2_{\alpha}$$4. **Rounding-back**: Transform best candidate back to original ambiguity space

### 4.2 Success Rate

The ambiguity resolution success rate is bounded by:$$P_s \leq 1 - F_{\chi^2}(f, \chi^2_{\alpha})$$where$f$is the number of ambiguity parameters and$F_{\chi^2}$is the chi-squared CDF. For practical geodetic surveys,$P_s > 99.9\%$is targeted.

---

## 5. Tropospheric Modeling for GNSS

### 5.1 Zenith Path Delay

The zenith total delay (ZTD, penundaan zenith total) has hydrostatic (dry) and wet components:$$\text{ZTD} = \text{ZHD} + \text{ZWD}$$**Saastamoinen model** for ZHD:$$\text{ZHD} = \frac{0.0022768 \cdot P}{1 - 0.00266\cos(2\phi) - 0.00028h}$$where$P$is surface pressure (hPa),$\phi$is latitude (rad), and$h$is height (km).

### 5.2 Mapping Functions

The slant delay is obtained using a mapping function$m(E)$:
$$\Delta_{\text{slant}} = \text{ZHD} \cdot m_H(E) + \text{ZWD} \cdot m_W(E)$$

VMF3 (Vienna Mapping Function 3) is the current state-of-the-art, based on numerical weather model output.

### 5.3 Case Study: GPS-PWV over Jakarta

GPS-derived precipitable water vapor (PWV) at Jakarta's CORS stations shows strong correlation with rainfall ($r = 0.72$, $p < 0.01$). During the January 2020 Jakarta floods, PWV exceeded 70 mm for 5 consecutive days — a significant predictor for heavy rainfall events, useful for BMKG's early warning (peringatan dini) systems.

---

## References

1. Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS – Global Navigation Satellite Systems*. Springer.
2. Teunissen, P. J. G., & Kleusberg, A. (Eds.) (1998). *GPS for Geodesy*, 2nd ed. Springer.
3. Bock, Y., & Dammets, R. (2009). "100 years of Geodesy," in *Global Geodetic Observing System*. Springer.
4. Kouba, J., & Héroux, P. (2001). "Precise Point Positioning using IGS orbit and clock products," *GPS Solutions*, 5(2), 12–28.
5. Dousa, J. et al. (2017). "PPP-RTK for regional networks: CORS-based approach," *J. Geod.*, 91, 1385–1399.
6. Indonesian BIG (2023). "CORS-Indonesia: Network Status and Applications." Technical Report.
