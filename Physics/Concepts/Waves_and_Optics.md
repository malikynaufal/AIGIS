---
tags: [aigis, concept, physics, waves, optics]
created: 2026-07-27
updated: 2026-07-27
---

# Waves \u0026 Optics

## Wave Equation, Interference, Diffraction, Polarization

**Core Idea:** Waves transfer energy without transferring matter. The wave equation describes propagation; interference and diffraction reveal wave nature; polarization reveals transverse nature.

---

## 1. Wave Equation and Solutions

### One-Dimensional Wave Equation

$$ \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} $$ where $v$ = wave speed,$y(x,t) $= displacement.

### General Solution (d'Alembert
)

$$ y(x,t) = f(x - vt) + g(x + vt) $$

-$f$ = right-traveling wave
-$g$ = left-traveling wave

### Harmonic Wav
e

$$ y(x,t) = A \cos(kx - \omega t + \phi) $$ where:
-$A$ = amplitude
- $k = 2\pi/\lambda$= wave number
-$ \omega = 2\pi f$= angular frequency
-$ \phi$= phase constant
- $v = \omega/k = \lambda f$---

## 2. Superposition and Interference

### Principle of Superposition
When waves overlap, the resultant displacement is the algebraic sum

$y_{\text{total}}(x,t) = \sum_i y_i(x,t) $$$

### Constructive Interference
Waves in phase: $ \Delta \phi = 2\pi n$

$A_{\text{total}} = A_1 + A_2 $$$

### Destructive Interference
Waves out of phase: $ \Delta \phi = (2n+1)\pi$

$$

A_{\text{total}} = |A_1 - A_2| $$

### Double-Slit Interference (Young's Experiment)
Path difference: $ \Delta r = d\sin\theta$- Bright fringes: $d\sin\theta = m\lambda$- Dark fringes: $d\sin\theta = (m+\frac{1}{2})\lambda$**Fringe spacing:**$ \Delta y = \frac{\lambda L}{d} $ (small angle)

---

## 3. Diffraction

### Single-Slit Diffraction (Fraunhofer)
Intensity pattern

$$ I(\theta) = I_0 \left(\frac{\sin\beta}{\beta}\right)^2, \quad \beta = \frac{\pi a \sin\theta}{\lambda} $$ Minima: $$ a\sin\theta = m\lambda \quad (m = \pm1, \pm2, \dots) $### Diffraction Grating$
Multiple slits: $N$ slits of width $a$, separation $d$ Principal maxima: $d\sin\theta = m\lambda$**Angular dispersion:**$ \frac{d\theta}{d\lambda} = \frac{m}{d\cos\theta} $**Resolving power:** $R = \frac{\lambda}{\Delta\lambda} = mN$---

## 4. Polarization

### Types of Polarization
| Type | Electric Field Behavior |
|------|------------------------|
| Linear | $ \vec{E}$oscillates along fixed line |
| Circular | $ \vec{E}$rotates in circle |
| Elliptical | $ \vec{E}$traces ellipse |

### Malus's Law (Linear Polarizer
)

$I = I_0 \cos^2\theta $ where $\theta$ = angle between polarization direction and transmission axis.

### Brewster's Angle
Reflected light perfectly polarized (s-polarized) when

$$ \tan\theta_B = \frac{n_2}{n_1} $$

### Jones Calculus (Matrix Representation)
| Component | Jones Vector |
|-----------|--------------|
| Horizontal | $ \begin{pmatrix}1\\0\end{pmatrix}$ |
| Vertical | $ \begin{pmatrix}0\\1\end{pmatrix}$ |
| 45° Linear | $ \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$ |
| Right Circular | $ \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix} $ |

Polarizers and wave plates are $2\times2$ matrices.

---

## 5. Electromagnetic Waves (Refresher)

### Wave Equation in Vacuu
m

$$ \nabla^2\vec{E} = \mu_0\epsilon_0\frac{\partial^2\vec{E}}{\partial t^2} $$

### Speed of Ligh
t

$c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998\times10^8 \text{ m/s} $$$

### In a Mediu
m

$v = \frac{c}{n}, \quad n = \sqrt{\epsilon_r\mu_r} $$$

---

## 6. Fourier Optics (Introduction)

### Fourier Transform in Optics
Fraunhofer diffraction pattern is the **Fourier transform** of the aperture function

$$ U(x,y) = \mathcal{F}\{A(\xi,\eta)\} $$

### Example: Rectangular Apertur
e

$$ U(x,y) \propto \text{sinc}\left(\frac{\pi a x}{\lambda z}\right)\text{sinc}\left(\frac{\pi b y}{\lambda z}\right) $$

---

## 7. Lasers (Basics)

### Principles

- Population inversion

- Stimulated emission

- Optical cavity (feedback)

### Common Laser Types
| Type | Wavelength | Application |
|------|------------|-------------|
| He-Ne | 632.8 nm | Alignment, holography |
| Nd:YAG | 1064 nm | LIDAR, machining |
| Diode | 780–1550 nm | Telecom, sensors |
| Fiber | 1550 nm | GNSS carrier phase |

---

## 8. Key Equations Summary

| Formula | Name | Use |
|---------|------|-----|
| $y(x,t) = A\cos(kx-\omega t+\phi) $ | Harmonic wave | General wave description |
| $d\sin\theta = m\lambda$ | Double-slit maxima | Interference |
| $I(\theta) = I_0(\sin\beta/\beta)^2$ | Single-slit diffraction | Diffraction envelope |
| $d\sin\theta = m\lambda$ | Grating equation | Spectroscopy |
| $I = I_0\cos^2\theta$ | Malus's law | Polarizer transmission |
| $ \tan\theta_B = n_2/n_1$ | Brewster's angle | Polarized reflection |
| $R = mN$ | Grating resolution | Spectral resolution |

---

## 9. Worked Examples

### Example 1: Double Slit Fringes$ \lambda = 632.8 $nm, $d = 0.2 $mm, $L = 2 $m
.

$$ \Delta y = \frac{\lambda L}{d} = \frac{632.8\times10^{-9} \times 2}{0.2\times10^{-3}} = 6.33 \text{ mm} $$

### Example 2: Diffraction Limit of Telescope
Aperture $D = 2.4 $m (Hubble),$ \lambda = 500 $nm
.

$$ \theta_{\text{min}} = 1.22\frac{\lambda}{D} = 1.22 \times \frac{500\times10^{-9}}{2.4} = 0.25 \text{ arcsec} $$

---

## Study Problems
1. Derive the intensity distribution for two-slit interference with finite slit width $a$ and separation $d$.
2. A diffraction grating has 500 lines/mm. What is the angular separation between 500 nm and 501 nm in first order?
3. Calculate the Brewster angle for light going from air ($n=1$) to water ($n=1.33$).
4. Use Jones calculus to find the output polarization after a quarter-wave plate at 45° to linear polarization.
5. Estimate the coherence length of a He-Ne laser with linewidth$ \Delta\nu = 1 $MHz.

---

## References

- Hecht, "Optics" (5th ed.)

- Saleh \u0026 Teich, "Fundamentals of Photonics"

- OpenStax University Physics Vol. 3 (Ch. 3-4)

- MIT OCW 8.03: Vibrations and Waves

- Feynman Lectures Vol. I (Ch. 28-35)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
