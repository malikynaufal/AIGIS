---
tags: [geodesy, concept, nation, aigis]
aliases: [Indonesia, TM3, DGN95, BIG, Proyeksi Indonesia, Koordinat Indonesia]
created: 2026-07-12
updated: 2026-07-27
---

# 🇮🇩 Indonesia — Proyeksi Geospasial

Indonesia is a large archipelago spanning longitudes 95°E to 141°E, making it a challenging case for map projection and geodetic reference frames. Indonesia has its own national geodetic datum, official projection systems, and authoritative mapping agency.

## Official Datum: DGN95

**DGN95** (Datum Geodesi Nasional 1995) is Indonesia's official geodetic datum:

| Property | Value |
|----------|-------|
| **Ellipsoid** | WGS84 (identical) |
| **Origin** | Geocentric (tied to IGS/ITRF) |
| **Epoch** | 2000.0 (approx.) |
| **CORS network** | CORS-Indonesia (~60 stations) |
| **Agency** | BIG (Badan Informasi Geospasial) |

DGN95 is practically identical to WGS84(G2296) at the centimeter level. CORS-Indonesia stations provide real-time GNSS coverage for high-accuracy surveying across the archipelago.

## Regional Datums and Historical Datums

Before DGN95 was adopted in 1995, Indonesia used several legacy datums:

| Datum | Period | Ellipsoid | Origin | Notes |
|-------|--------|-----------|--------|-------|
| **Sistem Datum Nasional (SND)** | 1920–1980s | Bessel 1841 | Batavia (Jakarta) | Japanese military survey legacy |
| **SND-18/IB** | 1950s–1980s | Bessel 1841 | Local triangulation | Post-independence adjustment |
| **IDGN (Indonesia Datum Geodetic Nasional)** | 1980s | Modified Everest / local | Javanese datum | Transition to geocentric |
| **DGN95** | 1997–present | WGS84 | Geocentric | Current standard |

### Why a Local Datum Was Replaced

The pre-DGN95 local datums (e.g., Bessel-based) were not geocentric, creating systematic offsets of **5–100 m** across the archipelago when converting to WGS84. The adoption of DGN95 eliminated this problem and aligned Indonesia with international standards.

## BIG — Badan Informasi Geospasial

**BIG** (Geospatial Information Agency) is Indonesia's authoritative body for geospatial data, standards, and policy:

| BIG Function | Details |
|--------------|---------|
| **Geospatial standards** | Defines CRS, projections, datum, reference systems |
| **DGN95 management** | Maintains and updates the national datum |
| **CORS-Indonesia** | Operates ~60 continuous GNSS stations across the archipelago |
| **Geoid model** | GeoidINDO (geoid model for Indonesia based on EGM2008 adapted to regional gravity) |
| **Base maps** | Rupabumi dasar (1:50,000), thematic maps |
| **Licensing** | Regulates geospatial data access (UU No. 27/2022 on Spatial Information) |
| **Perpres 9/2016** | Spatial reference framework and implementation |

### BIG's National Reference Frame

BIG maintains:

- The official coordinate system: DGN95 in WGS84

- Grid system: TM3° (UTM-based 3° Transverse Mercator strips)

- Height system: Orthometric heights using the GeoidINDO geoid model

- Gravity network: National gravity measurement network

## Indonesia's Projection System: TM3°

Indonesia uses the **TM3°** (3-degree Transverse Mercator) system as its primary cadastral and mapping projection:

| TM3° Strip | Central Meridian | Strip Number | Coverage |
|------------|------------------|--------------|----------|
| 1 | 93°E | 1 | Western Sumatra |
| 2 | 96°E | 2 | Riau |
| 3 | 99°E | 3 | West Java |
| 4 | 102°E | 4 | Central Java |
| 5 | 105°E | 5 | East Java |
| 6 | 108°E | 6 | Banten/Sulawesi |
| 7 | 111°E | 7 | Kalimantan |
| 8 | 114°E | 8 | Sulawesi |
| 9 | 117°E | 9 | Eastern Indonesia |
| 10 | 120°E | 10 | Papua West |
| 11 | 123°E | 11 | Papua |
| 12 | 126°E | 12 | Maluku |
| 13 | 129°E | 13 | Maluku East |
| 14 | 132°E | 14 | Papua East |
| 15 | 135°E | 15 | Indonesia extreme east |

| TM3° Parameter | Value |
|----------------|-------|
| Zone width | 3° longitude |
| Scale factor $k_0$ | 0.9995 |
| False easting $E_0$ | 500,000 m |
| False northing $N_0$ | 0 m (N) / 10,000,000 m (S) |
| Ellipsoid | WGS84 / GRS80 |
| Grid origin | Central meridian intersection at equator |

### Comparison: TM3° vs. UTM 6° Zones Over Indonesia

| Property | TM3° (Indonesian) | UTM (6° zones) |
|----------|---------------------|------------------|
| Max distortion at edge | +0.016% | +0.040% |
| Number of zones for Indonesia | 15 strips | 5 zones (48–52) |
| Distortion at zone edge | 0.016% | 0.040% |
| Best for | Cadastral, engineering | General mapping |

## Reference Frame Status

Indonesia is transitioning its geospatial reference frame:

| Aspect | Status |
|--------|--------|
| **Horizontal** | DGN95 (WGS84-based), tied to IGS |
| **Height** | Orthometric (using GeoidINDO, based on EGM2008 + regional gravity) |
| **Vertical datum** | Indonesia Mean Sea Level (Pasang Surut Jakarta) |
| **CORS network** | CORS-Indonesia (~60 stations online, real-time data) |
| **Gravity network** | BIG gravity measurements for geoid model |

### Indonesia's Geoid Model

The **GeoidINDO** model (developed by BIG) provides geoid undulations $N $adapted to Indonesian regional gravity data. In practice, Indonesia often uses EGM2008 with local refinement:

| Model | Accuracy (Indonesia) | Coverage |
|-------|-----------------------|----------|
| EGM2008 (global) | ±10–30 cm over Indonesia | Global |
| EGM2008 + regional gravity | ±2–5 cm over Indonesia | Enhanced |
| GeoidINDO (BIG, in development) | Target < 5 cm | Indonesia |

## Worked Example: DGN95 Conversion

**Problem:** Convert a legacy Bessel-1861 point (pre-DGN95) to DGN95.

**Given:**
Legacy:$\phi_{Bessel} = -6.20^\circ$, $\lambda_{Bessel} = 106.85^\circ$(Jakarta area)

**Approach:**
1. Apply a 7-parameter Helmert transformation (Bessel → WGS84):
 -$T_x = -347 $m,$T_y = 213 $m,$T_z = -104 $m (approximate for Jakarta region)
 -$s = -1.5 \times 10^{-6} $(1.5 ppm)
 -$R_x = -6.5″, R_y = 5.3″, R_z = -2.1″$2. Convert Bessel geodetic → Bessel ECEF.
3. Apply Helmert → WGS84 ECEF.
4. Convert WGS84 ECEF → WGS84 geodetic = DGN95 coordinates.

**Typical result:** Legacy → DGN95 shift is$20$–$100$ m depending on location, consistent with the datum offset history.

## Practical Implications for Indonesian Geodesy

1. **New surveys** should always use DGN95 (WGS84) + TM3° for cadastral work.
2. **Legacy data** (pre-1995) in local datums needs transformation (grid or Helmert) before integration.
3. **BIG guidelines** define the official procedures — always follow BIG standards.
4. **CORS-Indonesia** provides free RTK corrections for DGN95 — any surveyor with a GNSS receiver can achieve cm-level accuracy on DGN95.
5. Indonesia has adopted the **Indonesia Spatial Reference System** (SRN Indonesia) as the official spatial reference framework since UU No. 27/2022 on Spatial Information.

## SIG (GIS) in Indonesian Geodesy

| GIS Application | Geodesy Role |
|-----------------|--------------|
| **BIG Geospatial Portal** | Official national maps and spatial data |
| **CORS monitoring** | DGN95 reference station status |
| **Cadastral SIG** | Land registration in DGN95/TM3° |
| **Topographic mapping** | BIG topographic maps use TM3° projection |
| **Disaster management** | Flood/inundation mapping referencing orthometric heights |

## References

- BIG (Badan Informasi Geospasial). www.big.go.id

- Perpres No. 9 Tahun 2016 tentang Penetapan Peraturan Pemerintah Pengganti UU No. 2 Tahun 2021 tentang Cipta Kerja menjadi Undang-Undang (Spatial Information).

- UU No. 27/2022 tentang Informasi Spasial.

- NGA. EGM2008 documentation and grid files.

## Related

- [[DGN95]] · [[TM3°]] · [[UTM]] · [[Transverse Mercator]] · [[Big (Indonesia)]] · [[Geodesy MOC]] · [[SIG]]

➡️ [[Geodesy MOC]] · [[Kurikulum Teknik Geodesi]]
