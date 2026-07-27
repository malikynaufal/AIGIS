# 📚 Semester 3: Sistem Referensi Geodesi

**Kode:** TKD212303
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Mata kuliah ini mempelajari sistem koordinat geodetik, ellipsoid referensi, datum geodetik, dan transformasi koordinat. Pemahaman tentang sistem referensi mutlak diperlukan dalam setiap aktivitas survei dan pemetaan.

## Topik Utama

### 1. Sistem Koordinat

**Geodetik** $(\varphi, \lambda, h) $:

$ $ X = (N+h)\cos\varphi\cos\lambdaY = (N+h)\cos\varphi\sin\lambdaZ = (N(1-e^2)+h)\sin\varphi $ $**Geosentrik Kartesian (ECEF)**$ (X,Y,Z) $:

- Dihitung dari ellipsoid referensi

- Tersedia dari pengukuran GNSS

**Lokal ENU** $ (E, N, U) $:

- Rotasi dari ECEF ke local tangent plane

- Berguna untuk survei lapangan

### 2. Ellipsoid Referensi

- [[Reference Ellipsoid]] — parameter ellipsoid

- [[WGS84]] — ellipsoid GPS/global

- [[GRS80]] — ellipsoid NAD83/ETRS89

- Perbandingan parameter antar ellipsoid

### 3. Datum Geodetik

- **Datum lokal**: SAD69, ID74, Batavia (minimisasi residual di kawasan)

- **Datum global**: WGS84, ITRF (geosentrik, berpusat di pusat massa Bumi)

- **Sejarah Indonesia**: Batavia → ID74 → DGN95 → IGD (pengembangan)

### 4. Transformasi Koordinat

- **Transformasi Helmert 7-parameter**: $ X_T = s\cdot R\cdot X_S + T$

- **Grid-based shifts**: NTv2, NADCON

- **Transformasi epoch**: konversi antar epoch ITRF

### 5. Elemen Waktu dan Presisi

- **Waktu GPS**: epoch, minggu GPS

- **Presisi vs akurasi**: definisi dan pembedaan

## Tujuan Pembelajaran
1. Memahami dan mengkonversi antar sistem koordinat
2. Menghitung transformasi antar datum
3. Menentukan parameter ellipsoid referensi
4. Memahami hubungan datum dan kerangka acuan

## Referensi

- Torge, W. & Müller, J., *Geodesy* (4th ed.), De Gruyter, 2012.

- Hofmann-Wellenhof, B. et al., *GNSS — Global Navigation Satellite Systems*, Springer, 2008.

- BIG Indonesia, *Pedoman Datum Referensi Spasial Indonesia*, 2022.

➡️ [[Semester 3]] · [[Geodesy MOC]] · [[Geodetic Datum]] · [[ITRF]]