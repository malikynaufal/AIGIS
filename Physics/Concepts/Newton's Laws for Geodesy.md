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

$$\sum \vec{F} = 0 \implies \vec{v} = \text{constant} $$An object at rest stays at rest; an object in motion stays in motion with constant velocity unless acted upon by a net external force.

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
:

$$\sum F_x = ma_x, \quad \sum F_y = ma_y$$

### Worked Example: Block on Inclined Plane (with friction)
A block of mass $m $on incline angle $\theta $with coefficient of friction $\mu$:

**Free-body diagram (text):**
```
Normal N ↑
 [ m ] → mg sinθ (component down incline)
 mg cosθ ↓
 → friction f = μN opposing motion
```

**Equations:**

- Perpendicular: $N - mg\cos\theta = 0 \implies N = mg\cos\theta$- Along incline:$mg\sin\theta - \mu N = ma$-$a = g(\sin\theta - \mu\cos\theta)$**Dimensional check:**$[a] = [g] = m/s^2$✓

---

## 2. Second Law (Force Law
)

$$\vec{F}_{\text{net}} = m\vec{a} = \frac{d\vec{p}}{dt} $$

Net force equals mass times acceleration (or rate of change of momentum).

### Component Form (Cartesian
)

$$F_x = m\ddot{x}, \quad F_y = m\ddot{y}, \quad F_z = m\ddot{z} $$

### Important Force Types
| Force | Expression | Origin |
|-------|-----------|--------|
| Gravity | $\vec{F} = -GMm/r^2\,\hat{r} $ | Mass attraction |
| Spring | $\vec{F} = -kx\,\hat{x} $ | Elastic restoring |
| Friction (kinetic) | $f_k = \mu_k N$ | Surface contact |
| Normal | $\vec{N} \perp $surface | Contact constraint |
| Drag | $\vec{F}_D = -b\vec{v} $or$-\frac{1}{2}C_D\rho A v^2\hat{v} $ | Fluid resistance |
| Centripetal | $\vec{F}_c = -mv^2/r\,\hat{r} $ | Circular motion |

### Geodesy Connection

- **Satellite orbital mechanics:**$\vec{F}_{\text{gravity}} = m\vec{a}_{\text{centripetal}} $- **GNSS signal propagation:** Forces on satellites perturb orbits

- **Earth rotation:** Centrifugal force contributes to Earth's ellipsoidal shape

- **Atmospheric drag on LEO satellites:** Non-gravitational force perturbation

**Vector Form for Geodesy (3D):*
*

$$m \begin{bmatrix} \ddot{x} \\ \ddot{y} \\ \ddot{z} \end{bmatrix} = \vec{F}_{\text{gravity}} + \vec{F}_{\text{drag}} + \vec{F}_{\text{solar rad}} + \vec{F}_{\text{thrust}} $$

---

## 3. Third Law (Action-Reaction
)

$$\vec{F}_{12} = -\vec{F}_{21} $$

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
| Non-holonomic | Rolling without slipping | $dx = R\,d	heta$(differential) |
| Rheonomic | Moving support | $f(q, t) = 0$(time-dependent) |
| Scleronomic | Fixed support | $f(q) = 0$(time-independent) |

### Lagrangian Framework (Preview)
For constrained systems, introduce generalized coordinates $q_i$:

$$L = T - V\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0$$This is equivalent to Newton's laws but handles constraints naturally.

---

## 5. Applications in Geodesy

### Satellite Orbit Determination
From Newton's 2nd law + Law of Universal Gravitation:

$$m\frac{d^2\vec{r}}{dt^2} = -\frac{GMm}{r^3}\vec{r} + \vec{F}_{\text{perturb}} $$

**Perturbation forces ($\vec{F}_{\text{perturb}} $):**
| Force | Magnitude | Effect |
|-------|-----------|--------|
| Earth oblateness ($J_2$) | ~$10^{-3} $ m/s² | Dominant, secular drift |
| Atmospheric drag | ~$10^{-6} $–$10^{-8} $ m/s² | LEO decay, semi-major axis |
| Solar radiation pressure | ~$10^{-7} $ m/s² | GPS, Galileo eccentricity |
| Third-body (Moon/Sun) | ~$10^{-6} $ m/s² | Long-period variations |
| Relativistic correction | ~$10^{-10} $m/s² | Clock + orbit, ppm level |

### Earth's Gravity Field
From Newton's laws + potential theory:

$$U(\vec{r}) = \frac{GM}{r} \quad \text{(spherical)}V(\vec{r}) = \frac{GM}{r} \left[ 1 - \sum_{n=2}^{\infty} \sum_{m=0}^{n} \left(\frac{R}{r}\right)^n P_{nm}(\sin\phi) (C_{nm}\cos m\lambda + S_{nm}\sin m\lambda) \right
]

$$### Inertial Navigation$$

\vec{a}_{\text{measured}} = \vec{a}_{\text{true}} - \vec{g} + \vec{a}_{\text{rotation}} $$---

## 6. Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\vec{F} = m\vec{a} $ | Newton's 2nd | Everything |
| $F = G\frac{m_1m_2}{r^2} $ | Universal Gravitation | Orbits, gravity field |
| $\vec{F}_c = m\omega^2\vec{r} $ | Centrifugal force | Earth shape, rotating frames |
| $\vec{\tau} = \vec{r} \times \vec{F} $ | Torque | Gyroscopes, attitude |
| $L = I\omega$ | Angular momentum | Earth rotation, satellite attitude |
| $\vec{J} = \int \vec{F}\,dt = \Delta\vec{p} $ | Impulse-momentum | Collisions, burns |

---

## 7. Common Mistakes
1. **Confusing coordinate acceleration vs. proper acceleration** — accelerometers measure proper accel
2. **Forgetting centrifugal force in Earth-fixed frame** — it's part of "gravity" (plumb line direction)
3. **Using scalar instead of vector forms** — geodesy is 3D, always use vectors
4. **Ignoring frame of reference** — inertial vs. Earth-fixed vs. topocentric
5. **Applying action-reaction to the same object** — they always act on different bodies

---

## Study Problems
1. Derive circular orbit velocity:$v = \sqrt{GM/r} $2. Compute GPS satellite altitude from orbital period (12 sidereal hours)
3. Calculate $J_2 $perturbation on GPS orbit over 1 day
4. Explain why Earth's equatorial bulge causes $J_2 $effect
5. A 5 kg block slides down a frictionless 30° incline. Find acceleration and the time to slide 10 m.
6. Two objects attract gravitationally with force $F$. If the distance is doubled and one mass is tripled, what is the new force?

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
