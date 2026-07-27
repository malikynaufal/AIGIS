---
code: FKD211101
name: Fisika Dasar I — Classical Mechanics
SKS: 3
semester: 1
department: Fisika
tags: [physics, mechanics, kinematics, newtons-laws, classical-mechanics]
created: 2026-07-27
---

# FKD211101 — Fisika Dasar I: Classical Mechanics

## Course Overview

This foundational course introduces the principles of classical mechanics — the study of motion, forces, and energy. Students develop problem-solving skills using vector analysis and calculus-based methods, building the physical intuition essential for all advanced physics courses in the UGM curriculum.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** None
**Co-requisites:** Kalkulus I

---

## 📋 Topics & Outline

### Unit 1: Vectors and Kinematics (Weeks 1–4)

- Vector algebra: addition, dot product, cross product, unit vectors

- Position vectors and displacement in 1D, 2D, 3D

- Velocity and acceleration in Cartesian and polar coordinates

- **Equations of motion:** `r(t) = r₀ + v₀t + ½at²`

- Projectile motion: trajectory, range, maximum height

- Relative motion and reference frame transformations

### Unit 2: Newton's Laws of Motion (Weeks 5–8)

- **Newton's First Law:** Inertia and inertial reference frames

- **Newton's Second Law:** F = ma (vector form: **F** = m**a**)

- **Newton's Third Law:** Action-reaction pairs

- Types of forces: gravity, normal force, friction (static & kinetic), tension

- Free-body diagrams as the primary problem-solving tool

- Circular motion: centripetal acceleration `a_c = v²/r`

### Unit 3: Work, Energy, and Power (Weeks 9–12)

- Work done by a force: W = ∫ **F** · d**r**

- Kinetic energy: K = ½mv²

- Potential energy: gravitational U = mgh, elastic U = ½kx²

- **Work-Energy Theorem:** W_net = ΔK

- **Conservation of Mechanical Energy:** E = K + U = constant

- Power: P = dW/dt = **F** · **v**

### Unit 4: Momentum and Collisions (Weeks 13–16)

- Linear momentum: **p** = m**v**

- Impulse: **J** = ∫ **F** dt = Δ**p**

- **Conservation of Momentum:** Σ**p**_initial = Σ**p**_final

- Elastic, inelastic, and perfectly inelastic collisions

- Center of mass: **R**_cm = Σ m_i **r**_i / Σ m_i

- Rocket propulsion and variable mass systems

- Review and final examination

---

## 🔬 Key Equations

```
Kinematics: v = v₀ + at
 x = x₀ + v₀t + ½at²
 v² = v₀² + 2a(x - x₀)

Newton's 2nd: F_net = ma = m(dv/dt)

Work-Energy: W = ∫ F·dr = ΔKE

Conservation: KE_i + PE_i = KE_f + PE_f

Momentum: p = mv
 F = dp/dt

Circular: a_c = v²/r = ω²r
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Apply vector operations to solve multi-dimensional motion problems
2. Construct free-body diagrams and apply Newton's laws to complex force systems
3. Use energy methods (conservation laws) as alternatives to direct force analysis
4. Solve collision problems using conservation of momentum and energy
5. Analyze circular and projectile motion quantitatively
5. Connect classical mechanics concepts to geodetic applications (satellite orbits, gravity field)
7. Solve problems using energy methods and conservation principles
8. Apply impulse-momentum to collision and variable-mass problems

---

## 🌍 Connections to Geodesy

| Mechanics Concept | Geodesy Application |
|---|---|
| Newton's gravitational law | Earth's gravity field modeling |
| Projectile motion | Satellite orbit prediction |
| Conservation of energy | Potential theory (height systems) |
| Rotational motion | Earth rotation, precession, nutation |
| Reference frames | ECEF, ECI coordinate transformations |

---

## 📚 References

1. Halliday, D., Resnick, R., & Walker, J. (2013). *Fundamentals of Physics*, 10th ed. Wiley.
2. Serway, R.A. & Jewett, J.W. (2018). *Physics for Scientists and Engineers*, 10th ed. Cengage.
3. Tipler, P.A. & Mosca, G. (2007). *Physics for Scientists and Engineers*, 6th ed. W.H. Freeman.
4. Kleppner, D. & Kolenkow, R.J. (2013). *An Introduction to Mechanics*, 2nd ed. Cambridge.
5. OpenStax. *University Physics Vol. 1* — free at openstax.org

## 🌐 Online Resources

- MIT OCW 8.01 Classical Mechanics: https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/

- Khan Academy Physics — Forces: https://khanacademy.org/science/physics

- PhET Simulations — Forces and Motion: https://phet.colorado.edu/
5. HyperPhysics — Mechanics: http://hyperphysics.phy-astr.gsu.edu/hbase/mech.html

---

## 🧪 Worked Examples

### Example 1: Projectile with Air Resistance (Linear)
A ball is thrown at $v_0 = 20 $ m/s at $45° $ with linear drag force $ec{F}_D = -bv $.

**Equations of motion:**

$ $ m\ddot{x} = -b\dot{x}, \quad m\ddot{y} = -mg - b\dot{y} $$

For small drag ( $ b \ll mg/v_0 $), first-order correction:

$ $

x(t) = rac{mv_0\cos	heta}{b}(1 - e^{-bt/m})y(t) = rac{1}{b}\left(mv_0\sin	heta + rac{m^2g}{b}
ight)(1 - e^{-bt/m}) - rac{mgt}{b} $$

The range is reduced compared to vacuum and the trajectory is no longer symmetric.

### Example 2: Inelastic Collision on Frictionless Surface
Block A ( $ m_1 = 3 $kg, $ v_1 = 4 $m/s) collides with Block B ( $ m_2 = 1 $kg, $ v_2 = -2 $m/s). Perfectly inelastic (stick together).

**Conservation of momentum:**

$ $

m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f3(4) + 1(-2) = 4 v_f10 = 4 v_f \implies v_f = 2.5 	ext{ m/s
}

**Energy lost:**

 \Delta K = rac{1}{2}(3)(16) + rac{1}{2}(1)(4) - rac{1}{2}(4)(6.25) = 24 + 2 - 12.5 = 13.5 	ext{ J}

$$

### Example 3: Satellite Orbit from Newton's Second Law
A satellite orbits Earth at altitude $ h = 200 $km above the surface. Find the orbital speed.

**Given:** $ R_E = 6371 $km, $ GM = 3.986 	imes 10^{14} $m³/s², $ r = R_E + h = 6571 $km
.

$ v = \sqrt{rac{GM}{r}} = \sqrt{rac{3.986 	imes 10^{14}}{6.571 	imes 10^6}} = 7784 	ext{ m/s} pprox 7.8 	ext{ km/s} $ $$

**Period:** $ T = rac{2i r}{v} = rac{2i(6571)}{7784} = 5.32 	imes 10^3 	ext{ s} pprox 89 	ext{ min} $### Example 4: Work Done by Variable Force
A force $ F(x) = 3x^2 + 2x $acts on a 2 kg particle from $ x = 0 $to $ x = 3 $ m
.

$W = \int_0^3 (3x^2 + 2x)\,dx = [x^3 + x^2]_0^3 = 27 + 9 = 36 	ext{ J} $ By work-energy theorem: $W = \Delta K $, so $ v_f = \sqrt{2W/m} = \sqrt{72/2} = 6 $m/s (if $ v_i = 0$).

---

## 🔧 Dimensional Analysis Guide

| Quantity | SI Units | Common Units |
|----------|---------|--------------|
| Force | N = kg·m/s² | — |
| Energy | J = kg·m²/s² | eV, kcal |
| Power | W = J/s | hp |
| Momentum | kg·m/s | — |
| Angular momentum | kg·m²/s | J·s, ℏ |
| Moment of inertia | kg·m² | — |
| Torque | N·m | — |

**Quick check:** Always verify final answer has correct dimensions before computing numbers.

---

## 🌐 Additional Online Resources

- **PhET: Forces in 1D** — https://phet.colorado.edu/en/simulations/forces-1d

- **Walter Lewin MIT Lectures (8.01)** — https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/

- **HyperPhysics: Mechanics** — http://hyperphysics.phy-astr.gsu.edu/hbase/mech.html

- **Khan Academy: Momentum & Collisions** — https://www.khanacademy.org/science/physics/linear-momentum

- **OpenStax University Physics Vol. 1** — https://openstax.org/details/books/university-physics-volume-1

- **Feynman Lectures Vol. 1 (Ch. 4-18)** — https://www.feynmanlectures.caltech.edu/I_toc.html

