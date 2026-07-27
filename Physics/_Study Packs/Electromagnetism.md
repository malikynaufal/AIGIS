---
tags: [physics, study-pack, aigis, electromagnetism]
aliases: [Electromagnetism, EM Study Pack]
created: 2026-07-12
updated: 2026-07-27
---

# 📚 Study Pack — Electromagnetism
_Expanded: EM Waves, Radiation, Waveguides

---

## 1. Maxwell's Equations (Review)

### Differential Form

$$\begin{aligned}
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
\end{aligned} $$---

## 2. Electromagnetic Waves

### Wave Equation Derivation
Take curl of Faraday's law
:

$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B})$$Using $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} = -\nabla^2\vec{E} $(since $\nabla\cdot\vec{E} = 0 $in vacuum)
:

$$\nabla^2\vec{E} = \mu_0\epsilon_0\frac{\partial^2\vec{E}}{\partial t^2} $$

Wave speed:$c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998\times10^8 $m/s.

### Plane Wave Solutions

$$\vec{E} = \vec{E}_0 e^{i(\vec{k}\cdot\vec{r} - \omega t)}\vec{B} = \vec{B}_0 e^{i(\vec{k}\cdot\vec{r} - \omega t)} $$where $\omega = ck$,$ |\vec{B}_0| = |\vec{E}_0|/c$,$\vec{E} \\perp \vec{B} \\perp \vec{k} $.

### Energy and Momentum

- **Energy density:** $u = \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0}B^2$- **Poynting vector:**$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B} $- **Intensity:**$I = \langle S \rangle = \frac{1}{2}\epsilon_0 c E_0^2$### Polarization States
| Type | $\vec{E} $behavior |
|------|---------------------|
| Linear | Oscillates along fixed direction |
| Circular | $|E_x| = |E_y| $, $\Delta\phi = \pm\pi/2$ |
| Elliptical | General case |

---

## 3. Electromagnetic Radiation

### Larmor Formula (Power radiated by accelerating charge
)

$$P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3} $$For non-relativistic acceleration $a$.

### Dipole Radiation
Electric dipole moment $\vec{p} = \sum_i q_i \vec{r}_i$. Far field:

$$\vec{E}_{\theta} = \frac{1}{4\pi\epsilon_0}\frac{\ddot{p}\sin\theta}{c^2 r} $$Total power:$P = \frac{\mu_0}{6\pi c}\ddot{p}^2$(same as Larmor).

### Radiation Resistance
For an oscillating dipole antenna:

$$R_{\text{rad}} = \frac{2}{3}\frac{\mu_0 c}{\lambda^2}(qL)^2 \\quad \text{(for length $L$, charge $q$, frequency $f $with $\lambda = c/f$)} $$

---

## 4. Waveguides and Transmission Lines

### Rectangular Waveguide
For a rectangular waveguide of width $a$, height $b$, the modes are TE$_{mn} $ and TM$_{mn} $.

**Cutoff frequency:**

$$f_{c,mn} = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2} $$**Phase velocity:**$v_p = \frac{c}{\sqrt{1 - (f_c/f)^2}} > c$**Group velocity:**$v_g = c\sqrt{1 - (f_c/f)^2} < c $Note:$v_p \cdot v_g = c^2$(no information travels faster than $c$).

### Transmission Line (TEM Mode)

$$V(z,t) = V_0^+ e^{-\gamma z} e^{i(\omega t - \beta z)} + V_0^- e^{+\gamma z} e^{i(\omega t + \beta z)} $$- Propagation constant:$\gamma = \alpha + i\beta = \sqrt{(R + i\omega L)(G + i\omega C)} $- Characteristic impedance:$Z_0 = \sqrt{(R + i\omega L)/(G + i\omega C)} $### Smith Chart Applications
Used for impedance matching, reflection coefficient measurement, and SWR calculations.

---

## 5. Applications in Geodesy and GNSS

### GNSS Signal Propagation
| Band | Frequency | Wavelength | Use |
|------|-----------|------------|-----|
| L1 | 1575.42 MHz | 19.0 cm | C/A code, carrier phase |
| L2 | 1227.60 MHz | 24.4 cm | P(Y) code, ionosphere-free combo |
| L5 | 1176.45 MHz | 25.5 cm | Safety-of-life aviation |

### Ionospheric Dela
y

$$\Delta_{\text{ion}} = \frac{40.3}{f^2} \int N_e \, ds \\quad \text{(meters)} $$where $N_e$= electron density (electrons/m³),$f$= frequency (Hz).

### Faraday Rotatio
n

$$\Omega_F = \frac{e^2}{2\epsilon_0 m_e c}\int N_e B_{\\parallel} \, ds \\quad \text{(radians)} $$

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $c = 1/\sqrt{\mu_0\epsilon_0} $ | Speed of light | EM wave speed |
| $\vec{S} = \vec{E}\times\vec{B}/\mu_0$ | Poynting vector | Power flow |
| $P = q^2a^2/(6\pi\epsilon_0 c^3)$ | Larmor formula | Radiated power |
| $f_c = (c/2)\sqrt{(m/a)^2 + (n/b)^2} $ | Waveguide cutoff | Mode cutoff |
| $v_p \cdot v_g = c^2$ | Waveguide identity | Phase/group velocity |

---

## Problems
1. Derive the wave equation for $\vec{B} $in vacuum and show it has the same speed.
2. A plane wave has $E_0 = 100 $V/m. Find $B_0$, intensity, and radiation pressure.
3. Find the cutoff wavelength for TE$_{10} $mode in a rectangular waveguide of width 2.286 cm.
4. Calculate the power radiated by an electron accelerated at$10^{15} $ m/s².
5. Show that the group velocity in a waveguide equals the particle velocity in a relativistic particle.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
