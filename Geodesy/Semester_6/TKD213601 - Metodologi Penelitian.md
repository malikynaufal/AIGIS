# Metodologi Penelitian

**Kode:** TKD213601 
**Sifat:** Wajib 
**SKS:** 

## Deskripsi

Metodologi Penelitian (TKD213601) adalah mata kuliah fundamental yang membekali mahasiswa S1 Geodesi dengan kerangka kerja ilmiah untuk merancang, melaksanakan, dan mengkomunikasikan penelitian di bidang geodesi dan geomatika. Mata kuliah ini mencakup pembentukan hipotesis, tinjauan literatur sistematis, teknik pengumpulan data lapangan dan laboratorium, analisis statistik, serta penulisan ilmiah sesuai standar akademik Indonesia.

## Tujuan Pembelajaran

Setelah menyelesaikan mata kuliah ini, mahasiswa akan mampu:

1. Merumuskan pertanyaan penelitian dan hipotesis yang teruji secara ilmiah
2. Melakukan tinjauan literatur sistematis menggunakan database ilmiah
3. Merancang metode pengumpulan data yang valid dan reliabel
4. Menerapkan teknik analisis statistik untuk data geospatial
5. Menulis proposal penelitian dan laporan ilmiah dengan struktur yang benar
6. Mengidentifikasi publikasi ilmiah yang sesuai untuk diseminasi hasil

## Modul Pembelajaran

### Modul 1: Filosofi dan Paradigma Penelitian
Landasan epistemologis penelitian ilmiah:

- Penelitian kuantitatif vs. kualitatif vs. metode campuran di geospatial

- Paradigma positivisme dan interpretivisme dalam konteks survei

- Penalaran deduktif dan induktif dalam ilmu geodesi

- Konsep ontologi lapangan dan batas spasial

- Etika penelitian: informed consent, anonimitas data, dan reprodusibilitas

### Modul 2: Perumusan Masalah dan Hipotesis
Teknik merumuskan masalah penelitian yang terstruktur:

- Identifikasi celah pengetahuan (knowledge gap) dari literatur

- Pembuatan pertanyaan penelitian yang F.O.C.U.S (Focused, Original, Clear, Understandable, Significant)

- Hipotesis nol ($H_0$) dan hipotesis alternatif ($H_1$)

- Konsep signifikansi statistik: tingkat $\alpha = 0.05$ dan nilai-$p$- Kerangka konseptual dan diagram alir penelitian

- Batasan ruang dan waktu penelitian geospatial

### Modul 3: Tinjauan Literatur Sistematis
Metode penelusuran dan sintesis literatur ilmiah:

- Penggunaan database: Google Scholar, Scopus, Web of Science, Garuda

- Strategi pencarian kata kunci dan Boolean operators

- Manajemen referensi dengan Mendeley, Zotero, atau EndNote

- Sintesis naratif dan meta-analisis untuk topik geospatial

- Penilaian kualitas sumber (peer review, impact factor)

- Penulisan tinjauan pustaka yang kritis dan terstruktur

### Modul 4: Teknik Pengumpulan Data
Metode akuisisi data untuk penelitian geodesi:

- Survei terestris: total station, leveling, GPS/GNSS statik dan RTK

- Penginderaan jauh: citra satelit (optik, radar, LiDAR) dan foto udara

- Data sekunder: peta RBI, DEM nasional, data batas administrasi

- Teknik sampling untuk validasi lapangan

- Desain jaringan kontrol geodetik

- Dokumentasi metadata dan lineage data

### Modul 5: Analisis Statistik untuk Data Geospatial
Teknik kuantitatif dan kualitatif untuk analisis data:

- Statistik deskriptif: mean, median, standar deviasi, skewness

- Uji normalitas: Shapiro-Wilk, Kolmogorov-Smirnov

- Uji hipotesis:$t$-test, ANOVA, Friedman test

- Regresi linear dan regresi spasial: $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \varepsilon$- Analisis autokorelasi spasial: Indeks Moran's $I$, Geary's $C$- Geostatistik: kriging, semivariogram, dan interpolasi spasial

- Validasi model: RMSE, MAE,$R^2$

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}I = \frac{n}{S_0}\frac{\sum_i\sum_j w_{ij}(x_i - \bar{x})(x_j - \bar{x})}{\sum_i (x_i - \bar{x})^2} $$

### Modul 6: Penulisan Ilmiah
Komposisi karya tulis ilmiah yang terstandar:

- Struktur IMRaD (Introduction, Methods, Results, and Discussion)

- Penulisan abstrak yang informatif (150-250 kata)

- Pembuatan tabel dan grafik yang efektif

- Sitasi dan daftar pustaka (APA 7th ed., IEEE, Vancouver)

- Penulisan untuk jurnal terakreditasi SINTA

- Teknik menghindari plagiarisme (Similarity Index <20%)

## Tugas Proyek

### Proposal Penelitian (Individu, 30%)
Setiap mahasiswa menulis proposal penelitian lengkap (3000-4000 kata):

- **Latar Belakang** (500 kata): konteks, urgensi, dan celah penelitian

- **Rumusan Masalah** (200 kata): pertanyaan penelitian spesifik

- **Tinjauan Pustaka** (1000 kata): sintesis minimal 15 referensi

- **Metodologi** (800 kata): desain penelitian, instrumen, analisis

- **Jadwal dan Anggaran** (500 kata): timeline 6 bulan, biaya

- **Daftar Pustaka**: minimal 20 referensi (60% jurnal terindeks)

### Analisis Data Kelompok (20%)
Analisis dataset geospatial yang disediakan menggunakan Python/R:

- Eksplorasi data dan visualisasi

- Uji statistik sesuai pertanyaan penelitian

- Interpretasi hasil dan diskusi

## Penilaian

| Komponen | Bobot | Keterangan |
|---|---|---|
| Tugas Individu | 20% | Review jurnal, ringkasan literatur |
| Proposal Penelitian | 30% | Proposal lengkap sesuai template |
| Proyek Analisis Kelompok | 20% | Laporan analisis data geospatial |
| Ujian Tengah Semester | 15% | Teori metodologi dan statistik |
| Ujian Akhir Semester | 15% | Desain penelitian dan aplikasi |

## Referensi

1. Creswell, J.W. & Creswell, J.D., "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches", 5th Ed., SAGE, 2018
2. Nasution, S., "Metode Penelitian Naturalistik Kualitatif", Penerbit Universitas Indonesia, 2019
3. Haining, R., "Spatial Data Analysis: Theory and Practice", Cambridge University Press, 2003
4. Wulder, M.A. & Franklin, S.E., "Remote Sensing and Image Interpretation", 7th Ed., Wiley, 2016
5. Badan Standarisasi Nasional, "SNI ISO 19157:2017 - Geographic Information - Data Quality"
6. Moradi, A. et al., "Statistical Methods for Geographers", Springer, 2021
7. Sugiyono, "Metode Penelitian Kuantitatif, Kualitatif, dan R&D", Alfabeta, 2019
8. Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2020-2024 - Big Data dan Data Spasial