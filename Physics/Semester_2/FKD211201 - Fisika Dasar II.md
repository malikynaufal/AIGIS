---
code: FKD211201
name: Fisika Dasar II — Electromagnetism & Circuits
SKS: 3
semester: 2
department: Fisika
tags: [physics, electromagnetism, circuits, electricity, magnetism]
created: 2026-07-27
---

# FKD211201 — Fisika Dasar II: Electricity and Magnetism

## Course Overview

This course introduces the fundamental principles of electricity and magnetism — the twin pillars of classical electromagnetism. Starting from Coulomb's law and electric fields, the course progresses through circuits, magnetic fields, and electromagnetic induction, providing the foundation required for understanding waves, optics, and modern physics.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Dasar I (mechanics)
**Co-requisites:** Kalkulus II

---

## 📋 Topics & Outline

### Unit 1: Electrostatics (Weeks 1–4)

- **Electric charge:** quantization, conservation, conductors vs. insulators

- **Coulomb's Law:** F = kq₁q₂/r² (vector form)

- **Electric field:** E = F/q, field lines, superposition

- **Gauss's Law:** ∮ E·dA = Q_enc/ε₀
  - Applications: infinite line charge, infinite plane, spherical shell

- **Electric potential:** V = -∫E·dr, potential energy U = qV

- Equipotential surfaces and conductors in electrostatic equilibrium

### Unit 2: Electric Current and Circuits (Weeks 5–8)

- **Current:** I = dQ/dt, conventional vs. electron flow

- **Resistance and Ohm's Law:** V = IR, resistivity ρ = RA/L

- **Power:** P = IV = I²R = V²/R

- **DC circuit analysis:**
  - Kirchhoff's rules: junction rule (ΣI_in = ΣI_out) and loop rule (ΣΔV = 0)
  - Series and parallel resistors
  - Wheatstone bridge
  - RC circuits: charging (q = Cε(1-e^{-t/RC})), discharging

- **Internal resistance and emf:** ε = V + Ir

- Capacitors: C = Q/V, energy stored U = ½CV²

- Time constant τ = RC

### Unit 3: Magnetism (Weeks 9–12)

- **Magnetic field:** B-field, magnetic forces on moving charges

- **Lorentz force:** F = qv × B

- **Magnetic field of a current:** Biot-Savart law

- **Ampere's Law:** ∮ B·dl = μ₀I_enc
  - Applications: solenoid (B = μ₀nI), toroid, infinite wire

- **Magnetic force on a current-carrying wire:** F = IL × B

- **Torque on a current loop:** τ = NIAB sin(θ)

- Magnetic materials: diamagnetism, paramagnetism, ferromagnetism

### Unit 4: Electromagnetic Induction (Weeks 13–16)

- **Faraday's law:** ε = -dΦ_B/dt

- **Lenz's law:** direction of induced current opposes change

- **Magnetic flux:** Φ_B = ∫ B·dA

- **Motional emf:** ε = Bℓv

- **Inductors:** L = NΦ/I, energy U = ½LI²

- **RL circuits:** time constant τ = L/R

- **LC oscillations:** energy exchange between L and C

- **Maxwell's modification:** displacement current

---

## 🔬 Key Equations

```
Coulomb:          F = k(q₁q₂/r²)  k = 1/(4πε₀) = 8.99×10⁹ N·m²/C²
Electric Field:   E = F/q = kq/r² 
Gauss's Law:      ∮ E·dA = Q_enc/ε₀
Potential:        V = kq/r, ΔV = -∫E·dr
Ohm's Law:        V = IR
Power:            P = IV
Biot-Savart:      dB = μ₀/4π · (Idl × r̂)/r²
Ampere's Law:     ∮ B·dl = μ₀I_enc
Faraday:          ε = -dΦ_B/dt
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Calculate electric and magnetic fields for symmetric charge/current distributions
2. Apply Gauss's law and Ampere's law to simplify calculations
3. Analyze DC and RC circuits using Kirchhoff's rules
4. Compute electromagnetic induction and motional emf
5. Understand the connection between electricity and magnetism
6. Apply electromagnetic principles to geophysical and geodetic instruments

---

## 📚 References

1. Halliday, D., Resnick, R., & Walker, J. (2013). *Fundamentals of Physics*, 10th ed. Wiley.
2. Serway, R.A. & Jewett, J.W. (2018). *Physics for Scientists and Engineers*, 10th ed. Cengage.
3. Griffiths, D.J. (2017). *Introduction to Electrodynamics*, 4th ed. Cambridge. (Reference)
4. MIT OCW 8.02 Electricity & Magnetism: https://ocw.mit.edu/courses/8-02-electricity-and-magnetism-spring-2016/
5. HyperPhysics — Electricity & Magnetism: http://hyperphysics.phy-astr.gsu.edu/hbase/electric.html

---

## 🧪 Worked Examples

### Example 1: Gauss's Law — Infinite Line Charge
Find the electric field from an infinite line charge with linear density $\lambda$.

**Choose Gaussian surface:** Cylinder of radius $r$, length $L$, coaxial with line.
$$\oint ec{E} \cdot dec{A} = E(2\pi r L) = rac{\lambda L}{\epsilon_0}$$

$$
E = rac{\lambda}{2\pi\epsilon_0 r}$$**Dimensional check:**$[\lambda] = C/m$, $[\epsilon_0] = F/m$, $[r] = m$
$$

rac{C/m}{(F/m)(m)} = rac{C}{F\cdot m} = rac{V}{m}$$✓

### Example 2: RC Circuit Charging
A 10 μF capacitor charges through a 1 MΩ resistor from a 12 V source.

**Time constant:**$	au = RC = (10^6)(10^{-5}) = 10$s

**Voltage across capacitor:**$$V_C(t) = 12(1 - e^{-t/10}) 	ext{ V}$$**At$t = 10$s (one time constant):**$V_C = 12(1 - e^{-1}) = 12(0.632) = 7.59$V

**At$t = 30$s (three time constants):**$V_C = 12(0.950) = 11.4$V

### Example 3: Magnetic Field of a Solenoid
A solenoid has 500 turns, length 0.5 m, carrying 2 A.$$B = \mu_0 n I = (4\pi 	imes 10^{-7})(500/0.5)(2) = 4\pi 	imes 10^{-7} 	imes 1000 	imes 2 = 2.51 	ext{ mT}
$$

### Example 4: Motional EMF
A conducting bar ($L = 0.3$m) moves at$v = 5$m/s through$B = 0.5$T.$$arepsilon = BLv = (0.5)(0.3)(5) = 0.75 	ext{ V}$$### Example 5: Inductance and Energy
An inductor$L = 0.5$H carries current$I = 4$A.

**Energy stored:**$$U = rac{1}{2}LI^2 = rac{1}{2}(0.5)(16) = 4 	ext{ J}
$$

---

## 🌐 Additional Online Resources

- **PhET: Circuit Construction Kit** — https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc

- **MIT OCW 8.02 Electricity & Magnetism** — https://ocw.mit.edu/courses/8-02-electricity-and-magnetism-spring-2016/

- **OpenStax University Physics Vol. 2** — https://openstax.org/details/books/university-physics-volume-2

- **Khan Academy: Electricity & Magnetism** — https://www.khanacademy.org/science/physics/electric-magnetic-forces

- **Feynman Lectures Vol. II (Ch. 1-18)** — https://www.feynmanlectures.caltech.edu/II_toc.html

- **HyperPhysics: Electricity & Magnetism** — http://hyperphysics.phy-astr.gsu.edu/hbase/electric.html

