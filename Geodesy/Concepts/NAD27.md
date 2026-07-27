---
tags: [geodesy, concept, reference-frame, legacy, aigis]
aliases: [NAD27, North American Datum 1927]
created: 2026-07-12
updated: 2026-07-27
---

# 📍 NAD27

**NAD27** (North American Datum 1927) was the first North American horizontal datum covering the entire continent (US, Canada, Mexico). It is a **local datum** based on the Clarke 1866 [[Reference Ellipsoid]], fixed at a single triangulation point (Meades Ranch, Kansas).

## Key Parameters

| Parameter | NAD27 Value | Modern (WGS84) Comparison |
|-----------|-------------|---------------------------|
| **Ellipsoid** | Clarke 1866 | WGS84 (GRS80) |
| **Semimajor axis a** | 6,378,206.4 m | 6,378,137.0 m |
| **Flattening f** | 1/294.978698 | 1/298.257223563 |
| **Origin** | Meades Ranch, Kansas (39°13'26.68"N, 98°32'34.47"W) | Geocentric |
| **Datum type** | Single-station (local) | Geocentric (global) |

## Historical Context

| Year | Development |
|------|-------------|
| **1840's** | First US Coast Survey (USCS) triangulation, several local datums (MEADOW, MEADES RANCH, etc.) |
| **1901** | Preliminary adjustment of US datum (7 stations, 0.1 m accuracy) |
| **1909** | North American Datum (NAD) — 60 stations, 2 m accuracy |
| **1927** | NAD27 — First full 4-station adjustment covering US, Canada, Mexico |
| **1938–1948** | Smaller regional adjustments (e.g., Alabama, Florida) |
| **1948–1968** | New geodetic arcs in North America, original datums |
| **1969–1987** | Conversion to NAD83 began |

### The Meades Ranch Origin

The station at Meades Ranch, Kansas, was chosen as the fundamental point because of its central location in the triangulation network. It was given:
$$
\phi_0 = 39^\circ\,13'\,26.686''\ \text{N}\lambda_0 = 98^\circ\,32'\,30.506''\ \text{W
}$ $All coordinate differences were measured radially from this point. The **azimuth** was also defined at Meades Ranch: $$\alpha_0 = 75^\circ\,53'\,17.2''$ $ ## Parameters of the Clarke 1866 Ellipsoid

| Parameter | Value |
|-----------|-------|
| $a$| 6,378,206.4 m |
|$b$(derived) | 6,356,583.8 m |
|$f$| 1/294.978698 |
|$ e^2 $| 0.006768658 |
|$ e'^2 $ | 0.006814785 |
| Location difference vs WGS84 | Up to 180 m |

## Datum Shift: NAD27 → WGS84/NAD83

The offset between NAD27 and modern datums varies across North America. Direct Helmert transformation is inaccurate because NAD27 was a **single-station** datum (no geocentric alignment).

### Typical Offsets

| Region | $dX$ (NAD27−WGS84) | $dY$ | $dZ$ |
|--------|--------------------|------|------|
| Contiguous US | −15 to −50 m | ±20 m | 0 to +20 m |
| Alaska | −100 to +70 m | −100 to +90 m | −30 to +80 m |
| Canada | −50 to 0 m | 0 to +50 m | ±30 m |
| Hawaii | −50 to −100 m | −100 to −200 m | −20 to +100 m |

### Recommended Approach: Grid-Based Shifts

For NAD27 → NAD83/WGS84 conversion, use **NADCON** (US) or **NTv2** (Canada):

- **NADCON** (US National Ocean Service): Grid shift files at 30″ × 30″ resolution. Covers CONUS, Alaska, Hawaii, Puerto Rico.

- **NTv2** (Natural Resources Canada): Grid shift files for Canada at 1′ × 1′ resolution.

### Helmert 7-Parameter (Bursa-Wolf) Approximation

For NAD27→WGS84 (continental US), approximate parameters:

| Parameter | Value |
|-----------|-------|
| $T_x$ | −8 m |
| $T_y$ | +152 m |
| $T_z$ | −178 m |
| $s$| +3.6 × 10⁻⁶ (3.6 ppm) |
|$ R_x $| −24.7″ |
|$ R_y $| +14.5″ |
|$ R_z$ | +2.37″ |

These yield ~±20 m accuracy — not good enough for cadastral or engineering work. Grid shifts are mandatory.

## Why NAD27 Still Matters

- **Historical maps and surveys** (USGS topo maps drawn before 1990) may use NAD27.

- **NGS data sheets** for stations not yet readjusted may still be in NAD27.

- **Oil and gas records** (especially offshore) may reference NAD27.

- **Legacy GIS data** may be in NAD27 — detection and transformation are routine.

## Replacement: NAD83

In 1986, North America adopted [[NAD83]] based on the [[GRS80]] ellipsoid and an Earth-centered origin. By 2011, NAD83 had been readjusted to more closely match [[ITRF]].

| Comparison | NAD27 | NAD83 |
|------------|-------|-------|
| Ellipsoid | Clarke 1866 | GRS80 |
| Origin | Local (Meades Ranch) | Geocentric |
| Datum type | Single-station (local) | Realization from ITRF |
| Adjustment size | 35,000 stations | 250,000 stations |
| Accuracy | ±10 m (relative) | ±0.01 m (relative) |
| Conversion to WGS84 | Up to ±180 m | < 1 m |

## References

- NOAA/NGS (1989). *North American Datum of 1983*. NOAA Professional Paper No. 2.

- National Geodetic Survey (2002). *History of the North American Datum*.

- Vanček, P. & Krakiwsky, E. J. (1982). *Geodesy: The Concepts*.

- NGS NADCON users guide: www.ngs.noaa.gov/TOOLS/Nadcon/Nadcon.html

## Related

- [[Datum]] · [[NAD83]] · [[Horizontal Datum]] · [[Helmert Transformation]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
