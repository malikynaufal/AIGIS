# Skripsi

**Kode:** TKD4802  
**Sifat:** Wajib  
**SKS:** 6  

## Deskripsi

Skripsi (TKD4802) adalah karya tulis ilmiah formal yang disusun oleh mahasiswa sebagai salah satu syarat utama untuk memperoleh gelar Sarjana Geodesi. Penelitian ini merupakan hasil pemikiran orisinal mahasiswa dalam memecahkan masalah di bidang geodesi, fotogrametri, penginderaan jauh, SIG, atau manajemen lahan melalui metodologi ilmiah yang sistematis, terukur, dan dipertanggungjawabkan di bawah bimbingan dosen pembimbing.

## Tujuan Pembelajaran

Setelah menyelesaikan skripsi ini, mahasiswa mampu:

1. Melakukan penelitian ilmiah mandiri sesuai metodologi yang tepat
2. Menganalisis data geodesi/geomatika dengan teknik statistik dan spasial yang valid
3. Menulis karya ilmiah sesuai standar akademik nasional (SINTA)
4. Mempertahankan hasil penelitian secara logis di depan tim penguji
5. Mengintegrasikan teori geodesi dengan solusi praktis terhadap masalah nyata

## Topik Penelitian Umum

| Bidang | Contoh Topik |
|--------|-------------|
| GNSS | Optimasi PPP untuk monitoring deformasi tanah Jakarta |
| Fisika Geodesi | Pemetaan geoid Indonesia dengan data airborne gravity |
| Penginderaan Jauh | Klasifikasi tutupan lahan menggunakan Sentinel-2 dan Random Forest |
| SIG | WebGIS untuk mitigasi bencana longsor |
| Hidrografi | Estimasi kedalaman sungai menggunakan bathymetry UAV |
| Kadastral | Pemodelan 3D kadastral untuk manajemen ruang vertikal |
| Fotogrametri | Pembuatan DEM dari foto udara drone untuk pemetaan kontur |

## Tahapan Skripsi

### 1. Proposal Skripsi (Semester 7 – Minggu 1-4)
- **Pemilihan Topik**: Menentukan minat riset (misal: analisis deformasi, klasifikasi citra, pemetaan kadastral 3D)
- **Studi Literatur**: Mencari jurnal nasional/internasional relevan (minimal 15 referensi)
- **Penyusunan Proposal**: Bab 1 (Pendahuluan), Bab 2 (Tinjauan Pustaka), Bab 3 (Metodologi)
- **Seminar Proposal (Sempro)**: Presentasi desain riset untuk mendapatkan masukan

### 2. Riset dan Pengumpulan Data (Minggu 5-10)
- **Persiapan Survei/Eksperimen**: Kalibrasi alat, izin lapangan, pengumpulan data primer/sekunder
- **Akuisisi Data**: Eksekusi metode (survei GPS/Total Station, ekstraksi citra satelit, pengumpulan data GIS)
- **Quality Control**: Validasi data awal (outlier removal, pengecekan konsistensi data)

### 3. Analisis dan Pembahasan (Minggu 11-16)
- **Pengolahan Data**: Pemrosesan spasial (QGIS, ArcGIS, Python, SNAP, ENVI)
- **Analisis Statistik**: Pengujian hipotesis, pemodelan spasial, akurasi
  - Uji normalitas: $H_0$: data berdistribusi normal (Shapiro-Wilk, $p > 0.05$)
  - RMSE: $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}$
  - Overall Accuracy: $OA = \frac{\sum_{i=1}^{k}p_{ii}}{n}$
  - Kappa Coefficient: $\kappa = \frac{p_o - p_e}{1 - p_e}$
- **Pembahasan (Bab 4)**: Interpretasi hasil, perbandingan dengan penelitian terdahulu
- **Bab 5**: Kesimpulan dan rekomendasi

### 4. Penulisan dan Pendadaran (Minggu 17-20)
- **Drafting Akhir**: Format sesuai pedoman penulisan fakultas
- **Pengecekan Plagiarisme**: Memastikan similarity index < 20% (Turnitin)
- **Ujian Pendadaran (Sidang Skripsi)**: Presentasi hasil dan sesi tanya jawab
- **Revisi**: Perbaikan berdasarkan masukan penguji

## Format Skripsi (Struktur Standar)

- **Halaman Depan**: Judul, logo, identitas mahasiswa/pembimbing
- **Abstrak** (Bahasa Indonesia & Inggris, 150-250 kata)
- **Bab 1: Pendahuluan**: Latar belakang, rumusan masalah, batasan, tujuan, manfaat
- **Bab 2: Tinjauan Pustaka**: Teori dasar, penelitian terkait, kerangka konseptual
- **Bab 3: Metodologi**: Lokasi studi, data, alat, prosedur kerja, diagram alir analisis
- **Bab 4: Hasil dan Pembahasan**: Visualisasi (peta, tabel, grafik), analisis teknis, interpretasi
- **Bab 5: Penutup**: Kesimpulan dan saran untuk penelitian lanjutan
- **Daftar Pustaka**: Standar APA 7th ed. atau IEEE
- **Lampiran**: Data mentah, tabel kalkulasi, foto lapangan, surat izin

## Penilaian

| Komponen | Bobot | Keterangan |
|---|---|---|
| Kualitas Proposal | 10% | Orisinalitas, metodologi, signifikansi |
| Kinerja Riset (Lapangan/Data) | 20% | Ketelitian, akurasi, kedalaman analisis |
| Kualitas Naskah Skripsi | 30% | Kedalaman pembahasan, sistematika, tata tulis |
| Ujian Pendadaran (Sidang) | 40% | Penguasaan teori dan hasil, argumentasi logis |

## Tips Sukses Skripsi

- **Topik vs Minat**: Pilih topik yang Anda minati, bukan sekadar "yang cepat selesai"
- **Pembimbing**: Komunikasi proaktif dengan dosen pembimbing minimal 2x per bulan
- **Data**: Pastikan ketersediaan data riset sebelum memutuskan judul final
- **Sistematika**: Tulis sedikit demi sedikit setiap hari; jangan menumpuk di akhir
- **Software**: Gunakan Reference Manager (Mendeley/Zotero) untuk daftar pustaka otomatis
- **Version Control**: Backup naskah dan kode di Git repository
- **Data Open Source**: Manfaatkan USGS Earth Explorer, Copernicus Open Access Hub, BIG Geoportal

## Referensi

1. Panduan Penulisan Skripsi Fakultas Teknik / Prodi Geodesi [berlaku internal]
2. Creswell, J.W. & Creswell, J.D., "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches", 5th Ed., SAGE, 2018
3. Badan Informasi Geospasial (BIG), https://www.big.go.id/
4. Copernicus Open Access Hub, https://scihub.copernicus.eu/
5. USGS Earth Explorer, https://earthexplorer.usgs.gov/
6. Standar penulisan ilmiah Prodi Geodesi — Pedoman Plagiarisme dan Sitasi
7. Pedoman etika akademik universitas terkait plagiarisme dan properti intelektual