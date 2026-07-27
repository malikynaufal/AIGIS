---
tags: [geodesy, concept, projection, aigis]
aliases: [Mercator, Mercator Projection, Peta Mercator]
created: 2026-07-12
---

# 🧭 Mercator (Projection)

The **Mercator** projection is a **conformal** cylindrical map projection that preserves local angles and shapes — making it the classic chart for marine and aerial navigation, where a constant compass bearing (rhumb line) appears as a straight line on the map.

## Derivation & Key Formulas

For a sphere of radius $R$, the Mercator projection maps a point at latitude $\phi $and longitude $\lambda $to coordinates$(x, y)$:

$$x = R \, (\lambda - \lambda_0)y = R \ln \left[ \tan \left( \frac{\pi}{4} + \frac{\phi}{2} \right) \right] = R \, \text{gd}^{-1}(\phi)$$where $\lambda_0 $is the **central meridian** (garis tengah), and $\text{gd}^{-1} $is the inverse **Gudermannian function**
:

$$\text{gd}^{-1}(\phi) = \sinh^{-1}(\tan \phi) = \text{artanh}(\sin \phi)$$

The inverse (map → sphere)
:

$$\phi = 2 \, \arctan\!\left(e^{y/R}\right) - \frac{\pi}{2}, \qquad \lambda = \lambda_0 + \frac{x}{R} $$

### Conformality (Konformitas)

A map projection is **conformal** when the scale factor is the same in all directions at every point, preserving angles locally. For Mercator this means the **Tissot's indicatrix** at any point is a circle, not an ellipse.

## Scale Factor

The **point scale factor** (skala titik) of Mercator at latitude $\phi $is:

$$k(\phi) = \sec \phi = \frac{1}{\cos \phi} $$

This means:

- At the equator ($\phi = 0°$), $k = 1$— no distortion.

- At$60°$N/S,$k = 2$— distances are doubled.

- As $\phi \to \pm 90°$, $k \to \infty$— the poles cannot be shown (singularitas).

The **scale factor along the meridian** (a) and along the parallel (b) satisfy $k_m = \sec\phi $and $k_p = \sec\phi$, so $k_m = k_p$, confirming conformality.

### Areal Distortion

Because scale grows as $\sec\phi$, **area** is distorted by a factor of $\sec^2\phi$:

$$\text{Area distortion} = k^2 = \sec^2\phi$$At $\phi = 60°$:$\sec^2(60°) = 4$, so a region at 60° N appears four times its true area. This is why Greenland looks larger than Africa on a Mercator map, even though Africa is about 14 times larger in reality.

## Transverse Mercator (Transverse Mercator)

The **Transverse Mercator** (Transverse Mercator / TM) is obtained by rotating the cylinder $90°$so it touches the sphere along a **meridian** instead of the equator. This makes it ideal for mapping regions that are elongated in the N–S direction (wilayah memanjang utara-selatan).

The **Universal Transverse Mercator** (UTM / UTM) system divides the Earth into **60 zones**, each$6°$of longitude wide, with a transverse Mercator projection per zone.

### UTM Scale Factor

Each UTM zone has a central meridian with a scale factor of $k_0 = 0{.}9996$(pengurangan skala)
:

$$x = k_0 \, R \, (\lambda - \lambda_0) \cos \phi, \qquad y = k_0 \, R \, \text{gd}^{-1}(\phi)$$

The false easting is$500{,}000 $m to keep easting values positive (false easting$= 500000 $m).

## Mercator vs Web Mercator (Peta Web)

**Web Mercator** (also EPSG:3857, Pseudo-Mercator) is a variant used by virtually every web mapping platform (Google Maps, Leaflet, OpenStreetMap):

| Property | Classic Mercator (EPSG:3395) | Web Mercator (EPSG:3857) |
|----------|-------------------------------|--------------------------|
| Sphere/ellipsoid | Sphere only | Sphere (assumed $a = b$— simplifikasi) |
| True shape | Correct (conformal) | Approximately conformal |
| Area distortion | Same — grows as $\sec^2\phi$ | Same |
| Use case | Nautical charts, global GIS | Web tiles, interactive maps |
| Valid latitude | All | Typically limited to $\pm 85{.}05°$ |
| EPSG code | 3395 | 3857 |

**Perbedaan utama** (key difference): Web Mercator assumes a spherical Earth and uses the same formula but caps the latitude at approximately $\pm 85°05'40''$because the projection goes to infinity at the poles — on a web map, the poles simply don't appear (puncak kutub terpotong).

In practice, for most web mapping applications the spherical approximation introduces errors of at most $\sim 0{.}3\%$ relative to an ellipsoidal computation — acceptable for tile-based display at consumer zoom levels.

## Applications in Navigation (Aplikasi Navigasi)

1. **Rhumb line (loxodrome)** navigation: A ship maintaining constant bearing draws a straight line on a Mercator chart. The loxodrome curve on the sphere becomes a straight line, enabling simple visual course plotting.
2. **Marine piloting / pelayaran**: Nautical charts worldwide (INT — International Chart) use Mercator projection.
3. **Aeronautical charts**: VFR (Visual Flight Rules) charts often adopt Mercator; IFR high-altitude charts use Lambert Conformal Conic (conformal but not cylindrical).
4. **GIS and web mapping**: OpenLayers, Mapbox, Leaflet, Google Maps — all use Web Mercator tiles for fast, seamless panning and zooming.
5. **Military / defense**: NATO and national mapping agencies use Transverse Mercator variants (e.g., UTM, MGRS) for tactical planning.

## Strengths and Limitations

**Kelebihan** (Pros):

- **Konformal**: angles preserved — ideal for navigation

- Straight rhumb lines — easy course plotting

- Seamless global rectangular grid at low latitudes

**Kekurangan** (Cons):

- Area wildly distorted at high latitudes (tidak ada di dekat kutub)

- Cannot show the poles ($\phi = \pm 90°$ is a singularity / singularitas)

- Distances can only be trusted at the equator or locally

## Related

- [[Map Projection]] · [[Transverse Mercator]] · [[UTM]] · [[Geodesy MOC]] · [[Map Projection]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
