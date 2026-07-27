---
tags: [aigis, concept, physics, astronomy, reference-frames]
aliases: [Celestial Coordinates, Astronomical Coordinates]
created: 2026-07-27
---

# Celestial Coordinates

**Core Idea:** Celestial coordinates map positions on the sky, analogous to latitude/longitude on Earth. Essential for geodetic astronomy — determining azimuth from star observations.

## Coordinate Systems

| System | Basis | Use in Geodesy |
|--------|-------|----------------|
| **Equatorial** (RA, Dec) | Earth's equator, vernal equinox | Star catalogs |
| **Horizontal** (Az, El) | Local horizon, zenith | Observer-based surveys |
| **Ecliptic** (λ, β) | Earth's orbital plane | Sun/moon positions |
| **Galactic** (l, b) | Milky Way plane | Not used in geodesy |

## Key Relationships
$$

\sin(el) = \sin\phi \sin\delta + \cos\phi \cos\delta \cos(H)$$where$H = \text{LST} - \alpha$ (hour angle = local sidereal time minus right ascension).

## In Geodesy

- **Azimuth determination:** Observe star → compute horizontal coordinates → derive geodetic azimuth

- **Time systems:** UTC, UT1, TAI, GPS time — all needed for accurate star positions

- **Earth Orientation Parameters:** Link celestial and terrestrial frames

## Related

- [[Precession and Nutation]] — Star position corrections

- [[Time Systems]] — UTC, UT1, sidereal time

- [[ITRF]] — Terrestrial reference frame

---
*Part of [[Physics MOC]] → [[Geodesy MOC]]*