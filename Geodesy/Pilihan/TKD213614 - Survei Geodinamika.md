---
tags: [aigis, geodesy, pilihan, geodynamics, tectonics, crustal-deformation, gnss]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Survei Geodinamika (Geodynamic Surveying)

**Kode:** TKD213614 | **SKS:** 3 (2-1) | **Semester:** 5–7

## Course Overview

Geodynamic surveying monitors Earth's crustal motion using repeated high-accuracy GNSS campaigns and InSAR techniques. The course covers design of geodetic networks for tectonic studies, velocity field estimation, strain analysis, and geological interpretation of results. Essential for understanding Indonesia's complex tectonic setting.

## Key Topics

### 1. Geodynamic GNSS Networks

| Design Aspect | Requirement for Geodynamics |
|---------------|---------------------------|
| Baseline length | 50–500 km (tectonic) |
| Observation time | 24–72 hours static |
| Accuracy | 1–3 mm horizontal, 5–10 mm vertical |
| Reoccupation | Annual or semi-annual |
| Processing | [[PPP]] or double-difference |

### 2. Velocity Field Estimation

**Simple velocity model:**
$$
\begin{pmatrix} v_E \\ v_N \end{pmatrix} = \frac{1}{n} \sum_{i=1}^{n} \frac{\Delta \mathbf{r}_i}{\Delta t_i}$ $### 3. Strain Rate Analysis

**Strain rate tensor:**
$$
\dot{\epsilon} =
\begin{pmatrix}
\epsilon_{xx} & \epsilon_{xy} \\
\epsilon_{yx} & \epsilon_{yy}
\end{pmatrix}
=
\frac{1}{2} \begin{pmatrix}
2\frac{\partial v_E}{\partial x} & \frac{\partial v_E}{\partial y} + \frac{\partial v_N}{\partial x} \\
\frac{\partial v_E}{\partial y} + \frac{\partial v_N}{\partial x} & 2\frac{\partial v_N}{\partial y}
\end{pmatrix}$ $**Maximum shear strain:**$$
\dot{\gamma}_{max} = \sqrt{(\dot{\epsilon}_{xx} - \dot{\epsilon}_{yy})^2 + 4\dot{\epsilon}_{xy}^2}
$$
# ## 4. Indonesian Case Studies

| Region | Tectonics | GPS Velocity |
|--------|-----------|-------------|
| Sumatera | Oblique subduction | 67 mm/yr |
| Java | Orthogonal subduction | 50–70 mm/yr |
| Sulawesi | Triple junction | 30–50 mm/yr |
| Papua | Collision | 50–100 mm/yr |

## Field Campaign Design

- Monumentation: deep-braced (3 m) or rock anchors
- Antenna: geodetic (choke ring)
- Duration: ≥ 5 days for first epoch, ≥ 3 days subsequent
- Processing: GAMIT/GLOBK, Bernese, or GIPSY

## Related Concepts

- [[Crustal Deformation]] — Physical deformation
- [[Plate Tectonics]] — Plate motion
- [[ITRF]] — Reference frame
- [[Survei Deformasi]] — Related survey course
- [[GPS]] — GNSS component
- [[GNSS]] — Satellite positioning

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
