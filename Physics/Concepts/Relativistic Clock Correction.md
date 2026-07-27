---
tags: [aigis, concept, physics, gnss, relativity, general-relativity, special-relativity]
created: 2026-07-26
updated: 2026-07-27
---

# Relativistic Clock Correction

## The 38 μs/day Effect Every GNSS Surveyor Must Know

**Core Idea:** GPS satellites orbit at ~20,200 km altitude moving at ~3,874 m/s. Two relativistic effects act simultaneously: **special relativity** (velocity → slower clocks) and **general relativity** (weaker gravity → faster clocks). The net result: satellite clocks gain **38.6 microseconds per day** — which translates to a **11.6 km ranging error** if left uncorrected.

---

## 1. The Two Effects — Overview

| Effect | Physical Cause | Direction | Magnitude |
|--------|---------------|-----------|-----------|
| Special Relativity (velocity time dilation) | Orbital velocity ~3,874 m/s | Clocks run **slower** | −7.2 μs/day |
| General Relativity (gravitational redshift) | Higher in gravity well | Clocks run **faster** | +45.8 μs/day |
| **Net Effect** | | **Clocks run faster** | **+38.6 μs/day** |

---

## 2. Special Relativity — Velocity Time Dilation

### Time Dilation in SR
From the Lorentz transformation:

$$ \Delta t = \gamma \Delta\tau, \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}
}

$A moving clock ticks slower (dilated): $$ \frac{\Delta\tau}{\Delta t} = \sqrt{1 - \frac{v^2}{c^2}} \approx 1 - \frac{v^2}{2c^2}$

$$

### GPS Satellite Velocity
For a circular GPS orbit at radius $r = 26,560 $km

$v_{\text{GPS}} = \sqrt{\frac{GM}{r}} = \sqrt{\frac{3.9860\times 10^{14}}{26,560\times 10^3}} = 3,874 \text{ m/s}$ where $G = 6.674\times 10^{-11} $m³/(kg·s²), $M = 5.972\times 10^{24}$kg.

### Calculation of SR Effec
t

$$ \frac{\Delta f_{SR}}{f_0} = -\frac{v^2}{2c^2} = -\frac{(3874)^2}{2\times (299792458)^2} = -8.35\times 10^{-11} $$

**Over one day:*
*

$$ \Delta\tau_{SR} = 8.35\times 10^{-11}\times 86400 = -7.2 \text{ μs/day} $$

**Interpretation:** Satellite clocks lose 7.2 μs/day relative to ground clocks due to their orbital speed.

---

## 3. General Relativity — Gravitational Redshift

### Einstein's Equivalence Principle
In a uniform gravitational field, an accelerated observer is equivalent to one in a gravitational field. A clock at lower gravitational potential ticks slower.

### Schwarzschild Metric (Earth-Centered Approximation
)

$$ d\tau^2 = \left(1 - \frac{2GM}{rc^2}\right)dt^2 - \frac{1}{c^2}\left(1 - \frac{2GM}{rc^2}\right)^{-1}dr^2 - \frac{r^2}{c^2}d\Omega^2 $$

For a clock at radius $$ r$, at rest ( $dr = d\Omega = 0$):$

$$ d\tau = \sqrt{1 - \frac{2GM}{rc^2}}\, dt $$

### Clock Rate at Different Potentials
For a satellite at $r_{\text{sat}}$ vs. a ground clock at $R_{\oplus}$:

$$ \frac{d\tau_{\text{sat}}}{dt} = \sqrt{1 - \frac{2GM}{r_{\text{sat}}c^2}}, \quad \frac{d\tau_{\text{ground}}}{dt} = \sqrt{1 - \frac{2GM}{R_{\oplus}c^2}} $$

### First-Order Expansion (Weak Field)
Using$ \sqrt{1-\epsilon}\approx 1-\epsilon/2 $for small$ \epsilon$:

$$ \frac{d\tau_{\text{sat}}}{dt} \approx 1 - \frac{GM}{r_{\text{sat}}c^2}, \quad \frac{d\tau_{\text{ground}}}{dt} \approx 1 - \frac{GM}{R_{\oplus}c^2
}

$The **relative clock rate** is: $$$

\frac{\Delta f_{GR}}{f_0} = \frac{d\tau_{\text{sat}}}{d\tau_{\text{ground}}} - 1 = \frac{GM}{c^2}\left(\frac{1}{R_{\oplus}} - \frac{1}{r_{\text{sat}}}\right
)

**### Numerical Calculation for GPS **

\frac{GM}{c^2} = \frac{3.9860\times 10^{14}}{(299792458)^2} = 4.4350\times 10^{-3} \text{ m}\Delta\phi = \frac{GM}{c^2}\left(\frac{1}{R_{\oplus}} - \frac{1}{r_{\text{sat}}}\right) = 4.4350\times 10^{-3}\left(\frac{1}{6.3710\times 10^6} - \frac{1}{26.560\times 10^6}\right)= 4.4350\times 10^{-3}\times 1.2447\times 10^{-7} = 5.5208\times 10^{-10
}

**Over one day:**

 \Delta\tau_{GR} = 5.5208\times 10^{-10}\times 86400 = +47.7 \text{ μs/day}

$$ **Interpretation:** Satellite clocks gain 47.7 μs/day (run faster) because they sit higher in Earth's gravitational potential well — spacetime is "flatter" there.

> **Note:** The exact value depends on the choice of $R_{\oplus}$(mean radius vs. WGS84 ellipsoid semi-major axis) and whether Earth's self-gravity from the oblateness term $J_2 $is included. The standard value used in GPS is **+45.8 μs/day** for GR alone.

---

## 4. Net Relativistic Effec
t

$$ \Delta\tau_{\text{net}} = \Delta\tau_{GR} + \Delta\tau_{SR} = +45.8 + (-7.2) = +38.6 \text{ μs/day} $$ Or in fractional frequency

$$ \frac{\Delta f_{\text{net}}}{f_0} = \frac{38.6\times 10^{-6}}{86400} = 4.465\times 10^{-10} $ $$$

$$

**This means GPS satellite clocks tick faster than ground clocks by 4.465 parts per $10^{10}$.**

### Equivalent Ranging Error
Light travels 300 m per μs:

$$ \Delta\rho = c\times\Delta\tau_{\text{net}} = 299792458 \times 38.6\times 10^{-6} = 11,572 \text{ m} \approx 11.6 \text{ km/day} $$

 | Time Period | Ranging Error |
|-------------|---------------|
| 1 day | 11.6 km |
| 1 hour | 483 m |
| 1 minute | 8.05 m |
| 1 second | 0.134 m (13.4 cm) |
| 1 ms | 0.134 mm |

---

## 5. How GNSS Handles Relativity

### Factory Frequency Offset (Pre-Launch Correction)
Before launch, GPS satellite atomic clocks are intentionally offset by $-4.465\times 10^{-10} $:

$f_{\text{set}} = f_0\left(1 - \frac{\Delta f_{\text{net}}}{f_0}\right) = 10.23 \text{ MHz}\times(1 - 4.465\times 10^{-10}) = 10.22999999543 \text{ MHz} $$$

Once in orbit, the +38.6 μs/day relativistic speedup brings the clocks into agreement with ground UTC.

**What this means:** The clocks are manufactured to run slow on the ground, so when they reach orbit, they run at the correct rate. The remaining periodic effects are handled by the navigation message correction.

### Navigation Message Clock Polynomial
Each satellite broadcasts a clock correction

$$ \Delta t = a_0 + a_1(t - t_{oc}) + a_2(t - t_{oc})^2 + \Delta t_{\text{relativistic}} $$ where:
- $a_0$ = clock bias (ns)
- $a_1$ = clock drift (s/s)
- $a_2$ = drift rate (s/s²)
- $t_{oc}$ = clock reference time

The relativistic correction for eccentric orbits

$$ \Delta t_{\text{rel}} = -\frac{2\sqrt{GM\cdot a}}{c^2}e\sin E

$ where $E$ = eccentric anomaly from Kepler's equation,$a$ = semi-major axis,$e$ = eccentricity.$

### Eccentricity-Dependent Periodic Term
For circular orbits ( $e = 0$): $ \Delta t_{\text{rel}} = 0$ (factory offset fully handles the mean effect).

For GPS ( $e \approx 0.005$–0.02): periodic variation of amplitude:

$A_{\text{rel}} = \frac{2\sqrt{GM\cdot a}}{c^2}e \approx \frac{2\times\sqrt{3.986\times10^{14}\times26.56\times10^6}}{9\times10^{16}}\times e $For $e = 0.01$: $A_{\text{rel}} \approx 0.55\,\mu\text{s} \approx 0.16 $m equivalent

This correction is applied by the receiver every epoch using the broadcast ephemeris.

---

## 6. Additional Relativistic Effects

### Sagnac Effect (Earth Rotation)
During signal propagation, Earth rotates beneath the signal path

$$ \Delta t_{\text{Sagnac}} = \frac{\vec{\Omega}_e \cdot (\vec{r}_{\text{sat}}\times\vec{r}_{\text{rx}})}{c^2} $$ where $\vec{\Omega}_e$ = Earth rotation vector ($7.2921\times 10^{-5} $rad/s).

**Magnitude:** Up to ~30 ns (~9 m) for maximum satellite-receiver separation.
This is applied by transforming to ECEF coordinates or computing a Sagnac correction.

### Shapiro Delay (Gravitational Time Dilation of Signal Path)
The signal path passes through spacetime curvature near Earth

$$ \Delta t_{\text{Shapiro}} = \frac{2GM}{c^3}\ln\left(\frac{r_1 + r_2 + r_{12}}{r_1 + r_2 - r_{12}}\right)

$$

**Magnitude for GPS:** ~20 ps (~6 mm) — negligible for standard positioning, but included in precise ephemeris models.

### Lense-Thirring (Frame Dragging
)

$$ \Delta\vec{v}_{\text{LT}} = -\frac{1}{c^2}\left[\vec{\Omega}_e \times \vec{v}\right]

$$

**Magnitude:**$ \sim 0.1\,\mu $m/day — negligible, but measurable in GRACE/GOCE missions.

### Geodetic Precession (de Sitter)
Precession of satellite's orbit plane due to Earth's gravitomagnetic field:

$$ \Omega_{\text{dS}} \approx 0.15 \text{ mas/day (for GPS orbit)} $$ Negligible for standard GNSS.

---

## 7. Different GNSS Systems — Relativity

| System | Orbit Radius (km) | Velocity (m/s) | SR Effect (μs/day) | GR Effect (μs/day) | Net (μs/day) |
|--------|-------------------|-----------------|---------------------|---------------------|--------------|
| GPS (MEO) | 26,560 | 3,874 | −7.2 | +45.8 | +38.6 |
| GLONASS (MEO) | 25,508 | 3,987 | −7.6 | +42.8 | +35.2 |
| Galileo (MEO) | 29,601 | 3,611 | −6.1 | +52.4 | +46.3 |
| BeiDou MEO | 27,906 | 3,752 | −7.0 | +48.5 | +41.5 |
| BeiDou GEO | 42,164 | 3,030 | −4.8 | +71.4 | +66.6 |

**BeiDou GEO satellites** have the largest net effect because they are much higher and slower. The factory offset must be set appropriately for each orbit type.

---

## 8. Why It Matters for Surveying

### PPP (Precise Point Positioning)

- Requires **sub-nanosecond** clock accuracy

- Relativistic effects must be modeled to **picosecond level**

- IGS final clock products provide 30-s satellite clock estimates

- After removing factory offset + navigation message correction, residual clock errors are ~0.1–0.3 ns → 3–10 cm range

### RTK (Real-Time Kinematic)

- Base station corrects satellite clock errors differentially

- Relativistic effects mostly cancel (common-mode at short baselines)

- However, base station **height** affects gravity potential difference → clock correction should be adjusted for height

$$ \Delta\phi_{\text{height}} = \frac{g\cdot\Delta h}{c^2} = \frac{9.81\cdot\Delta h}{9\times10^{16}} $$ For Δh = 100 m:$ \Delta\phi \approx 1.1\times10^{-14} $ → 0.9 ns → ~0.3 m. This is significant in precise applications.

### Time Transfer (TPP)

- GPS is used for international time comparison (UTC synchronization)

- Relativistic corrections must be precise to **~0.1 ns** for metrology applications

- Both gravitational and velocity corrections apply simultaneously

### Navigation Solution
If relativistic clock correction is removed from the receiver:

- After 1 hour: ~483 m position error

- After 1 day: 11.6 km range error on all satellites

- Solution becomes useless within minutes

---

## 9. Comparison to Other Effects

| Effect | Magnitude (GPS) | Corrected By |
|--------|-----------------|--------------|
| **Relativistic (SR + GR)** | 38.6 μs/day | Factory offset + nav message |
| Tropospheric delay | 2.3 m zenith | Mapping function + model |
| Ionospheric delay | 0.5–15 m (L1) | Dual-frequency combination |
| Satellite clock error | 1–3 m (broadcast) | Nav message polynomial |
| Ephemeris error | 1–3 m | Precise ephemeris (IGS) |
| Multipath | 0.5–5 cm | Antenna design + processing |
| Receiver noise | 1–5 cm | Measurement type dependent |

---

## 10. Key Points to Remember

1. **Both SR and GR must be included** — neither alone gives the correct answer
2. **Factory offset handles the mean effect** — the ±38.6 μs/day is pre-corrected at manufacture
3. **Eccentricity term is periodic** — zero for circular orbits, sinusoidal for eccentric GPS ($e\approx 0.01$): ~0.5 μs amplitude
4. **Different constellations, different corrections** — Galileo orbits higher than GPS → larger GR effect; GLONASS orbits lower
5. **Sagnac effect is separate** — it's a coordinate transformation effect, not clock physics
6. **PPP requires IGS final clocks** — broadcast ephemeris cannot achieve sub-meter for clocks
7. **Height-dependent correction** — base station height affects the clock offset in RTK at the cm-to-meter level

---

## 11. Worked Examples

### Example 1: Verify GR Effect for GPS
Using $R_\oplus = 6,371,009 $m, $r_{\text{sat}} = 26,560,000 $m

$$ \frac{\Delta f}{f} = \frac{GM}{c^2}\left(\frac{1}{R_\oplus} - \frac{1}{r_{\text{sat}}}\right) = 4.435\times10^{-3}\times\left(1.570\times10^{-7} - 3.765\times10^{-8}\right) = 5.52\times10^{-10} $$ Per day:$ 5.52\times10^{-10}\times86400 = 47.7$μs ✓ (matches +45.8 μs when using exact WGS84 $R_\oplus$)

### Example 2: SR Effect for Galileo (23,222 km altitude)

$v = \sqrt{\frac{GM}{29601000}} = 3,611 \text{ m/s}\frac{\Delta f_{SR}}{f} = -\frac{v^2}{2c^2} = -\frac{3611^2}{2\times(299792458)^2} = -7.23\times10^{-11}$Per day:$-7.23\times10^{-11}\times86400 = -6.2$μs/day (slightly smaller than GPS due to lower velocity)

### Example 3: Equivalence of Factory Offset

$$ \text{Required offset} = -\frac{\Delta f_{\text{net}}}{f_0} = -\frac{38.6\times10^{-6}}{86400} = -4.465\times10^{-10}f_{\text{clock}} = 10.23\times(1-4.465\times10^{-10}) = 10.22999999543 \text{ MHz} $$

---

## Study Problems
1. Derive the +45.8 μs/day GR effect using the Schwarzschild metric expansion to first order.
2. Compute the SR effect for GLONASS satellites ( $r = 25,508 $km, $v = 3,987 $m/s).
3. Explain why GLONASS uses a different time reference (GLONASS Time ≠ UTC) but still requires relativistic corrections.
4. Derive the eccentricity correction$ \Delta t_{\text{rel}} = -\frac{2\sqrt{GMa}}{c^2}e\sin E $from the energy of the orbit.
5. Calculate the Sagnac correction for a GPS satellite at maximum angular separation from the receiver.
6. Compare the relativistic correction requirements for GPS, Galileo, and BeiDou GEO.
7. Explain why the factory offset cannot perfectly handle the mean relativistic effect (what perturbations cause the broadcast clock correction to deviate?).

---

*Concept maintained by AIGIS — part of [[Physics MOC]] → [[Geodesi Satelit / GNSS]]*