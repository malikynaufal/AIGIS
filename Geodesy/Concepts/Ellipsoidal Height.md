---
tags: [geodesy, concept, heights, aigis]
aliases: [Ellipsoidal Height, h, Tinggi Elipsoidal, Geodetic Height]
created: 2026-07-12
updated: 2026-07-27
---

# 📈 Ellipsoidal Height (h)

**Ellipsoidal height** $h$\(also called *geodetic height*) is the distance measured above the [[Reference Ellipsoid]] along the ellipsoidal *normal* (the perpendicular to the ellipsoid surface). It is what [[GNSS]]/[[GPS]] receivers measure **directly**.

## The Height Trio

Every point on Earth has three distinct height values:

| Symbol | Name | Reference Surface | How It Is Obtained |
|--------|------|-------------------|--------------------|
| $h$ | Ellipsoidal height | [[Reference Ellipsoid]] | GNSS/GPS directly |
| $H$ | [[Orthometric Height]] | [[Geoid]] (mean sea level) | Spirit leveling |
| $N$ | [[Geoid Undulation]] | Separation (geoid − ellipsoid) | Geoid model output |

### Fundamental Relatio
n$ $h = H + N$$This simple equation is the bridge between satellite-based positioning (ellipsoidal) and traditional surveying (orthometric). For a GNSS survey: measure $h$ via satellite, subtract$N$from a geoid model, obtain$H$ usable for mapping and engineering.

## Geometric Meaning

At a point $P$ with geodetic latitude$\phi$and longitude$ \lambda $:

- The ellipsoidal height$h$ extends along the *ellipsoidal normal* (the line perpendicular to the ellipsoid at $\phi, \lambda$).

- This line does **not** pass through Earth's center of mass (except at the equator and poles), unlike the geocentric radius.

- The point's ECEF coordinates are:$ $X = (N + h)\cos\phi\cos\lambdaY = (N + h)\cos\phi\sin\lambdaZ = \left(N(1 - e^2) + h\right)\sin\phi $$where $ N = \frac{a}{\sqrt{1 - e^2\sin^2\phi}} $ is the radius of curvature in the prime vertical.

## Physical Interpretation

- **Ellipsoidal height is geometric**, not physical.

- Because the [[Reference Ellipsoid]] is a smooth mathematical surface, $h$ takes no account of gravity, topography, or mass distributions.

- Values range from about $-100$ m (ocean trenches relative to ellipsoid) to $+9000$ m (Mt. Everest ellipsoidal height).

## Typical Values at Selected Locations (WGS84)

| Location | $\phi$|$\lambda$ | Ortho. H (m) | N (m) | Ellip. h (m) |
|----------|--------|-----------|--------------|-------|--------------|
| Mt. Everest | 27.99°N | 86.93°E | 8848.9 | ~−25 | ~8824 |
| Dead Sea | 31.50°N | 35.50°E | −430.5 | ~−20 | ~−450 |
| Indian Ocean | 0° | 80°E | 0 | ~−105 | −105 |
| North Atlantic | 50°N | 10°W | 0 | ~+50 | 50 |

The geoid undulation $N$ varies by ±110 m globally, causing significant differences between $h$ and$H$.

## Accuracy Considerations

| Level | Ellipsoidal Height Accuracy | Application |
|-------|----------------------------|-------------|
| Consumer GPS | ±5–10 m | Navigation |
| SBAS (WAAS/EGNOS) | ±1–2 m | Aviation |
| RTK (Real-Time Kinematic) | ±1–3 cm | Surveying |
| Static GNSS (post-processed) | ±2–10 mm | Geodesy, deformation |
| PPP (Precise Point Positioning) | ±2–5 cm | Remote positioning |

## The Curse of Ellipsoidal Height in Practice

- **No direct physical meaning** — a water surface does not follow a constant-$h$ surface.

- **Requires geoid model** to convert to orthometric height for civil engineering.

- **Datum-dependent** — the same point has different $h$ on different ellipsoids (e.g., WGS84 vs. GRS80 differ by ~1 mm, but NAD27 vs. WGS84 differ by tens of meters).

## Relationship to Gravity

The gradient of ellipsoidal height with respect to gravity potential is$ $\frac{dh}{dW} = -\frac{1}{\gamma}$$where $ \gamma $ is normal gravity at the ellipsoid. This connects height systems with [[Physical Geodesy]] and the [[Gravity Field]].

## See also

- [[Orthometric Height]] — The physically meaningful height above sea level

- [[Geoid Undulation]] — The conversion factor $N$- [[Geodetic Coordinates]] — Complete position representation ( $\phi, \lambda, h$)

- [[Geocentric Cartesian ECEF]] — Conversion to/from $X,Y,Z$## References

- Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS — Global Navigation Satellite Systems*. Springer.

- Heiskanen, W. A. & Moritz, H. (1967). *Physical Geodesy*. Freeman.

- Torge, W. & Müller, J. (2012). *Geodesy*. de Gruyter.

## Related

- [[Geoid]] · [[Orthometric Height]] · [[Geoid Undulation]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
