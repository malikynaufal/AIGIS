---
tags: [physics, study-pack, aigis, waves, optics, fourier]
aliases: [Waves and Optics, Wave Optics Pack]
created: 2026-07-12
updated: 2026-07-27
---

# 📚 Study Pack — Waves and Optics
_Expanded: Fourier Optics, Lasers Basics

---

## 1. Wave Equation and Solutions

### 1D Wave Equation

$$ \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} $ $

General solution: $$ y(x,t) = f(x-vt) + g(x+vt) $### Harmonic Wav
e

$ $ y(x,t) = A\cos(kx - \omega t + \phi) $$

- $ k = 2\pi/\lambda $ (wave number)
-$ \omega = 2\pi f $ (angular frequency)
- $ v = \omega/k = \lambda f $---

## 2. Interference

### Double Slit (Young)
Path difference: $ \Delta r = d\sin\theta $- **Bright fringes:**$ d\sin\theta = m\lambda $- **Dark fringes:**$ d\sin\theta = (m+\frac{1}{2})\lambda $ Fringe spacing: $ \Delta y = \frac{\lambda L}{d} $### Multiple Slits (Diffraction Grating)
Principal maxima: $ d\sin\theta = m\lambda $ Angular dispersion: $ \frac{d\theta}{d\lambda} = \frac{m}{d\cos\theta} $ Resolving power: $  R = \frac{\lambda}{\Delta\lambda} = mN $---

## 3. Diffraction

### Single Slit (Fraunhofer
)

$ $ I(\theta) = I_0 \left(\frac{\sin\beta}{\beta}\right)^2, \quad \beta = \frac{\pi a\sin\theta}{\lambda} $$

Minima: $ $ a\sin\theta = m\lambda \quad (m \neq 0) $### Circular Aperture (Airy Pattern
)

$$ I(\theta) = I_0 \left(\frac{2J_1(\pi D\sin\theta/\lambda)}{\pi D\sin\theta/\lambda}\right)^2 $ $

First minimum: $ \theta_{\min} \approx 1.22\lambda/D $**Rayleigh criterion:**$ \theta_{\min} = 1.22\lambda/D $---

## 4. Polarization

### Jones Calculus
| Element | Jones Matrix |
|---------|-------------|
| Horizontal polarizer | $ \begin{pmatrix}1&0\\0&0\end{pmatrix} $ |
| Vertical polarizer | $ \begin{pmatrix}0&0\\0&1\end{pmatrix} $ |
| 45° polarizer | $ \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix} $ |
| QWP (fast axis horizontal) | $ \begin{pmatrix}1&0\\0&-i\end{pmatrix} $ |
| HWP (fast axis horizontal) | $ \begin{pmatrix}1&0\\0&-1\end{pmatrix} $ |

### Malus's La
w

$ I = I_0 \cos^2\theta $ $

### Brewster's Angl
e

$$ \tan\theta_B = n_2/n_1

$ $

---

## 5. Fourier Optics (Introduction)

### Key Idea
Fraunhofer diffraction pattern = **Fourier Transform** of aperture function.

### Aperture Function $ A(x,y) $ For a slit of width $  a $:

$ $

A(x) = \text{rect}(x/a) = \begin{cases}1 & |x| < a/2 \\ 0 & \text{otherwise}\end{cases
}

**### Far-Field Pattern **

 U(f_x, f_y) = \mathcal{F}\{A(x,y)\} $ where spatial frequencies $ f_x = x/(\lambda z) $, $ f_y = y/(\lambda z) $.

### Example: Rectangular Aperture

$ $ \mathcal{F}\{\text{rect}(x/a)\text{rect}(y/b)\} = ab\,\text{sinc}(\pi a f_x)\text{sinc}(\pi b f_y
)

**### Example: Circular Aperture **

 \mathcal{F}\{\text{circ}(r/a)\} = \frac{2J_1(2\pi a f)}{2\pi a f} \propto \frac{J_1(\rho)}{\rho}

$$

# ## Convolution Theorem
For two apertures: $ A_1 * A_2 \leftrightarrow \mathcal{F}\{A_1\} \cdot \mathcal{F}\{A_2\} $---

## 6. Laser Basics

### Principles
1. **Population inversion:** $ N_2 > N_1 $ (non-thermal distribution)
2. **Stimulated emission:** Photon + excited atom → 2 photons
3. **Optical cavity:** Feedback via mirrors

### Rate Equations (4-Level System)

$ $ \frac{dN_2}{dt} = R_p - \frac{N_2}{\tau_2} - W(N_2 - N_1)\frac{d\phi}{dt} = W(N_2 - N_1)\phi - \frac{\phi}{\tau_c} $$

where $\phi $ = photon density,$ \tau_c $= cavity lifetime.

### Threshold Conditio
n

$ $ W(N_2 - N_1) = \frac{1}{\tau_c} $$

# ## Common Laser Types
| Type | Wavelength | Application |
|------|------------|-------------|
| He-Ne | 632.8 nm | Alignment, holography |
| Nd:YAG | 1064 nm | LIDAR, machining |
| Diode | 780–1550 nm | Telecom, GNSS |
| Fiber | 1550 nm | Telecom, sensing |
| Ti:Sapphire | 700–1000 nm | Ultrafast, spectroscopy |

### Coherence

- **Temporal coherence:**$ \tau_c \approx 1/\Delta\nu $- **Spatial coherence:** $ A_c \approx (\lambda L/D)^2 $- **Coherence length:** $ L_c = c\tau_c = c/\Delta\nu $---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $ d\sin\theta = m\lambda $ | Interference/grating | Fringe positions |
| $ I = I_0(\sin\beta/\beta)^2 $ | Single-slit diffraction | Intensity pattern |
| $ I = I_0[2J_1(\rho)/\rho]^2 $ | Circular aperture | Airy disk |
| $ I = I_0\cos^2\theta $ | Malus's law | Polarizer transmission |
| $ \tan\theta_B = n_2/n_1 $ | Brewster's angle | Polarized reflection |
| $ \mathcal{F}\{A(x,y)\} $ | Fourier optics | Far-field pattern |
| $ L_c = c/\Delta\nu $ | Coherence length | Interferometry |

---

## Problems
1. Calculate the angular resolution of a 10-m telescope at 500 nm. Compare to Hubble (2.4 m).
2. A laser has linewidth 1 MHz. What is its coherence length?
3. Use Jones calculus to find the output of a QWP at 45° followed by a horizontal polarizer for 45° linear input.
4. Find the Fraunhofer pattern of a triangular aperture of base $ b $ and height $  h $.
5. A He-Ne laser ( $ \lambda = 632.8 $ nm) passes through a 0.2 mm slit at 2 m distance. Find the width of the central maximum.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
