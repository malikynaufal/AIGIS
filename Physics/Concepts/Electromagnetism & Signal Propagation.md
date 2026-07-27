---
tags: [aigis, concept, physics, electromagnetism, waves, signals, gnss]
created: 2026-07-27
updated: 2026-07-27
---

# Electromagnetism & Signal Propagation

## For Geodesy & GNSS Applications

**Core Idea:** Maxwell's equations unify electricity, magnetism, and light into a single framework. In geodesy, electromagnetic wave propagation is the basis of GNSS positioning — GPS, GLONASS, Galileo all rely on precise knowledge of how signals travel through the ionosphere, troposphere, and multipath environments.

---

## Fundamental Concepts

### Maxwell's Equations (Differential Form)

| Equation | Name | Statement |
|----------|------|-----------|
| $ \nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} $ | Gauss's law | Electric charges produce electric fields |
| $ \nabla \cdot \mathbf{B} = 0 $ | Gauss's law for magnetism | No magnetic monopoles |
| $ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} $ | Faraday's law | Changing magnetic fields produce electric fields |
| $ \nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t} $ | Ampère-Maxwell law | Currents and changing E-fields produce B-fields |

### Electromagnetic Wave Equation

From Maxwell's equations in vacuum (no sources)

$ $ \nabla^2 \mathbf{E} = \mu_0\varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} $$

**Speed of light:*
*

$ c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 299{,}792{,}458\ \text{m/s} $$$

# ## Plane Wave Solutio
n

$ $ \mathbf{E}(\mathbf{r}, t) = \mathbf{E}_0 \exp[i(\mathbf{k} \cdot \mathbf{r} - \omega t)]

$$

| Parameter | Symbol | Relation |
|-----------|--------|----------|
| Wave vector | $ \mathbf{k} $ | $ |\mathbf{k}| = \frac{2\pi}{\lambda} = \frac{\omega}{c} $ |
| Angular frequency | $ \omega $ | $ \omega = 2\pi f $ |
| Wavelength | $ \lambda $ | $ \lambda = c/f $ |
| Phase velocity | $ v_p $ | $ v_p = c/n $ (in medium with index $  n $) |

### Refraction in Media

| Medium | Index $ n $ | GNSS signal effect |
|--------|-----------|-------------------|
| Vacuum | 1.0000 | Reference (no delay) |
| Troposphere (wet) | ~1.0003 | ~2 m zenith delay |
| Troposphere (dry) | ~1.000284 | ~2.3 m zenith delay |
| Ionosphere (free electrons) | frequency-dependent | ±15 m (L1) to ±60 m (L5) |
| Multipath (reflective surfaces) | N/A | Phase distortion |

---

## In Geodesy & GNSS Context

### Ionospheric Delay

The ionosphere is a dispersive medium (frequency-dependent). The group delay and phase advance

$ $ \Delta\rho_{\text{iono}} = \frac{40.3 \cdot TEC}{f^2} $$

where:
- $ TEC $ = total electron content (electrons/m² along signal path)
-$ f $ = carrier frequency

**Dual-frequency combination** eliminates ionosphere

$ $ \rho_{\text{iono-free}} = \frac{f_1^2 \rho_1 - f_2^2 \rho_2}{f_1^2 - f_2^2} $$

For GPS: $ $ f_1 = 1575.42 $ MHz, $ f_2 = 1227.60 $ MHz $

### Tropospheric Delay

| Component | Zenith delay | Mapping function |
|-----------|-------------|------------------|
| Hydrostatic (dry) | ~2.3 m | $ m_h(\theta) = \frac{1}{\sin\theta + 0.00143\tan\theta + 0.0445/(\sin\theta+0.013)} $ |
| Wet | ~0.2–0.3 m | Requires meteorological data or estimation |

### GPS Signal Structure

**Carrier frequencies (L-band):**

- L1: 1575.42 MHz ( $\lambda \approx 19.05 $ cm)

- L2: 1227.60 MHz ( $\lambda \approx 24.42 $ cm)

- L5: 1176.45 MHz ( $\lambda \approx 25.48 $ cm)

**Multipath error:**
If direct signal combines with reflected signal

$ S = S_d + S_r e^{i\Delta\phi} $ where $\Delta\phi = \frac{2\pi}{\lambda}\cdot 2d\cos\theta $ (d = reflector distance).

Multipath period: $ T_m = \frac{\lambda}{2d\dot{\theta}} $— can be filtered if known.

### Pseudorange & Carrier Phase

**Pseudorange:*
*

$ $ \rho = c \cdot (t_{rx} - t_{tx}) + c\delta_{rx} - c\delta_{sat} + \delta_{iono} + \delta_{trop} + \delta_{mp} + \varepsilon

$$

**Carrier phase:*
*

$ $ \Phi = \lambda N + \rho + c\delta_{rx} - c\delta_{sat} - \delta_{iono} + \delta_{trop} + \varepsilon_\Phi

$ where $  N $ is the integer ambiguity (key to centimeter-level positioning).$

### Faraday Rotation in Ionosphere

The ionosphere rotates the polarization plane of EM signals

$ $ \Delta\chi = \frac{e^3}{8\pi^2\varepsilon_0 m_e^2 c^2} \frac{B \cos\theta}{f^2} \cdot TEC

$$

This affects signal reception quality and is used in geomagnetic studies.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ c = 1/\sqrt{\mu_0\varepsilon_0} $ | Speed of light | EM wave velocity |
| $ \Delta\rho_{iono} = 40.3 \cdot TEC / f^2 $ | Ionospheric delay | GPS error |
| $ \rho_{iono-free} = (f_1^2\rho_1 - f_2^2\rho_2)/(f_1^2-f_2^2) $ | Dual-freq combination | Eliminate iono |
| $ c \cdot \Delta t = \text{range} $ | Time-of-flight | Pseudorange |
| $ \Phi = \lambda N + \rho + \text{errors} $ | Carrier phase equation | RTK/PPP |
| $ \nabla \times \mathbf{B} = \mu_0\varepsilon_0\partial_t\mathbf{E} $ | Ampère-Maxwell | EM theory |

---

## Related Concepts

- [[GNSS]] — Full GNSS system integration

- [[Ionospheric Delay]] — Detailed ionospheric models

- [[PPP]] — Precise point positioning

- [[RTK]] — Real-time kinematics

- [[Newtonian Mechanics]] — Satellite dynamics (orbital mechanics)

- [[Gravitational Potential]] — Relativistic corrections

---

## Study Problems

1. **Recall:** Compute the GPS L1 wavelength. How many wavelengths fit in 1 km?
2. **Application:** A GPS dual-frequency receiver measures $ \rho_1 = 20,000,000.150 $  m and $\rho_2 = 20,000,000.430 $ m. Compute the ionosphere-free range and the ionospheric delay at L1.
3. **Derivation:** Show that the speed of an EM wave in vacuum is $c \approx 3 \times 10^8 $ m/s using $ \mu_0 = 4\pi \times 10^{-7} $ H/m and $\varepsilon_0 = 8.854 \times 10^{-12} $ F/m.
4. **Real-world:** During a solar storm, TEC increases by a factor of 10. What is the new ionospheric delay at L1 for a zenith signal? What positioning error does this introduce?

---

## Common Mistakes

1. **Confusing group velocity and phase velocity:** In dispersive media they differ — group velocity carries information.
2. **Ignoring sign:** Ionospheric delay is a group delay but phase advance — same magnitude, opposite sign.
3. **Treating troposphere as vacuum delay:** It's ~2.5 m of range error if unaccounted for.
4. **Assuming multipath can be eliminated by dual-frequency:** Multipath is geometry-dependent, not frequency-dependent.
5. **Forgetting that $N$ (integer ambiguity) must be resolved** — without it, carrier phase is only useful for relative positioning.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*