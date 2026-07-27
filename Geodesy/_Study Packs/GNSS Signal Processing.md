---
tags: [geodesy, study-pack, gnss, signal-processing, aigis]
aliases: [GNSS Signal Processing]
created: 2026-07-27
---

# 📚 Study Pack — GNSS Signal Processing

_A comprehensive study guide covering carrier phase, code pseudorange, atmospheric delays, and modern multi‑frequency processing. Target length: ~6,000 words._

> **Prerequisites:** [[GNSS]], [[Reference Ellipsoid]], [[Least Squares Adjustment]], [[Time and Frequency Standards]]

---

## 1. Introduction

GNSS positioning relies on measuring the **travel time** of electromagnetic signals from satellites to a receiver. Two fundamental observables are used:

| Observable | Symbol | Noise level | Ambiguity | Key challenge |
|------------|--------|-------------|-----------|---------------|
| **Code pseudorange** | $P$ | 0.3–1.0 m | None | Multipath, ionosphere |
| **Carrier phase** | $\Phi$ | 1–2 mm | Integer $N$ (cycles) | Cycle slips, ambiguity resolution |

The signal structure for modern multi‑frequency GNSS:

| Constellation | Freq. | Name | Wavelength | Chip rate / modulation |
|---------------|-------|------|------------|------------------------|
| GPS | 1575.42 MHz | L1 C/A, L1C, L1P(Y) | 19.0 cm | 1.023 MHz / BPSK(1) |
| GPS | 1227.60 MHz | L2 P(Y), L2C | 24.4 cm | 1.023 MHz / BPSK(1) |
| GPS | 1176.45 MHz | L5 | 25.5 cm | 10.23 MHz / BPSK(10) |
| GLONASS | 1602 + k·0.5625 MHz | G1, G2 | — | FDMA |
| Galileo | 1575.42 MHz | E1 (OS) | 19.0 cm | BOC(1,1) / BPSK(1) |
| Galileo | 1191.795 MHz | E5a | 25.1 cm | AltBOC(15,10) |
| Galileo | 1278.75 MHz | E6 | 23.4 cm | BPSK(5) |
| BeiDou | 1561.098 MHz | B1C | 19.2 cm | BOC(1,1) |
| BeiDou | 1207.14 MHz | B2a | 24.8 cm | AltBOC(15,10) |
| BeiDou | 1268.52 MHz | B2b | 23.6 cm | BPSK(10) |

---

## 2. Observation Equations

### 2.1. Code Pseudorange

$$P_{r,f}^s = \rho_r^s + c(\delta t_r - \delta t^s) + I_{r,f}^s + T_r^s + d_{r,f}^s + d_f^s + \varepsilon_P$$

### 2.2. Carrier Phase

$$\Phi_{r,f}^s = \rho_r^s + c(\delta t_r - \delta t^s) - I_{r,f}^s + T_r^s + \lambda_f N_{r,f}^s + \delta_{r,f}^s + \delta_f^s + \varepsilon_\Phi$$

| Term | Description | Frequency dependence |
|------|-------------|---------------------|
| $\rho_r^s$ | Geometric range | None |
| $\delta t_r, \delta t^s$ | Receiver & satellite clock | None |
| $I_{r,f}^s$ | Ionospheric delay | $\propto 1/f^2$ |
| $T_r^s$ | Tropospheric delay | None (non‑dispersive) |
| $\lambda_f N$ | Ambiguity term (phase only) | $\propto 1/f$ |
| $d_{r,f}, d_f^s$ | Code/phase hardware delays | Hardware-specific |
| $\varepsilon$ | Thermal noise + multipath | Varies |

---

## 3. Atmospheric Delays

### 3.1. Ionospheric Delay

The ionosphere is a dispersive medium. For frequency $f$:

$$I_{r,f}^s = \frac{\alpha \cdot \text{STEC}_r^s}{f^2} \quad \text{where } \alpha = \frac{40.3}{c} \;\text{m}^3\text{s}^{-2}$$

- **STEC** = Slant Total Electron Content (electrons/m² along the ray path).
- Vertical TEC (VTEC) relates via mapping function: $\text{STEC} = \text{VTEC} \cdot M(z')$, where $M(z') = \frac{1}{\cos z'}$ for thin‑shell model at height ~350 km.

**Models for correction:**
| Model | Type | Accuracy | Use case |
|-------|------|----------|----------|
| Klobuchar (broadcast) | Analytic | 50–60% removal | Single‑freq standalone |
| NeQuick G (Galileo) | Analytic | ~70% removal | Single‑freq Galileo |
| IGS GIM (Global Ionosphere Map) | Spherical harmonics | 2–5 TECU | Precise post‑processing |
| CODE, JPL, ESA, UPC GIMs | Varies | 1–3 TECU | PPP, RTK |
| **Dual‑frequency IF combination** | Exact (1st order) | 99.9% removal | Standard for precise work |

### 3.2. Tropospheric Delay

Non‑dispersive delay split into hydrostatic and wet components:

$$T_r^s = T_h^s + T_w^s = m_h(e) ZHD + m_w(e) ZWD$$

| Component | Zenith delay | Mapping function |
|-----------|--------------|------------------|
| Hydrostatic (dry) | ZHD ≈ 2.3 m (zenith) | VMF3, GMF, NMF |
| Wet | ZWD ≈ 0.1–0.3 m (zenith) | VMF3, GMF, NMF |

**VMF3** (Vienna Mapping Function 3) uses ECMWF numerical weather model data — currently the state of the art for PPP.

---

## 4. Linear Combinations

### 4.1. Ionosphere‑Free (IF) Combinations

| Name | Formula | Wavelength | Noise |
|------|---------|------------|-------|
| L1/L2 phase IF | $\Phi_{IF} = \frac{f_1^2}{f_1^2-f_2^2}\Phi_1 - \frac{f_2^2}{f_1^2-f_2^2}\Phi_2$ | **Non‑integer** | ~3× single freq |
| L1/L2 code IF | $P_{IF} = \frac{f_1^2}{f_1^2-f_2^2}P_1 - \frac{f_2^2}{f_1^2-f_2^2}P_2$ | — | ~3× single freq |

### 4.2. Wide‑Lane (WL) and Narrow‑Lane (NL)

| Name | Formula | Wavelength (GPS) | Use |
|------|---------|------------------|-----|
| **Wide‑Lane phase** | $\Phi_{WL} = \frac{f_1}{f_1-f_2}\Phi_1 - \frac{f_2}{f_1-f_2}\Phi_2$ | 86.2 cm | Ambiguity bootstrapping |
| **Narrow‑Lane phase** | $\Phi_{NL} = \frac{f_1}{f_1+f_2}\Phi_1 + \frac{f_2}{f_1+f_2}\Phi_2$ | 10.7 cm | Final AR |
| **Melbourne‑Wübbena** | $\Phi_{MW} = \frac{f_1\Phi_1 - f_2\Phi_2}{f_1-f_2} - \frac{f_1 P_1 + f_2 P_2}{f_1+f_2}$ | 86.2 cm | WL ambiguity resolution |

---

## 5. Ambiguity Resolution

### 5.1. The Integer Least Squares Problem

$$\hat{\mathbf{a}}_{\text{int}} = \underset{\mathbf{a} \in \mathbb{Z}^n}{\arg\min} \; (\mathbf{a} - \hat{\mathbf{a}}_{\text{float}})^\top \mathbf{Q}_{\hat{\mathbf{a}}}^{-1} (\mathbf{a} - \hat{\mathbf{a}}_{\text{float}})$$

### 5.2. LAMBDA Method

1. **Decorrelation**: Find unimodular matrix $\mathbf{Z}$ such that $\mathbf{Z}\mathbf{Q}_{\hat{\mathbf{a}}}\mathbf{Z}^\top$ is nearly diagonal.
2. **Search**: Integer search in transformed space (ellipsoidal region).
3. **Back‑transform**: $\hat{\mathbf{a}}_{\text{int}} = \mathbf{Z}^{-1} \hat{\mathbf{z}}_{\text{int}}$.
4. **Validation**: Ratio test or Difference test.

**Validation thresholds:**
- Ratio test: $\frac{\text{2nd best}}{\text{best}} > 3.0$ (or 4.0 for critical apps)
- Difference test: $\text{2nd best} - \text{best} > 10$

### 5.3. Partial Ambiguity Resolution (PAR)

Fix a subset of ambiguities with highest success rate, re‑estimate the rest as floats. Increases overall fixing rate in challenging environments.

---

## 6. Cycle Slip Detection and Repair

A **cycle slip** is a sudden jump in the integer ambiguity due to loss of lock.

### 6.1. Detection methods

| Method | Principle | Detects |
|--------|-----------|---------|
| **Melbourne‑Wübbena** | WL combination nearly constant | Large slips (> 1 cycle) |
| **Geometry‑free (GF)** | $\Phi_1 - \Phi_2$ varies with ionosphere | Small slips (1–2 cycles) |
| **Time‑differenced phase** | $\Phi(t) - \Phi(t-1)$ vs predicted range | All slip sizes |
| **Triple‑difference** | $\Delta\Delta\Delta\Phi$ between 3 epochs, 2 sats | Cycle slips without geometry |

### 6.2. Repair

Once detected, the ambiguity is re‑initialised:
- If WL ambiguity fixed, restore the integer.
- Otherwise, re‑estimate as float and later re‑resolve.

---

## 7. Multi‑GNSS Processing

Modern receivers track GPS + GLONASS + Galileo + BeiDou + QZSS + NavIC. Processing strategies:

### 7.1. System‑Specific Considerations

| Constellation | Challenge | Solution |
|---------------|-----------|----------|
| **GLONASS** | FDMA → inter‑frequency biases (IFB) | Estimate IFB per satellite or use calibration |
| **Galileo** | AltBOC on E5, E6 | Special correlation, inter‑frequency bias models |
| **BeiDou** | GEO/IGSO/MEO mix, B1C/B2a/B2b | Use B1C/B2a for IF; handle satellite‐dependent biases |
| **QZSS** | Compatible with GPS | Treat as GPS augmentation |

### 7.2. Combined Observation Model

Stack observations from all systems, estimate:
- Common receiver position, clock, troposphere
- System‐specific receiver clocks (GST, BDT, etc.)
- Inter‐system biases (ISBs)
- Satellite‐specific phase biases (for PPP‑AR)

---

## 8. Worked Example — Dual‑Frequency Positioning

**Scenario:** Static receiver in Bandung, 2‑hour session, GPS L1/L2.

| Step | Action | Formula/Tool |
|------|--------|--------------|
| 1 | Load RINEX 3.04 obs + nav | `gfzrnx`, `teqc` |
| 2 | Compute satellite positions (broadcast eph) | $\mathbf{X}^s(t) = f(\text{eph})$ |
| 3 | Form IF code + phase | $\Phi_{IF} = \alpha_1\Phi_1 + \alpha_2\Phi_2$ |
| 4 | Estimate troposphere (VMF3) | $ZTD = ZHD + ZWD$ |
| 5 | Float solution (Kalman filter) | $\hat{\mathbf{x}}_{\text{float}}$ |
| 6 | MW WL ambiguity resolution | $\hat{N}_{WL} \in \mathbb{Z}$ |
| 7 | NL ambiguity resolution (LAMBDA) | $\hat{N}_{NL} \in \mathbb{Z}$ |
| 8 | Fixed solution | $\hat{\mathbf{x}}_{\text{fixed}}$ |
| 9 | Quality check: residuals, ratio test | $\sigma < 1$ cm horiz, ratio > 3 |

**Result:** Horizontal precision 0.8 cm, vertical 1.5 cm.

---

## 9. Advanced Topics

### 9.1. Precise Point Positioning (PPP) Signal Processing

- Uses undifferenced observations.
- Requires precise orbits/clocks (IGS Rapid/Final/Real‑time).
- Phase biases from IGS MGEX enable PPP‑AR.
- Convergence: 15–30 min (float), 5–10 min (AR).

### 9.2. Real‑Time Kinematic (RTK) Signal Processing

- Double‑differenced carrier phase.
- Network RTK: VRS, FKP, MAC, SSR (RTCM 3.x MSM).
- Latency critical: < 2 s for cm‑level.

### 9.3. PPP‑RTK (State Space Representation)

- SSR corrections: orbit, clock, code bias, phase bias, ionosphere, troposphere.
- Ambiguity resolution in real time.
- Convergence < 1 min with dense SSR network.

### 9.4. Tight Coupling with INS

- GNSS provides absolute position/velocity updates.
- INS provides high‑rate attitude/position between GNSS epochs.
- Kalman filter fuses both; robust to GNSS outages.

---

## 10. Software Tools

| Tool | Type | Strength |
|------|------|----------|
| **RTKLIB** | Open source | RTK, PPP, post‑processing, GUI + CLI |
| **gLAB** | Open source (UPC) | Teaching, PPP, multi‑GNSS |
| **Bernese GNSS Software** | Academic/Commercial | High‑precision, campaigns, networks |
| **GIPSY‑OASIS** | NASA/JPL | PPP, orbit determination |
| **GNSS‑SDR** | Open source | Software‑defined receiver, research |
| **GipsyX** | JPL | Modern PPP, PPP‑AR |
| **MagicGNSS** | GMV | Cloud PPP, PPP‑RTK |
| **BNC** | BKG | NTRIP caster, real‑time monitoring |

---

## 11. Practice Problems

1. **Derive the ionosphere‑free combination** for Galileo E1 (1575.42 MHz) and E5a (1191.795 MHz). What is the wavelength?
2. **Compute the WL ambiguity** for GPS L1/L2: if $\Phi_1 = 2\,456\,123.4$ cycles, $\Phi_2 = 1\,987\,654.3$ cycles, what is $\Phi_{WL}$ in cycles?
3. **Cycle slip detection**: Given 30‑second epoch interval, satellite elevation 45°, a geometry‑free phase change of 12.3 cycles between epochs — is this a slip or ionosphere?
4. **Ambiguity validation**: Ratio test yields 2.8. Should you fix? What additional checks would you perform?
5. **ISB estimation**: Explain how to estimate inter‐system bias between GPS and Galileo in a combined PPP solution.

---

## 12. Summary Checklist

- [ ] Understand code vs phase observables.
- [ ] Derive ionosphere‑free and wide‑lane combinations.
- [ ] Explain troposphere modelling (ZHD/ZWD + mapping function).
- [ ] Describe LAMBDA ambiguity resolution and validation.
- [ ] Detect and repair cycle slips.
- [ ] Handle multi‑GNSS inter‐system biases.
- [ ] Outline PPP, RTK, and PPP‑RTK workflows.
- [ ] Use at least one open‑source tool (RTKLIB, gLAB) to process a dataset.

---

## 13. References

- Hofmann‑Wellenhof, B., Lichtenegger, H., Wasle, E., *GNSS – Global Navigation Satellite Systems*, Springer, 2008.
- Misra, P. & Enge, P., *Global Positioning System: Signals, Measurements, and Performance*, Ganga‑Jamuna Press, 2012.
- Teunissen, P.J.G., *The Least‑Squares Ambiguity Decorrelation Adjustment (LAMBDA)*, J. Geodesy 70, 1995.
- Odijk, D., *Precise Point Positioning with Partial Ambiguity Fixing*, GPS Solutions 2002.
- Montenbruck, O. et al., *Multi‑GNSS Signal‑in‐Space Range Error Assessment*, GPS Solutions 2015.
- IGS MGEX Products: https://igs.org/mgex/
- RTCM 10403.x Differential GNSS Standards: https://www.rtcm.org/

➡️ [[Geodesy MOC]] · [[_Study Packs]] · [[GNSS]] · [[PPP]] · [[RTK]]