---
tags: [aigis, concept, physics, mechanics, newton, geodesy]
aliases: [Newton's Laws, Newtons Laws]
created: 2026-07-26
updated: 2026-07-27
---

# Newton's Laws of Motion

## General Applications and Geodesy

**Core Idea:** Three laws describing the relationship between forces and motion — the foundation of classical mechanics, orbital mechanics, and satellite geodesy.

---

## 1. First Law (Law of Inertia)

$$ \sum \vec{F} = 0 \implies \vec{v} = \text{constant} $$

An object at rest stays at rest; an object in motion stays in motion with constant velocity unless acted upon by a net external force.

### Physical Meaning

- Defines **inertial reference frames** — frames where Newton's 1st law holds
- There is no absolute rest; any non-accelerating frame is equally valid

### Geodesy Connection

- Reference frames: Inertial (ICRS) vs. non-inertial (Earth-fixed, ECEF)
- GNSS satellites: "free fall" orbits follow this in curved spacetime
- Inertial navigation: Accelerometers measure deviation from inertial motion

### Free-Body Diagram Method (Systematic Approach)
1. **Choose the object** to analyze (isolate the system)
2. **Draw all forces** acting on it (gravity, normal, friction, applied)
3. **Set up coordinate system** (align one axis with acceleration)
4. **Apply Newton's 2nd law** in component form

$$ \sum F_x = ma_x, \quad \sum F_y = ma_y $$

### Worked Example: Block on Inclined Plane (with friction)
A block of mass $m$ on incline angle $\theta$ with coefficient of friction $\mu$:

**Free-body diagram:**

```
Normal N ↑
 [ m ] → mg sinθ (component down incline)
 mg cosθ ↓
 → friction f = μN opposing motion
```

**Equations:**

- Perpendicular: $N - mg\cos\theta = 0 \implies N = mg\cos\theta$
- Along incline: $mg\sin\theta - \mu N = ma$
- $a = g(\sin\theta - \mu\cos\theta)$

**Worked numeric example:** $m = 5\,\text{kg}$, $\theta = 30°$, $\mu = 0.2$:

$$a = 9.81(\sin 30° - 0.2\cos 30°) = 9.81(0.5 - 0.173) = 9.81 \times 0.327 = 3.21\,\text{m/s}^2$$

**Dimensional check:** $[a] = [g] = \text{m/s}^2$ ✓

---

## 2. Second Law (Force Law)

$$ \vec{F}_{\text{net}} = m\vec{a} = \frac{d\vec{p}}{dt} $$

Net force equals mass times acceleration (or rate of change of momentum).

### Component Form (Cartesian)

$$F_x = m\ddot{x}, \quad F_y = m\ddot{y}, \quad F_z = m\ddot{z}$$

### Important Force Types

| Force | Expression | Origin |
|-------|-----------|--------|
| Gravity | $\vec{F} = -GMm/r^2\,\hat{r}$ | Mass attraction |
| Spring | $\vec{F} = -kx\,\hat{x}$ | Elastic restoring |
| Friction (kinetic) | $f_k = \mu_k N$ | Surface contact |
| Normal | $\vec{N} \perp$ surface | Contact constraint |
| Drag | $\vec{F}_D = -b\vec{v}$ or $-\frac{1}{2}C_D\rho A v^2\hat{v}$ | Fluid resistance |
| Centripetal | $\vec{F}_c = -mv^2/r\,\hat{r}$ | Circular motion |

### Geodesy Connection

- **Satellite orbital mechanics:** $\vec{F}_{\text{gravity}} = m\vec{a}_{\text{centripetal}}$
- **GNSS signal propagation:** Forces on satellites perturb orbits
- **Earth rotation:** Centrifugal force contributes to Earth's ellipsoidal shape
- **Atmospheric drag on LEO satellites:** Non-gravitational force perturbation

**Vector Form for Geodesy (3D):**

$$m \begin{bmatrix} \ddot{x} \\ \ddot{y} \\ \ddot{z} \end{bmatrix} = \vec{F}_{\text{gravity}} + \vec{F}_{\text{drag}} + \vec{F}_{\text{solar rad}} + \vec{F}_{\text{thrust}}$$

---

## 3. Third Law (Action-Reaction)

$$ \vec{F}_{12} = -\vec{F}_{21} $$

For every action, there's an equal and opposite reaction.

### Key Points

- Forces always come in pairs
- Acts on different objects (not on the same object!)
- Same magnitude, opposite direction
- Always simultaneous

### Geodesy Connection

- **Tidal forces:** Earth-Moon-Sun gravitational interactions
- **GRACE satellite pair:** Mutual gravitational attraction measures mass changes
- **Satellite-to-satellite tracking:** K-band ranging between GRACE-FO

---

## 4. Constraints and Generalized Forces

### Types of Constraints

| Constraint Type | Example | Mathematical Form |
|----------------|---------|-------------------|
| Holonomic | Bead on wire | $f(q_1, q_2, \dots, t) = 0$ |
| Non-holonomic | Rolling without slipping | $dx = R\,d\theta$ (differential) |
| Rheonomic | Moving support | $f(q, t) = 0$ (time-dependent) |
| Scleronomic | Fixed support | $f(q) = 0$ (time-independent) |

### Lagrangian Framework (Preview)

For constrained systems, introduce generalized coordinates $q_i$:

$$L = T - V$$

The Euler-Lagrange equation gives the equations of motion:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0$$

This is equivalent to Newton's laws but handles constraints naturally.

**Example — Simple pendulum:** $L = \frac{1}{2}ml^2\dot{\theta}^2 - mgl(1-\cos\theta)$

$$\frac{d}{dt}(ml^2\dot{\theta}) + mgl\sin\theta = 0 \implies \ddot{\theta} + \frac{g}{l}\sin\theta = 0$$

---

## 5. Applications in Geodesy

### Satellite Orbit Determination

From Newton's 2nd law + Law of Universal Gravitation:

$$m\frac{d^2\vec{r}}{dt^2} = -\frac{GMm}{r^3}\vec{r} + \vec{F}_{\text{perturb}}$$

**Perturbation forces ($\vec{F}_{\text{perturb}}$):**

| Force | Magnitude | Effect |
|-------|-----------|--------|
| Earth oblateness ($J_2$) | $\sim 10^{-3}\,\text{m/s}^2$ | Dominant, secular drift |
| Atmospheric drag | $\sim 10^{-6}$–$10^{-8}\,\text{m/s}^2$ | LEO decay, semi-major axis |
| Solar radiation pressure | $\sim 10^{-7}\,\text{m/s}^2$ | GPS, Galileo eccentricity |
| Third-body (Moon/Sun) | $\sim 10^{-6}\,\text{m/s}^2$ | Long-period variations |
| Relativistic correction | $\sim 10^{-10}\,\text{m/s}^2$ | Clock + orbit, ppm level |

### Earth's Gravity Field (Spherical Harmonic Expansion)

From Newton's laws + potential theory:

$$U(\vec{r}) = \frac{GM}{r} \quad \text{(spherical)}$$

$$V(\vec{r}) = \frac{GM}{r} \left[ 1 - \sum_{n=2}^{\infty} \sum_{m=0}^{n} \left(\frac{R}{r}\right)^n P_{nm}(\sin\phi) (C_{nm}\cos m\lambda + S_{nm}\sin m\lambda) \right]$$

where $P_{nm}$ are associated Legendre polynomials, $C_{nm}$ and $S_{nm}$ are spherical harmonic coefficients from EGM2008.

### Worked Example: GPS Satellite Orbit

GPS satellite at altitude $h = 20{,}200\,\text{km}$:

1. **Orbital radius:** $r = R_E + h = 6{,}371 + 20{,}200 = 26{,}571\,\text{km}$
2. **Orbital velocity:** $v = \sqrt{GM/r} = \sqrt{3.986\times10^{14}/26{,}571{,}000} = 3{,}874\,\text{m/s}$
3. **Orbital period:** $T = 2\pi r/v = 2\pi \times 26{,}571{,}000/3{,}874 \approx 43{,}080\,\text{s} \approx 11.97\,\text{hours}$

### Inertial Navigation

$$\vec{a}_{\text{measured}} = \vec{a}_{\text{true}} - \vec{g} + \vec{a}_{\text{rotation}}$$

where $\vec{a}_{\text{rotation}}$ includes Coriolis and centrifugal effects.

**Example — Inertial navigation error growth:**

For a MEMS accelerometer with bias $b = 1\,\text{mg} = 0.00981\,\text{m/s}^2$:

Position error after $t = 3600\,\text{s}$: $\Delta x = \frac{1}{2}bt^2 = \frac{1}{2}(0.00981)(3600)^2 = 63{,}500\,\text{m} \approx 63.5\,\text{km}$

This shows why GNSS aiding is essential for long-duration inertial navigation.

---

## 6. Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\vec{F} = m\vec{a}$ | Newton's 2nd | Everything |
| $F = G\frac{m_1 m_2}{r^2}$ | Universal Gravitation | Orbits, gravity field |
| $\vec{F}_c = m\omega^2\vec{r}$ | Centrifugal force | Earth shape, rotating frames |
| $\vec{\tau} = \vec{r} \times \vec{F}$ | Torque | Gyroscopes, attitude |
| $\vec{L} = I\omega$ | Angular momentum | Earth rotation, satellite attitude |
| $\vec{J} = \int \vec{F}\,dt = \Delta\vec{p}$ | Impulse-momentum | Collisions, burns |
| $U = -\frac{GMm}{r}$ | Gravitational potential | Orbit energy |
| $v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$ | Escape velocity | Launch requirements |
| $\omega_{\text{circ}} = \sqrt{\frac{GM}{r^3}}$ | Circular orbit angular velocity | GPS, GLONASS orbit design |

---

## Worked Examples

### Example 1: Escape Velocity from Earth

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R_E}} = \sqrt{\frac{2 \times 3.986 \times 10^{14}}{6.371 \times 10^6}} = \sqrt{1.250 \times 10^8} \approx 11{,}180\,\text{m/s} \approx 11.2\,\text{km/s}$$

### Example 2: Geostationary Orbit Radius

$$r = \left(\frac{GM T^2}{4\pi^2}\right)^{1/3} = \left(\frac{3.986\times10^{14} \times (86400)^2}{4\pi^2}\right)^{1/3} \approx 42{,}164\,\text{km}$$

Altitude above Earth's surface: $h = r - R_E = 42{,}164 - 6{,}371 = 35{,}786\,\text{km}$ ✓

### Example 3: $J_2$ Perturbation on GPS Orbit

Rate of change of RAAN due to Earth oblateness ($J_2 = 1.0826 \times 10^{-3}$):

$$\dot{\Omega} = -\frac{3}{2} J_2 \frac{n R_E^2}{a^2(1-e^2)^2} \cos i$$

For GPS ($a = 26{,}571\,\text{km}$, $e \approx 0$, $i = 55°$):

$$\dot{\Omega} \approx -3.1°/\text{day}$$

This must be accounted for in precise orbit determination.

---

## Common Mistakes

1. **Confusing coordinate acceleration vs. proper acceleration** — accelerometers measure proper acceleration
2. **Forgetting centrifugal force in Earth-fixed frame** — it's part of "gravity" (plumb line direction)
3. **Using scalar instead of vector forms** — geodesy is 3D, always use vectors
4. **Ignoring frame of reference** — inertial vs. Earth-fixed vs. topocentric
5. **Applying action-reaction to the same object** — they always act on different bodies

---

## Study Problems

1. Derive circular orbit velocity: $v = \sqrt{GM/r}$
2. Compute GPS satellite altitude from orbital period (12 sidereal hours)
3. Calculate $J_2$ perturbation on GPS orbit over 1 day
4. Explain why Earth's equatorial bulge causes $J_2$ effect
5. A 5 kg block slides down a frictionless 30° incline. Find acceleration and time to slide 10 m.
6. Two objects attract gravitationally with force $F$. If the distance is doubled and one mass is tripled, what is the new force?

---

## References

1. **IERS Conventions (2010)** — IERS Technical Note No. 36. [https://hpiers.obspm.fr/iers/eop/eop.php](https://hpiers.obspm.fr/iers/eop/eop.php)
2. **OpenStax University Physics** — OpenStax. [https://openstax.org/details/books/university-physics](https://openstax.org/details/books/university-physics)
3. **MIT OpenCourseWare — 8.01 Classical Mechanics** — Walter Lewin. [https://ocw.mit.edu/courses/8-01-classical-mechanics-fall-1999/](https://ocw.mit.edu/courses/8-01-classical-mechanics-fall-1999/)
4. **ESA GNSS Bureau** — GNSS Orbit Determination. [https://www.esa.int/Applications/GNSS](https://www.esa.int/Applications/GNSS)
5. **NIMA/NGA Technical Report TR8350.2** — Department of Defense World Geodetic System 1984. [https://earth-info.nga.mil/](https://earth-info.nga.mil/)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
