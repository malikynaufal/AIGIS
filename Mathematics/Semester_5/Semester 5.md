---
title: Semester 5 Overview
type: semester-overview
semester: 5
tags: [mathematics, semester-5, curriculum]
created: 2026-07-27
---

# Semester 5 — Applications

> *"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding."* — Thurston
> Part of [[Mathematics MOC]]. Semester 5 applies accumulated mathematical tools to practical problems.

## 📚 Course List

| Code | Course | SKS | Core Concepts |
|------|--------|-----|---------------|
| MGM211501 | [[Metode Numerik]] (Numerical Methods) | 3 | ODEs, PDEs, optimization, SVD |
| MGM211502 | [[Teori Graf]] (Graph Theory) | 3 | Graphs, networks, spectral theory |
| MGM211503 | [[Optimisasi]] (Optimization) | 3 | LP, KKT, duality, gradient methods |
| MGM211504 | [[Kecerdasan Buatan]] (Artificial Intelligence) | 3 | Search, ML, neural networks |
| MGM211505 | [[Visi Komputer]] (Computer Vision) | 3 | Image processing, 3D reconstruction |

**Total SKS: 15**

## 🗺️ Concept Map

```mermaid
flowchart TD
 NumM[Num Methods] --> ODE[Numerical ODE]
 NumM --> PDE[Numerical PDE]
 NumM --> SVD[SVD & PCA]
 TG[Graph Theory] --> Net[Network Analysis]
 TG --> Spec[Spectral Theory]
 Opt[Optimization] --> LP[Linear Programming]
 Opt --> NLP[Nonlinear Programming]
 AI[Artificial Intelligence] --> Search[Search Algorithms]
 AI --> ML[Machine Learning]
 AI --> NN[Neural Networks]
 CV[Computer Vision] --> Stereo[Stereo Vision]
 CV --> Photog[Photogrammetry]

 Opt --> |KKT| LeastSq[Least Squares [[Least Squares Adjustment]]]
 ML --> |Classification| RemoteSense[Remote Sensing]
 CV --> |Bundle Adj| Mapping[Geodetic Mapping [[Geodesy MOC]]]
```

## 🎯 Learning Outcomes

1. **Numerical Methods:** Solve ODEs and PDEs numerically
2. **Graph Theory:** Model networks, analyze connectivity
3. **Optimization:** Formulate and solve LP/NLP problems
4. **AI:** Implement search, ML, and neural network algorithms
5. **Computer Vision:** Process images, reconstruct 3D scenes

---
*See also: [[Mathematics MOC]], [[Study Plan]], [[Semester 4/Semester 4]], [[Semester 6/Semester 6]]*
