---
code: FKD211103
name: Aljabar Linear
SKS: 2
semester: 1
department: Matematika
tags: [mathematics, linear-algebra, vectors, matrices, linear-transformations]
created: 2026-07-27
---

# FKD211103 — Aljabar Linear

## Course Overview

Linear algebra provides the mathematical language for describing spaces, transformations, and systems — indispensable in physics from quantum mechanics (Hilbert spaces) to classical mechanics (rotation matrices) to geodesy (coordinate transformations and least-squares adjustment). This course builds both computational skill and conceptual understanding.

**Contact Hours:** 2 SKS (2 hours lecture per week)
**Prerequisites:** None
**Co-requisites:** Kalkulus I

---

## 📋 Topics & Outline

### Unit 1: Vectors and Vector Spaces (Weeks 1–5)

- **Geometric vectors:** displacement, velocity, acceleration as vectors

- Vector operations: addition, scalar multiplication, dot product, cross product

- **Dot product:** **a**·**b** = |a||b|cos(θ) — projection, work calculation

- **Cross product:** **a**×**b** = |a||b|sin(θ) n̂ — torque, angular momentum

- Triple products: scalar triple product (volume), vector triple product

- **Vector spaces:** definition, examples (R², R³, function spaces)

- Subspaces, linear independence, basis, and dimension

### Unit 2: Matrices and Systems of Equations (Weeks 6–10)

- Matrix operations: addition, multiplication, transpose

- **Gaussian elimination** and row echelon form

- Solving linear systems Ax = b: existence and uniqueness

- **Determinants:** definition, properties, cofactor expansion, geometric interpretation

- **Inverse matrices:** (AB)⁻¹ = B⁻¹A⁻¹, computing A⁻¹

- **Eigenvalues and eigenvectors:** Av = λv

- Characteristic equation: det(A - λI) = 0

- Diagonalization of symmetric matrices

### Unit 3: Linear Transformations and Applications (Weeks 11–14)

- **Linear maps:** definition, kernel (null space), image (column space)

- Rotation, reflection, scaling as matrix transformations

- **Coordinate transformations:** passive vs active transformations

- **Orthogonal matrices:** Q⁻¹ = Qᵀ (rotations preserve inner product)

- Singular Value Decomposition (SVD) — introduction

- **Applications in physics:** rotation of reference frames, quantum states

- **Applications in geodesy:** coordinate transformations, least squares adjustment

---

## 🔬 Key Concepts

```
Dot Product:        a · b = a₁b₁ + a₂b₂ + a₃b₃
Cross Product:      a × b = |i  j  k |
                            |a₁ a₂ a₃|
                            |b₁ b₂ b₃|

Eigenvalue Problem: Av = λv
Determinant:        det(A) = Σ sign(σ) ∏ a_{i,σ(i)}
Matrix Inverse:     A⁻¹ = adj(A)/det(A)
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Perform vector operations and interpret them geometrically and physically
2. Solve systems of linear equations using matrix methods
3. Compute eigenvalues and eigenvectors and understand their significance
4. Represent and apply linear transformations using matrices
5. Use linear algebra tools for coordinate transformations in geodesy
6. Apply least-squares methods to overdetermined systems

---

## 📚 References

1. Strang, G. (2016). *Introduction to Linear Algebra*, 5th ed. Wellesley-Cambridge.
2. Anton, H. & Rorres, C. (2013). *Elementary Linear Algebra*, 11th ed. Wiley.
3. Lay, D.C. et al. (2015). *Linear Algebra and Its Applications*, 5th ed. Pearson.
4. MIT OCW 18.06 Linear Algebra (Gilbert Strang): https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
5. 3Blue1Brown — Essence of Linear Algebra: https://www.3blue1brown.com/topics/linear-algebra
