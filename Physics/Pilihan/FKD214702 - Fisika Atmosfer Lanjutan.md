---
title: "Fisika Atmosfer Lanjutan"
subject: "Fisika Pilihan"
tags:
 - atmospheric-physics
 - radiation-transfer
 - climate-modeling
 - SKS: 3
---

# FKD214702 — Fisika Atmosfer Lanjutan
**Advanced Atmospheric Physics** | 3 SKS (Satuan Kredit Semester)

## Overview

Advanced atmospheric physics (fisika atmosfer lanjutan) extends the foundational study of the atmosphere to quantitative radiative transfer theory, atmospheric chemistry, numerical climate modeling, and tropospheric process analysis. Students will develop the mathematical tools needed to understand how electromagnetic radiation interacts with atmospheric constituents, how chemical cycles drive ozone and greenhouse gas budgets, and how general circulation models simulate Earth's climate. Emphasis is placed on applications relevant to Indonesia's tropical atmosphere (atmosfer tropis).

---

## 1. Radiative Transfer (Perambatan Radiasi)

### 1.1 The Radiative Transfer Equation

The specific intensity $I_\nu $ along a path $  s $ through the atmosphere satisfies $ $ \frac{dI_\nu}{ds} = -\kappa_\nu I_\nu + j_\nu

$ where $\kappa_\nu $ is the absorption coefficient (koefisien absorpsi) and $ j_\nu $ is the emission coefficient. In terms of optical depth $ \tau_\nu$:

$ $ \frac{dI_\nu}{d\tau_\nu} = I_\nu - S_\nu

$ where $ S_\nu = j_\nu / \kappa_\nu $ is the source function (fungsi sumber). Under local thermodynamic equilibrium (LTE), $ S_\nu = B_\nu(T) $ is the Planck function.

### 1.2 Beer–Lambert Law and Optical Depth

For a homogeneous layer of thickness $ \Delta z$:

$ $

I_\nu = I_{\nu,0} \exp(-\tau_\nu) = I_{\nu,0} \exp(-\kappa_\nu \cdot \rho \cdot \Delta z
)

$ The optical depth is: $$

\tau_\nu = \int_0^z \kappa_\nu(z') \rho(z')\, dz' $ $

### 1.3 Thermal Radiation Budget

The outgoing longwave radiation (OLR) at the top of atmosphere is

$$ \text{OLR} = \int_0^\infty \int_0^{2\pi} \int_0^{\pi/2} I_\nu \cos\theta \sin\theta \, d\theta \, d\phi \, d\nu

$For a grey atmosphere with emissivity $ \varepsilon$:

$ $ \text{OLR} = \varepsilon \sigma T_s^4

$ where $\sigma = 5.67 \times 10^{-8} $  W m⁻² K⁻⁴ is the Stefan–Boltzmann constant and $ T_s $ is surface temperature.

| Radiation Component | Approximate Value (W/m²) |
|---|---|
| Incoming solar (shortwave) | 1361 (solar constant) |
| Absorbed by atmosphere | ~75 |
| Reflected by clouds/aerosols | ~100 |
| Surface absorbed solar | ~170 |
| Surface emitted longwave | ~398 |
| Atmospheric window | ~40 |
| Greenhouse back-radiation | ~340 |

---

## 2. Atmospheric Chemistry (Kimia Atmosfer)

### 2.1 Ozone Photochemistry

The Chapman cycle describes stratospheric ozone (ozon) formation and destruction:

1. $O_2 + h\nu (\lambda < 242\;\text{nm}) \rightarrow 2O $ 2. $  O + O_2 + M \rightarrow O_3 + M $ 3. $ O_3 + h\nu \rightarrow O_2 + O $ 4. $  O + O_3 \rightarrow 2O_2 $ Catalytic destruction by $ HO_x $, $ NO_x $, and $ ClO_x $ species accelerates ozone loss. The steady-state ozone concentration is

$ $ [O_3]_{ss} = \frac{J_1 [O_2] [M]}{k_4 [O]} $$

# ## 2.2 Greenhouse Gas Radiative Forcing

The radiative forcing $ \Delta F $ due to CO₂ concentration change is approximated $ $ \Delta F = 5.35 \ln\left(\frac{C}{C_0}\right) \;\text{W/m}^2

$ For a doubling from $ C_0 = 280 $ ppm to $  C = 560 $ ppm: $ \Delta F \approx 3.7 $ W/m².

For methane ( $ \text{CH}_4 $):

$ $ \Delta F_{\text{CH}_4} = 0.036 \left(\sqrt{M} - \sqrt{M_0}\right) \;\text{W/m}^2

$ where $ M$ is CH₄ concentration in ppb.

---

## 3. Climate Models (Model Iklim)

### 3.1 General Circulation Models (GCM)

GCMs solve the primitive equations of atmospheric dynamics on a discretized grid:

**Momentum equations** (horizontal, $p $-coordinates):

$ $ \frac{\partial u}{\partial t} = -(u \cdot \nabla) u + fv - \frac{\partial \Phi}{\partial x} + F_
x

**Thermodynamic equation:**

\frac{\partial T}{\partial t} = -u \cdot \nabla T + \frac{\omega}{c_p}(\gamma_d - \gamma) + Q/c_
p

**Continuity equation:**

 \nabla \cdot \vec{v} + \frac{\partial \omega}{\partial p} = 0

$$

# ## 3.2 Model Hierarchy

| Model Type | Dimensions | Key Features |
|---|---|---|
| EBM (Energy Balance) | 0-D to 1-D | Global mean temperature; albedo |
| GCM | 3-D | Full dynamics, thermodynamics |
| ESM (Earth System) | 3-D | Includes carbon cycle, vegetation |
| RCM (Regional) | 2-D/3-D | Nested; higher resolution (10–50 km) |
| CMIP6 Ensemble | Multi-model | Coupled intercomparison project |

### 3.3 Downscaling for Indonesia

For Indonesia's complex archipelago, statistical and dynamical downscaling (penurunan skala) are critical. A GCM at 100 km resolution cannot resolve the diurnal cycle over Java (~700 km wide). RegCM4 (ICTP) applied at 5 km resolution captures monsoon onset timing with improved accuracy over coarse models.

---

## 4. Tropospheric Modeling (Pemodelan Troposfer)

### 4.1 Convective Parameterization

In the tropics, organized deep convection (konveksi) transports heat and moisture vertically. The Arakawa–Schubert parameterization assumes quasi-equilibrium between convection and large-scale forcing

$ $ \frac{\partial \overline{q}}{\partial t} + \text{advection} = P - E + \int G(b_e) \Delta_q(b_e)\, db_e

$where $ G(b_e) $ is the cloud work function and $\Delta_q $ is moisture detrainment.

### 4.2 Case Study: Indonesian Maritime Continent

The Maritime Continent (Wilayah Maritim Indonesia) presents unique challenges for tropospheric modeling:

- **Diurnal cycle of convection**: Morning convection over land, afternoon/evening offshore propagation of convective systems.

- **Madden–Julian Oscillation (MJO)**: Intraseasonal (30–90 day) modulation of convection propagating eastward from the Indian Ocean.

- **ENSO teleconnections**: El Niño causes drought over Indonesia; La Niña causes flooding.

Research at BMKG and BMKG-BPPTIK uses WRF (Weather Research and Forecasting) model at 3 km resolution to predict convective events, achieving >80% accuracy for 24-hour precipitation forecasts during the wet season (musim hujan).

---

## References

1. Liou, K. N. (2002). *An Introduction to Atmospheric Radiation*, 2nd ed. Academic Press.
2. Wallace, J. M., & Hobbs, P. V. (2006). *Atmospheric Science: An Introductory Survey*, 2nd ed. Academic Press.
3. Seinfeld, J. H., & Pandis, S. N. (2016). *Atmospheric Chemistry and Physics*, 3rd ed. Wiley.
4. IPCC (2021). *Climate Change 2021: The Physical Science Basis* (AR6 WG I). Cambridge University Press.
5. Neale, R. B., & Slingo, J. (2006). "The Maritime Continent and Its Role in the Climate System," *ASR Letters*, 7.
6. Aldrian, E., & Susanto, R. D. (2003). "Identification of three dominant rainfall regions within Indonesia," *Int. J. Climatol.*, 23, 1435–1452.
