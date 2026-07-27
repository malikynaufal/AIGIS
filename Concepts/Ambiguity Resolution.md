---
tags: [aigis, concept, geodesy, gnss, ambiguity-resolution]
aliases: [Ambiguity Resolution, Integer Ambiguity]
created: 2026-07-27
---

# Ambiguity Resolution

**Core Idea:** Carrier phase observations include an unknown integer number of wavelengths ($N$). Resolving this integer ambiguity is the key to centimeter-level GNSS positioning.

## The Problem

$$\Phi = \lambda N + \rho + c(dt_r - dt_s) - d_{iono} + d_{trop} + \varepsilon$$

- $\Phi$ = measured phase (observable)
- $N$ = integer ambiguity (unknown, must be integer!)
- $\lambda$ = carrier wavelength (19 cm for GPS L1)

## Resolution Methods

| Method | Approach | Time to Fix |
|--------|----------|-------------|
| **Float solution** | Estimate $N \in \mathbb{R}$ | — |
| **LAMBDA** | Search integer candidates in transformed space | Seconds to minutes |
| **Wide-lane/Narrow-lane** | Combine frequencies to get wider wavelength | Fast |
| **Melbourne-Wübbena** | Wide-lane minus narrow-lane combination | Minutes |
| **Pseudorange bootstrapping** | Use code to narrow float ambiguity | Seconds |

## LAMBDA Method

$$\hat{N}_{fixed} = \arg\min_{\mathbf{N} \in \mathbb{Z}^n} (\hat{N}_{float} - \mathbf{N})^T Q_N^{-1} (\hat{N}_{float} - \mathbf{N})$$

1. Decorrelate with Z-transform
2. Search integer grid
3. Back-transform to original space
4. Ratio test: $\text{Ratio} = \frac{\Delta_2}{\Delta_1} > 3.0$ → fixed

## Success Criteria

- **Fix rate:** Percentage of epochs with successful integer fix
- **Ratio test:** Ratio of second-best to best residual > 3.0
- **Bootstrapped success probability:** $P_s = \prod_{i=1}^n (1 - 2\Phi(|q_i| - 0.5))$

## Related

- [[GNSS]] — Full positioning context
- [[RTK]] — Real-time ambiguity resolution
- [[PPP]] — Precise Point Positioning
- [[Least Squares Adjustment]] — Float solution

---
*Part of [[Geodesy MOC]]*