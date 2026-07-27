---
tags: [geodesy, semester-5, praktikum, gnss, surveying, ugm]
created: 2026-07-27
---

# 📚 Praktikum Survei GNSS (*GNSS Surveying Lab*)

**Kode:** TKD213506
**Sifat:** Wajib
**SKS:** 1 (0-1)
**Prasyarat:** Survei GNSS (TKD213505) — harus diambil bersamaan

---

## 📋 Deskripsi

Praktikum ini melatih mahasiswa dalam pengoperasian receiver GNSS geodetik, perencanaan observasi, pengolahan data baseline, dan penentuan koordinat presisi menggunakan metode statik, rapid statik, dan RTK.

---

## 🛰️ Modul Praktikum

### Modul 1: Pengenalan Peralatan GNSS Geodetik

- **Receiver geodetik**: Dual-frequency, multi-konstelasi (GPS+GLONASS+Galileo+BeiDou)

- **Antenna**: Choke-ring atau ground-plane, ARP (Antenna Reference Point)

- **Aksesoris**: Tribrach, tripod, kabel data, battery

- **Pengukuran tinggi antena**: Slant height → vertical height

$$h_{\text{vert}} = \sqrt{h_{\text{slant}}^2 - r_{\text{antenna}}^2} $$### Modul 2: Perencanaan Observasi GNSS

- **PDOP prediction**: Menggunakan software planning (RTKLIB, Trimble Planning
)

$$PDOP < 6 \text{ (minimal)}, < 4 \text{ (optimal)} $$

- **Elevation mask**:$10^\circ$–$15^\circ$(standard Indonesia)

- **Session planning**: Baseline < 10 km → 15–30 menit; Baseline 10–50 km → 1–2 jam

- **Sky plot**: Analisis obstruksi di lokasi survei

### Modul 3: Metode Statik (Static Surveying)

- **Prosedur lapangan**:
 1. Setup receiver di titik yang akan diukur
 2. Catat tinggi antena (sebelum & sesudah)
 3. Log sheet: station ID, receiver S/N, antena type, start/stop time, weather
 4. Durasi: 45–120 menit (tergantung baseline)

- **Data format**: RINEX 3.03 / 3.04 (.obs, .nav, .glo, .gal)

- **Base station**: INACORS atau receiver yang dipasang di titik ikat

### Modul 4: Rapid Static & Stop-and-Go

- **Rapid Static**: 15–30 menit per titik, baseline < 20 km

- **Stop-and-Go**: Inisialisasi di titik ikat → 2–5 menit per titik rover

- **Re-inisialisasi**: Setiap 30 menit atau setelah lost-lock

### Modul 5: RTK (Real-Time Kinematic)

- **Setup Base-Rover**: Radio link (UHF 433/900 MHz) atau NTRIP via internet

- **Initialisasi**: OTF (On-The-Fly) — butuh 30–60 detik

- **Pengukuran titik**: 5–10 epoch per titik → rata-rata koordinat

- **Check**: Ukur ulang 10% titik untuk QC

### Modul 6: Pengolahan Data dengan RTKLIB

- **RTKCONV**: Konversi data receiver → RINEX 3

- **RTKPOST**: Post-processing baseline (static, kinematic, PPP)

- **Konfigurasi**:
 - Elevation mask:$15^\circ$
 - Ionosphere: Ionosphere-free linear combination ($LC$)
 - Troposphere: Saastamoinen model + estimation
 - Ambiguity: Fix-and-hold (LAMBDA method)

- **Output**: .pos (coordinate), .stat (quality), .res (residual)

### Modul 7: Quality Control & Evaluasi

- **Residual analysis**: Plot residual vs epoch

- **RMS error**: Bandingkan koordinat dengan titik kontrol

$$RMS = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - x_{\text{ref}})^2} $$

- **Cycle slip detection**: Analisis MW (Melbourne-Wübbena) combination

- **PDOP masking**: Buang epoch dengan PDOP > 6

### Modul 8: Laporan Praktikum
Setiap modul menghasilkan laporan yang mencakup:
1. **Tujuan** — apa yang diukur
2. **Metode** — prosedur lapangan & pengolahan
3. **Data mentah** — RINEX header, log sheet
4. **Hasil pengolahan** — koordinat, RMS, residual
5. **Analisis** — ketelitian, faktor kesalahan
6. **Kesimpulan** — akurasi yang dicapai

---

## 🛠️ Software & Tools

| Software | Fungsi | Lisensi |
|----------|--------|---------|
| **RTKLIB** (RTKPOST, RTKCONV, RTKNAVI) | Full GNSS processing suite | Open source (BSD) |
| **Trimble Business Center** | Commercial processing | Commercial |
| **Leica Infinity** | Commercial processing | Commercial |
| **TEQC** | Quality checking RINEX | Open source |
| **GAMIT/GLOBK** | Scientific network adjustment | Academic (MIT) |
| **QGIS** | Visualisasi hasil | Open source (GPL) |
| **Google Earth** | Visualisasi track & points | Free |

---

## ✅ Tugas Akhir Praktikum

Setiap mahasiswa menyelesaikan **satu proyek survei GNSS penuh**:
1. Perencanaan observasi (PDOP, satellite visibility)
2. Observasi lapangan (base + 3 rover points)
3. Pengolahan baseline (static + RTK)
4. Perbandingan akurasi: static vs RTK
5. Laporan akhir + file RINEX + file .pos

---

## 📚 Referensi

1. **RTKLIB Manual** — Takasu, T., *RTKLIB: An Open Source Program Package for GNSS Positioning*
2. **Hofmann-Wellenhof et al.**, *GNSS — Global Navigation Satellite Systems*, Springer, 2008
3. **Leick, A. et al.**, *GPS Satellite Surveying*, 4th ed., Wiley, 2015
4. **BIG**, *Pedoman Survei GNSS untuk Jaring Kontrol Geodesi*
5. **IGS**, *RINEX 3.04 Format Specification*

➡️ [[Semester 5]] · [[GNSS]] · [[Geodesy MOC]] · [[RTK]] · [[PPP]]
