---
tags: [aigis, concept, geodesy, geoid, orthometric-height, physical-geodesy, gravimetry]
created: 2026-07-27
updated: 2026-07-27
---

# Geoid

## For Geodesy & Physical Geodesy

**Core Idea:** The geoid is equipotential surface of gravity that best fits global mean sea level. It defines the "true" shape of Earth for height systems. Geoid undulation $N $ (the distance between the ellipsoid and the geoid) converts between ellipsoidal height $  h $ and orthometric (gravity-based) height $  H $: $  h = H + N $.

---

## Fundamental Concepts

### The Geoid Defined

- **Equipotential surface** of the gravity field $ W = \text{const} $- Passes through mean sea level (MSL) globally

- Irregular due to mass anomalies (mountains, trenches, density variations)

- **Not a mathematical surface** — must be modeled from gravity data

### Height Systems

| Height Type | Symbol | Reference Surface | Units |
|-------------|--------|-------------------|-------|
| **Ellipsoidal** | $ h $ | Reference ellipsoid | m |
| **Orthometric** | $ H $ | Geoid (MSL) | m |
| **Normal** | $ H^*$ | Quasi-geoid | m |
| **Dynamic** | $ H_d $ | Geopotential number | m²/s² |

### Fundamental Relationships

$ $  h = H + Nh = H^* + \zetaN - \zeta = \text{dynamic topography}$$

where:
-$ N $ = **geoid undulation** (ellipsoid → geoid)
-$\zeta $= **quasi-geoid undulation** (ellipsoid → quasi-geoid)

---

## Computing the Geoid

### From Gravity Anomalies (Stokes' Integral
)

$ $ N_p = \frac{R}{4\pi\gamma} \int_\sigma \Delta g(q) S(\psi)\,d\sigma(q)$$

where:
-$ S(\psi) = \sin\psi + 3\sin\psi/2 \cot(\psi/2) - 2 $= Stokes function
-$\Delta g $= gravity disturbance
-$\psi $= spherical distance from point $  p $**Practical limitation:** Requires global gravity data.

### From Gravimetric-geometric Hybrid (Remove-Compute-Restore)

**Step 1 (Remove):** Subtract the ellipsoidal gravity field computed from a reference ellipsoi
d

$ $\Delta g_{res} = \Delta g_{obs} - g_{ref} $ $**Step 2 (Compute):** Compute $  N $ from residual gravity using Stokes' integral

**Step 3 (Restore):** Add back the gravity from topography (Bouguer plate approximation
)

$ $  N = N_{res} + N_{topo} $$

# ## Modern Hybrid Methods

| Method | Source | Resolution |
|--------|--------|------------|
| EGM96 | Satellite + gravimetry | 16' × 16' |
| EGM2008 | EIGEN-GL04C | 5' × 5' (~10 km) |
| EIGEN-6C4 | GOCE + GRACE | 5' × 5' |
| GOCO05s | GRACE + GOCE | 5' × 5' |
| EGM2020 (in development) | Improved models | Higher resolution |

### GOCE Satellite Contribution

GOCE (Gravity Field and Steady-State Ocean Circulation Explorer) measured gravity gradients:

$ $ \begin{aligned}
\Gamma_{xx} &= \frac{\partial^2 V}{\partial x^2} - \frac{2}{r}V + \text{...} \\
\Gamma_{zz} &= \frac{\partial^2 V}{\partial z^2} - \frac{2}{r}V
\end{aligned} $$---

## In Geodesy Context

### GPS Heighting Problem

GNSS gives ellipsoidal height $ h $. Surveying needs orthometric height $  H $:

$ $  H = h - N $ $**Example:** If $  h = 25.000 $ m and $  N = 37.514 $ m (EGM2008 at Jakarta)

$ $  H = 25.000 - 37.514 = -12.514\ \text{m}$$

(negative = below geoid!)

Or wait —$ N $ is positive (ellipsoid above geoid), so $  H = 25.000 - 37.514 = -12.514 $ m would mean the ground is 12.5 m BELOW the geoid. This happens in areas near oceans where the geoid dips.

### Geoid Models for Indonesia

Using EGM2008 for Indonesia:

| Location | $ N $ (EGM2008, m) | Reference ellipsoid |
|----------|------------------|---------------------|
| Jakarta (south coast) | ~37 m | WGS84 |
| Sumatra (equatorial) | ~31 m | WGS84 |
| Papua (highlands) | ~10 m | WGS84 |
| Java mountains | ~40 m | WGS84 |

### Dynamic Topography (Ocean Bottom)

In the ocean, the geoid IS the sea surface. Dynamic topography $\eta_{dyn} $ is the deviation of the actual sea surface from the geoid $ $\eta_{dyn} = \frac{1}{\rho g} \int \text{ocean currents (dynamic)} + \text{wind-driven} + \text{thermosteric} $$

This is important for ocean geoid models and sea level studies.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ h = H + N $ | Height relationship | GPS heighting |
| $ N_p = \frac{R}{4\pi\gamma}\int \Delta g S d\sigma $ | Stokes' equation | Geoid from gravity |
| $\Gamma_{ij} = \partial_i\partial_j V - \frac{2}{r}\delta_{ij}V $ | GOCE gradients | Satellite gravity |
| $ N_{modern} = N_{residual} + N_{topo} $ | Remove-Compute-Restore | Practical geoid |

---

## Related Concepts

- [[Physical Geodesy]] — Broader context

- [[Geodetic Coordinates]] — Ellipsoidal height $ h $- [[Orthometric Height]] — Gravity-based height $  H $- [[WGS84]] / [[GRS80]] — Reference ellipsoids

- [[Eccentricity]] — Used in gravity formulas

- [[Least Squares Adjustment]] — Geoid modeling as inverse problem

---

## Study Problems

1. **Recall:** Explain why GPS gives ellipsoidal height, not orthometric height. What additional measurement is needed?
2. **Application:** Compute orthometric height for a point with $ h = 50.000 $  m and $ N = 37.514 $ m. Is the point above MSL? (Answer depends on sign convention — check EGM2008 value for your location.)
3. **Derivation:** Derive the relationship $\Delta h = 0 \implies dH = -dN $ (along the geoid surface). What does this tell you about how geoid undulation affects orthometric heights?
4. **Real-world:** You need to connect a GPS benchmark to a national leveling network. The GPS ellipsoidal heights are known, and $ N $ from EGM2008 has an accuracy of ±5 cm. What is the uncertainty in the resulting orthometric heights?

---

## Common Mistakes

1. **Assuming $ N $ is always positive** — it can be negative (geoid below ellipsoid, e.g., near Indian Ocean).
2. **Confusing $ N $ (geoid undulation) with $\zeta $ (quasi-geoid)** for practical applications.
3. **Not accounting for the geoid model's accuracy** in height transformations.
4. **Using the wrong sign:**$ H = h - N $ (subtract), NOT add $  N $.
5. **Treating orthometric heights as ellipsoidal heights** — they differ by $ N$, which can be tens of meters.

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*