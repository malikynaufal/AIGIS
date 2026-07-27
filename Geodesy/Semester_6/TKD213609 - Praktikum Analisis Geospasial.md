# Praktikum Analisis Geospasial

**Kode:** TKD213609
**Sifat:** Wajib
**SKS:**

## Deskripsi

Praktikum Analisis Geospasial (TKD213609) adalah mata kuliah praktik laboratorium yang membekali mahasiswa dengan keterampilan analisis spasial menggunakan Sistem Informasi Geografis (SIG/GIS). Praktikum ini mencakup operasi overlay, analisis jaringan (network analysis), geoprocessing, dan tool-tool spasial terintegrasi melalui QGIS dan ArcGIS, dengan studi kasus nyata di Indonesia.

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa akan mampu:

1. Melakukan operasi overlay spasial: intersect, union, identity, clip
2. Menjalankan analisis jaringan: rute terpendek, travelling salesman, ketersediaan jasa
3. Menerapkan geoprocessing model untuk pemrosesan data spasial otomatis
4. Melakukan interpolasi spasial (kriging, IDW) untuk pemetaan tematik
5. Membuat peta analisis spasial profesional dengan layout yang benar

## Modul Praktikum

### Modul 1: Pengelolaan Data Spasial
Eksplorasi dan pengelolaan data vektor serta raster:

- Format data: Shapefile, GeoPackage, GeoTIFF, PostGIS

- Proyeksi dan transformasi koordinat (WGS84 → UTM Zona 48S-49S)

- Penggabungan data: merge, dissolve, spatial join

- Join tabel atribut dengan data spasial

- Eksplorasi atribut: query SQL pada kolom spasial

- Latihan: membuat peta kota Bandung dengan layer jalan, sungai, dan batas administrasi

### Modul 2: Analisis Overlay
Operasi spasial gabungan beberapa layer:

- **Intersect** ( $A \cap B $): potongan spasial dua layer

- **Union** ( $ A \cup B $): penggabungan spasial

- **Symmetrical Difference** ( $ A \Delta B $): selisih spasial

- **Clip** (potong layer dengan polygon batas area)

- **Erase**: menghapus bagian overlay dari layer utama

- Buffer zone: penghalusan jarak dari garis/point ( $ d $ meter dari simpul)

- Proximity analysis: jarak terdekat ke titik layanan

- Contoh: menganalisis area potensial pembangunan (lahan + akses jalan + ketersediaan air)

### Modul 3: Analisis Jaringan (Network Analysis)
Optimasi rute dan aksesibilitas menggunakan topologi jaringan:

- **Shortest Path Analysis**: algoritma Dijkstra pada jaringan jalan

$ $ d(v) = \min_{(u,v) \in E}[d(u) + w(u,v)] $ $

- **Service Area**: waktu tempuh (isochrone) dari titik layanan

- **Traveling Salesman Problem (TSP)**: optimasi rute pengiriman ke $ n $ titik

- **Facility Location**: optimal placement lokasi layanan baru

- **Origin-Destination (OD) Matrix**: matriks waktu/jarak antar titik

- Data input: jaringan jalan OSM, titik demand, titik supply

- Latihan: menentukan rute distribusi bantuan logistik di Kabupaten Cianjur

### Modul 4: Geoprocessing dan Model Builder
Otomasi analisis spasial dengan model alur kerja:

- **QGIS Graphical Modeler**: membuat model reusabel

- **ArcGIS ModelBuilder**: visual programming untuk geoprocessing

- **Scripting Python** dengan PyQGIS/ArcPy untuk automasi

- Iterasi input (batch processing) untuk beberapa area studi

- Parameterisasi model: input, output, dan parameter pengguna

- Contoh model: rekapitulasi tutupan lahan per kecamatan dari raster land cover

- Error handling dan logging untuk model kompleks

### Modul 5: Interpolasi Spasial
Membangun surface kontinu dari data titik diskrit:

- **Inverse Distance Weighting (IDW)**

$ $\hat{Z}(x_0) = \frac{\sum_{i=1}^{n}\frac{Z(x_i)}{d(x_0, x_i)^p}}{\sum_{i=1}^{n}\frac{1}{d(x_0, x_i)^p}
}

$ $- **Ordinary Kriging**: model semivariogram dan prediksi terbaik tidak bias:

$ $\gamma(h) = \frac{1}{2N(h)}\sum_{i=1}^{N(h)}[Z(x_i) - Z(x_i+h)]^2

$$

- **Spline** dan **Natural Neighbour** untuk permukaan halus

- Analisis residual dan validasi silang (leave-one-out)

- Perbandingan metode interpolasi berdasarkan RMSE

- Contoh: interpolasi peta curah hujan bulanan dari stasiun BMKG

### Modul 6: Produksi Peta dan Komunikasi Hasil
Desain dan komposisi peta profesional:

- Komponen peta: judul, legenda, skala, proyeksi, sumber data, arah utara

- Classifikasi data kuantitatif: equal interval, quantile, natural breaks, standard deviation

- Skema warna: ColorBrewer, sequential, diverging

- Penggunaan layout composer QGIS

- Ekspor: PDF, PNG, GeoTIFF untuk cetak dan web

- Tugas akhir: peta tematik kecamatan di Jawa Barat dengan minimal 4 layer

## Tugas dan Laporan

### Tugas Per Modul (40%)

- Tugas ringkas per modul (1-2 halaman, screenshots dan hasil)

- Dokumentasi langkah kerja dan hasil intermediate

### Proyek Akhir (60%)
Analisis spasial komprehensif untuk studi kasus pilihan:

- **Topik**: Analisis lokasi optimal fasilitas kesehatan di Kabupaten X

- **Data**: batas kecamatan, lokasi puskesmas, jaringan jalan, populasi, DEM

- **Analisis**: proximity, network (service area), overlay, weighted overlay

- **Laporan**: 10-15 halaman dengan peta penuh

- **Presentasi**: 10 menit + 5 menit tanya jawab

## Penilaian

| Komponen | Bobot |
|---|---|
| Tugas Praktikum (6 modul) | 40% |
| Proyek Akhir - Laporan | 30% |
| Proyek Akhir - Presentasi | 15% |
| Kehaktifan dan Partisipasi | 15% |

## Perangkat Lunak

- **QGIS 3.28 LTS** (Free/Open Source) — utama

- **ArcGIS Pro 3.x** (ESRI) — komplementer

- **PostGIS** — database spasial untuk data besar

- **Google Earth Engine** (opsional) — cloud computing spasial

- **Python 3.8**: rasterio, geopandas, networkx, shapely

## Referensi

1. Longley, P.A. et al., "Geographic Information Systems and Science", 3rd Ed., Wiley, 2015
2. QGIS Development Team, "QGIS User Guide", v3.28 LTS, 2023
3. ESRI, "ArcGIS Pro Help: Network Analyst", 2022
4. Burrough, P.A. & McDonnell, R.A., "Principles of Geographical Information Systems", 3rd Ed., Oxford University Press, 2015
5. OSM Foundation, "OpenStreetMap Wiki - Routing", 2023