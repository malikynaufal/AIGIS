---
code: FKD211406
name: Grafika Komputer
SKS: 2
semester: 4
department: Informatika/Fisika
tags: [computer-graphics, visualization, 3d-rendering, matplotlib]
created: 2026-07-27
---

# FKD211406 — Grafika Komputer

## Course Overview

Computer graphics for physics — transforming data and mathematical models into visual representations. This course covers 2D/3D rendering, scientific visualization, and programmable graphics pipelines, enabling students to create publication-quality visualizations of physical phenomena and experimental data.

**Contact Hours:** 2 SKS (1 hour lecture + 1 hour lab per week)
**Prerequisites:** Pemrograman Lanjutan, Aljabar Linear
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: 2D Rendering and Coordinate Systems (Weeks 1–4)

- **Coordinate transforms:** window-to-viewport mapping

- **Affine transformations in 2D:** translation, rotation, scaling, shear

- **Matrix representation:** homogeneous coordinates

- **2D clipping algorithms:** Cohen-Sutherland for line clipping

- **Rendering pipelines in Matplotlib** — drawing custom shapes

- **Plotting styles:** publication-quality formatting, fonts, and color schemes

### Unit 2: 3D Transformations and Projection (Weeks 5–8)

- **3D coordinate systems:** world → camera → screen transformations

- **Rotation matrices:** about x, y, z axes; Euler angles

- **Translation and scaling in 3D** using 4×4 homogeneous coordinates

- **Projections:**
  - Orthographic projection (parallel lines remain parallel)
  - Perspective projection (foreshortening)

- **View frustum** and aspect ratio

- **Quaternions** — representing 3D rotations without gimbal lock

### Unit 3: Scientific Visualization (Weeks 9–12)

- **Scalar field visualization:**
  - Color maps (colormaps for physics: 'viridis', 'inferno', 'coolwarm')
  - Contour plots and filled contours
  - Isosurfaces (marching cubes) for 3D scalar fields

- **Vector field visualization:**
  - Arrow plots, quiver plots
  - Streamlines and flow lines
  - Vector field topology

- **Surface rendering:** wireframe, shaded, texture-mapped

- **Volume rendering** (introductory): ray-casting approach

- **Animation:** time-evolving data

### Unit 4: Advanced Graphics and Visualization Tools (Weeks 13–16)

- **3D interactive plotting** with `plotly`, `mayavi`

- **Using Python's graphics libraries:**
  - `matplotlib.animation` — physics simulations
  - `ipywidgets` — interactive parameter exploration
  - `numpy-stl` — 3D mesh processing

- **Geophysical data visualization:**
  - DEM (digital elevation model) rendering
  - Terrain shading and slope maps
  - Heat maps for gravity data

- **Color theory** for scientific communication (e.g., perceptually uniform colormaps)

- **Final project:** create a 3D visualization of a physics dataset

---

## 🔬 Key Transformations

```
2D Rotation:     [x']   [cosθ  -sinθ] [x]
                 [y'] = [sinθ   cosθ] [y]

3D Homogeneous:  T = [1 0 0 tx]    Rx = [1   0    0  0]
                      [0 1 0 ty]         [0 cosθ -sinθ 0]
                      [0 0 1 tz]         [0 sinθ  cosθ 0]
                      [0 0 0  1]         [0   0    0  1]

Perspective projection: x' = x·d/z, y' = y·d/z
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Apply 2D and 3D affine transformations using matrix operations
2. Implement orthographic and perspective projections
3. Create publication-quality visualizations of scalar and vector fields
4. Generate animated visualizations of time-dependent physics data
5. Use Python libraries for interactive and static 3D graphics
6. Produce effective scientific visualizations for presentations and publications

---

## 📚 References

1. Foley, J.D. et al. (1996). *Computer Graphics: Principles and Practice*, 2nd ed. Addison-Wesley.
2. Hearn, D. & Baker, M.P. (2004). *Computer Graphics with OpenGL*, 3rd ed. Prentice Hall.
3. Telea, A.C. (2014). *Data Visualization: Principles and Practice*, 2nd ed. CRC Press.
4. Tufte, E.R. (2001). *The Visual Display of Quantitative Information*, 2nd ed. Graphics Press.
5. Rougier, N.P. (2021). *Scientific Visualization: Python + Matplotlib* (online book).
