---
title: "Pemodelan Fisika Bumi"
subject: "Fisika Pilihan"
tags:
  - earth-physics
  - plate-tectonics
  - seismology
  - gravity-modeling
  - SKS: 3
---

# FKD214708 — Pemodelan Fisika Bumi
**Earth Physics Modeling** | 3 SKS (Satuan Kredit Semester)

## Overview

Earth physics modeling (pemodelan fisika bumi) applies the principles of classical mechanics, thermodynamics, and wave physics to understand the interior structure, dynamics, and surface processes of our planet. This course covers plate tectonics (lempeng tektonik), heat flow (aliran panas), seismic wave propagation (perambatan gelombang seismik), and gravity modeling (pemodelan gravitasi), with emphasis on the quantitative methods used to infer Earth's structure from surface observations. Applications are drawn from Indonesia's tectonic setting — one of the most geophysically active regions on Earth.

---

## 1. Plate Tectonics (Tektonik Lempeng)

### 1.1 Rigid Plate Motion on a Sphere

Plate motion on Earth's surface is described as rotation about a Euler pole (polar Euler). For a plate rotating with angular velocity $\boldsymbol{\omega}$ about pole $(\phi_p, \lambda_p)$, the velocity at point $(\phi, \lambda)$ is:

$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$$

The components:

$$v_e = \omega \cdot R \cos\phi \sin\alpha$$
$$v_n = \omega \cdot R \sin(\Delta\sigma) \cdot \cos\alpha$$

where $\Delta\sigma$ is the angular distance from the Euler pole, and $\alpha$ is the azimuth.

### 1.2 Spreading Rate and Age Relationship

At mid-ocean ridges, the relationship between ocean floor depth $d$ and age $t$ follows the plate cooling model:

$$d(t) = d_r + c\sqrt{t}$$

where $d_r$ is the ridge depth (~2500 m) and $c \approx 350\;\text{m/Myr}^{1/2}$.

| Tectonic Setting | Characteristic Rate | Example (Indonesia) |
|---|---|---|
| Convergent (subduction) | 20–100 mm/yr | Java Trench (~65 mm/yr) |
| Divergent (spreading) | 10–150 mm/yr | Banda Sea back-arc |
| Transform (sliding) | 5–50 mm/yr | Sumatran Fault System |
| Collisional | 20–50 mm/yr | Banda Arc collision |

### 1.3 Case Study: Sunda Plate Kinematics

The Sunda Plate (lempeng Sunda) moves northward at ~50 mm/yr relative to the Eurasian Plate. GNSS measurements from BIG's CORS network confirm:

$$\mathbf{v}_{\text{Sunda}} = (20 \pm 2)\hat{e} + (45 \pm 3)\hat{n} \;\text{mm/yr}$$

This convergence drives the megathrust (patahan megathrust) beneath Java and Sumatra, generating devastating earthquakes and tsunamis.

---

## 2. Heat Flow (Aliran Panas Bumi)

### 2.1 Heat Equation in the Earth

The temperature distribution $T(\mathbf{r}, t)$ in the Earth satisfies:

$$\rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + H$$

where $\rho$ is density, $c_p$ is specific heat, $k$ is thermal conductivity, and $H$ is volumetric heat production (from radioactive decay of $^{238}$U, $^{235}$U, $^{232}$Th, $^{40}$K).

### 2.2 Surface Heat Flow

The surface heat flow density $q$ is:

$$q = -k \frac{\partial T}{\partial z}\bigg|_{z=0}$$

Typical values:

| Tectonic Setting | Heat Flow (mW/m²) |
|---|---|
| Old oceanic crust | 40–50 |
| Mid-ocean ridge | 200–1000+ |
| Continental shield | 30–50 |
| Volcanic region | 80–200+ |
| Indonesian volcanic arc | 100–150 |

### 2.3 Geothermal Gradient

The average continental geothermal gradient is:

$$\frac{dT}{dz} \approx 25\text{–}30 \;\text{°C/km}$$

For Indonesia's volcanic regions (e.g., Sarulla, Lahendong geothermal fields), gradients reach 50–100 °C/km near heat sources.

### 2.4 Thermal Boundary Layers

The lithosphere acts as a thermal boundary layer (lapisan batas termal) with temperature profile:

$$T(z) = T_s + (T_m - T_s)\frac{\text{erf}(z/2\sqrt{\kappa t})}{\text{erf}(z_m/2\sqrt{\kappa t})}$$

where $\kappa = k/(\rho c_p)$ is thermal diffusivity ($\kappa \approx 10^{-6}$ m²/s), and $T_m \approx 1300$ °C is mantle temperature.

---

## 3. Seismic Wave Propagation (Perambatan Gelombang Seismik)

### 3.1 Elastic Wave Equations

In a homogeneous, isotropic, elastic medium, the wave equations for displacement $\mathbf{u}$:

**P-wave (gelombang P — kompresional):**

$$\rho \frac{\partial^2 \mathbf{u}}{\partial t^2} = (\lambda + \mu)\nabla(\nabla \cdot \mathbf{u}) + \mu\nabla^2\mathbf{u}$$

P-wave velocity:

$$v_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = \sqrt{\frac{K + 4\mu/3}{\rho}}$$

**S-wave (gelombang S — geser):**

$$v_S = \sqrt{\frac{\mu}{\rho}}$$

where $\lambda$ and $\mu$ are Lamé parameters, $K$ is bulk modulus, and $\rho$ is density.

### 3.2 Earth's Velocity Structure

| Layer | Depth (km) | $v_P$ (km/s) | $v_S$ (km/s) | State |
|---|---|---|---|---|
| Crust (kerak) | 0–35 | 5.5–6.8 | 3.0–3.9 | Solid |
| Upper mantle (manle atas) | 35–410 | 8.1–9.9 | 4.4–5.6 | Solid |
| Transition zone | 410–660 | 9.9–10.7 | 5.6–6.0 | Solid |
| Lower mantle | 660–2890 | 10.7–13.7 | 6.0–7.3 | Solid |
| Outer core (inti luar) | 2890–5150 | 8.0–10.3 | 0 (liquid) | Liquid |
| Inner core (inti dalam) | 5150–6371 | 11.0–11.3 | 3.5 | Solid |

### 3.3 Ray Theory and Snell's Law

Seismic ray paths follow Snell's law (hukum Snell) in the velocity-varying Earth:

$$\frac{\sin i}{v} = p = \text{constant along ray}$$

where $i$ is the angle of incidence and $p$ is the ray parameter. This leads to the travel time integral:

$$T(p) = 2\int_{z_1}^{z_2} \frac{\eta^2(z)}{\sqrt{\eta^2(z) - p^2}}\,dz, \quad \eta(z) = \frac{1}{v(z)}$$

### 3.4 Surface Wave Dispersion

Rayleigh wave group velocity $c_g$ as a function of period $T$ depends on the shear velocity structure. For a simple crustal model:

$$c_g(T) \approx \alpha \cdot v_{S,\text{crust}} + \beta \cdot v_{S,\text{mantle}}$$

Longer periods sample deeper structures, providing information on mantle velocity.

---

## 4. Gravity Modeling (Pemodelan Gravitasi)

### 4.1 Gravity Anomaly

The gravity anomaly $\Delta g$ is the difference between observed and predicted gravity:

$$\Delta g = g_{\text{obs}} - g_{\text{ref}}$$

**Bouguer anomaly** (anomali Bouguer):

$$\Delta g_B = g_{\text{obs}} - g_{\text{theoretical}} + \delta g_{\text{terrain}} - 2\pi G \rho h$$

where $2\pi G\rho h$ is the Bouguer slab correction (~0.1119 mGal/m for $\rho = 2670$ kg/m³).

### 4.2 Forward Modeling

For a 2D body with density contrast $\Delta\rho$:

$$\Delta g(x) = 2G\Delta\rho \int \frac{z\,dz\,dx'}{(x-x')^2 + z^2}$$

Talwani's method (1959) computes the gravity of arbitrary polygons.

### 4.3 Inversion

Given observed anomaly $\Delta g_{\text{obs}}$, we solve for model parameters $\mathbf{m}$:

$$\Delta g_{\text{obs}} = G(\mathbf{m}) + \boldsymbol{\epsilon}$$

Linearized: $\mathbf{d} = \mathbf{J}\Delta\mathbf{m}$ where $\mathbf{J}$ is the Jacobian (partial derivatives). The regularized solution:

$$\Delta\hat{\mathbf{m}} = (\mathbf{J}^T\mathbf{J} + \lambda^2\mathbf{I})^{-1}\mathbf{J}^T\mathbf{d}$$

---

## 5. Case Study: Subduction Zone Modeling

The Java subduction zone (zona subduksi Jawa) is modeled using joint gravity-seismic inversion:

1. **Seismic data**: Constrain plate geometry from reflection/refraction profiles
2. **Gravity data**: Fill gaps between seismic lines with 3D density models
3. **Result**: The subducting Indo-Australian slab dips at ~15° near the trench, steepening to ~70° at 300 km depth. A low-density region above the slab (density contrast: $-50$ to $-200$ kg/m³) is interpreted as a hydrated mantle wedge — critical for understanding volcanic arc magmatism (magma) in Java.

This combined approach improves hazard models (model bahaya) for the >150 million people living in Java's volcanic arc.

---

## References

1. Turcotte, D. L., & Schubert, G. (2014). *Geodynamics*, 3rd ed. Cambridge University Press.
2. Shearer, P. M. (2009). *Introduction to Seismology*, 2nd ed. Cambridge University Press.
3. Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*, 2nd ed. Cambridge University Press.
4. Stein, S., & Wysession, M. (2003). *An Introduction to Seismology, Earthquakes, and Earth Structure*. Blackwell.
5. Djamaluddin, I. et al. (2012). "Subduction dynamics in the Sunda-Banda Arc," *J. Asian Earth Sci.*, 59, 124–135.
6. Simandjuntak, T. O., & Barber, A. J. (1996). "Contrasting tectonic styles in the Neogene orogenic belts of Indonesia," *Geol. Soc. London Spec. Publ.*, 106, 185–201.
