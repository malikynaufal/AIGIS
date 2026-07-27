# 📚 Semester 4: Grafika Komputer dan Visualisasi

**Kode:** TKD212406
**Sifat:** Wajib
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Mata kuliah ini mempelajari konsep dan teknik grafika komputer 3D dan visualisasi data geospasial. Mahasiswa mempelajari rendering, modeling 3D, dan visualisasi data berbasis web.

## Topik Utama

### 1. Dasar Grafika Komputer

- **Raster vs Vektor**: model data gambar

- **Transformasi geometri**: translation, rotation, scaling (matrix 4×4)

- **Perspective projection**:
$$\begin{bmatrix} x_w \\ y_w \\ z_w \\ w \end{bmatrix} = \begin{bmatrix} 2n/(r-l) & 0 & (r+l)/(r-l) & 0 \\ 0 & 2n/(t-b) & (t+b)/(t-b) & 0 \\ 0 & 0 & -(f+n)/(f-n) & -2fn/(f-n) \\ 0 & 0 & -1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$

### 2. Modeling 3D

- Mesh modeling (triangulation)

- Point cloud → mesh conversion

- DEM → 3D terrain rendering

- Texture mapping dan UV mapping

### 3. Shading dan Rendering

- Lambertian / Phong shading models

- Z-buffer algorithm

- Ray tracing

- Real-time rendering pipeline (OpenGL/WebGL)

### 4. Visualisasi Data Geospasial

- **DEM visualization**: hypsometric tinting, hillshade, slope maps

- **3D city models**: CityGML LOD 0–4

- **Web mapping**: Leaflet.js, OpenLayers, Mapbox GL

- **3D visualization**: CesiumJS, Three.js, deck.gl

### 5. Tools

- **Blender**: 3D modeling dan rendering

- **QGIS 3D**: Visualisasi 3D geospasial

- **Three.js / CesiumJS**: Visualisasi 3D berbasis web

- **BlenderGIS**: Import data geospasial ke Blender

## Tujuan Pembelajaran
1. Memahami dasar transformasi grafika komputer
2. Membuat model 3D dari data geospasial
3. Menghasilkan visualisasi DEM dan kota 3D
4. Mengimplementasikan visualisasi berbasis web

## Referensi

- Foley, J.D. et al., *Computer Graphics: Principles and Practice* (3rd ed.), Addison-Wesley, 1996.

- Zeiler, M., *Exploring ArcGIS*, ESRI Press, 2010.

- CesiumJS Documentation: https://cesium.com/learn/cesiumjs-learn/

➡️ [[Semester 4]] · [[Geodesy MOC]] · [[Map Projection]]