---
tags: [aigis, concept, physics, relativity, lorentz]
created: 2026-07-27
updated: 2026-07-27
---

# Special Relativity

## Lorentz Transforms, 4‑Vectors, E = mc²

**Core Idea:** Einstein’s 1905 theory states that the laws of physics are the same in all inertial frames, and that the speed of light $c $ is constant. This forces time dilation and length contraction.

---

## 1. Two Postulates

**Postulate 1 (Relativity):** The laws of physics are identical in all inertial frames.

**Postulate 2 (Light Speed):** In any inertial frame, the speed of light in vacuum is $ c = 2.998	imes10^8 $ m/s, independent of the source.

---

## 2. Lorentz Transformations

### Coordinates Transformation ($ x, t 	o x', t'$) for Frame Moving at $ v $ along $ x $

$ $

x' = \gamma(x - vt)t' = \gamma\left(t - rac{vx}{c^2}
ight)\gamma = rac{1}{\sqrt{1 - v^2/c^2}
}

**### Inverse Transformation **

x = \gamma(x' + vt')t = \gamma\left(t' + rac{vx'}{c^2}
ight)

$$

### Worked Example: GPS Time Dilation (Special Relativity)
For a GPS satellite at orbital speed $ v = 3874 $ m/s:
1.$eta = v/c = 3874/3	imes10^8 = 1.29 	imes 10^{-5} $ 2.$ \gamma = 1/\sqrt{1-eta^2} pprox 1 + 8.3	imes 10^{-11} $ 3. Per day: $ \Delta t = v^2/(2c^2) 	imes T = -7.2\,\mu	ext{s} $ (satellite clock runs *slower*)

---

## 3. Consequences

### Time Dilation
A clock at rest in frame $ S' $ runs slow when viewed from $ S $:

$ $ \Delta t = \gamma \Delta t_0

$$

### Length Contraction
A rod at rest in $ S' $ with length $ L_0 $ appears shorter in $ S $:

$ $

L = rac{L_0}{\gamma
}

**### Velocity Addition **

u' = rac{u - v}{1 - uv/c^2
}

**### Mass–Energy Equivalence **

E = mc^2E^2 = (pc)^2 + (mc^2)^
2

**### Relativistic Momentum **

 \mathbf{p} = \gamma m \mathbf{v}

$ For a photon: $ E = pc $ (rest mass = 0).

### Doppler Shif
t

$ f_{	ext{obs}} = f_{	ext{source}} \sqrt{rac{1 + eta}{1 - eta}} \quad 	ext{(receiver and source receding)} $ $

---

## 4. Spacetime and 4‑Vectors

### Minkowski Metric

$$

ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2\eta_{\mu
u} = 	ext{diag}(-1, +1, +1, +1
)

**### 4‑Position **

x^\mu = (ct, x, y, z
)

**### 4‑Velocity **

u^\mu = \gamma(c, \mathbf{v})u^\mu u_\mu = -c^
2

**### 4‑Momentum **

p^\mu = (E/c, \gamma m\mathbf{v}
)

**### 4‑Gradient **

\partial_\mu = \left(rac{\partial}{\partial ct},
abla
ight)

$ $

### Lorentz Invariants (in Minkowski metric)

- Interval $ s^2 $: same in all frames

- Mass squared: $ p^\mu p_\mu = -m^2 c^2 $- Energy‑momentum relation: $ E^2 - (pc)^2 = (mc^2)^2 $---

## 5. Spacetime Diagram
Plot $ x $ vs. $ ct $:

- World‑line: trajectory of a particle through spacetime

- Light cone at 45° defines causal regions

- Future = interior of forward light cone

- Past = interior of backward light cone

- Elsewhere = causally disconnected

---

## 6. Common Pitfalls
1. **Symmetry of time dilation**: Both observers see *the other* clock as slower. The resolution is *not* a true paradox: observers disagree on simultaneity.
2. **Twin paradox**: Resolved because traveling twin accelerates and changes frames; returning twin is younger.
3. **Forgetting γ**: At everyday speeds ($eta < 10^{-4} $), γ − 1 ≈ β²/2. Always expand for small β.

---

## 7. Worked Examples

### (a) Muon Decay
Muons produced at 60 km altitude travel at $ v = 0.998c $ ($ \gamma = 15.8 $). Lifetime in lab frame: $ au = 2.2\,\mu	ext{s} $.

- Lab distance before decay: $ L = v	au = 0.998c 	imes 2.2\,\mu	ext{s} = 660 $ m (not enough!).

- Proper lifetime: $ au_0 = 	au/\gamma = 0.14\,\mu	ext{s} $.

- Distance in muon frame: $ L_0 = L/\gamma = 60/15.8 = 3.8 $ km. Better still: in lab frame, muons live $ \gamma 	au = 35\,\mu	ext{s} $, covering 10.4 km — explaining observation.

### (b) Relativistic Kinetic Energy
For electron at $ v = 0.9c $:

- $ K = (\gamma - 1)mc^2 = (2.29 - 1) 	imes 0.511\,	ext{MeV} = 0.66\,	ext{MeV} $- Classical: $ K = rac{1}{2}mv^2 $ would give $ 0.5	imes0.511	imes0.81 = 0.21\,	ext{MeV} $ (off by factor 3).

---

## 8. Applications to Geodesy

| Effect | Magnitude | Application |
|--------|-----------|-------------|
| Special time dilation (GPS) | −7.2 µs/day | Must be corrected |
| Gravitational redshift | +45.7 µs/day (GR) | Must be corrected |
| Sagnac effect | up to ±133 ns | Earth rotation |
| Relativistic clock correction | overall | GNSS ephemeris generation |

**Dimensional check:**$ [E = mc^2] = 	ext{kg}\cdot(	ext{m/s})^2 = 	ext{J} $✓

---

## 9. Key Equations Summary

| Equation | Name | Use |
|----------|------|-----|
| $ x' = \gamma(x-vt) $, $ t' = \gamma(t - vx/c^2) $ | Lorentz transform | Frame transformation |
| $ \Delta t = \gamma\Delta t_0 $ | Time dilation | Moving clocks |
| $ L = L_0/\gamma $ | Length contraction | Moving rods |
| $ E = \gamma mc^2 $ | Relativistic energy | Particle energy |
| $ E^2 = (pc)^2 + (mc^2)^2 $ | Energy‑momentum | Massive or massless particles |
| $ u' = (u-v)/(1 - uv/c^2) $ | Velocity addition | Composition of velocities |
| $ p^\mu = (E/c, \gamma m\mathbf{v}) $ | 4‑momentum | Lorentz covariant |

---

## Study Problems
1. A spaceship passes Earth at $ v = 0.6c $. Earth’s clock advances 10 s. How much proper time elapses on the ship?
2. Derive the formula for relativistic kinetic energy from $ K = \int F\,ds $.
3. Show that the dispersion relation $ E^2 = (pc)^2 + m^2c^4 $ is Lorentz invariant.
4. Compute the time dilation correction per day for a GPS satellite.
5. Two photons are emitted in opposite directions from a star. Find the relative speed in any frame.

---

## References

- Einstein (1905) "On the Electrodynamics of Moving Bodies"

- Griffiths, "Introduction to Electrodynamics" (relativistic chapters)

- Taylor & Wheeler, "Spacetime Physics" (2nd ed.)

- MIT OCW 8.033: Relativity

- Feynman Lectures Vol. I (Ch. 15-21)

- OpenStax University Physics Vol. 3 (Ch. 5)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
