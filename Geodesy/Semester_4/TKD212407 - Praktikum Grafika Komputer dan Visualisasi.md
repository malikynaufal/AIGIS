# Praktikum Grafika Komputer dan Visualisasi

**Kode:** TKD212407  
**Sifat:** Wajib  
**SKS:** 1  

## Deskripsi

Praktikum ini memberikan pengalaman praktis dalam grafika komputer untuk aplikasi geospasial, meliputi penggunaan QGIS, web mapping, dan 3D terrain visualization.

## Catatan Kuliah

### QGIS (Quantum GIS)
QGIS adalah software SIG open-source yang powerful untuk visualisasi dan analisis data spasial.

#### Setup dan Konfigurasi
```
Project Settings:
- CRS: EPSG:4326 (WGS84) atau EPSG:32748 (UTM Zone 48S)
- Project Coordinate System: UTM untuk pengukuran
```

#### Import dan Visualisasi Data
```python
# QGIS Python Console Example
from qgis.core import QgsVectorLayer, QgsProject

# Load shapefile
layer = QgsVectorLayer('/path/to/data.shp', 'Survey Points', 'ogr')
QgsProject.instance().addMapLayer(layer)

# Symbolisasi
from qgis.core import QgsMarkerSymbol
symbol = QgsMarkerSymbol.createSimple({
    'name': 'circle',
    'color': 'red',
    'size': '3.0'
})
layer.renderer().setSymbol(symbol)
```

### Web Mapping dengan Leaflet
Leaflet adalah library JavaScript untuk peta interaktif berbasis web.

#### Setup Basic Map
```javascript
// Initialize map
var map = L.map('map').setView([-6.2088, 106.8456], 10);

// Add tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
}).addTo(map);

// Add marker
L.marker([-6.2088, 106.8456]).addTo(map)
    .bindPopup('Kantor UGM')
    .openPopup();
```

#### Coordinate System Handling
```javascript
// WGS84 to UTM conversion
function wgs84ToUtm(lat, lon) {
    var zoneNumber = Math.floor((lon + 180) / 6) + 1;
    var isNorth = lat >= 0;
    
    // Simplified UTM conversion
    var x = lon * 111320;
    var y = Math.log(Math.tan((45 + lat/2) * Math.PI / 180)) * 6378137;
    
    return { easting: x, northing: y };
}
```

### 3D Terrain Visualization
Pembuatan visualisasi terrain 3D menggunakan WebGL dan DEM data.

#### DEM to 3D Mesh
```javascript
// Three.js example
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

function createTerrainFromDem(demData) {
    var geometry = new THREE.PlaneGeometry(100, 100, demData.width-1, demData.height-1);
    var vertices = geometry.attributes.position.array;
    
    for (var i = 0; i < demData.height; i++) {
        for (var j = 0; j < demData.width; j++) {
            var idx = (i * demData.width + j);
            var elevation = demData.values[i][j];
            vertices[idx * 3 + 2] = elevation; // Z coordinate = elevation
        }
    }
    
    geometry.computeVertexNormals();
    return new THREE.Mesh(geometry, new THREE.MeshPhongMaterial({ color: 0x00ff00 }));
}
```

### Integrasi Data Geospasial
#### Menghubungkan Citra dengan Koordinat
$$
\begin{aligned}
X_{gis} &= X_{origin} + col \times pixel\_size \\
Y_{gis} &= Y_{origin} - row \times pixel\_size
\end{aligned}
$$

#### Coordinate Transformation Example
```python
# Proses transformasi koordinat untuk visualisasi
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:4326", "EPSG:32748", always_xy=True)
x_utm, y_utm = transformer.transform(lon_wgs84, lat_wgs84)

# Format untuk QGIS
print(f"UTM Coordinates: {x_utm:.3f}, {y_utm:.3f}")
```

### Animasi dan Interaktivitas
#### Real-time Data Visualization
```javascript
// Update lokasi real-time
function updateMarkerPosition(marker, newPosition) {
    marker.setLatLng([newPosition.lat, newPosition.lng]);
    marker.bindPopup(`
        <h3>Posisi Saat Ini</h3>
        <p>Lat: ${newPosition.lat.toFixed(6)}</p>
        <p>Lon: ${newPosition.lng.toFixed(6)}</p>
        <p>Time: ${new Date().toLocaleTimeString()}</p>
    `);
}

// Set interval update
setInterval(function() {
    var newPos = getCurrentPosition(); // Fungsi untuk mendapatkan posisi
    updateMarkerPosition(myMarker, newPos);
}, 5000);
```

## Tugas dan Praktikum

### Tugas 1: QGIS Basic
**Objektif:** Memahami dasar-dasar QGIS untuk visualisasi data spasial

**Prosedur:**
1. Install dan setup QGIS
2. Import data shapefile dan raster
3. Buat symbology dan label
4. Export hasil visualisasi

### Tugas 2: Web Mapping Implementation
**Objektif:** Membuat peta interaktif berbasis web

**Prosedur:**
1. Setup project HTML/JavaScript
2. Implementasi Leaflet/OpenLayers
3. Add overlay layers
4. Deploy ke web server

### Tugas 3: 3D Terrain Visualization
**Objektif:** Membuat visualisasi terrain 3D

**Prosedur:**
1. Download DEM data
2. Setup Three.js/WebGL environment
3. Load dan proses DEM
4. Tambahkan tekstur dan lighting

### Tugas 4: Data Integration
**Objektif:** Mengintegrasikan berbagai data geospasial

**Prosedur:**
1. Load data tabular (CSV)
2. Convert ke format spasial
3. Visualisasikan pada peta
4. Analisis spatial

### Proyek Akhir
1. **Web GIS Application**: Sistem informasi geografis berbasis web
2. **3D City Model**: Model 3D kota dengan tekstur fotorealistik
3. **Interactive Dashboard**: Dashboard visualisasi data real-time

### Penilaian
- **Laporan Tugas (40%)**: Laporan dari 4 tugas praktikum
- **Proyek Akhir (35%)**: Presentasi dan dokumentasi proyek
- **Kemampuan Praktis (15%)**: Evaluasi keterampilan programming
- **Presentasi (10%)**: Presentasi proyek dan demo