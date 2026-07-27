---
title: "MGM214713 - Statistika Bayesian"
subject: "Matematika Terapan / Statistika"
tags: [bayesian, posterior, prior, mcmc, hierarchical-models]
course_code: "MGM214713"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214713 - Statistika Bayesian
## Bayesian Statistics

**Course Code:** MGM214713  
**SKS:** 3 (3-0)  
**Semester:** 6  
**Prerequisites:** Probabilitas & Statistika, Kalkulus Lanjutan  

---

## Overview / Gambaran Umum

Statistika Bayesian adalah kerangka kerja inferensi statistik yang menggunakan Teorema Bayes untuk memperbarui probabilitas ketika bukti baru tersedia. Berbeda dari statistika klasik (Frequentist) yang memperlakukan parameter sebagai nilai tetap, Bayes memperlakukan parameter sebagai variabel acak dengan distribusi. Pendekatan ini sangat cocok untuk masalah geodesi yang melibatkan ketidakpastian (uncertainty), data berukuran kecil, dan penggabungan informasi dari berbagai sumber (data GNSS, leveling, gravimetri).

> **Catatan:** "Bayesian statistics memungkinkan kita mengatakan 'Saya yakin dengan tingkat keyakinan 95% bahwa parameter ini berada di interval ini' — sesuatu yang statistika klasik tidak bisa klaim secara teknis." — *Esensi distribusi posterior*

---

## 1. Teorema Bayes

### 1.1 Formulasi Dasar

$$P(\theta | D) = \frac{P(D | \theta) \cdot P(\theta)}{P(D)}$$

di mana:
- $P(\theta)$ = **prior** (keyakinan awal tentang parameter sebelum data).
- $P(D|\theta)$ = **likelihood** (kemungkinan data diberikan parameter).
- $P(D) = \int P(D|\theta) P(\theta) d\theta$ = **marginal likelihood** (normalisasi).
- $P(\theta|D)$ = **posterior** (keyakinan diperbarui setelah melihat data).

### 1.2 Contoh: Estimasi Koordinat

Mengestimasi posisi stasiun GNSS dari $n$ pengukuran yang diasumsikan normal:

- Prior: $\theta \sim \mathcal{N}(\mu_0, \sigma_0^2)$
- Likelihood: $D_i | \theta \sim \mathcal{N}(\theta, \sigma^2)$
- Posterior: $\theta | D \sim \mathcal{N}(\mu_n, \sigma_n^2)$ dengan:

$$\mu_n = \frac{\sigma^2 \mu_0 + n\sigma_0^2 \bar{D}}{\sigma^2 + n\sigma_0^2}, \quad \sigma_n^2 = \frac{\sigma^2 \sigma_0^2}{\sigma^2 + n\sigma_0^2}$$

Prior $\mu_0$ (data lama) dan data baru $\bar{D}$ digabungkan secara natural.

## 2. Pemilihan Prior

- **Non-informatif (Jeffreys prior):** $P(\theta) \propto \sqrt{I(\theta)}$ di mana $I(\theta)$ adalah informasi Fisher.
- **Informatif:** Berdasarkan studi sebelumnya (misal: posisi awal dari tabel).
- **Conjugate prior:** Prior yang jenisnya sama dengan posterior (mudah dihitung).

## 3. MCMC (Markov Chain Monte Carlo)

Untuk posterior kompleks yang tidak tertutup secara analitik:
- **Gibbs Sampling:** Iteratif mengambil sampel dari distribusi kondisional penuh.
- **Metropolis-Hastings:** Proposal + Accept/Reject.

## 4. Hierarchical Models

Model tingkat lanjut yang menangani pengelompokan data (misal: beberapa stasiun dalam satu blok tektonik).

## 5. Referensi

1. **Gelman, A., et al.** (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.
2. **Kruschke, J. K.** (2014). *Doing Bayesian Data Analysis* (2nd ed.). Academic Press.
3. **Robert, C. P.** (2007). *The Bayesian Choice* (2nd ed.). Springer.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214713. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*