# 📚 Semester 4: Praktikum Sistem Fotogrametri Digital

**Kode:** TKD212405
**Sifat:** Wajib
**SKS:** 1 (0-1)

## Deskripsi

Praktikum ini melatih mahasiswa dalam pemrosesan fotogrametri digital menggunakan perangkat lunak terkini. Mahasiswa akan mempraktikkan alur kerja dari foto udara mentah hingga produk akhir (orthophoto, DEM, peta 3D).

## Materi Praktikum

### Modul 1: Akuisisi dan Persiapan Data Foto Udara

- Validasi metadata kamera

- Kalibrasi kamera (parameter IO)

- Import data ke software fotogrametri

### Modul 2: Aerial Triangulation

- Tie point extraction (SIFT/ORB feature matching)

- Bundle adjustment menggunakan least squares

- Optimasi parameter kamera

### Modul 3: Digital Elevation Model (DEM)

- Stereo matching: semi-global matching (SGM) / dense matching

- Pembuatan point cloud (dense point cloud)

- Editing point cloud dan DEM

- Export DEM dalam format GeoTIFF

### Modul 4: Orthophoto Generation

- Orthorektifikasi menggunakan DEM

- Mozaiking dan seamline editing

- Color balancing antar tile

- Export orthophoto

### Modul 5: Feature Extraction (Vektorisasi)

- Ekstraksi bangunan (3D building → LoD2)

- Ekstraksi jalan dan sungai

- Editing vektor di QGIS/ArcGIS

- Pembuatan peta dasar

### Modul 6: Quality Control

- Ground Control Points (GCP) validation

- Check point analysis — residual dan RMSE

- Absolute accuracy vs relative accuracy

## Perangkat Lunak

| Software | Fungsi | Lisensi |
|----------|--------|---------|
| Agisoft Metashape | Full photogrammetric pipeline | Commercial (educational available) |
| Pix4DMapper | Mapping-focused photogrammetry | Commercial |
| OpenDroneMap | Open-source photogrammetry | Open source (GPL) |
| QGIS + GRASS | Produk akhir dan editing | Open source (GPL) |
| CloudCompare | Point cloud analysis | Open source (GPL) |
| Blender + BlenderGIS | 3D visualization | Open source (GPL) |

## Tugas Akhir
Mahasiswa menyelesaikan satu proyek fotogrametri penuh (akuisisi hingga peta akhir) dan mengumpulkan laporan yang mencakup:

- Parameter kamera dan data akuisisi

- Hasil aerial triangulation (residual GCP)

- DEM dan orthophoto

- Analisis akurasi

## Referensi

- Agisoft, *Metashape User Manual*, 2024.

- Luhmann, T. et al., *Close-Range Photogrammetry and 3D Imaging*, De Gruyter, 2014.

- OpenDroneMap Documentation: https://docs.opendronemap.org/

➡️ [[Semester 4]] · [[Geodesy MOC]] · [[Fotogrametri Dasar]]