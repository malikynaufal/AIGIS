---
title: "MGM214715 - Pengambilan Keputusan"
subject: "Ilmu Komputer / Riset Operasi"
tags: [decision-analysis, decision-trees, ahp, topsis, mcdm]
course_code: "MGM214715"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214715 - Pengambilan Keputusan
## Decision Science

**Course Code:** MGM214715  
**SKS:** 3 (3-0)  
**Semester:** 6  
**Prerequisites:** Statistika Dasar, Aljabar Linear  

---

## Overview / Gambaran Umum

Pengambilan Keputusan (Decision Science) adalah disiplin yang menggabungkan statistik, matematika, dan logika untuk memilih alternatif optimal di tengah ketidakpastian. Dalam konteks geodetik, ini penting untuk perencanaan jaringan pengamatan, pemilihan lokasi stasiun, dan alokasi anggaran. Mata kuliah ini membahas pohon keputusan, AHP (Analytical Hierarchy Process), TOPSIS, dan metode Multi-Criteria Decision Making (MCDM).

> **Catatan:** "Setiap keputusan adalah perhitungan implisit dari nilai, risiko, dan alternatif yang tersedia." — *Esensi Pengambilan Keputusan*

---

## 1. Pohon Keputusan (Decision Tree)

Struktur pohon yang menggambarkan keputusan (decision nodes), kejadian (chance nodes), dan hasil (end nodes).

### 1.1 Expected Monetary Value (EMV)

$$\text{EMV} = \sum_i P_i \cdot V_i$$

di mana $P_i$ = probabilitas hasil ke-$i$, $V_i$ = nilai hasil ke-$i$.

### 1.2 Expected Value of Perfect Information (EVPI)

$$\text{EVPI} = \text{EVPI}_{\text{with PI}} - \text{EVPI}_{\text{without PI}}$$

Nilai maksimum yang harus dikeluarkan untuk informasi sempurna.

## 2. AHP (Analytical Hierarchy Process)

Metode Saaty untuk keputusan multi-kriteria.

### 2.1 Matriks Perbandingan

Bangun matriks berpasangan $A$ di mana $a_{ij}$ = tingkat penting kriteria $i$ relatif terhadap $i$.

| Skor | Makna |
|------|-------|
| 1 | Sama penting |
| 3 | Moderat lebih penting |
| 5 | Sangat penting |
| 7 | Sangat-sangat penting |
| 9 | Mutlak penting |

### 2.2 Eigenvalue dan Konsistensi

- Hitung vek eigen dominan (bobot kriteria).
- Cek konsistensi: $\text{CR} = \frac{CI}{RI} < 0.1$ (di mana $CI = \frac{\lambda_{\max} - n}{n-1}$).

## 3. TOPSIS (Technique for Order Preference)

### 3.1 Langkah-langkah

1. Normalisasi matriks keputusan.
2. Hitung matriks terbobot.
3. Tentukan solusi ideal positif (PIS) dan negatif (NIS).
4. Hitung jarak ke PIS ($S^+$) dan NIS ($S^-$).
5. Hitung skor: $C^* = \frac{S^-}{S^+ + S^-}$ (semakin dekat ke 1, semakin baik).

## 4. Aplikasi Geospasial

### 4.1 Studi Kasus: Pemilihan Lokasi Stasiun GNSS Baru

**Kriteria:**
- Biaya (C1)
- Akses jalan (C2)
- Interferensi sinyal (C3)
- Jarak ke jaringan ada (C4)

**Alternatif:** Lokasi A, B, C, D

| Lokasi | Biaya (juta) | Akses | Interferensi | Jarak (km) |
|--------|-------------|-------|--------------|------------|
| A | 500 | 8 | 2 | 5 |
| B | 800 | 9 | 4 | 10 |
| C | 600 | 7 | 1 | 15 |
| D | 400 | 6 | 3 | 8 |

Dengan AHP, bobot kriteria diperoleh: $w = [0.35, 0.25, 0.20, 0.20]$.

Setelah normalisasi TOPSIS, **Lokasi A** mendapatkan skor tertinggi ($C^* = 0.73$), menjadi rekomendasi.

## 5. Referensi

1. **Saaty, T. L.** (2008). *Decision Making for Leaders: The Analytic Hierarchy Process*. Springer.
2. **Hwang, C. L., & Yoon, K.** (1981). *Methods for Multiple Pattern Decision Making*. Springer.
3. **Keeney, R. L., & Raiffa, H.** (1993). *Decisions with Multiple Objectives*. Cambridge Univ. Press.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214715. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*