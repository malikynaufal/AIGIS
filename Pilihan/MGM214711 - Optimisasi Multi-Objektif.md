---
title: "MGM214711 - Optimisasi Multi-Objektif"
subject: "Matematika Terapan / Riset Operasi"
tags: [optimization, pareto, nsga-ii, multi-criteria]
course_code: "MGM214711"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214711 - Optimisasi Multi-Objektif
## Multi-Objective Optimization

**Course Code:** MGM214711  
**SKS:** 3 (3-0)  
**Semester:** 6  
**Prerequisites:** Kalkulus Multivariabel, Aljabar Linear  

---

## Overview / Gambaran Umum

Dalam dunia nyata, kita jarang hanya mengoptimasi satu target. Kita sering berhadapan dengan target yang saling bertentangan (trade-off), misal: meminimalkan biaya pembangunan stasiun GNSS namun memaksimalkan akurasi geometrik (DOP). Mata kuliah ini mempelajari optimisasi multi-objektif (MOO) di mana solusi tunggal optimal tidak ada; yang ada adalah **Front Pareto**.

> **Catatan:** "Solusi optimal adalah kompromi yang kita pilih, bukan angka yang kita hitung." — *Esensi MOO*

---

## 1. Konsep Dasar

- **Dominansi Pareto:** Solusi A mendominasi B jika A tidak lebih buruk dari B di semua objektif dan secara tegas lebih baik di minimal satu objektif.
- **Front Pareto:** Himpunan solusi yang tidak didominasi oleh solusi lainnya (non-dominated).

## 2. Teknik Pemecahan

- **Weighted Sum:** Mengubah multi-objektif menjadi satu dengan bobot $\sum w_i f_i$.
- **NSGA-II (Non-dominated Sorting Genetic Algorithm):** Algoritma evolusioner untuk menemukan Front Pareto secara efisien.
- **Constraint Method:** Mengoptimasi satu objektif dengan batasan pada objektif lain.

## 3. Aplikasi Geodesi

- Desain jaringan pengamatan (meminimalkan biaya vs akurasi).
- Rute optimal dengan mempertimbangkan waktu tempuh, konsumsi bahan bakar, dan risiko jalur.

## 4. Referensi

1. **Deb, K.** (2001). *Multi-Objective Optimization using Evolutionary Algorithms*. Wiley.
2. **Miettinen, K.** (1999). *Nonlinear Multiobjective Optimization*. Kluwer.
3. **Marler, R. T., & Arora, J. S.** (2004). Survey of multi-objective optimization methods for engineering. *Structural and Multidisciplinary Optimization*.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214711. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*