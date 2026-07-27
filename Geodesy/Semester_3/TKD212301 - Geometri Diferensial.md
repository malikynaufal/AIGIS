# 📚 Semester 3: Geometri Diferensial

**Kode:** TKD212301
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Geometri Diferensial adalah mata kuliah yang mempelajari bentuk dan sifat-sifat geometris dari permukaan dan manifold dalam ruang Euclidean dan non-Euclidean. Konsep-konsep ini menjadi dasar penting dalam geodesi karena bumi memiliki sifat-sifat geometris yang dapat dimodelkan secara differensial.

Dalam konteks geodesi, geometri differensial digunakan untuk memahami bentuk bumi yang sebenarnya, menghasilkan model reference ellipsoid yang lebih akurat, menganalisis deformasi kerak bumi, dan melakukan pemetaan ke permukaan bumi.

## Topik Utama

### 1. Kurva dan Permukaan

- **Kurva ruang** dan parametrizasi

- **Bidang osilasi** dan distribusi berat

- **Kurevatur Gaussian** $K = \kappa_1\kappa_2$dan *mean curvature*$H = (\kappa_1+\kappa_2)/2$- Hubungan dengan derajat flattening ellipsoid

### 2. Tensor Metrik dan Koneksi

- **Tensor metrik pertama** (first fundamental form):$$I = ds^2 = E\,du^2 + 2F\,du\,dv + G\,dv^2$$- **Tensor metrik kedua** (second fundamental form):$$II = L\,du^2 + 2M\,du\,dv + N\,dv^2$$- **Kurevatur Gaussian** dari tensor metrik:$$K = \frac{LN-M^2}{EG-F^2}$$- **Koneksi Levi-Civita** dan simbol Christoffel

### 3. Garis Geodesik
Garis geodesik adalah garis terpendek antara dua titik pada permukaan. Persamaan diferensial garis geodesik pada permukaan:$$\frac{d^2u^i}{ds^2} + \Gamma^i_{jk}\frac{du^j}{ds}\frac{du^k}{ds} = 0
$$

Aplikasi dalam geodesi: perhitungan jarak ellipsoidal ([[Vincenty Formula]]).

### 4. Aplikasi dalam Geodesi

- **Model bumi** — reference ellipsoid sebagai permukaan kuadratik

- **Analisis deformasi kerak** — menggunakan tensor regangan (strain tensor)

- **Pemetaan** — proyeksi peta sebagai transformasi permukaan

## Tujuan Pembelajaran
1. Memahami tensor metrik dan kurevatur pada permukaan
2. Menurunkan persamaan geodesik
3. Menerapkan konsep differensial dalam model ellipsoid
4. Menganalisis deformasi menggunakan tensor regangan

## Referensi

- Do Carmo, M.P., *Differential Geometry of Curves and Surfaces*, Dover, 1976.

- O'Neill, B., *Elementary Differential Geometry* (2nd ed.), Academic Press, 2006.

- Graustein, W.C., *Differential Geometry*, Dover, 1964.

➡️ [[Semester 3]] · [[Geodesy MOC]] · [[Reference Ellipsoid]]