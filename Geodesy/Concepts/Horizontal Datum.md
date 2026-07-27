---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [Horizontal Datum, Datum Horizontal, Local Datum, Geodetic Datum]
created: 2026-07-12
updated: 2026-07-27
---

# 🧭 Horizontal Datum

A **horizontal datum** defines the relationship (position + orientation) between a [[Reference Ellipsoid]] and the Earth's body, enabling horizontal coordinates (latitude, longitude) to be assigned to real points. It answers: *where is the ellipsoid in relation to the Earth?*

## Components of a Horizontal Datum

| Component | What It Defines | Example Values |
|-----------|----------------|----------------|
| **Reference Ellipsoid** | Shape of the Earth model | WGS84, GRS80, Clarke 1866 |
| **Origin point** | Where $\phi, \lambda$ are defined | Greenwich (ITRF), Meades Ranch (NAD27) |
| **Orientation** | Axes direction | Earth-centered, Earth-fixed (modern) or conventional pole + meridian |
| **Epoch** | Time of definition | 1984.0 (WGS84), 1989.0 (ETRS89) |
| **Velocity field** | Station motion (if any) | Present in ITRF; absent in "fixed" frames |

## Local vs. Global Datums

| Property | Local Datum | Global Datum |
|----------|-------------|--------------|
| **Example** | NAD27, ED50, DGN95 | WGS84, ITRF2014, ETRS89 |
| **Origin** | Single triangulation station | Center of mass (geocentric) |
| **Ellipsoid** | Often fitted regionally | GRS80 or WGS84 |
| **Coverage** | National or regional | Worldwide |
| **Coordinates vary with time** | No | Yes (plate tectonics) |
| **CORS network** | Not required | Required |
| **Satellite era compatible** | Not natively | Yes |

## Key Historical and Modern Datums

### American Datums

| Datum | Year | Ellipsoid | Origin | Status |
|-------|------|-----------|--------|--------|
| **NAD27** | 1927 | Clarke 1866 | Meades Ranch, KS | Legacy only |
| **NAD83** | 1986 | GRS80 | Geocentric (≈ITRF89) | Still used in US |
| **NAD83(2011)** | 2011 | GRS80 | ≈ITRF2008 at epoch 2010 | Current US realization |
| **NATRF2022** | 2022 | GRS80 | ITRF2020 + 3 plates | New US realization |

### European Datums

| Datum | Year | Ellipsoid | Origin | Status |
|-------|------|-----------|--------|--------|
| **ED50** | 1950 | International 1924 | Pulkovo | Legacy |
| **ETRS89** | 1989 | GRS80 | Geocentric (≈ITRF89) | Current EU |
| **ITRF2014** | 2014 | GRS80 | Geocentric | Active reference |

### Asian Datums

| Datum | Year | Ellipsoid | Origin | Status |
|-------|------|-----------|--------|--------|
| **DGN95** | 1995 | WGS84 | Geocentric | Indonesia |
| **SAD69** | 1969 | South American 1969 | Local (Brazil) | Legacy |
| **JGD2011** | 2011 | GRS80 | Geocentric | Japan |
| **GCS94** | 1994 | GRS80 | Geocentric | China (CGCS2000) |

## Indonesia's DGN95

The **Datum Geodesi Nasional 1995** (DGN95) is Indonesia's official geodetic datum:

- **Ellipsoid:** WGS84

- **Origin:** Geocentric (essentially identical to WGS84 at time of definition)

- **Realization:** Tied to ITRF94/ITRF2000 through CORS-Indonesia network

- **Status:** Current official datum for mapping, cadastral, and engineering surveys

| DGN95 Property | Value |
|----------------|-------|
| Semimajor axis | 6,378,137 m |
| Flattening | 1/298.257223563 |
| Coordinates | Essentially WGS84 |
| Grid projection | UTM (6° zones) or TM3° strips |

## Brazil's SAD69

The **South American Datum 1969** was the regional datum for South America:

- **Ellipsoid:** South American 1969 ($a = 6,378,160$m,$1/f = 298.25$)

- **Origin:** Chua Station, Goiás, Brazil

- **Replaced by** SIRGAS2000 (geocentric, tied to ITRF95), now the official South American datum

| Parameter | SAD69 | SIRGAS2000 |
|-----------|-------|------------|
| Ellipsoid | S. American 1969 | WGS84/GRS80 |
| Origin | Local (Chua) | Geocentric |
| Accuracy vs WGS84 | ±5–20 m (Helmert 7-param) | ±0.01 m (essentially WGS84) |

## Why Datum Matters in Practice

- **GPS gives WGS84** coordinates; old maps may be NAD27, ED50, DGN95, etc.

- **The same φ,λ pair maps to different real-world locations** on different datums — this is the classic "GPS vs map" offset.

- **Converting between datums** requires a [[Datum Transformation]]: 3-parameter (Bursa-Wolf), 7-parameter (Helmert), or grid-based (NADCON/NTv2).

- **Errors of 50–500 m** can occur if datums are confused.

## Modern Datum Definition (ITRF-Based)

All current global and regional datums are now defined as realizations of [[ITRF]]:
$$\mathbf{X}_{ITRF2014}(t) = \mathbf{T} + (1+s)\mathbf{R}\,\mathbf{X}_{ETRS89}(t)$$

This means a modern datum is: an ITRF realization + plate model + a transformation epoch = a fixed frame on a given tectonic plate.

## References

- Torge, W. & Müller, J. (2012). *Geodesy*, Chapter 10.

- NGA (2014). *WGS84 Technical Report*.

- BIG (2019). *Peraturan Kepala BIG No. 2/2019 tentang Datum*.

## Related

- [[Datum]] · [[Datum Transformation]] · [[Helmert Transformation]] · [[NAD27]] · [[NAD83]] · [[ETRS89]] · [[Indonesia]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]]
