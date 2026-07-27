---
tags: [aigis, concept, physics, mechanics, newtonian, forces, motion]
created: 2026-07-27
updated: 2026-07-27
---

# Newtonian Mechanics

## For Geodesy & Geophysics Applications

**Core Idea:** Newton's three laws of motion form the foundation of classical mechanics, describing how forces produce motion. In geodesy, Newtonian mechanics governs satellite dynamics, Earth's rotation, and geodynamic processes (tides, post-glacial rebound, plate tectonics).

---

## Fundamental Concepts

### Newton's Three Laws

| Law | Statement | Mathematical Form |
|-----|-----------|-------------------|
| **I (Inertia)** | A body remains at rest or in uniform motion unless acted upon by a net force | $\sum \mathbf{F} = 0 \implies \mathbf{v} = \text{const} $ |
| **II (F=ma)** | Net force equals mass times acceleration | $\sum \mathbf{F} = m\mathbf{a} = m\frac{d\mathbf{v}}{dt} $ |
| **III (Action-Reaction)** | For every action, there is an equal and opposite reaction | $\mathbf{F}_{12} = -\mathbf{F}_{21} $ |

### Kinematics in ℝ³

| Quantity | Symbol | Definition | Units |
|----------|--------|------------|-------|
| Position | $\mathbf{r} $ | Displacement vector | m |
| Velocity | $\mathbf{v} = \dot{\mathbf{r}} $ | Time derivative of position | m/s |
| Acceleration | $\mathbf{a} = \dot{\mathbf{v}} = \ddot{\mathbf{r}} $ | Time derivative of velocity | m/s² |

**Equations of motion (constant acceleration):**

$$\mathbf{v} = \mathbf{v}_0 + \mathbf{a}t\mathbf{r} = \mathbf{r}_0 + \mathbf{v}_0 t + \frac{1}{2}\mathbf{a}t^2||\mathbf{v}||^2 = ||\mathbf{v}_0||^2 + 2\mathbf{a} \cdot (\mathbf{r} - \mathbf{r}_0
)

$$### Newton's Gravitational Law$$

\mathbf{F}_{12} = -G\frac{m_1 m_2}{r^2}\hat{\mathbf{r}}_{12} $$ | Parameter | Symbol | Value |
|-----------|--------|-------|
| Gravitational constant | $G$ | $6.67430 \times 10^{-11}\ \text{m}^3\text{kg}^{-1}\text{s}^{-2} $ |
| Earth mass | $M_\oplus$ | $5.972 \times 10^{24}\ \text{kg} $ |
| Earth mean radius | $R_\oplus$ | $6371.0\ \text{km} $ |
| Standard gravity | $g$ | $9.80665\ \text{m/s}^2$ |

### Work, Energy, Power

| Quantity | Formula | Units |
|----------|---------|-------|
| **Work** | $W = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} $ | J (joule) |
| **Kinetic energy** | $K = \frac{1}{2}mv^2$ | J |
| **Potential energy** | $U = -\int \mathbf{F} \cdot d\mathbf{r} $ | J |
| **Conservation** | $K + U = E = \text{const} $ | (isolated system) |
| **Power** | $P = \frac{dW}{dt} = \mathbf{F} \cdot \mathbf{v} $ | W (watt) |

### Momentum

| Quantity | Formula | Units |
|----------|---------|-------|
| Linear momentum | $\mathbf{p} = m\mathbf{v} $ | kg·m/s |
| Impulse | $\mathbf{J} = \int \mathbf{F}\,dt = \Delta\mathbf{p} $ | kg·m/s |
| Angular momentum | $\mathbf{L} = \mathbf{r} \times \mathbf{p} $ | kg·m²/s |
| Torque | $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} $ | N·m |

### Central Force Motion

For $\mathbf{F} = f(r)\hat{\mathbf{r}} $(e.g., gravity)
:

$$\mathbf{L} = \mathbf{r} \times m\mathbf{v} = \text{const} $$

This gives **Kepler's Second Law**: Equal areas swept in equal times.

---

## In Geodesy & Geophysics Context

### Gravitational Potential

For a point mass
:

$$U(r) = -\frac{GM}{r} $$

For a extended body (Earth), expand in spherical harmonics
:

$$U(r,\theta,\lambda) = \frac{GM}{r}\left[1 + \sum_{n=2}^\infty \left(\frac{a}{r}\right)^n J_n P_n(\cos\theta) + \dots\right]$$

-$J_2 \approx 1.0826 \times 10^{-3} $(Earth's oblateness)
-$J_2 $causes **precession** of the equinoxes (~50"/year)
-$J_2 $causes **nodal regression** of satellite orbits

### Earth Tides (Luni-Solar)

The tidal potential at Earth's surface
:

$$U_T = \frac{GM_s}{D}\left(\frac{r}{D}\right)^2 P_2(\cos Z_s) + \frac{GM_m}{d}\left(\frac{r}{d}\right)^2 P_2(\cos Z_m)$$

-$M_s$= Sun mass,$M_m$= Moon mass
-$D$, $d$= Sun/Earth and Moon/Earth distances
-$Z_s$, $Z_m$= zenith angles

This drives:

- Ocean tides (~0.3–0.5 m)

- Solid Earth tides (~0.3 m)

- Polar motion excitation

### Satellite Orbital Mechanics

**Kepler's Equation:*
*

$$M = E - e\sin E$$

where:
-$M$= mean anomaly (time-scaled)
-$E$= eccentric anomaly (geometric)
-$e$= orbital eccentricity

From $E$, compute true anomaly $\nu$:

$$\tan\frac{\nu}{2} = \sqrt{\frac{1+e}{1-e}}\tan\frac{E}{2} $$### Earth Rotation

The Euler equations for torque-free rigid body rotation:

$$I_1\dot{\omega}_1 + (I_3 - I_2)\omega_2\omega_3 = 0I_2\dot{\omega}_2 + (I_1 - I_3)\omega_3\omega_1 = 0I_3\dot{\omega}_3 + (I_2 - I_1)\omega_1\omega_2 = 0$$Earth's dynamic flattening $H = (C-A)/C \approx 1/305 $drives **free core nutation** (~433-day period).

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $\sum \mathbf{F} = m\mathbf{a} $ | Newton's 2nd law | Dynamics |
| $\mathbf{F} = -G\frac{Mm}{r^2}\hat{\mathbf{r}} $ | Gravitation | Gravity field |
| $W = \int \mathbf{F} \cdot d\mathbf{r} $ | Work | Energy |
| $K + U = E$ | Energy conservation | Orbit stability |
| $\mathbf{L} = \mathbf{r} \times m\mathbf{v} $ | Angular momentum | Central forces |
| $M = E - e\sin E$ | Kepler's equation | Orbit computation |
| $\mathbf{v}_{circ} = \sqrt{GM/r} $ | Circular orbit speed | GNSS satellites |

---

## Related Concepts

- [[Gravitational Potential]] — Potential field from Newtonian gravity

- [[Physical Geodesy]] — Gravity field of the real Earth

- [[GNSS]] — Orbital mechanics for satellite navigation

- [[Least Squares Adjustment]] — Dynamics + observations

- [[Relativistic Clock Correction]] — GR effects on satellite clocks

---

## Study Problems

1. **Recall:** A satellite in circular orbit at altitude $h = 20,200 $km (GPS orbit). Compute its orbital period, velocity, and the centripetal acceleration. Compare $a_c $to surface gravity $g$.
2. **Application:** The tidal potential has a $P_2(\cos Z) $dependence. Show that $P_2(x) = \frac{1}{2}(3x^2-1)$. Then compute the ratio of solar to lunar tidal forces at Earth (use $M_s/M_m = 2.7 \times 10^7$, $D/d \approx 390$).
3. **Derivation:** Derive the orbital energy $E = -\frac{GMm}{2a} $for an elliptical orbit. (Hint: start from vis-viva equation.)
4. **Real-world:** A geodetic GNSS station records position with sub-cm precision. The dominant signal is the diurnal/semidiurnal Earth tide. If the vertical tide amplitude is ~30 cm, estimate the maximum horizontal velocity from the tidal loading. (Hint: assume sinusoidal displacement.)

---

## Common Mistakes

1. **Confusing mass and weight:**$W = mg $on Earth's surface, but weight changes with $g$(altitude, latitude, local geology).
2. **Forgetting vector direction:** Force and acceleration are vectors; magnitude alone isn't enough.
3. **Using $F = mv $instead of $F = ma$:** Force equals mass times acceleration, not velocity.
4. **Ignoring non-inertial frames:** Coriolis and centrifugal forces appear in rotating Earth frame.
5. **Mixing up energy and momentum:** Energy is scalar, momentum is vector; both are conserved but in different ways.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*