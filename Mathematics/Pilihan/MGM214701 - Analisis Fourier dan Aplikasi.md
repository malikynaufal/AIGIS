---
title: "MGM214701 - Analisis Fourier dan Aplikasi"
subject: "Matematika Terapan / Geodesi"
tags: [fourier, signal-processing, geodesy, spectral-analysis, fft]
course_code: "MGM214701"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214701 - Analisis Fourier dan Aplikasi

## Fourier Analysis and Applications

**Course Code:** MGM214701
**SKS:** 3 (3-0)
**Semester:** 5
**Prerequisites:** Kalkulus Lanjutan, Persamaan Diferensial

---

## Overview / Gambaran Umum

Analisis Fourier (Fourier Analysis) adalah cabang matematika yang mempelajari representasi fungsi atau sinyal sebagai superposisi (penjumlahan) dari fungsi-fungsi sinusoidal sederhana. Konsep ini fundamental dalam pemrosesan sinyal (signal processing), geodesi, fisika, dan rekayasa. Mata kuliah ini mencakup deret Fourier untuk fungsi periodik, transformasi Fourier untuk sinyal non-periodik, Fast Fourier Transform (FFT) untuk komputasi efisien, serta aplikasi dalam analisis data geodesi seperti dekomposisi gelombang maritim, koreksi atmosfer ionosfer, dan pemfilteran noise pada data GNSS.

> **Catatan:** "Analisis Fourier memungkinkan kita memecah sinyal kompleks menjadi komponen frekuensi constitutifnya — seperti memisahkan nada-nada musik dalam sebuah orkestra." — *Prinsip Superposisi Fourier*

---

## 1. Deret Fourier (Fourier Series)

### 1.1 Definisi dan Konvergensi

Untuk fungsi periodik $f(x) $ dengan periode $ 2\pi $ (atau $ 2L$), deret Fourier didefinisikan sebagai:

$ $

f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right) \right
]

$$

di mana koefisien Fourier dihitung dengan: $ $ a_0 = \frac{1}{L} \int_{-L}^{L} f(x) \, dxa_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) \, dxb_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) \, dx $ $ **Teorema Konvergensi Dirichlet:** Jika $ f(x) $ piecewise-continuous dan memiliki turunan piecewise-continuous pada $ [-L, L] $, maka deret Fourier konvergen ke $ f(x)$ di titik kontinuitas, dan ke rata-rata limit kiri-kanan di titik diskontinuitas.

### 1.2 Bentuk Eksponensial Kompleks

Menggunakan rumus Euler $e^{i\theta} = \cos\theta + i\sin\theta $, deret Fourier dapat ditulis lebih ringkas:

$ $

f(x) \sim \sum_{n=-\infty}^{\infty} c_n e^{i n \pi x / L
}

$$

dengan: $ $ c_n = \frac{1}{2L} \int_{-L}^{L} f(x) e^{-i n \pi x / L} \, dx $$

# ## 1.3 Parseval's Identity (Identitas Parseval)

Energi total sinyal dalam domain waktu sama dengan energi dalam domain frekuensi

$ $\frac{1}{2L} \int_{-L}^{L} |f(x)|^2 \, dx = \frac{|a_0|^2}{4} + \frac{1}{2} \sum_{n=1}^{\infty} (|a_n|^2 + |b_n|^2) = \sum_{n=-\infty}^{\infty} |c_n|^2

$$

---

## 2. Transformasi Fourier (Fourier Transform)

### 2.1 Definisi untuk Sinyal Non-Periodik

Untuk sinyal $f(t) \in L^1(\mathbb{R}) $, transformasi Fourier dan inversnya:

$ $\mathcal{F}\{f(t)\} = F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \, dt\mathcal{F}^{-1}\{F(\omega)\} = f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} \, d\omega

$$

# ## 2.2 Sifat-Sifat Penting

| Sifat | Domain Waktu | Domain Frekuensi |
|-------|--------------|------------------|
| **Linearitas** | $a f(t) + b g(t) $ | $  a F(\omega) + b G(\omega) $ |
| **Pergeseran Waktu** | $ f(t - t_0) $ | $ e^{-i\omega t_0} F(\omega) $ |
| **Pergeseran Frekuensi** | $ e^{i\omega_0 t} f(t) $ | $ F(\omega - \omega_0) $ |
| **Skalasi** | $ f(at) $ | $\frac{1}{|a|} F(\frac{\omega}{a}) $ |
| **Diferensiasi** | $ f'(t) $ | $ i\omega F(\omega) $ |
| **Integrasi** | $\int_{-\infty}^t f(\tau) d\tau $|$\frac{F(\omega)}{i\omega} + \pi F(0)\delta(\omega) $ |
| **Konvolusi** | $ (f * g)(t) $ | $ F(\omega) G(\omega) $ |
| **Perkalian** | $ f(t) g(t) $ | $\frac{1}{2\pi} (F * G)(\omega) $ |

### 2.3 Transformasi Fourier Diskrit (DFT)

Untuk sinyal diskrit $ x[n] $ panjang $  N $:

$ $

X[k] = \sum_{n=0}^{N-1} x[n] e^{-i 2\pi k n / N}, \quad k = 0, 1, \dots, N-
1

$$

Invers DFT: $ $ x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{i 2\pi k n / N}$$ ---

## 3. Fast Fourier Transform (FFT)

### 3.1 Algoritma Cooley-Tukey

FFT mengurangi kompleksitas DFT dari $O(N^2) $ menjadi $ O(N \log N) $ dengan memanfaatkan simetri dan periodisitas twiddle factors $ W_N = e^{-i 2\pi / N} $.

**Struktur Radix-2 DIT (Decimation-in-Time):**

- Bagi $ N $ menjadi dua subsequences genap/ganjil

- Rekursif hingga $ N=2 $ (butterfly operation)

- Gabungkan hasil dengan twiddle factors

### 3.2 Operasi Butterfly

Untuk $ N=2 $:

$ $\begin{bmatrix} X[0] \\ X[1] \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x[0] \\ x[1] \end{bmatrix
}

$$

Untuk umum: $ $ X[k] = E[k] + W_N^k O[k]X[k + N/2] = E[k] - W_N^k O[k]$$

di mana $ E[k] $ dan $ O[k] $ adalah DFT subsequences genap dan ganjil.

### 3.3 Zero-Padding dan Spectral Leakage

| Teknik | Tujuan | Trade-off |
|--------|--------|-----------|
| **Zero-padding** | Interpolasi spektrum (visual smoothing) | Tidak menambah resolusi frekuensi aktual |
| **Windowing** (Hann, Hamming, Blackman) | Mengurangi spectral leakage | Memperlebar main lobe, menurunkan resolusi |
| **Overlap-add / Overlap-save** | FFT convolution untuk sinyal panjang | Kompleksitas implementasi |

---

## 4. Aplikasi dalam Geodesi dan Pemrosesan Sinyal

### 4.1 Analisis Spektral Data GNSS

Data koordinat stasiun GNSS mengandung noise multi-sumber: multipath (periodik harian), drift sistematik, gempa bumi, deformasi tektonik. Analisis Fourier memisahkan komponen:

```python

# Contoh Python: Periodogram untuk data GNSS
import numpy as np
from scipy.signal import periodogram

# Data harian North component (mm)
t = np.arange(0, 365*3) # 3 tahun
north = 2*np.sin(2*np.pi*t/365.25) + 0.5*np.sin(2*np.pi*t/1) + np.random.normal(0, 1, len(t))

f, Pxx = periodogram(north, fs=1.0, window='hann', scaling='spectrum')

# Puncak di f ≈ 1/365.25 (tahunan) dan f ≈ 1 (harian/multipath)
```

### 4.2 Koreksi Ionosfer (TEC Mapping)

Total Electron Content (TEC) dari data GNSS dual-fase GNSS global dianalisis dengan Fourier 2D untuk memodelkan variasi spasial-temporal ionosfer

$ $\mathrm{TEC}(\phi, \lambda, t) \approx \sum_{m,n} C_{mn}(t) Y_{mn}(\phi, \lambda)

$$

di mana $ Y_{mn} $ adalah harmonik bola (spherical harmonics) — generalisasi Fourier ke bola.

### 4.3 Desain Filter Digital

Filter Butterworth/Chebyshev dirancang di domain frekuensi lalu diimplementasikan via IFFT

$ $ H(\omega) = \frac{1}{\sqrt{1 + (\omega/\omega_c)^{2n}}} \quad \text{(Butterworth low-pass)}$$

# ## 4.4 Studi Kasus: Dekomposisi Gelombang Laut (Ocean Tide Analysis)

Data ketinggian air (tide gauge) 1 tahun dianalisis untuk ekstraksi konstituen astronomis:

| Konstituen | Periode (jam) | Frekuensi (siklus/hari) | Amplituda (cm) | Fase (derajat) |
|------------|---------------|--------------------------|----------------|----------------|
| **M2** (Bulan utama) | 12.42 | 1.932 | 85.2 | 142.3 |
| **S2** (Matahari utama) | 12.00 | 2.000 | 32.1 | 168.7 |
| **K1** (Diurnal bulan) | 23.93 | 1.003 | 18.5 | 95.2 |
| **O1** (Diurnal lunar) | 25.82 | 0.929 | 12.3 | 78.4 |
| **N2** (Elliptisitas bulan) | 12.66 | 1.896 | 8.7 | 134.1 |

> **Hasil:** Model harmonic dengan 37 konstituen menjelaskan >95% varians data. Residual digunakan untuk deteksi tsunami/storm surge.

---

## 5. Worked Example / Contoh Terstruktur

### Soal: Hitung koefisien Fourier untuk $f(x) = x $ pada $ [-\pi, \pi] $**Langkah 1:** Identifikasi sifat fungsi.$ f(x) = x $ adalah fungsi **ganjil** ( $ f(-x) = -f(x) $), sehingga $ a_n = 0 $ untuk semua $  n $ (termasuk $ a_0 $).

**Langkah 2:** Hitung $ b_n $:

$ $ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x \sin(nx) \, dx $$

Integrasi parsial: $ u = x, dv = \sin(nx)dx \Rightarrow du = dx, v = -\frac{1}{n}\cos(nx) $

$ $

b_n = \frac{1}{\pi} \left[ -\frac{x}{n}\cos(nx) \Big|_{-\pi}^{\pi} + \frac{1}{n}\int_{-\pi}^{\pi} \cos(nx) \, dx \right]= \frac{1}{\pi} \left[ -\frac{\pi}{n}\cos(n\pi) + \frac{\pi}{n}\cos(-n\pi) + 0 \right]= \frac{2}{n} (-1)^{n+1
}

$$**Hasil:** $ $ f(x) = 2 \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin(nx) = 2\left(\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots\right
)

$$ **Verifikasi Parseval:** $ $\frac{1}{2\pi}\int_{-\pi}^{\pi} x^2 dx = \frac{\pi^2}{3} = 2\sum_{n=1}^{\infty} \frac{1}{n^2} = 2 \cdot \frac{\pi^2}{6} \quad \checkmark

$$ ---

## References / Referensi

1. **Bracewell, R. N.** (2000). *The Fourier Transform and Its Applications* (3rd ed.). McGraw-Hill.
2. **Oppenheim, A. V., & Schafer, R. W.** (2010). *Discrete-Time Signal Processing* (3rd ed.). Prentice Hall.
3. **Brigham, E. O.** (1988). *The Fast Fourier Transform and Its Applications*. Prentice Hall.
4. **Press, W. H., et al.** (2007). *Numerical Recipes: The Art of Scientific Computing* (3rd ed.). Cambridge Univ. Press — Ch. 12 (FFT).
5. **Seeber, G.** (2003). *Satellite Geodesy* (2nd ed.). de Gruyter — Ch. 5 (Signal processing in GNSS).
6. **Hofmann-Wellenhof, B., et al.** (2008). *GNSS – Global Navigation Satellite Systems*. Springer — Ch. 6 (Time series analysis).
7. **Agnew, D. C.** (2007). *Earth Tides*. In: *Treatise on Geophysics*, Vol. 3. Elsevier.

---

## Appendix: Quick Reference / Referensi Cepat

| Notasi | Artian |
|--------|--------|
| $\mathcal{F}, \mathcal{F}^{-1} $ | Transformasi Fourier & Invers |
| $ F(\omega), X[k] $ | Spektrum frekuensi (kontinu/diskrit) |
| $ W_N = e^{-i2\pi/N} $ | Twiddle factor FFT |
| $\delta(\omega) $ | Dirac delta function |
| $*$ | Konvolusi |
| $\star $ | Korelasi silang |
| $\mathrm{sinc}(x) = \frac{\sin(\pi x)}{\pi x} $ | Fungsi sink (transformasi persegi) |

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214701. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*