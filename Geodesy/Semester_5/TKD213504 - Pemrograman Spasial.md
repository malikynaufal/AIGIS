# Pemrograman Spasial (*Spatial Programming*)

**Kode:** TKD213504
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Pengolahan Data Geospasial, Algoritma dan Struktur Data

---

## 1. Overview

Spatial programming (*pemrograman spasial*) is the practice of writing code to process, analyze, and visualize geospatial data. It combines computational thinking with geographic concepts, using libraries such as **GDAL/OGR**, **Shapely**, **GeoPandas**, and the **QGIS Python API (PyQGIS)**.

### 1.1 Python Geospatial Ecosystem

| Library | Function |
|---------|----------|
| **GDAL/OGR** | Raster/vector I/O, reprojection |
| **Shapely** | Geometric operations (buffer, intersection) |
| **GeoPandas** | DataFrame with spatial capabilities |
| **PyProj** | Map projections and coordinate transformations |
| **Folium** | Interactive web maps |
| **Rasterio** | Raster data handling |
| **PyQGIS** | QGIS automation and plugin development |

---

## 2. GDAL (Geospatial Data Abstraction Library)

### 2.1 Overview

GDAL is the de facto standard for geospatial data I/O. It supports over 200 formats including GeoTIFF, Shapefile, KML, GPKG, NetCDF, and more.

### 2.2 Python Bindings

```python
from osgeo import gdal, ogr, osr

# Open raster
ds = gdal.Open('dem.tif')
band = ds.GetRasterBand(1)
arr = band.ReadAsArray()

# Get projection
proj_wkt = ds.GetProjection()
print(proj_wkt)

# Get geotransform (origin + pixel size)
gt = ds.GetGeoTransform()

# gt = (top_left_x, pixel_width, rotation_x,

#       top_left_y, rotation_y, pixel_height)
```

### 2.3 Coordinate Reference System (CRS)

```python
from osgeo import osr

# Define source and target CRS
srs_src = osr.SpatialReference()
srs_src.ImportFromEPSG(4326)  # WGS84

srs_dst = osr.SpatialReference()
srs_dst.ImportFromEPSG(32648)  # UTM Zone 48S

# Create coordinate transformation
coord_trans = osr.CoordinateTransformation(srs_src, srs_dst)
point = coord_trans.TransformPoint(lon, lat)
```

### 2.4 Reprojection

```python

# Warp (reproject) raster
ds_warped = gdal.Warp(
    'output.tif',
    'input.tif',
    dstSRS='EPSG:32648',
    resampleAlg=gdal.GRA_Bilinear
)
```

### 2.5 Vector I/O with OGR

```python
from osgeo import ogr

# Open vector
driver = ogr.GetDriverByName('ESRI Shapefile')
ds = driver.Open('boundary.shp', 0)  # 0 = read-only
layer = ds.GetLayer()

# Iterate features
for feature in layer:
    geom = feature.GetGeometryRef()
    fid = feature.GetFID()
    attrs = {field: feature.GetField(field)
             for field in ['id', 'name', 'area']}
    print(f"Feature {fid}: {attrs}")

# Create new feature
new_feature = ogr.Feature(layer.GetLayerDefn())
new_feature.SetGeometry(geom)
new_feature.SetField('name', 'New Parcel')
layer.CreateFeature(new_feature)
```

---

## 3. Shapely — Geometric Operations

### 3.1 Geometry Types

```python
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import unary_union

# Point
p = Point(1.0, 2.0)

# LineString
line = LineString([(0, 0), (1, 1), (2, 0)])

# Polygon (with hole)
ext = [(0, 0), (0, 10), (10, 10), (10, 0)]
hole = [(2, 2), (2, 4), (4, 4), (4, 2)]
poly = Polygon(ext, [hole])
```

### 3.2 Spatial Predicates

| Predicate | Description |
|-----------|-------------|
| `a.intersects(b)` | a and b share space |
| `a.touches(b)` | a and b share boundary only |
| `a.crosses(b)` | a crosses through b |
| `a.within(b)` | a is inside b |
| `a.contains(b)` | b is inside a |
| `a.overlaps(b)` | a and b partially overlap |
| `a.equals(b)` | a and b are identical |

### 3.3 Spatial Operations

```python

# Buffer
buffered = poly.buffer(100)  # 100m buffer

# Intersection
intersection = poly1.intersection(poly2)

# Union
union = poly1.union(poly2)

# Difference
diff = poly1.difference(poly2)

# Symmetric difference
sym_diff = poly1.symmetric_difference(poly2)

# Centroid
centroid = poly.centroid

# Area
area = poly.area

# Length
length = line.length
```

### 3.4 Spatial Index (STRtree)

```python
from shapely.strtree import STRtree

# Build spatial index
geoms = [poly1, poly2, poly3, ...]
tree = STRtree(geoms)

# Query
query_result = tree.query(search_geom)

# Returns indices of geometries intersecting search_geom
```

---

## 4. GeoPandas — Spatial DataFrames

### 4.1 Basic Operations

```python
import geopandas as gpd

# Read vector data
gdf = gpd.read_file('parcels.shp')

# Inspect
print(gdf.crs)
print(gdf.columns.tolist())
print(gdf.geometry.type.value_counts())

# Filter
urban_parcels = gdf[gdf['land_use'] == 'residential']

# Spatial join (overlay)
points_gdf = gpd.read_file('points.shp')
joined = gpd.sjoin(points_gdf, gdf, how='inner', predicate='within')

# Dissolve (group and merge)
dissolved = gdf.dissolve(by='district', aggfunc='sum')
```

### 4.2 Geometric Operations

```python

# Buffer all geometries
gdf['buffer'] = gdf.buffer(100)

# Calculate area (in CRS units)
gdf['area_m2'] = gdf.area

# Centroid
gdf['centroid'] = gdf.geometry.centroid

# Simplify (reduce vertices)
gdf['simplified'] = gdf.simplify(tolerance=10)

# Convex hull
gdf['hull'] = gdf.geometry.convex_hull

# Minimum bounding box
gdf['bbox'] = gdf.geometry.minimum_rotated_rectangle
```

### 4.3 Coordinate Reference System

```python

# Check CRS
print(gdf.crs)

# Set CRS (if missing)
gdf.crs = 'EPSG:4326'

# Reproject
gdf_utm = gdf.to_crs('EPSG:32648')

# Calculate area in square meters
gdf_utm['area_m2'] = gdf_utm.area
```

### 4.4 Spatial Analysis

```python

# Buffer + spatial join
buffers = gdf.buffer(500)
buffer_gdf = gpd.GeoDataFrame(geometry=buffers, crs=gdf.crs)
intersections = gpd.sjoin(buffer_gdf, points_gdf, how='inner')

# Voronoi diagram
from geopandas import gpd
voronoi = gpd.GeoSeries(gdf.geometry.voronoi_polygons())

# Clip
clipped = gdf.clip(mask_polygon)
```

---

## 5. PyQGIS — QGIS Python API

### 5.1 Loading Layers

```python
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsRasterLayer,
    QgsVectorFileWriter, QgsField, QgsFields
)

# Load vector layer
layer = QgsVectorLayer('parcels.shp', 'Parcels', 'ogr')
QgsProject.instance().addMapLayer(layer)

# Load raster layer
raster = QgsRasterLayer('dem.tif', 'DEM', 'gdal')
QgsProject.instance().addMapLayer(raster)

# Access layer by name
layers = QgsProject.instance().mapLayersByName('Parcels')
```

### 5.2 Feature Iteration and Modification

```python

# Iterate features
layer.startEditing()
for feature in layer.getFeatures():
    geom = feature.geometry()
    area = geom.area()
    # Update field
    layer.changeAttributeValue(feature.id(), 2, area)  # field 2 = area
layer.commitChanges()

# Add new feature
fields = layer.fields()
new_feature = QgsFeature()
new_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(0, 0)))
new_feature.setAttributes(['New ID', 'New Name'])
layer.addFeature(new_feature)
```

### 5.3 Processing Algorithms

```python
from qgis.core import QgsProcessingFeedback
import processing

# Buffer
result = processing.run("native:buffer", {
    'INPUT': layer,
    'DISTANCE': 100,
    'SEGMENTS': 5,
    'OUTPUT': 'memory:'
})

# Clip
result = processing.run("native:clip", {
    'INPUT': layer,
    'OVERLAY': mask_layer,
    'OUTPUT': 'memory:'
})
```

---

## 6. GPS Data Processing Scripts

### 6.1 Reading NMEA Data

```python
import serial
import pynmea2

def read_gps(port='/dev/ttyUSB0', baud=9600):
    ser = serial.Serial(port, baudrate=baud, timeout=1)
    while True:
        line = ser.readline().decode('ascii', errors='replace')
        if line.startswith('$GPGGA'):
            msg = pynmea2.parse(line)
            print(f"Lat: {msg.latitude}, Lon: {msg.longitude}")
            print(f"Time: {msg.timestamp}, Alt: {msg.altitude}")
```

### 6.2 RINEX Data Processing

```python

# Using RTKLIB (str2short) via subprocess
import subprocess

# Convert RINEX to observation
cmd = ['rnx2rtk', '-o', 'solution.txt',
       'base.obs', 'rover.obs', 'base.nav']
subprocess.run(cmd)

# Parse solution
import pandas as pd
sol = pd.read_csv('solution.txt', comment='%',
                  sep='\s+', header=None,
                  names=['date', 'time', 'lat', 'lon', 'height'])
```

### 6.3 GNSS Quality Analysis

```python
import numpy as np

def pdop(sat_positions, receiver_pos):
    """Calculate Position Dilution of Precision."""
    n = len(sat_positions)
    H = np.zeros((n, 4))
    for i, sat in enumerate(sat_positions):
        dx = sat[0] - receiver_pos[0]
        dy = sat[1] - receiver_pos[1]
        dz = sat[2] - receiver_pos[2]
        dist = np.sqrt(dx**2 + dy**2 + dz**2)
        H[i] = [-dx/dist, -dy/dist, -dz/dist, 1]
    Q = np.linalg.inv(H.T @ H)
    pdop = np.sqrt(np.trace(Q[:3, :3]))
    return pdop
```

---

## 7. Web Mapping Integration

### 7.1 Folium

```python
import folium

# Create map
m = folium.Map(location=[-7.7975, 110.3695], zoom_start=12)

# Add GeoJSON
folium.GeoJson('parcels.geojson',
               name='Parcels',
               style_function=lambda x: {
                   'fillColor': 'green',
                   'color': 'black',
                   'weight': 1,
                   'fillOpacity': 0.4
               }).add_to(m)

# Add markers
for idx, row in gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=row['name']
    ).add_to(m)

m.save('map.html')
```

### 7.2 GeoPandas to GeoJSON

```python

# Export to GeoJSON for web use
gdf.to_file('parcels.geojson', driver='GeoJSON')

# Simplify for web (reduce file size)
gdf_simplified = gdf.simplify(tolerance=10)
gdf_simplified.to_file('parcels_web.geojson', driver='GeoJSON')
```

---

## 8. Performance Optimization

### 8.1 Spatial Index

```python

# Use spatial index for large datasets
sindex = gdf.sindex
possible_matches_index = list(sindex.intersection(search_geom.bounds))
possible_matches = gdf.iloc[possible_matches_index]
precise_matches = possible_matches[possible_matches.intersects(search_geom)]
```

### 8.2 Dask for Large Data

```python
import dask_geopandas

# Parallel processing of large GeoDataFrames
dask_gdf = dask_geopandas.from_geopandas(gdf, npartitions=4)
result = dask_gdf.sjoin(other_gdf).compute()
```

### 8.3 Memory Management

```python

# Process in chunks
for i in range(0, len(gdf), 1000):
    chunk = gdf.iloc[i:i+1000]
    result = process_chunk(chunk)
    # Save result
```

---

## 9. Indonesian Geospatial Data Sources

| Source | URL | Format |
|--------|-----|--------|
| **BIG** (Geospasial) | https://www.big.go.id | Shapefile, GeoPackage |
| **DEWI** (Water Resources) | https://dewi.dephub.go.id | GeoJSON, Shapefile |
| **KLHK** (Forestry) | https://dbhl.klhk.go.id | GeoJSON |
| **BPS** (Statistics) | https://sig.bps.go.id | GeoJSON, CSV |
| **OpenStreetMap** | https://www.openstreetmap.org | PBF, Shapefile |

---

## 10. Best Practices

1. **Always check CRS** before spatial operations
2. **Use appropriate data types** (GeoPackage > Shapefile)
3. **Validate geometries** before analysis
4. **Use spatial indexes** for large datasets
5. **Handle missing data** gracefully
6. **Document coordinate systems** in metadata
7. **Validate results** with independent data

---

## References

1. Gillies, S. et al. (2016). *Geospatial Python*. Apress.
2. Butler, H. et al. (2019). *Learning Geospatial Analysis with Python*. Packt.
3. GDAL/OGR Documentation: https://gdal.org/python/
4. GeoPandas Documentation: https://geopandas.org/
5. PyQGIS Documentation: https://docs.qgis.org/latest/en/docs/pyqgis_developer.html
6. BPN (2021). *Pedoman Penggunaan Data Geospasial*.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*
