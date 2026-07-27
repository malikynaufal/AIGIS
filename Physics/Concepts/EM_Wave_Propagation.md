---
tags: [physics, concept, aigis]
aliases: [EM Wave Propagation]
created: 2026-07-27
---

# EM Wave Propagation

> Wave equation, plane waves, polarization, reflection/refraction, waveguides

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** EM waves propagate through space and media, subject to absorption, scattering, and refraction by charged particles and dielectrics.

> **Geodesy Connection:** GNSS signals propagate through the ionosphere (dispersive) and troposphere (non-dispersive), causing measurable delays used for atmospheric sounding.

---

## 🧮 Key Equations

$$

\begin{equation}
\mathbf{E} = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}
\end{equation}
\text{(Plane wave solution)}

$ $

$$

\begin{equation}
n = \frac{c}{v} = \sqrt{\varepsilon_r \mu_r}
\end{equation}
\text{(Refractive index)}

$ $

$$

\begin{equation}
n^2 = 1 - \frac{\omega_p^2}{\omega^2}
\end{equation}
\text{(Ionospheric refractive index, cold plasma)}

$ $

$$

\begin{equation}
\omega_p = \sqrt{\frac{N_e e^2}{m_e \varepsilon_0}}
\end{equation}
\text{(Plasma frequency)}

**### Ionospheric Delay **

\begin{equation}
\Delta I = \frac{40.3 \cdot \text{TEC}}{f^2}
\end{equation}
\text{(Ionospheric path delay in meters)}

$ $

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** Like ripples spreading on a pond — the ionosphere acts like a lens that bends and slows radio waves.

> **Key insight:** GNSS signals travel at light speed in vacuum but slow down in ionized plasma, with delay proportional to $ 1/f^2 $.

> **Geodesy intuition:** Dual-frequency GPS removes 99% of ionospheric error by exploiting the $ 1/f^2 $ dispersion.

---

## 🔗 Links

- **Related:** [[Electrodynamics]] · [[Atmospheric_Physics]]
- **Geodesy:** [[Orbital_Mechanics]] · [[Relativistic_Applications]]
- **Study Pack:** [[_Study Packs/]]

*Last updated: 2026-07-27*