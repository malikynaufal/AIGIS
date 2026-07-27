---
title: "Pemrosesan Sinyal Digital"
subject: "Fisika Pilihan"
tags:
  - signal-processing
  - Fourier
  - DSP
  - filters
  - SKS: 3
---

# FKD214705 — Pemrosesan Sinyal Digital
**Digital Signal Processing** | 3 SKS (Satuan Kredit Semester)

## Overview

Digital signal processing (pemrosesan sinyal digital, DSP) is the mathematical backbone of modern measurement systems, from seismic data analysis to remote sensing and communications. This course covers the discrete Fourier transform and its fast implementation, FIR and IIR filter design, spectral analysis techniques, and noise reduction strategies. Students will learn to implement DSP algorithms in Python/MATLAB and apply them to real geophysical and engineering signals.

---

## 1. Fourier Transform for Discrete Signals (Transformasi Fourier Diskrit)

### 1.1 DTFT, DFT, and FFT

The **Discrete-Time Fourier Transform (DTFT)** provides the frequency-domain representation of a discrete sequence $x[n]$:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

For finite-length sequences of $N$ points, the **Discrete Fourier Transform (DFT)** samples the DTFT at $N$ equally-spaced frequencies:

$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}, \quad k = 0, 1, \ldots, N-1$$

The inverse DFT (IDFT) recovers the time-domain signal:

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] e^{j2\pi kn/N}$$

### 1.2 Fast Fourier Transform (FFT)

The Cooley–Tukey FFT algorithm reduces DFT complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(N\log_2 N)$. For a 1-million-point signal:

- DFT: $10^{12}$ operations (impractical)
- FFT: $\approx 2 \times 10^7$ operations (real-time feasible)

### 1.3 Important Properties

| Property (Sifat) | Time Domain | Frequency Domain |
|---|---|---|
| Linearity | $ax[n] + by[n]$ | $aX[k] + bY[k]$ |
| Time shift | $x[n - n_0]$ | $X[k] \cdot e^{-j2\pi kn_0/N}$ |
| Convolution | $x[n] * h[n]$ | $X[k] \cdot H[k]$ |
| Parseval's theorem | $\sum |x[n]|^2$ | $\frac{1}{N}\sum |X[k]|^2$ |
| Symmetry (real input) | — | $X[k] = X^*[N-k]$ |

### 1.4 Spectral Leakage and Windowing

When $N$ does not exactly contain an integer number of signal periods, spectral leakage (kebocoran spektrum) occurs. Windowing reduces this effect:

$$x_w[n] = x[n] \cdot w[n]$$

Common windows (jendela):

| Window | Main Lobe Width | Side Lobe Level | Use Case |
|---|---|---|---|
| Rectangular | $2/N$ | −13 dB | When no leakage expected |
| Hanning | $4/N$ | −31 dB | General purpose |
| Hamming | $4/N$ | −43 dB | Better side lobe rejection |
| Blackman | $6/N$ | −58 dB | Narrowband signals |
| Kaiser ($\beta=8$) | Variable | −50 dB | Tunable trade-off |

---

## 2. FIR Filters (Penyaring FIR)

### 2.1 Definition and Properties

A Finite Impulse Response (FIR) filter of order $N$:

$$y[n] = \sum_{k=0}^{N} b_k \, x[n-k]$$

**Advantages**: Always stable (stabil), linear phase possible, no feedback. **Disadvantage**: Requires high order for sharp cutoff.

### 2.2 Linear Phase Condition

FIR filters have linear phase when the coefficients are symmetric: $b_k = b_{N-k}$. This ensures all frequency components experience the same group delay:

$$\tau_g(\omega) = -\frac{d\phi(\omega)}{d\omega} = \frac{N}{2} \quad \text{(constant)}$$

### 2.3 Design Methods

**Window method**: Design by truncating the ideal impulse response with a window.

Example — Lowpass filter with cutoff $f_c = 1$ kHz at $f_s = 8$ kHz:

$$h_{\text{ideal}}[n] = \frac{\sin(\omega_c(n - N/2))}{\pi(n - N/2)}, \quad \omega_c = 2\pi f_c / f_s$$

Using a Hamming window of length $N = 31$:

$$h[n] = h_{\text{ideal}}[n] \cdot w_{\text{Hamming}}[n], \quad 0 \leq n \leq N-1$$

**Parks–McClellan (Remez exchange)**: Optimal equiripple design minimizing:

$$\max_\omega |H(e^{j\omega}) - H_d(e^{j\omega})| \quad \text{in the weighted Chebyshev sense}$$

---

## 3. IIR Filters (Penyaring IIR)

### 3.1 Definition

An Infinite Impulse Response filter uses both input and output history:

$$y[n] = \sum_{k=0}^{M} b_k\, x[n-k] - \sum_{k=1}^{L} a_k\, y[n-k]$$

Transfer function:

$$H(z) = \frac{B(z)}{A(z)} = \frac{b_0 + b_1 z^{-1} + \cdots + b_M z^{-M}}{1 + a_1 z^{-1} + \cdots + a_L z^{-L}}$$

### 3.2 Analog-to-Digital Filter Design

IIR design starts from an analog prototype and applies a bilinear transform:

**Bilinear transform** (transformasi bilineal):

$$z = \frac{1 + sT/2}{1 - sT/2}$$

This maps the left-half $s$-plane to the inside of the unit circle, preserving stability. Frequency warping:

$$\omega_d = \frac{2}{T}\tan\left(\frac{\omega_a T}{2}\right)$$

### 3.3 Common IIR Types

| Type | Characteristics (Karakteristik) |
|---|---|
| Butterworth | Maximally flat magnitude; no ripples in passband |
| Chebyshev Type I | Equiripple in passband; steeper rolloff than Butterworth |
| Chebyshev Type II | Equiripple in stopband; flat passband |
| Elliptic (Cauer) | Equiripple in both; sharpest rolloff for given order |
| Bessel | Maximally flat group delay; preserved waveform shape |

### 3.4 Stability Criterion

An IIR filter is stable (stabil) if all poles lie inside the unit circle in the $z$-plane:

$$|p_i| < 1 \quad \forall \; i = 1, 2, \ldots, L$$

---

## 4. Spectral Analysis and Noise Reduction

### 4.1 Power Spectral Density Estimation

**Welch's averaged periodogram**: Segment the signal into $M$ overlapping blocks, window each, compute $\frac{1}{N_w}|X_i[k]|^2$, and average:

$$\hat{P}_{\text{Welch}}[k] = \frac{1}{M}\sum_{i=1}^{M} \frac{|X_i[k]|^2}{N_w \cdot U}$$

where $U = \frac{1}{N_w}\sum w^2[n]$ is the window power correction factor.

### 4.2 Spectral SNR Enhancement

For a signal buried in white noise, coherent averaging of $M$ segments improves SNR:

$$\text{SNR}_{\text{improved}} = \text{SNR}_{\text{input}} + 10\log_{10}(M) \;\text{dB}$$

### 4.3 Wavelet Denoising (Pengurangan Noise Wavelet)

The discrete wavelet transform (DWT) decomposes a signal into multi-resolution scales. Denoising proceeds by:

1. Decompose $x[n]$ into wavelet coefficients $w_j[k]$
2. Threshold coefficients: $\hat{w}_j[k] = \text{sign}(w_j[k]) \cdot \max(|w_j[k]| - \lambda, 0)$ (soft thresholding)
3. Reconstruct $\hat{x}[n]$ from thresholded coefficients

The universal threshold (Donoho & Johnstone):

$$\lambda = \sigma \sqrt{2 \ln N}$$

---

## 5. Worked Example: Seismic Signal Enhancement

**Problem**: Extract a P-wave arrival buried in microseismic noise at SNR = 3 dB.

**Solution steps**:

1. **Spectral analysis**: Compute Welch PSD; identify signal band at 2–10 Hz, noise band at 0.1–2 Hz
2. **Bandpass FIR filter**: Design 2–10 Hz passband (order 100, Hamming window)
3. **Apply filter** using `scipy.signal.filtfilt` for zero-phase filtering:

```python
from scipy.signal import firwin, filtfilt
b = firwin(101, [2, 10], pass_zero=False, fs=100)
y = filtfilt(b, 1, x)
```

4. **Result**: SNR improves from 3 dB to ~18 dB (15 dB gain from filtering + coherent stacking)
5. **Pick P-wave**: Onset clearly visible; automated STA/LTA picks arrival with ±0.1 s accuracy

---

## References

1. Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-Time Signal Processing*, 3rd ed. Pearson.
2. Proakis, J. G., & Manolakis, D. G. (2007). *Digital Signal Processing*, 4th ed. Pearson.
3. Oppenheim, A. V., & Willsky, A. S. (2013). *Signals and Systems*, 2nd ed. Pearson.
4. Haykin, S. (2014). *Adaptive Filter Theory*, 5th ed. Pearson.
5. Donoho, D. L., & Johnstone, I. M. (1994). "Ideal spatial adaptation by wavelet shrinkage," *Biometrika*, 81(3), 425–455.
6. Widodo, S. (2018). *Pengolahan Sinyal Digital untuk Aplikasi Geofisika*. ITB Press.
