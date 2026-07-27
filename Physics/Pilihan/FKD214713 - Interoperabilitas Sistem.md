---
title: "Interoperabilitas Sistem"
subject: "Fisika Pilihan"
tags:
  - interoperability
  - OGC-standards
  - APIs
  - data-exchange
  - SKS: 3
---

# FKD214713 — Interoperabilitas Sistem
**System Interoperability** | 3 SKS (Satuan Kredit Semester)

## Overview

System interoperability (interoperabilitas sistem) ensures that heterogeneous geospatial and geophysical systems can exchange, interpret, and use data seamlessly. This course covers OGC (Open Geospatial Consortium) web service standards — WMS, WFS, WCS, WMTS — RESTful API design, metadata catalogs, and data exchange formats. Students will learn to build interoperable systems that connect Indonesia's diverse government agencies, research institutions, and international partners, enabling the sharing of geospatial information across organizational and technical boundaries.

---

## 1. OGC Web Services (Layanan Web OGC)

### 1.1 Service Architecture Overview

The OGC Service Architecture follows a layered model:

```
[Client Application]
        ↓ (HTTP requests/responses)
[OGC Web Service Interface]
        ↓ (data access layer)
[Data Store (database, file system, API)]
```

### 1.2 Web Map Service (WMS — Layanan Peta Web)

WMS serves rendered map images (PNG, JPEG) from geospatial data:

**Key operations**:

| Operation | Description (Deskripsi) | Example Request |
|---|---|---|
| `GetCapabilities` | Service metadata | `?SERVICE=WMS&REQUEST=GetCapabilities` |
| `GetMap` | Map image (raster) | `?SERVICE=WMS&REQUEST=GetMap&LAYERS=...` |
| `GetFeatureInfo` | Query point attributes | `?SERVICE=WMS&REQUEST=GetFeatureInfo&QUERY_LAYERS=...` |
| `GetLegendGraphic` | Legend image | `?SERVICE=WMS&REQUEST=GetLegendGraphic` |

**GetMap request parameters**:

```
SERVICE=WMS
VERSION=1.3.0
REQUEST=GetMap
LAYERS=topografi,administrasi
CRS=EPSG:4326
BBOX=-6.4,106.6,-6.1,107.0
WIDTH=1024
HEIGHT=768
FORMAT=image/png
TRANSPARENT=TRUE
```

### 1.3 Web Feature Service (WFS — Layanan Fitur Web)

WMS serves rendered images; WFS serves vector features (geometry + attributes) in GML or GeoJSON:

**Key operations**:

| Operation | Description | Output |
|---|---|---|
| `GetCapabilities` | Feature types, operations | XML (service metadata) |
| `DescribeFeatureType` | Schema for a feature type | XML (XSD) |
| `GetFeature` | Actual feature data | GML 3.1.1 / GeoJSON |
| `Transaction` | Create/update/delete (WFS-T) | XML response |

**WFS GetFeature example**:

```
SERVICE=WFS
VERSION=2.0.0
REQUEST=GetFeature
TYPE_NAMES=geospasial:station_cors
OUTPUT_FORMAT=application/json
COUNT=10
CQL_FILTER=ST_DWithin(geom,GeometryFromText('POINT(106.8456 -6.2088)',4326),50000)
```

### 1.4 Web Coverage Service (WCS — Layanan Covarage Web)

WCS serves gridded (raster) data with full pixel values, unlike WMS which only serves rendered images:

| Operation | Purpose | Data |
|---|---|---|
| `GetCapabilities` | Available coverages | Metadata |
| `DescribeCoverage` | Coverage schema | Band info, CRS, resolution |
| `GetCoverage` | Raw raster data | GeoTIFF, NetCDF, ZARR |

WCS is essential for scientific applications requiring pixel-level access (elevation models, satellite imagery, climate model output).

### 1.5 Comparison Table

| Feature | WMS | WFS | WCS | WMTS |
|---|---|---|---|---|
| Output type | Image (PNG/JPEG) | Vector (GML/GeoJSON) | Raster (GeoTIFF) | Tile images |
| Data precision | Visual only | Full attributes | Full pixel values | Visual only |
| Performance | Good | Slow for large data | Moderate | Excellent (cached) |
| Use case (Penggunaan) | Visualization | Analysis, editing | Scientific analysis | Web basemaps |
| Transaction support | No | Yes (WFS-T) | No | No |

---

## 2. RESTful APIs for Geospatial Services

### 2.1 OGC API — Features

The modern replacement for WFS, using RESTful design and OpenAPI 3.0:

```yaml

# OpenAPI snippet for OGC API — Features
/openapi.yaml:
  paths:
    /collections/{collectionId}/items:
      get:
        summary: List features in a collection
        parameters:
          - name: collectionId
            in: path
            required: true
          - name: limit
            in: query
            schema:
              type: integer
              default: 10
          - name: bbox
            in: query
            schema:
              type: array
              items:
                type: number
        responses:
          '200':
            content:
              application/geo+json:
                schema:
                  $ref: '#/components/schemas/FeatureCollection'
```

### 2.2 API Design Best Practices

| Principle (Prinsip) | Description |
|---|---|
| Resource-oriented | URIs represent spatial resources |
| Stateless | Each request contains all information |
| HATEOAS | Responses include links to related resources |
| Versioning | API version in URL or header |
| Pagination | `limit`/`offset` or cursor-based |
| Content negotiation | Accept header for format selection |

### 2.3 GeoServer vs. MapServer vs. QGIS Server

| Feature | GeoServer | MapServer | QGIS Server |
|---|---|---|---|
| Standards support | Full OGC | Full OGC | Full OGC |
| Admin interface | Web GUI | Config files | QGIS projects |
| Raster support | Via GeoTIFF, NetCDF | Excellent | Good |
| Vector support | PostGIS, Shapefile, etc. | PostGIS, OGR | PostGIS |
| Performance | High (Java, GeoWebCache) | High (C) | Moderate |
| Community | Large, active | Mature | Growing |

---

## 3. Metadata Catalogs (Katalog Metadata)

### 3.1 Why Metadata Catalogs?

Without a metadata catalog (katalog metadata), finding geospatial data is like searching a library without a catalog system. The ISO 19115 standard ensures consistent documentation.

### 3.2 Catalog Service (CSW — Catalogue Service for the Web)

OGC CSW enables searching and retrieving metadata records:

**GetRecords search**:

```xml
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2"
    service="CSW" version="2.0.2" maxRecords="10">
  <csw:Query typeNames="csw:Record">
    <csw:Constraint version="1.1.0">
      <ogc:Filter>
        <ogc:PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">
          <ogc:PropertyName>csw:AnyText</ogc:PropertyName>
          <ogc:Literal>elevasi digital</ogc:Literal>
        </ogc:PropertyIsLike>
      </ogc:Filter>
    </csw:Constraint>
  </csw:Query>
</csw:GetRecords>
```

### 3.3 STAC (SpatioTemporal Asset Catalog)

STAC is a modern, lightweight alternative to CSW, using JSON and designed for cloud-native workflows:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "S2A_MSIL2A_20230101_JAKARTA",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "properties": {
    "datetime": "2023-01-01T02:30:00Z",
    "platform": "sentinel-2a",
    "cloud_cover": 5.2
  },
  "assets": {
    "B04": { "href": "https://storage.googleapis.com/.../B04.tif", "type": "image/tiff" }
  }
}
```

---

## 4. Data Exchange Formats (Format Pertukaran Data)

### 4.1 Format Comparison

| Format | Geometry | Attributes | Compression | Use Case |
|---|---|---|---|---|
| Shapefile (.shp) | Yes | Yes (dBASE) | No | Legacy exchange |
| GeoJSON | Yes (GeoJSON spec) | Yes | No (text) | Web APIs |
| GML | Yes (XML schema) | Yes | gzip | OGC standard |
| GeoPackage (.gpkg) | Yes (SF SQL) | Yes | SQLite | Mobile, portable |
| GeoTIFF | Gridded | Via metadata | LZW | Raster data |
| NetCDF-4 | Gridded (multi-dim) | Via attributes | HDF5 | Climate, ocean |
| ZARR | Gridded (cloud) | Via attributes | Blosc, gzip | Cloud-native chunks |

### 4.2 Coordinate Transformation in Exchange

When exchanging data between systems, coordinate reference system (CRS) mismatches are a common source of errors. Best practice:

1. Always include CRS metadata (EPSG code)
2. Store data in a canonical CRS (WGS 84 / EPSG:4326 or the national standard)
3. Transform on-the-fly for display using `cs2cs` (PROJ) or GDAL:

```bash

# Transform from DGN2000-48S to WGS84
cs2cs +proj=utm +zone=48 +south +ellps=WGS84 +to +proj=longlat +datum=WGS84 \
    input_coordinates.txt > output_coordinates.txt
```

---

## 5. Case Study: Multi-Agency Disaster Response System

During the 2018 Palu earthquake and tsunami ($M_w$ 7.5), multiple Indonesian agencies needed to share data rapidly:

| Agency | Data Type | System |
|---|---|---|
| BMKG | Seismic waveforms, tsunami alerts | GEOFON, custom |
| BNPB | Damage assessment, shelter locations | InaRISK |
| BIG | Maps, satellite imagery, GADM boundaries | INDE portal |
| LAPAN | Satellite imagery (Landsat, Sentinel) | BRIN-LAPAN portal |
| TNI AL | Naval hydrographic charts | Custom |

**Interoperability solution**: A GeoNode instance deployed by BIG served as the central hub:

- WMS layers from multiple agencies published via OGC standards

- Metadata catalog (CSW) enabled data discovery

- GeoJSON WFS feeds provided real-time damage boundaries

- API gateway aggregated feeds into a common operational picture

**Lesson learned** (Pelajaran yang didapat): Without pre-existing interoperability agreements, agencies default to email and WhatsApp for data sharing during crises. Pre-crisis OGC service deployment and standardized APIs are essential.

---

## References

1. OGC (2023). "OGC API — Features Part 1: Core." Open Geospatial Consortium.
2. OGC (2006). "Web Map Service Implementation Specification (WMS 1.3.0)." OGC 06-042.
3. OGC (2014). "Web Feature Service Standard (WFS 2.0)." OGC 09-025r1.
4. ISO 19115-1:2014. "Geographic information — Metadata — Part 1: Fundamentals."
5. Santoro, F. et al. (2020). "STAC: SpatioTemporal Asset Catalogs specification." Radiant Earth.
6. BIG & BNPB (2019). "Sistem Informasi Geospasial untuk Penanggulangan Bencana." Jakarta.
