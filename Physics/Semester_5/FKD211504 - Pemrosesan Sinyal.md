---
code: FKD211504
name: Pemrosesan Sinyal
SKS: 3
semester: 5
department: Fisika/Informatika
tags: [signal-processing, fourier-analysis, filtering, time-series]
created: 2026-07-27
---

# FKD211504 — Pemrosesan Sinyal

## Course Overview

Signal processing is the art of extracting information from measurements. This course covers Fourier analysis, filtering, spectral estimation, and digital signal processing fundamentals. Signal processing is a prerequisite for understanding GNSS signal structure, geophysical data analysis, and any physics involving measurement and data interpretation.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour lab per week)
**Prerequisites:** Kalkulus II, Persamaan Diferensial, Elektromagnetik
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Continuous-Time Signals and Systems (Weeks 1–4)

- **Signals:** continuous vs. discrete, periodic vs. aperiodic, even vs. odd

- **Energy and power** of signals

- **Unit step function u(t)** and Dirac delta δ(t)

- **Linear time-invariant (LTI) systems:** fundamental properties

- **Convolution:** y(t) = x(t) * h(t) = ∫ x(τ)h(t-τ)dτ

- **Complex exponentials** as eigenfunctions of LTI systems

### Unit 2: Fourier Analysis (Weeks 5–9)

- **Fourier series:** represent periodic signals as sum of sines/cosines
  ```
  x(t) = a₀/2 + Σ_{n=1}∞ [a_n cos(nω₀t) + b_n sin(nω₀t)]
  ```
  - Coefficients from orthogonality of trigonometric functions

- **Fourier transform (FT):**
  ```
  X(ω) = ∫_{-∞}^{∞} x(t) e^{-iωt} dt
  x(t) = (1/2π) ∫_{-∞}^{∞} X(ω) e^{iωt} dω
  ```

- **Key Fourier transform pairs:**
  - δ(t) ↔ 1 (impulse contains all frequencies)
  - rect(t) ↔ sinc(ω/2) — rectangular ↔ sinc function
  - e^{-at}u(t) ↔ 1/(a + iω) (exponential decay)

- **Properties:** linearity, time shift (= phase shift), frequency shift, scaling, duality

- **Parseval's theorem:** ∫|x(t)|²dt = (1/2π)∫|X(ω)|²dω

### Unit 3: Sampling and Discrete-Time Processing (Weeks 10–13)

- **Sampling theorem (Nyquist-Shannon):** need f_s > 2f_max
  - **Nyquist rate:** f_N = 2f_max
  - Aliasing: if undersampled, high frequencies masquerade as low

- **Discrete-time Fourier transform (DTFT):** X(Ω) = Σ x[n] e^{-iΩn}

- **Discrete Fourier transform (DFT):** for finite-length sequences
  - X[k] = Σ_{n=0}^{N-1} x[n] e^{-i2πkn/N}, k = 0,...,N-1

- **Fast Fourier Transform (FFT):** O(N log N) algorithm vs. O(N²) for DFT

- **Spectrogram:** time-frequency representation (short-time FT)

### Unit 4: Filtering and Applications (Weeks 14–16)

- **Filter types:**
  - Low-pass, high-pass, band-pass, band-stop
  - **Butterworth filters:** maximally flat passband
  - Chebyshev and elliptic filters (steeper roll-off, ripple in passband)

- **Digital filter design:**
  - FIR (finite impulse response): always stable, linear phase
  - IIR (infinite impulse response): more efficient, can be unstable

- **Measurement noise:** distinguishing signal from noise
  - Signal-to-noise ratio (SNR) and filtering trade-offs

- **Applications in physics:**
  - GNSS signal processing: correlation, acquisition, tracking
  - Seismic data filtering
  - Instrument response correction
  - Time series smoothing and prediction

---

## 🔬 Key Operations

```
Convolution:        y(t) = x(t) * h(t) = ∫x(τ)h(t-τ)dτ
Fourier:            X(ω) = ∫x(t)e^{-iωt}dt
Nyquist:            f_s ≥ 2f_max
DFT:                X[k] = Σ x[n]e^{-i2πkn/N}
Real convolution in time = multiplication in frequency
Real multiplication in time = convolution in frequency
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Compute Fourier series and Fourier transforms of standard signals
2. Apply the convolution theorem to analyze LTI systems
3. Understand sampling theory and avoid aliasing in data acquisition
4. Implement the FFT for spectral analysis of measured signals
5. Design and apply digital filters to real-world data
6. Apply signal processing to GNSS and geophysical measurements

---

## 📚 References

1. Oppenheim, A.V. & Willsky, A.S. (1996). *Signals and Systems*, 2nd ed. Prentice Hall.
2. Proakis, J.G. & Manolakis, D.G. (2006). *Digital Signal Processing*, 4th ed. Pearson.
3. Lyons, R.G. (2010). *Understanding Digital Signal Processing*, 3rd ed. Prentice Hall.
4. Smith, S.W. (2002). *Digital Signal Processing: A Practical Guide*. Newnes. (Free online)
5. MIT OCW 6.003 Signals and Systems: https://ocw.mit.edu
