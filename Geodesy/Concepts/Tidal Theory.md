---
tags: [geodesy, concept, physical-geodesy, aigis]
aliases: [Tidal Theory, Teori Pasang Surut]
created: 2026-07-27
---

# 🌊 Tidal Theory

**Tidal theory** in geodesy studies the periodic deformation of the solid Earth, oceans, and atmosphere caused by gravitational attraction of the Moon, Sun, and other celestial bodies. These **tidal effects** must be modelled and removed (or corrected) in precise geodetic measurements — otherwise they introduce systematic errors of **0.1–1.0 m** in positions.

> **Indonesian term:** *Teori Pasang Surut (Pasut)*

---

## 1. Three Components of Tidal Deformation

| Component | Physical cause | Effect on measurements |
|-----------|---------------|------------------------|
| **Earth (body) tides** | Gravitational pull deforms solid Earth | Displaces ground by ~0.3 m vertically |
| **Ocean tides** | Deformation of ocean surface | Changes ocean loading → deforms ground by ~0.05 m |
| **Pole tide** | Change in rotation pole position | Periodic signal ~0.01 m |

---

## 2. Earth (Solid) Tides

The tidal potential from a body of mass $m $ at distance $  r $ is expanded in spherical harmonics. The dominant term is the **second‑degree** component (the first degree is a pure translation and does not deform) $ $ V_{\text{tide}}(r,\theta,\lambda,t) = \sum_{n=2}^{3} \sum_{m=0}^{n} V_{nm}(\theta,\lambda,t)\left(\frac{r_0}{r}\right)^{n+1} $$

# ## 2.1. Displacement due to solid Earth tides

The IERS Conventions (2010) prescribe the displacement at the Earth's surface as:

$ $ \begin{aligned}
\Delta r &= \sum_{n=2}^{3} h_n \frac{V_n(\theta,\lambda)}{g} \cdot r_0 \\
\Delta\theta &= \sum_{n=2}^{3} l_n \frac{1}{r_0}\frac{\partial V_n}{\partial\theta} \cdot \frac{r_0}{g} \\
\Delta\lambda &= \sum_{n=2}^{3} l_n \frac{1}{r_0\sin\theta}\frac{\partial V_n}{\partial\lambda} \cdot \frac{r_0}{g}
\end{aligned} $$

where:

| Symbol | Meaning |
|--------|---------|
| $ h_n $ | Love number (radial deformation);$ h_2 \approx 0.609 $, $ h_3 \approx 0.295 $ |
| $ l_n $ | Shida number (horizontal deformation);$ l_2 \approx 0.085 $, $ l_3 \approx 0.015 $ |
| $ g $ | Mean gravity at surface |
| $ V_n $ | $  n $‑th degree tidal potential |
| $ r_0 $ | Mean Earth radius |

### 2.2. Typical amplitude

| Direction | Typical amplitude (peak) | Period |
|-----------|--------------------------|--------|
| **Radial** (up/down) | ~30 cm | ~12 hours (semidiurnal) |
| **Horizontal** | ~5 cm | ~12 hours |

> After correction for solid Earth tides, residuals should be **< 5 mm**.

---

## 3. Ocean Tides and Loading

### 3.1. Ocean tide models

The deforming of the ocean surface under tidal forces creates a loading that pushes down on the Earth's crust. Ocean tide models provide the water column height $ H_i(\theta,\lambda,t) $ at grid points:

| Model | Source | Resolution | Coverage |
|-------|--------|------------|----------|
| **FES2014** | LEGOS/Toulouse | 1/16° | Global |
| **GOT4.8** | GSFC | 1° (with correction) | Global |
| **TPXO9** | Oregon State | 1/6° | Global |
| **NAO.99b** | JAMSTEC | 1/8° | Global |

### 3.2. Ocean loading displacement

The displacement due to ocean loading

$ $\mathbf{d}_{\text{load}}(t) = \sum_i \int_{\text{area}} \mathbf{G}(\theta,\theta_i) \cdot \rho_w \cdot H_i(\theta_i,\lambda_i,t)\,\mathrm{d}\Omega

$$

where $\mathbf{G} $ is the Green's function for elastic loading (relates a point mass at the surface to the displacement at the observation point). The **Bos & Becker (2012)** Green's functions are widely used.

| Direction | Typical amplitude | Notes |
|-----------|-------------------|-------|
| Vertical | 2–5 cm | Largest at coastlines |
| Horizontal | 1–2 cm | |

### 3.3. Loading in Indonesia

Indonesia's complex coastlines and numerous islands mean:

- **Ocean loading can be 3–10 cm vertical** at coastal stations.

- **Essential for PPP and precise levelling** in island areas.

- Use FES2014 or GOT4.8 for corrections.

---

## 4. Tide Gauges and Mean Sea Level

Tide gauges record the ocean surface height relative to a fixed benchmark

$ $\text{MSL}(T) = \frac{1}{T}\int_0^T \eta(t)\,\mathrm{d}t

$$

| Tidal constituent | Symbol | Period | Type | Origin |
|-------------------|--------|--------|------|--------|
| Principal lunar semidiurnal | $ M_2 $ | 12.421 h | Semidiurnal | Moon |
| Principal solar semidiurnal | $ S_2 $ | 12.000 h | Semidiurnal | Sun |
| Larger lunar elliptic | $ N_2 $ | 12.658 h | Semidiurnal | Moon (elliptic orbit) |
| Luni‑solar diurnal | $ K_1 $ | 23.934 h | Diurnal | Moon + Sun |
| Principal lunar diurnal | $ O_1 $ | 25.819 h | Diurnal | Moon |
| Solar diurnal | $ P_1 $ | 24.066 h | Diurnal | Sun |
| Mean sea level | $ M_0 $ | — | — | Integration of series |

The equilibrium tide (theoretical response to a point mass) has a maximum range of ~0.54 m at high latitudes.

---

## 5. Worked Example – Solid Earth Tide Correction

Compute the radial displacement at a point in Jakarta ( $\varphi = -6.2°$, $\lambda = 106.8°$) due to the Moon at a given epoch.

The Moon's tidal potential coefficient $ V_2 $ (degree 2) can be evaluated from the Moon's position. For a typical alignment:

$ $\Delta r = h_2 \frac{V_2}{g} \cdot r_0 \approx 0.609 \times \frac{0.15\;\text{m}^2\text{s}^{-2}}{9.78\;\text{m s}^{-2}} \times 6\,371\,000 \;\text{m} \approx 29.4\;\text{cm} $$

(The exact value depends on the Moon's position; the maximum is ~40 cm.)

---

## 6. Diagram – Tidal Correction Pipeline for GNSS

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200" width="700" height="200">
 <rect width="700" height="200" fill="#1a1a2e" rx="8"/>
 <text x="350" y="25" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle">GNSS Tidal Correction Workflow</text>
 <!-- Steps -->
 <g font-family="sans-serif" font-size="10" fill="#fff" text-anchor="middle">
 <rect x="20" y="60" width="120" height="50" fill="#4cc9f0" rx="6"/>
 <text x="80" y="85">Observation epoch</text>
 <rect x="160" y="60" width="130" height="50" fill="#7209b7" rx="6"/>
 <text x="225" y="80">Solid Earth Tide</text>
 <text x="225" y="92">h₂, l₂, V₂</text>
 <rect x="310" y="60" width="120" height="50" fill="#f72585" rx="6"/>
 <text x="370" y="80">Ocean Loading</text>
 <text x="370" y="92">FES2014 / GOT4.8</text>
 <rect x="450" y="60" width="120" height="50" fill="#f9c74f" rx="6"/>
 <text x="510" y="80">Pole Tide</text>
 <text x="510" y="92">IERS pole coords</text>
 <rect x="590" y="60" width="90" height="50" fill="#06d6a0" rx="6"/>
 <text x="635" y="85">Corrected pos.</text>
 </g>
 <!-- Arrows -->
 <g stroke="#fff" stroke-width="2" fill="none" marker-end="url(#a)">
 <line x1="140" y1="85" x2="160" y2="85"/>
 <line x1="290" y1="85" x2="310" y2="85"/>
 <line x1="430" y1="85" x2="450" y2="85"/>
 <line x1="570" y1="85" x2="590" y2="85"/>
 </g>
 <text x="350" y="170" fill="#ccc" font-size="10" font-family="sans-serif" text-anchor="middle">After all corrections, residual tidal signal &lt; 5 mm</text>
</svg>

---

## 7. Related

- [[Physical Geodesy]] – the field that studies gravity and tides.

- [[Geoid]] – the geoid is an equipotential surface affected by tides.

- [[Gravity Field]] – tidal forces contribute to temporal gravity variations.

- [[IERS]] – publishes tidal models and corrections.

- [[GNSS]] – precise positioning requires tidal corrections.

---

## 8. References

- Petit, G. & Luzum, B. (eds.), *IERS Conventions (2010)*, Chapter 7: Tidal Displacements, IERS TN No. 36, 2010.

- Agnew, D.C., *Earth Tides*, in *Treatise on Geophysics*, Vol. 3, 2007. DOI:10.1016/B978-044452748-6.00059-5

- Bos, M.S. & Becker, M., *On the accuracy of global ocean loading Green's functions*, Geophys. J. Int., 191, 1407‑1427, 2012. DOI:10.1111/j.1365-246X.2012.05694.x

- Ray, R.D., *Precise comparisons of bottom‑pressure recorders and ocean tide models*, Geophys. J. Int., 2013.

- FES2014 global ocean tide model, LEGOS/Toulouse, https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes.html

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]