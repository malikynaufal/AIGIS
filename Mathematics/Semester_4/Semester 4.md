---
title: Semester 4 Overview
type: semester-overview
semester: 4
tags: [mathematics, semester-4, curriculum]
created: 2026-07-27
---

# Semester 4 — Computational Methods

> *"Computation is the new mathematics."* — Part of [[Mathematics MOC]]
> Building on the foundations of calculus and linear algebra, Semester 4 develops computational tools essential for geodesy, data analysis, and machine learning.

## 📚 Course List

| Code | Course | SKS | Core Concepts |
|------|--------|-----|---------------|
| MGM211401 | [[Kalkulus Numerik]] (Numerical Methods) | 3 | Root-finding, interpolation, numerical integration |
| MGM211402 | [[Statistika Matematika]] (Math Statistics) | 3 | Estimation, hypothesis testing, Bayesian inference |
| MGM211403 | [[Aljabar Abstrak]] (Abstract Algebra) | 3 | Groups, rings, fields, Galois theory |
| MGM211404 | [[Analisis Kompleks]] (Complex Analysis) | 3 | Analytic functions, residues, conformal mappings |
| MGM211405 | Pemrograman Web (Web Programming) | 3 | HTML, CSS, JavaScript |
| MGM211406 | Rekayasa Perangkat Lunak (Software Engineering) | 3 | SDLC, testing, documentation |

**Total SKS: 18**

## 🗺️ Concept Map

```mermaid
flowchart TD
    Numerical[Numerical Methods] --> Root[Root Finding]
    Numerical --> Interp[Interpolation]
    Numerical --> Integrat[Numerical Integration]
    Numerical --> LinAlg[Numerical Linear Algebra]
    StatMath[Statistical Methods] --> Est[Estimation Theory]
    StatMath --> HypTest[Hypothesis Testing]
    StatMath --> Bayes[Bayesian Inference]
    AbsAlg[Abstract Algebra] --> Groups[Group Theory]
    AbsAlg --> Ring[Ring Theory]
    AbsAlg --> Finite[Finite Fields]
    CompAnal[Complex Analysis] --> Res[Residue Theory]
    CompAnal --> Conf[Conformal Mapping]
    
    Root --> |Newton-Raphson| LeastSquares[Least Squares [[Least Squares Adjustment]]]
    LinAlg --> |Eigenvalues| AbsAlg
    HypTest --> |Confidence Intervals| GNSS[GNSS Positioning]
    Conf --> |Fluid Flow| Geodesy[Geodesy [[Geodesy MOC]]]
```

## 🎯 Learning Outcomes

By the end of this semester, you should be able to:

1. **Numerical Methods:** Implement root-finding, interpolation, and numerical integration algorithms
2. **Statistical Inference:** Derive MLE, construct confidence intervals, perform hypothesis tests
3. **Abstract Algebra:** Work with groups, rings, and finite fields; apply Galois theory
4. **Complex Analysis:** Evaluate complex integrals using residues; find conformal mappings

## 📐 Key Connections to Geodesy

| Course | Geodesy Application |
|--------|-------------------|
| Numerical Methods | Solving nonlinear least-squares adjustment |
| Statistical Inference | Error ellipses, network quality analysis |
| Abstract Algebra | Cryptographic protocols for GNSS |
| Complex Analysis | Potential theory, geoid modeling |

## 📚 Required Reading

- Burden & Faires, *Numerical Analysis* (MGM211401)
- Casella & Berger, *Statistical Inference* (MGM211402)
- Dummit & Foote, *Abstract Algebra* (MGM211403)
- Ahlfors, *Complex Analysis* (MGM211404)

## ⏰ Study Rhythm

| Day | Focus | Duration |
|-----|-------|----------|
| Mon | Numerical Methods — new topic | 2 hrs |
| Tue | Statistical Methods — new topic | 2 hrs |
| Wed | Abstract Algebra — new topic | 2 hrs |
| Thu | Complex Analysis — new topic | 2 hrs |
| Fri | Problem sets (all 4 courses) | 3 hrs |
| Sat | Review + cross-course connections | 2 hrs |
| Sun | Rest + light preview | 1 hr |

---
*See also: [[Mathematics MOC]], [[Study Plan]], [[Semester 3/Semester 3]], [[Semester 5/Semester 5]]*
