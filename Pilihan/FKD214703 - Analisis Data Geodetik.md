---
title: "Analisis Data Geodetik"
subject: "Fisika Pilihan"
tags:
  - geodesy
  - time-series
  - spectral-analysis
  - least-squares
  - SKS: 3
---

# FKD214703 — Analisis Data Geodetik
**Geodetic Data Analysis** | 3 SKS (Satuan Kredit Semester)

## Overview

Geodetic data analysis (analisis data geodetik) provides the mathematical and statistical framework for interpreting observations from GNSS networks, leveling surveys, gravimeters, and space-geodetic techniques. This course covers time series analysis (analisis seri waktu), spectral methods (metode spektral), digital filtering, least-squares estimation (metode kuadrat terkecil), and hypothesis testing — all essential for detecting tectonic deformation, postglacial rebound, and sea-level change. Applications focus on the Indonesian geodetic network maintained by BIG (Badan Informasi Geospasial).

---

## 1. Time Series Analysis (Analisis Seri Waktu)

### 1.1 Components of a Geodetic Time Series

A GNSS coordinate time series at station $i$ can be decomposed:

$$x_i(t) = v \cdot t + \sum_{j} \left[a_j \sin(\omega_j t) + b_j \cos(\omega_j t)\right] + \sum_{k} c_k \cdot H(t - t_k) + \epsilon_i(t)$$

| Component (Komponen) | Symbol | Physical Meaning |
|---|---|---|
| Linear trend | $v$ | Tectonic velocity (mm/yr) |
| Annual signal | $\omega_1 = 2\pi/365.25$ d⁻¹ | Thermal/hydrological loading |
| Semi-annual | $\omega_2 = 2\omega_1$ | Tidal aliasing, atmospheric |
| Offsets | $c_k$ | Antenna change, earthquake, equipment swap |
| Colored noise | $\epsilon_i$ | Flicker + random walk noise |

### 1.2 Stochastic Noise Models

The power spectral density (PSD) of geodetic noise is typically:

$$P(f) = P_0 f^{-\alpha}$$

where $\alpha = 0$ (white noise), $\alpha = 1$ (flicker/1-$f$ noise), or $\alpha = 2$ (random walk). Real GNSS series exhibit a mixture. The maximum likelihood estimation (MLE) approach of Langbein (2004) fits:

$$\text{MLE} = \max_{\theta} \left[-\frac{N}{2}\ln(2\pi) - \frac{1}{2}\ln|\Sigma(\theta)| - \frac{1}{2}(\mathbf{d} - \mathbf{m})^T \Sigma^{-1}(\theta)(\mathbf{d} - \mathbf{m})\right]$$

where $\Sigma(\theta)$ is the covariance matrix parameterized by noise amplitudes $\theta$.

### 1.3 Velocity Uncertainty

Formal velocity uncertainties $\sigma_v$ assuming white noise are typically underestimated by a factor of 2–5 for annual-span series. Correct stochastic modeling yields realistic uncertainties:

$$\sigma_{v,\text{corrected}} \approx \sigma_{v,\text{formal}} \times \sqrt{N/2} \quad \text{(for random-walk-dominated noise)}$$

---

## 2. Spectral Methods (Metode Spektral)

### 2.1 Discrete Fourier Transform

For a uniformly sampled series $x[n]$ with $N$ samples and sampling interval $\Delta t$:

$$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i2\pi kn/N}, \quad k = 0, 1, \ldots, N-1$$

The power spectrum is:

$$P[k] = \frac{|X[k]|^2}{N \cdot \Delta t}$$

Frequency resolution: $\Delta f = 1/(N\Delta t)$.

### 2.2 Periodogram and Welch's Method

The raw periodogram has high variance. Welch's method reduces variance by:

1. Dividing the series into $M$ overlapping segments
2. Windowing each segment (Hanning, Hamming)
3. Computing periodograms and averaging

Variance reduction factor: $\approx M^{-1}$ at the cost of reduced frequency resolution.

### 2.3 Lomb–Scargle Periodogram

For unevenly sampled data (common in geodesy due to data gaps), the Lomb–Scargle periodogram estimates power at frequency $\omega$:

$$P(\omega) = \frac{1}{2} \left[\frac{\left(\sum_j x_j \cos\omega(t_j-\tau)\right)^2}{\sum_j \cos^2\omega(t_j-\tau)} + \frac{\left(\sum_j x_j \sin\omega(t_j-\tau)\right)^2}{\sum_j \sin^2\omega(t_j-\tau)}\right]$$

False alarm probability: $P_{\text{FA}} = 1 - (1 - e^{-z})^M$, where $z = P(\omega)/\langle P \rangle$ and $M$ is independent frequencies.

---

## 3. Filtering (Penyaringan Sinyal)

### 3.1 Common Filters in Geodesy

| Filter (Penyaring) | Passband | Use Case |
|---|---|---|
| Running average (rata-rata bergerak) | Low-pass | Smoothing, removing daily noise |
| Bandpass (Nyquist–annual) | 1/(365 d) to 1/(2 d) | Isolating sub-daily signals |
| Wiener filter | Signal-dependent | Optimal noise removal |
| Kalman filter | Recursive | Real-time deformation monitoring |

### 3.2 Kalman Filter Formulation

State-space model:

$$\mathbf{x}_{k+1} = \mathbf{F}_k \mathbf{x}_k + \mathbf{w}_k, \quad \mathbf{w}_k \sim \mathcal{N}(0, \mathbf{Q}_k)$$
$$\mathbf{z}_k = \mathbf{H}_k \mathbf{x}_k + \mathbf{v}_k, \quad \mathbf{v}_k \sim \mathcal{N}(0, \mathbf{R}_k)$$

Prediction:

$$\hat{\mathbf{x}}_{k|k-1} = \mathbf{F}_{k-1}\hat{\mathbf{x}}_{k-1|k-1}, \quad \mathbf{P}_{k|k-1} = \mathbf{F}_{k-1}\mathbf{P}_{k-1|k-1}\mathbf{F}_{k-1}^T + \mathbf{Q}_{k-1}$$

Update:

$$\mathbf{K}_k = \mathbf{P}_{k|k-1}\mathbf{H}_k^T(\mathbf{H}_k\mathbf{P}_{k|k-1}\mathbf{H}_k^T + \mathbf{R}_k)^{-1}$$
$$\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k(\mathbf{z}_k - \mathbf{H}_k\hat{\mathbf{x}}_{k|k-1})$$

---

## 4. Least-Squares Estimation (Metode Kuadrat Terkecil)

### 4.1 Linear Least Squares

For observation equations $\mathbf{d} = \mathbf{A}\mathbf{x} + \mathbf{e}$, the ordinary least-squares (OLS) solution minimizes $\mathbf{e}^T\mathbf{e}$:

$$\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{d}$$

Covariance: $\Sigma_{\hat{x}} = \sigma_0^2 (\mathbf{A}^T\mathbf{A})^{-1}$, with a posteriori variance $\hat{\sigma}_0^2 = \mathbf{e}^T\mathbf{e}/(n-u)$.

### 4.2 Weighted and Generalized Least Squares

If observations have known covariance $\Sigma_d$:

$$\hat{\mathbf{x}} = (\mathbf{A}^T\Sigma_d^{-1}\mathbf{A})^{-1}\mathbf{A}^T\Sigma_d^{-1}\mathbf{d}$$

### 4.3 Tikhonov Regularization (Ridge Regression)

When $\mathbf{A}^T\mathbf{A}$ is ill-conditioned (poorly conditioned):

$$\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{A} + \lambda^2 \mathbf{I})^{-1}\mathbf{A}^T\mathbf{d}$$

The regularization parameter $\lambda$ is chosen by L-curve or cross-validation.

---

## 5. Hypothesis Testing in Geodesy

### 5.1 F-Test for Model Selection

Comparing two models with $u_1$ and $u_2$ parameters ($u_2 > u_1$):

$$F = \frac{(\mathbf{e}_1^T\mathbf{e}_1 - \mathbf{e}_2^T\mathbf{e}_2)/(u_2 - u_1)}{\mathbf{e}_2^T\mathbf{e}_2/(n - u_2)} \sim F(u_2-u_1, n-u_2)$$

### 5.2 Case Study: Detecting Coseismic Offsets

After the 2018 Lombok earthquake ($M_w$ 6.9), GNSS stations on Lombok measured coseismic offsets. Using a pre-earthquake velocity model and post-earthquake observations:

$$\Delta x_{\text{obs}} = \Delta x_{\text{predicted}}(\text{dislocation model}) + \text{noise}$$

A $\chi^2$ test ($\chi^2 = \Delta\mathbf{x}^T\Sigma^{-1}\Delta\mathbf{x}$) with $p < 0.05$ confirms whether the observed offsets are consistent with Okada elastic dislocation models, validating source parameters used for tsunami hazard assessment (penilaian bahaya tsunami).

---

## References

1. Blewitt, G., & Lavallée, D. (2002). "Effect of annual signals on geodetic velocity," *J. Geophys. Res.*, 107(B7), 2145.
2. Langbein, J. (2004). "Noise in two-color electronic distance meter measurements revisited," *J. Geophys. Res.*, 109, B05406.
3. Williams, S. D. P. (2003). "The effect of coloured noise on the uncertainties of rates estimated from geodetic time series," *J. Geod.*, 76, 483–494.
4. Montgomery, D. C., Peck, E. A., & Vining, G. G. (2012). *Introduction to Linear Regression Analysis*, 5th ed. Wiley.
5. Bogartz, R. S. (2006). "Least Squares for Surveyors," in *Geomatics Techniques*, FIG Commission 6.
6. Djamaluddin, I. et al. (2019). "GNSS crustal deformation in Sulawesi and surrounding regions," *Geod. Geodyn.*, 10(3), 203–211.
