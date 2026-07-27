---
tags: [physics, study-pack, aigis, relativity, spacetime]
aliases: [Special Relativity, SR Study Pack]
created: 2026-07-12
updated: 2026-07-27
---

# 📚 Study Pack — Special Relativity
_Spacetime Diagrams, Relativistic Dynamics, E = mc²_

---

## 1. Two Postulates

1. **Relativity Principle:** All inertial frames are equivalent; laws of physics are identical in all.
2. **Speed of Light:** Light propagates at $c = 2.998\times10^8 $m/s in vacuum, independent of source motion.

---

## 2. Lorentz Transformations

### Derivation
Start with 1D motion:$x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2) $where $\gamma = 1/\sqrt{1 - v^2/c^2} $.

### Full 4D Transformation

$$x' = \gamma(x - vt)t' = \gamma(t - vx/c^2)y' = y, \quad z' = 
z

$$### Inverse Transformation$$

x = \gamma(x' + vt')t = \gamma(t' + vx'/c^2
)

$$### Matrix Form$$

\begin{pmatrix} ct' \\ x' \\ y' \\ z' \end{pmatrix} = \begin{pmatrix} \gamma & -\gamma\beta & 0 & 0 \\ -\gamma\beta & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} ct \\ x \\ y \\ z \end{pmatrix} $$---

## 3. Consequences

### Time Dilatio
n

$$\Delta t = \gamma \Delta t_0$$where $\Delta t_0$(proper time) is measured by clock at rest relative to events.

### Length Contractio
n

$$L = L_0/\gamma$$where $L_0$(proper length) measured in object's rest frame.

### Velocity Additio
n

$$u' = \frac{u - v}{1 - uv/c^2
}

$$### Relativistic Doppler Shift$$

\nu_{\text{obs}} = \nu_{\text{source}} \sqrt{\frac{1 + \beta}{1 - \beta}} \quad \text{(receding)}\nu_{\text{obs}} = \nu_{\text{source}} \sqrt{\frac{1 - \beta}{1 + \beta}} \quad \text{(approaching)} $$### Worked Example: Muon Decay
Muons produced at 60 km altitude with $v = 0.998c$ ($\gamma = 15.8$). Proper lifetime $\tau_0 = 2.2$ $\mu $s.

**Classical:** $d = v\tau = 0.998c \times 2.2\,\mu\text{s} = 660 $m → would not reach Earth.

**Relativistic:** In Earth frame, muon lifetime is $\gamma\tau_0 = 34.8$ $\mu $s, so $d = v\gamma\tau_0 = 10.4 $km. Probability of surviving 60 km:$P = e^{-60/10.4} = 0.003$(still small but measurable).

---

## 4. Spacetime Diagrams

### Minkowski Metric
Four-vectors:$x^\mu = (ct, x, y, z)$**Interval:*
*

$$s^2 = -c^2 t^2 + x^2 + y^2 + z^2$$

**Invariance:**$s^2 = s'^2$(Lorentz invariant)

### Light Cone Classification
| Type | $s^2$ | Causally Connected? |
|------|-------|---------------------|
| Timelike | $s^2 < 0$ | Yes |
| Null (lightlike) | $s^2 = 0$ | Yes (at speed of light) |
| Spacelike | $s^2 > 0$ | No |

### World Lines

- **Massive particles:**$dx/dt < c$(inside light cone)

- **Light:**$dx/dt = \pm c$(on light cone)

- FTL particles (tachyons, hypothetical):$dx/dt > c$(outside cone)

### Proper Time Along World Lin
e

$$\Delta\tau = \int \sqrt{1 - \frac{v(t)^2}{c^2}} \, dt$$

---

## 5. Relativistic Dynamics

### Energy-Momentum Four-Vecto
r

$$p^\mu = (E/c, \vec{p})$$

**Norm:**$p^\mu p_\mu = -(mc)^2$### Relativistic Energ
y

$$E = \gamma mc^2$$

- **Rest energy:**$E_0 = mc^2$- **Kinetic energy:**$K = (\gamma - 1)mc^2$### Relativistic Momentu
m

$$\vec{p} = \gamma m\vec{v} $$

### Energy-Momentum Relatio
n

$$E^2 = (mc^2)^2 + (pc)^2$$

#### Limits:
-$p \ll mc$: $E \approx mc^2 + p^2/(2m)$(Newtonian limit)
-$p \gg mc$: $E \approx pc$(ultrarelativistic, e.g., photons)

### Worked Example: LHC Proton
Proton with $K = 7 $TeV, rest mass $m_p c^2 = 938 $MeV:

1.$\gamma = 1 + K/(m_p c^2) = 1 + 7000/0.938 = 7463$2.$v/c = \sqrt{1 - 1/\gamma^2} \approx 1 - 10^{-8} $(99.999999%$c$)
3. Total $E = \gamma m_p c^2 = 7.001 $TeV

---

## 6. Four-Vector Formulation

### Four-Velocit
y

$$u^\mu = \frac{dx^\mu}{d\tau} = \gamma(c, \vec{v})$$

Normalization:$u^\mu u_\mu = -c^2$### Four-Acceleratio
n

$$a^\mu = \frac{du^\mu}{d\tau} $$

Property:$u^\mu a_\mu = 0$(orthogonal to four-velocity)

### Electromagnetic Field Tenso
r

$$F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\m
u

$$Maxwell's equations in covariant form:$$

\partial_\mu F^{\mu\nu} = \mu_0 J^\nu\partial_{[\alpha} F_{\beta\gamma]} = 0$$---

## 7. Applications in Geodesy and GNSS

### Relativistic Corrections for GNSS

| Effect | Formula | Magnitude (per day) |
|--------|---------|---------------------|
| Special time dilation | $\Delta t = -v^2/(2c^2) \cdot T$ | $-7.2$µs |
| Gravitational time dilation | $\Delta t = \Delta U/c^2 \cdot T$ | $+45.7$µs |
| Sagnac effect | $\Delta t = 2\vec{\Omega}\cdot\vec{A}/c^2$ | up to $\pm133 $ns |

**Net correction:**$-38.5$µs/day (must be compensated for clock accuracy)

### Relativistic Orbit Perturbation (Schwarzschild
)

$$\vec{a}_{\text{rel}} = \frac{GM}{c^2 r^2}\left[\left(4\frac{GM}{r} - v^2\right)\hat{r} + 4(\vec{v}\cdot\hat{r})\vec{v}\right]$$

### Light Deflection (GR)
For a ray passing near the Sun
:

$$\Delta\theta = \frac{4GM}{c^2 b} = 1.75'' \text{ (at Sun's limb)} $$

---

## 8. Problems

1. A spaceship travels at$0.8c $to a star 10 ly away. Find travel time (Earth), proper time (ship), and aging difference.

2. An electron has KE = 1.00 MeV. Compute its speed and $\gamma$ ($m_e c^2 = 0.511 $MeV).

3. Two protons collide head-on, each with KE = 7 TeV (LHC). Find the center-of-mass energy.

4. Derive the Doppler shift for light:$\nu_{\text{obs}} = \nu_{\text{src}}\sqrt{(1+\beta)/(1-\beta)} $.

5. A GPS satellite travels at $v = 3.87 $km/s at altitude 20,200 km. Calculate the special relativistic time dilation in $\mu $s/day.

6. Prove $E^2 = (pc)^2 + (mc^2)^2 $from $p^\mu p_\mu = -(mc)^2$.

7. An astronaut carries a clock. At what speed must she travel so that 1 yr ship time = 10 yr Earth time?

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $x' = \gamma(x-vt)$, $t' = \gamma(t-vx/c^2)$ | Lorentz transform | Frame transformation |
| $\Delta t = \gamma\Delta t_0$ | Time dilation | Moving clocks |
| $L = L_0/\gamma$ | Length contraction | Moving rods |
| $u' = (u-v)/(1-uv/c^2)$ | Velocity addition | Relativistic composition |
| $E = \gamma mc^2$ | Relativistic energy | Total energy |
| $K = (\gamma-1)mc^2$ | Relativistic KE | Kinetic energy |
| $\vec{p} = \gamma m\vec{v} $ | Relativistic momentum | Momentum |
| $E^2 = (mc^2)^2 + (pc)^2$ | Energy-momentum | Combined relation |

---

## References

- Taylor & Wheeler, "Spacetime Physics" (2nd ed.)

- Griffiths, "Introduction to Electrodynamics" (Ch. 12)

- Feynman Lectures Vol. I (Ch. 15-21)

- MIT OCW 8.033: Relativity

- OpenStax University Physics Vol. 3 (Ch. 5)

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
