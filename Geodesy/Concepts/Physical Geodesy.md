---
tags: [aigis, concept, geodesy, physical-geodesy, gravity, potential-theory, stokes]
created: 2026-07-27
updated: 2026-07-27
---

# Physical Geodesy — Gravity Field & Potential Theory

## For Geodesy & Earth Sciences

**Core Idea:** Physical geodesy studies Earth's gravity field and uses it to determine the geoid, height systems, and temporal gravity variations. Potential theory — the mathematical framework — describes how gravity varies with position and ties together satellite observations, surface gravity measurements, and the shape of the geoid.

---

## The Gravity Field

### Gravitational vs. Gravity Potential

| Potential | Symbol | Definition | Sources |
|-----------|--------|------------|---------|
| **Gravitational** | $V$ | $V(\mathbf{r}) = G \iiint \frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} dV'$ | All mass (Earth, Moon, Sun) |
| **Centrifugal** | $\Phi$ | $\Phi = \frac{1}{2}\omega^2 d^2$ ($d$= distance from rotation axis) | Earth rotation |
| **Gravity** | $W$ | $W = V + \Phi$ | Combined |
| **Normal gravity** | $U$ | Gravity of a reference ellipsoid | Reference Earth Model |
| **Disturbing** | $T$ | $T = W - U$ | Anomalous masses |

### Spherical Harmonic Expansion of the Gravitational Potentia
l

$$V(r,\theta,\lambda) = \frac{GM}{r}\sum_{n=0}^{\infty}\sum_{m=0}^{n} \left(\frac{a}{r}\right)^n \left[\bar{C}_{nm}\cos m\lambda + \bar{S}_{nm}\sin m\lambda\right] \bar{P}_{nm}(\cos\theta)$$

| Term | Meaning | Value for Earth |
|------|---------|-----------------|
| $\bar{C}_{00} $ | Mass term | 1.0 (normalized) |
| $\bar{C}_{10},\bar{S}_{10} $ | Geocenter | ~0 (with origin at CM) |
| $\bar{C}_{20} $ | Oblateness | $-4.841 \times 10^{-4} $ |
| $\bar{C}_{21},\bar{S}_{21} $ | Pole position | Varies (polar motion) |
| $\bar{C}_{22},\bar{S}_{22} $ | Equatorial ellipticity | $2.43 \times 10^{-6} $ |

### Normal Gravity Formulas

**International Gravity Formula 1980** (GRS80)
:

$$g_{rs}(\phi) = 9.780327 \left[ 1 + 0.0053024 \sin^2\phi - 0.0000058 \sin^2 2\phi \right] \quad \text{m/s}^2$$

**WGS84 (EGM96):*
*

$$g_{wgs}(\phi) = 9.7803253359 \cdot \frac{1 + 0.00193185265241\sin^2\phi}{\sqrt{1 - 0.00669437999014\sin^2\phi}} \quad \text{m/s}^2$$

---

## Key Physical Geodesy Quantities

| Quantity | Symbol | Formula | Meaning |
|----------|--------|---------|---------|
| Geoid undulation | $N$ | $N = \frac{T}{\gamma} $(Bruns formula) | Ellipsoid–geoid distance |
| Gravity anomaly | $\Delta g$ | $\Delta g = g_P - \gamma_Q$ | Observed minus normal |
| Gravity disturbance | $\delta g$ | $\delta g = g_P - \gamma_P$ | At same point |
| Vertical deflection | $\xi,\eta$ | $\xi = -\frac{1}{\gamma R}\frac{\partial T}{\partial \phi} $, $\eta = -\frac{1}{\gamma R\cos\phi}\frac{\partial T}{\partial \lambda} $ | Plumb line gradient |
| Potential difference | $\Delta W$ | $\Delta W = W_A - W_B$ | Between two points |

### Bruns' Formul
a

$$N = \frac{W(P) - U(Q_0)}{\gamma(Q_0)} = \frac{T(P)}{\gamma(Q_0)} $$This elegantly links the geoid undulation $N$to the disturbing potential $T$.

### Stokes' Integral (Gravimetric Geoid)

$$N = \frac{R}{4\pi\gamma_0} \iint_\sigma \Delta g \, S(\psi)\, d\sigma$$where $S(\psi)$ is Stokes' function. **Prerequisite:** No masses above the geoid, global gravity anomaly data.

### Molodensky's Theory

For areas with topography, we cannot use Stokes directly. Molodensky uses gravity disturbances at the Earth's surface (not geoid) and solves for the quasi-geoid.

---

## In Geodesy Context

### Contributions to the Gravity Field

| Source | Magnitude (mGal) | Wavelength |
|--------|------------------|------------|
| Mean Earth (ellipsoid) | 978,000 | ∞ |
| Oblateness ($J_2$) | ~10,000 | Continental |
| Crustal structure | ±200 | 100–1000 km |
| Mountains | ±100 | 10–100 km |
| Sedimentary basins | ±50 | 50–500 km |
| Isostasy | ±30 | 50–200 km |
| Ocean tides | ±0.3 | 12–24 h (periodic) |

### GOCE & GRACE Missions

| Mission | Year | Measurement | Resolution | Use |
|---------|------|-------------|------------|-----|
| **GRACE** | 2002-2017 | Inter-satellite ranging | ~300 km | Time-variable gravity |
| **GOCE** | 2009-2013 | Gravity gradiometry | ~80 km | High-resolution static field |

**GRACE application:** Monitors groundwater depletion, ice sheet mass loss, sea level rise from steric effects.

### Gravity Reduction Methods

| Method | Correction Applied | Purpose |
|--------|-------------------|---------|
| **Free-air** | $\delta g_{FA} = -0.3086 h$ | Height correction only |
| **Bouguer** | $\delta g_B = -2\pi G\rho h$ | Remove mass above geoid |
| **Terrain** | Variable | Remove/downward-continue topography |
| **Isostatic** | Airy/Pratt compensation | Remove isostatic effects |

**Free-air correction:**$\delta g_{FA} = -\frac{\partial \gamma}{\partial h} h \approx -0.3086h $mGal/m

**Simple Bouguer correction:**$\delta g_B = +0.1119 \, \rho \, h$ mGal ($\rho $in g/cm³)

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $W = V + \Phi$ | Gravity potential | Definition |
| $N = T/\gamma$ | Bruns' formula | Geoid from potential |
| $N = \frac{R}{4\pi\gamma} \iint \Delta g\, S(\psi)\, d\sigma$ | Stokes' integral | Gravimetric geoid |
| $g(\phi) = 9.780327(1 + 0.0053024\sin^2\phi - 0.0000058\sin^22\phi)$ | Normal gravity | GRS80 formula |
| $\Delta g_{FA} = g + 0.3086h - \gamma$ | Free-air anomaly | Corrected anomaly |

---

## Related Concepts

- [[Geoid]] — The equipotential surface

- [[Gravity Field]] — Earth's gravity in detail

- [[Least Squares Adjustment]] — Spherical harmonic coefficient estimation

- [[Reference Ellipsoid]] — Normal gravity reference

- [[GNSS]] — Gravity field for orbit determination

- [[IERS]] — Gravity standards

---

## Study Problems

1. **Recall:** Compute normal gravity at the equator, 45° latitude, and pole using the GRS80 formula. (Answer: ~9.780, ~9.806, ~9.832 m/s² respectively.)
2. **Application:** A gravity measurement at $h = 500 $m gives $g = 9,803,450$μGal. Normal gravity at sea level is 9,803,000 μGal. Compute free-air anomaly. (1 mGal = 1000 μGal.)
3. **Derivation:** Derive the free-air gradient $\partial\gamma/\partial h = -2\gamma/a = -0.3086 $mGal/m.
4. **Real-world:** The Bouguer anomaly over a mountain range is -50 mGal. What does this indicate about isostatic compensation?

---

## Common Mistakes

1. **Confusing gravitational potential $V $with gravity potential $W$:** $W = V + \Phi$ (includes rotation).
2. **Applying Stokes' integral without removing topography:** The integration requires no masses above the geoid.
3. **Using the wrong normal gravity formula:** GRS80 vs WGS84 differ at the μGal level (significant for precise work).
4. **Forgetting to account for time-variable gravity (GRACE):** The static field changes with hydrology, ice, and tectonics.
5. **Mixing mGal (10⁻⁵ m/s²) with μGal (10⁻⁸ m/s²):** 1 μGal ≈ 1 nm/s² — precision of modern gravimeters.

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*