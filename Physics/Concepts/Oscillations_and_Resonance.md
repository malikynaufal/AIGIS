---
tags: [aigis, concept, physics, oscillations, resonance, vibrations]
created: 2026-07-27
updated: 2026-07-27
---

# Oscillations \u0026 Resonance

## Damped, Forced Oscillations, Quality Factor

**Core Idea:** Oscillatory systems exchange energy between kinetic and potential forms. Damping dissipates energy; driving forces can produce resonance.

---

## 1. Simple Harmonic Motion (SHM)

### Equation of Motion
$$

\frac{d^2x}{dt^2} + \omega_0^2 x = 0$$### Solution$$x(t) = A\cos(\omega_0 t + \phi)$$where$\omega_0 = \sqrt{k/m}$(natural angular frequency).

### Energy

- Kinetic:$K = \frac{1}{2}mv^2 = \frac{1}{2}m\omega_0^2 A^2 \sin^2(\omega_0 t + \phi)$- Potential:$U = \frac{1}{2}kx^2 = \frac{1}{2}m\omega_0^2 A^2 \cos^2(\omega_0 t + \phi)$- Total:$E = \frac{1}{2}m\omega_0^2 A^2$(constant)

---

## 2. Damped Oscillations

### Equation of Motion$$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0
$$

### Underdamped ($b^2 < 4mk$, i.e., $\gamma < \omega_0$)
$$

x(t) = A e^{-\gamma t}\cos(\omega_d t + \phi)$$where:
-$\gamma = b/(2m)$(damping coefficient)
-$\omega_d = \sqrt{\omega_0^2 - \gamma^2}$(damped frequency)
-$\omega_d < \omega_0$ always

### Critically Damped ($b^2 = 4mk$)
Fastest return to equilibrium without oscillation.
$$x(t) = (A + Bt)e^{-\gamma t}$$

### Overdamped ($b^2 > 4mk$)
Slow exponential return, no oscillation.

### Quality Factor $Q$
$$

Q = \frac{\omega_0}{2\gamma} = \frac{\omega_0 m}{b}$$Higher$Q$→ less damping → more oscillations before decay.

|$Q$Value | Description |
|-----------|-------------|
|$Q \approx 0.5$| Critically damped |
|$Q \approx 1-10$| Lightly damped |
|$Q \approx 10-100$| Good resonance |
|$Q \approx 10^3-10^6$| Very low loss (lasers, atoms) |

---

## 3. Forced Oscillations and Resonance

### Equation of Motion (Driving Force)$$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = F_0\cos(\omega t)$$### Ste-State Solution$$x(t) = A(\omega)\cos(\omega t - \delta)$$### Amplitude Response$$A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\gamma\omega)^2}}$$### Phase Response$$\tan\delta = \frac{2\gamma\omega}{\omega_0^2 - \omega^2}$$### Resonance
Maximum amplitude at:$$\omega_{\text{res}} = \sqrt{\omega_0^2 - 2\gamma^2} \quad \text{(amplitude resonance)}
$$

For small damping ($\gamma \ll \omega_0$): $\omega_{\text{res}} \approx \omega_0$Maximum amplitude at resonance:$$A_{\text{max}} = \frac{F_0}{2\gamma m\omega_0} = \frac{Q \cdot F_0}{m\omega_0^2}$$### Power Absorption$$P(\omega) = \frac{F_0^2}{2b}\frac{\gamma^2}{\gamma^2 + (\omega-\omega_0)^2} \quad \text{(Lorentzian, near resonance)}$$Full width at half-maximum (FWHM):$\Delta\omega = 2\gamma = \omega_0/Q$---

## 4. Coupled Oscillations

### Two Coupled Oscillators$$m_1\ddot{x}_1 = -k_1 x_1 - k_{12}(x_1 - x_2)
$$

$$
m_2\ddot{x}_2 = -k_2 x_2 + k_{12}(x_1 - x_2)$$### Normal Modes
Solutions are superpositions of normal modes:$$x_i(t) = A_i e^{i\omega_\alpha t + \phi_\alpha}$$For$m_1 = m_2 = m$and$k_1 = k_2 = k$:

- **In-phase mode:** $\omega_+ = \sqrt{k/m}$(center of mass oscillates)

- **Out-of-phase mode:**$\omega_- = \sqrt{(k+2k_{12})/m}$(centers move oppositely)

---

## 5. Applications

### Geophysics
| Application | Type |
|-------------|------|
| Seismic waves | Elastic oscillations of Earth |
| Atmospheric tides | Forced oscillation by Moon/Sun |
| Pendulum gravimeters | SHM measurement of gravity |
| Resonance of GNSS satellites | Orbital resonance |

### Everyday Examples
| System |$\omega_0$| Typical$Q$|
|--------|-----------|-------------|
| Clock pendulum |$2\pi/1$ s$^{-1}$|$10^3$|
| Guitar string |$2\pi f$(100-1000 Hz) |$10^2-10^3$|
| LC circuit |$1/\sqrt{LC}$|$10^2-10^4$|
| Quartz crystal |$2\pi \times 32768$Hz |$10^4-10^5$|

---

## 6. Key Equations Summary

| Formula | Name | Use |
|---------|------|-----|
|$\omega_0 = \sqrt{k/m}$| Natural frequency | SHM |
|$\omega_d = \sqrt{\omega_0^2 - \gamma^2}$| Damped frequency | Damped oscillation |
|$Q = \omega_0/(2\gamma)$| Quality factor | Damping measure |
|$A_{\text{res}} = Q F_0/(m\omega_0^2)$| Resonance amplitude | Maximum response |
|$\Delta\omega = \omega_0/Q$ | Bandwidth | Resonance sharpness |

---

## Study Problems
1. A 2 kg mass on a spring ($k = 200$N/m) has damping coefficient$b = 2$N·s/m. Find$\omega_0$, $\gamma$, $\omega_d$, and $Q$.
2. A driven oscillator has $Q = 50$, natural frequency 100 Hz. At what frequency range (FWHM) does the amplitude exceed half-maximum?
3. Show that the average power dissipated equals the average power supplied at resonance.
4. Two coupled pendulums (equal mass, connected by spring). Find normal mode frequencies if $k_{12}/k = 0.1$.
5. An earthquake produces ground oscillations at 0.5 Hz with amplitude 2 mm. A building has natural frequency 0.5 Hz and $Q = 5$. Find the resonance amplification factor.

---

## References

- OpenStax University Physics Vol. 1 (Ch. 15: Oscillations)

- Morin, "Introduction to Classical Mechanics" (Ch. 10)

- Feynman Lectures Vol. I (Ch. 22-23)

- Landau & Lifshitz, "Mechanics" (Ch. 5)

- MIT OCW 8.03: Vibrations and Waves

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
