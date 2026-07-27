---
tags: [physics, study-pack, aigis, satellite-physics, orbital-mechanics, gnss]
aliases: [Satellite Physics, Orbital Mechanics, Satellite Dynamics]
created: 2026-07-27
updated: 2026-07-27
---

# 📚 Study Pack — Satellite Physics
*Orbital mechanics, perturbations, GPS satellite motion, and relativistic effects.*

---

## 1. Two-Body Problem (Keplerian Motion)

### Newton's Law of Gravitation

$$ \vec{F} = -\frac{GMm}{r^2}\hat{r
}

**### Energy and Angular Momentum (Conserved) **

E = \frac{1}{2}mv^2 - \frac{GMm}{r} = \text{constant}\vec{h} = \vec{r} \times \vec{v} = \text{constant} $$

### Orbital Elements (Classical Keplerian)
| Element | Symbol | Description |
|---------|--------|-------------|
| Semi-major axis | $a$ | Orbit size |
| Eccentricity | $e$ | Orbit shape ($0 \le e < 1$) |
| Inclination | $i$ | Tilt relative to equator |
| Right ascension of ascending node | $ \Omega$ | Longitude of ascending node |
| Argument of perigee | $ \omega$ | Orientation of ellipse in plane |
| True anomaly | $f$ | Position in orbit (angle from perigee) |
| Mean anomaly | $M$ | Mean angular position (linear with time) |

### Kepler's Laws
1. **Elliptical orbits:** $r = \frac{a(1-e^2)}{1 + e\cos f}$2. **Equal areas in equal times:**$ \frac{dA}{dt} = \frac{h}{2} = \text{constant} $ 3. **Period relation:** $T = 2\pi\sqrt{\frac{a^3}{GM}}$### Vis-viva Equatio
n

$$ v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right) $$

### Orbit Types
| Type | Eccentricity | Semi-major axis | Period |
|------|--------------|-----------------|--------|
| LEO (Low Earth Orbit) | ~0 | 6,378–8,000 km | ~90 min |
| MEO (Medium Earth Orbit) | ~0 | 8,000–35,000 km | 2–24 h |
| GPS/GLONASS/Galileo | ~0.01 | ~26,560 km | 12 h sidereal |
| GEO (Geostationary) | 0 | 42,164 km | 24 h sidereal |
| HEO (Highly Elliptical) | >0.5 | varies | varies |

---

## 2. Coordinate Systems

### ECI (Earth-Centered Inertial)

- Origin: Earth's center of mass

- X-axis: Vernal equinox direction

- Z-axis: Earth's rotation axis (North)

- Non-rotating with Earth

### ECEF (Earth-Centered Earth-Fixed)

- Rotates with Earth

- X-axis: Prime meridian (Greenwich)

- Z-axis: Earth's rotation axis

- **WGS84 / ITRF** reference frames

### Transformatio
n

$$ \vec{r}_{ECEF} = R_z(\theta_G)\vec{r}_{ECI} $$ where $\theta_G$ = Greenwich sidereal time (GST).

### Topocentric (Local) Coordinates

- Origin: Observer on Earth's surface

- East-North-Up (ENU) or Azimuth-Elevation-Range (AER)

---

## 3. Perturbation Theory

### Osculating Elements
At any instant, the satellite follows a Keplerian ellipse whose elements slowly change due to perturbations.

### Gaussian Variational Equations (Lagrange Planetary Equations)

$$ \frac{da}{dt} = \frac{2}{n\sqrt{1-e^2}}\left[ e\sin f \cdot S + \frac{p}{r} \cdot T \right]\frac{de}{dt} = \frac{\sqrt{1-e^2}}{na}\left[ \sin f \cdot S + \left( \cos f + \frac{e + \cos f}{1 + e\cos f} \right) \cdot T \right]\frac{di}{dt} = \frac{r\cos(\omega+f)}{na\sqrt{1-e^2}} \cdot W

$where $S$,$T$,$W$ are perturbing accelerations in **radial**, **transverse** (along-track), **normal** directions.

### Principal Perturbations (Order of Magnitude)

| Perturbation | GPS (20,200 km) | LEO (500 km) | GEO (35,786 km) |
|--------------|-----------------|--------------|-----------------|
| $J_2$(oblateness) | ~10⁻⁴ m/s² | ~10⁻³ m/s² | ~10⁻⁵ m/s² |
| Atmospheric drag | Negligible | **Dominant** | Negligible |
| Solar radiation pressure | ~10⁻⁷ m/s² | ~10⁻⁷ m/s² | **Dominant** |
| Third body (Moon/Sun) | ~10⁻⁶ m/s² | ~10⁻⁶ m/s² | ~10⁻⁶ m/s² |
| Relativistic | ~10⁻¹⁰ m/s² | ~10⁻¹⁰ m/s² | ~10⁻¹⁰ m/s² |

---

## 4. J₂ Perturbation (Earth's Oblateness)

### Earth's Gravity Potentia
l

$U = \frac{GM}{r}\left[1 - J_2\left(\frac{a_e}{r}\right)^2 P_2(\sin\phi) + J_3\left(\frac{a_e}{r}\right)^3 P_3(\sin\phi) + \cdots \right]$where $J_2 \approx 1.08263 \times 10^{-3} $, $a_e = 6,378,137 $m.

### Secular Rates (Long-term, averaged over orbit)

**Right ascension of ascending node:*
*

$$ \dot{\Omega} = -\frac{3}{2} n J_2 \left(\frac{a_e}{a}\right)^2 \frac{\cos i}{(1-e^2)^2} $$

**Argument of perigee:*
*

$$ \dot{\omega} = \frac{3}{4} n J_2 \left(\frac{a_e}{a}\right)^2 \frac{5\cos^2 i - 1}{(1-e^2)^2} $$

**Mean anomaly:*
*

$$ \dot{M} = n + \frac{3}{4} n J_2 \left(\frac{a_e}{a}\right)^2 \frac{3\cos^2 i - 1}{(1-e^2)^{3/2}} $$

**Critical inclination:**$ \dot{\omega} = 0 $at$ i = 63.4^\circ $or $116.6^\circ$ (Molniya orbits).

### GPS Relevance

- For GPS ( $a \approx 26,560 $km, $i = 55^\circ$, $e \approx 0.01$):
 - $ \dot{\Omega} \approx -0.044^\circ$/day (westward precession)
 - $ \dot{\omega} \approx +0.069^\circ$/day

- Precession period of orbital plane: ~8.3 years

---

## 5. Atmospheric Drag

### Drag Acceleration

$$ \vec{a}_D = -\frac{1}{2} \frac{C_D A}{m} \rho v^2 \hat{v} $$ where $C_D \approx 2.2$ (drag coefficient),$A/m$= area-to-mass ratio,$ \rho$= atmospheric density.

### Density Models

- **Exponential model:**$ \rho = \rho_0 \exp(-(h-h_0)/H) $- **Scale height $H$:** ~50–100 km (varies with solar activity)

- **Models:** NRLMSISE-00, JB2008, DTM2020

### Orbital Decay

- Period change: $ \frac{dT}{dt} \propto -\rho a^{1/2} $- Lifetime at 400 km: ~months–years

- Lifetime at 800 km: ~decades

- **Solar cycle:** Density at 400 km varies ×10–100 between solar min/max

---

## 6. Solar Radiation Pressure (SRP)

### Acceleratio
n

$$ \vec{a}_{SRP} = -\frac{C_R A}{m} \frac{P_{solar}}{c} \left(\frac{1 \text{ AU}}{r}\right)^2 \hat{r}_{sun} $$ where $C_R \approx 1.2$–$1.8$(reflectivity coefficient), $P_{solar} = 4.56 \times 10^{-6}$N/m² at 1 AU.

### Yarkovsky Effect (for small bodies)
Thermal emission creates non-gravitational force — relevant for asteroids, not GNSS satellites.

---

## 7. Third-Body Perturbations (Sun, Moon)

### Tidal Potentia
l

$$ \Delta U = \frac{GM_3}{r_3^3} r^2 P_2(\cos\psi)

$where $\psi$ = angle between satellite and third-body vectors.

### Secular Effects on Eccentricity Vecto
r

$$ \frac{d\vec{e}}{dt} \propto \frac{GM_3}{a_3^3} \frac{a^4}{GM} \left[ \text{periodic terms} \right]

$$ For GPS:

- **Moon:** Causes ~0.2°/yr variation in $e$ and $ \omega$- **Sun:** Similar magnitude

- **Resonance effects:** Near 2:1 resonance (e.g., Galileo orbits)

---

## 8. GPS Satellite Motion Specifics

### Constellation Design
| Parameter | GPS | GLONASS | Galileo | BeiDou |
|-----------|-----|---------|---------|--------|
| Semi-major axis | 26,560 km | 25,508 km | 29,601 km | MEO: 27,906 km |
| Inclination | 55° | 64.8° | 56° | 55° (MEO) |
| Period (sidereal) | 11 h 58 m | 11 h 15 m | 14 h 4 m | ~12.6 h |
| Repeat cycle | ~1 sidereal day | ~8 sidereal days | 10 sidereal days | varies |
| Orbit planes | 6 | 3 | 3 | 3 (MEO) |
| Satellites/plane | 4 (nominal) | 8 | 10 | 7–8 |

### Ground Track Repeat
GPS: $T_{sidereal} \approx 23h 56m 4s$; GPS period = 11h 58m 2s (half sidereal day).
Ground track repeats every **sidereal day** (16 orbits = 1 day).

### Broadcast Ephemeris (Keplerian + Corrections)
Keplerian elements at reference epoch $t_{oe}$:

- $M_0, \Delta n, e, \sqrt{a}, \Omega_0, i_0, \omega, \Omega_{dot}, i_{dot} $Corrections (harmonic):
- $C_{uc}, C_{us}$(amplitude of cosine/sine corrections to argument of latitude)
- $C_{rc}, C_{rs}$(corrections to radius)
- $C_{ic}, C_{is}$(corrections to inclination)

### Precise Orbits (IGS)

- **Final (IGS final):** 2 cm accuracy, ~2 weeks latency

- **Rapid:** 3–5 cm, ~1 day

- **Ultra-rapid:** ~10 cm, real-time / few hours

- Format: SP3 (standard product 3)

---

## 9. Relativistic Effects on Satellite Clocks

### General Relativity (Gravitational Redshift
)

$$ \frac{\Delta f_{GR}}{f_0} = \frac{\Delta U}{c^2} = \frac{GM}{c^2}\left(\frac{1}{R_{\oplus}} - \frac{1}{r_{sat}}\right)

$$ GPS: **+45.8 μs/day** (clocks run faster at altitude)

### Special Relativity (Time Dilation
)

$$ \frac{\Delta f_{SR}}{f_0} = -\frac{v^2}{2c^2} $$ GPS: **-7.2 μs/day** (clocks run slower due to orbital velocity)

### Net Effec
t

$$ \frac{\Delta f_{net}}{f_0} = \frac{+45.8 - 7.2}{\text{day}} = +38.6 \mu\text{s/day} $$

### Factory Frequency Offset
GPS clocks set to: $f = 10.23 \text{ MHz} \times (1 - 4.465 \times 10^{-10}) = 10.22999999543 \text{ MHz} $Once in orbit, relativistic speedup brings them into sync with ground UTC.

### Periodic Relativistic Effect (Eccentricity)
For $e \neq 0$:

$$ \Delta t_{ecc} = -\frac{2\sqrt{GM a}}{c^2} e \sin E

$where $E$ = eccentric anomaly. Amplitude: ~0.5 μs for GPS ( $e \approx 0.01$).

### Receiver Application
The receiver applies the broadcast clock correction polynomial:

$$ \Delta t = a_0 + a_1(t-t_{oc}) + a_2(t-t_{oc})^2 + \Delta t_{relativistic} $$

---

## 10. Relativistic Effects on Signal Propagation

### Shapiro Delay (Gravitational Time Delay
)

$$ \Delta t_{Shapiro} = \frac{2GM}{c^3}\ln\left(\frac{r_1 + r_2 + r_{12}}{r_1 + r_2 - r_{12}}\right)

$$ For GPS: ~20 ps (negligible for standard positioning, relevant for PPP-AR)

### Sagnac Effect
Earth rotation during signal propagation

$$ \Delta t_{Sagnac} = \frac{2\vec{\Omega}_e \cdot (\vec{r}_1 \times \vec{r}_2)}{c^2} $$ where $\vec{\Omega}_e$ = Earth rotation vector.

Typical: up to **30 ns** (~9 m) for LEO-to-ground links; smaller for MEO-to-ground.

---

## 11. Orbit Determination Methods

### Batch Least Squares
Minimize sum of squared residuals

$$ \min \sum_i \left( \frac{O_i - C_i(\vec{x})}{\sigma_i} \right)^2

$where $O_i$ = observations (range, range-rate, angles), $C_i$ = computed values from estimated state$ \vec{x}$.

### Kalman Filter (Sequential Estimation)

- **Predict:** $ \hat{\vec{x}}_{k|k-1} = \Phi \hat{\vec{x}}_{k-1|k-1} $, $P_{k|k-1} = \Phi P_{k-1|k-1} \Phi^T + Q$- **Update:** $K_k = P_{k|k-1}H^T(HP_{k|k-1}H^T + R)^{-1}$, $ \hat{\vec{x}}_{k|k} = \hat{\vec{x}}_{k|k-1} + K_k(\vec{z}_k - H\hat{\vec{x}}_{k|k-1}) $Used in real-time orbit determination (e.g., GPS navigation solution, PPP).

### Dynamic vs. Kinematic

- **Dynamic:** Uses force model (gravity, drag, SRP, etc.) — smoother, model-dependent

- **Kinematic:** Pure geometry (phase + code) — no force model, noisier, but no model errors

- **Reduced-dynamic:** Hybrid — dynamic with empirical accelerations to absorb model errors

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $T = 2\pi\sqrt{a^3/GM}$ | Kepler's 3rd law | Orbital period |
| $v^2 = GM(2/r - 1/a)$ | Vis-viva | Satellite velocity |
| $ \dot{\Omega} = -\frac{3}{2}nJ_2(a_e/a)^2\cos i/(1-e^2)^2$ | J₂ node precession | Long-term orbit evolution |
| $ \Delta f_{net}/f_0 = +38.6 \mu\text{s/day} $ | GPS relativistic clock | Clock synchronization |
| $ \Delta t_{ecc} = -\frac{2\sqrt{GMa}}{c^2}e\sin E$ | Eccentricity correction | Relativistic periodic term |
| $ \vec{a}_D = -\frac{1}{2}\frac{C_D A}{m}\rho v^2\hat{v} $ | Drag acceleration | LEO orbit decay |

---

## Problems
1. Calculate the semi-major axis of a GPS satellite given its 12-hour sidereal period.
2. Compute the J₂-induced nodal precession rate for GPS ($a=26,560 $km,$i=55^\circ$, $e=0.01$).
3. Estimate the atmospheric drag force on a 1,000 kg satellite at 400 km altitude ( $C_D=2.2$, $A=5 $m²,$ \rho=2\times10^{-12} $ kg/m³).
4. Verify the +38.6 μs/day net relativistic clock offset for GPS using $v=3,874 $m/s and $r=26,560 $km.
5. Derive the Sagnac correction for a GPS receiver at 45°N latitude receiving from a satellite at zenith.
6. Explain why Molniya orbits use $i=63.4^\circ $and what$ \dot{\omega}=0 $achieves.
7. Compare the dominant perturbations for GPS, LEO, and GEO satellites.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*