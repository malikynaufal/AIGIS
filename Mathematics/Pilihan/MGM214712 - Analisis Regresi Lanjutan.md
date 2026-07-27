---
title: "MGM214712 - Analisis Regresi Lanjutan"
subject: "Matematika Terapan / Statistika"
tags: [regression, multivariate, ridge, lasso, modeling]
course_code: "MGM214712"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214712 - Analisis Regresi Lanjutan

## Advanced Regression Analysis

**Course Code:** MGM214712  
**SKS:** 3 (3-0)  
**Semester:** 6  
**Prerequisites:** Statistika Dasar, Aljabar Linear  

---

## Overview / Gambaran Umum

Analisis Regresi Lanjutan melampaui OLS (Ordinary Least Squares) dasar. Mata kuliah ini membahas model untuk data multivariat, data kategorik (Logistik), serta teknik regularisasi untuk data dimensi tinggi (Ridge/LASSO). Fokus utama adalah pemilihan model, diagnostik residual, dan akurasi prediksi untuk model geodetik yang kompleks.

## 1. Regresi Linear Berganda (MLR)
$$

Y = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k + \varepsilon$$- **Asumsi:** Linearitas, Homoskedastisitas, Independensi, Normalitas.

- **Masalah:** Multikolinearitas (cek VIF).

## 2. Regresi Kategorik dan Logistik

- **Logistik:** Untuk variabel dependen biner (misal: sukses/gagal deteksi sinyal).

- **Poisson:** Untuk data perhitungan (count data).

## 3. Regularisasi (Shrinkage)

Untuk mencegah overfitting dan menangani multikolinearitas:

- **Ridge:** Penalty$L_2$ ($\sum \beta^2$).

- **LASSO:** Penalty $L_1$ ($\sum |\beta|$); dapat melakukan pemilihan fitur (beberapa $\beta \to 0$).

## 4. Referensi

1. **Montgomery, D. C., et al.** (2012). *Introduction to Linear Regression Analysis*. Wiley.
2. **Kutner, M. H., et al.** (2005). *Applied Linear Statistical Models*. McGraw-Hill.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214712. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*