---
tags: [aigis, concept, physics, waves, oscillations, signal processing]
created: 2026-07-27
updated: 2026-07-27
---

# Waves & Oscillations

## For Geodesy, GNSS, and Signal Processing

**Core Idea:** Waves describe periodic disturbances that propagate energy without mass transport. In geodesy, waves include seismic waves (monitoring tectonic deformation), ocean waves (affecting sea level), and electromagnetic waves (GNSS signals). Signal processing extracts information from wave observations.

---

## Fundamental Concepts

### Simple Harmonic Motion (SHM)

$$ x(t) = A\cos(\omega t + \phi) $ $

 | Quantity | Symbol | Units | Meaning |
|----------|--------|-------|---------|
| Amplitude | $ A $ | m | Maximum displacement |
| Angular frequency | $ \omega $ | rad/s | $ \omega = 2\pi f $ |
| Frequency | $ f $ | Hz = 1/s | Cycles per second |
| Period | $ T $ | s | $ T = 1/f = 2\pi/\omega $ |
| Phase | $ \phi $ | rad | Initial condition |

**SHM differential equation:*
*

$ $ \ddot{x} + \omega_0^2 x = 0

$ Solution: $ x(t) = A\cos(\omega_0 t + \phi) $**Damped oscillation:*$
*

$ $ \ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0

$$

| Damping | Condition | Solution |
|---------|-----------|----------|
| Underdamped | $ \gamma < \omega_0 $ | $ x = e^{-\gamma t}(A\cos\omega_d t + B\sin\omega_d t) $ |
| Critically damped | $ \gamma = \omega_0 $ | $ x = (A+Bt)e^{-\omega_0 t} $ |
| Overdamped | $ \gamma > \omega_0 $ | $ x = Ae^{r_1 t} + Be^{r_2 t} $ |

where $ \omega_d = \sqrt{\omega_0^2 - \gamma^2} $.

### Wave Equation

The 1D wave equation:

$ $ \frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2} $$

**General solution:**$ y(x,t) = f(x - vt) + g(x + vt) $ | Wave Type | Speed | Medium |
|-----------|-------|--------|
| Sound | $ v = \sqrt{B/\rho} $ | Fluids, solids |
| EM wave | $ v = c/n $ | Any medium |
| Seismic (P-wave) | $ v_P = \sqrt{(\lambda+2\mu)/\rho} $ | Earth's interior |
| Seismic (S-wave) | $ v_S = \sqrt{\mu/\rho} $ | Earth's interior |
| Gravity wave | $ v = \sqrt{g/k\tanh(kh)} $ | Ocean surface |

### Superposition & Interference

**Constructive:**$ \Delta \phi = 2m\pi $ (amplitudes add)
**Destructive:**$ \Delta \phi = (2m+1)\pi $ (amplitudes subtract)

### Beats

Two waves of slightly different frequencies

$ y = 2A\cos\left(\frac{\omega_1 - \omega_2}{2}t\right)\cos\left(\frac{\omega_1 + \omega_2}{2}t\right) $Beat frequency: $ f_{beat} = |f_1 - f_2| $### Doppler Effec
t

$ f_{obs} = f_0 \frac{v \pm v_{obs}}{v \mp v_{source}} $ $ **GNSS application:** Satellite motion shifts the received frequency. For GPS satellite velocity ~3.9 km/s $

$$ \frac{\Delta f}{f} \approx \frac{v_{sat}}{c} \approx \frac{3900}{3\times10^8} \approx 13\ \mu\text{s} $ $

---

## Fourier Series (Applied)

Any periodic function with period $ T $ decomposes

$ $ f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[a_n\cos(n\omega_0 t) + b_n\sin(n\omega_0 t)\right] $$

where $\omega_0 = 2\pi/T $:

$ a_0 = \frac{2}{T}\int_0^T f(t)\,dta_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t)\,dtb_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t)\,dt $ $ | Function | First 5 harmonic coefficients |$
|----------|-------------------------------|
| Square wave | $ \frac{4A}{\pi}\sum_{n=1,3,5,\dots} \frac{1}{n}\sin(n\omega t) $ |
| Sawtooth | $ \frac{2A}{\pi}\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}\sin(n\omega t) $ |
| Triangle wave | $ \frac{8A}{\pi^2}\sum_{n=1,3,5,\dots} \frac{(-1)^{(n-1)/2}}{n^2}\sin(n\omega t) $ |

---

## In Geodesy & GNSS Context

### Tidal Harmonic Analysis

Earth tides are decomposed into tidal constituents:

| Constituent | Period | Source | Amplitude (vertical, max) |
|-------------|--------|--------|---------------------------|
| M₂ | 12.42 h | Lunar semi-diurnal | ~0.3 m |
| S₂ | 12.00 h | Solar semi-diurnal | ~0.15 m |
| K₁ | 23.93 h | Lunar diurnal | ~0.1 m |
| O₁ | 25.82 h | Solar diurnal | ~0.05 m |
| N₂ | 12.66 h | Lunar elliptical | ~0.03 m |

These are fit using least-squares to find amplitudes and phases from time series.

### Seismic Wave Analysis

| Wave Type | Speed (typical) | Use |
|-----------|-----------------|-----|
| P-wave (compressional) | 5–8 km/s | Early warning |
| S-wave (shear) | 3–4.5 km/s | Structural studies |
| Surface waves (Love, Rayleigh) | 2–4 km/s | Damage assessment |

### Signal Leakage & Windowing

**Window functions** reduce spectral leakage when sampling finite signals:

| Window | Main lobe width | Side lobe level |
|--------|----------------|----------------|
| Rectangular (no window) | 2N | -13 dB |
| Hann | 5N | -31 dB |
| Hamming | 5N | -41 dB |
| Blackman | 7N | -58 dB |

### GPS Signal Processing

GPS L1 carrier at 1575.42 MHz with chipping rate 1.023 MHz (C/A code). The cross-correlation

$ $ R(\tau) = \int s(t) \cdot s(t-\tau)\,dt $$

peaks when $ \tau $ matches the code delay — used for ranging.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $x(t) = A\cos(\omega t + \phi) $ | SHM | Oscillations |
| $ \ddot{x} + \omega_0^2 x = 0 $ | SHM ODE | Free oscillation |
| $ \frac{\partial^2 y}{\partial t^2} = v^2\frac{\partial^2 y}{\partial x^2} $ | Wave equation | Wave propagation |
| $ f_{obs} = f_0 \frac{c}{c - v_s} $ | Doppler | Moving satellite |
| $ a_n = \frac{2}{T}\int f\cos(n\omega_0 t) $ | Fourier | Signal decomposition |
| $ R(\tau) = \int s(t)s(t-\tau)dt $ | Cross-correlation | GPS ranging |

---

## Related Concepts

- [[Newtonian Mechanics]] — SHM from harmonic restoring forces

- [[Electromagnetism & Signal Propagation]] — EM waves, Fourier of signals

- [[Differential Equations intro]] — Solving wave/oscillation ODEs

- [[Error Propagation]] — Noise in wave measurements

- [[Least Squares Adjustment]] — Tidal harmonic estimation

---

## Study Problems

1. **Recall:** A mass-spring system has $ k = 100 $ N/m, $ m = 1 $ kg. Find $ \omega_0 $, $ T $, and $ f $. (Answer: $ \omega_0 = 10 $ rad/s, $ T = 0.628 $ s, $ f = 1.59 $ Hz.)
2. **Application:** A tidal record has 30 days at 60 s cadence. Can it resolve M₂ (12.42 h period) from S₂ (12.00 h period)? (Hint: compute Nyquist and frequency resolution.)
3. **Derivation:** Derive the damped frequency $ \omega_d = \sqrt{\omega_0^2 - \gamma^2} $ from $ \ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$.
4. **Real-world:** A GNSS signal at L1 propagates through the troposphere. The wet delay varies diurnally. The signal is sampled for 24 hours at 1 Hz. What's the lowest frequency you can resolve, and would you be able to see the diurnal (1 cycle/24h ≈ 116 μHz) component?

---

## Common Mistakes

1. **Confusing angular frequency $ \omega $ with frequency $ f $:** $ \omega = 2\pi f $, not $ \omega = f$.
2. **Sign in Doppler:** Approaching → higher frequency, receding → lower.
3. **Confusing phase velocity and group velocity** in dispersive media.
4. **Ignoring leakage** in DFT — always window spectral data unless the observation window is an integer multiple of the period.
5. **Mixing up P-waves and S-waves:** P is faster, S cannot travel through liquids.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*