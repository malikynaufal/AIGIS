# 📚 Semester 3: Fotogrametri Dasar

**Kode:** TKD212304
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Fotogrametri Dasar mempelajari prinsip-prinsip pengukuran dari foto udara dan citra satelit untuk menghasilkan peta, model elevasi digital, dan produk geospasial lainnya. Mata kuliah ini mencakup geometri kamera, orientasi foto, stereoskopi, dan ekstraksi informasi 3D.

## Topik Utama

### 1. Geometri Kamera

$$x = -f\frac{a_1(X-X_0)+b_1(Y-Y_0)+c_1(Z-Z_0)}{a_3(X-X_0)+b_3(Y-Y_0)+c_3(Z-Z_0)}$$
$$y = -f\frac{a_2(X-X_0)+b_2(Y-Y_0)+c_2(Z-Z_0)}{a_3(X-X_0)+b_3(Y-Y_0)+c_3(Z-Z_0)}$$

- $f$ = focal length
- $(X_0, Y_0, Z_0)$ = posisi kamera
- $a_i, b_i, c_i$ = elemen orientasi luar

### 2. Orientasi Foto

**Orientasi Dalam (Interior Orientation)**: parameter kamera (focal length, principal point, lens distortion).

**Orientasi Luar (Exterior Orientation)**: 6 parameter — posisi $(X_0,Y_0,Z_0)$ dan orientasi sudut $(\omega,\varphi,\kappa)$.

### 3. Stereoskopi dan Parallax

Parallax stereoskopik:
$$B = Z_1 - Z_2 \quad\text{(base)}$$
$$p = x_1 - x_2 \quad\text{(x-parallax)}$$

Perhitungan tinggi dari parallax:
$$\Delta h = \frac{H \cdot \Delta p}{B + \Delta p}$$

### 4. Orthorektifikasi

Mengoreksi distorsi geometrik pada foto akibat relief:
$$X = X_0 + (Z-Z_0)\frac{a_1x + a_2y - a_3f}{c_1x + c_2y - c_3f}$$

### 5. Digital Photogrammetry Workflow

1. **Aerial triangulation** — bundle adjustment, hitung parameter orientasi
2. **Stereo matching** — automatic DTM generation
3. **Orthophoto generation** — true ortho
4. **Feature extraction** — vektorisasi bangunan, jalan, sungai

### 6. UAV Photogrammetry

- Platform UAV (drone) untuk area kecil (< 5 km²)
- Software: Agisoft Metashape, Pix4D, DJI Terra
- GSD (Ground Sample Distance) tipikal: 1-5 cm

## Tujuan Pembelajaran
1. Memahami geometri proyeksi kamera
2. Melakukan orientasi foto (dalam dan luar)
3. Menghitung tinggi objek dari stereoskopi
4. Menghasilkan orthophoto dan DEM

## Referensi
- Wolf, P.R. & Dewitt, B.A., *Elements of Photogrammetry with Applications in GIS* (4th ed.), McGraw-Hill, 2014.
- Luhmann, T. et al., *Close-Range Photogrammetry and 3D Imaging* (2nd ed.), De Gruyter, 2014.
- Kraus, K., *Photogrammetry — Geometry from Images and Laser Scans* (2nd ed.), De Gruyter, 2007.

➡️ [[Semester 3]] · [[Geodesy MOC]] · [[Map Projection]] · [[Geodetic Coordinates]]