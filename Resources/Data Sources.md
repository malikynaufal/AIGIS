# 🌐 Geodesy Data Sources

*Curated list of publicly accessible geodetic data products, organised by service/agency.*

---

## 1. International GNSS Service (IGS)

| Product | Format | Cadence | Precision | Link |
|---------|--------|---------|-----------|------|
| **Final orbits** | SP3, CLK | 2-week delay | ~1.5 cm | https://cddis.nasa.gov/ |
| **Rapid orbits** | SP3, CLK | ~18 h delay | ~3 cm | https://cddis.nasa.gov/ |
| **Ultra-rapid orbits** | SP3, CLK | 3 h latency | ~5 cm | https://cddis.nasa.gov/ |
| **Real-time orbits** | RTCM SSR | ~5 s | ~5 cm | https://igs.bkg.bund.de/ |
| **Ionosphere maps (GIM)** | IONEX | Daily | 2–5 TECU | https://cddis.nasa.gov/ |
| **Antenna calibrations** | ANTEX | Update | — | https://igs.org/ |
| **Station coordinates + velocity** | SNX | Yearly | 1–2 mm | https://igs.org/ |

IGS Website: https://igs.org/

---

## 2. IERS Products

| Product | Description | Link |
|---------|-------------|------|
| **ITRF2020 coordinates + velocities** | 1800+ station positions | https://itrf.ign.fr/en/solutions/ |
| **EOP (Earth Orientation Parameters)** | $x_p, y_p, UT1-UTC, LOD | https://datacenter.iers.org/ |
| **IERS Conventions 2010** | Tidal models, atmosphere models | https://www.iers.org/ |
| **IGS realizations** | Annual solution SINEX | https://itrf.ign.fr/ |

---

## 3. NOAA/NGS (USA)

| Product | Description | Link |
|---------|-------------|------|
| **CORS (Continuously Operating Reference Station)** | ~3000 USA stations | https://www.ngs.noaa.gov/CORS/ |
| **OPUS** | Online PPP processing | https://www.ngs.noaa.gov/OPUS/ |
| **GEOID12B** | USA geoid model (1-arcmin) | https://www.ngs.noaa.gov/GEOID12B/ |
| **NAD83 coordinates** | CORS positions + transforms | https://www.ngs.noaa.gov/ |
| **NADCON5** | Datum conversion grids | https://www.ngs.noaa.gov/ |

---

## 4. BIG Indonesia (Badan Informasi Geospasial)

| Product | Description | Link |
|---------|-------------|------|
| **CORS-ID** | Indonesian reference stations | https://cors.big.go.id/ |
| **NTRIP caster** | Real-time corrections | cors.big.go.id:2101 (RTCM 3.x) |
| **IDGeoid2020** | National geoid model | https://tanahair.indonesia.go.id/ |
| **Peta dasar 1:50,000** | Topographic base maps | https://tanahair.indonesia.go.id/ |
| **TM-3° EPSG codes** | Projection parameters for Indonesia | https://epsg.org/ (EPSG:32748-32754) |
| **Jaringan Kontrol** | Orde 0-3 control points | https://tanahair.indonesia.go.id/ |

---

## 5. LAPAN / BRIN (Indonesia)

| Product | Description | Link |
|---------|-------------|------|
| **LAPAN-A2 / A3** | Indonesian Earth observation satellites | https://www.brin.go.id/ |
| **Citra Satelit Nasional** | Domestic satellite imagery | https://indahai.brin.go.id/ |
| **Indonesia EOX** | Sentinel-2 processed for Indonesia | Various regional portals |

---

## 6. Gravity Data

| Product | Description | Source | Link |
|---------|-------------|--------|------|
| **EGM2008** | Global geoid (degree 2190) | NGA/USA | https://earth-info.nga.mil/ |
| **EGM96** | Legacy global geoid | NGA/NASA | https://earth-info.nga.mil/ |
| **GRACE/GRACE-FO** | Time-varying gravity field | NASA/DLR | https://podaac.jpl.nasa.gov/ |
| **GOCE** | Static gravity gradients | ESA | https://earth.esa.int/ |
| **ICGEM** | IAG gravity field model service | GFZ | http://icgem.gfz-potsdam.de/ |
| **SRTM** | 30m DEM (near-global) | NASA | https://earthexplorer.usgs.gov/ |

---

## 7. Atmospheric Data

| Product | Description | Source | Link |
|---------|-------------|--------|------|
| **ECMWF weather data** | Troposphere + tide | ECMWF | https://www.ecmwf.int/ |
| **NCEP/NCAR reanalysis** | Global weather model | NOAA | https://www.esrl.noaa.gov/ |
| **IGS troposphere** | Zenith delay products | IGS | https://igs.org/ |
| **IONEX maps** | Global ionosphere (GIM) | CODE, JPL, IGS | https://ftp.aiub.unibe.ch/ |

---

## 8. Tide and Sea Level

| Product | Description | Source | Link |
|---------|-------------|--------|------|
| **FES2014** | Global ocean tide model | LEGOS/Toulouse | https://www.aviso.altimetry.fr/ |
| **GOT4.8** | Global ocean tide model | GSFC | https://podaac.jpl.nasa.gov/ |
| **TPXO9** | Global ocean tide model | Oregon State | https://volkov.oce.orst.edu/tides/global.html |
| **Sea Level Change** | Satellite altimetry MSL | NASA JPL | https://sealevel.nasa.gov/ |
| **NOAA Tides & Currents** | USA tide gauge data | NOAA | https://tidesandcurrents.noaa.gov/ |

---

## 9. Satellite / Altimetry

| Product | Description | Source | Link |
|---------|-------------|--------|------|
| **Sentinel-6** | Altimetry SSH | ESA/NASA | https://sentinel.esa.int/ |
| **Sentinel-1** | SAR for InSAR | ESA | https://scihub.copernicus.eu/ |
| **Sentinel-2** | Multi-spectral EO | ESA | https://sentinel.esa.int/ |
| **ALOS (PALSAR/JASM)** | Japanese SAR/optical | JAXA | https://www.eorc.jaxa.jp/ALOS/ |
| **ASTER GDEM** | Global DEM 30m | NASA/JAXA | https://earthdata.nasa.gov/ |

---

## 10. Indonesia-Specific Data Portals

| Portal | Description | URL |
|--------|-------------|-----|
| **BIG Tanah Air** | National geospatial data | https://tanahair.indonesia.go.id/ |
| **CORS-ID** | GNSS reference stations | https://cors.big.go.id/ |
| **Kementerian ATR/BPN** | Land administration | https://atrbpn.go.id/ |
| **BMKG** | Meteorological data | https://data.bmkg.go.id/ |
| **BPBD** | Disaster data | https://bpbd.go.id/ |

---

## 11. References

- IGS Products, https://igs.org/products/
- ITRF Solutions, https://itrf.ign.fr/en/solutions/
- NGS Educational Resources, https://geodesy.noaa.gov/INFO/
- BIG Indonesia, https://tanahair.indonesia.go.id/
- IERS Products and Services, https://datacenter.iers.org/

➡️ [[Resources]] · [[Geodesy MOC]]