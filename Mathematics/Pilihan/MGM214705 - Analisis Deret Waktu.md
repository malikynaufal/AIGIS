---
title: "MGM214705 - Analisis Deret Waktu"
subject: "Matematika Terapan / Statistika"
tags: [time-series, ARIMA, forecasting, autocorrelation, spectral-analysis, stationarity]
course_code: "MGM214705"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214705 - Analisis Deret Waktu

## Time Series Analysis

**Course Code:** MGM214705
**SKS:** 3 (3-0)
**Semester:** 5
**Prerequisites:** Probabilitas & Statistika, Aljabar Linear

---

## Overview / Gambaran Umum

Analisis deret waktu (time series analysis) mempelajari data yang diurutkan secara kronologis untuk menemukan pola, tren, siklus, dan melakukan peramalan (forecasting). Dalam geodesi, data deret waktu muncul dari posisi stasiun GNSS harian, pengukuran pasang surut, pengukuran gravitasi, dan deformasi kerak bumi. Mata kuliah ini mencakup stasionaritas, fungsi autokorelasi (ACF/PACF), model ARIMA, analisis spektral, dan metode peramalan modern.

> **Catatan:** "Deret waktu adalah sinyal dari dinamika bumi yang tersimpan dalam angka — tugas kita adalah membaca kode alam dari data." — *Prinsip interpretasi data geodetik*

---

## 1. Konsep Dasar

### 1.1 Komponen Deret Waktu

Model dekomposisi klasik:

$$ Y_t = T_t + S_t + R_t \quad \text{(additif)}Y_t = T_t \cdot S_t \cdot R_t \quad \text{(multitipikatif)}$$ | Komponen | Simbol | Penjelasan |
|----------|--------|-----------|
| **Tren** | $T_t$ | Perubahan jangka panjang (misal: tektonik) |
| **Musiman** | $S_t$ | Pola berulang dengan periode tetap (misal: harian, tahunan) |
| **Residual** | $R_t$ | Noise random, gempa bumi, error pengukuran |

### 1.2 Stasionaritas

**Stasionaritas lemah (weak stationarity):**
1. Mean konstan: $E[Y_t] = \mu $untuk semua $t$.
2. Variansi konstan: $\text{Var}(Y_t) = \sigma^2 $untuk semua $t $.
3. Autokorelasi hanya bergantung lag: $\text{Cov}(Y_t, Y_{t+k}) = \gamma(k) $.

**Uji Stasionaritas:**

| Uji | Hipotesis $H_0$ | Statistik | Threshold |
|-----|-----------------|-----------|-----------|
| **Augmented Dickey-Fuller (ADF)** | Unit root ada (non-stasioner) | $\tau = \frac{\hat{\rho}-1}{SE(\hat{\rho})} $ | Critical values (MacKinnon) |
| **Phillips-Perron (PP)** | Unit root ada | Non-parametrik koreksi ADF | — |
| **KPSS** | Stasioner (terbalik!) | $\eta = \frac{1}{T^2}\sum_t S_t^2 / \hat{\sigma}^2 $ | Critical values |

**Pendekatan:** ADF reject $H_0$→ stasioner. KPSS fail to reject $H_0$→ stasioner.

### 1.3 Differencing untuk Stasionaritas

Untuk tren linear: first difference $\nabla Y_t = Y_t - Y_{t-1} $.

Untuk tren polinomial orde $d$:

$$\nabla^d Y_t = \sum_{j=0}^{d} (-1)^j \binom{d}{j} Y_{t-j} $$ Seasonal differencing:$\nabla_s Y_t = Y_t - Y_{t-s} $(misal:$s=7 $ untuk data harian mingguan).

---

## 2. Fungsi Autokorelasi

### 2.1 Autokorrelasi (ACF
)

$$\hat{\rho}(k) = \frac{\hat{\gamma}(k)}{\hat{\gamma}(0)} = \frac{\frac{1}{T}\sum_{t=1}^{T-k}(Y_t - \bar{Y})(Y_{t+k} - \bar{Y})}{\frac{1}{T}\sum_{t=1}^{T}(Y_t - \bar{Y})^2} $$

- **Bartlett interval:**$\hat{\rho}(k) \pm \frac{1.96}{\sqrt{T}} $ (95% confidence)

- Untuk $|k| > p $ (AR(p)),$\hat{\rho}(k) $ cutoff eksponensial.

### 2.2 Autokorelasi Parsial (PACF
)

$$\hat{\phi}_{kk} = \text{partial correlation}(Y_t, Y_{t-k} | Y_{t-1}, \dots, Y_{t-k+1})

$$ Dihitung dengan regresi $$ Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \cdots + \phi_k Y_{t-k} + \varepsilon_t $$

### 2.3 Identifikasi Model dari ACF/PACF

| Model | ACF Pattern | PACF Pattern |
|-------|-------------|--------------|
| **AR(p)** | Exponential decay / damped sine | Cutoff pada lag $p$ |
| **MA(q)** | Cutoff pada lag $q$ | Exponential decay / damped sine |
| **ARMA(p,q)** | Exponential decay (tanpa cutoff tegas) | Exponential decay (tanpa cutoff tegas) |
| **ARIMA(p,d,q)** | Apply pada data $\nabla^d Y_t $| Apply pada data $\nabla^d Y_t $ |

---

## 3. Model ARIMA

### 3.1 Definisi ARIMA(p, d, q)

**ARIMA(p, d, q):*
*

$$\phi(B)(1-B)^d Y_t = \theta(B)\varepsilon_t

$$ di mana:
-$p$ = orde AutoRegressive
-$d$ = orde differencing (integrated)
-$q$ = orde Moving Average
-$B$ = backshift operator: $B Y_t = Y_{t-1}$-$\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \cdots - \phi_p B^p $-$\theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \cdots + \theta_q B^q $-$\varepsilon_t \sim \text{WN}(0, \sigma^2) $ (white noise)

### 3.2 Model Spesifik

**AR(1):**$Y_t = \phi_1 Y_{t-1} + \varepsilon_t$- Stabil jika $|\phi_1| < 1 $.

- $\text{ACF}(k) = \phi_1^{|k|} $**MA(1):**$Y_t = \varepsilon_t + \theta_1 \varepsilon_{t-1}$- Selalu stabil.
-$\text{ACF}(1) = \frac{\theta_1}{1+\theta_1^2} $, $\text{ACF}(k) = 0 $untuk$ |k| > 1$.

**ARIMA(1,1,1):** $(1-\phi_1 B)(1-B)Y_t = (1+\theta_1 B)\varepsilon_t$

$$ Y_t - Y_{t-1} = \phi_1(Y_{t-1} - Y_{t-2}) + \varepsilon_t + \theta_1 \varepsilon_{t-1}$$

### 3.3 SARIMA: Model Seasonal

ARIMA musiman $\text{SARIMA}(p,d,q)(P,D,Q)_s $:

$$\Phi(B^s)\phi(B)(1-B)^d(1-B^s)^D Y_t = \Theta(B^s)\theta(B)\varepsilon_t

$$**Contoh SARIMA(1,1,1)(1,1,1) $_{12} $** untuk data bulanan tahunan:

- Non-seasonal: $(1-\phi_1 B)(1-B)Y_t$- Seasonal: $(1-\Phi_1 B^{12})(1-B^{12})Y_t$### 3.4 Prosedur Box-Jenkins

| Langkah | Aktivitas | Alat |
|---------|-----------|------|
| 1. **Identifikasi** | Cek stasionaritas, pilih p,d,q | ADF, ACF, PACF |
| 2. **Estimasi** | Estimasi parameter $\phi, \theta $ | MLE atau CSS |
| 3. **Diagnostik** | Cek residual white noise | Ljung-Box, ACF residual |
| 4. **Peramalan** | Forecast + prediction intervals | $\hat{Y}_{T+k|T} \pm 1.96 \cdot \hat{\sigma}_k $ |

### 3.5 Kriteria Seleksi Model

| Kriteria | Rumus | Interpretasi |
|----------|-------|-------------|
| **AIC** | $-2\ln L + 2k $ | Keseimbangan goodness-of-fit & parsimony |
| **AICc** | $\text{AIC} + \frac{2k(k+1)}{N-k-1} $| Koreksi untuk $N$ kecil |
| **BIC** | $-2\ln L + k \ln N $ | Lebih konservatif dari AIC |
| **RMSE** | $\sqrt{\frac{1}{N}\sum(Y_t-\hat{Y}_t)^2} $ | Error prediksi (in-sample) |
| **MAPE** | $\frac{100}{N}\sum\left|\frac{Y_t-\hat{Y}_t}{Y_t}\right| $ | Error relatif (persen) |

---

## 4. Analisis Spektral

### 4.1 Spektral Density Function

Untuk stasioner, representasi frekuensi via **Wiener-Khintchine theorem:**

$$

S(f) = \sum_{k=-\infty}^{\infty} \gamma(k) e^{-i2\pi fk}\gamma(k) = \int_{-1/2}^{1/2} S(f) e^{i2\pi fk} \, d
f

$$### 4.2 Periodogram $$ I(f_j) = \frac{1}{T}\left|\sum_{t=1}^{T} Y_t e^{-i2\pi f_j t}\right|^2, \quad f_j = \frac{j}{T}$$ Properti:$\mathbb{E}[I(f_j)] \approx S(f_j) $(asymptotically unbiased) tetapi $\text{Var}[I(f_j)] \approx S(f_j)^2 $ (**tidak konsisten!**).

### 4.3 Estimator Spektrum Tapere
d

$$ I_{taper}(f) = \frac{1}{h} \left| \sum_{t=1}^{T} w_t Y_t e^{-i2\pi ft} \right|^2 $$

| Window/Taper | Rumus | Leakage | Resolution |
|-------------|-------|---------|------------|
| Rectangular | $w_t = 1$ | Tinggi (picket fence effect) | Terbaik |
| Hann | $w_t = \frac{1}{2}(1-\cos(2\pi t/T))$ | Rendah | Baik |
| Welch | Segmentasi + rata-rata | Sangat rendah | Berkurang |

### 4.4 Studi Kasus: Analisis Pasang Surut (Tides)

Data ketinggian air harian selama 3 tahun (1095 hari) dianalisis:

**Periodogram menunjukkan puncak pada frekuensi:**
-$f = 0.03866 $cpd → periode 25.85 jam → **O1** (diurnal lunar)
-$f = 0.04007 $cpd → periode 24.96 jam → **K1** (luni-solar)
-$f = 0.07996 $cpd → periode 12.51 jam → **M2** (semi-diurnal lunar)
-$f = 0.08333$ cpd → periode 12.00 jam → **S2** (semi-diurnal solar)

> **Hasil:** Model SARIMA(2,1,1)(1,1,1)$_7 $ memberikan RMSE = 4.2 cm, cocok untuk peramalan water level real-time.

---

## 5. Peramalan (Forecasting) Modern

### 5.1 Exponential Smoothing (ETS)

| Model | Level | Tren | Musiman | Model Persamaan |
|-------|-------|------|---------|----------------|
| **SES** (Simple) | $l_t$ | — | — | $l_t = \alpha Y_t + (1-\alpha)l_{t-1}$ |
| **Holt** (Double) | $l_t$ | $b_t$ | — | $b_t = \beta^*(l_t - l_{t-1}) + (1-\beta^*)b_{t-1}$ |
| **Holt-Winters** | $l_t$ | $b_t$ | $s_t$ | $s_t = \gamma(Y_t - l_{t-1} - b_{t-1}) + (1-\gamma)s_{t-m}$ |

Peramalan $k $langkah ke depan (Holt-Winters additive)

$$\hat{Y}_{T+k|T} = l_T + k \cdot b_T + s_{T+k-m} $$

### 5.2 Perbandingan Model Peramalan

| Model | Kelebihan | Kekurangan | Cocok Untuk |
|-------|----------|------------|-------------|
| **ARIMA** | Flexible, teori kuat | Pemilihan manual p,d,q | Data tanpa komponen musiman kuat |
| **ETS** | Interpretable, automatic | Terbatas untuk non-linear | Data dengan trend & seasonality |
| **SARIMA** | Seasonal handling kuat | Kompleks untuk seasonal ganda | Data bulanan/tahunan |
| **Prophet** (Facebook) | Robust, mudah | Black box | Bisnis forecasting |
| **BSTS** | Bayesian uncertainty | Komputasi lambat | Small data, uncertainty quantification |

### 5.3 Forecast Intervals

Peramalan $k$-step ahead untuk ARIMA:

$$\hat{Y}_{T+k|T} = \mu + \sum_{j=1}^{k} \psi_j \hat{\varepsilon}_{T+k-j
}

$$ Interval kepercayaan 95%: $$\hat{Y}_{T+k|T} \pm 1.96 \cdot \sigma \sqrt{\sum_{j=0}^{k-1} \psi_j^2}

$$ ---

## 6. Worked Example

### Soal: Modelkan data penjualan harian (7 hari) dan peramalkan hari ke-8.

**Data:** 23, 27, 30, 28, 32, 35, 31

**Langkah 1:** Cek tren — ada kenaikan jelas. Terapkan differencing

$$\nabla Y_t: \quad 4, 3, -2, 4, 3, -4

$$

**Langkah 2:** ACF/PACF differenced data menunjukkan MA(1) cocok (ACF cut off lag 1).

**Langkah 3:** Fit ARIMA(0,1,1)

$$\nabla Y_t = \varepsilon_t + \theta_1 \varepsilon_{t-1} $$ Estimasi:$\hat{\theta}_1 = -0.65 $ (via MLE).

**Langkah 4:** Peramalan:
-$\nabla \hat{Y}_8 = \hat{\theta}_1 \hat{\varepsilon}_7 = (-0.65)(31 - 34.5) = 2.275 $-$\hat{Y}_8 = 31 + 2.275 \approx 33.3$

---

## References / Referensi

1. **Box, G. E. P., Jenkins, G. M., & Reinsel, G. C.** (2015). *Time Series Analysis: Forecasting and Control* (5th ed.). Wiley.
2. **Hyndman, R. J., & Athanasopoulos, G.** (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts — [otexts.com/fpp3](https://otexts.com/fpp3)
3. **Brockwell, P. J., & Davis, R. A.** (2002). *Introduction to Time Series and Forecasting* (2nd ed.). Springer.
4. **Shumway, R. H., & Stoffer, D. S.** (2017). *Time Series Analysis and Its Applications* (4th ed.). Springer.
5. **Chatfield, C.** (2003). *The Analysis of Time Series: An Introduction* (6th ed.). CRC Press.
6. **Agnew, D. C.** (1992). The time-frequency analysis of geodetic data. *Journal of Geophysical Research*.
7. **Hofmann-Wellenhof, B., et al.** (2008). *GNSS – Global Navigation Satellite Systems*. Springer — Ch. 7 (Time series in positioning).

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214705. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*