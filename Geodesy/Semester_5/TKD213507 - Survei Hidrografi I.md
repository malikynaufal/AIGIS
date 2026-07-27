# Survei Hidrografi I (*Hydrographic Survey I*)

**Kode:** TKD213507
**Sistat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Geodesi Fisis, Survei Topografi

---

## 1. Overview

Hydrographic surveying (*survei hidrografi*) is the science of measuring and describing the physical features of bodies of water, submerged lands, and related coastal areas. The primary goal is to provide data for nautical charting, dredging, construction, resource management, and hazard assessment.

The Indonesian archipelago, with >17,000 islands and >6.4 million km² of territorial waters, relies heavily on hydrographic surveys for safe navigation, resource development, and maritime administration.

---

## 2. Fundamental Principles

### 2.1 Datum — *Datum Air Laut*

Hydrographic surveys require a reference datum for depths sounding measurements.

| Datum | Description | Used In |
|-------|-------------|---------|
| **MLLW** (Mean Lower Low Water) | Semidiurnal tide minimum average | US nautical charts |
| **MHWS** (Mean High Water Springs) | Highest spring tide average | UK/IHO standard |
| **ATD** (Average Tide Level — AADT/AHL) | Average of all tidal observations | Indonesia |
| **MLW** (Lowest Water Level) | Lowest astronomical tide | Extreme low chart datum |
| **CD** (Chart Datum) | Lowest predictable tide | IHO standard |

#### Indonesian Datum — *Air Laut Indonesia*

Indonesia uses **Tidak Berpasang Surut** (non-tidal) for areas without significant tidal range, and **Air Pasang Surut** (tidal) for coastal areas. The national chart datum is based on:

- **ATD** (Average Tide Level) established at tidal gauge stations

- **Geoid** integration via satellite altimetry

### 2.2 Soundings (*Sounding*)

A sounding is a depth measurement from the water surface to the seabed:
$$

\text{Depth}_{Chart} = \text{Observed Depth} - \text{Tide Correction} + \text{Heel Correction}$$where:
-$\text{Observed Depth}$= echo sounder reading
-$\text{Tide Correction}$= difference between water surface and CD
-$\text{Heel Correction}$= ship list correction:$\delta d = d \cdot \sin\theta$for heel angle$\theta$### 2.3 Corrections Applied to Soundings

1. **Heel correction** — for ship list$$d_{corrected} = \frac{d}{\cos\theta}$$2. **Draft correction** — for ship's draft:$$d_{corrected} = d - \text{static draft}$$3. **Speed correction** — for transducer movement
4. **Temperature/sound speed correction** — via CTD cast
5. **Tide correction** — to chart datum

---

## 3. Echo Sounder (*Echo Sounder*)

### 3.1 Single-Beam Echo Sounder (SBES)

The single-beam echo sounder (SBES) transmits a single acoustic pulse vertically downward and measures the two-way travel time:$$d = \frac{c \cdot t}{2}$$where:
-$d$= depth
-$c$= speed of sound in water (~1500 m/s)
-$t$= two-way travel time

#### Single-Beam Characteristics

| Parameter | Typical Value |
|-----------|---------------|
| Beam width | 3°–12° (cone) |
| Swath width | nadir only (1 track) |
| Resolution | ~0.1% of depth |
| Accuracy | ±0.1 m or ±0.1% × depth |
| Frequency range | 20 Hz – 400 kHz |

#### Frequency vs. Resolution

| Frequency | Depth Range | Resolution |
|-----------|-------------|------------|
| 50 kHz | 0–1000 m | ~0.5% depth |
| 100 kHz | 0–500 m | ~0.2% depth |
| 200 kHz | 0–200 m | ~0.1% depth |
| 300–700 kHz | <100 m | cm-level |

### 3.2 Sound Velocity Profile (SVP)

The speed of sound in water varies with **depth**, **salinity**, and **temperature**:$$c = 1449.2 + 4.6T - 0.055T^2 + 0.00029T^3 + (1.34 - 0.01T)(S - 35) + 0.016z$$where:
-$T$= temperature (°C)
-$S$= salinity (psu)
-$z$= depth (m)

A **CTD** ( Conductivity-Temperature-Depth) cast is performed regularly to measure the SVP for ray-bending correction.

### 3.3 Ray-Bending Correction

Because sound speed varies with depth, the acoustic beam path is refracted (curved). The ray-tracing equation:$$\frac{\cos\theta(z)}{c(z)} = \text{constant}
$$

This causes systematic errors in deep water, especially with steep beam angles.

---

## 4. Bathymetric Maps (*Peta Bathymetri*)

### 4.1 Bathymetric Contours

Bathymetric charts represent underwater topography through contour lines of equal depth. Depths ($-$values) are shown with negative numbers.

Types of bathymetric representation:

- **Contour lines** — isobaths (lines of equal depth)

- **Shading** — hillshade-style illumination

- **Tinted contours** — color-filled depth ranges

- **3D surface** — perspective rendering

### 4.2 Tidal Datum in Nautical Charts

- **IHO S-4 standard** specifies minimum requirements for chart datum

- **Safety considerations:** Chart datum is set such that ~1–2% of observations fall below CD

- **Indonesian practice:** Uses **ATDL** (Air Pasang Surut Indonesia), adjusted per tidal station

### 4.3 Chart Components

A nautical chart includes:
1. **Chart datum (CD)** — reference for depths
2. **Soundings** — depth values (in meters)
3. **Safety contours** — shallowest depth shown
4. **Hatch marks** — shallow areas marked with depth values
5. **Symbols** — wrecks, rocks, buoys, obstacles
6. **Tidal diamonds** — tidal current information
7. **Sounding datum** — conversion notes

---

## 5. Survey Planning

### 5.1 Coverage Requirements$$D_{track} = 3 \cdot d \cdot \sin(\alpha_{max})$$where$d$is the depth and$\alpha_{max}$is the maximum beam angle. This ensures overlapping tracks for complete coverage.

### 5.2 Line Spacing$$s = D_{swath} - 2 \cdot \Delta$$where:
-$D_{swath}$= swath width (at depth$d$): $D_{swath} = 2d \cdot \tan(\alpha_{max})$-$\Delta$= overlap (typically 10–25%)

For IHO **Order** standards:

| Order | Coverage | Typical Use |
|-------|----------|-------------|
| Special Order | 100% coverage | Ports, harbors |
| Order 1 | 100% coverage | Approach channels |
| Order 2 | 100% coverage | Coastal approaches |
| Order 3 | 100% coverage | General coastal |
| Order 4 | 100% coverage | Area coverage |

### 5.3 Survey Specifications (IHO)

| Parameter | Special Order | Order 1 | Order 2 | Order 3 |
|-----------|---------------|---------|---------|---------|
| **Position accuracy** | ±0.5 m | ±1 m | ±5 m | ±10 m |
| **Depth accuracy** | ±0.1 m ± 1% | ±0.25 m ± 1% | ±0.5 m ± 1% | ±0.5 m ± 1% |
| **Line spacing** | 10–25 m | 50 m | 100–200 m | >200 m |

---

## 6. Equipment and Instruments

### 6.1 Primary Equipment

| Instrument | Function | Accuracy |
|-----------|----------|----------|
| Single-beam echosounder | Depth measurement | ±0.1–0.3% depth |
| Multibeam echosounder (MBES) | Swath bathymetry | ±0.01 m ± 0.1% depth |
| DGPS/RTK GNSS | Vessel positioning | ±0.02–0.5 m |
| MRU (Motion Reference Unit) | Heave, pitch, roll | ±0.01° |
| CTD | Sound speed profiling | ±0.1 m/s |
| Tide gauge | Water level measurement | ±0.01 m |
| Fathometer (deep-water) | Deep sounding | ±0.2% depth |

### 6.2 Tide Gauge

A tide gauge (*pengukur pasang surut*) measures sea surface height relative to a benchmark. Types:

- **Pressure gauge** — measures hydrostatic pressure at seabed$$P = \rho \cdot g \cdot h + P_{atm}$$- **Acoustic tide gauge** — measures water column resonant frequency

- **Radar tide gauge** — microwave reflection at water surface

- **Tide staff** — visual/manual (obsolete for precise work)

---

## 7. Data Processing Workflow

```
1. Data ingestion (raw sounding file)
   ↓
2. Tide correction (raw depth → CD)
   ↓
3. Heel correction (ship list)
   ↓
4. Sound speed correction (ray-bending)
   ↓
5. Position correction (raw → local datum)
   ↓
6. Gridding (interpolation to regular grid)
   ↓
7. Quality control (sounding removal, SDE check)
   ↓
8. Chart production (IHO S-57 / S-100)
```

### 7.1 Gridding Methods

| Method | Algorithm | Best For |
|--------|-----------|----------|
| **Inverse Distance Weighting** | IDW | Sparse data |
| **Minimum Curvature** | Splines | Smooth surfaces |
| **Natural Neighbor** | Voronoi | Irregular data |
| **Triangulation** | TIN | Contour generation |
| **Cressman/Nicolson** | Successive passes | Meteorological data |

### 7.2 Quality Control (QC) — IHO S-44

**Standard Deviation of Depth Error (SDE):**$$\text{SDE} = \sqrt{\frac{\sum_{i=1}^{n} (d_i - \bar{d})^2}{n-1}}$$where$d_i$are the difference between sounding and predicted depth from a digital terrain model.

**Requirements:**
-$\text{SDE} \leq 0.25$m for Order 1
-$\text{SDE} \leq 0.5$m for Order 2/3

---

## 8. Indonesian Hydrographic Surveying

### 8.1 Hydro-Oceanographic Office

**HO** (*Hydro-Oceanographic*) of the Indonesian Navy conducts hydrographic surveys under BHO (*Badan Hidrografi dan Oseanografi TNI AL*).

### 8.2 Nautical Chart Production

- Charts are produced per **IHO S-57** standard

- Modern transition to **S-100** — Universal Hydrographic Data Model (based on ISO 19100 family)

- **Indonesian Sailing Directions** (*Buku Petunjuk Pelayaran Indonesia*) include hydrographic notes

### 8.3 Coastal and Island Areas

| Region | Challenge | Survey Priority |
|--------|-----------|-----------------|
| **Kepulauan Riau** | Shallow waters, shipping routes | High (trade lanes) |
| **Papua/Sulawesi** | Coral reefs, shoals | High (navigation hazard) |
| **Jakarta Bay** | Dredging, ports | Very high (infrastructure) |
| **NTT/NTB** | Coral reefs, small-island navigation | Medium |

---

## 9. Key Formulas

| Quantity | Formula | Unit |
|----------|---------|------|
| Depth from sonar |$d = \frac{c \cdot t}{2}$| m |
| Sound speed (Mackenzie) |$c = 1449.2 + ...$| m/s |
| Heel correction |$d_{corr} = \frac{d}{\cos\theta}$| m |
| Swath width |$D = 2d \cdot \tan\alpha_{max}$| m |
| Tide correction |$d_{CD} = d_{raw} - \Delta tide$| m |
| Line spacing |$s = D_{swath}(1 - overlap)$ | m |

---

## References

1. IHO (2008). *Standards for Hydrographic Surveys*, 6th ed. (S-44).
2. IHO (2023). *S-57 Transfer Standard for Digital Hydrographic Data*.
3. IHO (2021). *S-100 Universal Hydrographic Data Model*.
4. Stow, D.A. (2017). *Hydrographic Surveying*. Springer.
5. Liddell, B.H. (1987). *Hydrographic Surveying*. US Naval Institute Press.
6. BIG/HO Indonesia. *Pedoman Survei Hidrografi Nasional*.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*
