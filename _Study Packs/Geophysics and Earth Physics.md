---
tags: [physics, study-pack, aigis, geophysics, earth-physics, seismology]
aliases: [Geophysics, Earth Physics, Geophysics Study Pack]
created: 2026-07-27
updated: 2026-07-27
---

# 📚 Study Pack — Geophysics and Earth Physics
*The physics beneath our feet — seismic waves, gravity, magnetism, and heat flow.*

---

## 1. Earth's Internal Structure

### Layered Model
| Layer | Depth (km) | State | Density (kg/m³) | Key Property |
|-------|-----------|-------|-----------------|--------------|
| Crust (continental) | 0–40 | Solid | 2,700 | Low density, granitic |
| Crust (oceanic) | 0–10 | Solid | 3,000 | Basaltic |
| Upper Mantle | 40–410 | Solid | 3,400–3,800 | Partial melt zone (asthenosphere) |
| Transition Zone | 410–660 | Solid | 3,800–4,400 | Mineral phase transitions |
| Lower Mantle | 660–2,891 | Solid | 4,400–5,600 | High viscosity |
| Outer Core | 2,891–5,150 | Liquid | 9,900–12,200 | Fe-Ni alloy, convecting |
| Inner Core | 5,150–6,371 | Solid | 12,800–13,100 | Crystalline iron |

### Seismic Discontinuities
- **Mohorovičić (Moho):** Crust–mantle boundary, P-wave velocity jumps from ~6.5 to ~8.1 km/s
- **Gutenberg discontinuity:** Core–mantle boundary, S-wave shadow (liquid outer core)
- **Lehmann discontinuity:** Outer core–inner core boundary

---

## 2. Seismology

### Seismic Wave Theory

**Body Waves:**
$$v_P = \sqrt{\frac{K + \frac{4}{3}\mu}{\rho}}, \quad v_S = \sqrt{\frac{\mu}{\rho}}$$

where $K$ = bulk modulus, $\mu$ = shear modulus, $\rho$ = density.

- **P-waves (compressional):** Longitudinal, fastest, travel through all media
- **S-waves (shear):** Transverse, slower, **cannot** travel through liquids ($\mu = 0$ for fluids)

**Velocity Ratio:**
$$\frac{v_P}{v_S} = \sqrt{\frac{2(1-\nu)}{1-2\nu}}$$

where $\nu$ = Poisson's ratio (typically 0.25 → $v_P/v_S = \sqrt{3}$).

### Surface Waves
| Wave Type | Motion | Velocity | Decay |
|-----------|--------|----------|-------|
| Rayleigh | Retrograde elliptical (vertical plane) | $v_R \approx 0.92 \, v_S$ | $\propto e^{-kz}$ (exponential with depth) |
| Love | Horizontal shear (transverse) | $v_L \approx v_S \cdot t_s/(t_s+t_l)$ | $\propto e^{-kz}$ |

### Seismic Ray Theory (Snell's Law)
$$\frac{\sin\theta_i}{v_i} = \frac{\sin\theta_j}{v_j} = p = \text{ray parameter (constant)}$$

**Critical angle:** $\sin\theta_c = v_1/v_2$ (total internal reflection).

### Travel Time Curves
- **Direct wave:** Linear $t = x/v$
- **Refracted wave:** Head wave along discontinuity
- **Reflected wave:** Hyperbolic moveout $t = \sqrt{t_0^2 + x^2/v^2}$

### Earthquake Magnitude Scales
| Scale | Measure | Formula |
|-------|---------|---------|
| Local ($M_L$) | Maximum amplitude | $M_L = \log_{10} A - \log_{10} A_0$ |
| Body wave ($m_b$) | P-wave amplitude | $m_b = \log_{10}(A/T) + Q(\Delta, h)$ |
| Surface wave ($M_s$) | Surface wave amplitude | $M_s = \log_{10}(A/T) + 1.66\log_{10}\Delta + 3.3$ |
| Moment ($M_w$) | Seismic moment | $M_w = \frac{2}{3}\log_{10}M_0 - 10.7$ |

**Seismic moment:** $M_0 = \mu A d$ (shear modulus × fault area × slip)

---

## 3. Gravity and Gravity Anomalies

### Bouguer Gravity Anomaly
$$\Delta g_B = g_{\text{obs}} - \gamma_0 + \delta g_B + \delta g_T + \delta g_F$$

where:
- $\gamma_0$ = normal gravity (reference ellipsoid)
- $\delta g_B = 2\pi G\rho h$ = Bouguer slab correction (terrain below station)
- $\delta g_T$ = topographic correction (terrain above and around station)
- $\delta g_F$ = free-air correction $= 0.3086 \cdot h$ (mGal/m)

### Free-Air Anomaly
$$\Delta g_{FA} = g_{\text{obs}} - \gamma_0 + 0.3086h$$
Used in geoid determination (Bruns' formula $N = \Delta g_{FA}/\gamma$).

### Isostasy
The principle that topographic loads are compensated by density variations at depth.

**Airy Model:**
$$h\rho_c = H(\rho_m - \rho_c)$$
- Continental crust ($\rho_c \approx 2,700$ kg/m³) has **root** $H = h\rho_c/(\rho_m - \rho_c) \approx 5h$ (root is ~5× topographic height)
- Oceanic crust ($\rho_c \approx 3,000$ kg/m³) has **root** $H \approx 3.5h$

**Pratt Model:** Lateral density variations at fixed depth $D$:
$$(\rho_0 - \rho_c)D = \rho_c h$$

### Moho Depth from Gravity
$$h_{Moho} \approx \frac{\Delta g_B}{2\pi G \Delta\rho}$$
Typical: 30–40 km (continental), 5–10 km (oceanic).

---

## 4. Geomagnetism

### Earth's Magnetic Field
$$\vec{B}(\vec{r}) = -\nabla V(\vec{r})$$

**Magnetic scalar potential (external):**
$$V = a\sum_{n=1}^{\infty}\sum_{m=0}^{n}\left(\frac{a}{r}\right)^{n+1}P_n^m(\cos\theta)[g_n^m\cos m\phi + h_n^m\sin m\phi]$$

### Main Field Parameters (2025)
| Parameter | Value |
|-----------|-------|
| $B$ at equator | ~30 μT |
| $B$ at poles | ~60 μT |
| Dipole moment | $8.0 \times 10^{22}$ A·m² |
| Declination (varies) | 0°–30° depending on location |
| Inclination (dip) | 0° (equator) to 90° (poles) |

### Secular Variation
- Field changes over years–decades
- Drift rate: ~0.1°/year (westward)
- Measured by repeat ground surveys and satellite missions (Swarm)

### Geomagnetic Polarity Reversals
- Timescale: $10^4$–$10^6$ years
- Current field may be weakening (~10% over 200 years)
- Recorded in paleomagnetic data (striped seafloor pattern)

### External Field Sources
- **Ring current:** Partially shields Earth from solar wind ($K_p$ index)
- **Magnetospheric storms:** Can induce GICs (ground-induced currents) in power grids

---

## 5. Heat Flow and Thermal Structure

### Surface Heat Flow
$$q = -k\frac{dT}{dz}$$

where $k$ = thermal conductivity, $dT/dz$ = temperature gradient.

**Measured values:**
| Region | Heat Flow (mW/m²) |
|--------|-------------------|
| Continents (average) | 65 |
| Oceans (average) | 101 |
| Mid-ocean ridges | 200–500 |
| Continental shields | 40–50 |
| Active volcanic areas | >150 |

### Geothermal Gradient
$$\frac{dT}{dz} = \frac{q}{k}$$
- Continental crust: ~25 K/km (typical)
- Oceanic crust: ~10–15 K/km (higher $k$, lower $q$)

### Heat Sources
$$q_{\text{total}} = q_{\text{radiogenic}} + q_{\text{primordial}}$$

**Radiogenic heat production:**
$$A = A_0 \exp(-z/h_s)$$
where $h_s$ = scale height (~10 km for crustal rocks).

| Isotope | Half-life (Ga) | Contribution |
|---------|----------------|-------------|
| $^{238}$U | 4.47 | ~40% |
| $^{235}$U | 0.70 | ~4% |
| $^{232}$Th | 14.05 | ~40% |
| $^{40}$K | 1.25 | ~16% |

### Lithospheric Thermal Thickness
$$T(z) = T_s + \frac{q}{k}z$$
Geotherm crosses solidus → defines thermal lithosphere thickness (~100–250 km).

---

## 6. Plate Tectonics Physics

### Plate Driving Forces
- **Mantle convection:** Thermal buoyancy drives large-scale circulation
- **Slab pull:** Dense subducting plate pulls rest (dominant force, ~$10^{13}$ N/m)
- **Ridge push:** Gravitational sliding from elevated ridge ($\sim 3 \times 10^{12}$ N/m)
- **Basal drag:** Coupling to mantle flow (can drive or resist)

### Rheology of the Lithosphere

**Ductile (creep) flow — power-law:**
$$\dot{\epsilon} = A\sigma^n \exp\left(-\frac{Q}{RT}\right)$$

where $\dot{\epsilon}$ = strain rate, $\sigma$ = stress, $n$ ≈ 3–4, $Q$ = activation energy.

**Brittle failure — Byerlee's Law:**
$$\tau \approx 0.85\sigma_n \quad (\text{for } \sigma_n < 200 \text{ MPa})$$
$$\tau \approx 50 + 0.6\sigma_n \quad (\text{for } \sigma_n > 200 \text{ MPa})$$

### Plate Velocity and Heat Transport
- Plate velocity ~1–10 cm/yr
- **Péclet number:** $\text{Pe} = vL/\kappa$
  - $\text{Pe} \gg 1$: advection dominates (plate tectonics)
  - $\text{Pe} \ll 1$: conduction dominates (shields)

---

## 7. Geodesy–Geophysics Connection

### Relationship Between Gravity and Topography
$$\Delta g_{FA} = 2\pi G \rho_{crust} h \cdot f(\text{isostasy})$$
- Complete isostatic compensation: $\Delta g_B \approx 0$ over long wavelengths
- Incomplete compensation: positive Bouguer anomalies

### Post-Glacial Rebound (GIA)
- Viscoelastic response of mantle to ice sheet removal
- Measured by GPS: uplift rates up to 1 cm/yr (Scandinavia, Canada)
- Reveals mantle viscosity: $\eta \approx 10^{21}$ Pa·s (upper mantle)

### Earth Tides
- Solid Earth deformation due to Moon and Sun
- Tidal gravity signal: ~100 μGal (0.1 mGal)
- Measured by superconducting gravimeters

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $v_P = \sqrt{(K + 4\mu/3)/\rho}$ | P-wave velocity | Seismology |
| $\Delta g_B = g_{obs} - \gamma + 2\pi G\rho h$ | Bouguer anomaly | Gravity interpretation |
| $q = -k(dT/dz)$ | Heat flow | Thermal structure |
| $\dot{\epsilon} = A\sigma^n e^{-Q/RT}$ | Power-law creep | Lithosphere rheology |
| $M_w = \frac{2}{3}\log_{10}M_0 - 10.7$ | Moment magnitude | Earthquake size |

---

## Problems
1. Calculate P- and S-wave velocities for $\rho = 3,300$ kg/m³, $K = 130$ GPa, $\mu = 75$ GPa.
2. Determine the Bouguer slab correction for a station at 1,000 m elevation on granite ($\rho = 2,670$ kg/m³).
3. Estimate the depth of the Moho beneath an ocean using a Bouguer anomaly of $-30$ mGal.
4. Calculate the heat flow through the continental crust if $k = 2.5$ W/(m·K) and $dT/dz = 25$ K/km.
5. Compare slab pull and ridge push forces for a subducting plate with density contrast 50 kg/m³.
6. Explain why S-waves cannot cross the outer core and how this proves its liquid state.
7. Estimate the age of oceanic lithosphere at 1,000 km from a mid-ocean ridge (half-space cooling model).

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
