---
tags: [aigis, geodesy, pilihan, web-gis, geoserver, leaflet]
aliases: [Web GIS, SIG Web]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Sistem Informasi Geografis Berbasis Web (Web GIS)

**Kode:** TKD214716 | **SKS:** 3 (2-1) | **Semester:** 6–8

## Course Overview

Development of web-based GIS applications using open-source libraries: GeoServer, Leaflet, OpenLayers, PostGIS backend, and REST APIs. Covers map tiling, WMS/WFS services, and interactive spatial data visualization.

## Key Topics

### 1. Web GIS Architecture

| Layer | Technology | Role |
|-------|-----------|------|
| Database | PostgreSQL/PostGIS | Spatial data |
| Server | GeoServer, MapServer | OGC services |
| Client | Leaflet, OpenLayers | UI/map display |
| API | REST, WMS, WFS, WCS | Data exchange |

### 2. Leaflet Example
```javascript
var map = L.map('map').setView([-7.8, 110.4], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
 maxZoom: 19
}).addTo(map);
var marker = L.marker([-7.8, 110.4]).addTo(map);
marker.bindPopup('<b>UGM Geodesy</b>').openPopup();
```

### 3. GeoServer Configuration
- Store: PostGIS connection
- Layer: SQL-based views
- Style: SLD (Styled Layer Descriptor)

---
*Maintained by AIGIS — part of [[Geodesy MOC]]*
