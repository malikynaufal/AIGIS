---
tags: [geodesy, study-pack, gravity, instrumentation, aigis]
aliases: [Gravity Measurement, Pengukuran Gravitas]
created: 2026-07-27
---

# 📚 Study Pack — Gravity Measurement

_Covering absolute and relative gravimeters, gravity networks, and the role of gravity in geodesy. Target length: ~4,500 words._

> **Prerequisites:** [[Gravity Field]], [[Geoid]], [[Physical Geodesy]]

---

## 1. Introduction

Gravity measurements quantify the Earth's gravitational field strength at a point. The **gravity vector** $\mathbf{g} $ combines gravitational attraction and centrifugal acceleration $ $\mathbf{g} = \nabla W

$$

At the Earth's surface, the **normal gravity** on the [[Reference Ellipsoid]] (Somigliana formula)$ $\gamma_0 = \frac{a\,g_p\sin^2\varphi + b\,g_e\cos^2\varphi}{\sqrt{a^2\cos^2\varphi + b^2\sin^2\varphi}} $$

where $ g_e = 9.780326\,7715\;\text{m/s}^2 $ (equatorial) and $ g_p = 9.832186\,3685\;\text{m/s}^2 $ (polar).

Free‑air correction

$ $\delta g_{FA} = 2\gamma\frac{h}{R} \approx 0.3086\;h \;\text{mGal/m} $$

Bouguer correction $ $\delta g_B = 2\pi G\rho h \approx 0.04193\;h \;\text{mGal/m} $$

> **Indonesian term:** *Pengukuran Gravitasi*

---

## 2. Units

| Unit | Symbol | Definition | Typical value |
|------|--------|------------|---------------|
| Gal | Gal | $ 1\;\text{cm/s}^2 = 0.01\;\text{m/s}^2 $ | ~980 Gal at equator |
| Milligal | mGal | $ 10^{-3} $ Gal | 1 mGal ≈ 1 ppm of $ g $ |
| Microgal | $\mu $ Gal |$ 10^{-6} $ Gal | High‑precision (1 nm/s²) |
| SI | $\text{m/s}^2 $ | Base SI unit | ~9.78–9.83 m/s² |
| Eötvös (E) | E | $ 10^{-9}\;\text{s}^{-2} $ | Gravity gradient |

---

## 3. Absolute Gravimeters

### 3.1. Free‑Fall Absolute Gravimeter

**Principle:** Drop a mass in vacuum; measure its acceleration directly from $ g = d^2z/dt^2 $.

| Instrument | Manufacturer | Principle | Accuracy |
|------------|--------------|-----------|----------|
| **FG5** | Micro‑g LaCoste | Free‑fall (corner‑cube reflector in vacuum tube) | 1 $\mu $ Gal |
| **A10** | Micro‑g LaCoste | Transportable free‑fall | 10 $\mu $ Gal |
| **iGrav** | Micro‑g LaCoste | Superconducting, continuous | 1 $\mu $ Gal (long‑term) |
| **T‑014** | METTLER TOLEDO | Ball‑bearing free‑fall | 10 $\mu $ Gal |
| **Absolute gravimeters (quantum)** | NIST (prototype) | Atom interferometry | 0.1 $\mu $ Gal |

**FG5 operating principle:**

1. A corner‑cube reflector is dropped from rest in a vacuum chamber.
2. A laser interferometer records the position at regular time intervals.
3. The acceleration $ g $ is derived from the second difference of positions.
4. The result is corrected for: local terrain, tidal effects, ocean loading, polar motion, atmospheric pressure
.

$ $ g_{\text{corrected}} = g_{\text{observed}} - \delta g_{\text{tide}} - \delta g_{\text{atm}} - \delta g_{\text{polar}} - \delta g_{\text{load}}$$

### 3.2. Typical Correction Magnitudes

| Correction | Order of magnitude | Formula / Source |
|------------|-------------------|------------------|
| Solid Earth tide | ±0.3 mGal | IERS Conventions Ch.7 |
| Ocean loading | ±0.03 mGal | FES2014 |
| Atmospheric pressure | ~0.3 μBar/mBar | Local barometer |
| Polar motion | ±0.01 mGal | IERS pole coordinates |
| Gravity gradient (terrain) | 0–1 mGal | DEM model |

---

## 4. Relative Gravimeters

### 4.1. Spring‑Based Gravimeter (LaCoste–Romberg)

| Property | Details |
|----------|---------|
| Principle | Spring mass on a LaCoste athermal spring; measures gravity difference |
| Precision | ~0.01 mGal |
| Accuracy | 0.05–0.1 mGal (after calibration) |
| Drift | 0.01–0.05 mGal/hour |
| Weight | ~5 kg (field model D) |
| Key use | Relative gravity surveys, microgravity |

The measurement equation

$ $ g_{\text{station}} = g_{\text{base}} + C \cdot R + d \cdot (t - t_0) + \text{corrections}$$

where $ C $= calibration factor,$ R $ = reading,$ d $ = drift rate,$ t $ = time.

### 4.2. Scintrex CG‑6 Autograv

| Property | Details |
|----------|---------|
| Principle | Quartz spring (aerostat design) |
| Precision | 0.5 $\mu $ Gal |
| Drift | < 2 $\mu $ Gal/hour |
| Weight | ~7 kg |
| Temperature compensation | Built‑in |

### 4.3. Relative Gravimeter Comparison

| Instrument | Precision | Drift | Best for |
|------------|-----------|-------|----------|
| **LC‑R Model D** | 0.01 mGal | 0.05 mGal/hr | Classical surveys |
| **LC‑R Model G** | 0.005 mGal | 0.02 mGal/hr | Microgravity, time‑lapse |
| **Scintrex CG‑6** | 0.5 μGal | 2 μGal/hr | Modern field work |
| **Scintrex CG‑5** | 1 μGal | 4 μGal/hr | Legacy field work |
| **Z‑L (Burris)** | 2 μGal | 10 μGal/hr | Rapid surveys |

---

## 5. Gravity Network Design

### 5.1. Network Hierarchy

| Level | Purpose | Accuracy | Connection |
|-------|---------|----------|------------|
| **Primary (absolute)** | Long‑term reference | 1 μGal | FG5 at IGSN71 stations |
| **Secondary (relative, precise)** | Regional control | 5–10 μGal | Connected to primary |
| **Tertiary (relative, reconnaissance)** | Detailed surveys | 50–100 μGal | Connected to secondary |
| **Microgravity** | Engineering, archaeology | 0.01 mGal | Local surveys |

### 5.2. Base Station Concept

Gravity surveys always reference **base stations** with known gravity values. The base station gravity is the anchor; all stations are measured relative to it.

$ $ g_{\text{station}} = g_{\text{base}} + \Delta g_{\text{field measurements}}$$

### 5.3. Tying to International Reference

The international gravity standard is the **International Gravity Standardization Net 1971 (IGSN71)**, with 1 254 stations worldwide.

| Reference | Source |
|-----------|--------|
| IGSN71 | International Association of Geodesy (IAG) |
| WGGS2011 | IAG Working Group on Global Gravity Data |
| GOCE satellite | Global gravity gradients from orbit |

---

## 6. Satellite Gravity Missions

| Mission | Agency | Period | Method | Precision |
|---------|--------|--------|--------|-----------|
| **GRACE** | NASA/DLR | 2002–2017 | Satellite‑to‑satellite tracking | ~1 cm equivalent water height (monthly) |
| **GRACE‑FO** | NASA/DLR | 2018–present | + Laser ranging interferometer | Improved over GRACE |
| **GOCE** | ESA | 2009–2013 | Gravity gradiometry | ~100 km resolution |
| **CHAMP** | GFZ | 2000–2010 | Satellite‑to‑satellite | ~300 km resolution |
| **Swarm** | ESA | 2013–present | Magnetic + gravity | Complementary |

Satellite gravity gives the **long‑wavelength** field (degree < 150); surface gravimetry fills in the high‑frequency detail.

---

## 7. Worked Example — Relative Gravity Survey

**Given:** Base station gravity $ g_B = 978\,052.432 $ mGal (IGSN71 reference).

| Station | Reading | Time | Correction |
|---------|---------|------|------------|
| Base (t₀) | 4521.2 | 08:00 | — |
| Station A | 4535.7 | 09:00 | — |
| Base (return) | 4521.4 | 10:00 | — |
| Station B | 4548.3 | 11:00 | — |
| Base (final) | 4521.5 | 12:00 | — |

**Step 1: Drift rate** (average over the day)

$ $\text{Drift} = \frac{4521.5 - 4521.2}{4\;\text{h}} = 0.075\;\text{counts/hour} $$

**Step 2: Drift correction at each station time:** $ $\begin{aligned}
\text{Station A}: \;& \text{drift correction} = 0.075 \times (9-8) = 0.075 \\
\text{Station B}: \;& \text{drift correction} = 0.075 \times (11-8) = 0.225
\end{aligned
}

$$ **Step 3: Drift‑corrected readings:** $ $

\begin{aligned}
R_A^{\text{corr}} &= 4535.7 - 0.075 = 4535.625\\
R_B^{\text{corr}} &= 4548.3 - 0.225 = 4548.075
\end{aligned}

$$ **Step 4: Gravity difference** (using calibration factor $ C = 1.0 $ mGal/count):

$ $

\begin{aligned}
\Delta g_A &= R_A^{\text{corr}} - R_{B,\text{avg}}^{\text{corr}} = 4535.625 - 4521.3 = 14.325\;\text{mGal}\\
\Delta g_B &= 4548.075 - 4521.3 = 26.775\;\text{mGal}
\end{aligned
}

$$**Step 5: Station gravities:** $ $ g_A = 978\,052.432 + 14.325 = 978\,066.757\;\text{mGal}g_B = 978\,052.432 + 26.775 = 978\,079.207\;\text{mGal}$$ ---

## 8. Diagram — Gravimeter Types

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200" width="700" height="200">
 <rect width="700" height="200" fill="#1a1a2e" rx="8"/>
 <text x="350" y="25" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle">Gravimeter Classification</text>
 <!-- Absolute branch -->
 <rect x="40" y="60" width="120" height="35" fill="#4cc9f0" rx="4"/>
 <text x="100" y="83" fill="#1a1a2e" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Absolute</text>
 <rect x="20" y="115" width="80" height="30" fill="#06d6a0" rx="4"/>
 <text x="60" y="135" fill="#1a1a2e" font-size="10" font-family="sans-serif" text-anchor="middle">Free‑Fall</text>
 <rect x="110" y="115" width="80" height="30" fill="#06d6a0" rx="4"/>
 <text x="150" y="135" fill="#1a1a2e" font-size="10" font-family="sans-serif" text-anchor="middle">Atom Interf.</text>
 <line x1="80" y1="95" x2="60" y2="115" stroke="#fff" stroke-width="1"/>
 <line x1="80" y1="95" x2="150" y2="115" stroke="#fff" stroke-width="1"/>
 <!-- Relative branch -->
 <rect x="250" y="60" width="120" height="35" fill="#f9c74f" rx="4"/>
 <text x="310" y="83" fill="#1a1a2e" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Relative</text>
 <rect x="220" y="115" width="80" height="30" fill="#7209b7" rx="4"/>
 <text x="260" y="135" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">Spring</text>
 <rect x="310" y="115" width="80" height="30" fill="#7209b7" rx="4"/>
 <text x="350" y="135" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">Supercond.</text>
 <line x1="300" y1="95" x2="260" y2="115" stroke="#fff" stroke-width="1"/>
 <line x1="300" y1="95" x2="350" y2="115" stroke="#fff" stroke-width="1"/>
 <!-- Sat branch -->
 <rect x="490" y="60" width="120" height="35" fill="#f72585" rx="4"/>
 <text x="550" y="83" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Satellite</text>
 <rect x="470" y="115" width="80" height="30" fill="#ff9f1c" rx="4"/>
 <text x="510" y="135" fill="#1a1a2e" font-size="10" font-family="sans-serif" text-anchor="middle">GRACE/‑FO</text>
 <rect x="560" y="115" width="80" height="30" fill="#ff9f1c" rx="4"/>
 <text x="600" y="135" fill="#1a1a2e" font-size="10" font-family="sans-serif" text-anchor="middle">GOCE</text>
 <line x1="540" y1="95" x2="510" y2="115" stroke="#fff" stroke-width="1"/>
 <line x1="540" y1="95" x2="600" y2="115" stroke="#fff" stroke-width="1"/>
</svg>

---

## 9. Applications in Geodesy

| Application | How gravity helps |
|-------------|-------------------|
| **Geoid modelling** | Gravity anomalies → Stokes integral →$ N $ (see [[Geoid]]) |
| **Survey height conversion** | Convert $ h $→$ H $ using gravimetric geoid |
| **Oil & mineral exploration** | Bouguer anomaly maps → subsurface density |
| **Volcanic monitoring** | Gravity changes → magma movement |
| **Hydrogeology** | Water table changes affect local $ g$ |
| **Engineering** | Void detection, archaeological prospection |

---

## 10. References

- Torge, W. & Müller, J., *Geodesy* (4th ed.), De Gruyter, 2012.

- Torge, W., *Gravimetry*, De Gruyter, 1989.

- Pontoise, B. et al., *Absolute gravimetry for geology, volcanology, and hydrogeology*, Comptes Rendus Physique, 2020.

- Crossley, D., Hinderer, J., Riccardi, U., *Measuring gravity everywhere*, Comptes Rendus Geoscience, 2013.

- IAG Division I: *Reference Frames*, https://iag.dgfi.tum.de/

- Micro‑g LaCoste, *FG5/FG5X Absolute Gravimeter*, Technical Manual, 2023.

- GRACE‑FO Mission: https://www.gracefo.jpl.nasa.gov/

- GOCE Mission: https://earth.esa.int/eogateway/missions/goce

➡️ [[Geodesy MOC]] · [[_Study Packs]] · [[Gravity Field]] · [[Geoid]]