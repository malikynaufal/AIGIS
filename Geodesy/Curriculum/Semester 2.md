---
title: Geodesy Semester 2 - Measurement & Programming
tags: [geodesy, curriculum, measurement, programming]
---

# 📗 Semester 2: Measurement Systems & Computation

## Overview
Transitioning from theory to practice: learning how to measure the Earth and how to process that data using modern programming environments.

## ✍️ Core Courses

### 1. Sistem Koordinat (Coordinate Systems)

- **Topics**: Terrestrial vs. Celestial systems, ECEF, Geodetic (φ, λ, h), and local topocentric systems (ENU).

- **Mathematical Focus**: Transformation matrices and ellipsoidal geometry.

- **Key Formula**: $X = (N+h)\cos\phi\cos\lambda$### 2. Hitung Perataan (Least Squares Adjustment)

- **Topics**: Error theory, weight matrices, observation equations, and stochastic models.

- **Geodetic Application**: Minimizing residuals in surveying networks.

- **Key Formula**:$\hat{x} = (A^T P A)^{-1} A^T P L$

### 3. Pemrograman Komputer (Computer Programming)

- **Focus**: Python for Geodesy. Libraries: `numpy`, `scipy`, `matplotlib`.

- **Tasks**: Implementing the Vincenty formula and parsing NMEA GPS strings.

### 4. Survei Terestris II (Terrestrial Surveying II)

- **Practical**: Use of Total Stations, Digital Levels, and measurement of horizontal/vertical control networks.

## 🧭 Roadmap
Focus on mastering **Matrix Algebra** this semester, as it is the language of [[Least Squares Adjustment]].
