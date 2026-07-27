---
tags: [geodesy, concept, reference-frame, aigis]
aliases: [ETRS89, European Terrestrial Reference System 1989]
created: 2026-07-12
updated: 2026-07-27
---

# 🌍 ETRS89

**ETRS89** (European Terrestrial Reference System 1989) is the stable European reference frame, based on the [[GRS80]] ellipsoid and fixed to the stable part of the Eurasian Plate. Unlike global frames such as [[ITRF]] which drift with plate tectonics, ETRS89 is designed to have **no residual motion** across Europe.

## Key Concept — Plate-Fixed Frame

ETRS89 is coincident with [[ITRF]]/[[ITRF]] at **epoch 1989.0** (January 1, 1989), and then **held fixed** to the Eurasian Plate. This means:

- A coordinate in ETRS89 does **not change** over time within stable Eurasia.
- The same point in ITRF2000/2005/2008/2014/2020 **drifts** east-north-east at ~2–3 cm/year due to plate motion.
- Converting between ETRS89 and a current ITRF realization requires accounting for **Eurasia plate rotation** via a **14-parameter Helmert transformation** that is epoch-dependent.

## Relationship to ITRF

The transformation between ETRS89 and ITRF at epoch $t$ follows:

$$\mathbf{X}_{ITRF}(t) = \mathbf{X}_{ETRS89} + \mathbf{T}(t) + \mathbf{R}(t)\cdot\mathbf{X}_{ETRS89} + \mathbf{S}(t)$$

where $\mathbf{T}$, $\mathbf{R}$, $\mathbf{S}$ are the time-dependent translation, rotation, and scale parameters published by [[IERS]]/[[ITRF]].

| ITRF Realization | Transformation to ETRS89 (at epoch 2010.0) |
|------------------|---------------------------------------------|
| ITRF2000 → ETRS89 | $\mathbf{T}: (0.054, 0.051, -0.048)$ m |
| ITRF2005 → ETRS89 | $\mathbf{T}: (0.054, 0.051, -0.048)$ m |
| ITRF2014 → ETRS89 | $\mathbf{T}: (0.054, 0.051, -0.048)$ m |
| ITRF2020 → ETRS89 | $\mathbf{T}: (0.054, 0.050, -0.049)$ m |

*Note: Values approximate; consult EUREF technical notes for official parameters.*

## Velocity Field

ETRS89 eliminates the **Eurasian plate motion** (~2.5 cm/yr east-north-east) but local intraplate deformations (Fennoscandian post-glacial rebound, Alpine tectonics) remain:

| Region | Residual Velocity | Cause |
|--------|-------------------|-------|
| Scandinavia (Fennoscandia) | Up to +11 mm/yr uplift | Glacial isostatic adjustment (GIA) |
| Central Europe | < 1 mm/yr | Stable plate interior |
| Mediterranean (Greece, Turkey) | 5–30 mm/yr SW | Plate boundary deformation |
| Iceland | 15–25 mm/yr WNW | Mid-Atlantic spreading |

These residuals are modeled by **EUVN** (European Vertical Reference Network) and **EPN** (EUREF Permanent GNSS Network) velocity models.

## Datum Realization

ETRS89 is realized through:

1. **EUREF Permanent GNSS Network (EPN)** — ~300 continuously operating GNSS stations across Europe.
2. **EUREF densification campaigns** — National CORS networks tied to EPN.
3. **Official transformation grids** — National NTv2 grids for converting from legacy datums (e.g., ED50, ED79, national datums).

### ETRS89 Realizations by Country

| Country | ETRS89 Realization | National EPSG Code |
|---------|-------------------|---------------------|
| Germany | ETRS89/DREF91 | EPSG:25831-25833 |
| France | RGF93 v2 | EPSG:2154 |
| UK | OSGB36 (≈ETRS89 via OSTN15 grid) | EPSG:27700 |
| Italy | ETRF2000 (RDN2008) | EPSG:6707-6709 |
| Spain | REGCAN95 (Canaries), ETRS89 (mainland) | EPSG:25829-25831 |
| Sweden | SWEREF99 | EPSG:3006-3011 |
| Norway | EUREF89 (WGS84-derived ETRS89) | EPSG:25832-25835 |

## Importance for European Geodesy

- **Official datum** for EU-wide spatial data under INSPIRE directive.
- **Cadastral basis** for land registration in most European countries.
- **CORS networks** state that their coordinates are in ETRS89.
- Transition from legacy datums (ED50, national datums) is well-documented with official grid shift files.

## Related Concepts in the European Frame

- [[GRS80]] — The underlying ellipsoid
- [[ITRF]] — The global frame ETRS89 locks to at epoch 1989.0
- [[ITRF]] — The organization maintaining ETRS89
- [[Horizontal Datum]] — The broader datum concept
- [[Helmert Transformation]] — Used to convert between ITRF realizations and ETRS89

## References
- EUREF Technical Notes: www.euref.eu
- Boucher, C., & Altamimi, Z. (2010). *ITRS, ETRS89, and Their Relationship*. IERS Technical Note.
- INSPIRE Directive (2007/2/EC) — Infrastructure for Spatial Information in the European Community.

## Related
- [[Datum]] · [[GRS80]] · [[ITRF]] · [[Horizontal Datum]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]]
