---
tags: [geodesy, concept, reference-system, aigis]
aliases: [Datum, Geodetic Datum, Datum Geodesi]
created: 2026-07-12
updated: 2026-07-27
---

# 🌐 Geodetic Datum

A **geodetic datum** defines the relationship between a mathematical model (the [[Reference Ellipsoid]]) and the physical Earth. It specifies:
1. The **ellipsoid parameters** (size and shape),
2. The **orientation and position** of the ellipsoid relative to the Earth.

Changing the datum can shift coordinates by **tens of metres** — making datum knowledge essential for all geospatial work.

> **Indonesian term:** *Datum Geodesi*

---

## 1. Types of Datums

### 1.1. Local (Regional / Classic) Datums

A local datum minimises residuals over a limited area:

| Datum | Ellipsoid | Origin | Area | Accuracy |
|-------|-----------|--------|------|----------|
| **NAD27** | Clarke 1866 | Meades Ranch, Kansas (39°13'N, 98°32'W) | North America | ~10 m |
| **SAD69** | GRS67 | South American Geocentric Datum | South America + Indonesia | ~5–10 m |
| **ED50** | Hayford 1909 | Herstmonceux, UK | Western Europe | ~10 m |
| **ID74** | GRS67 | Centre of figure | Indonesia | ~10–20 m |
| **Tokyo** | Bessel 1841 | Tokyo Astronomical Observatory | Japan, SE Asia | ~10–30 m |
| **Batavia** | Bessel 1841 | Batavia (Jakarta) | Indonesia (legacy) | ~20–50 m |

### 1.2. Global (Geocentric) Datums

A global datum has the ellipsoid centre coinciding with Earth's centre of mass (geocentre):

| Datum | Ellipsoid | Origin | Frame |
|-------|-----------|--------|-------|
| **WGS84** | WGS84 | Earth geocentre | Co‑aligned with [[ITRF]] to ~10 cm |
| **ITRF2020** | [[GRS80]] (or WGS84) | Earth geocentre (realised by VLBI+SLR+GNSS+DORIS) | ITRF2020, epoch 2015.0 |
| **ETRS89** | GRS80 | European Terrestrial Frame (co‑moving with Eurasian plate) | ETRF2014 |
| **NAD83(2011)** | GRS80 | N. American plate frame | NRAT14 |
| **GDA2020** | GRS80 | Australian plate frame | AGFS2014 |
| **DGN95** | WGS84 | Geocentre (aligned with WGS84) | 1995 epoch (approx ITRF91) |

---

## 2. Geodetic vs Geocentric Datum

| Aspect | Local Datum | Global Datum |
|--------|-------------|--------------|
| Ellipsoid position | "Best fit" over region | Centred at Earth's mass centre |
| Orientation | Defined by 1–3 datum points | Defined by global geodetic techniques |
| Accuracy in region | Good locally | Good everywhere |
| Accuracy elsewhere | Poor | Good everywhere |
| Example | SAD69, NAD27, Batavia | WGS84, ITRF2020 |
| Used today | Legacy maps | All GNSS work |

---

## 3. Indonesian Datum History

| Datum/Frame | Epoch | Ellipsoid | Realisation |
|-------------|-------|-----------|-------------|
| **Batavia** | Pre‑1900 | Bessel 1841 | 5 triangulation stations |
| **ID74** | 1974 | GRS67 | Centroid of Indonesian triangulation network |
| **DGN95** | 1995 | WGS84 | Aligned to ITRF91; used for national mapping |
| **DGN95/ITRF97** | ~2000 | WGS84 | Updated realisation using CORS |
| **IGD (Indonesian Geodetic Datum)** | 2020+ | WGS84 | ITRF2014 at epoch 2020.0; active modernisation by BIG |

> All current GNSS work in Indonesia produces coordinates in **ITRF/WGS84**.

---

## 4. ITRF Realisations

The [[ITRF]] is maintained by the IERS and consists of successive realisations, each incorporating more precise observations:

| Realisation | Epoch | Techniques | Improvement over prior |
|-------------|-------|------------|------------------------|
| ITRF88 | 1988 | VLBI, SLR, LLR | First global frame |
| ITRF91 | 1988 | + DORIS | Improved |
| ITRF93 | 1988 | + GPS | Improved |
| ITRF94 | 1994 | Refined combinations | Improved |
| ITRF96 | 1994 | Improved modelling | Improved |
| ITRF97 | 1997 | + better troposphere models | Improved |
| ITRF2000 | 2000 | Station network growth | ~5 mm global |
| ITRF2005 | 2000 | + improved combination strategy | ~3 mm global |
| ITRF2008 | 2005 | Improved frame quality | ~3 mm global |
| ITRF2014 | 2010 | Nonlinear station motions modelled | ~2 mm global |
| **ITRF2020** | 2015 | + higher‑order ionosphere, improved troposphere | **~1–2 mm global** |

---

## 5. Datum Transformation (between local and global)

To convert coordinates from a local datum to WGS84/ITRF:

1. **Helmert transformation** (see [[Helmert Transformation]]) — uses 3+4=7 parameters.
2. **Grid‑based shifts** — NTv2, NADCON, ETRS89 grids (see [[PROJ]]).
3. **Direct datum points** — use the defining stations of the local datum.

### Example: SAD69 → WGS84 (Epicentre Helmert)

$$T_x = +66.87 \;\text{m},\; T_y = -4.37 \;\text{m},\; T_z = +38.52 \;\text{m}$$
$$\omega_x = \omega_y = \omega_z = 0,\quad s = -0.27\;\text{ppm}$$

For a point in Jakarta ($\varphi = -6.2°$):
$$\Delta X \approx 66.87,\; \Delta Y \approx -4.37,\; \Delta Z \approx 38.52\;\text{m}$$

**Residuals** after the 7‑parameter fit may reach 5–10 m across Indonesia.

---

## 6. Practical Implications

| Scenario | Datum issue | Solution |
|----------|------------|----------|
| Overlay old map on GNSS point | Offsets 10–100 m | Use published datum transformation parameters |
| Building coordinates in WGS84 vs UTM | Same datum, different projection | Apply projection formulas (see [[Map Projection]]) |
| GNSS‑derived orthometric heights | $h = H + N$; need datum‑consistent geoid model | Use IGS/WGS84 geoid undulation |
| Historical land titles | Referenced to Batavia or ID74 | Apply Helmert conversion |

---

## 7. Related

- [[Reference Ellipsoid]] – the ellipsoid chosen for a datum.
- [[ITRF]] – the global datum standard.
- [[Helmert Transformation]] – converting between datums.
- [[DGN95]] – Indonesia's current official datum.
- [[WGS84]] – GPS global datum.
- [[Geodetic Coordinates]] – coordinates defined relative to the datum's ellipsoid.

---

## 8. References

- Boucher, C., Altamimi, Z., *Memo: Specifications for Reference Frame Fixing in the Analysis of a EUREF Campaign*, EUREF, 1991.
- Bock, Y. & Gardner, L., *From NAD27 to NAD83: The Transition Between Datum Transformations*, Surveying and Land Information Systems 1992.
- Altamimi, Z., Rebischung, P., Métivier, L., Collilieux, X., *ITRF2014: A New Release of the ITRF*, JGR Solid Earth, 2016.
- BIG Indonesia, *Pedoman Datum Referensi Spasial Indonesia*, 2022.
- NGA, *World Geodetic System 1984 (WGS‑84)*, NGA.STND.0036_2.0.0_WGS84, 2024.
- EPSG Guidance Note 7‑2, *Coordinate Reference Systems*, IOGP, 2024.

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]