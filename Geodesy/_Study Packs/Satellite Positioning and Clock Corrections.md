---
aliases: [Satellite Positioning, GPS Clock Corrections, GNSS Positioning, Clock Corrections Study]
tags: [geodesy, physics, GPS, GNSS, satellite, clock-corrections, relativistic, ionosphere, study-pack]
created: 2026-07-25
subject: Geodesy & Physics
type: study-pack
status: complete
---

# Satellite Positioning and Clock Corrections

## A Cross-Subject Study Pack: Physics × Geodesy

> **Purpose:** This study pack bridges **classical/relativistic physics** and **geodetic science** through the lens of satellite positioning. It is written for an Indonesian Geodesy undergraduate — starting from fundamentals and building toward advanced topics. Every section connects the underlying physics to its practical geodetic application.

---

## Table of Contents

1. [[#1. What Is Satellite Positioning?]]
2. [[#2. The Physics of Signal Propagation]]
3. [[#3. Clock Types and Time Systems]]
4. [[#4. Relativistic Corrections]]
5. [[#5. Ionospheric and Tropospheric Delays]]
6. [[#6. Carrier Phase vs Pseudorange]]
7. [[#7. How Clock Errors Affect Position Accuracy]]
8. [[#8. Real-World Applications]]
9. [[#9. Research Papers and Resources]]

---

## 1. What Is Satellite Positioning?

### 1.1 The Big Idea

Satellite positioning — most commonly **GPS** (Global Positioning System), but now part of a larger family called **GNSS** (Global Navigation Satellite System) — determines your 3D position on (or near) Earth by measuring the **time it takes for radio signals to travel from multiple satellites to your receiver**.

The core insight is deceptively simple:

> **Distance = Speed × Time**
>
> If you know the signal travels at the speed of light, *c*, and you measure the travel time Δt, then the range is **ρ = c · Δt**.

But "knowing the travel time" requires both the satellite's clock and your receiver's clock to agree perfectly — which they don't. This **clock offset** is the central challenge of GNSS positioning.

### 1.2 GNSS Constellations

| Constellation | Country/Region | Satellites | Signal Frequencies |
|---|---|---|---|
| **GPS** (NAVSTAR) | USA | 31 (active) | L1 (1575.42 MHz), L2 (1227.60 MHz), L5 (1176.45 MHz) |
| **GLONASS** | Russia | 24 | L1/L2 (FDMA + CDMA) |
| **Galileo** | EU | 30 (planned) | E1, E5a, E5b, E6 |
| **BeiDou** (BDS) | China | 45+ (BDS-3) | B1, B2, B3 |
| **QZSS** | Japan | 4 | L1, L2, L5 (augments GPS) |
| **NavIC** (IRNSS) | India | 7 | L5, S-band |

Modern receivers use **multi-constellation, multi-frequency** tracking — using signals from 20–40+ satellites simultaneously.

### 1.3 How Positioning Works

1. **Satellite ephemeris** (broadcast orbit parameters) tells you *where each satellite is* at the time of transmission.
2. **Receiver measures pseudorange** — the apparent distance to each satellite.
3. **Minimum of 4 satellites needed** because there are 4 unknowns:
 - 3D position: **(X, Y, Z)**
 - Receiver clock offset: **δt**

The observation equation for satellite *i*:
$$
\rho_i = \sqrt{(X_i - X_u)^2 + (Y_i - Y_u)^2 + (Z_i - Z_u)^2} + c \cdot \delta t_u + \varepsilon_i$ $Where:

- ρ_i = measured pseudorange to satellite i

- (X_i, Y_i, Z_i) = satellite position (from ephemeris)

- (X_u, Y_u, Z_u) = receiver position (unknown)

- δt_u = receiver clock offset (unknown)

- ε_i = all remaining errors (atmospheric, multipath, noise, ...)

With 4+ satellites, this becomes a **least-squares problem** (overdetermined system).

### 🧭 Geodetic Application
Satellite positioning is the backbone of **geodetic reference frames**. The International Terrestrial Reference Frame (ITRF) is realized through GNSS observations from a global network of permanent stations. Indonesian geodetic work — from cadastral surveying to tectonic plate monitoring — all starts here.

### 📚 Resources

- [GPS.gov — How GPS Works](https://www.gps.gov/systems/gps/performance/accuracy/) (US Government, free)

- Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS – Global Navigation Satellite Systems: GPS, GLONASS, Galileo, and More*. Springer. (Check university library or SpringerOpen chapters)

- Montenbruck, O. et al. (2017). "The Multi-GNSS Experiment (MGEX) of the International GNSS Service." *Journal of Geodesy*, 91, 737–748. [Open Access](https://doi.org/10.1007/s00190-017-1008-9)

---

## 2. The Physics of Signal Propagation

### 2.1 Electromagnetic Waves

GPS signals are **electromagnetic (EM) waves** — oscillating electric and magnetic fields propagating through space. The fundamental physics
$$
c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 299{,}792{,}458 \text{ m/s}$ $Where:

- μ₀ = permeability of free space (4π × 10⁻⁷ H/m)

- ε₀ = permittivity of free space (8.854 × 10⁻¹² F/m)

**Key insight:** The speed of light *c* is not arbitrary — it's a fundamental constant derived from the electromagnetic properties of vacuum.

### 2.2 Signal Structure

GPS L1 signal (1575.42 MHz) carries:

- **Coarse/Acquisition (C/A) code** — chip rate 1.023 MHz, wavelength λ ≈ 19.05 cm

- **Navigation message** — 50 bps data with ephemeris, almanac, clock corrections

- **Encrypted P(Y) code** — military use, chip rate 10.23 MHz

The signal is a **spread-spectrum** signal — the C/A code "spreads" the low-rate navigation data across a wider bandwidth, making it resistant to interference.

### 2.3 Propagation in Vacuum vs. Media

In vacuum, all EM waves travel at *c*, regardless of frequency. But in **material media** (atmosphere, ionosphere), the effective speed decreases
$$v = \frac{c}{n}$ $where *n* is the **refractive index** of the medium (n > 1 for atmosphere).

The travel time becomes
$$
\Delta t = \int_{\text{satellite}}^{\text{receiver}} \frac{n(s)}{c} \, ds$ $This integral along the signal path is the **true geometric range** divided by *c*, plus all the delay contributions.

### 2.4 Group Delay vs. Phase Velocity

Two critical concepts from wave physics:

- **Phase velocity** (v_p): speed at which the carrier wave's phase propagates

- **Group velocity** (v_g): speed at which the modulation (code/pseudorange) propagate
s
$$
v_g = v_p - \lambda \frac{dv_p}{d\lambda} $ $In dispersive media (like the ionosphere), v_p ≠ v_g, and they have **opposite signs** for the ionospheric effect:

- The **code (pseudorange)** is **delayed** (v_g < c)

- The **carrier phase** is **advanced** (v_p > c)

This is why the **ionospheric code delay = − ionospheric phase advance** — a critical relationship for dual-frequency corrections.

### 2.5 Signal Attenuation

By the time GPS signals reach the ground, they are incredibly weak — about **−130 dBm** (roughly 10⁻¹⁶ watts). For context, this is about 1000 times weaker than the signal from a GPS satellite received at the top of the atmosphere. The signal-to-noise ratio (C/N₀) is typically 35–50 dB-Hz.

### 🧭 Geodetic Application
Understanding EM propagation physics is essential for modeling **signal delays** in geodetic positioning. The distinction between phase velocity and group velocity directly explains why carrier-phase observations have opposite ionospheric errors from code observations — a principle exploited in dual-frequency geodetic receivers.

### 📚 Resources

- Halliday, D., Resnick, R., & Walker, J. — *Fundamentals of Physics*, Ch. 32 (Electromagnetic Waves)

- Klobuchar, J.A. (1991). "Ionospheric Algorithms for the GPS User." *Navigation*, 38(1), 29–56. [Available via ION archive](https://www.ion.org/publications/abstract.cfm?articleID=1668)

- Kaplan, E.D. & Hegarty, C.J. (2017). *Understanding GPS/GNSS: Principles and Applications*, 3rd ed. Artech House. (University library access recommended)

---

## 3. Clock Types and Time Systems

### 3.1 Why Timing is Everything

In GNSS, **1 nanosecond of timing error = 30 centimeters of range error** (since c ≈ 0.3 m/ns). This means clocks need to be accurate to a few nanoseconds — or better.

### 3.2 Atomic Clocks

Atomic clocks are the heart of both GPS satellites and ground control stations. They work on the principle that atoms absorb and emit electromagnetic radiation at **precisely defined frequencies**.

**Cesium (¹³³Cs) clocks:**

- Transition: hyperfine splitting of the ground state

- Frequency: 9,192,631,770 Hz (this *defines* the SI second)

- Stability: ~10⁻¹³ over 1 day

**Rubidium (⁸⁷Rb) clocks:**

- Transition: ground-state hyperfine splitting at 6.834 GHz

- Stability: ~10⁻¹² over 1 day

- Used on most GPS IIF and GPS III satellites

**Hydrogen maser:**

- Stability: ~10⁻¹⁵ over 1 day

- Used on ground reference stations (IGS network)

- Not used on satellites (too large/heavy)

**Quartz oscillators (receivers):**

- Stability: ~10⁻⁹ to 10⁻¹⁰ over 1 day

- Cheap, small, power-efficient

- The *receiver clock error* is the 4th unknown solved in the positioning equations

### 3.3 GPS Time System

GPS has its own time reference:

| Time System | Origin | Reference | Note |
|---|---|---|---|
| **GPS Time (GPST)** | Jan 6, 1980 00:00:00 UTC | 12 constant cesium clocks at USNO + satellite clocks | Continuous, no leap seconds |
| **UTC** | Same epoch (effectively) | Coordinated Universal Time | Has leap seconds; GPST = UTC + leap seconds (currently +18 s) |
| **GLONASS Time (GLONASST)** | Same epoch | Moscow segment of UTC(SU) | Follows UTC, includes leap seconds |
| **Galileo System Time (GST)** | Aug 21, 1999 | UTC reference, no leap seconds | Similar design philosophy to GPS |
| **BeiDou Time (BDT)** | Jan 1, 2006 | UTC reference, no leap seconds | Synchronized to UTC via NTSC China |

**Critical point for geodesists:** GPS navigation messages broadcast a **clock correction polynomial** for each satellite
$$
\delta t^{SV} = a_{f0} + a_{f1}(t - t_{oc}) + a_{f2}(t - t_{oc})^2$ $Where:

- a_f0 = clock bias (seconds)

- a_f1 = clock drift (seconds/second)

- a_f2 = clock drift rate (seconds/second²)

- t_oc = reference epoch for the clock parameters

- t = GPS time of signal transmission

### 3.4 Time Transfer Techniques

Precise geodetic work requires comparing clocks across continents. Methods include:

- **GPS Carrier-Phase Time Transfer** — uses phase measurements to compare remote clocks at sub-nanosecond precision

- **Two-Way Satellite Time Transfer (TWSTT)** — signals exchanged in both directions to cancel path delays

- **Precise Point Positioning (PPP)** — uses precise satellite clock products to achieve time transfer accuracy of ~0.1 ns

### 🧭 Geodetic Application
The International GNSS Service (IGS) produces **precise satellite clock corrections** (at 5-second or 30-second intervals) that are essential for geodetic-quality positioning. These products effectively turn GPS satellites into portable atomic clocks — enabling time transfer with stability that rivals dedicated two-way methods.

### 📚 Resources

- [NIST — Atomic Clocks](https://www.nist.gov/pml/time-and-frequency-division/atomic-clocks-and-frequency-standard) (free, authoritative)

- Lewandowski, W. et al. (2012). "International Atomic Time and the BIPM." *IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control*, 59(3).

- Petit, G. & Luzum, B. (2010). *IERS Conventions (2010)*, Ch. 9 (Time Scales). [BIPM, free PDF](https://www.iers.org/IERS/EN/Publications/TechnicalNotes/tn36.html)

- Ashby, N. (2003). "Relativity in the Global Positioning System." *Living Reviews in Relativity*, 6, 1. [Open Access](https://doi.org/10.12942/lrr-2003-1)

---

## 4. Relativistic Corrections

> **This is where Physics and Geodesy meet most dramatically.** Without relativistic corrections, GPS positions would drift by about **10 km per day**.

### 4.1 Special Relativity — Time Dilation Due to Velocity

GPS satellites orbit at approximately 3.874 km/s. According to **special relativity**, a moving clock runs slower than a stationary one
$$
\Delta t' = \frac{\Delta t}{\sqrt{1 - v^2/c^2}} \approx \Delta t \left(1 + \frac{v^2}{2c^2}\right)$ $The **slowing factor** for GPS satellites $$\frac{v^2}{2c^2} = \frac{(3874)^2}{2(299{,}792{,}458)^2} \approx -8.34 \times 10^{-11} $ $This means satellite clocks **run slow** by about **−7.2 μs/day** due to their orbital velocity.

### 4.2 General Relativity — Gravitational Time Dilation

GPS satellites orbit at ~20,200 km altitude, where the gravitational potential is weaker than on Earth's surface. According to **general relativity**, clocks in weaker gravitational fields run **faster**
$$
\Delta t' = \Delta t \left(1 + \frac{GM}{c^2} \left(\frac{1}{R_{\text{Earth}}} - \frac{1}{R_{\text{sat}}}\right)\right)$ $Where:

- G = gravitational constant (6.674 × 10⁻¹¹ N⋅m²/kg²)

- M = mass of Earth (5.972 × 10²⁴ kg)

- R_Earth = Earth's equatorial radius (6,378 km)

- R_sat = orbital radius of GPS satellite (~26,560 km)

The **speeding factor**
$$
\frac{GM}{c^2}\left(\frac{1}{R_E} - \frac{1}{R_s}\right) \approx +4.59 \times 10^{-10} $ $This means satellite clocks **run fast** by about **+45.9 μs/day** due to gravitational effects.

### 4.3 The Net Relativistic Effect

| Effect | Sign | Magnitude (per day) |
|---|---|---|
| Special relativity (velocity) | Clock runs **slow** | −7.2 μs/day |
| General relativity (gravity) | Clock runs **fast** | +45.9 μs/day |
| **Net effect** | Clock runs **fast** | **+38.7 μs/day** |

**38.7 microseconds per day × c ≈ 11.6 km per day!**

If uncorrected, GPS would become useless within hours.

### 4.4 How GPS Corrects for Relativity

The correction is applied at the **satellite clock level** in two ways:

**A. Pre-launch frequency adjustment:**
The satellite's clock frequency is intentionally offset **before launch**. The fundamental frequency is
$$
f_{\text{actual}} = 10.229999999543 \text{ MHz} \quad \text{(instead of 10.23 MHz)} $ $This counteracts the **net constant relativistic effect** (the +38.7 μs/day).

**B. In-orbit relativistic correction (broadcast):**
The remaining **eccentric orbit effect** varies with the satellite's position in its elliptical orbit. This is corrected by the **relativistic correction** term in the navigation message
$$
\Delta t_r = -2\frac{\sqrt{G \cdot M_A}}{c^2} \cdot e \sqrt{a} \sin E_k$ $Where:

- e = eccentricity of satellite orbit

- a = semi-major axis of orbit

- E_k = eccentric anomaly at time of transmission

- M_A = mass of Earth

- G = gravitational constant

This term accounts for the fact that the satellite's speed (and altitude) varies as it moves through its elliptical orbit, causing the relativistic effect to oscillate.

### 4.5 Higher-Order Relativistic Effects

For the most precise geodetic applications (sub-millimeter level), additional relativistic terms matter:

- **Lense-Thirring (frame-dragging):** Earth's rotation "drags" spacetime; effect is ~2 mm in range

- **Geodetic precession:** ~0.01 mm — currently negligible for most applications

- **Second-order Doppler:** included in the standard relativistic correction

- **Signal propagation curvature:** gravitational bending of signal path (~0.01 mm)

### 🧭 Geodetic Application
Relativistic corrections are **not optional** — they are built into the GPS system design. But geodesists also need to understand them for: (1) precise time transfer across the IGS network, (2) verifying the consistency of ITRF reference frame realizations, and (3) the subtle relativistic effects in inter-constellation combinations (GPS+GLONASS+Galileo have different correction implementations).

### 📚 Resources

- Ashby, N. (2003). "Relativity in the Global Positioning System." *Living Reviews in Relativity*, 6, 1. [Open Access](https://doi.org/10.12942/lrr-2003-1) — **THE definitive reference**

- GPS Interface Specification (IS-GPS-200), Rev. M. [GPS.gov](https://www.gps.gov/technical/icwg/) — Section 20.3.3.3.3.0 (Relativistic Corrections)

- [Verdult, F. (2015). "The GPS system explained from a relativity viewpoint"](https://www.astron.nl/onderzoek/onderzoekslijnen/gnss) — TU Delft MSc thesis, freely available

- Einstein, A. (1905). *Zur Elektrodynamik bewegter Körper* (Special Relativity). [English translation, free](https://www.fourmilab.ch/etexts/einstein/specrel/specrel.pdf)

- Einstein, A. (1916). "The Foundation of the General Theory of Relativity." [English translation, free](https://www.phy.pku.edu.cn/~qhcao/resources/file/Einstein_GeneralRelativity.pdf)

---

## 5. Ionospheric and Tropospheric Delays

### 5.1 Overview of Atmospheric Layers

The signal from a GPS satellite passes through several atmospheric layers, each causing a different type of delay:

| Layer | Altitude | Effect on GPS Signal | Type |
|---|---|---|---|
| **Ionosphere** | 60–1000 km | Dispersive delay (frequency-dependent) | Plasma of free electrons |
| **Troposphere** | 0–~15 km | Non-dispersive delay (same for all frequencies) | Neutral gas + water vapor |
| **Stratosphere** | 15–50 km | Included in tropospheric models | Also neutral gas |

The **ionospheric delay** is the **largest error source** in GPS positioning (~2–50 meters depending on solar activity). The **tropospheric delay** adds another ~2.3 meters at zenith (up to ~25 meters at low elevation angles).

### 5.2 Ionospheric Delay — The Physics

The ionosphere is a plasma — ionized gas with free electrons and ions. For EM waves propagating through a plasma, the **refractive index** is
$$n = \sqrt{1 - \frac{f_p^2}{f^2}}$ $Where:

- f_p = plasma frequency ≈ 9√(N_e) Hz (N_e = electron density in electrons/m³)

- f = GPS signal frequency (e.g., L1 = 1575.42 MHz)

For GPS frequencies (f >> f_p), this simplifies to
$$
n \approx 1 - \frac{f_p^2}{2f^2} = 1 - \frac{40.3 \cdot N_e}{c^2 \cdot f^2} $ $The **ionospheric range delay** (group delay for pseudorange)$$ \Delta \rho_{\text{iono}} = +\frac{40.3}{f^2} \int_{\text{path}} N_e \, ds = \frac{40.3 \cdot \text{STEC}}{f^2} $ $Where **STEC** = Slant Total Electron Content (in electrons/m²) — the integral of electron density along the signal path.

**Key relationships:**

- Delay ∝ 1/f² (dispersive — different for L1 and L2)

- Delay increases with solar activity (higher electron density)

- Delay is worst near the equator and at the **equatorial ionization anomaly (EIA)** — directly affecting Indonesia!

### 5.3 Dual-Frequency Ionospheric Correction

Because the ionospheric delay is frequency-dependent, a **dual-frequency receiver** can eliminate the first-order ionospheric effect (~99.9% of total)
$$
\rho_{\text{iono-free}} = \frac{f_1^2 \cdot \rho_1 - f_2^2 \cdot \rho_2}{f_1^2 - f_2^2} $ $Where ρ₁ and ρ₂ are pseudoranges on L1 and L2 respectively.

This is the **ionosphere-free linear combination** — the standard workhorse of geodetic positioning.

**For single-frequency users**, the **Klobuchar model** (broadcast in the navigation message) removes about 50–60% of the ionospheric delay
$$
\Delta t_{\text{iono}} = F \left[5 \times 10^{-9} + A \left(1 - \frac{x^2}{2} + \frac{x^4}{24}\right)\right]$ $Where F is an obliquity factor, A is the amplitude (from broadcast coefficients α₀–α₃), and x is the phase of the cosine curve.

### 5.4 Tropospheric Delay — The Physics

The troposphere is a **neutral atmosphere** (no free electrons). Its refractivity is
$$
(n - 1) \times 10^6 = 77.6 \frac{P}{T} + 3.73 \times 10^5 \frac{e}{T^2} $ $Where:

- P = total atmospheric pressure (hPa)

- T = temperature (Kelvin)

- e = water vapor partial pressure (hPa)

The first term is the **hydrostatic** (dry) component (~90% of total delay). The second term is the **wet** component (~10% but harder to model).

**Zenith delays:**

- Zenith Hydrostatic Delay (ZHD): ~2.3 m (can be precisely modeled from surface pressure)

- Zenith Wet Delay (ZWD): ~0.01–0.3 m (highly variable, depends on water vapor)

**Mapping to slant delay:*
*
$$
\Delta \rho_{\text{tropo}} = m_h(\theta) \cdot ZHD + m_w(\theta) \cdot ZWD$ $Where m_h and m_w are **mapping functions** (hydrostatic and wet) that depend on the satellite elevation angle θ. Common mapping functions: **VMF1**, **NMF** (Niell Mapping Function), **GMF** (Global Mapping Function).

### 5.5 Troposphere Estimation in Geodetic Positioning

In geodetic processing (e.g., Bernese, GAMIT, RTNet), the ZHD is typically **fixed** from a numerical weather model, and the **ZWD is estimated** as an additional parameter in the least-squares adjustment. This is critical because:

- ZHD is predictable to ~1 mm from surface pressure

- ZWD varies rapidly and must be estimated from the GNSS observations themselves

- This makes GNSS a powerful **atmospheric sensing tool** — "GNSS meteorology"

### 🧭 Geodetic Application
Indonesia sits near the **geomagnetic equator**, where ionospheric delays are among the **largest in the world** (especially during solar maximum). The equatorial ionization anomaly (EIA) creates strong electron density gradients that make single-frequency positioning particularly challenging. This is a major motivation for deploying **multi-frequency receivers** and **dense CORS networks** in Indonesia (e.g., BIG's CORS network).

The tropospheric delay estimation from GNSS is used operationally for **weather forecasting** in Indonesia — water vapor fields from GPS observations are assimilated into BMKG's numerical weather prediction models.

### 📚 Resources

- Klobuchar, J.A. (1987). "Design and Characteristics of the GPS Ionospheric Time Delay Algorithm." *Proceedings of ION GPS-87*. [Free via ION archive](https://www.ion.org/)

- Saastamoinen, J. (1972). "Atmospheric Correction for the Troposphere and Stratosphere in Ranging Satellites." *Proc. 1st Int. Symp. on Satellite Geodesy*. — Classic tropospheric delay model

- Boehm, J. et al. (2006). "Mapping functions for tropospheric delay estimates." *Journal of Geodesy*, 79, 192–204. [Open Access](https://doi.org/10.1007/s00190-005-0027-x)

- [CODE (Center for Orbit Determination in Europe) ionosphere products](https://www.aiub.unibe.ch/navigation/gnss_research/gnss_data_and_products/ionosphere) — free ionosphere maps

- Hernández-Pajares, M. et al. (2009). "The ionosphere: effects, modeling, and monitoring." *Satellite Navigation and Communication Systems*, Springer.

---

## 6. Carrier Phase vs Pseudorange

### 6.1 Pseudorange — The "Ruler" Approach

**Pseudorange** is the measured time delay multiplied by the speed of light
$$\rho = c \cdot \Delta t$ $The code (C/A or P-code) on the satellite signal is correlated with a locally generated replica in the receiver. The offset at maximum correlation gives the travel time.

**Characteristics:**

- **Unambiguous** — you get the full range directly

- **Noisy** — precision is ~15–30 cm for C/A code, ~15 cm for P-code

- **Affordable** — single-frequency receivers can measure it

- **Affected by multipath** — code multipath can be 1–2 meters

### 6.2 Carrier Phase — The "Ruler with Marks" Approach

The carrier signal itself (e.g., L1 at 1575.42 MHz, wavelength λ ≈ 19.05 cm) can be tracked as a continuous phase measurement. The carrier phase observation is
$$
\Phi = \rho + c(\delta t_u - \delta t^{SV}) + \lambda N - I_{\Phi} + T + \varepsilon_{\Phi} $ $Where:

- Φ = carrier phase measurement (in meters)

- ρ = geometric range

- N = **integer ambiguity** (unknown number of whole cycles between satellite and receiver)

- I_Φ = ionospheric phase advance (opposite sign to pseudorange delay)

- T = tropospheric delay (same for both)

- ε_Φ = measurement noise (~1–2 mm)

### 6.3 The Integer Ambiguity Problem

The carrier phase is like a ruler with **millimeter marks but no numbers** — you know the fractional part precisely, but you don't know how many whole wavelengths are between you and the satellite.

**Resolution of the ambiguity N is the key challenge of high-precision GNSS:**

- **Static positioning:** ambiguity resolution typically takes 15–30 minutes for convergence

- **Kinematic positioning:** requires external constraints (e.g., RTK corrections)

- Methods: LAMBDA method, least-squares ambiguity search, single-difference / double-difference processing

### 6.4 Comparison Table

| Property | Pseudorange | Carrier Phase |
|---|---|---|
| **Precision** | ~15–30 cm | ~1–2 mm |
| **Ambiguity** | Unambiguous | Integer ambiguity must be resolved |
| **Noise** | Higher | Much lower |
| **Multipath sensitivity** | Moderate (code-dependent) | Lower (but cycle slips possible) |
| **Ionospheric effect** | Delay (+ sign) | Advance (− sign) |
| **Tracking requirement** | Continuous signal lock needed | Continuous phase lock needed |
| **Time to initialize** | Immediate | Minutes to hours (for static) |

### 6.5 Linear Combinations

Geodesists use combinations of measurements to exploit the strengths of each:

| Combination | Formula | Purpose |
|---|---|---|
| **Ionosphere-free (LIF)** | (f₁²·Φ₁ − f₂²·Φ₂)/(f₁² − f₂²) | Removes 99.9% ionospheric delay |
| **Wide-lane (WL)** | Φ_WL = Φ₁ − Φ₂ (λ_WL ≈ 86.2 cm) | Easier ambiguity resolution |
| **Narrow-lane (NL)** | Φ_NL = Φ₁ + (f₂/f₁)·Φ₂ (λ_NL ≈ 10.7 cm) | Higher precision |
| **Geometry-free (GF)** | Φ₁ − (f₁/f₂)²·Φ₂ | Ionosphere monitoring |
| **Melbourne-Wübbena** | Wide-lane pseudorange − Narrow-lane phase | Cycle slip detection |

### 🧭 Geodetic Application
**Carrier phase measurements are the foundation of geodetic positioning.** Without them, the mm-level precision required for tectonic monitoring, deformation analysis, and reference frame realization would be impossible. The integer ambiguity resolution process — particularly the **LAMBDA method** developed at TU Delft — is one of the most important algorithmic contributions in modern geodesy.

### 📚 Resources

- Teunissen, P.J.G. & Kleusberg, A. (1998). *GPS for Geodesy*, 2nd ed. Springer. [Chapters freely available via SpringerLink at university libraries](https://doi.org/10.1007/978-3-642-72013-0)

- Teunissen, P.J.G. (1995). "The Least-Squares Ambiguity Decorrelation Adjustment." *Journal of Geodesy*, 69, 361–373. [Open Access](https://doi.org/10.1007/BF00806876) — **The LAMBDA method paper**

- Blewitt, G. (1997). "Carrier Phase Ambiguity Resolution for the Global Positioning System Applied to Geodetic Baselines up to 2000 km." *Journal of Geophysical Research*, 102(B8), 17,293–17,310.

- [RINEX format specification](https://www.aiub.unibe.ch/download/gnss/RINEX304.pdf) — Standard data format for GNSS observations (free)

---

## 7. How Clock Errors Affect Position Accuracy

### 7.1 The Fundamental Error Equation

From the basic observation equation
$$
\rho_i = \sqrt{(X_i - X_u)^2 + (Y_i - Y_u)^2 + (Z_i - Z_u)^2} + c \cdot \delta t_u + \varepsilon_i$ $A clock error of δt directly causes a range error of c·δt. But the effect on **position** depends on **satellite geometry**.

### 7.2 Satellite Geometry — GDOP

The **Geometric Dilution of Precision (GDOP)** quantifies how satellite geometry amplifies range errors into position errors
$$
\sigma_{\text{position}} = \text{GDOP} \times \sigma_{\text{range}} $ $| GDOP Value | Quality | Position Error (σ_range = 1 m) |
|---|---|---|
| 1 | Ideal | 1 m |
| 2 | Excellent | 2 m |
| 3 | Good | 3 m |
| 5 | Moderate | 5 m |
| 10 | Poor | 10 m |
| >20 | Very poor | >20 m |

The **DOP components** decompose into:

- **PDOP** (Position DOP): 3D position (X, Y, Z) × σ_range

- **HDOP** (Horizontal DOP): horizontal position × σ_range

- **VDOP** (Vertical DOP): vertical position × σ_range

- **TDOP** (Time DOP): receiver clock error × σ_range / c

**GDOP² = PDOP² + TDOP²**

### 7.3 Specific Clock Error Scenarios

#### Scenario 1: Receiver clock error (solved as unknown)
The receiver clock offset is estimated as the 4th parameter — it doesn't directly degrade position, but **it consumes one degree of freedom**. With only 4 satellites, you get no redundancy. With more satellites, the clock error can be estimated precisely and its effect on position is minimized by good geometry.

#### Scenario 2: Satellite clock error (broadcast)
If a satellite's broadcast clock correction has an error of 1 ns:

- Range error: 0.3 m

- This is partially mitigated by **differential techniques** (both base and rover see similar errors)

- In **single-point positioning (SPP)**, residual satellite clock errors of 1–5 ns contribute ~0.3–1.5 m to position error

#### Scenario 3: Receiver clock instability
Receiver oscillators drift by ~1 μs/second. Without correction:

- Position error accumulates at ~300 m/s — position is meaningless after 1 second

- That's why the receiver clock is estimated continuously as the 4th unknown

### 7.4 Error Budget — Where Do Errors Come From?

For **standard single-point positioning (SPP)**:

| Error Source | 1σ Range Error (m) | Notes |
|---|---|---|
| Satellite clock (broadcast) | 1–5 | Corrected by navigation message |
| Satellite ephemeris | 1–3 | From broadcast navigation data |
| **Ionosphere** | **2–50** | Largest single error; solar activity dependent |
| Troposphere | 0.5–5 | Depends on elevation angle |
| Multipath | 0.5–2 | Site-dependent |
| Receiver noise | 0.5–1 | Depends on receiver quality |
| **Combined (RSS)** | **~5–15 m** | Typical for L1 SPP |

For **precise positioning (carrier-phase-based)**:

| Error Source | Residual After Correction (mm) |
|---|---|
| Satellite clock (precise products) | 0.01–0.1 |
| Ionosphere (dual-freq) | 1–3 |
| Troposphere (estimated) | 5–10 (vertical) |
| Multipath | 5–15 |
| Receiver noise | 1–2 |
| Ambiguity resolution | 0–5 (if resolved) |
| **Combined** | **~2–10 mm (horizontal)** |

### 7.5 Error Propagation Mathematics

The least-squares solution for position
$$\hat{x} = (A^T P A)^{-1} A^T P L$ $The covariance matrix of the estimated parameters $$Q_{xx} = (A^T P A)^{-1}$ $Where A is the design matrix (geometry), P is the weight matrix (inverse of observation variance), and L is the observation-minus-computed vector. The diagonal elements of Q_xx give the variance of each estimated parameter — and GDOP = √(trace(Q_xx)).

### 🧭 Geodetic Application
Understanding the error budget is essential for **network design** (where to place CORS stations), **survey planning** (when to observe for best results), and **data quality assessment** (is my solution reliable?). For Indonesian geodesy, the ionospheric error budget is particularly critical — during **solar maximum** (the next expected around 2025–2026), ionospheric errors over equatorial regions can exceed 50 meters for single-frequency users.

### 📚 Resources

- Hofmann-Wellenhof, B. et al. (2008). *GNSS — Global Navigation Satellite Systems*. Springer. Ch. 6 (Error Budget)

- Langley, R.B. (1997). "GPS Receiver System Noise." *GPS World*, 8(6), 47–53. [Classic reference on error characterization](https://gpsworld.com/)

- [Online GPS Error Simulator — NGS](https://www.ngs.noaa.gov/tools/) — Free tools from NOAA's National Geodetic Survey

- Misra, P. & Enge, P. (2011). *Global Positioning System: Signals, Measurements, and Performance*, 2nd ed. Ganga-Jamuna Press. [Free PDF from authors' website](https://www.ae.gatech.edu/people/penge/GPS_book.html)

---

## 8. Real-World Applications

### 8.1 Precise Point Positioning (PPP)

**PPP** is a technique where a **single receiver** achieves centimeter-level accuracy using **precise satellite orbit and clock products** from a service like IGS — without needing a nearby base station.

**How it works:**
1. Use IGS precise satellite clock products (available with ~2-hour latency in real-time or post-processed)
2. Apply ionosphere-free linear combination
3. Estimate receiver position, clock, troposphere, and integer ambiguities
4. Wait for the filter to converge (30 min–2 hours depending on application)

**Achievable accuracy:**

- Static PPP: 1–3 mm (horizontal), 3–5 mm (vertical) after 24 hours

- Kinematic PPP: 2–5 cm (horizontal), 3–8 cm (vertical) after convergence

**Real-time PPP services:**
| Service | Provider | Accuracy | Latency |
|---|---|---|---|
| CSRS-PPP | NRCan (Canada) | 1–3 cm | Post-processed |
| GipsyX | JPL/NASA | 1–2 cm | Post-processed |
| BNC/BKG | BKG (Germany) | 2–5 cm | Real-time stream |
| PPP-RTK (e.g., Trimble CenterPoint) | Commercial | 2–4 cm | Real-time |

**Indonesian context:** PPP is increasingly used for **geodetic control surveys** in remote areas where establishing a CORS network is impractical. BIG (Badan Informasi Geospasial) is exploring PPP services for national spatial data infrastructure.

### 8.2 Real-Time Kinematic (RTK)

**RTK** achieves centimeter-level accuracy in real-time by using a **base station** (at a known coordinate) to compute **corrections** for the rover:

1. Base station observes satellites and computes the difference between observed and computed ranges
2. These **corrections are transmitted** to the rover (via radio, cellular internet, etc.)
3. The rover applies corrections, eliminating common errors (satellite clock, ephemeris, ionosphere, troposphere)
4. Carrier-phase ambiguity resolution gives centimeter-level position

**Key equation (single-difference between base B and rover R for satellite j):**
$$
\Delta \phi_{BR}^j = \Delta \rho_{BR}^j + c \cdot \Delta \delta t_{BR} + \lambda \cdot \Delta N_{BR}^j + \text{residuals} $$The atmospheric and satellite clock errors largely cancel in the differencing.

**RTK Performance:**

- Horizontal: 1–2 cm

- Vertical: 2–3 cm

- Initialization time: typically <30 seconds

- Range from base: typically 15–30 km (limited by spatial decorrelation of errors)

**Network RTK (NRTK):**
Instead of a single base, a **network of CORS** stations provides interpolated corrections:

- VRS (Virtual Reference Station): generates a virtual base at the rover's position

- FKP (Flächen-Korrektur-Parameter): sends area correction parameters

- MAC (Master-Auxiliary Concept): sends raw corrections from multiple reference stations

**Indonesian context:** BIG operates the **Indonesian CORS network (SOPAC-compatible)** and is developing NRTK services for surveying and mapping. The dense CORS network in Java and other developed islands supports real-time RTK via cellular correction services (e.g., BIGnet).

### 8.3 GNSS Geodesy Applications

| Application | Technique | Accuracy Required |
|---|---|---|
| **Tectonic plate monitoring** | Static GPS, 24+ hour sessions | 1–3 mm |
| **Coseismic/postseismic deformation** | Continuous GPS (cGPS) | 1–5 mm |
| **Sea-level monitoring** | GPS-Acoustic (GPS-A) | 1–2 cm (vertical) |
| **Crustal loading** | Network GPS | 1–3 mm |
| **Reference frame realization** | Global GNSS network (IGS) | 1–2 mm |
| **Precise timing** | GPS time transfer | 0.1–1 ns |
| **Navigation/surveying** | SPP/RTK | 1–3 m / 1–2 cm |
| **Precision agriculture** | RTK / PPP-RTK | 2–5 cm |
| **Autonomous vehicles** | PPP-RTK / INS-GNSS | 5–10 cm |

### 8.4 Indonesia-Specific Applications

- **BIG CORS Network:** Part of the global IGS network; used for ITRF realization in the Indonesian region

- **Tectonic monitoring:** Indonesia sits on the Pacific Ring of Fire — GNSS stations track convergence rates of the Indo-Australian, Eurasian, and Pacific plates (rates of 6–7 cm/year in Sumatra, ~3 cm/year in Java)

- **Land subsidence:** Jakarta is sinking at 1–25 cm/year in some areas — cGPS stations monitor this and support the new capital (Nusantara) project

- **Sea-level rise:** GPS-Acoustic observations around Indonesian coasts contribute to global sea-level records

- **Volcanic monitoring:** Continuous GPS at active volcanoes (Merapi, Sinabung, Agung) detects magma chamber inflation/deflation

- **Agricultural mapping:** RTK surveys for the national land cadastral system (ATR/BPN)

### 📚 Resources

- Zumberge, J.F. et al. (1997). "Precise point positioning for the efficient and robust analysis of GPS data from large networks." *Journal of Geophysical Research*, 102(B3), 5005–5017. [Open Access](https://doi.org/10.1029/96JB03860) — **The foundational PPP paper**

- Kouba, J. & Héroux, P. (2001). "Precise Point Positioning Using IGS Orbit and Clock Products." *GPS Solutions*, 5, 12–28. [Open Access](https://doi.org/10.1007/PL00127224)

- Rizos, C. (2002). "Alternatives to the GPS position determination system." *Survey Review*, 36, 155–164. — Overview of RTK and network RTK

- [IGS — International GNSS Service](https://igs.org/) — Free data, orbits, clock products

- [BIG — Badan Informasi Geospasial](https://www.big.go.id/) — Indonesia's national mapping/geospatial agency

- [UNAVCO (now EarthScope)](https://www.unavco.org/) — GPS data archive for geoscience (free data access)

---

## 9. Research Papers and Resources

### 9.1 Foundational Papers (Must-Reads)

1. **Ashby, N.** (2003). "Relativity in the Global Positioning System." *Living Reviews in Relativity*, 6, 1.
 - [https://doi.org/10.12942/lrr-2003-1](https://doi.org/10.12942/lrr-2003-1) — Open Access
 - *The definitive treatment of relativistic effects in GPS. Start here.*

2. **Teunissen, P.J.G.** (1995). "The Least-Squares Ambiguity Decorrelation Adjustment: A Method for Fast GPS Integer Ambiguity Resolution." *Journal of Geodesy*, 69, 361–373.
 - [https://doi.org/10.1007/BF00806876](https://doi.org/10.1007/BF00806876) — Open Access
 - *The LAMBDA method — the most important algorithm in high-precision GNSS.*

3. **Zumberge, J.F., Heflin, M.B., Jefferson, D.C., Watkins, M.M., & Webb, F.H.** (1997). "Precise point positioning for the efficient and robust analysis of GPS data from large networks." *Journal of Geophysical Research*, 102(B3), 5005–5017.
 - [https://doi.org/10.1029/96JB03860](https://doi.org/10.1029/96JB03860) — Open Access
 - *The paper that launched PPP.*

4. **Saastamoinen, J.** (1972). "Atmospheric Correction for the Troposphere and Stratosphere in Ranging Satellites." *Proc. 1st International Symposium on Satellite Geodesy*, pp. 247–251.
 - *The classic tropospheric delay model still used as a baseline today.*

5. **Klobuchar, J.A.** (1987). "Design and Characteristics of the GPS Ionospheric Time Delay Algorithm." *Proceedings of ION GPS-87*, pp. 280–290.
 - *The broadcast ionospheric model used by every single-frequency GPS receiver.*

### 9.2 Advanced / Recent Papers

6. **Kouba, J. & Héroux, P.** (2001). "Precise Point Positioning Using IGS Orbit and Clock Products." *GPS Solutions*, 5, 12–28.
 - [https://doi.org/10.1007/PL00127224](https://doi.org/10.1007/PL00127224) — Open Access

7. **Böhm, J., Niell, A., Tregoning, P., & Schuh, H.** (2006). "Global Mapping Functions (GMF): A new empirical mapping function based on numerical weather model data." *Geophysical Research Letters*, 33, L07301.
 - [https://doi.org/10.1029/2005GL025546](https://doi.org/10.1029/2005GL025546) — Open Access
 - *Modern tropospheric mapping function.*

8. **Hernández-Pajares, M. et al.** (2009). "The ionosphere: effects, modeling, and monitoring." *Satellite Systems and Mobile Communication*. Springer.
 - *Comprehensive ionosphere review for GNSS.*

9. **Dow, J.M., Neilan, R.E., & Rizos, C.** (2009). "The International GNSS Service in a changing landscape of Global Navigation Satellite Systems." *Journal of Geodesy*, 83, 191–198.
 - [https://doi.org/10.1007/s00190-008-0300-3](https://doi.org/10.1007/s00190-008-0300-3) — Open Access

10. **Montenbruck, O. et al.** (2017). "The Multi-GNSS Experiment (MGEX) of the International GNSS Service." *Journal of Geodesy*, 91, 737–748.
 - [https://doi.org/10.1007/s00190-017-1008-9](https://doi.org/10.1007/s00190-017-1008-9) — Open Access

### 9.3 Textbooks

| Title | Authors | Year | Notes |
|---|---|---|---|
| *GPS for Geodesy* | Teunissen & Kleusberg | 1998 | Classic geodetic GPS text |
| *Global Positioning System: Signals, Measurements, and Performance* | Misra & Enge | 2011 | Comprehensive; **free PDF from authors** |
| *GNSS — Global Navigation Satellite Systems* | Hofmann-Wellenhof et al. | 2008 | Multi-GNSS perspective |
| *Understanding GPS/GNSS: Principles and Applications* | Kaplan & Hegarty | 2017 | Industry standard |
| *Satellite Geodesy* | Seeber | 2003 | Broad geodetic perspective |
| *Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems* | Groves | 2013 | Good for understanding integration |

### 9.4 Free Online Courses and Lectures

- [MIT OpenCourseWare — GPS and Geodesy](https://ocw.mit.edu/) — Search for "GPS" or "geodesy"

- [TU Delft — GNSS course materials](https://gssc.igge.tudelft.nl/) — Lecture notes, exercises (free)

- [UNSW — GNSS course materials](https://www.gps.caltech.edu/~davidm/gnss/) — Links to lecture recordings

- [AUSPOS — Australian Online GPS Processing Service](https://ga.gov.au/scientific-topics/positioning-auspos) — Free GPS processing service from Geoscience Australia

- [BKG GNSS Data Processing](https://gnss.bkg.bund.de/) — Free tools and documentation

### 9.5 Open Data Sources

| Resource | URL | What It Provides |
|---|---|---|
| **IGS** | [igs.org](https://igs.org/) | Orbits, clocks, station data (free) |
| **CDDIS** | [cddis.nasa.gov](https://cddis.nasa.gov/) | NASA's GNSS data archive |
| **UNAVCO** | [unavco.org](https://www.unavco.org/) | Geoscience GPS data |
| **RINEX** | [aiub.unibe.ch](https://www.aiub.unibe.ch/) | IGS RINEX data (free) |
| **SOPAC** | [sopac.ucsd.edu](https://sopac.ucsd.edu/) | GNSS data archive and processing |
| **CODE** | [aiub.unibe.ch](https://www.aiub.unibe.ch/navigation/gnss_research/gnss_data_and_products/ionosphere) | Ionosphere products, precise orbits |

### 9.6 Software (Free/Open-Source)

| Software | Purpose | License |
|---|---|---|
| **RTKLIB** | Open-source GNSS processing (SPP, DGPS, RTK, PPP) | BSD |
| **GAMIT/GLOBK** | Geodetic GPS processing (MIT) | Academic free |
| **Bernese** | High-precision geodetic processing | Academic license |
| **AUSPOS** | Online GPS processing service | Free service |
| **CSRS-PPP** | Online PPP processing service | Free service |
| **GFZ GOPS** | GNSS data processing | Free |

---

## Summary: The Physics-Geodesy Bridge

```
 PHYSICS FOUNDATIONS GEODETIC APPLICATIONS
 ───────────────── ──────────────────────
 E&M wave propagation ────────────────► Signal delay modeling
 Speed of light (c) ──────────────────► Pseudorange computation
 Atomic clock physics ────────────────► Precise time transfer
 Special relativity ──────────────────► Satellite clock offset
 General relativity ──────────────────► Gravitational time dilation
 Plasma physics (ionosphere) ─────────► Dual-freq corrections
 Atmospheric thermodynamics ──────────► Tropospheric delay models
 Wave dispersion ─────────────────────► Group vs. phase velocity
 Error propagation ───────────────────► DOP analysis, adjustment
 Least-squares estimation ────────────► Position solution, PPP, RTK
```

**The central lesson:** Satellite positioning is fundamentally a physics problem applied to geodetic practice. Every centimeter of positioning accuracy comes from understanding and correcting the physics of signal propagation, timekeeping, and Earth's atmosphere.

---

> **Last updated:** 2026-07-25
> **Study pack by:** AIGIS for Geodesy × Physics cross-subject review
> **Next steps:** See [[Geoid]] for related geoid modeling study pack
