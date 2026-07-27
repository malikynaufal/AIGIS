# Analisis Geospasial (*Spatial Analysis*)

**Kode:** TKD213608
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Pemrograman Spasial, Model Terrain Digital

---

## 1. Overview

Spatial analysis (*analisis geospasial*) is the process of examining the locations, attributes, and relationships of features in spatial data through computational techniques. It answers "where," "what," "how," and "why" questions about geographic phenomena using quantitative methods.

---

## 2. Core Spatial Analysis Operations

### 2.1 Overlay Analysis

Overlay combines two or more spatial datasets sharing the same geographic space to create a new dataset.

#### Vector Overlay

| Operation | Description | Output |
|-----------|-------------|--------|
| **Intersection** | Features in both layers | Intersecting geometry |
| **Union** | All features from both layers | Full coverage |
| **Difference** | A minus B | A not in B |
| **Symmetric Difference** | A XOR B | Non-overlapping |
| **Identity** | A with B's attributes | A + B attributes |

```python
import geopandas as gpd

# Intersection
intersection = gpd.overlay(gdf1, gdf2, how='intersection')

# Union
union = gpd.overlay(gdf1, gdf2, how='union')

# Difference
diff = gpd.overlay(gdf1, gdf2, how='difference')

# Symmetric difference
sym_diff = gpd.overlay(gdf1, gdf2, how='symmetric_difference')

# Identity
identity = gpd.overlay(gdf1, gdf2, how='identity')
```

#### Raster Overlay (Map Algebra)$\$$C = f(A, B)$\$ $where$f$can be:

- **Arithmetic:**$ A + B$, $A - B$, $A imes B$, $A / B$- **Logical:**$A ext{ AND } B$, $A ext{ OR } B$, $ext{NOT } A$- **Relational:**$A > B$, $A == B$, $A < B$```python
import rasterio
from rasterio.enums import Resampling

# Read rasters
with rasterio.open('raster1.tif') as src1, rasterio.open('raster2.tif') as src2:
 arr1 = src1.read(1)
 arr2 = src2.read(1, out_shape=arr1.shape, resampling=Resampling.bilinear)

# Map algebra
result = arr1 + arr2 # or arr1 * arr2, arr1 / arr2, etc.
```

### 2.2 Buffer Analysis

Buffers define zones around features at a specified distance.

**Single distance:**
```python
gdf['buffer'] = gdf.buffer(distance=1000) # 1000 meters
```

**Variable distance (field-based):**
```python
gdf['buffer'] = gdf.apply(lambda row: row.geometry.buffer(row['buffer_dist']), axis=1)
```

**Multi-ring buffers:**
```python
from shapely.ops import unary_union

distances = [100, 500, 1000]
buffers = [gdf.geometry.buffer(d) for d in distances]
multi_ring = gpd.GeoDataFrame(geometry=buffers)
```

**Dissolve buffer (merged):**
```python
buffer = gdf.buffer(500).dissolve()
### 2.3 Interpolation

Interpolation estimates values at unmeasured locations from measured points.

#### Inverse Distance Weighting (IDW)$\$ $z_0 = \frac{\sum_{i=1}^{n} w_i z_i}{\sum_{i=1}^{n} w_i},

```python
from scipy.interpolate import griddata
import numpy as np

# Points
points = np.array([(x_i, y_i) for x_i, y_i in zip(gdf.geometry.x, gdf.geometry.y)])
values = gdf['value'].values

# Grid
xi = np.linspace(xmin, xmax, nx)
yi = np.linspace(ymin, ymax, ny)
xi, yi = np.meshgrid(xi, yi)

# IDW
grid = griddata(points, values, (xi, yi), method='linear') # 'nearest', 'cubic'
```

#### Kriging (Geostatistical)

Uses variogram to model spatial autocorrelation$ $\gamma(h) = \frac{1}{2N(h)} \sum_{i=1}^{N(h)} [z(x_i) - z(x_i + h)]^2$ $```python
from pykrige.ok import OrdinaryKriging

OK = OrdinaryKriging(
 x=gdf.geometry.x,
 y=gdf.geometry.y,
 z=gdf['value'],
 variogram_model='spherical',
 verbose=False
)

z, ss = OK.execute('grid', xi, yi)
```

#### Spline

Minimizes curvature:

```python
from scipy.interpolate import Rbf

spline = Rbf(points[:,0], points[:,1], values, function='thin_plate')
z = spline(xi, yi)
```

### 2.4 Network Analysis

Analysis of connectivity and flow along linear networks (roads, rivers, pipelines).

#### Shortest Path (Dijkstra)

```python
import networkx as nx

# Build graph from line data
G = nx.Graph()
for _, row in gdf_lines.iterrows():
 G.add_edge(row['from'], row['to'], weight=row['length'])

# Shortest path
path = nx.shortest_path(G, source='A', target='B', weight='weight')
distance = nx.shortest_path_length(G, source='A', target='B', weight='weight')
```

#### Service Area (Isochrones)

```python

# Isochrone at 30 minutes
service_area = nx.single_source_dijkstra_path_length(G, source='A', cutoff=30*60)
```

#### Flow Direction / Accumulation

```python

# In GRASS GIS or TauDEM:

# r.watershed - Flow direction, accumulation, stream network

# Or in Python with pysheds:
from pysheds.grid import Grid

grid = Grid.from_raster('dem.tif')
flowdir = grid.flowdir(grid.read_raster('dem.tif'))
acc = grid.accumulation(flowdir)
```

---

## 3. Spatial Statistics

### 3.1 Point Pattern Analysis

#### Quadrat Analysis

Tests for complete spatial randomness (CSR)$\$ $\chi^2 = \sum_{i=1}^{q} \frac{(O_i - E)^2}{E} $ $where$O_i$= observed points in quadrat$i$, $E = n/q $= expected.

#### Nearest Neighbor Analysis

**Clark-Evans index:*
*$ $R = \frac{\bar{r}_{obs}}{\bar{r}_{exp}} = \frac{\frac{1}{n}\sum r_i}{0.5\sqrt{A/n}}$ $|$R$ Value | Pattern |
|-----------|---------|
| $R \approx 1$ | Random |
| $R < 1$ | Clustered |
| $R > 1$ | Regular/Dispersed |

```python
from pointpats import PointPattern
from pointpats.distance_statistics import nndist

pp = PointPattern(gdf[[Coordinates]].values)
r_obs = pp.nndist.mean()
r_exp = 0.5 * np.sqrt(pp.area / len(pp))
R = r_obs / r_exp
```

#### Ripley's K Functio
n$ $ K(d) = \frac{A}{n^2} \sum_{i \neq j} \frac{I(d_{ij} \leq d)}{w_{ij}}$ $```python
from pointpats import K_function

k = K_function(pp, distances=[100, 200, 500, 1000])
```

### 3.2 Spatial Autocorrelation

#### Global Moran's
I$ $I = \frac{n}{S_0} \frac{\sum_i \sum_j w_{ij}(x_i - \bar{x})(x_j - \bar{x})}{\sum_i (x_i - \bar{x})^2}$ $where$ S_0 = \sum_i \sum_j w_{ij} $.

```python
from esda.moran import Moran

moran = Moran(gdf['value'], weights_matrix)
print(moran.I, moran.p_sim)
```

#### Local Moran's I (LISA)

Identifies clusters (HH, LL) and outliers (HL, LH):

```python
from esda.moran import Moran_Local

lisa = Moran_Local(gdf['value'], weights_matrix)
gdf['quadrant'] = lisa.q # 1=HH, 2=LH, 3=LL, 4=HL
gdf['significant'] = lisa.p_sim < 0.05
```

#### Geary's C$ $C = \frac{(n-1)}{2S_0} \frac{\sum_i \sum_j w_{ij}(x_i - x_j)^2}{\sum_i (x_i - \bar{x})^2}$ $ 3.3 Spatial Regression

**OLS (Ordinary Least Squares):*
*$ $## 3.3 Spatial Regression

**OLS (Ordinary Least Squares):*
*y = X\beta + \epsilon $ $# ## 3.3 Spatial Regression

**OLS (Ordinary Least Squares):*
*y = X\beta + \epsilon

**Spatial Lag Model (SAR):*
*$ $y = \rho W y + X\beta + \epsilon$ $**Spatial Error Model (SEM):*
*$ $y = X\beta + \epsilon, \quad \epsilon = \lambda W \epsilon + u $ $```python
from spreg import ML_Lag, ML_Error

# Spatial lag
lag_model = ML_Lag(y, X, w)

# Spatial error
error_model = ML_Error(y, X, w)
```

---

## 4. Raster Analysis

### 4.1 Map Algebra Operations

| Category | Operations |
|----------|------------|
| **Local** | Cell-by-cell: +, -, *, /, max, min, reclassify |
| **Focal** | Neighborhood: mean, sum, median, majority, variety |
| **Zonal** | Zone statistics: mean, sum, min, max, std by zone |
| **Global** | Distance, cost path, viewshed |

### 4.2 Focal Statistics (Moving Window)

```python
import rasterio
from scipy.ndimage import uniform_filter, median_filter

with rasterio.open('dem.tif') as src:
 arr = src.read(1)

# 3x3 mean filter
mean_3 = uniform_filter(arr, size=3)

# 5x5 median filter
median_5 = median_filter(arr, size=5)
```

### 4.3 Zonal Statistics

```python
from rasterstats import zonal_stats

stats = zonal_stats(gdf_zones, 'value.tif', stats=['mean', 'sum', 'min', 'max', 'std'])
gdf_zones = gdf_zones.join(pd.DataFrame(stats))
```

### 4.4 Cost Surface and Least-Cost Path

```python
import networkx as nx

# Cost surface from multiple factors
cost = (slope_factor * 0.4 + landcover_factor * 0.3 + distance_factor * 0.3)

# Least-cost path
path = nx.shortest_path(G, source=start, target=end, weight='cost')
```

### 4.5 Viewshed Analysis

```python

# From r.viewshed in GRASS, or:
from rsgislib.imageutils import viewshed

# Or using rasterio + custom algorithm

# Ray-casting from observer point
```

---

## 5. Terrain Analysis (from DEM)

### 5.1 Primary Derivatives

| Derivative | Formula | Unit |
|------------|---------|------|
| **Slope** | $\alpha = \arctan\sqrt{(artial z/artial x)^2 + (artial z/artial y)^2} $| degrees/% |
| **Aspect** |$ heta = \arctan2(-artial z/artial x, artial z/artial y)$\$| 0–360° |
| **Curvature (profile)** |$ k_p = \frac{z_{xx}z_x^2 + 2z_{xy}z_xz_y + z_{yy}z_y^2}{(z_x^2 + z_y^2)^{3/2}} $| 1/m |
| **Curvature (plan)** |$ k_{pl} = \frac{z_{xx}z_y^2 - 2z_{xy}z_xz_y + z_{yy}z_x^2}{(z_x^2 + z_y^2)^{3/2}} $ | 1/m |

```python
from scipy.ndimage import sobel

# Slope
dx = sobel(dem, axis=1) * cellsize
dy = sobel(dem, axis=0) * cellsize
slope = np.degrees(np.arctan(np.sqrt(dx**2 + dy**2)))

# Aspect
aspect = np.degrees(np.arctan2(-dx, dy))
aspect = (aspect + 360) % 360
```

### 5.2 Secondary Derivatives

- **Hillshade** — simulated illumination

- **TPI** (Topographic Position Index) — relative position

- **TRI** (Terrain Ruggedness Index) — surface roughness

- **SPI** (Stream Power Index) — erosion potential

- **TWI** (Topographic Wetness Index) —$\ln(a / an\beta)$\$---

## 6. Indonesian Spatial Analysis Applications

### 6.1 Disaster Risk Analysis

| Hazard | Analysis Method |
|--------|----------------|
| **Flood** | HAND model + rainfall + river network |
| **Landslide** | Slope + lithology + land cover + rainfall |
| **Earthquake** | Fault distance + PGA + soil amplification |
| **Tsunami** | Inundation modeling + DEM + fault source |

### 6.2 Land Suitability Analysis

Multi-criteria evaluation (MCE) using **AHP** (Analytic Hierarchy Process)$\$ $S = \sum_{i=1}^{n} w_i \cdot x_i$ $where$w_i$ are weights from pairwise comparison matrix.

### 6.3 Watershed Management

- **Delineation** — pour point + flow direction

- **Sediment yield** — USLE/RUSLE model

- **Water balance** — rainfall - ET - runoff

---

## 7. Software Tools

| Software | Strength |
|----------|----------|
| **QGIS** | General GIS, plugin ecosystem |
| **ArcGIS Pro** | Commercial, advanced tools |
| **GRASS GIS** | Raster/terrain, hydrology |
| **SAGA GIS** | Terrain analysis, geostatistics |
| **GeoDa** | Spatial statistics (Moran, LISA) |
| **PySAL** | Python spatial analysis library |
| **Google Earth Engine** | Cloud-based, large-scale |

---

## 8. Key Formulas Summary

| Concept | Formula |
|---------|---------|
| IDW | $z_0 = \frac{\sum w_i z_i}{\sum w_i}$ |
| Variogram | $\gamma(h) = \frac{1}{2N}\sum(z_i - z_{i+h})^2 $|
| Moran's I |$ I = \frac{n}{S_0}\frac{\sum w_{ij}(x_i-\bar{x})(x_j-\bar{x})}{\sum(x_i-\bar{x})^2} $|
| Nearest neighbor |$ R = \frac{\bar{r}_{obs}}{0.5\sqrt{A/n}} $|
| Slope |$\alpha = \arctan\sqrt{(artial z/artial x)^2 + (artial z/artial y)^2} $|
| TWI |$\ln(a / an\beta)$\$ |

---

## References

1. Longley, P.A. et al. (2015). *Geographic Information Systems and Science*, 4th ed. Wiley.
2. O'Sullivan, D. & Unwin, D. (2014). *Geographic Information Analysis*, 2nd ed. Wiley.
3. Anselin, L. (1995). *Local Indicators of Spatial Association — LISA*. Geographical Analysis.
4. Burrough, P.A. & McDonnell, R.A. (1998). *Principles of GIS*, 2nd ed. Oxford.
5. Hengl, T. (2009). *A Practical Guide to Geostatistical Mapping*. University of Amsterdam.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*