# Praktikum Analisis Citra Penginderaan Jauh

**Kode:** TKD213607
**Sifat:** Wajib
**SKS:**

## Deskripsi

Praktikum Analisis Citra Penginderaan Jauh (TKD213607) adalah mata kuliah praktik laboratorium yang mendampingi mata kuliah teori TKD213606. Mahasiswa akan mengerjakan alur kerja pengolahan citra satelit secara langsung menggunakan perangkat lunak standar industri seperti ENVI, SNAP (ESA), dan QGIS. Praktikum ini mencakup preprocessing, klasifikasi terbimbing, kalkulasi NDVI, segmentasi, dan penilaian akurasi menggunakan data Landsat 8 dan Sentinel-2 untuk wilayah Indonesia.

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa akan mampu:

1. Mengimpor, memvisualisasikan, dan memproyeksikan citra satelit multi-band
2. Melakukan koreksi atmosferik menggunakan algoritma DOS (Dark Object Subtraction) dan FLAASH
3. Melakukan klasifikasi terbimbing (supervised classification) dengan algoritma Maximum Likelihood dan Random Forest
4. Menghitung indeks spektral (NDVI, NDWI, EVI, SAVI) dan menginterpretasikannya
5. Melakukan segmentasi citra dan klasifikasi berbasis objek (OBIA)
6. Menyusun matriks konfusi dan melaporkan metrik akurasi klasifikasi

## Modul Praktikum

### Modul 1: Pengenalan Perangkat Lunak
Eksplorasi antarmuka dan data:

- **ENVI**: menampilkan band RGB, band calculator, metadata viewer

- **SNAP (ESA)**: import Sentinel-2 L1C, reproyeksi, graph builder

- **QGIS**: plugin Semi-Automatic Classification, raster calculator, map composer

- **Sen2Cor**: koreksi atmosferik Sentinel-2 dari L1C ke L2A

- Latihan: memuat citra Landsat 8 path/row 120/65 (Jawa Tengah)

### Modul 2: Preprocessing dan Koreksi
Transformasi data mentah ke data siap analisis:

- Kalibrasi digital number (DN) ke Top of Atmosphere (TOA) reflectance:
$$
\rho_{TOA} = \frac{i \cdot L_\lambda \cdot d^2}{ESUN_\lambda \cdot \cosheta_s} $ $- Koreksi atmosferik SNAP (Sen2Cor) untuk Sentinel-2

- Koreksi geometrik menggunakan Ground Control Points (GCP)

- Mosaicing, cropping, dan reproyeksi (UTM → WGS 84)

- Landsat 8 pan-sharpening: Gram-Schmidt, Brovey, IHS

### Modul 3: Indeks Spektral
Menghitung dan menginterpretasikan indeks dari citra:

- NDVI untuk pemetaan vegetasi$ $NDVI = \frac{Band5 - Band4}{Band5 + Band4} \quad (ext{Landsat 8})$\$ $- NDWI untuk deteksi badan air

- SAVI (Soil Adjusted Vegetation Index) untuk lahan terbuka$ $ SAVI = \frac{(NIR - Red)(1 + L)}{NIR + Red + L} $ $- EVI untuk koreksi atmosferik setengah

- Color slicing dan thresholding untuk pemisahan kelas

- Tugas: membuat peta NDVI Pulau Bali dengan threshold $NDVI < 0.2$ lahan terbuka, $0.2 < NDVI < 0.6$ vegetasi jarang, $NDVI > 0.6$ vegetasi lebat

### Modul 4: Klasifikasi Terbimbing (Supervised)
Teknik klasifikasi piksel berbasis training sample:

- Pengambilan training sample menggunakan Region of Interest (ROI) dengan minimal 50 piksel per kelas

- Klasifikasi Maximum Likelihood$ $ p(\omega_i|x) = \frac{p(x|\omega_i)P(\omega_i)}{p(x)}$ $- Support Vector Machine (SVM) dengan kernel RBF

- Random Forest dengan 100 trees

- K-fold cross-validation untuk validasi training set

- Perbandingan hasil antar algoritma

### Modul 5: Klasifikasi Berbasis Objek (OBIA)
Segmentasi dan klasifikasi berdasarkan bentuk spasial:

- Segmentasi multiresolusi (eCognition / SNAP):
 - Skala: 50-100-200
 - Bentuk: 0.1
 - Compactness: 0.5

- Aturan fuzzy untuk klasifikasi segmen

- Feature extraction: bentuk, tekstur, konteks, indeks

- OBIA vs. per-piksel: akurasi lebih tinggi untuk area heterogen

### Modul 6: Penilaian Akurasi
Validasi hasil klasifikasi:

- Pengumpulan ground truth (minimal 50 titik per kelas)

- Matriks konfusi 2D: baris = referensi, kolom = klasifikasi

- Metrik akurasi:
 - **Overall Accuracy**: proporsi benar
 - **Kappa Coefficient**:$ $\hat{\kappa} = \frac{N\sum_{i=1}^{r}x_{ii} - \sum_{i=1}^{r}(x_{i+} \cdot x_{+i})}{N^2 - \sum_{i=1}^{r}(x_{i+} \cdot x_{+i})} $$- **User's Accuracy**: probabilitas piksel kelas A di lapangan sesuai peta
 - **Producer's Accuracy**: probabilitas piksel terklasifikasi benar

- ROC curve dan area under curve (AUC) untuk model klasifikasi

## Laporan Praktikum

### Format Laporan

- Judul, nama, NIM, tanggal

- Tujuan dan area studi (contoh: Subang, Jawa Barat)

- Data dan perangkat lunak yang digunakan

- Metodologi: diagram alir preprocessing → klasifikasi → akurasi

- Hasil: peta tematik, tabel matriks konfusi, grafik NDVI

- Diskusi: sumber kesalahan, keterbatasan, usulan perbaikan

- Kesimpulan dan lampiran

## Penilaian

| Komponen | Bobot |
|---|---|
| Laporan Praktikum per Modul (6 module) | 50% |
| Proyek Akhir: Klasifikasi Tutupan Lahan (Landsat 8) | 30% |
| Ujian Praktik (real-time processing) | 20% |

## Perangkat Lunak

- **ENVI 5.6** (Harris Geospatial) — preprocessing dan klasifikasi

- **SNAP 9.0** (ESA) — Sentinel-2 processing

- **QGIS 3.28** (OSGeo) — visualisasi dan layout peta

- **eCognition Developer 9.0** (Trimble) — OBIA

- **Sen2Cor 2.10** — koreksi atmosferik Sentinel-2

- **Python 3.8** (rasterio, scikit-learn, matplotlib) — processing alternatif

## Referensi

1. ENVI, "ENVI 5.6 User's Guide", L3Harris, 2021
2. ESA, "SNAP Desktop User Manual", v9.0, 2022
3. Congalton, R.G. & Green, K., "Assessing the Accuracy of Remotely Sensed Data: Principles and Practices", 3rd Ed., CRC Press, 2019
4. Trimble, "eCognition Developer Reference Book", 2020
5. USGS, "Landsat 8 Surface Reflectance Code (LASRC)", 2021