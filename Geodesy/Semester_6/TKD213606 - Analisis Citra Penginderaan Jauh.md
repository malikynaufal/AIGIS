# Analisis Citra Penginderaan Jauh

**Kode:** TKD213606 
**Sifat:** Wajib 
**SKS:** 

## Deskripsi

Analisis Citra Penginderaan Jauh (TKD213606) adalah mata kuliah teori yang membahas prinsip, teknik, dan aplikasi penginderaan jauh (remote sensing) dalam konteks geodesi dan geomatika. Mahasiswa mempelajari dasar elektromagnetik, preprocessing citra, ekstraksi fitur, klasifikasi spektral dan spasial, deteksi perubahan, serta penilaian akurasi — dengan penekanan pada penginderaan jauh optik, SAR, dan LiDAR untuk pemetaan Indonesia.

## Tujuan Pembelajaran

Setelah menyelesaikan mata kuliah ini, mahasiswa akan mampu:

1. Menjelaskan prinsip dasar penginderaan jauh dan interaksi radiasi elektromagnetik dengan permukaan bumi
2. Melakukan preprocessing citra satelit: koreksi atmosferik, geometrik, dan radiometrik
3. Menerapkan metode ekstraksi fitur dan klasifikasi citra untuk peta tutupan lahan
4. Melakukan deteksi perubahan spasial menggunakan citra multi-temporal
5. Menilai akurasi hasil klasifikasi menggunakan matriks konfusi

## Modul Pembelajaran

### Modul 1: Prinsip Dasar Penginderaan Jauh
Fisika radiasi elektromagnetik dan interaksi dengan permukaan bumi:

- Spektrum elektromagnetik: UV, Visible, NIR, SWIR, TIR, microwave

- Sinar matahari sebagai sumber radiasi pasif

- Hukum Planck dan radiasi benda hitam: $B_\lambda = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_BT}-1} $- Konsep spektrum reflektan:$\rho_\lambda = \frac{L_\lambda}{E_\lambda} $untuk material tanah, air, dan vegetasi

- Karakteristik spektrum air:$\rho$ rendah di NIR ($\rho_{NIR} < 0.05$)

- Karakteristik spektrum vegetasi: red edge di 700nm dan plateu di NIR

- Platform penginderaan jauh: satelit (Landsat, Sentinel, SPOT), pesawat, drone

### Modul 2: Platform dan Sensor
Pemahaman terhadap sistem penginderaan jauh utama:

- **Landsat 8/9 OLI**: 11 band, resolusi spasial 15-100m, revisit 16 hari

- **Sentinel-2 MSI**: 13 band (B1-B12), resolusi 10-60m, revisit 5 hari

- **Sentinel-1 SAR**: C-band, dual polarization (VV/VH), all-weather

- **LiDAR**: pulsa laser untuk model elevasi presisi tinggi

- **Drone**: resolusi sub-meter untuk survei lokal

- Sensor aktif vs. pasif; resolusi spasial, spektral, temporal, radiometrik

### Modul 3: Preprocessing Citra
Langkah pemrosesan citra mentah menjadi citra siap analisis:

- **Koreksi atmosferik**: MODTRAN, 6S, Dark Object Subtraction

- Transformasi Top of Atmosphere (TOA) ke Bottom of Atmosphere (BOA)

- **Koreksi geometrik**: orthorectification menggunakan DEM dan GCPs

- Koreksi radiometrik: kalibrasi DN ke reflectance permukaan

- Pemotongan (cropping), reproyeksi, dan penataan ulang piksel

### Modul 4: Ekstraksi Fitur dan Indeks
Teknik mendapatkan informasi dari citra:

- Indeks Vegetasi Normalized Difference Vegetation Index:

$$NDVI = \frac{NIR - RED}{NIR + RED
}

$$- NDWI (Normalized Difference Water Index) untuk deteksi air:$$

NDWI = \frac{GREEN - NIR}{GREEN + NIR
}

$$- EVI (Enhanced Vegetasi Index) untuk vegetasi padat:$$

EVI = 2.5 \times \frac{NIR - RED}{NIR + 6 \times RED - 7.5 \times BLUE + 1} $$

- Pita rasio dan indeks tekstur

- Transformasi PCA (Principal Component Analysis) untuk kompresi data

- Edge detection dan segmentasi citra

### Modul 5: Klasifikasi Citra
Teknik pengelompokan piksel berdasarkan spektrum:

- **Supervised**: Maximum Likelihood, Support Vector Machine (SVM), Random Forest

- **Unsupervised**: K-means clustering, ISODATA

- Training samples: homogenitas, representativitas, jumlah minimal ($n \geq 10 \times p $dimensi)

- Deep learning: Convolutional Neural Networks (CNN) untuk klasifikasi citra

- Perbandingan metode berdasarkan kompleksitas dan akurasi

### Modul 6: Deteksi Perubahan dan Akurasi
Analisis perubahan spasial temporal:

- **Post-classification comparison**: matriks transisi tutupan lahan

- **Image differencing**:$\Delta DN = DN_{t_2} - DN_{t_1} $- **Change Vector Analysis (CVA)**: deteksi perubahan multivariate

- **LandTrendr**: analisis tren temporal Landsat

- Matriks konfusi dan metrik akurasi:
 - Overall Accuracy:$OA = \frac{\sum_{i=1}^{k}p_{ii}}{n} $- Kappa Coefficient:$\kappa = \frac{p_o - p_e}{1 - p_e} $
 - Producer's Accuracy dan User's Accuracy per kelas

## Pustaka Utama

1. Jensen, J.R., "Remote Sensing of the Environment: An Earth Resource Perspective", 3rd Ed., Pearson, 2014
2. Richards, J.A. & Jia, X., "Remote Sensing Digital Image Analysis: An Introduction", 5th Ed., Springer, 2012
3. Campbell, J.B. & Wynne, R.H., "Introduction to Remote Sensing", 5th Ed., Guilford Press, 2011
4. Lillesand, T.M. et al., "Remote Sensing and Image Interpretation", 7th Ed., Wiley, 2015
5. USGS, "Landsat 8 Data Users Manual", 2021
6. European Space Agency, "Sentinel-2 User Handbook", 2015

## Referensi Tambahan

- Schowengerdt, R.A., "Remote Sensing: Models and Methods for Image Processing", 3rd Ed., Academic Press, 2007

- Gao, F. et al., "MODIS Vegetation Index Products", NASA, 2020

- IPCC, "Guidelines for National Greenhouse Gas Inventories", Vol. 4: AFOLU, 2006