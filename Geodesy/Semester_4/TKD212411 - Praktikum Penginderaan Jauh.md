# Praktikum Penginderaan Jauh

**Kode:** TKD212411
**Sifat:** Wajib
**SKS:** 1

## Deskripsi

Praktikum ini mempelajari teknik-teknik penginderaan jauh (remote sensing) meliputi akuisisi data, preprocessing, klasifikasi, dan assessment akurasi untuk analisis spasial.

## Catatan Kuliah

### Pengertian Penginderaan Jauh
Penginderaan jauh adalah teknik untuk mendapatkan informasi tentang objek atau area tanpa kontak fisik, umumnya melalui sensor pada pesawat atau satelit.

### Jenis Sensor
1. **Passive Remote Sensing**: Menggunakan radiasi matahari (multispektral, hyperspektral)
2. **Active Remote Sensing**: Menggunakan sumber energi sendiri (radar, LiDAR)

### Akuisisi Data
Proses pengumpulan data meliputi:

- Pemilihan area of interest (AOI)

- Pemilihan waktu akuisisi (season, weather condition)

- Koordinasi dengan penyedia data (Bakosurtanal, LAPAN)

### Preprocessing
Preprocessing diperlukan untuk mempersiapkan data analisis:

#### 1. Radiometric Correction
$$
L_{corrected} = \frac{L_{sensor} - L_{min}}{L_{max} - L_{min}} imes (Digital Number_{max} - Digital Number_{min}
)$\$ $2. Geometric Correction$ $# 2. Geometric Correction

### # 2. Geometric Correction

\begin{bmatrix} X_{ground} \\ Y_{ground} \end{bmatrix} = \begin{bmatrix} a_1 & a_2 \\ b_1 & b_2 \end{bmatrix} \begin{bmatrix} X_{pixel} \\ Y_{pixel} \end{bmatrix} + \begin{bmatrix} a_3 \\ b_3 \end{bmatrix
}$ $3. Atmospheric Correction$ $# 3. Atmospheric Correction

### # 3. Atmospheric CorrectionL_{atm\_corrected} = L_{sensor} - L_{path}$ $Klasifikasi Citra
Klasifikasi mengelompokkan piksel berdasarkan karakteristik spektral:

1. **Supervised Classification**
 - Maximum Likelihood Classification
 - Minimum Distance Classification
 - Support Vector Machine (SVM)
 - Neural Network

2. **Unsupervised Classification**
 - K-means Clustering
 - ISODATA (Iterative Self-Organizing Data Analysis Technique)

### Accuracy Assessment
Evaluasi akurasi menggunakan confusion matrix:$ $## Klasifikasi Citra
Klasifikasi mengelompokkan piksel berdasarkan karakteristik spektral:

1. **Supervised Classification**
 - Maximum Likelihood Classification
 - Minimum Distance Classification
 - Support Vector Machine (SVM)
 - Neural Network

2. **Unsupervised Classification**
 - K-means Clustering
 - ISODATA (Iterative Self-Organizing Data Analysis Technique)

### Accuracy Assessment
Evaluasi akurasi menggunakan confusion matrix:\begin{aligned}
ext{Overall Accuracy} &= \frac{ext{Sum of Diagonal Elements}}{ext{Total Samples}} imes 100\%
\end{aligned}\begin{aligned}
ext{User Accuracy} &= \frac{ext{Correctly Classified Pixels per Class}}{ext{Total Pixels Classified per Class}} imes 100\%
\end{aligned}\begin{aligned}
ext{Producer Accuracy} &= \frac{ext{Correctly Classified Pixels per Class}}{ext{Total Reference Pixels per Class}} imes 100\%
\end{aligned}$$# ## Klasifikasi Citra
Klasifikasi mengelompokkan piksel berdasarkan karakteristik spektral:

1. **Supervised Classification**
 - Maximum Likelihood Classification
 - Minimum Distance Classification
 - Support Vector Machine (SVM)
 - Neural Network

2. **Unsupervised Classification**
 - K-means Clustering
 - ISODATA (Iterative Self-Organizing Data Analysis Technique)

### Accuracy Assessment
Evaluasi akurasi menggunakan confusion matrix:\begin{aligned}
ext{Overall Accuracy} &= \frac{ext{Sum of Diagonal Elements}}{ext{Total Samples}} imes 100\%
\end{aligned}\begin{aligned}
ext{User Accuracy} &= \frac{ext{Correctly Classified Pixels per Class}}{ext{Total Pixels Classified per Class}} imes 100\%
\end{aligned}\begin{aligned}
ext{Producer Accuracy} &= \frac{ext{Correctly Classified Pixels per Class}}{ext{Total Reference Pixels per Class}} imes 100\%
\end{aligned}

### Aplikasi dalam Geodesi
Penginderaan jauh digunakan untuk:
1. **Pemetaan Topografi**: Produksi DEM/DTM
2. **Land Cover Mapping**: Pemetaan tutupan lahan
3. **Urban Monitoring**: Pemantauan perubahan kota
4. **Disaster Management**: Monitoring bencana alam
5. **Climate Studies**: Analisis perubahan iklim

### Software Penginderaan Jauh

- **ERDAS IMAGO**: Analisis citra komersial

- **ENVI**: Analisis spektral lanjut

- **QGIS**: Pemetaan open-source dengan plugin remote sensing

- **Google Earth Engine**: Platform cloud untuk analisis temporal

## Tugas dan Proyek

### Tugas Individu
1. **Preprocessing Citra**: Lakukan correction pada citra Landsat/Sentinel
2. **Klasifikasi Sederhana**: Bandingkan metode supervised dan unsupervised
3. **Accuracy Assessment**: Hitung dan bandingkan akurasi berbagai metode

### Proyek Kelompok
1. **Land Cover Change Detection**: Analisis perubahan tutupan lahan
2. **Vegetation Index Analysis**: Analisis NDVI untuk area pertanian
3. **Urban Heat Island**: Pemanfaatan citra thermal

### Penilaian

- **Tugas Praktikum (40%)**: Laporan dan hasil praktikum

- **Proyek Akhir (35%)**: Proyek analisis penginderaan jauh

- **Ujian Praktikum (25%)**: Evaluasi kemampuan praktis