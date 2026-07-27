---
tags: [aigis, geodesy, pilihan, spatial-database, postgres, postgis, database]
aliases: [Spatial Database, Basis Data Spasial]
created: 2026-07-27
updated: 2026-07-27
---

# Pilihan: Basis Data Spasial (Spatial Database)

**Kode:** TKD214712 | **SKS:** 3 (2-1) | **Semester:** 6–8

## Course Overview

Spatial database design and implementation using PostgreSQL/PostGIS. Covers spatial indexing (R-tree, GiST), spatial query optimization (ST_ operations), and integration with GIS clients.

## Key Topics

### 1. PostgreSQL + PostGIS

| Feature | PostGIS | Non-Spatial DB |
|---------|---------|----------------|
| Geometry types | Point, LineString, Polygon, Multi* | None |
| Spatial index | GiST | B-tree only |
| Spatial functions | ST_Distance, ST_Intersects, ST_Area | None |
| Coordinate system | SRID support | Not available |

### 2. Spatial Queries

```sql
-- Common PostGIS queries
SELECT ST_Distance(a.geom, b.geom) FROM parcels a, schools b;
SELECT ST_Area(ST_Transform(geom, 32749)) FROM land_parcels;
SELECT ST_Intersects(a.geom, buffer.geom) AS includes;
```

### 3. Spatial Indexing

- R-tree (via GiST): $O(\log N)$ search
- Grid indexing for rasters

---
*Maintained by AIGIS — part of [[Geodesy MOC]]*
