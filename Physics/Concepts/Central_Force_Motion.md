---
tags: [physics, concept, aigis]
aliases: [Central Force Motion]
created: 2026-07-27
---

# Central Force Motion (Gerak Gaya Sentral)

> Kepler problem, effective potential, orbits, Bertrand's theorem, scattering

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Central force motion describes particle trajectories under forces directed toward (or away from) a fixed point — the foundation of orbital mechanics, planetary motion, and satellite dynamics.

> **Geodesy Connection:** Satellite orbits under Earth's gravity; the two-body problem in GNSS orbit determination; perturbation theory for precise orbit prediction.

---

## 🧮 Key Equations

### Central Force

A central force depends only on distance $r$ and is directed along the radial unit vector:

$$
\mathbf{F} = f(r)\hat{\mathbf{r}}
$$

Since $\nabla \times \mathbf{F} = 0$ for any radial force, central forces are conservative with potential energy $V(r)$ such that $f(r) = -dV/dr$.

### Conserved Quantities

For central force motion, three quantities are conserved:

**Energy** (Energi):

$$
E = \frac{1}{2}m\dot{r}^2 + \frac{L^2}{2mr^2} + V(r) = \text{const}
$$

**Angular momentum** (Momentum sudut):

$$
L = mr^2\dot{\phi} = \text{const}
$$

**Orbital plane:** The motion is confined to a plane since $\mathbf{L}$ is constant.

### Effective Potential (Potensial Efektif)

The radial motion can be described using an effective potential:

$$
V_{\text{eff}}(r) = V(r) + \frac{L^2}{2mr^2}
$$

The effective potential combines the true potential with the centrifugal barrier $\frac{L^2}{2mr^2}$. Stable circular orbits occur at the minimum of $V_{\text{eff}}$:

$$
\left.\frac{dV_{\text{eff}}}{dr}\right|_{r_0} = 0 \quad \text{and} \quad \left.\frac{d^2V_{\text{eff}}}{dr^2}\right|_{r_0} > 0
$$

### Orbit Equation (Persamaan Orbit)

Using the substitution $u = 1/r$ and $\phi$ as the independent variable, the radial equation transforms to the Binet equation:

$$
\frac{d^2u}{d\phi^2} + u = -\frac{m}{L^2 u^2} f(1/u)
$$

### Kepler Orbit (Orbit Kepler)

For an inverse-square force $f(r) = -k/r^2$ (gravity or Coulomb), the orbit is a conic section:

$$
r = \frac{p}{1 + e\cos(\phi - \phi_0)}
$$

where:

$$
p = \frac{L^2}{mk}, \quad e = \sqrt{1 + \frac{2EL^2}{mk^2}}
$$

The eccentricity $e$ determines the orbit type:

| $e$ value | Orbit type | Description |
|-----------|-----------|-------------|
| $e = 0$ | Circle | Perfectly circular |
| $0 < e < 1$ | Ellipse | Bound orbit (行星 orbits) |
| $e = 1$ | Parabola | Escape trajectory |
| $e > 1$ | Hyperbola | Unbound scattering |

### Kepler's Laws (Hukum Kepler)

| Law | Statement | Mathematical Form |
|-----|-----------|-------------------|
| 1st — Ellipses | Orbits are conic sections with the central body at one focus | $r = \frac{a(1-e^2)}{1+e\cos\phi}$ |
| 2nd — Equal areas | Radius vector sweeps equal areas in equal times | $\frac{dA}{dt} = \frac{L}{2m} = \text{const}$ |
| 3rd — Harmonic law | Period squared is proportional to semi-major axis cubed | $T^2 = \frac{4\pi^2}{GM}a^3$ |

### Energy in Kepler Orbits

The total energy depends only on the semi-major axis $a$:

$$
E = -\frac{k}{2a} = -\frac{GMm}{2a}
$$

The period is:

$$
T = 2\pi\sqrt{\frac{a^3}{GM}}
$$

### Virial Theorem (Teorema Virial)

For bound orbits under power-law potentials $V(r) = \alpha r^n$:

$$
2\langle T \rangle = n\langle V \rangle
$$

For gravity ($n = -1$):

$$
2\langle T \rangle = -\langle V \rangle \quad \Longrightarrow \quad E = -\langle T \rangle
$$

The total energy equals minus the average kinetic energy — a striking result.

### Bertrand's Theorem

Only two types of central force potentials produce closed orbits for all bound trajectories:

$$
V(r) = -\frac{k}{r} \quad \text{(Kepler/Coulomb)} \qquad \text{and} \qquad V(r) = \frac{1}{2}kr^2 \quad \text{(Harmonic oscillator)}
$$

### Scattering Cross Section

For a repulsive $1/r$ potential (Rutherford scattering):

$$
\frac{d\sigma}{d\Omega} = \left(\frac{k}{4E}\right)^2 \frac{1}{\sin^4(\theta/2)}
$$

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** A satellite orbiting Earth is like a ball rolling in a bowl — the effective potential creates a valley where the orbit sits. Too little energy, and it spirals in; too much, and it escapes.

> **Key insight:** The conservation of angular momentum is what prevents matter from falling into the center — the centrifugal barrier $L^2/(2mr^2)$ creates a wall at small $r$. Without angular momentum, everything would collapse.

> **Geodesy intuition:** GNSS satellites follow near-circular Kepler orbits ($e \approx 0.02$). Perturbation theory treats Earth's oblateness ($J_2$), lunisolar gravity, and solar radiation pressure as small corrections to the ideal Keplerian motion.

---

## 🧪 Worked Examples

### Example 1: Geostationary Orbit Radius

**Problem:** Find the radius of a geostationary orbit where the orbital period matches Earth's rotation period (86,164 s sidereal day).

**Solution:**

Using Kepler's third law:

$$
T^2 = \frac{4\pi^2}{GM}a^3 \quad \Longrightarrow \quad a^3 = \frac{GMT^2}{4\pi^2}
$$

With $GM = 3.986 \times 10^{14}$ m³/s² and $T = 86{,}164$ s:

$$
a^3 = \frac{3.986 \times 10^{14} \times (86164)^2}{4\pi^2} = \frac{3.986 \times 10^{14} \times 7.424 \times 10^{9}}{39.478}
$$

$$
a^3 = \frac{2.959 \times 10^{24}}{39.478} = 7.495 \times 10^{22} \text{ m}^3
$$

$$
a = (7.495 \times 10^{22})^{1/3} = 4.216 \times 10^{7} \text{ m} \approx 42{,}164 \text{ km}
$$

Altitude above Earth's surface: $h = a - R_\oplus = 42{,}164 - 6{,}371 = 35{,}793$ km.

---

### Example 2: Escape Velocity Using Energy Conservation

**Problem:** Find the escape velocity from Earth's surface using the effective potential / energy method.

**Solution:**

At the surface, the total energy is:

$$
E = \frac{1}{2}mv_{\text{esc}}^2 - \frac{GMm}{R_\oplus}
$$

For escape, the particle reaches $r \to \infty$ with zero kinetic energy: $E = 0$.

Setting $E = 0$:

$$
\frac{1}{2}mv_{\text{esc}}^2 = \frac{GMm}{R_\oplus}
$$

$$
v_{\text{esc}} = \sqrt{\frac{2GM}{R_\oplus}} = \sqrt{\frac{2 \times 3.986 \times 10^{14}}{6.371 \times 10^6}} = \sqrt{1.251 \times 10^{8}}
$$

$$
v_{\text{esc}} = 11{,}186 \text{ m/s} \approx 11.2 \text{ km/s}
$$

This is $\sqrt{2}$ times the orbital velocity at the surface, consistent with the energy analysis of Kepler orbits.

---

## 📚 References

| Source | Topic | URL |
|--------|-------|-----|
| MIT OCW 8.01 (Classical Mechanics) | Central forces, Kepler orbits, orbital mechanics | https://ocw.mit.edu/courses/8-01-classical-mechanics-fall-2016/ |
| OpenStax University Physics Vol. 1 | Newton's gravitation, orbital motion | https://openstax.org/books/university-physics-volume-1/pages/13-3-satellite-orbits-and-energy |
| HyperPhysics — Kepler's Laws | Kepler orbits, effective potential | http://hyperphysics.phy-astr.gsu.edu/hbase/mechanics/kepler.html |
| Goldstein, Classical Mechanics | Ch. 3: Central forces, Kepler problem | https://sites.psu.edu/johnsonteaching/files/2021/07/Goldstein-Classical-Mechanics-3rd-Edition.pdf |
| IERS Conventions | Earth rotation, precession models | https://iers.org/IERS/EN/Publications/Conventions/conventions.html |

---

## 🔗 Links

- **Related:** [[Newtonian_Mechanics]] · [[Orbital_Mechanics]]
- **Geodesy:** [[Gravitational_Potential_Theory]] · [[Orbital_Mechanics]]
- **Study Pack:** [[_Study Packs/]]

*Created by AIGIS Physics Specialist · Part of the AIGIS Knowledge Machine*
*Last updated: 2026-07-27*
