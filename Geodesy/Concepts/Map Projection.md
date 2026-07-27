---
tags: [aigis, concept, geodesy, map-projection, utm, mercator, distortion, coordinate-systems]
created: 2026-07-27
updated: 2026-07-27
---

# Map Projection

## For Geodesy & Mapping

**Core Idea:** Map projections transform the curved ellipsoid onto a flat plane. Every projection introduces distortion (area, shape, distance, or direction) — no flat map can preserve all four. Understanding projection theory enables correct selection, interpretation, and coordinate transformation for surveying, GIS, and navigation.

---

## Fundamental Concepts

### The Projection Problem

$$(x, y) = f(\phi, \lambda) \quad \text{and} \quad (\phi, \lambda) = g(x, y)$ $

**Tissot's Indicatrix** — the infinitesimal ellipse showing distortion:

| No Distortion | Equal-Area | Conformal | Equidistant |
|--------------|------------|-----------|-------------|
| Circle ($ a=b=1 $) | Area same globally | Shape preserved locally | Scale along one direction constant |

### Distortion Parameters

| Parameter | Symbol | Meaning |
|-----------|--------|---------|
| Scale factor (north-south) | $ m $ | $ h = \frac{d s_\text{map}}{d s_\text{ellipsoid}} $ (meridian) |
| Scale factor (east-west) | $ n $ | $ k = \frac{d s_\text{map}}{d s_\text{ellipsoid}} $ (parallel) |
| Maximum angular distortion | $\omega $|$\sin(\omega/2) = \frac{|h-n|}{h+n} $ |
| Area scale | $ S $ | $ S = h \cdot n \cdot \sin\theta $ (or $ h \cdot n $ for conformal) |

---

## Classification of Projections

### By Preserved Property

| Type | Property | Use |
|------|----------|-----|
| **Conformal** (Mercator, UTM, Lambert Conformal Conic) | Shape preserved locally; angles correct | Navigation, topographic maps |
| **Equal-Area** (Lambert Azimuthal Equal-Area, Albers) | Area correct | Thematic mapping, area computation |
| **Equidistant** (Equirectangular, Azimuthal Equidistant) | Scale along one direction correct | Distance measurement |
| **Compromise** (Robinson, Winkel Tripel) | None preserved; balanced distortion | General-purpose, web maps |

### By Projection Surface

| Surface | Example | Properties |
|---------|---------|------------|
| **Cylindrical** | Mercator, Transverse Mercator | Good near equator/central meridian |
| **Conic** | Lambert Conformal Conic, Albers | Good for mid-latitude zones |
| **Azimuthal (planar)** | Stereographic, Gnomonic | Good at poles; true direction from center |

---

## Key Projections in Detail

### Mercator (Regular Cylindrical Conformal)

$ $

x = R\lambday = R \ln\left[\tan\left(\frac{\pi}{4} + \frac{\phi}{2}\right)\right
]

$$**Inverse:** $ $

\lambda = \frac{x}{R}\phi = 2\arctan(e^{y/R}) - \frac{\pi}{2
}

$$ **Scale factor:** $ $ m = \frac{1}{\cos\phi} = \sec\phi $$ **Distortion:** Scale increases toward poles (infinite at poles). Used for navigation (straight lines are loxodromes).

### Universal Transverse Mercator (UTM)

**Zone system:** 60 zones, each 6° wide:

| Zone | Central Meridian Longitude |
|------|---------------------------|
| Zone 48 | 105°E (west Java) |
| Zone 49 | 111°E (Borneo) |
| Zone 50 | 117°E (Sulawesi) |
| Zone 51 | 123°E (east Indonesia) |

**Scale factor (central meridian):**$ k_0 = 0.9996 $**Easting formula:*
*

$ $ E = 500{,}000 + [k_0 \text{(}N + \text{...})]$$

False easting = 500,000 m (to avoid negative coordinates)
False northing = 0 m (northern hemisphere), 10,000,000 m (southern)

**Scale variation:*
*

$ $ k = k_0\left(1 + \frac{\lambda'^2}{2}\cos^2\phi\right)$$

where $\lambda'$ is the longitude difference from central meridian. Maximum scale error ~0.1% at zone edges.

### Lambert Conformal Conic (LCC)

Used for Indonesia's large meridional extent:

$ $ n = \frac{\ln(\cos\phi_1/\cos\phi_2)}{\ln[\tan(\pi/4+\phi_2/2)/\tan(\pi/4+\phi_1/2)]}F = \frac{\cos\phi_1 \tan^n(\pi/4+\phi_1/2)}{n}r = F / \tan^n(\pi/4+\phi/2)$$

$\phi_1, \phi_2 $= standard parallels where scale is exact.

### Stereographic (Azimuthal Conformal)

**Used for:** Polar regions, GNSS satellite orbits visualization
.

$ $ k = \frac{2}{1 + \sin\phi_0\sin\phi + \cos\phi_0\cos\phi\cos\Delta\lambda}$$

---

## In Geodesy Context

### UTM Zones for Indonesia

| Zone | Longitude Range | Covers |
|------|----------------|--------|
| 46 | 93°E–99°E | Sumatra |
| 47 | 99°E–105°E | Sumatra, Java |
| 48 | 105°E–111°E | Java, Bali, Kalimantan |
| 49 | 111°E–117°E | Kalimantan, Sulawesi |
| 50 | 117°E–123°E | Sulawesi |
| 51 | 123°E–129°E | Maluku |
| 52 | 129°E–135°E | Papua |
| 53 | 135°E–141°E | Papua |

**Indonesia spans 8 UTM zones** — coordinates are only meaningful with zone number.

### Coordinate Conversion Steps

1. **Geodetic**$ (\phi, \lambda, h) $ on reference ellipsoid (e.g., WGS84)
2. **Geocentric**$ (X, Y, Z) $ ECEF
3. **Projected**$ (E, N) $ UTM or other projection

Accuracy check: Convert back and compare; closure error should be < 1 mm.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ x = R\lambda $, $ y = R\ln\tan(\pi/4+\phi/2) $ | Mercator forward | Navigation |
| $ m = 1/\cos\phi $ | Mercator scale | Distortion at latitude |
| $ k_0 = 0.9996 $ | UTM scale factor | Central meridian |
| $ k = k_0(1+\lambda'^2\cos^2\phi/2) $ | UTM scale variation | Scale at distance |
| $ S = h\cdot n $ | Area scale | Distortion type |

---

## Related Concepts

- [[Reference Ellipsoid]] — Base geometry for projections

- [[UTM]] — Universal Transverse Mercator

- [[Transverse Mercator]] — The underlying projection

- [[Mercator]] — Regular cylindrical conformal

- [[Geodetic Coordinates]] — Latitude, longitude input

- [[Projected Coordinates]] — Easting, northing output

- [[PROJ]] — Software library

---

## Study Problems

1. **Recall:** Why is there a false easting of 500,000 m in UTM?
2. **Application:** A point in Jakarta has coordinates $ (\phi, \lambda) = (-6.1745°, 106.8227°) $. Which UTM zone? Compute the UTM easting and northing (WGS84). What is the scale factor at this point?
3. **Derivation:** Show that Mercator is conformal by computing the scale factors $ h $ and $ k $ and showing $ h = k $.
4. **Real-world:** If you measure a distance in UTM at the zone edge (maximum scale error 0.1%), what is the difference between the measured UTM distance and true ellipsoidal distance over 1 km?

---

## Common Mistakes

1. **Forgetting which zone you're in:** UTM coordinates are meaningless without zone number.
2. **Confusing UTM northings in southern hemisphere:** Always subtract from 10,000,000 m south of equator.
3. **Treating UTM distances as ellipsoidal:** The scale factor applies — correct first.
4. **Using the wrong ellipsoid:** WGS84, GRS80, Bessel all give different projected coordinates.
5. **Ignoring central meridian scale factor:** $ k_0 = 0.9996$ means scale at central meridian is 0.9996, not 1.0.

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*