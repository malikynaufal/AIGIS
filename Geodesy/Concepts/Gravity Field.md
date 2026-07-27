---
tags: [geodesy, concept, physical-geodesy, aigis]
aliases: [Gravity Field, Medan Gaya Berat, Gravity]
created: 2026-07-12
---

# 🌀 Gravity Field

The **gravity field** of Earth is the combined effect of gravitational attraction and the centrifugal force arising from Earth's daily rotation. Every point in and around the Earth experiences a net acceleration $\vec{g} $that defines the direction of "down" at that location and shapes the equipotential surfaces upon which geodesy is built
.

$$\vec{g} = \vec{g}_{\text{grav}} + \vec{g}_{\text{centrifugal}} $$**Medan gaya berat** (gravity field) is the vector field $\vec{g}(\mathbf{r}) $that varies with position both in magnitude and direction.

## Mathematical Representation: Spherical Harmonics

Because Earth is roughly spherical, the gravity potential $W $is most conveniently expanded in **spherical harmonics** — an infinite series of orthogonal functions on the sphere
:

$$W(r, \theta, \lambda) = \frac{GM}{r} \sum_{n=0}^{\infty} \sum_{m=0}^{n} \left( \frac{a}{r} \right)^{n} \left( C_{nm} \cos m\lambda + S_{nm} \sin m\lambda \right) P_{nm}(\cos \theta)$$

| Symbol | Meaning | Bahasa Indonesia |
|--------|---------|------------------|
| $W$ | Gravity potential | Potensi gravitasi |
| $G$ | Gravitational constant | Konstanta gravitasi |
| $M$ | Earth's mass | Massa Bumi |
| $r$ | Radial distance from Earth's centre | Jarak radial dari pusat Bumi |
| $a$ | Reference ellipsoid semi-major axis | Sumbu semi-mayor ellipsoid acuan |
| $C_{nm}, S_{nm} $ | Stokes (cos/sin) potential coefficients | Koefisien potensial Stokes |
| $P_{nm} $ | Associated Legendre function | Fungsi Legendre terkait |
| $\theta$ | Geocentric colatitude | Kolatitud kosmik |
| $\lambda$ | Longitude | Bujur |

- The $n=0, m=0 $term is the **monopole** — the point-mass potential $GM/r$.

- The $n=1, m=0 $term is the **dipole** — due to Earth's equatorial bulge and centrifugal effects.
-$n \geq 2 $terms are **higher-degree harmonics** capturing the irregular mass distribution (mountains, subduction zones, mantle convection).

- The fully normalized (Schmidt semi-normalized) coefficients $\bar{C}_{nm}, \bar{S}_{nm} $are the ones published by global models (EGM96, EGM2008, GOCO06s).

**Koefisien potensial** (potential coefficients) $C_{nm} $and $S_{nm} $are estimated from satellite orbit perturbations (GRACE, GOCE), surface gravity measurements, and satellite altimetry.

## The Gravity Potential & Its Properties

The total gravity potential $W $combines the attractive Newtonian potential $V $and the centrifugal potential $\Phi$:

$$W = V + \Phi, \qquad \Phi = -\frac{1}{2} \omega^{2} r^{2} \cos^{2} \theta$$where $\omega $is Earth's angular velocity (rotasi Bumi). Key properties:

1. **Laplace's equation** outside the mass:$\nabla^{2} V = 0$.
2. **Poisson's equation** inside the mass: $\nabla^{2} V = 4\pi G\rho$.
3. The gravity vector is the gradient of the potential: $\vec{g} = -\nabla W$.

The potential is what links **geometry** (ellipsoids) to **physics** (the gravity field) — a cornerstone of **Physical Geodesy** (Geodesi Fisika).

## Gravity Anomalies

A **gravity anomaly** is the difference between observed gravity $g_{\text{obs}} $and a computed normal gravity $\gamma $on the reference ellipsoid
:

$$\Delta g = g_{\text{obs}} - \gamma$$

Types of gravity anomaly:

- **Free-air anomaly**$\Delta g_{\text{FA}} $: Corrects for elevation only (butur bebas).

$$\Delta g_{\text{FA}} = g_{\text{obs}} + g_{\text{Fay}} - \gamma$$where $g_{\text{Fay}} \approx 0{.}3086 \;\text{mGal/m} $is the free-air gradient (gradien butur bebas).

- **Bouguer anomaly**$\Delta g_{\text{B}} $: Further removes the attraction of the rock slab between the station and the ellipsoid (koreksi Bouguer).

$$\Delta g_{\text{B}} = \Delta g_{\text{FA}} - g_{\text{Bouguer}}; \quad g_{\text{Bouguer}} = 2\pi G \rho h \approx 0{.}0419 \;\rho h \;\text{mGal} $$with $\rho $in g/cm³ and $h $in metres.

- **Isostatic anomaly**: Removes isostatic compensation (keseimbangan isostatik) as well — used to study deep crustal structure.

Gravity anomalies reveal subsurface density variations that cannot be seen from geometry alone. Positive anomalies often correspond to high-density features (basement uplifts, ophiolites); negative anomalies to sedimentary basins or zones of low crustal density.

## The Geoid Computation

The **geoid** is the equipotential surface of the gravity field that coincides (ideally) with mean sea level. Its undulation $N$(geoid undulation, aturan geoid) relative to the ellipsoid at point$(\phi, \lambda) $is given by:

**Stokes' formula** (integral approach)
:

$$N(\phi, \lambda) = \frac{R}{4\pi \gamma} \iint_{\sigma} \Delta g(\phi', \lambda') \, S(\psi) \, d\sigma'$$where $S(\psi) $is the **Stokes kernel function**
:

$$S(\psi) = \frac{d}{d\psi} \left[ \psi \, \frac{\cos\frac{\psi}{2}}{\sin\frac{\psi}{2}} \right]$$and $\psi $is the **angular distance** between the computation point and the integration point, computed via the spherical law of cosines
:

$$\cos \psi = \sin\phi \sin\phi' + \cos\phi \cos\phi' \cos(\lambda - \lambda')$$

**Practical modern approach**: Use a truncated spherical harmonic expansion (EGM2008 to degree/order 2190 or even 4240) and compute the geoid height directly
:

$$N(\phi, \lambda) = \frac{GM}{\gamma a} \sum_{n=2}^{N_{\max}} \sum_{m=0}^{n} \left( \frac{a}{r} \right)^{n+1} \frac{1}{\gamma} \left( C_{nm} \cos m\lambda + S_{nm} \sin m\lambda \right) P_{nm}(\cos \phi) \cdot \frac{n+1}{n} $$

The **relationship between ellipsoidal height**$h$, **orthometric height**$H$, and **geoid height**$N $is:

$$h = H + N$$

This equation is one of the most important in physical geodesy, allowing conversion between GNSS-derived ellipsoidal heights and traditional levelling-derived orthometric heights.

## Global Gravity Models

| Model | Max degree/order | Year | Source |
|-------|------------------|------|--------|
| EGM96 | 360 | 1996 | Joint NASA/NGA |
| EGM2008 | 2190 | 2008 | EGM Development Team |
| GOCO05S | 200 | 2010 | Combined GOCE + GRACE |
| GOCO06s | 360 | 2016 | Combined GOCE + GRACE/GRACE-FO |
| EIGEN-6C4 | 2190 | 2018 | GFZ/DGFI/GRGS |

Satellite missions such as **GRACE** (Gravity Recovery and Climate Experiment) and **GOCE** (Gravity field and steady-state Ocean Circulation Explorer) have revolutionised our ability to model the gravity field at high resolution, tracking temporal variations due to ice-sheet melt, groundwater depletion, and post-glacial rebound.

## Related

- [[Geoid]] · [[Geoid Undulation]] · [[Reference Ellipsoid]] · [[Physical Geodesy]] · [[Kurikulum Overview]]

➡️ [[Geodesy MOC]]
