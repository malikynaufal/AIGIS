---
tags: [aigis, geodesy, pilihan, spatial-data-structure, gis, topology]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Struktur Data Spasial (Spatial Data Structures)

**Kode:** TKD213611 | **SKS:** 3 (3-0) | **Semester:** 4–6

## Course Overview

Spatial Data Structures covers the representation, storage, and management of spatial data in both vector and raster formats. Focus on data models (GML, GeoJSON, Shapefile), spatial indexing, topology, and efficient querying for large spatial datasets.

## Key Topics

### 1. Vector Spatial Data Models

| Model | Type | Storage | Strengths | Weaknesses |
|-------|------|---------|-----------|------------|
| Shapefile | Legacy vector | `.shp .shx .dbf` | Simple, universal | 2 GB limit, no topology |
| GeoJSON | Text vector | `.geojson` | Web-friendly | Large file size |
| GML (ISO 19136) | XML vector | `.gml` | Full schema | Verbose, complex |
| GeoPackage | SQLite | `.gpkg` | Modern, OGC standard | Relatively new |

### 2. Spatial Indexing

**R-tree:** $O(\log N) $ search, $ O(N \log N) $ build

$ $

\text{MBB}(R_i) = (x_{\min}, y_{\min}, x_{\max}, y_{\max}) \quad \text{(Minimum Bounding Rectangle)}

$$

**Grid index:**

$ $ x_{cell} = \left\lfloor x / w_{cell} \right\rfloor, \quad y_{cell} = \left\lfloor y / h_{cell} \right\rfloor

$$

# ## 3. Topological Data Structures

| Topology | Description | GIS Example |
|----------|-------------|-------------|
| Adjacency | Shared edges between polygons | Parcel maps |
| Connectivity | Edge connections at nodes | Road networks |
| Containment | Polygon within polygon | Islands within seas |
| Order | Directional relationships | River networks |

**Planar enforcement:** All polygon boundaries are shared between features:

$ $

\bigcup A_i = \text{complete coverage}, \quad A_i \cap A_j = \emptyset \quad (i \neq j)

$$

# ## 4. Raster Data

| Property | Description | Typical Values |
|----------|-------------|----------------|
| Cell size | Ground resolution | 0.5 m — 1 km |
| Bands | Spectral channels | 3–15 (multispectral) |
| Depth | Bit depth | 8 bit (0–255), 16 bit, 32 bit float |
| Compression | Algorithm | LZW, DEFLATE, JPEG2000 |
| Pyramids | Multi-resolution | 2× resampling |

## Related Concepts

- [[Basis Data Spasial]] — Spatial databases
- [[Sistem Informasi Geografis Terapan]] — Applied GIS
- [[Pemrograman Spasial]] — Spatial programming
- [[GeographicLib]] — Geodesic algorithms

---

*Maintained by AIGIS — part of [[Geodesy MOC]]*
