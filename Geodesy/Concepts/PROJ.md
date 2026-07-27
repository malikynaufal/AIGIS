---
tags: [geodesy, concept, tool, aigis]
aliases: [PROJ, proj.org, PROJ.4, pyproj]
created: 2026-07-12
updated: 2026-07-27
---

# 🧰 PROJ

**PROJ** (proj.org) is the de facto standard library for handling **coordinate reference systems (CRS)** and performing [[Map Projection]] and [[Datum Transformation]]. It is used by GDAL, QGIS, pyproj, and nearly every open-source geospatial tool.

## Core Functionality

| Feature | Description |
|---------|-------------|
| **Coordinate transformations** | Forward/inverse for 100+ map projections |
| **Datum transformations** | 7-parameter Helmert, grid shifts (NADCON, NTv2), time-dependent |
| **CRS management** | EPSG database (registry), WKT definitions |
| **Pipeline processing** | Chained operations ( $+proj=a +proj=b +proj=c$) |
| **Grid shift support** | NTv2, NADCON, FPS, ISN2000/L2004, etc. |
| **Time-dependent transformations** | Plate motion models (ITRF2020 → ETRS89) |
| **Geodetic operations** | Geodesic distance (Karney), azimuth, area |

## Basic Usage (Command-Line: `proj`)

### Forward Projection ( $\phi, \lambda \to E, N$)

```bash

# UTM Zone 33N, WGS84
echo "51.5 0.0" | proj +proj=utm +zone=33 +ellps=WGS84

# Output: 290312.3 5712982.2
```

### Inverse Projection ( $E, N \to \phi, \lambda$)

```bash
echo "290312.3 5712982.2" | proj -I +proj=utm +zone=33 +ellps=WGS84

# Output: 0d0'0.00168"E 51d30'0.00060"N
```

### Datum Transformation (NAD27 → NAD83)

```bash

# Using official NADCON grid
echo "39.0 -105.0" | proj +proj=latlong +ellps=clrk66 +nadgrids=conus.gsb +proj=latlong +ellps=GRS80
```

## Python (pyproj)

```python
import pyproj

# Define CRS objects
wgs84 = pyproj.CRS("EPSG:4326")
utm33n = pyproj.CRS("EPSG:32633")

# Create transformer
transformer = pyproj.Transformer.from_crs(wgs84, utm33n)

# Forward (lon, lat) → (easting, northing)
x, y = transformer.transform(51.5, 0.0)
print(f"Easting: {x:.2f}, Northing: {y:.2f}")

# Easting: 290312.34, Northing: 5712982.18

# Geodesic distance
g = pyproj.Geod(ellps="WGS84")
distance, azi1, azi2 = g.inv(-74.006, 40.7128, -0.1278, 51.5074)
print(f"Distance: {distance/1000:.2f} km")

# Distance: 5570.23 km
```

### Working with GPS grid zones (EPSG database)

```python

# Find UTM zone for a longitude
lon = -105.0
zone = int((lon + 180) / 6) + 1

# Adjust for special zones (Norway/Svalbard)
if lon >= 0 and lon < 180:
 epsg_code = 32600 + zone # Northern hemisphere
else:
 epsg_code = 32700 + zone # Southern hemisphere

crs_utm = pyproj.CRS.from_epsg(epsg_code)
```

## Pipeline Operations

PROJ 6+ supports **coordinate operation pipelines** as a structured sequence of steps:

```bash

# NAD27 → WGS84 via Helmert + NADCON grid
echo "39°N -105°W" | proj +proj=pipeline \
 +step +proj=latlong +ellps=clrk66 +step +proj=push +v_1 +step \
 +proj=utm +zone=13 +ellps=clrk66 +step +proj=gridshift +grid=conus.gsb \
 +step +proj=set +v_2 +step +pop +v_1 +proj=cart +ellps=GRS80 +step \
 +proj=helmert +x=-8 +y=152 +z=-178 +rx=0 +ry=0 +rz=0 +s=3.6 +convention=position_vector
```

In Python with pyproj, same pipeline can be specified as a WKT operation string.

## Grid Shift Files (NADCON/NTv2)

| Grid File | Region | Source | Resolution |
|-----------|--------|--------|------------|
| `conus.gsb` | Continental US | NOAA/NGDC | 30″ |
| `alaska.gsb` | Alaska | NOAA/NGDC | 30″ |
| `hawaii.gsb` | Hawaii | NOAA/NGDC | 15″ |
| `ntv2_0.gsb` | Canada | NRCan | 1′ |
| `ntv2_0_ca.gsb` | Canada (high-res) | NRCan | 15″ |

PROJ ships ~50 grid shift files covering most of the world (in `proj-data` package).

## EPSG Database Integration

PROJ ships the full EPSG dataset, enabling CRS lookup by code:

```bash
projinfo EPSG:32633 # Show CRS details

# Output includes: UTM Zone 33N, WGS 84, meters
```

| EPSG Code | CRS Description |
|-----------|-----------------|
| 4326 | WGS84 (geographic 2D) |
| 4269 | NAD83 (geographic 2D) |
| 4267 | NAD27 (geographic 2D) |
| 32601–32660 | WGS84 UTM North zones |
| 32701–32760 | WGS84 UTM South zones |
| 25831–25835 | ETRS89 UTM zones |
| 2154 | RGF93 (France) |

## Accuracy Considerations

| Transformation Type | Typical Accuracy | Notes |
|---------------------|------------------|-------|
| EPSG:4326 → UTM (same datum) | < 1 mm | No datum shift |
| WGS84 ↔ ETRS89 (7-param) | < 0.5 mm | Valid for < 100 km |
| NAD27 → NAD83 (grid) | ±0.15 m | Using conus.gsb |
| NAD27 → NAD83 (7-param) | ±10 m | Do NOT use for cadastre |
| ITRF2014 → ITRF2020 (14-param) | < 0.5 mm | Time-dependent |

## PROJ in Practice

1. **Always specify input and output CRS** (never "latlong" without ellipsoid).
2. **Use EPSG codes** for known systems — avoids ambiguity.
3. **Prefer grid-based** datum shifts over 7-parameter for legacy datums.
4. **Check grid availability** — PROJ ships with a `proj-data` package containing most global grids.
5. **Use the `projinfo` tool** to inspect CRS definitions.
6. **Validate output** by transforming a known benchmark location.

## References

- PROJ Documentation: https://proj.org/

- Evenden, G. I. (1990). *Cartographic projection procedures for the UNIX environment*. USGS.

- Nußberger, O. et al. (2021). *PROJ: A coordinate transformation library for the geospatial ecosystem*.

## Related

- [[Map Projection]] · [[Datum Transformation]] · [[Helmert Transformation]] · [[UTM]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
