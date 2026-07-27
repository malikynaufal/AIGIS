---
tags: [aigis, concept, physics, signal-processing, fourier-analysis, filtering]
created: 2026-07-27
updated: 2026-07-27
---

# Signal Processing

## Fourier Transform, Filtering, Spectral Analysis, Noise, and Sampling Theorem

**Core Idea:** Signal processing extracts meaningful information from measured data by separating signals from noise, analyzing frequency content, and applying mathematical transformations. It is the backbone of GNSS positioning, geophysical data analysis, and all precision measurement systems.

---

## 1. Signals and Systems

### Signal Classification

| Property | Types | Example |
|----------|-------|---------|
| **Continuous vs Discrete** | $f(t) $ vs $ f[nT] $ | Analog vs digital |
| **Periodic vs Aperiodic** | $ f(t) = f(t+T) $ vs $ f(t) \to 0$ | Carrier wave vs pulse |
| **Deterministic vs Stochastic** | Known function vs random process | Sine wave vs noise |
| **Energy vs Power** | Finite $ \int |f|^2 dt $ vs $ |f|^2 $ bounded | Transient vs steady-state |

### Energy and Power
**Energy signal:*
*

$ E = \int_{-\infty}^{\infty} |f(t)|^2 \, dt \quad [\text{finite, aperiodic}] $$$

**Power signal:*
*

$ P = \lim_{T\to\infty} \frac{1}{T}\int_{-T/2}^{T/2} |f(t)|^2 \, dt \quad [\text{finite, periodic}] $ $ **Parseval's Theorem** (Energy conservation) $

$$ \int_{-\infty}^{\infty}|f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^2 d\omega = \int_{-\infty}^{\infty}|F(f)|^2 df

$ $

---

## 2. Fourier Transform

### Continuous Fourier Transfor
m

$$ F(\omega) = \mathcal{F}\{f(t)\} = \int_{-\infty}^{\infty} f(t) \, e^{-i\omega t} \, dt $ $

**Inverse:*
*

$$ f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega) \, e^{i\omega t} \, d\omega $ $

### Discrete Fourier Transform (DFT)
For $ N $ samples $ x[n] $ at times $ t_n = nT $:

$ $

X[k] = \sum_{n=0}^{N-1} x[n] \, e^{-i 2\pi kn/N
}

**Inverse DFT:** x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] \, e^{i 2\pi kn/N} $$ $ $

$$

**Fast Fourier Transform (FFT):**$ O(N\log N) $ algorithm for DFT computation.

### Key Fourier Properties
| Property | Time Domain | Frequency Domain |
|----------|-------------|------------------|
| Linearity | $ ax + by $ | $ aX + bY $ |
| Time shift | $ x[n - n_0] $ | $ X[k] \cdot e^{-i2\pi kn_0/N} $ |
| Frequency shift | $ x[n] \cdot e^{i2\pi kn_0/N} $ | $ X[k - k_0] $ |
| Convolution | $ (x * h)[n] = \sum_m x[m]h[n-m] $ | $ X[k] \cdot H[k] $ |
| Multiplication | $ x[n] \cdot h[n] $ | $ \frac{1}{N}(X * H)[k] $ (circular) |
| Differentiation | $ \frac{dx}{dt} $ | $ i\omega \cdot X(\omega) $ |

### Fourier Pairs (Important)
| Time Domain | Frequency Domain | Bandwidth |
|-------------|------------------|-----------|
| $ \delta(t) $ (impulse) | 1 | $ \infty $ (white) |
| $ \text{rect}(t/T) $ (gate) | $ T\text{sinc}(\pi fT) $ | $ \sim 1/T $ |
| $ e^{-at}u(t) $ (exponential) | $ \frac{1}{a+j\omega} $ | $ \sim a $ |
| $ e^{-at^2} $ (Gaussian) | $ \sqrt{\pi/a}\, e^{-\omega^2/4a} $ | $ \sim \sqrt{a} $ |
| $ e^{j\omega_0 t} $ (carrier) | $ 2\pi\delta(\omega - \omega_0) $ | 0 (monochromatic) |

---

## 3. Spectral Analysis

### Power Spectral Density (PSD)
The PSD describes how signal power is distributed across frequency

$ S_{xx}(f) = \lim_{T\to\infty} \frac{1}{T}|F_T(f)|^2 $$$

**Wiener-Khinchin Theorem:*
*

$ S_{xx}(f) = \mathcal{F}\{R_{xx}(\tau)\} $ where $ R_{xx}(\tau) = E[x(t)x(t+\tau)] $= autocorrelation function.

### Welch's Method (Practical PSD Estimation)
1. Divide signal into overlapping segments
2. Window each segment (Hamming, Hanning, Blackman)
3. Compute FFT of each segment
4. Average magnitude-squared spectr
a

$ $ \hat{S}_{xx}(f) = \frac{1}{K}\sum_{k=1}^{K}\frac{|X_k(f)|^2}{M
}

**### Spectral Resolution **

 \Delta f = \frac{1}{T} = \frac{f_s}{N}

$$

- For 1-hour GNSS observation at 30 s sampling ( $ N=120 $): $ \Delta f \approx 0.028 $ mHz

- Longer observation → better spectral resolution

### Cross-Spectral Densit
y

$ S_{xy}(f) = \mathcal{F}\{R_{xy}(\tau)\} = \mathcal{F}\{E[x(t)y(t+\tau)]\} $$$

**Coherence function:*
*

$ $ \gamma_{xy}^2(f) = \frac{|S_{xy}(f)|^2}{S_{xx}(f)S_{yy}(f)} $$

Measures linear correlation in the frequency domain.$ \gamma^2 = 1 $: perfect linear relationship.

---

## 4. Filtering

### Filter Classifications

| Type | Passes | Rejects |
|------|--------|---------|
| **Low-pass (LPF)** | $ |f| < f_c $ | $ |f| > f_c $ |
| **High-pass (HPF)** | $ |f| > f_c $ | $ |f| < f_c $ |
| **Band-pass (BPF)** | $ f_1 < |f| < f_2 $ | Outside |
| **Band-stop (notch)** | Outside $ f_1 $– $ f_2 $ | $ f_1 < |f| < f_2 $ |

### Ideal vs Real Filters
| Property | Ideal | Real |
|----------|-------|------|
| Attenuation | 0 dB pass,$-\infty $ dB stop | 0.1–3 dB pass, 20–80 dB/decade stop |
| Transition | Infinitely sharp | Finite roll-off |
| Phase | Zero (infinite order) | Non-zero (introduces distortion) |
| Realization | Non-causal (infinite delay) | Causal (finite delay) |

### FIR vs IIR Filters

**FIR (Finite Impulse Response):*
*

$ $ y[n] = \sum_{k=0}^{M} h[k] x[n-k] $$

- **Stable:** always (no feedback)

- **Linear phase:** symmetric impulse response $ h[k] = h[M-k] $- **Drawback:** Requires more taps for sharp cutoff

**IIR (Infinite Impulse Response):*
*

$ $ y[n] = \sum_{k=0}^{M} a_k x[n-k] - \sum_{k=1}^{N} b_k y[n-k] $$

- More efficient (fewer coefficients for same response)

- Can have nonlinear phase (phase distortion)

- Potential stability issues (poles inside unit circle)

### Common Filter Designs

- **Butterworth:** Maximally flat passband (no ripple)

- **Chebyshev Type I:** Equiripple passband, monotonic stopband

- **Chebyshev Type II:** Monotonic passband, equiripple stopband

- **Elliptic (Cauer):** Equiripple both passband and stopband, sharpest transition

---

## 5. Noise in Signals

### Noise Types

| Type | PSD | Character | Source |
|------|-----|-----------|--------|
| **White** | $ S(f) = S_0 $ (constant) | Uncorrelated | Thermal noise, quantization |
| **Pink (1/f)** | $ S(f) \propto 1/f $ | Correlated | Flicker, oscillator drift |
| **Brownian (1/f²)** | $ S(f) \propto 1/f^2 $ | Random walk | Clock drift, wander |
| **Blue** | $ S(f) \propto f $ | Anti-correlated | Differentiation noise |
| **Band-limited white** | Flat within band, zero outside | Band-limited | ADC noise floor |

### Signal-to-Noise Ratio (SNR
)

$ $ \text{SNR} = \frac{P_{\text{signal}}}{P_{\text{noise}}} = \frac{S_{ss}(f)}{S_{nn}(f)} $$

In dB $ $

 \text{SNR}_{\text{dB}} = 10\log_{10}\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right)

$$

# ## Noise Reduction by Averaging
For $ N $ uncorrelated measurements, averaging reduces noise by $ \sqrt{N} $:

$ $ \sigma_{\bar{x}} = \frac{\sigma_x}{\sqrt{N}} $$

**GNSS example:** 1-hour post-processed solution (120 epochs at 30 s): noise reduced by $ \sqrt{120} \approx 11 $×.

### Allan Variance (Time-Frequency Stability)
Used to characterize noise processes in clocks and sensors

$ $ \sigma_y^2(\tau) = \frac{1}{2}\langle (y_{n+1} - y_n)^2\rangle

$$

| Slope on log-log plot | Noise type | Physical meaning |
|-----------------------|-----------|------------------|
| $-1 $ | White phase | Measurement noise |
| $ 0 $ | Flicker phase | 1/f type |
| $+1 $ | Random walk phase | Clock drift |
| $-1/2 $ | White frequency | White noise in clock |
| $ 0 $ | Flicker frequency | $ 1/f $ frequency noise |
| $+1/2 $ | Random walk frequency | Frequency drift |

---

## 6. Sampling and Quantization

### Nyquist-Shannon Sampling Theore
m

$ $ \boxed{f_s \geq 2f_{\text{max}}} $$

If sampling rate is below $ 2f_{\text{max}} $: **aliasing** occurs — frequencies $  f > f_s/2 $ fold back to $ f_s - f $.

**Anti-aliasing filter:** Low-pass with cutoff $ f_c = f_s/2 $ applied before ADC.

### Oversampling and Undersampling

- **Oversampling ( $ f_s \gg 2f_{\text{max}} $):** Improves effective resolution, relaxes analog filter requirements
 - SNR improvement: $ \Delta\text{SNR} = 10\log_{10}(n/1) $ dB for $  n $-times oversampling
 - Resolution improvement: ~1 bit per doubling of oversampling rate

- **Undersampling (sub-Nyquist):** Intentional aliasing of bandpass signal — used in bandpass sampling for RF signals

### Quantization Noise
For $ N $-bit ADC with full scale $ 2V_{\text{ref}} $:

$ $ \text{SNR}_{\text{quantization}} = 6.02N + 1.76 \text{ dB} $$

**Example:** 16-bit ADC → SNR = 96.1 + 1.76 = 97.9 dB

### Effective Number of Bits (ENOB
)

$ $ \text{ENOB} = \frac{\text{SINAD (dB)} - 1.76}{6.02} $$

where SINAD = Signal-to-Noise-and-Distortion ratio.

---

## 7. Time Series Analysis

### Autocorrelation Functio
n

$ R_{xx}(\tau) = E[x(t)x(t+\tau)] = \lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}x(t)x(t+\tau)\,dt $$$

**Properties:**
- $ R_{xx}(0) = \sigma_x^2 + \mu_x^2 $ (maximum)
- $ R_{xx}(-\tau) = R_{xx}(\tau) $ (even function)
-$ |R_{xx}(\tau)| \leq R_{xx}(0) $### Spectral Windowing
Raw FFT of finite-length data → spectral leakage. Window functions reduce sidelobes:

| Window | Main lobe width | Side lobe level | Use |
|--------|----------------|-----------------|-----|
| Rectangular | Narrowest | -13 dB | No windowing (transient) |
| Hamming | 2× rectangular | -43 dB | General purpose |
| Hanning | 2× rectangular | -31 dB | Continuous signals |
| Blackman | 4× rectangular | -58 dB | Strong sidelobe rejection |
| Kaiser (β=5) | Variable | Variable | Tunable, adaptive |

**Leakage reduction:** Apply window $ w[n] $ before FFT: $ X[k] = \sum x[n]w[n]e^{-i2\pi kn/N} $### Cross-Correlation and Deconvolutio
n

$ R_{xy}(\tau) = E[x(t)y(t+\tau)] $$$

Used in:

- **GNSS:** Code tracking (correlate received code with local replica)

- **Seismology:** Cross-correlate seismograms for travel time analysis

- **Remote sensing:** Matched filtering for weak signal detection

### Deconvolution
Given $ y(t) = x(t) * h(t) $, recover $ x(t) $:

$ $ X(\omega) = \frac{Y(\omega)}{H(\omega)} $$

Requires knowledge of impulse response $ $ h(t) $. Sensitive to noise in $ H(\omega) $ near zero.$

---

## 8. Applications in Geodesy and GNSS

### GNSS Signal Processing

- **Carrier tracking loop (PLL):** Tracks L1 carrier phase with precision ~1 mm

- **Code tracking loop (DLL):** Tracks C/A code with precision ~1 m

- **Pseudorange computation:** Code delay × c → satellite-to-receiver range

### Precise Point Positioning (PPP)

- Requires sub-centimeter carrier phase precision

- **Kalman filter** estimates: position, clock bias, tropospheric zenith delay, ionosphere, ambiguities

- **Convergence time:** ~30 min (with dual-frequency + ionosphere-free combination)

### Geophysical Signal Processing

- **Seismic data:** FFT for frequency analysis, wavelet transform for time-frequency localization

- **Gravity data:** Filter long-wavelength (tectonics) vs. short-wavelength (bouguer anomalies)

- **Temperature time series:** Spectral analysis for climate oscillations (El Niño, QBO)

### Kalman Filter (Optimal Estimation)
State-space formulation for real-time estimation:

$ $ \text{State model: } \vec{x}_k = F_k\vec{x}_{k-1} + B_k\vec{u}_k + \vec{w}_k, \quad \vec{w}_k \sim \mathcal{N}(0, Q_k)\text{Measurement model: } \vec{z}_k = H_k\vec{x}_k + \vec{v}_k, \quad \vec{v}_k \sim \mathcal{N}(0, R_k
)

**Update:**

K_k = P_{k|k-1}H_k^T(H_kP_{k|k-1}H_k^T + R_k)^{-1}\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k(\vec{z}_k - H_k\hat{x}_{k|k-1}) $$

Used in: GNSS navigation solution, PPP ambiguity resolution, inertial navigation integration.

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $ F(\omega) = \int f(t)e^{-i\omega t}dt $ | Fourier transform | Frequency analysis |
| $ f_s \geq 2f_{\text{max}} $ | Nyquist theorem | Sampling rate |
| $ \sigma_{\bar{x}} = \sigma/\sqrt{N} $ | Noise reduction | Averaging |
| $ \text{SNR} = 6.02N + 1.76 $ dB | ADC SNR | Quantization noise |
| $ \gamma_{xy}^2 = \|S_{xy}\|^2/(S_{xx}S_{yy}) $ | Coherence | Frequency correlation |
| $ K = P H^T(HPH^T + R)^{-1} $ | Kalman gain | Optimal estimation |

---

## Problems
1. Compute the DFT of the sequence $ x[n] = \{1, 1, 1, 1, 0, 0, 0, 0\} $ and interpret the frequency components.
2. A GPS L1 carrier (1575.42 MHz) is sampled at 1 GHz — is this Nyquist-compliant? What about aliasing?
3. Design an anti-aliasing filter for 30-second GPS data acquisition with significant signals up to 0.0167 Hz.
4. Compute the Allan variance of a random walk noise with sampling interval $ \tau_0 = 1 $  s and $\sigma = 1 $ m.
5. Derive the SNR improvement from 10× oversampling a 16-bit ADC.
6. Explain the difference between FIR and IIR filters — advantages and disadvantages for GNSS filtering.
7. Compute the cross-correlation between two sine waves at slightly different frequencies and explain the beat phenomenon.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
