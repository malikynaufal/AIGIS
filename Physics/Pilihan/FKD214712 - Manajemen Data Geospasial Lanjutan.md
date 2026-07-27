---
title: "Manajemen Data Geospasial Lanjutan"
subject: "Fisika Pilihan"
tags:
 - geospatial-data
 - GIS
 - spatial-database
 - cloud-GIS
 - SKS: 3
---

# FKD214712 — Manajemen Data Geospasial Lanjutan
**Advanced Geospatial Data Management** | 3 SKS (Satuan Kredit Semester)

## Overview

Advanced geospatial data management (manajemen data geospasial lanjutan) addresses the storage, processing, and dissemination of massive spatial datasets — from terabyte-scale remote sensing archives to real-time GNSS streaming networks. This course covers spatial database design, cloud-based GIS platforms, OGC standards implementation, and scalable data pipelines. Students will work with PostgreSQL/PostGIS, cloud platforms (Google Earth Engine, AWS), and modern data engineering tools to build geospatial information systems suitable for Indonesia's national spatial data infrastructure (INDE — Indonesia National Spatial Data Infrastructure).

---

## 1. Spatial Databases (Basis Data Spasial)

### 1.1 Relational Model for Spatial Data

PostgreSQL with the PostGIS extension adds spatial types and operators:

```sql
-- Create a spatial table for GNSS stations
CREATE TABLE cors_stations (
 station_id VARCHAR(10) PRIMARY KEY,
 name TEXT NOT NULL,
 installation_date DATE,
 geom GEOMETRY(Point, 4326) -- WGS84
);

-- Create spatial index (R-tree based)
CREATE INDEX idx_stations_geom
ON cors_stations USING GIST(geom);

-- Find stations within 50 km of Jakarta city center
SELECT station_id, name, ST_Distance(
 geom::geography,
 ST_SetSRID(ST_MakePoint(106.8456, -6.2088), 4326)::geography
) / 1000 AS distance_km
FROM cors_stations
WHERE ST_DWithin(
 geom::geography,
 ST_SetSRID(ST_MakePoint(106.8456, -6.2088), 4326)::geography,
 50000
)
ORDER BY distance_km;
```

### 1.2 Spatial Indexing

| Index Type | Structure | Best For | Query Complexity |
|---|---|---|---|
| R-tree | Hierarchical rectangles | Range queries | $O(\log n) $ |
| Quad-tree | Recursive 4-way split | Point data | $ O(\log n) $ |
| kd-tree | k-dimensional binary tree | Nearest neighbor | $ O(\log n) $ average |
| Grid index | Regular grid cells | Simple overlap | $ O(1) $ lookup |
| Space-filling curve | Hilbert/Z-order | Linearization | $ O(\log n)$ |

PostGIS uses the GiST (Generalized Search Tree) framework, which supports R-tree, kNN, and other index types.

### 1.3 Coordinate Reference Systems (Sistem Referensi Koordinat)

| CRS Code | Name | Area | Use Case |
|---|---|---|---|
| EPSG:4326 | WGS 84 | Global | GPS, international |
| EPSG:32748 | UTM Zone 48S | Java, Bali | National mapping |
| EPSG:32749 | UTM Zone 49S | Eastern Java | Regional survey |
| EPSG:4326 | DGN 2000-3 | Indonesia (3° grid) | BIG standard |
| EPSG:23848 | DGN 2000-48 | UTM 48S (meters) | Engineering |

---

## 2. Cloud GIS (GIS Awan)

### 2.1 Google Earth Engine (GEE)

GEE provides petabytes of satellite imagery with cloud-based processing:

```javascript
// Cloud-free composite over Jakarta (Landsat 8/9)
var jakarta = ee.Geometry.Rectangle([106.6, -6.4, 107.0, -6.1]);

var composite = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
 .filterBounds(jakarta)
 .filterDate('2023-01-01', '2023-12-31')
 .filter(ee.Filter.lt('CLOUD_COVER', 10))
 .map(function(img) {
 var scaled = img.multiply(0.0000275).add(-0.2);
 return scaled.normalizedDifference(['SR_B5', 'SR_B4'])
 .rename('NDVI');
 })
 .median()
 .clip(jakarta);

Map.addLayer(composite, {min: -0.1, max: 0.8, palette: ['red','yellow','green']}, 'NDVI');
```

### 2.2 Cloud Platform Comparison

| Feature | GEE | AWS (S3+Lambda) | Microsoft Planetary Computer |
|---|---|---|---|
| Imagery archive | Landsat, Sentinel, MODIS | Custom upload | Landsat, Sentinel, CB |
| Compute model | Server-side JavaScript | Serverless functions | Jupyter + Dask |
| Free tier | Yes (academic) | Pay-per-use | Yes (STAC catalog) |
| Vector processing | Limited | Full (via GDAL) | Full (GeoPandas) |
| Indonesia coverage | Excellent | Depends on data | Good (STAC) |

---

## 3. OGC Standards for Data Management

### 3.1 Key Standards

| Standard | Purpose | Data Model |
|---|---|---|
| Simple Feature (SF) | Geometry types | Point, Line, Polygon, GeometryCollection |
| GML (Geography Markup Language) | Spatial data exchange | XML-based geometry + attributes |
| GeoJSON | Web-friendly spatial data | JSON geometry + properties |
| GeoPackage (GPKG) | SQLite-based spatial container | Tiles + features in one file |
| CityGML | 3D urban models | LOD 0–4 city objects |
| SensorML | Sensor metadata | Process description |

### 3.2 GeoPackage vs. Shapefile

| Criterion | GeoPackage | Shapefile |
|---|---|---|
| File limit | Single file | 3+ files (.shp, .dbf, .shx) |
| Geometry types | All types | Limited (no curves) |
| Attribute types | Full SQL types | 254 char text, numeric only |
| Max record size | Unlimited | 2 GB |
| Spatial index | R-tree (internal) | None built-in |
| CRS support | Embedded | Separate .prj file |
| Standard | OGC (2014) | ESRI (1990s) |

### 3.3 Metadata Standards

**ISO 19115** (Geographic Information — Metadata) defines mandatory and optional elements:

| Element Group | Key Fields | Purpose |
|---|---|---|
| Identification | Title, abstract, keywords | What is this dataset? |
| Quality | Lineage, accuracy, completeness | How good is it? |
| Spatial | CRS, bounding box, resolution | Where and at what scale? |
| Distribution | Format, access URL, fees | How to obtain it? |
| Temporal | Reference date, temporal extent | When? |

---

## 4. Data Pipelines (Saluran Pipa Data)

### 4.1 Architecture for Real-Time GNSS Processing

```
[GNSS Receivers] → [MQTT Broker] → [Stream Processor] → [PostGIS] → [API Layer] → [Clients]
 ↑ ↑
 (NTRIP Caster) (Apache Kafka / Flink)
```

**Components**:

1. **Ingestion**: RTKLIB or BNC (BKG NTRIP Client) streams RTCM data from CORS receivers
2. **Processing**: Real-time PPP or network RTK computation
3. **Storage**: TimescaleDB (PostgreSQL extension for time-series) with spatial indexing
4. **API**: GeoServer or pg_tileserv for OGC-compliant service delivery

### 4.2 ETL for Remote Sensing Data

Extract-Transform-Load pipeline for Sentinel-2 imagery:

```python

# Simplified ETL pipeline
import rasterio
from rasterio.mask import mask
from shapely.geometry import box

def process_sentinel2(scene_path, aoi_bbox):
 """Cloud-mask, clip, and reproject Sentinel-2 scene."""
 with rasterio.open(scene_path) as src:
 # Step 1: Cloud masking using SCL band
 scl = src.read(12) # Scene Classification Layer
 cloud_mask = ~((scl == 8) | (scl == 9) | (scl == 10))

 # Step 2: Clip to AOI
 aoi = box(*aoi_bbox)
 out_image, out_transform = mask(src, [aoi], crop=True)

 # Step 3: Apply cloud mask
 out_image[:, ~cloud_mask] = 0

 return out_image, out_transform
```

### 4.3 Data Volume Estimates for Indonesia

| Dataset | Spatial Resolution | Temporal Cadence | Annual Volume |
|---|---|---|---|
| Sentinel-2 imagery | 10 m | 5 days | ~2 TB |
| GNSS daily solutions | Station-level | Daily | ~500 MB |
| LiDAR (national DEM) | 0.5 m | One-time | ~500 TB |
| Seismic waveform | 200 sps | Continuous | ~500 GB |
| INSPIRE-compliant vector | 1:5000 | Annual update | ~10 GB |

---

## 5. Case Study: INDE (Indonesia National Spatial Data Infrastructure)

INDE (Infrastuktur Data Spasial Indonesia) under BIG aims to unify Indonesia's geospatial data:

- **Portal**: inde.big.go.id — metadata catalog with >250,000 datasets

- **Standards**: INSPIRE-aligned, OGC-compliant services

- **Data themes**: Administrative boundaries, land use, transportation, hydrography, elevation

- **Challenge**: Data from 34 provinces in varying formats (Shapefile, GeoTIFF, CAD drawings, paper maps)

- **Solution**: PostgreSQL/PostGIS backend with automated ETL using FME (Feature Manipulation Engine), serving data via WMS/WFS/WMTS

The system processes >100,000 spatial queries per day from government agencies, researchers, and the public.

---

## References

1. Obe, R. O., & Hsu, L. S. (2015). *PostGIS in Action*, 2nd ed. Manning Publications.
2. Longley, P. A., Goodchild, M. F., Maguire, D. J., & Rhind, D. W. (2015). *Geographic Information Science and Systems*, 4th ed. Wiley.
3. Gorelick, N. et al. (2017). "Google Earth Engine: Planetary-scale geospatial analysis for everyone," *Remote Sens. Environ.*, 202, 18–27.
4. ISO 19115-1:2014. "Geographic information — Metadata — Part 1: Fundamentals."
5. OGC (2022). "OGC API — Features Standard." Open Geospatial Consortium.
6. BIG (2023). "Pedoman Teknis INDE." Badan Informasi Geospasial, Jakarta.
