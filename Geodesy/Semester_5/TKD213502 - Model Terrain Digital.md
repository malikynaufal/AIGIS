# 📚 Semester 5: Model Terrain Digital

**Kode:** TKD213502
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Model Terrain Digital (DTM) mempelajari representasi permukaan bumi dalam bentuk digital. Mencakup topografi, kontur, TIN, DEM, DSM, grid terstruktur, dan aplikasinya.

## Topik Utama

### 1. Pendefinisian DTM/DEM/DSM

| Tipe | Definisi | Sumber |
|------|----------|--------|
| **DEM** | Elevasi tanah tanpa objek | Survei, interpolasi |
| **DSM** | Elevasi permukaan termasuk objek | Lidar, photogrammetry |
| **DTM** | Model digital terrain: permukaan alami + struktur | DEM + vektor |

### 2. Metode Pembuatan DEM

- **Grid terstruktur (raster)**: resolusi tetap (10, 25, 30, 90 m)

- **TIN** (Triangulated Irregular Network): triangulasi tidak beraturan

- **Contour-based**: dari peta kontur → garis → grid

- **Interpolasi**: Natural Neighbor, IDW, Kriging, Spline, TIN

$$ z = \sum_{i=1}^{n} w_i z_i $ $

### 3. Elevasi dan Kontur

- **Kontur lurus (direct)**: mengukur elevasi pada titik-titik reguler

- **Kontur tidak langsung**: interpolasi (TIN → isolines)

- **Kontur berindeks**: setiap 5 baris atau 10 baris

### 4. Turunan DE M (Terrain Attributes)

| Atribut | Rumus | Penggunaan |
|---------|-------|------------|
| Slope | $\sqrt{(artial z/artial x)^2 + (artial z/artial y)^2} $ | Drainage, landslide |
| Aspect | $\arctan(-artial z/artial x, artial z/artial y) $ | Solar radiation |
| Hillshade | $\cosheta_z\cos\alpha_i + \sinheta_z\sin\alpha_i\cos(hi_{az}-\alpha_{az}) $ | Visualisasi |
| Curvature | $ artial^2 z/artial x^2 $ | Drainage convergence |
| Roughness | $ ext{Var}(z_i) $ | Texture |
| TWI (Topographic Wetness Index) | $\ln(a/an\beta)$ | Hydrology |
| Flow Direction | D8 algorithm | Watershed |

### 5. Sumber Data
| Sumber | Resolusi | Kelebihan |
|--------|----------|-----------|
| SRTM (SRTM1/ASTER GDEM) | 30 m | Global coverage, OA |
| Sentinel-2 stereo | 10 m | Free, high quality |
| ICESat-2 ATL03/ATL08 | 17 m | Photon counting, beam |
| LiDAR ALS | 0.5 m | Dense, high detail |
| UAV LiDAR | 0.1 m | Very dense, affordable |
| GNSS+Photogrammetry | 0.01 m | Precise |

### 6. Aplikasi DTM

- **Flood modeling**: DEM → inundation mapping

- **Landslide susceptibility**: slope + aspect

- **Hydrology**: watershed delineation, stream network

- **Urban planning**: solar exposure, viewshed

- **Volume computation**: cut and fill from DEM comparison

## Tujuan Pembelajaran
1. Memahami DTM data types dan perbedaannya
2. Membangun DEM dari berbagai sumber
3. Menghitung turunan terrain (slope, aspect, curvature)
4. Menggunakan DTM untuk aplikasi hidrologi dan perencanaan

## Referensi

- Li, P., Wong, D.W., *Principles of Geomorphometry*, Springer, 2022.

- Sithole, G. & Malingreau, J.P. (eds.), *Digital Terrain Analysis in Soil Science and Geomorphology*, Elsevier, 2001.

- ArcGIS Pro *Spatial Analyst Tools* documentation (ESRI).

- White, R.A., *Topographic Analysis: A Practical Guide*, Springer, 2012.

➡️ [[Semester 5]] · [[Geodesy MOC]] · [[Geodetic Coordinates]] · [[Map Projection]]