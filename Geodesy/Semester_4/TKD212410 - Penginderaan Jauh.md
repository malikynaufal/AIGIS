# 📚 Semester 4: Penginderaan Jauh

**Kode:** TKD212410
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Penginderaan Jauh mempelajari pengukuran sifat fisik objek di permukaan bumi dari jarak jauh menggunakan sensor elektromagnetik. Mahasiswa memahami prinsip sensor, interpretasi citra, dan aplikasi dalam pemetaan dan monitoring lingkungan.

## Topik Utama

### 1. Dasar Penginderaan Jauh

- **Spektrosimetri elektromagnetik**: refleksi, emisi, transmisi

- **Atmospheric window**: band visible, IR, microwave

- **Spatial resolution, spectral resolution, radiometric resolution**

### 2. Citra Satelit Optik

| Satelit | Resolusi | Band | Kegunaan |
|---------|----------|------|----------|
| Sentinel-2 | 10 m | RGB+NIR | Vegetasi, pemetaan |
| Landsat 8/9 | 30 m | 11 band | Multi-decade monitoring |
| WorldView-3 | 0.31 m | PAN | High-res detail |
| SPOT-7 | 1.5 m | 4 band | National mapping |

### 3. Citra Radar (SAR)

- **Prinsip SAR**: synthetic aperture radar

- **Coherence & interferometry**: InSAR untuk deformasi

- **Polarimetry**: HV, VH, VV, HH — klasifikasi objek

- **C-band (Sentinel-1)**: penetrasi awan, cocok untuk Indonesia

### 4. Penginderaan Jauh Thermal

- **Thermal infrared**: band 10/11 (Landsat 8)

- **Land Surface Temperature (LST)**: penurunan suhu dari emisi

- Aplikasi: kebakaran hutan, heat island, geothermal

### 5. Analisis Citra

- **Radiometric correction**: topographic correction, atmospheric correction

- **Geometric correction**: rectification, orthorectification

- **Band ratio**: NDVI, NDWI, NDBI
$$
NDVI = \frac{NIR - Red}{NIR + Red}NDWI = \frac{Green - NIR}{Green + NIR}$$# ## 6. Aplikasi

- **Land cover classification**: supervised / unsupervised

- **Change detection**: pre/post disaster

- **LULC mapping** untuk perencanaan tata ruang

## Tujuan Pembelajaran
1. Memahami prinsip elektromagnetik penginderaan jauh
2. Menginterpretasi citra optik dan SAR
3. Melakukan analisis citra (klasifikasi, perubahan)
4. Menerapkan penginderaan jauh dalam pemetaan

## Referensi

- Jensen, J.R., *Remote Sensing of the Environment* (3rd ed.), Pearson, 2015.

- Schowengerdt, R.A., *Remote Sensing: Models and Methods for Image Processing* (3rd ed.), Academic Press, 2007.

- ESA Sentinel Online: https://sentinel.esa.int/

➡️ [[Semester 4]] · [[Geodesy MOC]] · [[SIG]]