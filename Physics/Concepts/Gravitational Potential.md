---
tags: [aigis, concept, physics, gravitation, geopotential]
aliases: [Gravitational Potential, Geopotential]
created: 2026-07-26
updated: 2026-07-27
---

# Gravitational Potential

## Potential Theory, Geopotential, Equipotential Surfaces

**Core Idea:** The gravitational potential $U $ describes the energy field of Earth's mass — from it we derive gravity, the geoid, and height systems.

---

## 1. Fundamental Concepts

### Gravitational Potential (Point Mass
)

$ $ U(\vec{r}) = -\frac{GM}{r} $$

where $ G = 6.674\times10^{-11} $ m³/(kg·s²), $  M = 5.972\times10^{24} $ kg,$  r = |\vec{r}| $**Physical meaning:** Work per unit mass to bring a test mass from infinity to point $ \vec{r} $.

### Gravity Vector from Potential

$ $ \vec{g} = \nabla U = \frac{\partial U}{\partial \vec{r}
}

$ In spherical coordinates: $ $ \vec{g} = \frac{\partial U}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial U}{\partial \phi}\hat{\phi} + \frac{1}{r\cos\phi}\frac{\partial U}{\partial \lambda}\hat{\lambda} $

$ $ ---

## 2. Potential Theory

### Laplace's Equation (Outside mass sources
)

$$ \nabla^2 U = 0

$ $

### Poisson's Equation (With mass sources
)

$$ \nabla^2 U = 4\pi G\rho

$ $

### Spherical Harmonic Expansion
The general solution (valid outside mass sources) for the gravitational potential

$$ U(r, \phi, \lambda) = \frac{GM}{r}\left[1 - \sum_{n=2}^{\infty} \sum_{m=0}^{n} \left(\frac{R_e}{r}\right)^n P_{nm}(\sin\phi)(C_{nm}\cos m\lambda + S_{nm}\sin m\lambda)\right] $ $

where:
- $ P_{nm} $ = associated Legendre polynomials
- $ C_{nm} $, $ S_{nm} $ = Stokes coefficients (from observation)
- $ R_e $ = mean Earth radius

### Key Properties of $ P_{nm} $- $ P_{nm}(\sin\phi) $ are orthogonal on $ [-1,1] $- $ P_0^0 = 1 $, $ P_1^0 = \sin\phi $ (dipole term — zero for Earth)
- $ P_2^0 = \frac{1}{2}(3\sin^2\phi - 1) $ (quadrupole — dominant $ J_2 $ term)

---

## 3. Normal Gravity and the Geoid

### Normal Gravity (Somigliana Formula
)

$ $ \gamma(\phi) = \frac{GM}{a^2} \cdot \frac{1 + k\sin^2\phi}{\sqrt{1-e^2\sin^2\phi}} $$

where $ k = \frac{b \cdot \gamma_p - a \cdot \gamma_a}{a \cdot \gamma_a} $ Numerical approximation (IGAFW 1980) $ $

 \gamma(\phi) = 9.780327(1 + 0.0053024\sin^2\phi - 0.0000058\sin^2 2\phi) \text{ m/s}^2

$$

# ## Equipotential Surfaces
Surfaces where gravitational potential is constant:

- **Geoid:** Equipotential surface that best fits mean sea level

- **Reference ellipsoid:** Rotationally symmetric equipotential (normal gravity)
- $ V = \text{const} $ on all equipotential surfaces (gradient of $  V $ is perpendicular to surface)

---

## 4. Geoid Undulation and Height Systems

### Disturbing Potentia
l

$ T = W - V $ where $  W $ = true gravity potential,$  V $ = normal gravity potential.

### Geoid Undulation (Bruns' Formula)

$ N = \frac{T}{\gamma} $$$

# ## Height Systems (Relationship)

|| Height Type | Definition | Relation |
|---|---|---|---|
| **Ellipsoidal ( $ h $)** | Distance from reference ellipsoid (GNSS) | $  h = H + N $ |
| **Orthometric ( $ H $)** | Height above geoid, along plumb line | $  H = h - N $ |
| **Normal ( $ H^*$)** | Height above quasigeoid | $ H^* = h - \zeta $ |
| **Dynamic ( $ H_{dyn} $)** | Proportional to gravity potential | $ H_{dyn} = \frac{C-W}{\gamma_0} $ |

### Molodensky's Formula
Relates the topographic effect on $ T $:

$ $ T(P) \approx \int_0^H \left(\frac{\partial \gamma^*}{\partial H^*}\right) \, dH^* \\quad \text{(approximate, simplified)} $$

---

## 5. Geopotential Number

A geopotential number $ C $ is the potential difference between the geoid and point P

$ C = \int_P^{\text{geoid}} g \, dh $ For practical computation (assuming constant $  g $):

$ C \approx \bar{g} \cdot H $ where $\bar{g} $ is the mean gravity along the plumb line from geoid to P.

---

## 6. Key Constants and Parameters

| Symbol | Value | Unit |
|--------|-------|------|
| $ GM $ | 3.986004418×10¹⁴ | m³/s² |
| $ a $ (equatorial radius) | 6,378,137 | m |
| $ b $ (polar radius) | 6,356,752.314 | m |
| $ f = (a-b)/a $ | 1/298.257223563 | — |
| $ \omega $ (rotation) | 7.292115×10⁻⁵ | rad/s |
| $ J_2 $ (dynamic form factor) | 1.08263×10⁻³ | — |
| $ \gamma_0 $ (equator) | 9.7803267715 | m/s² |
| $ \gamma_{90} $ (pole) | 9.8321863685 | m/s² |

### Normal Gravity Formula (Series Expansion
)

$ $ \gamma(\phi) \approx 9.780327\left[1 + (0.0053024 - 0.0000058\sin^2\phi)\sin^2\phi\right] \text{ m/s}^2

$$

---

## 7. Applications Checklist

| Application | Formula Used |
|-------------|-------------|
| GNSS heighting | $ H = h - N $ |
| Satellite orbit | $ U(\vec{r}_{\text{sat}}) \to $ force law $ \to $ orbit |
| Gravity anomalies | $ \Delta g = g_{\text{obs}} - \gamma $ |
| Geoid determination | Stokes integral over $ \Delta g $ |
| Physical geodesy | Disturbing potential $ T = W - V $ |
| Height anomaly | $ \zeta = T/\gamma^*$ |

---

## 8. Derivation of Normal Gravity Potential (Laplace)

The normal gravity potential on a rotating ellipsoid

$ V = \frac{GM}{r}\left[1 - \sum_{n=2}^{\infty} \left(\frac{a}{r}\right)^n J_n P_n(\sin\phi)\right] + \frac{\omega^2 r^2}{2}\cos^2\phi $$$

The first term is the potential due to the non-spherical mass distribution (zonal harmonics). The second term is the centrifugal potential from Earth's rotation.

---

## 9. Worked Examples

### Example 1: Geoid Undulation from GPS + Gravity
Given: GPS height $ h = 152 $ m, orthometric height $  H = 145 $ m
.

$ $ 

N = h - H = 152 - 145 = 7 \text{ m
}

**### Example 2: Normal Gravity at 45°N **

 \gamma(45°) = 9.780327(1 + 0.0053024 \times 0.5 - 0.0000058 \times \sin^2 90°)= 9.780327(1 + 0.0026512 - 0.0000058) = 9.780327 \times 1.0026454\approx 9.80619 \text{ m/s}^2

$$

# ## Example 3: Gravity at 10 km Altitude
Approximation: $ \Delta g \approx -2g \frac{\Delta h}{R} $

$ $ g(10\text{ km}) \approx 9.81 - 2(9.81)\frac{10000}{6.371\times10^6} = 9.81 - 0.0308 = 9.779 \text{ m/s}^2 $$

---

## 10. Study Problems
1. Compute the gravitational potential at the Earth's surface.
2. Derive normal gravity at latitude 45° using the Somigliana formula.
3. Convert between orthometric and ellipsoidal heights for a GNSS station.
4. Explain why geoid undulation varies geographically from -100 m (ocean) to +50 m (India).
5. Compute gravitational potential at GPS satellite altitude (20,200 km).
6. Expand the normal gravity potential $ V $ in zonal harmonics up to $ n=2$.
7. Show that equipotential surfaces are orthogonal to gravity vectors.

---

## References

- Torge, W. & Müller, J., "Geodesy" (4th ed.)

- Heiskanen & Moritz, "Physical Geodesy"

- Vaníček & Krakiwsky, "Geodesy: The Concepts"

- Featherstone & Rüeger, TUM-Grace gravity models

- OpenStax (gravitation chapters)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
