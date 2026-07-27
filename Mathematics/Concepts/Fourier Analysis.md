---
title: Fourier Analysis
type: concept
subject: Mathematics
tags: [mathematics, fourier-analysis, signal-processing, harmonic-analysis]
created: 2026-07-27
updated: 2026-07-27
---

# Fourier Analysis

> *"Fourier analysis is one of the most useful tools in applied mathematics."* — Stein & Shakarchi
> Part of [[Mathematics MOC]]. Central to signal processing, PDEs, image processing, and spectral methods.

## 1. Fourier Series

Any periodic function $f(x) $with period$ 2\pi $can be written: $$ f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)$$ ### Fourier Coefficients $$ a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) \, dx, \quad b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) \, dx $$### Complex Form $$ f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}, \quad c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} \, dx $$

### Convergence

**Dirichlet's Theorem:** If $f$ is piecewise smooth, the Fourier series converges to:

$$\frac{f(x^+) + f(x^-)}{2}

$$ at every point$ x $.

**Parseval's Theorem:**

$$\frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x)|^2 \, dx = |c_0|^2 + 2\sum_{n=1}^{\infty} |c_n|^2

$$

## 2. Fourier Transform

For non-periodic functions on $\mathbb{R} $:

$$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i \xi x} \, dx

$$**Inverse:**$$ f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) e^{2\pi i \xi x} \, d\xi $$

### Properties

| Property | Domain | Frequency Domain |
|----------|--------|-----------------|
| Linearity | $af + bg$ | $a\hat{f} + b\hat{g}$ |
| Time shift | $f(x - x_0)$ | $e^{-2\pi i \xi x_0} \hat{f}(\xi)$ |
| Frequency shift | $e^{2\pi i \xi_0 x} f(x)$ | $\hat{f}(\xi - \xi_0) $ |
| Scaling | $f(ax)$ | $\frac{1}{|a|}\hat{f}(\xi/a) $ |
| Differentiation | $f'(x)$ | $2\pi i \xi \hat{f}(\xi)$ |
| Convolution | $f * g$ | $\hat{f} \cdot \hat{g} $ |
| Multiplication | $f \cdot g$ | $\hat{f} * \hat{g} $ |

### Plancherel Theorem

$$\int_{-\infty}^{\infty} |f(x)|^2 \, dx = \int_{-\infty}^{\infty} |\hat{f}(\xi)|^2 \, d\xi

$$

## 3. Common Transforms

| Function $f(x)$ | Transform $\hat{f}(\xi) $ |
|-------------------|--------------------------|
| $e^{-\pi x^2}$ (Gaussian) | $e^{-\pi \xi^2}$ |
| $\chi_{[-1,1]} $ (rectangle) |$\frac{\sin(2\pi\xi)}{\pi\xi} $ |
| $e^{-\alpha |x|}$ | $\frac{2\alpha}{\alpha^2 + 4\pi^2\xi^2} $ |
| $\delta(x) $ (Dirac delta) |$1$ |
| $1$ | $\delta(\xi) $ |

## 4. Discrete Fourier Transform (DFT)

For $N$ samples $x_0, x_1, \dots, x_{N-1}$:

$$ X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}, \quad k = 0, 1, \dots, N-1 $$**Inverse DFT:**$$ x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k e^{2\pi i kn/N}$$

### Fast Fourier Transform (FFT)

Computes DFT in $O(N \log N)$ instead of $O(N^2)$. Cooley-Tukey algorithm (1965) is one of the most important algorithms in computational mathematics.

## 5. Uncertainty Principle

A function and its Fourier transform cannot both be "localized":

$$\left( \int x^2 |f(x)|^2 \, dx \right) \left( \int \xi^2 |\hat{f}(\xi)|^2 \, d\xi \right) \geq \frac{1}{16\pi^2}

$$

**Heisenberg:** The product of variances of position and momentum is bounded below.

## 6. Wavelets (Brief)

**Short-Time Fourier Transform (STFT):** Windowed Fourier analysis.

$$ STFT_f(g, \tau, \omega) = \int f(t) \overline{g(t-\tau)} e^{-i\omega t} \, dt $$**Wavelet Transform:** Multi-resolution analysis.

$$ W_f(a, b) = \frac{1}{\sqrt{a}} \int f(t) \overline{\psi\left(\frac{t-b}{a}\right)} dt $$

```mermaid
flowchart LR
 Signal[Signal f\(x\)] --> FT[Fourier Transform]
 Signal --> STFT[Short-Time FT]
 Signal --> WT[Wavelet Transform]
 FT --> Freq[Frequency Spectrum]
 STFT --> TF[Time-Frequency]
 WT --> MultiRes[Multi-Resolution]
```

## 7. Applications

| Field | Application |
|-------|-------------|
| **Signal Processing** | Filtering, spectral analysis, compression |
| **Image Processing** | JPEG (DCT), image filtering |
| **PDEs** | Separation of variables, heat equation solution |
| **Number Theory** | Riemann zeta function |
| **Quantum Mechanics** | Position-momentum duality |
| **Geodesy** | Spectral analysis of time series, tidal analysis |

## Practice Problems

1. Find the Fourier series of the square wave $f(x) = \text{sgn}(x)$ on $[-\pi, \pi]$.
2. Compute the Fourier transform of the Gaussian $f(x) = e^{-x^2/2}$.
3. Show that the convolution theorem holds: $\widehat{f*g} = \hat{f} \cdot \hat{g}$.
4. Implement a DFT and FFT in Python and compare timing.

## References

- Stein, E.M. & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton.
- Bracewell, R.N. (2000). *The Fourier Transform and Its Applications*. McGraw-Hill.
- Strang, G. (1994). *Wavelets and Filter Banks*. Wellesley-Cambridge.

---
*See also: [[Differential Equations]], [[Complex Analysis]], [[Probability Distributions]], [[Numerical Methods]]*
