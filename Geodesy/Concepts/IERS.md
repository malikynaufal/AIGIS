---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [IERS, International Earth Rotation Service, IERS Conventions]
created: 2026-07-12
updated: 2026-07-27
---

# 🌍 IERS (International Earth Rotation and Reference Systems Service)

The **IERS** (International Earth Rotation and Reference Systems Service) maintains the high-precision global reference frames — including the [[ITRF]] — and publishes the conventions (Earth rotation, precession, nutation, Earth deformation) that tie [[GNSS]], Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), and DORIS together.

## Core Mission

IERS is one of the five IUGG (International Union of Geodesy and Geophysics) services, established in 1988 as the merger of the International Earth Rotation Service (IERS) and the Bureau International de l'Heure (BIH). It provides:

1. **International Terrestrial Reference Frame (ITRF)** — the highest-precision global frame
2. **IERS Conventions** — the reference manual for all precision geodetic and astrometric work
3. **Earth Orientation Parameters (EOP)** — daily bulletin for rotation and orientation

## Earth Orientation Parameters (EOP)

EOP is the set of parameters that transforms between the Earth-fixed frame and the celestial (space) frame. IERS publishes these daily in Bulletin A and B:

### The Seven EOP Parameters

| Parameter | Symbol | Meaning | Typical Range |
|-----------|--------|---------|---------------|
| **X-polar motion** | $x_p$| Polar motion X-component | ±0.5″ ≈ ±15 m |
| **Y-polar motion** |$y_p$| Polar motion Y-component | ±0.5″ ≈ ±15 m |
| **UT1 − UTC** |$\Delta$UT1 | Earth rotation angle offset | −0.5 to +0.5 s ≈ −225 to +225 m at equator |
| **UT1 − TAI** | — | Earth rotation angle offset | Continuous |
| **LOD** | $\Delta$L | Length of day | 0.001–0.004 s variation |
| **Nut X** | $\epsilon_X$| Nutation X (long-term) | — |
| **Nut Y** |$\epsilon_Y$| Nutation Y (long-term) | — |

### Relationship to GNSS

GNSS satellites broadcast EOP via the navigation message:

- **X, Y** (polar motion): from GPS almanac, ±1 m accuracy

- **UT1−UTC**: encoded in GPS as UTC offset (0 or 1 s), updated every ~1 hr

- **Nut X, Nut Y**: nutation corrections, less commonly broadcast

- **LOD**: used in precise orbit determination (POD), not in broadcast

### EOP Bulletin Products

| Product | Content | Latency | Accuracy |
|---------|---------|---------|----------|
| **Bulletin A** | Final EOP series | 30–40 days | < 1 mas (0.001″) |
| **Bulletin A** | Rapid | 3–5 days | < 2–3 mas |
| **Bulletin A** | 1-day prediction | 0 days (real-time) | 5–10 mas |
| **Bulletin B** | Long-term combined | 2 months | < 0.1 mas |

## IERS Conventions

The **IERS Conventions** (latest: 2010, updated annually) define standards for:

| Conventions | Key Content |
|-------------|-------------|
| **Conventional Reference Frames** | ITRF definition, transformation between ITRF2020 → ITRF2014, etc. |
| **Earth Rotation** | ERA model, precession-nutation (IERS 2010A), polar motion |
| **Solid Earth Tides** | Deformation of geodetic stations due to lunar/solar attraction |
| **Ocean Tides** | Tidal loading displacements |
| **Atmospheric Tides** | Atmospheric pressure effects |
| **Post-Glacial Rebound** | Long-wavelength deformation models |
| **Antenna & Station Coordinates** | Antenna phase center offsets, monumentation standards |
| **Earth Orientation** | LOD corrections, UT1, polar motion conventions |

### Key IERS Reference Standards

| Item | Value/Model | Source |
|------|-------------|--------|
| Earth Rotation Angle (ERA) |$0.7790572732640 + 1.00273781191135448 T_U$ (turns) | IERS Conventions |
| Precession | P03 model (Capitaine et al.) | IERS 2010 |
| Nutation | IERS 2010A (MHB2000) | IERS 2010 |
| Free core nutation | Variable, ~0.7 yr period | IERS monitoring |

## IERS Components and Contributing Services

| Service | Technique | Contribution to ITRF |
|---------|-----------|---------------------|
| **IVS** (International VLBI Service) | Radio VLBI | Earth rotation, nutation |
| **ILRS** (International Laser Ranging Service) | Satellite Laser Ranging | Geocenter, scale |
| **IGS** (International GNSS Service) | GNSS | Orbits, stations, troposphere |
| **IPS/DORIS** (DORIS Service) | Doppler orbitometry | Stations, geocenter |
| **ICET** (IERS Combination Center) | Combination | Final ITRF computation |

## ITRF Generation by IERS

The process:
1. **Contributing technique centers** produce their own time series (positions, velocities).
2. **IERS combines** these time series to produce ITRF using the standard 7-parameter Helmert model with time-dependent parameters.
3. **IERS publishes** the ITRF coordinates/velocities as SINEX files + network of CORS stations.

| ITRF Realization | Data Span | # Stations | Accuracy |
|------------------|-----------|------------|----------|
| ITRF88 | 1980–1988 | ~200 | ~10 cm |
| ITRF89 | 1983–1989 | ~300 | ~5 cm |
| ITRF90 | 1983–1991 | ~400 | ~2 cm |
| ITRF91 | 1984–1991 | ~500 | ~1 cm |
| ITRF93 | 1984–1995 | ~500 | ~5 mm |
| ITRF96 | 1985–1996 | ~1000 | ~3 mm |
| ITRF97 | 1984–1998 | ~1000 | ~1 mm |
| ITRF2000 | 1988–2001 | ~1000 | < 1 mm |
| ITRF2005 | 1989–2005 | ~1000 | < 1 mm |
| ITRF2008 | 1990–2009 | ~1000 | < 1 mm |
| ITRF2014 | 1993–2014 | ~1200 | < 1 mm |
| **ITRF2020** | 2000–2020 | ~1200 | **< 0.3 mm** |

## IERS Links to Geodesy in Practice

| Application | IERS Contribution |
|-------------|-------------------|
| GNSS precise orbit determination | EOP (polar motion, LOD, UT1) |
| Precise Point Positioning (PPP) | ITRF station coordinates as reference |
| Tide gauge records | Sea level references in ITRF |
| Geoid modeling | Frame realization for gravity |
| Satellite mission design | Earth rotation standards |

## References

- Petit, G. & Luzum, B. (2010). *IERS Conventions (2010)*. IERS Technical Note No. 36.

- Altamimi, Z., Rebischung, P., Métivier, L., & Collilieux, X. (2016). *ITRF2014: A New Release...*. J. Geophys. Res., 121(8).

- IERS. www.iers.org

## Related

- [[ITRF]] · [[GNSS]] · [[IGS]] · [[Datum Transformation]] · [[Helmert Transformation]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Kurikulum Teknik Geodesi]]
