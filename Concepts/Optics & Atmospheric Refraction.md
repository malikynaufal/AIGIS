---
tags: [aigis, concept, physics, optics, refraction, geodesy, atmosphere]
created: 2026-07-27
updated: 2026-07-27
---

# Optics & Atmospheric Refraction

## For Geodesy & Geodetic Measurements

**Core Idea:** Optics describes the behavior of light, including refraction, diffraction, and interference. In geodesy, atmospheric refraction is a major systematic error source in angular measurements, level lines, and satellite observations. Understanding optics enables correction of these errors and understanding of optical surveying instruments.

---

## Fundamental Concepts

### Snell's Law of Refraction

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

| Medium | Refractive index $n$ |
|--------|---------------------|
| Vacuum | 1.0000 |
| Air (15°C, 101.3 kPa) | 1.000293 |
| Water | 1.333 |
| Glass (crown) | 1.52 |
| Ice | 1.31 |

**Total internal reflection:** Occurs when $\theta_1 > \theta_c$ where $\sin\theta_c = n_2/n_1$.

### Thin Lens Equation

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

where $f$ = focal length, $d_o$ = object distance, $d_i$ = image distance.

Magnification: $M = -d_i/d_o = h_i/h_o$

### Mirrors

| Surface | Formula |
|---------|---------|
| Flat mirror | Virtual image, same size, reversed |
| Concave | $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$, $f > 0$ |
| Convex | $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$, $f < 0$ |

---

## In Geodesy Context

### Geodetic Refraction

When a line of sight passes through the atmosphere, light rays bend. The geodetic refraction coefficient:

$$k = \frac{R}{R_e}$$

where $R$ = radius of curvature of the light ray, $R_e$ = Earth's radius of curvature.

**Typical values:**

| Condition | $k$ value |
|-----------|-----------|
| Horizontal | 0.13 (standard) |
| Vertical | 0.40 (standard) |
| Near ground (sun-heated) | 0.5–1.5 |
| Through temperature inversion | -0.5 to -1.0 (abnormal) |
| Stellar | 0.14 (astronomical) |

### Refraction in Leveling

**Differential leveling refraction error:**
$$\Delta h_{ref} \approx \frac{k}{2R} \cdot s^2$$

where $s$ = sight distance. For $k = 0.14$ and $s = 100$ m:
$\Delta h_{ref} \approx \frac{0.14}{2 \times 6{,}371{,}000} \times 10{,}000 \approx 0.1$ mm

**Rule of thumb:** Equal foresight and backsight distances cancel refraction.

### Refraction in Electronic Distance Measurement (EDM)

$$\Delta D_{atm} = D\left[\frac{N_0 P}{760} \cdot \frac{273.15}{273.15+T} - 1\right] \cdot 10^{-6}$$

where $N_0$ = refractivity at 0°C, 760 mmHg.

| Wavelength | $N_0$ (ppm) |
|------------|-------------|
| IR (EDM) | 270–280 |
| Visible | 285 |
| GPS L1 | 285 |

### Tropospheric Mapping Functions

The total tropospheric delay is the integral along the signal path:

$$\Delta\rho_{trop} = \int n_{wet}(s)\,ds + \int n_{dry}(s)\,ds$$

Mapping functions map zenith delay to slant delay:

**Simple cosine mapping:** $m(\theta) = 1/\cos\theta = \sec\theta$ (accurate above 20°)

**Niell Mapping Function (NMF):**
$$m(\theta) = \frac{1 + \frac{a}{1+\frac{b}{1+c}}}{\sin\theta + \frac{a}{\sin\theta + \frac{b}{\sin\theta + c}}}$$

where $a, b, c$ depend on station latitude and height.

### Atmospheric Dispersion

Refractive index varies with wavelength:

| Frequency band | Wavelength | Refractivity |
|---------------|------------|--------------|
| GPS L5 | 25.48 cm | ~285.0 ppm |
| GPS L2 | 24.42 cm | ~285.0 ppm |
| GPS L1 | 19.05 cm | ~285.0 ppm |

For GNSS, the atmosphere is essentially non-dispersive at microwave frequencies (unlike the ionosphere, which is dispersive).

### Lens-Based Surveying Instruments

**Theodolite optics:** Collimator lens focuses parallel light rays at focal point. Resolving power:
$$\delta = \frac{1.22\lambda}{D}$$

where $D$ = aperture diameter, $\lambda$ = wavelength. For $\lambda = 550$ nm and $D = 40$ mm: $\delta \approx 1.7$ arcsec.

**EDM prism:** Corner-cube reflector returns light along incident direction regardless of orientation (within ~30°).

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $n_1\sin\theta_1 = n_2\sin\theta_2$ | Snell's law | Refraction at interfaces |
| $k = R/R_e$ | Refraction coefficient | Line-of-sight bending |
| $\Delta h_{ref} = \frac{k}{2R}s^2$ | Refraction error in leveling | Height correction |
| $m(\theta) = 1/\cos\theta$ | Simple mapping | Zenith-to-slant mapping |
| $\delta = 1.22\lambda/D$ | Rayleigh criterion | Resolution limit |

---

## Related Concepts

- [[Electromagnetism & Signal Propagation]] — EM wave theory
- [[Optics & Atmospheric Refraction]] — Atmospheric signal delay
- [[Physical Geodesy]] — Gravity, atmosphere coupling
- [[Least Squares Adjustment]] — Correcting systematic errors

---

## Study Problems

1. **Recall:** A level sight is 120 m long. With refraction coefficient 0.14, compute the refraction error in mm.
2. **Application:** Compute the zenith tropospheric delay from hydrostatic ($ZHD = 2.3$ m) and wet ($ZWD = 0.2$ m) components at elevation angle 15° using simple cosine mapping.
3. **Derivation:** Starting from Snell's law, derive the critical angle for total internal reflection from glass ($n = 1.52$) to air.
4. **Real-world:** An EDM measures 2,040.150 m at temperature 25°C, pressure 1010 hPa. The refractivity is 280 ppm at standard conditions. Estimate the atmospheric correction.

---

## Common Mistakes

1. **Confusing refraction in light vs. radio:** Same physics, very different magnitude — optical refraction is much stronger.
2. **Assuming refraction is always positive:** Temperature inversions cause negative (abnormal) refraction.
3. **Ignoring elevation dependence:** Refraction mapping functions diverge at low elevations ($\theta < 10°$).
4. **Using constant $k$ for all conditions:** $k$ varies with time, weather, and terrain.
5. **Mixing up group and phase refraction:** For GNSS, group delay and phase advance are equal magnitude, opposite sign.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*