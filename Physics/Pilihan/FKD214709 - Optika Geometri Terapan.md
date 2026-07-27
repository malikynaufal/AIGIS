---
title: "Optika Geometri Terapan"
subject: "Fisika Pilihan"
tags:
 - optics
 - geometric-optics
 - telescopes
 - surveying-instruments
 - SKS: 3
---

# FKD214709 — Optika Geometri Terapan
**Applied Geometric Optics** | 3 SKS (Satuan Kredit Semester)

## Overview

Applied geometric optics (optika geometri terapan) extends the fundamentals of ray optics to the design and analysis of optical instruments used in geodetic surveying, remote sensing, and metrology. Students will master lens systems (sistem lensa), refraction in prisms, telescopes (teleskop), automatic leveling instruments (instrumen nivo), and photogrammetric cameras (kamera fotogrametri). The course bridges classical optics with modern instrument engineering, emphasizing the error budgets and calibration procedures required for precision measurement.

---

## 1. Review of Ray Optics (Ulasan Optika Berkas Sinar)

### 1.1 Snell's Law and Refraction

At an interface between media with refractive indices $n_1 $ and $n_2 $:

$ n_1 \sin\theta_1 = n_2 \sin\theta_2 $The apparent depth of an object at real depth $ d $ viewed from above $ d_{\text{apparent}} = \frac{d \cdot n_2}{n_1} $ $

### 1.2 Thin Lens Equation

For a thin lens with focal length $ f $:

$ $ \frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} $$

where $ d_o $is object distance (jarak objek) and $ d_i $is image distance (jarak bayangan). The magnification $ M = -\frac{d_i}{d_o} = \frac{h_i}{h_o} $ $

### 1.3 Thick Lens and Lensmaker's Equation

For a thick lens with radii $ R_1 $, $ R_2 $, thickness $ t $, and refractive index $ n $:

$ $ \frac{1}{f} = (n-1)\left[\frac{1}{R_1} - \frac{1}{R_2} + \frac{(n-1)t}{nR_1R_2}\right]

$$ ---

## 2. Lens Systems and Aberrations (Sistem Lensa dan Aberasi)

### 2.1 Gaussian Beam Optics

For laser-based instruments (leveling lasers, laser rangefinders), Gaussian beam propagation is more appropriate than ray optics

$ $ w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2} $$

where $ w_0 $is the beam waist (pinggang berkas), $ z_R = \pi w_0^2/\lambda $is the Rayleigh range, and $ w(z) $is the beam radius at distance $ z$.

### 2.2 Optical Aberrations (Aberasi Optik)

Real lenses introduce image distortions. The five Seidel aberrations:

| Aberration (Aberasi) | Description (Deskripsi) | Correction |
|---|---|---|
| Spherical (sferis) | Marginal rays focus closer than paraxial | Aspheric surface, doublet |
| Coma (koma) | Off-axis point → comet shape | Stop at front focal plane |
| Astigmatism (astigmatisme) | Tangential & sagittal focus differ | Symmetric lens design |
| Field curvature (kelengkungan bidang) | Focal surface is curved, not flat | Field flattener lens |
| Distortion (distorsi) | Straight lines appear curved | Symmetric doublet design |

### 2.3 Achromatic Doublet

An achromatic doublet (lensa achromatik) combines crown glass ( $n_1 $, low dispersion, Abbe number $ V_1 > 50 $) and flint glass ( $ n_2 $, high dispersion, $ V_2 < 40 $):

$ $ \frac{1}{f_1} + \frac{1}{f_2} = \frac{1}{f_{\text{total}}
}

$ Achromatic condition (kondisi achromatik): $$ \frac{1}{V_1 f_1} + \frac{1}{V_2 f_2} = 0

$ $

This eliminates chromatic aberration (aberasi kromatik) at two wavelengths.

---

## 3. Telescopes (Teleskop)

### 3.1 Refracting Telescope (Teleskop Refraktor)

The Keplerian telescope consists of an objective lens ( $f_o $) and eyepiece ( $ f_e $):

$ $ \text{Magnification} = M = -\frac{f_o}{f_e
}

$ The angular resolution (resolusi sudut) is limited by diffraction: $$ \theta_{\min} = 1.22 \frac{\lambda}{D}

$ where $D $ is the aperture diameter. For $ D = 10 $cm at $ \lambda = 550 $ nm: $ \theta_{\min} = 1.4 \times 10^{-6} $ rad $ = 0.28 $ arcsec.

### 3.2 Reflecting Telescope (Teleskop Reflektor)

Newtonian reflectors use a parabolic primary mirror

$z = \frac{r^2}{4f} $ $

Advantages: no chromatic aberration, larger apertures achievable. The 2.4-m capacity of a reflector at Bosscha Observatory (Observatorium Bosscha) in Lembang enables variable star monitoring (pengamatan bintang variabel).

### 3.3 Schmidt and Maksutov Cameras

Wide-field cameras used in satellite tracking and astrometry:

- **Schmidt camera**: Spherical primary mirror + corrector plate at center of curvature

- **Maksutov**: All-spherical optics; thicker but more compact

Field of view: Schmidt up to 5°–10°, Maksutov up to 2°–3°.

---

## 4. Leveling Instruments (Instrumen Nivo)

### 4.1 Optical Level (Nivo Optik)

An automatic level uses a compensator (kompensator) — a pendulum-mounted prism — to maintain horizontal line of sight (garis pandang horizontal) despite tilt

$h = (a - b) + \text{curvature-refraction correction} **Curvature and refraction correction**

c_r = 0.0675 \cdot d^2 \;\text{(m)} $$ where $ d $ is the sight distance in km. For $ d = 100 $m: $ c_r = 0.7 $mm.

### 4.2 Digital Level (Nivo Digital)

Digital levels (e.g., Leica DNA03, Trimble DiNi) read a barcoded staff (staff berkode batang) using image correlation

$h = \text{digital reading} - \text{benchmark elevation} $ $

Precision: 0.3 mm/km (double-run) — comparable to first-order leveling.

### 4.3 Precision Table

| Instrument Type | Precision (mm/km) | Application |
|---|---|---|
| Dumpy level | 2–3 | Construction leveling |
| Automatic level | 1–2 | Engineering survey |
| Digital level | 0.3–0.7 | Geodetic leveling |
| Invar wire leveling | 0.1 | Monitoring, tectonic |
| GNSS heighting | 5–20 | Geometric leveling replacement |

---

## 5. Photogrammetric Cameras (Kamera Fotogrametri)

### 5.1 Interior Orientation

The collinearity equations (persamaan kolinearitas) relate image coordinates $(x, y) $ to ground coordinates $(X, Y, Z)$:

$ x = x_0 - f \frac{a_1(X - X_0) + b_1(Y - Y_0) + c_1(Z - Z_0)}{a_3(X - X_0) + b_3(Y - Y_0) + c_3(Z - Z_0)}y = y_0 - f \frac{a_2(X - X_0) + b_2(Y - Y_0) + c_2(Z - Z_0)}{a_3(X - X_0) + b_3(Y - Y_0) + c_3(Z - Z_0)} $where $ (x_0, y_0) $ is the principal point, $f $ is focal length, and $ a_i, b_i, c_i $are rotation matrix elements.

### 5.2 Case Study: Aerial Survey of Jakarta

A drone-based photogrammetric survey of Jakarta's coastline uses a calibrated camera (focal length 15.4 mm, pixel size 2.4 μm) flying at 200 m AGL:

- Ground sampling distance (GSD): $0.068 $ m/pixel

- Horizontal accuracy: $ \pm 0.1 $ m (with GCPs)

- Vertical accuracy: $ \pm 0.15 $ m (supports coastal flood mapping — pemetaan banjir pesisir)

- Overlap: 80% forward, 60% lateral

Bundle adjustment (penyesuaian bundel) using Agisoft Metashape processes ~5000 images with 50 ground control points, producing a DEM with 0.1 m resolution.

---

## References

1. Hecht, E. (2017). *Optics*, 5th ed. Pearson.
2. Ghosh, S. K. (1988). *Analytical Photogrammetry*, 2nd ed. Pergamon Press.
3. Wolf, P. R., Dewitt, B. A., & Wilkinson, B. E. (2014). *Elements of Photogrammetry with Applications in GIS*, 4th ed. McGraw-Hill.
4. Mikš, A., & Novák, P. (2012). "Influence of lens aberrations on the imaging," *Opt. Eng.*, 51(5), 053201.
5. Luhmann, T. et al. (2020). *Close-Range Photogrammetry and 3D Imaging*, 3rd ed. De Gruyter.
6. Bosscha Observatory (2021). "Instrumentation Report." Institut Teknologi Bandung.
