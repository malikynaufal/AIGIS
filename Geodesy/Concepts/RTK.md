---
tags: [geodesy, concept, positioning, aigis]
aliases: [RTK, Real-Time Kinematic]
created: 2026-07-12
updated: 2026-07-27
---

# 🛰️ RTK (Real-Time Kinematic)

**RTK** is a [[GNSS]] technique giving **centimetre-level** positioning in real time by resolving carrier‑phase ambiguities relative to a nearby base station (or network). The rover receives real‑time corrections from the base via radio, cellular (NTRIP), or satellite (SSR).

> **Indonesian term:** *Real-Time Kinematic (RTK)*

---

## 1. Basic Principle

The raw carrier‑phase measurement on frequency $f$ from satellite $s$ at receiver$r$:$ $\Phi_{r,f}^s = \rho_r^s + c(\delta t_r - \delta t^s) + \lambda_f N_{r,f}^s + I_r^s + T_r^s + \epsilon_{\Phi} $$ | Symbol | Meaning |
|--------|---------|
| $\rho_r^s$| Geometric range |
| $c$| Speed of light |
|$\delta t_r, \delta t^s $| Receiver & satellite clock errors |
|$\lambda_f $| Wavelength of frequency$f$|
|$ N_{r,f}^s $| **Integer ambiguity** (cycles) |
|$ I_r^s $| Ionospheric delay |
|$ T_r^s $| Tropospheric delay |
|$\epsilon_{\Phi} $ | Measurement noise (~1 mm) |

The key difference from code pseudorange is the **integer ambiguity**$N$. Once$N$is resolved, $\Phi$ becomes an extremely precise range measurement (mm noise).

---

## 2. Single‑Difference and Double‑Difference

### 2.1. Single Difference (between rover $r$ and base$b$for the same satellite$s$)$\$ $\nabla\Phi_{rb,f}^s = \Phi_{r,f}^s - \Phi_{b,f}^s = \nabla\rho_{rb}^s + c(\delta t_r - \delta t_b) + \lambda_f \nabla N_{rb,f}^s + \nabla I_{rb}^s + \nabla T_{rb}^s
$$
Common errors (satellite clock, ephemeris, atmospheric delays for short baselines) **cancel out**.

### 2.2. Double Difference (between two satellites $s_1, s_2$)$\$ $\Delta\nabla\Phi_{rb,f}^{s_1s_2} = \nabla\Phi_{rb,f}^{s_1} - \nabla\Phi_{rb,f}^{s_2} = \Delta\nabla\rho_{rb}^{s_1s_2} + \lambda_f \Delta\nabla N_{rb,f}^{s_1s_2} + \Delta\nabla I_{rb}^{s_1s_2} + \Delta\nabla T_{rb}^{s_1s_2} $$Receiver clock terms also cancel. **Double‑difference carrier phase** is the standard RTK observable.

---

## 3. Ambiguity Resolution – The Key to RTK

The goal is to find integer ambiguities $\Delta\nabla N \in \mathbb{Z}$.

### 3.1. Float solution

First, solve for $\Delta\nabla N$ as real numbers using least squares $ $\hat{\mathbf{a}}_{\text{float}} = (\mathbf{A}^\top\mathbf{P}\mathbf{A})^{-1}\mathbf{A}^\top\mathbf{P}\boldsymbol{\ell} $$with covariance$ \mathbf{Q}_{\hat{\mathbf{a}}} $.

### 3.2. Integer least‑squares (ILS)

Search the integer grid:$ $\hat{\mathbf{a}}_{\text{int}} = \underset{\mathbf{a}\in\mathbb{Z}^n}{\arg\min} \quad (\mathbf{a} - \hat{\mathbf{a}}_{\text{float}})^\top \mathbf{Q}_{\hat{\mathbf{a}}}^{-1} (\mathbf{a} - \hat{\mathbf{a}}_{\text{float}})$\$$
Standard search algorithms:

- **LAMBDA** (Least‑squares AMBiguity Decorrelation Adjustment) – decorrelates $\mathbf{Q}$ before integer search (Teunissen, 1995).

- **MLAMBDA** / **Partial Fixing** – fixes a subset when full resolution is uncertain.

### 3.3. Validation – Ratio tes
t$ $\text{Ratio} = \frac{\text{Second‑best quadratic form}}{\text{Best quadratic form}} $$If$ \text{Ratio} > \text{threshold} $\(typically 3 or 4), the fix is accepted.

---

## 4. Network RTK / VRS

For larger areas (> 10–20 km baseline), single‑base RTK degrades due to spatially correlated errors (ionosphere, troposphere). **Network RTK** uses a network of permanent reference stations (CORS):

| Service | How it works | Standard |
|---------|--------------|----------|
| **VRS** (Virtual Reference Station) | Creates a synthetic base near the rover | RTCM 3.x MSM |
| **FKP** (Flächen‑Korrektur‑Parameter) | Sends interpolated atmospheric corrections | RTCM 3.x MSM |
| **MAC** (Master‑Auxiliary) | Sends raw data from all reference stations | RTCM 3.x MSM |
| **SSR** (State Space Representation) | Sends satellite‑wise orbit/clock/bias corrections | RTCM SSR |

---

## 5. Worked Example – Baseline Resolution

**Scenario:** Base at $X_b, Y_b, Z_b$\(known). Rover measures carrier phase on GPS L1 ( $\lambda = 0.19029367$ m) and L2 ( $\lambda = 0.24421021$ m) to 6 satellites.

Double‑difference float ambiguities (after least squares, cycles):

| Sat‑pair | L1 float | L2 float |
|----------|----------|----------|
| 1–2 | 12.003 | 9.002 |
| 1–3 | −5.998 | −4.499 |
| 1–4 | 23.001 | 17.251 |
| 1–5 | 8.000 | 6.000 |
| 1–6 | −17.004 | −12.753 |

Decorrelate with LAMBDA → integer candidates → best candidate$ $\hat{\mathbf{a}}_{\text{int}} = [12, -6, 23, 8, -17] \text{ cycles (L1)} $$Ratio test = 5.2 > 3.0 → **FIXED**.

Position precision after fixing:

- Horizontal: $\sigma_{xy} \approx 1$ cm + 1 ppm

- Vertical: $\sigma_z \approx 2$ cm + 1 ppm

---

## 6. RTK vs PPP vs Static

| Aspect | RTK | PPP | Static / Post‑processed |
|--------|-----|-----|--------------------------|
| **Latency** | Real‑time | Real‑time (PPP‑RT) / post | Post‑processed |
| **Baseline limit** | ~20 km (single base) / unlimited (network) | Global | Unlimited |
| **Accuracy (horiz)** | 1–2 cm | 2–5 cm (PPP) / 1–2 cm (PPP‑RT) | < 1 cm |
| **Convergence** | Instant (if fixed) | 15–30 min (PPP) / few min (PPP‑RT) | N/A (post) |
| **Infrastructure** | Base station / CORS | IGS products / SSR | None (after field) |
| **Ambiguity** | Integer‑fixed | Float or integer (PPP‑AR) | Integer‑fixed |

---

## 7. Diagram – RTK Architecture

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 350" width="700" height="350">
 <rect width="700" height="350" fill="#1a1a2e" rx="8"/>
 <text x="350" y="25" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle">RTK System Architecture</text>
 <!-- Satellites -->
 <g transform="translate(50,60)">
 <circle cx="0" cy="0" r="25" fill="#4cc9f0"/>
 <text x="0" y="5" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">GPS</text>
 <circle cx="60" cy="-20" r="25" fill="#4cc9f0"/>
 <text x="60" y="-15" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">GLO</text>
 <circle cx="120" cy="0" r="25" fill="#4cc9f0"/>
 <text x="120" y="5" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">GAL</text>
 <circle cx="60" cy="20" r="25" fill="#4cc9f0"/>
 <text x="60" y="25" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">BDS</text>
 </g>
 <!-- Signals -->
 <g stroke="#4cc9f0" stroke-width="1.5" fill="none" stroke-dasharray="4,2">
 <line x1="50" y1="85" x2="120" y2="150"/>
 <line x1="110" y1="40" x2="120" y2="150"/>
 <line x1="170" y1="85" x2="120" y2="150"/>
 <line x1="110" y1="80" x2="120" y2="150"/>
 </g>
 <!-- Base Station -->
 <g transform="translate(90,160)">
 <rect x="-30" y="-20" width="60" height="40" fill="#f9c74f" rx="4"/>
 <text x="0" y="-2" fill="#1a1a2e" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">BASE</text>
 <text x="0" y="14" fill="#1a1a2e" font-size="8" font-family="sans-serif" text-anchor="middle">Known coords</text>
 <circle cx="0" cy="35" r="8" fill="#f72585"/>
 <text x="0" y="55" fill="#f9c74f" font-size="9" font-family="sans-serif" text-anchor="middle">Radio/NTRIP</text>
 </g>
 <!-- Rover -->
 <g transform="translate(500,160)">
 <rect x="-30" y="-20" width="60" height="40" fill="#7209b7" rx="4"/>
 <text x="0" y="-2" fill="#fff" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">ROVER</text>
 <text x="0" y="14" fill="#fff" font-size="8" font-family="sans-serif" text-anchor="middle">Unknown coords</text>
 <circle cx="0" cy="35" r="8" fill="#f72585"/>
 <text x="0" y="55" fill="#7209b7" font-size="9" font-family="sans-serif" text-anchor="middle">Receives corr.</text>
 </g>
 <!-- Data link -->
 <line x1="150" y1="160" x2="470" y2="160" stroke="#f72585" stroke-width="3" marker-end="url(#a)"/>
 <text x="310" y="150" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">RTCM 3.x / NTRIP corrections</text>
 <!-- Output -->
 <g transform="translate(500,240)">
 <rect x="-40" y="-20" width="80" height="40" fill="#06d6a0" rx="4"/>
 <text x="0" y="5" fill="#1a1a2e" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">OUTPUT</text>
 <text x="0" y="20" fill="#1a1a2e" font-size="9" font-family="sans-serif" text-anchor="middle">cm‑level ENU</text>
 </g>
 <defs><marker id="a" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#f72585"/></marker></defs>
</svg>

---

## 8. Practical Tips for Indonesia

| Tip | Explanation |
|-----|-------------|
| **Network RTK preferred** | Baseline > 20 km with single base degrades rapidly due to equatorial ionosphere. |
| **CORS network** | BIG operates CORS (CORS‑ID); use via NTRIP (e.g., `cors.big.go.id:2101`). |
| **Elevation mask** | Use ≥ 15° to reduce multipath and low‑elevation ionospheric noise. |
| **Dual‑frequency** | Mandatory for ionosphere‑free combination and faster AR. |
| **Ambiguity validation** | Use ratio test threshold ≥ 3.0; verify with check points. |
| **Coordinate system** | Output typically in UTM zone 48–54 N (WGS84) or TM‑3° (ID74/DGN95). |

---

## 9. Related

- [[GNSS]] – the broader satellite positioning framework.

- [[PPP]] – alternative that does not require a base station.

- [[Local ENU NEU]] – RTK output frame.

- [[Least Squares Adjustment]] – used in baseline processing.

- [[Ambiguity Resolution|Integer Ambiguity Resolution]] – the mathematical core.

---

## 10. References

- Teunissen, P.J.G., *The Least‑Squares Ambiguity Decorrelation Adjustment (LAMBDA): A Method for Fast GPS Integer Ambiguity Estimation*, J. Geodesy 70, 65‑82, 1995. DOI:10.1007/BF00863419

- Hofmann‑Wellenhof, B., Lichtenegger, H., Wasle, E., *GNSS – Global Navigation Satellite Systems: GPS, GLONASS, Galileo, and more*, Springer, 2008.

- RTCM Special Committee No. 104, *RTCM Standard 10403.x for Differential GNSS (RTK) Services*, 2023.

- IGS State Space Representation (SSR) Format, https://kb.igs.org/hc/en-us/articles/210056498

- BIG Indonesia, *Pedoman Penggunaan Layanan CORS‑ID*, 2022. https://tanahair.indonesia.go.id/

➡️ [[Geodesy MOC]] · [[Basic Geodesy]] · [[Kurikulum Teknik Geodesi]]