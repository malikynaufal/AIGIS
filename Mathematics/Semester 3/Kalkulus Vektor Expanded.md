---
title: Semester 3 — Kalkulus Vektor (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, vector-calculus, semester-3, aigis, geodesy-applied]
---

# Semester 3 — Kalkulus Vektor (Expanded)

**Course**: MGM211301 — Kalkulus Vektor  
**Credits**: 3 SKS  
**Prerequisites**: [[Kalkulus I Expanded]], [[Kalkulus II Expanded]]

---

## Course Overview

Vector calculus extends calculus to vector fields. Covers gradient, divergence, curl, line integrals, surface integrals, and the classical integral theorems (Green, Stokes, Divergence). Essential for understanding gravity fields, electromagnetic theory, and fluid dynamics.

---

## Syllabus

### Unit 1: Vector Fields and Review

- **Scalar fields**: $f(x,y,z)$ assigns a number to each point
- **Vector fields**: $\\mathbf{F}(x,y,z) = P\\hat{i}+Q\\hat{j}+R\\hat{k}$
- Coordinate systems: Cartesian, cylindrical, spherical

### Unit 2: Differential Operators

- **Gradient**: $\\nabla f = (f_x, f_y, f_z)$ — direction of steepest ascent
- **Divergence**: $\\nabla \\cdot \\mathbf{F} = P_x + Q_y + R_z$ — outflow per unit volume
- **Curl**: $\\nabla \\times \\mathbf{F}$ — rotation per unit area
- **Laplacian**: $\\nabla^2 f = f_{xx}+f_{yy}+f_{zz}$

### Unit 3: Line Integrals

- Scalar: $\\int_C f\\,ds$
- Vector: $\\int_C \\mathbf{F}\\cdot d\\mathbf{r}$
- Conservative fields: $\\int \\nabla f \\cdot d\\mathbf{r} = f(\\mathbf{b})-f(\\mathbf{a})$

### Unit 4: Surface Integrals

- $\\iint_S f\\,dS = \\iint_D f(\\mathbf{r}(u,v))|\\mathbf{r}_u \\times \\mathbf{r}_v|\\,du\\,dv$
- Flux: $\\iint_S \\mathbf{F}\\cdot d\\mathbf{S}$

### Unit 5: Integral Theorems

- **Green's theorem** (2D): $\\oint_C P\\,dx + Q\\,dy = \\iint_D (Q_x-P_y)\\,dA$
- **Divergence theorem**: $\\oint_S \\mathbf{F}\\cdot d\\mathbf{S} = \\iiint_V \\nabla\\cdot\\mathbf{F}\\,dV$
- **Stokes' theorem**: $\\oint_C \\mathbf{F}\\cdot d\\mathbf{r} = \\iint_S \\nabla\\times\\mathbf{F}\\cdot d\\mathbf{S}$

---

## Geodesy Connections

- **Gravity field**: gradient of potential, divergence of field
- **Stokes integral**: Geoid computation from gravity anomalies
- **Laplacian**: $\\nabla^2 V = 4\\pi G\\rho$ (Poisson's equation)

---

➡️ [[Mathematics MOC]] | ➡️ [[Multivariable Calculus]]