---
tags: [aigis, concept, physics, kinematics, dynamics, central-force]
created: 2026-07-27
updated: 2026-07-27
---

# Kinematics \u0026 Dynamics

## Vectors, Motion in 2D/3D, Central Force Motion

**Core Idea:** Kinematics describes motion without forces; dynamics connects motion to forces via Newton's laws. Central force motion (gravity, electrostatics) produces conic section orbits.

---

## 1. Kinematics in 2D and 3D

### Position, Velocity, Acceleration

$$ \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}\vec{v}(t) = \frac{d\vec{r}}{dt} = \dot{x}\hat{i} + \dot{y}\hat{j} + \dot{z}\hat{k}\vec{a}(t) = \frac{d\vec{v}}{dt} = \ddot{x}\hat{i} + \ddot{y}\hat{j} + \ddot{z}\hat{k
}

**### Uniform Acceleration (2D Projectile)

** x(t) = v_0\cos\theta \cdot ty(t) = v_0\sin\theta \cdot t - \frac{1}{2}gt^2 $$ $

$

**Range** (level ground): $R = \frac{v_0^2 \sin 2\theta}{g}$**Maximum height**: $H = \frac{v_0^2 \sin^2\theta}{2g}$### Relative Velocit
y

$$ \vec{v}_{AC} = \vec{v}_{AB} + \vec{v}_{BC} $$

---

## 2. Newtonian Dynamics in Vector Form

### Newton's Second La
w

$$ \vec{F}_{\text{net}} = m\vec{a} = m\frac{d\vec{v}}{dt} $$

### Work-Energy Theore
m

$W = \int \vec{F}\cdot d\vec{r} = \Delta K = \frac{1}{2}m(v_f^2 - v_i^2) $$

### Powe
r

$P = \frac{dW}{dt} = \vec{F}\cdot\vec{v} $$

### Impulse-Momentu
m

$$ \vec{J} = \int \vec{F}\,dt = \Delta\vec{p} = m\vec{v}_f - m\vec{v}_i

$$

### Conservation of Angular Momentum
If$ \vec{\tau}_{\text{ext}} = 0$, then:

$$ \vec{L} = \vec{r}\times\vec{p} = \text{constant} $$

---

## 3. Central Force Motion

### Definitio
n

$$ \vec{F} = F(r)\hat{r} $$ A force directed along the line joining two particles.

### Key Properties
1. **Angular momentum is conserved** (torque is zero)
2. **Motion is confined to a plane** (Laplace-Runge-Lenz vector lies in plane)
3. **Area law** (Kepler's second law): $ \frac{dA}{dt} = \frac{L}{2m} = \text{const} $### Effective Potentia
l

$U_{\text{eff}}(r) = U(r) + \frac{L^2}{2mr^2}$Radial equation $$ m\ddot{r} = -\frac{dU_{\text{eff}}}{dr} $$

### Orbit Equatio
n

$$ r(\theta) = \frac{p}{1 + e\cos\theta} $$

where:
- $p = L^2/(mk|\alpha|)$(semi-latus rectum for inverse-square law)
- $e = \sqrt{1 + 2EL^2/(mk^2)}$(eccentricity)
- $k = |F_0|/r^2 = GMm$(gravitational)

### Classification by Energy
| $e$ | Orbit Type |
|-----|-----------|
| $e = 0$ | Circle |
| $0 < e < 1$ | Ellipse (bound) |
| $e = 1$ | Parabola (marginally bound) |
| $e > 1$ | Hyperbola (unbound) |

### Energy and Period (Elliptical Orbit
)

$E = -\frac{mk^2}{2L^2} \cdot p = -\frac{k}{2a} $$ **Period** (Kepler's Third Law)

$$ T^2 = \frac{4\pi^2 a^3}{GM} $$

where $a$ = semi-major axis.

---

## 4. Gravitational Orbits (Kepler Problem)

### First Law
Planets orbit in ellipses with the Sun at one focus.

### Second Law (Equal Areas
)

$$ \frac{dA}{dt} = \frac{L}{2m} = \text{constant} $$

### Third La
w

$$ T^2 = \frac{4\pi^2}{GM}a^3 $$

### Worked Example: Earth's Orbit
Semi-major axis $a = 1.496\times10^{11}$m, $M_\odot = 1.989\times10^{30} $kg
.

$T = 2\pi\sqrt{\frac{a^3}{GM}} = 2\pi\sqrt{\frac{(1.496\times10^{11})^3}{6.674\times10^{-11}\times1.989\times10^{30}}} = 3.156\times10^7 \text{ s} = 365.3 \text{ days} $$

**Dimensional check:**$[T] = \sqrt{\frac{m^3}{(m^3/kg/s^2)(kg)}} = \sqrt{s^2} = s$✓

---

## 5. Reference Frames and Non-Inertial Forces

### Fictitious Forces (in accelerating frame
)

$$ \vec{F}_{\text{eff}} = \vec{F}_{\text{real}} + \vec{F}_{\text{Coriolis}} + \vec{F}_{\text{centrifugal}} + \vec{F}_{\text{Euler}} $$

| Force | Expression | Example |
|-------|-----------|---------|
| Centrifugal | $-m\vec{\omega}\times(\vec{\omega}\times\vec{r}) $ | Rotating platform |
| Coriolis | $-2m\vec{\omega}\times\vec{v} $ | Weather systems, Foucault pendulum |
| Euler | $-m\dot{\vec{\omega}}\times\vec{r} $ | Starting/stopping rotation |

### Foucault Pendulum
Precession rate: $ \Omega = \omega\sin\phi$(where $\phi$ = latitude)

---

## 6. Key Equations Summary

| Formula | Name | Use |
|---------|------|-----|
| $ \vec{F} = m\vec{a} $ | Newton's 2nd Law | Dynamics |
| $ \vec{L} = \vec{r}\times\vec{p} $ | Angular momentum | Central forces |
| $U_{\text{eff}} = U(r) + L^2/(2mr^2)$ | Effective potential | Orbit analysis |
| $r = p/(1+e\cos\theta)$ | Orbit equation | Conic section orbits |
| $T^2 = 4\pi^2 a^3/(GM)$ | Kepler's 3rd Law | Orbital period |
| $E = -k/(2a)$ | Virial theorem | Orbital energy |
| $R = v_0^2\sin 2\theta/g$ | Range | Projectile motion |

---

## Study Problems
1. A projectile is launched at 50 m/s at 30° above horizontal. Find range, max height, and time of flight (g = 9.81 m/s²).
2. Derive the orbit equation $r(\theta) = p/(1+e\cos\theta) $from the radial equation for gravity.
3. Calculate the escape velocity from Earth's surface using energy conservation.
4. For a geostationary satellite, find the orbital radius and verify $T = 24 $hours.
5. Show that the period of a satellite in low Earth orbit is approximately 90 minutes using $T^2 = 4\pi^2 r^3/(GM)$.

---

## References

- Taylor, "Classical Mechanics" (Ch. 8-9)

- Goldstein, "Classical Mechanics" (Ch. 3)

- Morin, "Introduction to Classical Mechanics" (Ch. 8)

- Feynman Lectures Vol. I (Ch. 8-10)

- OpenStax University Physics Vol. 1 (Ch. 4, 13)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
