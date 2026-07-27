---
tags: [geodesy, concept, gis, aigis]
aliases: [SIG, Sistem Informasi Geografis, GIS, Geographic Information System]
created: 2026-07-12
updated: 2026-07-27
---

# 🗺️ SIG (Sistem Informasi Geografis / GIS)

**SIG** (Sistem Informasi Geografis — Geographic Information System) is the discipline and technology for capturing, storing, analyzing, managing, and visualizing spatial (geographic) data. In geodesy, SIG provides the critical context for turning raw coordinate data into meaningful maps, cadastral records, and spatial analysis.

## Core Components of a GIS

| Component | Description | Geodesy Connection |
|-----------|-------------|-------------------|
| **Hardware** | Workstations, servers, GPS receivers, CORS | Collect the coordinates |
| **Software** | QGIS, ArcGIS, GRASS SAGA — use PROJ for reprojection | Datum and CRS transform |
| **Data** | Vector (points/lines/polygons), raster (grids, imagery) | Geo-referenced, in CRS |
| **Methods** | Spatial queries, topology, overlay, buffering, interpolation | Geodetic computation |
| **People** | Surveyors, cartographers, analysts, mappers | Apply geodesy in practice |

## Data Models

### Vector Model

| Geometry | Example | Geodesy Use |
|----------|---------|-------------|
| **Point** | CORS station, benchmark | GNSS coordinates |
| **Line** | Road centerline, leveling traverse | [[Geodetic Coordinates]] → projected |
| **Polygon** | Cadastral parcel, administrative boundary | Area computation |

### Raster Model

| Raster Type | Example | Geodesy Use |
|-------------|---------|-------------|
| DEM (Digital Elevation Model) | SRTM, ASTER GDEM | Orthometric height, slope |
| Satellite imagery | Landsat, Sentinel | Imagery geo-referencing |
| Grid models | EGM2008 geoid grid | $\Delta N$ lookup |

## Coordinate Reference System (CRS) in SIG

Every SIG project must work in a consistent CRS:

### CRS Stack (in SIG)

```
1. Geometric CRS (Geodetic): φ, λ
 └── Datum: WGS84, NAD83, ETRS89
 └── Ellipsoid: GRS80, Clarke 1866

2. Projected CRS: E, N (meters)
 └── Projection: UTM, TM, Lambert, etc.
 └── Zone: Zone 48S (Jakarta)
 └── False origin: E₀ = 500,000, N₀ = 10,000,000
```

### CRS Assignment in Practice

| GIS Software | CRS Specification |
|--------------|-------------------|
| QGIS | EPSG code (e.g., 32648), WKT string |
| ArcGIS | WKID, factory code |
| PROJ | `+proj=utm +zone=48 +south` |
| GDAL/OGR | `-t_srs EPSG:32648` |

## Cadastral Applications (SIG + Datum + Projection)

| Cadastral Task | SIG/Geodesy Workflow |
|----------------|---------------------|
| **Land parcel mapping** | Survey → GNSS → SIG → Cadastral layer |
| **Property boundaries** | Polygons in ETRS89/UTM → SIG topology |
| **Title deed registration** | Coordinates in official CRS + datum |
| **Zoning and land use** | Overlay planning polygons |
| **Infrastructure planning** | Buffer, intersect roads/buildings |

### Indonesia SIG/Cadastral Context

In Indonesia:

- **Cadastral coordinates** use **DGN95** (WGS84-based) or ETRS89

- **Projection:** TM3° (3° Transverse Mercator) per province/region

- **BIG (Badan Informasi Geospasial)** defines the official national CRS

- **SIG software** must support Indonesia's TM3° CRS codes (e.g., EPSG:23833-23842 for northern hemisphere)

## SIG + Geodesy Integration

### Data Collection → SIG

```
Field survey (total station, RTK GNSS)
 → WGS84/Ellipsoidal heights (h)
 → SIG imports coordinates
 → Apply datum transformation (NAD27 → WGS84 via NADCON)
 → Reproject to local CRS (UTM/TM3°)
 → Store in SIG as layer
```

### SIG + Geoid Model Integration

In SIG, a geoid model (GEGrid, EGM2008) can be overlaid to convert ellipsoidal heights to orthometric heights:

```
1. Load GNSS layer with (h = ellipsoidal heights)
2. Load geoid raster (e.g., GEOID18 or EGM2008)
3. SIG "extract raster values" at point locations → N values
4. Compute H = h - N (field calculation or GIS calculator)
5. Store orthometric heights (H) as new attribute
```

## Common SIG Geodesy Operations

| Operation | SIG Tool / Workflow |
|-----------|---------------------|
| Geodetic → Projected reprojection | `qgis transform`, GDAL `ogr2ogr -s_srs -t_srs` |
| Buffer polygons | GIS buffer function |
| Intersect (overlay) | GIS `intersect_analysis` |
| Measure distance between two points | GIS measure (geodesic-aware) |
| Area computation | GIS "Calculate Geometry" → geodesic area |
| Coordinate validation | GPS field check against SIG coordinates |

## GIS Software and PROJ/CrsLib

All modern GIS software uses PROJ internally for CRS transformations:

| GIS Software | PROJ Integration |
|--------------|------------------|
| QGIS | Uses PROJ via GDAL (Qt GUI + CLI) |
| ArcGIS Pro (ESRI) | Uses Esri's internal CRS engine (PROJ-compatible) |
| PostGIS (PostgreSQL) | Uses PROJ for `ST_Transform` |
| GDAL/OGR | Uses PROJ as core CRS engine |
| GRASS GIS | Uses PROJ for coordinate access |
| Google Maps API | Web Mercator (spherical, EPSG:3857) |
| Mapbox/Leaflet | Web Mercator by default |

## Key GIS Considerations for Geodesy

1. **Always set the project CRS** before loading data.
2. **Always use the correct datum** — WGS84 (GPS) is not the same as local datums.
3. **Grid shift files** should be in the PROJ search path for legacy datum transformations.
4. **Vertical CRS** (orthometric heights) is a separate CRS from horizontal — SIG handling of heights varies widely.
5. **Coordinate precision** — SIG databases should store coordinates to sufficient decimal places (6 decimals ≈ 0.1 m).
6. **Topology rules** — Cadastral SIG uses topology (no gaps, no overlaps between parcels).

## References

- Longley, P. A. et al. (2015). *Geographic Information Systems & Science*. Wiley.

- QGIS Documentation: docs.qgis.org

- NGA Geospatial Information Repository: https://earth-info.nga.mil

- BIG (Indonesia): www.big.go.id

## Related

- [[Map Projection]] · [[PROJ]] · [[Datum Transformation]] · [[Geodetic Coordinates]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Kurikulum Teknik Geodesi]]
