---
title: "MGM214704 - Simulasi Monte Carlo"
subject: "Matematika Terapan / Geodesi"
tags: [monte-carlo, simulation, random-sampling, integration, markov-chain]
course_code: "MGM214704"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214704 - Simulasi Monte Carlo

## Monte Carlo Simulation

**Course Code:** MGM214704
**SKS:** 3 (3-0)
**Semester:** 5
**Prerequisites:** Probabilitas & Statistika, Algoritma Pemrograman

---

## Overview / Gambaran Umum

Metode Monte Carlo adalah kelas teknik komputasi stokastik (stochastic) yang menggunakan pengambilan sampel acak (random sampling) untuk menyelesaikan masalah matematika dan fisika secara numerik. Nama ini diambil dari Kasino Monte Carlo, Monaco. Teknik ini sangat kuat untuk menghitung integral dimensi tinggi, simulasi fisika, analisis risiko, dan — dalam konteks geodesi — estimasi properti statistik dari distribusi error pengukuran, analisis uncertainty model elevasi, dan simulasi propagasi orbit satelit.

> **Catatan:** "Metode Monte Carlo tidak menghilangkan kompleksitas — mereka mengubahnya dari deterministik menjadi stokastik." — *Prinsip Utama Metode Komputasional*

---

## 1. Dasar Pengambilan Sampel Acak

### 1.1 Angka Acak Pseudo-Random (PRNG)

Metode Monte Carlo bergantung pada kualitas generator bilangan acak:

| Metode | Periode | Status |
|--------|---------|--------|
| **Linear Congruential Generator (LCG)** | $2^{32} $atau$2^{48} $ | ❌ Lemah, period pendek |
| **Mersenne Twister (MT19937)** | $2^{19937}-1$ | ✅ Bagus untuk simulasi |
| **PCG** (Permuted Congruential Generator) | $2^{128}$ | ✅ Lebih baik, state kecil |
| **XorShift128+** | $2^{128}-1$ | ✅ Sangat cepat |
| **Cryptographic CSPRNG** | — | Untuk keamanan, bukan simulasi |

**LCG definisi:*
*

$$ X_{n+1} = (aX_n + c) \bmod m $$ Parameter Park-Miller minimal standar:$ m = 2^{31}-1 $,$a = 48271$,$c = 0$.

### 1.2 Transformasi Invers

Untuk menghasilkan variabel $X $dengan CDF $F_X$, langkah:
1. Generate $U \sim \text{Uniform}(0,1)$.
2. Hitung $X = F_X^{-1}(U)$.

**Contoh: Eksponensial** $X \sim \text{Exp}(\lambda)$:

$$

F(x) = 1 - e^{-\lambda x} \implies X = -\frac{1}{\lambda}\ln(U
)

$$**Contoh: Normal (Box-Muller Transform):**$$ Z_0 = \sqrt{-2\ln U_1}\cos(2\pi U_2)Z_1 = \sqrt{-2\ln U_1}\sin(2\pi U_2)$$ menghasilkan$ Z_0, Z_1 \sim \mathcal{N}(0,1) $ secara independen.

### 1.3 Metode Lain untuk Sampel dari Distribusi

| Metode | Distribusi | Prinsip |
|--------|-----------|---------|
| **Accept-Reject** | Semua (yang $f(x) \leq M \cdot g(x) $) | Reject dengan probabilitas tertentu |
| **Box-Muller** | Normal | Transformasi polar koordinat |
| **Marsaglia Polar** | Normal | Tanpa trigonometri |
| **Ziggurat** | Normal/eksponensial | Lebih cepat dari Box-Muller |
| **Metropolis-Hastings** | Arbitrary (markov chain) | Core MCMC |

---

## 2. Integrasi Monte Carlo

### 2.1 Estimasi Dasar

Untuk menghitung integral:

$$ I = \int_a^b f(x) \, dx $$**Monte Carlo sederhana:** Generate $N $sampel $x_1, \dots, x_N \sim \text{Uniform}(a, b)$:

$$\hat{I} = \frac{b-a}{N} \sum_{i=1}^{N} f(x_i
)

$$**Error standar:**$$\sigma_{\hat{I}} = \frac{(b-a)\sigma_f}{\sqrt{N}}

$$ di mana $\sigma_f $= standar deviasi $f$. Perhatikan: **error menurun dengan$1/\sqrt{N}$, tidak bergantung dimensi!**

### 2.2 Importance Sampling

Alih-alih sampling uniform, gunakan distribusi proposal $g(x)$:

$$

I = \int_a^b f(x) \, dx = \int_a^b \frac{f(x)}{g(x)} g(x) \, d
x

$$**Estimator:**$$\hat{I} = \frac{1}{N} \sum_{i=1}^{N} \frac{f(x_i)}{g(x_i)}, \quad x_i \sim g

$$ Optimal jika$ g(x) \propto |f(x)| $. Variansi minimum tercapai.

### 2.3 Variance Reduction Techniques

| Teknik | Pricipe | Reduksi Variansi |
|--------|---------|------------------|
| **Antithetic Variates** | Gunakan $U $dan $1-U$|$\text{Cov}(f(U), f(1-U)) < 0 $ |
| **Control Variates** | Gunakan fungsi $h $dengan integral diketahui | $\hat{I} = \hat{I}_f - c(\hat{I}_h - \int h) $ |
| **Stratified Sampling** | Bagi domain, sample per strata | Mengurangi variance jika f vary per strata |
| **Latin Hypercube** | Setiap dimensi divided sama banyak | Lebih efisien dari random untuk dimensi tinggi |

### 2.4 Contoh: Menghitung $\pi $ dengan Monte Carlo

Dalam kuadrat $[-1,1] \times [-1,1]$, lingkaran satuan $x^2 + y^2 \leq 1 $memiliki luas $\pi $.

$$\frac{\pi}{4} \approx \frac{\text{titik di dalam lingkaran}}{N} \implies \hat{\pi} = \frac{4}{N}\sum_{i=1}^{N} \mathbf{1}(x_i^2 + y_i^2 \leq 1)

$$```python
import numpy as np

N = 10_000_000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
inside = np.sum(x**2 + y**2 <= 1)
pi_est = 4 * inside / N
se = 4 * np.sqrt((inside/N) * (1 - inside/N) / N)
print(f"π ≈ {pi_est:.6f} ± {se:.6f}")

# Output: π ≈ 3.141648 ± 0.000154

### 2.5 Integral Multidimensi

Kekuatan utama Monte Carlo: error tetap $O(1/\sqrt{N})$terlepas dimensi.

Integral di mana metode kuadratur (Simpson, Gauss) gagal karena curse of dimensionality

$$ I = \int_0^1 \int_0^1 \cdots \int_0^1 f(x_1, \dots, x_d) \, dx_1 \cdots dx_d $$ Untuk$ d > 4 $, Monte Carlo lebih efisien dari metode grid dengan jumlah titik yang sama.

---

## 3. MCMC (Markov Chain Monte Carlo)

### 3.1 Prinsip

Untuk sampel dari distribusi target $\pi(x) $yang **tidak dikenal secara normalisasi** (karena $\int \pi(x)dx $sulit dihitung), MCMC membangun rantai Markov yang **invariant distribution-nya** adalah $\pi $.

### 3.2 Algoritma Metropolis-Hastings

**Langkah:**
1. Mulai dari $x_0$.
2. Untuk $i = 1, 2, \dots$:
 a. Generate proposal $x^* \sim q(x^* | x_{i-1})$.
 b. Hitung rasio:

$$\alpha = \min\left(1, \frac{\pi(x^*) \, q(x_{i-1} | x^*)}{\pi(x_{i-1}) \, q(x^* | x_{i-1})}\right)

$$ c. Accept$ x_i = x^*$dengan probabilitas $\alpha $; jika tidak,$x_i = x_{i-1}$.

**Properti:** $\{x_i\} $converges ke $\pi(x) $dalam distribusi, terlepas dari $x_0 $ (dengan syarat aperiodicity dan irreducibility).

### 3.3 Gibbs Sampling

Special case Metropolis-Hastings di mana **acceptance ratio selalu 1**:

- Sample $x_1 $dari $p(x_1 | x_2, x_3, \dots, x_d)$- Sample $x_2 $dari $p(x_2 | x_1, x_3, \dots, x_d)$- ... lanjutkan secara cyclic.

Cocok untuk model dimensi tinggi dengan conditional distribution yang diketahui.

### 3.4 HMC (Hamiltonian Monte Carlo)

Menggunakan dinamika Hamilton untuk proposal yang efisien dalam dimensi tinggi:

- Gunakan momentum $p $auxiliary variables.

- Update menggunakan Hamilton's equations

$$\dot{x} = \frac{\partial H}{\partial p}, \quad \dot{p} = -\frac{\partial H}{\partial x} $$

-$H(x, p) = -\log \pi(x) + \frac{1}{2}p^T p$(kinetic + potential energy)

Digunakan secara luas di **Stan**, probabilistic programming.

### 3.5 Convergence Diagnostics

| Diagnostik | Prinsip | Threshold |
|------------|---------|-----------|
| **R-hat (Gelman-Rubin)** | Bandingkan varians antar-dalam chain | $\hat{R} < 1.05 $ |
| **Effective Sample Size (ESS)** | Korelasi antar sampel | ESS > 400 |
| **Trace plot** | Visual inspection | Stationarity, mixing |
| **Geweke** | Bandingkan mean awal vs akhir | z-score < 1.96 |
| **Auto-correlation** | Cek $r(lag k) \to 0 $cepat | $r(k) < 0.05 $untuk $k > 10$ |

---

## 4. Aplikasi dalam Geodesi

### 4.1 Propagasi Uncertainty dalam Koordinat

Model geodetik umum: $\mathbf{y} = f(\mathbf{x}) + \boldsymbol{\varepsilon} $, di mana $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}_x, \Sigma_x) $.

**Monte Carlo Propagation:**
1. Draw $N $sampel $\mathbf{x}^{(i)} \sim \mathcal{N}(\boldsymbol{\mu}_x, \Sigma_x) $.
2. Hitung $\mathbf{y}^{(i)} = f(\mathbf{x}^{(i)}) $ untuk setiap sampel.
3. Estimasi: $\hat{\boldsymbol{\mu}}_y = \frac{1}{N}\sum \mathbf{y}^{(i)} $, $\hat{\Sigma}_y = \text{Cov}(\mathbf{y}) $.

### 4.2 Studi Kasus: Error Ellipse untuk Koordinat 2D

Sebuah stasiun GNSS memiliki koordinat estimasi $(\hat{X}, \hat{Y})$dengan kovarian

$$\Sigma = \begin{bmatrix} \sigma_X^2 & \sigma_{XY} \\ \sigma_{XY} & \sigma_Y^2 \end{bmatrix} $$ Monte Carlo digunakan ketika:

- Error non-normal (misalnya multipath, atmosfer)

- Transformasi non-linear (geodetic → cartesian)

- Korelasi antar-parameter kompleks

import numpy as np

N = 100_000
sigma_x, sigma_y, rho = 0.005, 0.003, 0.7 # meter
Sigma = np.array([[sigma_x**2, rho*sigma_x*sigma_y],
 [rho*sigma_x*sigma_y, sigma_y**2]])

coords = np.random.multivariate_normal([0, 0], Sigma, N)

# Error ellipse parameters
eigenvalues, eigenvectors = np.linalg.eigh(Sigma)
semi_major = 2 * np.sqrt(eigenvalues[1]) # 95%
semi_minor = 2 * np.sqrt(eigenvalues[0])
angle = np.degrees(np.arctan2(eigenvectors[1,1], eigenvectors[0,1]))

print(f"95% Error Ellipse: a={semi_major*1000:.2f}mm, "
 f"b={semi_minor*1000:.2f}mm, θ={angle:.1f}°")

# Output: a=12.65mm, b=6.54mm, θ=36.7°