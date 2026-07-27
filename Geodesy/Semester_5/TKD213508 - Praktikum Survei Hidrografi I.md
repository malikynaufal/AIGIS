---
tags: [geodesy, semester-5, praktikum, hydrographic, surveying, ugm]
created: 2026-07-27
---

# 📚 Praktikum Survei Hidrografi I (*Hydrographic Survey I Lab*)

**Kode:** TKD213508
**Sifat:** Wajib
**SKS:** 1 (0-1)
**Prasyarat:** Survei Hidrografi I (TKD213507) — harus diambil bersamaan

---

## 📋 Deskripsi

Praktikum ini melatih mahasiswa dalam pengoperasian echo sounder tunggal (single-beam), pengukuran pasang surut, dan pemrosesan data bathimetri. Kegiatan dilakukan di laboratorium (simulasi) dan di perairan sungai/teluk dekat kampus.

---

## 🌊 Modul Praktikum

### Modul 1: Peralatan Hidrografi

- **Single-beam echo sounder**: Operasi dan kalibrasi
  - Prinsip: $d = \frac{c \cdot t}{2}$(kedalaman =$\frac{v \times t}{2}$)

- **GNSS DGPS/RTK**: Posisi perahu

- **Tide gauge (water level logger)**: Pengukur pasang surut

- **Motion Reference Unit (MRU)**: Roll, pitch, heave sensor

- **CTD (Conductivity-Temperature-Depth)**: Profil kecepatan suara

### Modul 2: Kalibrasi dan Setup

- **Kalibrasi echo sounder**:
  - Draft calibration: $\Delta d = \text{draft statis} + \text{draft dinamis}$- Speed of sound:$c = 1449.2 + 4.6T - 0.055T^2$(Mackenzie formula)

- **Setup tide gauge**: Pasang logger air, zero calibration

- **CTD cast**: Ukur profil salinitas & suhu → hitung SVP

- **Transducer positioning**: Vertical atau ke-sonar (angled)
  

### Modul 3: Sounding di Air Dangkal

- **Pola lintasan**: Paralel, jarak lintasan$s = W_{\text{swath}} \times (1 - 0.20)$untuk 20% overlap

- **Kedalaman**: 1–5 m (muara sungai / perairan teluk)

- **Kecepatan kapal**: 4–6 knot (agar echo sounder stabil)

- **QC**: Cek kedalaman di titik kontrol (known depth)

### Modul 4: Pengukuran Pasang Surut (Tidal Observation)

- **Durasi**: 24 jam minimum (2 pasang surut penuh)

- **Logger interval**: 10–15 menit

- **Analisis**:
  - Identifikasi tipe pasang surut: semidiurnal, diurnal, mixed
  - Hitung MSL, MLLW, MHHW
  - Prediksi pasang surut berikutnya dari analisis harmonik

- **Reduksi sounding**:$d_{CD} = d_{\text{observed}} - (\eta_t - \eta_{CD})$### Modul 5: Data Processing Sederhana

- **Import**: Raw sounding file → software (HYPACK, QPS Qimera, atau open-source)

- **Koreksi**:
  1. Tide correction → referensi Chart Datum
  2. Heel correction →$d_{\text{corr}} = d / \cos\theta$(roll angle$\theta$)
  3. Draft correction → $d_{\text{net}} = d - \text{static draft}$- **Interpolasi**: IDW (Inverse Distance Weighting) ke grid raster$$z = \frac{\sum w_i z_i}{\sum w_i}, \quad w_i = d_i^{-p}$$- **Kontur**: Buat isobaths dari grid

### Modul 6: Kualitas Data & Analisis Kesalahan

- **SDE (Standard Deviation of Depth Error)**:$$\text{SDE} = \sqrt{\frac{\sum(z_{obs} - z_{model})^2}{n-1}}$$- **Crossline check**: Lintasan yang memotong lintasan utama → bandingkan kedalaman

- **Noise filtering**: Median filter, threshold based

- **Akurasi target**: SNI 8435 / IHO S-44 Order 2 → SDE$\leq 0.5$m

### Modul 7: Pembuatan Peta Bathimetri

- **Format output**: GeoTIFF (grid), SHAPEFILE (kontur), SHP/ASCII

- **Legenda**: Warna berdasarkan kedalaman (hypsometric tint)

- **Simbol**: Titik sounding, nama fitur bawah laut

- **Skala**: 1:5.000 – 1:25.000 (tergantung ukuran area)

---

## 🛠️ Software

| Software | Fungsi | Lisensi |
|----------|--------|---------|
| **HYPACK / Qimera** | MBES processing & QC | Commercial |
| **Garmin Quickdraw** | Quick contour (field use) | Commercial |
| **OpenCPN** | Navigation & chart display | Open source |
| **QGIS** | Peta akhir & analisis spasial | Open source (GPL) |
| **Python (NumPy/SciPy)** | Interpolasi, kontur | Open source |
| **Excel/Wavelet tidal** | Analisis pasang surut | Commercial/Open |

---

## 📐 Rumus Utama

| Kuantitas | Rumus |
|-----------|-------|
| Kedalaman |$d = c \cdot t / 2$|
| Kecepatan suara (Mackenzie) |$c = 1449.2 + 4.6T - 0.055T^2 + 1.34(S-35) + 0.016z$|
| Koreksi roll |$d_{\text{corr}} = d / \cos\phi$|
| Koreksi pasang surut |$d_{CD} = d_{\text{obs}} - \Delta\eta$|
| Interpolasi IDW |$z_p = \sum w_i z_i / \sum w_i$, $w_i = r_i^{-p}$|
| Swath width (single beam) |$W = 2d \cdot \tan(\alpha_{\max})$ |

---

## 📚 Referensi

1. **IHO**, *Standards for Hydrographic Surveys*, 6th ed. (S-44), 2008
2. **IHO**, *S-100 Universal Hydrographic Data Model*, 2021
3. **Survei Hidrografi I (TKD213507)** — Materi kuliah teori
4. **Kongsberg Maritime**, *EM Series MBES User Manual*
5. **BIG/BHO**, *Pedoman Survei Hidrografi Nasional*
6. **Stow, D.A.**, *Hydrographic Surveying*, Springer, 2017

➡️ [[Semester 5]] · [[Geodesy MOC]] · [[Geodesy MOC]] · [[Tidal Theory]]
