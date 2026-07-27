---
tags: [geodesy, concept, positioning, aigis]
aliases: [PPP, Precise Point Positioning]
created: 2026-07-12
updated: 2026-07-27
---

# 🛰️ PPP (Precise Point Positioning)

**Precise Point Positioning (PPP)** is a GNSS positioning technique that uses a **single receiver** together with externally provided **precise orbit and clock products** (from IGS or equivalent) to achieve decimetre‑to‑centimetre accuracy globally—without a local base station. The method relies on careful modelling of every error source that would normally be differenced away in RTK.

> **Indonesian term:** *Precise Point Positioning (PPP)*

---

## 1. Core Observation Model

The undifferenced (single‑station) carrier‑phase observation equation:

$$\Phi_{r,f}^s = \rho_r^s + c\bigl(\delta t_r - \delta t^s\bigr) + \lambda_f N_{r,f}^s + I_{r,f}^s + T_r^s + \Delta_{r,f}^s + \varepsilon_{\Phi} $ $ | Symbol | Meaning | How handled in PPP |
|--------|---------|---------------------|
| $\rho_r^s $ | Geometric range | Solved for in the position |
| $\delta t^s $ | Satellite clock | **Precise IGS clock product** (0.1 ns) |
| $\delta t_r $ | Receiver clock | Estimated as an unknown (or differenced out) |
| $ N_{r,f}^s $ | Integer ambiguity | Float or integer (PPP‑AR) |
| $ I_{r,f}^s $ | Ionospheric delay | Removed via ionosphere‑free (IF) combination |
| $ T_r^s $ | Tropospheric delay | Estimated (zenith + mapping function) |
| $\Delta_{r,f}^s $ | Phase centre offsets | IGS ANTEX model |
| $\varepsilon_{\Phi} $ | Noise + multipath | ~1 mm (carrier phase) |

The code pseudorange model is similar but no ambiguity term, higher noise (~30 cm).

---

## 2. Key Precise Products

| Product | Type | Source | Precision | Update rate |
|---------|------|--------|-----------|-------------|
| **Rapid orbits** | SP3 | IGS Rapid (IGR) | ~3 cm RMS | Daily |
| **Final orbits** | SP3 | IGS Final (IGF) | ~1.5 cm RMS | Bi‑weekly (2‑week latency) |
| **Real‑time orbits** | RT‑SSR | IGS / EMR / JAXA | ~5 cm | ~5 s |
| **Satellite clocks** | RINEX | IGS | 0.1–0.3 ns (Rapid) | 30 s / 5 s (RT) |
| **Code biases** | BSX | IGS MGEX | ~0.3 ns | Daily |
| **Phase biases** | .bias | IGS MGEX | Enables PPP‑AR | Daily |

---

## 3. Combinations Used in PPP

| Combination | Formula | Purpose | Wavelength |
|-------------|---------|---------|------------|
| **Ionosphere‑free (L‑C)** | $\Phi_{LC} = \frac{f_1^2}{f_1^2-f_2^2}\Phi_1 - \frac{f_2^2}{f_1^2-f_2^2}\Phi_2 $ | Removes 1st‑order ionosphere | **Non‑integer** |
| **Wide‑lane (WL)** | $\Phi_{WL} = \frac{f_1}{f_1-f_2}\Phi_1 - \frac{f_2}{f_1-f_2}\Phi_2 $ | Wide wavelength for bootstrapping | ~86 cm (GPS) |
| **Narrow‑lane (NL)** | $\Phi_{NL} = \frac{f_1}{f_1+f_2}\Phi_1 + \frac{f_2}{f_1+f_2}\Phi_2 $ | Final ambiguity resolution | ~10.7 cm (GPS) |
| **Geometry‑free (GF)** | $\Phi_{GF} = \Phi_1 - \Phi_2 $ | Ionospheric monitoring | — |

---

## 4. PPP Convergence and Ambiguity Resolution

### 4.1. Classical PPP (float)

- Ambiguities are **estimated as real numbers** (float).

- Typical convergence: **15–30 minutes** to reach decimetre level, further to cm.

- Accuracy: ~2–5 cm horizontal, ~5–8 cm vertical.

### 4.2. PPP‑AR (integer ambiguity resolution)

Using IGS‑compatible phase bias products, ambiguities can be fixed to integers:

- **Melbourne–Wübbena (MW) combination** resolves wide‑lane ambiguities.

- Narrow‑lane ambiguities resolved using precise biases.

- Convergence time reduced to **5–10 minutes**.

- Accuracy: **1–2 cm horizontal, 2–4 cm vertical** (competitive with RTK).

### 4.3. PPP‑RTK (Real‑Time PPP with SSR corrections)

Uses real‑time orbit, clock, code bias, and atmospheric corrections:

- Ambiguity resolution possible in real‑time.

- Convergence: **< 1 minute** (with good SSR network).

- Accuracy: cm‑level.

---

## 5. Tropospheric Estimation

The troposphere cannot be differenced out in PPP and must be estimated:

$ $ T_r^s = m_h^s(\text{elev})\cdot Z_h + m_w^s(\text{elev})\cdot Z_w $$

| Component | Mapping Function | Typical Value |
|-----------|------------------|---------------|
| Zenith hydrostatic ( $ Z_h $) | VMF3 / GMF | ~2.3 m (reduced) |
| Zenith wet ( $ Z_w $) | VMF3 / GMF | ~0.1–0.3 m |
| Mapping function $ m_h $ | VMF3, GMF, NMF | 1/cos(z) approx |

VMF3 (Vienna Mapping Function) is the current state‑of‑the‑art, derived from ECMWF NWP model data.

---

## 6. Worked Example – PPP Processing Workflow

**Input data:** Single‑frequency GPS receiver in Surabaya, Indonesia (2024‑06‑15).

| Step | Action | Result |
|------|--------|--------|
| 1 | Download IGS Final orbits + clocks (SP3, CLK) | Products for 2024‑06‑15 |
| 2 | Load RINEX 3.04 observation file | 4‑hour session, GPS L1/L2 |
| 3 | Apply corrections: precise orbits, clocks, P1/P2 biases, antenna calibration | Observation model set up |
| 4 | Estimate troposphere Zenith Delay (random‑walk) | ZD estimated per epoch |
| 5 | Solve position + float ambiguities (Kalman filter) | Coordinates: float |
| 6 | Apply MW + LAMBDA for AR | WL: fixed, NL: fixed |
| 7 | Final fixed position | $\sigma_{xy} = 1.8 $ cm,$\sigma_z = 3.2 $ cm |

---

## 7. PPP vs RTK

| Aspect | PPP | RTK |
|--------|-----|-----|
| **Infrastructure** | None (just internet) | Base station / CORS |
| **Latency** | 2 weeks (Final) / real‑time | Real‑time |
| **Baseline** | Global | < 20 km (single base) |
| **Accuracy (horiz)** | 1–5 cm | 1–2 cm |
| **Accuracy (vert)** | 3–8 cm (float), 2–4 cm (AR) | 2–5 cm |
| **Convergence** | 15–30 min (float), 5–10 min (AR) | Instant |
| **Best for** | Remote areas, autonomous vehicles, aviation | Construction, survey, engineering |

---

## 8. Related

- [[GNSS]] – the underlying constellation and signals.

- [[RTK]] – the differential counterpart to PPP.

- [[IGS]] – provides precise orbit and clock products.

- [[Geoid Undulation]] – both RTK and PPP yield ellipsoidal heights; need $ N$ for orthometric heights.

---

## 9. References

- Zumberge, J.F., Heflin, M.B., Jefferson, D.C., Watkins, M.M., Webb, F.H., *Precise Point Positioning for the Efficient and Robust Analysis of GPS Data from Large Networks*, JGR 102(B3), 5005‑5017, 1997. DOI:10.1029/96JB03860

- Gabor, M.J., Nerem, R.S., *GPS Carrier Phase Ambiguity Resolution Using Satellite‑Satellite Single Differences*, JGR 104(B2), 2715‑2730, 1999.

- Bertiger, W. et al., *Precise Real‑Time GPS Orbit and Clock Estimates for Improved GPS Performance*, JGR 2008.

- Laurichesse, D., Mercier, F., Berthias, J.-P., *Integer Ambiguity Resolution on Undifferenced GPS Phase Measurements and Its Application to PPP and Satellite Precise Orbit Determination*, Navigation 56(2), 135‑149, 2009.

- Kouba, J. & Héroux, P., *Precise Point Positioning Using IGS Orbit and Clock Products*, GPS Solutions 5(2), 12‑28, 2001. DOI:10.1007/PL00012883

- Teunissen, P.J.G., *Kinematic PPP‑RTK and Its Applicability to Multi‑GNSS*, J. Geodesy, 2022.

- IGS Real‑Time Service (RTS), https://igs.bkg.bund.de/root_ftp/IGS/ Products/rts/

➡️ [[Geodesy MOC]] · [[Basic Geodesy]] · [[Kurikulum Teknik Geodesi]]