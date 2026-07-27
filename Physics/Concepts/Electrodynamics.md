---
tags: [physics, concept, aigis, electromagnetism, waves, earth, geophysics]
created: 2026-07-27
updated: 2026-07-27
---

# Electrodynamics

## Maxwell's Equations and Applications in Geodesy

**Core idea:** Electrodynamics describes the relationship between electric and magnetic fields, their generation by charges and currents, and their propagation as electromagnetic waves. These principles are fundamental to GNSS signal propagation, remote sensing, and satellite communications.

---

## 📚 Core Concept

Electrodynamics is governed by **Maxwell's Equations**, the unified theory of electricity, magnetism, and light:

| Equation | Name | Physical Meaning |
|----------|------|-----------------|
| $\nabla \cdot \mathbf{D} = \rho_f$ | Gauss's Law (Electric) | Electric charges produce electric fields |
| $\nabla \cdot \mathbf{B} = 0$ | Gauss's Law (Magnetic) | No magnetic monopoles exist |
| $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | Faraday's Law | Changing magnetic fields induce electric fields |
| $\nabla \times \mathbf{H} = \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t}$ | Ampère-Maxwell Law | Electric currents and changing electric fields produce magnetic fields |

### Constitutive Relations

In a medium:
$$\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mathbf{J} = \sigma \mathbf{E}$$

where $\varepsilon = \varepsilon_0 \varepsilon_r$ is permittivity, $\mu = \mu_0 \mu_r$ is permeability, and $\sigma$ is conductivity.

---

## 🧮 Key Equations

### Electromagnetic Wave Equation

In free space ($\rho_f = 0, \mathbf{J}_f = 0$):

$$\nabla^2 \mathbf{E} - \mu_0\varepsilon_0\frac{\partial^2 \mathbf{E}}{\partial t^2} = 0$$

$$\nabla^2 \mathbf{B} - \mu_0\varepsilon_0\frac{\partial^2 \mathbf{B}}{\partial t^2} = 0$$

### Speed of Light

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 2.998 \times 10^8\,\text{m/s}$$

### Wave Propagation for GNSS

GNSS signals propagate at speed $c$ in vacuum, but in the ionosphere:

$$v_{\text{phase}} = \frac{c}{n}, \quad n = \sqrt{1 - \frac{\omega_p^2}{\omega^2}}$$

where $\omega_p = \sqrt{\frac{N_e e^2}{\varepsilon_0 m_e}}$ is the **plasma frequency** (critical frequency of the ionosphere).

### Electromagnetic Spectrum

| Band | Frequency | Wavelength | Geodesy Application |
|------|-----------|------------|---------------------|
| L-band (GPS, Galileo) | 1–2 GHz | 15–30 cm | GNSS positioning |
| C-band (Radar) | 4–8 GHz | 3.75–7.5 cm | Satellite radar altimetry |
| X-band (SAR) | 8–12 GHz | 2.5–3.75 cm | Synthetic Aperture Radar |
| Ku-band (Altimetry) | 12–18 GHz | 1.67–2.5 cm | Radar altimetry |
| Optical | $10^{14}$ Hz | 0.4–0.7 $\mu$m | Satellite laser ranging |

### Wave Parameters for GNSS

| Parameter | Formula | Value for GPS L1 |
|-----------|---------|-----------------|
| Frequency | $f$ | 1575.42 MHz |
| Wavelength | $\lambda = c/f$ | $19.04$ cm |
| Wavenumber | $k = 2\pi/\lambda$ | $33.01$ m$^{-1}$ |
| Angular frequency | $\omega = 2\pi f$ | $9.90 \times 10^9$ rad/s |

---

## 🌍 Geodesy Applications

### Ionospheric Delay

GNSS signals experience **group delay** and **phase advance** when passing through the ionosphere:

**Phase delay (excess path length):**
$$\Delta\Phi = -\frac{40.3}{cf^2} \cdot \text{TEC}$$

**Group delay (pseudorange delay):**
$$\Delta P = +\frac{40.3}{f^2} \cdot \text{TEC}$$

where **TEC** (Total Electron Content) = $\int N_e \, ds$, measured in TECU ($10^{16}$ e/m²).

### Faraday Rotation

Propagation through the ionospheric plasma rotates the polarization plane:

$$\Delta\psi = \frac{e^3}{8\pi^2\varepsilon_0 m_e^2 c f^2} \int N_e B \cos\theta \, ds$$

---

## 🔧 Worked Examples

### Example 1: Ionospheric Delay on L-band

For a GNSS signal at $f = 1.575\,\text{GHz}$ with TEC = 30 TECU:

$$\Delta P = \frac{40.3 \times (30 \times 10^{16})}{(1.575 \times 10^9)^2} = \frac{1.209 \times 10^{19}}{2.481 \times 10^{18}} \approx 4.87\,\text{m}$$

This means the ionosphere delays the signal by $\approx 5$ meters — a significant effect that must be corrected using dual-frequency measurements.

### Example 2: Plasma Frequency in Ionosphere

For an ionospheric layer with $N_e = 10^{12}\,\text{e/m}^3$:

$$f_p = \frac{\omega_p}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{10^{12} \times (1.602 \times 10^{-19})^2}{8.85 \times 10^{-12} \times 9.11 \times 10^{-31}}} \approx 9\,\text{MHz}$$

This is below the GNSS L-band frequency, so signals propagate through the ionosphere.

---

## 📖 Indonesian Glosses

| Term | Indonesian | English |
|------|-----------|---------|
| Medan listrik | Electric field | $\mathbf{E}$ (V/m) |
| Medan magnet | Magnetic field | $\mathbf{B}$ (T) |
| Gelombang elektromagnetik | Electromagnetic wave | Propagating $\mathbf{E}$ and $\mathbf{B}$ |
| Ionosfer | Ionosphere | Ionized layer 60–1000 km |
| Plasma | Plasma | Ionized gas of free electrons and ions |
| TEC (Kandungan Elektron Total) | Total Electron Content | $\int N_e\,ds$ (TECU) |

---

## 🔗 Links

- **Related:** [[Magnetostatics]] · [[EM_Wave_Propagation]]
- **Geodesy:** [[Ionospheric Delay]] · [[Signal_Processing]]
- **External:** OpenStax · MIT OCW

---

## References

1. **OpenStax University Physics Vol. 2** — Chapters on Electromagnetism. [https://openstax.org/details/books/university-physics-volume-2](https://openstax.org/details/books/university-physics-volume-2)
2. **MIT OCW 8.07 Electromagnetism II** — [https://ocw.mit.edu/courses/8-07-electromagnetism-ii-fall-2012/](https://ocw.mit.edu/courses/8-07-electromagnetism-ii-fall-2012/)
3. **Kursinski et al. (1997)** — "Observing Earth's atmosphere with GPS." J. Geophys. Res. [https://doi.org/10.1029/97JD00515](https://doi.org/10.1029/97JD00515)
4. **Langley (1998)** — "Propagation of the GPS Signals." GPS World, Vol. 9.
5. **IGS Atmosphere Working Group** — [https://igscb.bkg.bund.de/](https://igscb.bkg.bund.de/)

---

*Concept maintained by AIGIS — last updated 2026-07-27*
