---
tags: [aigis, concept, physics, electromagnetism, field-theory]
created: 2026-07-27
updated: 2026-07-27
---

# Electromagnetism

## Gauss's Law, Ampere's Law, and Maxwell's Equations

**Core Idea:** Electromagnetism unifies electricity, magnetism, and light. Maxwell's four equations describe the complete behavior of electromagnetic fields and their interaction with matter.

---

## 1. Electric Field and Coulomb's Law

### Coulomb's Law
Two point charges interact with a force:

$$\vec{F} = \frac{1}{4\pi\epsilon_0}\frac{q_1 q_2}{r^2}\hat{r} $$where $\epsilon_0 = 8.854 \times 10^{-12} $F/m (permittivity of free space).

### Electric Fiel
d

$$\vec{E} = \frac{\vec{F}}{q} = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}\hat{r} $$

**Superposition Principle:** For multiple charges
:

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0}\sum_i \frac{q_i(\vec{r} - \vec{r}_i)}{|\vec{r} - \vec{r}_i|^3} $$

---

## 2. Gauss's Law for Electricity

### Statement
The electric flux through any closed surface equals the enclosed charge divided by $\epsilon_0$:

$$\oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\epsilon_0
}

$$### Differential Form$$

\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$### Derivation from Coulomb's Law
Consider a point charge $q $at the origin. On a sphere of radius $r$:

- $\vec{E} = \frac{q}{4\pi\epsilon_0 r^2}\hat{r} $(radial)
-$d\vec{A} = r^2\sin\theta\,d\theta\,d\phi\,\hat{r} $(radial)
-$\vec{E}\cdot d\vec{A} = \frac{q}{4\pi\epsilon_0 r^2}\cdot r^2\sin\theta\,d\theta\,d\phi$

$$\oint \vec{E}\cdot d\vec{A} = \frac{q}{4\pi\epsilon_0}\int_0^{2\pi}d\phi\int_0^{\pi}\sin\theta\,d\theta = \frac{q}{4\pi\epsilon_0}\cdot 4\pi = \frac{q}{\epsilon_0} $$### Applications
| Geometry | Surface | Result |
|----------|---------|--------|
| Point charge | Sphere | $E = \frac{q}{4\pi\epsilon_0 r^2} $ |
| Infinite line ($\lambda$) | Cylinder | $E = \frac{\lambda}{2\pi\epsilon_0 r} $ |
| Infinite plane ($\sigma$) | Gaussian pillbox | $E = \frac{\sigma}{2\epsilon_0} $ |
| Conducting sphere | Outer sphere | $E = \frac{q}{4\pi\epsilon_0 r^2} $(outside) |

### Worked Example: Electric Field of a Thick Shell
A conducting spherical shell has inner radius $R_1$, outer radius $R_2$, charge $Q$.

- **Inside ($r < R_1$):** $E = 0$ (no enclosed charge)

- **Between shells ($R_1 < r < R_2$):** $E = 0$ (inside conductor)

- **Outside ($r > R_2$):** $E = \frac{Q}{4\pi\epsilon_0 r^2} $(total charge enclosed)

**Dimensional check:**$[E] = \frac{[q]}{\epsilon_0 [r^2]} = \frac{C}{(F/m)(m^2)} = \frac{C \cdot m}{F \cdot m^2} = \frac{V}{m} $✓

---

## 3. Magnetic Fields and Ampere's Law

### Biot-Savart Law
A current element $I\,d\vec{l} $produces a magnetic field
:

$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{I\,d\vec{l}\times\hat{r}}{r^2} $$where $\mu_0 = 4\pi \times 10^{-7} $T·m/A (permeability of free space).

### Ampere's Law
The line integral of $\vec{B} $around a closed loop equals $\mu_0 $times the enclosed current
:

$$\oint_C \vec{B}\cdot d\vec{l} = \mu_0 I_{\text{enc}} $$

### Differential For
m

$$\nabla \times \vec{B} = \mu_0\vec{J} $$

### Applications
| Geometry | Loop | Result |
|----------|------|--------|
| Infinite straight wire | Circle of radius $r$ | $B = \frac{\mu_0 I}{2\pi r} $ |
| Solenoid ($n $turns/m) | Rectangle inside | $B = \mu_0 n I$ |
| Toroid ($N $turns, radius $R$) | Circle of radius $r$ | $B = \frac{\mu_0 N I}{2\pi r} $ |

---

## 4. Faraday's Law and Lenz's Law

### Faraday's Law of Induction
A changing magnetic flux induces an electromotive force (EMF)
:

$$\mathcal{E} = -\frac{d\Phi_B}{dt} $$

### Differential For
m

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

**Lenz's Law:** The induced EMF drives a current whose magnetic field opposes the change in flux that produced it.

### Self-Inductanc
e

$$\mathcal{E} = -L\frac{dI}{dt} $$

For a solenoid:$L = \mu_0 n^2 \ell A $where $\ell $is length,$A $is cross-sectional area.

---

## 5. Maxwell's Equations (Complete Set)

### Differential Form$$\begin{aligned}
\nabla \cdot \vec{E} &= \frac{\rho}{\epsilon_0} [4pt]
\nabla \cdot \vec{B} &= 0 [4pt]
\nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} [4pt]
\nabla \times \vec{B} &= \mu_0\vec{J} + \mu_0\epsilon_0\frac{\partial \vec{E}}{\partial t}
\end{aligned
}

$$### Integral Form$$

\begin{aligned}
\oint_S \vec{E}\cdot d\vec{A} &= \frac{Q_{\text{enc}}}{\epsilon_0} [4pt]
\oint_S \vec{B}\cdot d\vec{A} &= 0 [4pt]
\oint_C \vec{E}\cdot d\vec{l} &= -\frac{d\Phi_B}{dt} [4pt]
\oint_C \vec{B}\cdot d\vec{l} &= \mu_0 I_{\text{enc}} + \mu_0\epsilon_0\frac{d\Phi_E}{dt}
\end{aligned} $$### Physical Meaning of Each Equation
| Equation | Name | Meaning |
|----------|------|---------|
| $\nabla \cdot \vec{E} = \rho/\epsilon_0$ | Gauss's Law (E) | Charges produce electric fields |
| $\nabla \cdot \vec{B} = 0$ | Gauss's Law (B) | No magnetic monopoles |
| $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$ | Faraday's Law | Changing B-field creates E-field |
| $\nabla \times \vec{B} = \mu_0\vec{J} + \mu_0\epsilon_0\partial\vec{E}/\partial t$ | Ampere-Maxwell | Currents and changing E-field create B-field |

### The Maxwell Displacement Current
The term $\mu_0\epsilon_0\frac{\partial \vec{E}}{\partial t} $was Maxwell's crucial addition to Ampere's law. It ensures charge conservation (continuity equation):

$$\nabla \cdot \vec{J} = -\frac{\partial\rho}{\partial t} $$

---

## 6. Electromagnetic Waves

### Derivation of the Wave Equation
From Faraday's and Ampere-Maxwell in vacuum ($\rho = 0$, $\vec{J} = 0$):

Take the curl of Faraday's Law:

$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0\epsilon_0\frac{\partial^2\vec{E}}{\partial t^2} $$Using the identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} = -\nabla^2\vec{E} $:

$$\boxed{\nabla^2\vec{E} = \mu_0\epsilon_0\frac{\partial^2\vec{E}}{\partial t^2}
}

$$This is the wave equation with speed:$$

c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998 \times 10^8 \text{ m/s
}

$$### Plane Wave Solutions$$

\vec{E} = \vec{E}_0\cos(\vec{k}\cdot\vec{r} - \omega t)\vec{B} = \vec{B}_0\cos(\vec{k}\cdot\vec{r} - \omega t)$$where $\omega = ck$,$ |\vec{B}_0| = |\vec{E}_0|/c$, and $\vec{E} \perp \vec{B} \perp \vec{k} $.

### Energy Density and Poynting Vector

$$u = \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0}B^2\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B} \quad \text{(Poynting vector, W/m}^2\text{)} $$**Dimensional analysis:**$[S] = \frac{[E][B]}{\mu_0} = \frac{(V/m)(T)}{(T\cdot m/A)} = \frac{V \cdot A}{m^2} = W/m^2$✓

---

## 7. EM Spectrum and Applications

| Wave | Frequency | Wavelength | Application |
|------|-----------|------------|-------------|
| Radio | < 3 GHz | > 10 cm | GNSS, broadcast |
| Microwave | 3–300 GHz | 1 mm–10 cm | Radar, GNSS L-band |
| Infrared | 300 GHz–400 THz | 750 nm–1 mm | Remote sensing |
| Visible | 400–800 THz | 400–750 nm | Optical geodesy |
| X-ray | > 10¹⁶ Hz | < 10 nm | Material analysis |

---

## 8. Dielectrics and Magnetic Materials

### Dielectric Constant
In a dielectric medium, the permittivity becomes $\epsilon = \kappa\epsilon_0 $where $\kappa $is the dielectric constant
.

$$\vec{E} = \frac{\vec{E}_{\text{vac}}}{\kappa} \quad \text{(inside dielectric)} $$

### Gauss's Law in Dielectric
s

$$\nabla \cdot \vec{D} = \rho_f \quad \text{where } \vec{D} = \epsilon\vec{E} $$

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $\vec{F} = q\vec{E} + q\vec{v}\times\vec{B} $ | Lorentz Force | Force on charge in E, B fields |
| $\nabla \cdot \vec{E} = \rho/\epsilon_0$ | Gauss's Law | Electric field from charge distributions |
| $\nabla \times \vec{B} = \mu_0\vec{J} + \mu_0\epsilon_0\partial\vec{E}/\partial t$ | Ampere-Maxwell | Magnetic field from currents |
| $\nabla \times \vec{E} = -\partial\vec{B}/\partial t$ | Faraday's Law | Induced EMF |
| $c = 1/\sqrt{\mu_0\epsilon_0} $ | Speed of light | EM wave propagation |
| $\vec{S} = \vec{E}\times\vec{B}/\mu_0$ | Poynting vector | Energy transport |

---

## Study Problems
1. Use Gauss's law to find the electric field inside and outside a uniformly charged sphere of radius $R $and total charge $Q$.
2. Derive Ampere's law for the magnetic field inside a long solenoid with $n $turns per meter.
3. Show that electromagnetic waves carry energy at the rate given by the Poynting vector.
4. A parallel plate capacitor has $\kappa = 3$, area $A$, separation $d$. Find the capacitance and the stored energy.
5. Verify the speed of light from $\mu_0 $and $\epsilon_0$ values.

---

## References

- OpenStax University Physics Vol. 2 (Chapters 5-7): Gauss's Law, Electric Potential

- MIT OCW 8.02: Electricity and Magnetism

- Griffiths, D.J., "Introduction to Electrodynamics" (4th ed.)

- Feynman Lectures Vol. II

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
