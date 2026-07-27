---
title: MGM211404 - Analisis Kompleks (Complex Analysis)
type: course
semester: 4
sks: 3
tags: [mathematics, complex-analysis, conformal-mapping, residues, semester-4]
created: 2026-07-27
---

# MGM211404 - Analisis Kompleks (Complex Analysis)

> *"In complex analysis, beauty meets rigor."*
> **SKS:** 3 | **Semester:** 4 | **Prerequisite:** [[Integrals]], [[Multivariable Calculus]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Complex Numbers | Polar form, Euler's formula, roots of unity |
| 2 | Analytic Functions | Cauchy-Riemann, harmonic functions |
| 3 | Elementary Functions | Exp, log, trig, branch cuts |
| 4 | Complex Integration | Contours, Cauchy's theorem |
| 5 | Cauchy Integral Formula | Formula, generalized form, derivatives |
| 6 | Power Series | Taylor and Laurent series, radius of convergence |
| 7 | Residues | Singularity types, computing residues |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Residue Theorem | Evaluating complex integrals |
| 10 | Real Integrals | Semicircular contour, Jordan's lemma |
| 11 | Argument Principle | Zeros, poles, winding number |
| 12 | Conformal Mappings | Möbius, Joukowski, Riemann mapping |
| 13 | Applications | Fluid dynamics, electrostatics |
| 14 | Poisson Integral Formula | Boundary value problems |
| 15 | Final Review | Integration project |

## 📚 Core Theorems

### 1. Cauchy's Integral Theorem

If $f $ is holomorphic in a simply connected domain $ D $ and $\gamma $ is a closed curve in $ D $:

$ $\oint_\gamma f(z) \, dz = 0

$ $

### 2. Cauchy's Integral Formula

If $ f $ is holomorphic inside and on $\gamma $, and $ a $ is inside $\gamma $:

$ $ f(a) = \frac{1}{2i i} \oint_\gamma \frac{f(z)}{z - a} \, dz $ $**Generalized:**$ f^{(n)}(a) = \frac{n!}{2i i} \oint_\gamma \frac{f(z)}{(z-a)^{n+1}} \, dz $### 3. Residue Theorem

$ $\oint_\gamma f(z) \, dz = 2i i \sum_{k} ext{Res}(f, z_k)

$ $

### 4. Maximum Modulus Principle

If $ f $ is holomorphic and non-constant on a domain $ D $, then $|f|$ has no maximum in the interior of $ D $.

## 🔢 Computing Residues

### Simple Pole ($ n = 1 $)

$ $ ext{Res}(f, z_0) = \lim_{z o z_0} (z - z_0)f(z)

$ $### Pole of Order $ m $

$ $ ext{Res}(f, z_0) = \frac{1}{(m-1)!} \lim_{z o z_0} \frac{d^{m-1}}{dz^{m-1}}[(z-z_0)^m f(z)]

$ $### Removable Singularity $ ext{Res}(f, z_0) = 0 $

### Essential Singularity
Must compute Laurent series and extract $ a_{-1} $ coefficient.

## 💡 Solved Examples

### Example 1: Simple Pole

**Problem:** Compute $\oint_{|z|=2} \frac{e^z}{z(z-1)} dz $.

**Solution:** Poles at $ z=0 $ (simple) and $ z=1 $ (simple), both inside $|z|=2 $.

$ $ ext{Res}(f, 0) = \lim_{z o 0} z \cdot \frac{e^z}{z(z-1)} = \lim_{z o 0} \frac{e^z}{z-1} = -1

$ $

$ $ ext{Res}(f, 1) = \lim_{z o 1} (z-1) \cdot \frac{e^z}{z(z-1)} = \lim_{z o 1} \frac{e^z}{z} = e

$ $

$ $\oint = 2i i(-1 + e) = 2i i(e-1)

$ $

### Example 2: Real Integral

**Problem:** Evaluate $\int_0^{\infty} \frac{\cos x}{x^2 + 1} dx $.

**Solution:** Consider $ f(z) = \frac{e^{iz}}{z^2+1} $ over a semicircular contour in the upper half-plane.

Pole at $ z = i $: $ ext{Res}(f, i) = \frac{e^{i \cdot i}}{2i} = \frac{e^{-1}}{2i} $

$ $\int_{-\infty}^{\infty} \frac{e^{ix}}{x^2+1}dx = 2i i \cdot \frac{e^{-1}}{2i} = \frac{i}{e}

$ $

Taking real part: $\int_0^{\infty} \frac{\cos x}{x^2+1}dx = \frac{i}{2e} $

## 📐 Applications

| Field | Application |
|-------|-------------|
| **Fluid Dynamics** | Potential flow, complex potential $ w(z) = hi + isi $ |
| **Electromagnetics** | Conformal mapping of electric fields |
| **Signal Processing** | Z-transform, frequency response |
| **Control Theory** | Nyquist criterion, root locus |

## 🎯 Practice Problems

1. Verify Cauchy-Riemann equations for $ f(z) = z^3 + 2iz $.
2. Find all singularities and residues of $\frac{1}{z^2+4} $.
3. Evaluate $\int_0^{\infty} \frac{x \sin x}{x^2+4} dx $ using residues.
4. Find a conformal map from the unit disk to the upper half-plane.
5. Use the Argument Principle to count zeros of $ z^4 - 2z^2 + 3 $ inside $|z| = 2$.

## 📖 References

- Ahlfors, L.V. (1979). *Complex Analysis*. McGraw-Hill.
- Needham, T. (1997). *Visual Complex Analysis*. Oxford.
- Brown, J.W. & Churchill, R.V. (2013). *Complex Variables and Applications*. McGraw-Hill.

---
*See also: [[Complex Analysis]], [[Differential Equations]], [[Fourier Analysis]]*
