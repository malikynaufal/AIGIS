# 🛠️ GNSS Software Resources

*A comprehensive listing of software tools for GNSS data processing, analysis, and applications. Organised by licence type and capability.*

---

## 1. Open Source / Free Software

| Software | Description | Developer | Key Capabilities | License |
|----------|-------------|-----------|------------------|---------|
| **RTKLIB** (RTKLib v2.4.3) | Real-time kinematic + PPP post-processing | T. Takasu | RTK, PPP, post-processing, IGS support | BSD-2 |
| **gLAB** | GNSS analysis and processing | UPC/IEEE | PPP, multi-GNSS, single/dual freq, education | GPL |
| **GNSS-SDR** | Software-defined GNSS receiver | CTTC | Signal processing, all constellations | GPL |
| **BNC** (BKG NTRIP Client) | Real-time data collection and streaming | BKG | NTRIP client, RTCM decoder, SSR | Free |
| **GPStk** (The GPS Toolkit) | C++ libraries for GNSS | UT Austin | RINEX, positioning, navigation | LGPL |
| **GRAND** (The GNSS DAta Tool) | High-precision GNSS analysis | TUGraz | PPP, SNN, post-processing | GPL |
| **NKL** (Net-based Kinematic Library) | Network RTK, VRS | BKG | Network RTK, datum conversion | Free |
| **RINEX Utilities** | RINEX format tools | GFZ, NASA, IGS | Data conversion, quality control | Free |

## 2. Academic / Research Software

| Software | Description | Developer | Key Capabilities | Access |
|----------|-------------|-----------|------------------|--------|
| **Bernese GNSS Software** | High-precision processing | AIUB | PPP, network, campaigns, iono, DORIS | Commercial (free for research) |
| **GIPSY-OASIS** | PPP and orbit determination | NASA/JPL | PPP, PPP-AR, orbit/clock, GRACE | Commercial/research |
| **GipsyX** | PPP (successor to GIPSY) | NASA/JPL | PPP-AR, multi-GNSS, real-time | Research licence |
| **Gaia** | GNSS-based precise positioning | NRCan | PPP, geoid, Canadian reference | Free for Canadian govt. |
| **PANDA** (Position And Navigation Data Analyst) | High-precision GNSS | WHU (Wuhan) | PPP, global network, LEO orbit | Research |

## 3. Commercial Software

| Software | Description | Developer | Key Capabilities | Licence Cost |
|----------|-------------|-----------|------------------|--------------|
| **Trimble Business Center (TBC)** | Full survey processing | Trimble | GNSS, total station, photogrammetry | $3,000-8,000 |
| **Leica Infinity** | Survey office software | Leica Geo | GNSS, total station, levelling, cloud | €2,000-6,000 |
| **Topcon Magnet Office** | Processing suite | Topcon | GNSS, total, UAV | $2,000-5,000 |
| **NovAtel Waypoint** | Post-processing | NovAtel/Grafnav | Inertial + GNSS, PPP | $5,000-15,000 |
| **Bernese GNSS** (commercial) | High-precision | AIUB | Dense network, campaigns | CHF 5,000-20,000 |
| **GAMIT/GLOBK** | GPS processing | MIT/SIO | Regional networks, campaigns | Free (research) |
| **Pix4Dmatic/ Mapper** | Photogrammetry | Pix4D | UAV processing, DM, orthophoto | €2,500-8,000 |
| **Agisoft Metashape** | Photogrammetry | Agisoft | UAV processing, 3D models | $179-3,499 |

## 4. GNSS Data Quality Tools

| Tool | Description | Developer | Key Capabilities | License |
|------|-------------|-----------|------------------|---------|
| **TeQC** (Translation, Editing, and Quality Check) | RINEX quality analysis | UNAVCO | Data quality, cycle slip detection, multipath | GPL |
| **gfzrnx** (GFZ RINEX Toolkit) | RINEX manipulation | GFZ | Editing, check, reformatting | Free |
| **BNC Quality Monitor** | Real-time quality assessment | BKG | RTCM, SSR, latency | Free |
| **RINEX-check** | Quality metrics | various | Multipath, SNR, cycle slips | Free |

## 5. Online Processing Services

| Service | Description | Provider | Key Capabilities | Access |
|---------|-------------|----------|------------------|--------|
| **AUSPOS** | Online GPS processing | Geoscience Australia | Single-base, global | Free |
| **OPUS** | Online Positioning User Service | NOAA/NGS | Static GPS PPP (NAD83, ITRF) | Free |
| **SCOUT** | Static GPS PPP | NASA/JPL | PPP, any epoch | Free |
| **e-GAP** | Online PPP processing | Geoscience Australia | Real-time PPP | Free |
| **CSRS-PPP** | Canadian Spatial Reference System | NRCan | PPP, ITRF/NAD83 | Free |
| **MagicGNSS** | Cloud processing | GMV | PPP, RTK, network, SV | Free (basic) |
| **Trimble RTX** | Real-time satellite corrections | Trimble | Real-time PPP (cm) | Subscription |

## 6. Tools for Indonesia-Specific Work

| Tool | Use Case | Notes |
|------|----------|-------|
| **CORS-ID NTRIP** | Real-time corrections from BIG | cors.big.go.id:2101 |
| **PROJ / GDAL** | Projection conversion (TM-3°, UTM, WGS84) | Use EPSG codes 32748-32754 |
| **IDGeoid2020** | Geoid undulation for Indonesia | Contact BIG for model download |
| **RTKLIB** | Field RTK work with Indonesian CORS | Configurable NTRIP client |
| **QGIS + Geoid Plugin** | National geoid + GNSS height conversion | Open-source |

## 7. IGS Product Download

| Product | Format | Source |
|---------|--------|--------|
| Final orbits | SP3 (.sp3) | https://cddis.nasa.gov/archive/gps/data/ |
| Rapid orbits | SP3 (.sp3) | ftp://igs.ensg.ign.fr/pub/igs/products/ |
| Real-time orbits (SSR) | RTCM SSR | https://igs.bkg.bund.de/ntrip/ |
| Satellite clocks | RINEX CLK (.clk) | https://cddis.nasa.gov/archive/gps/products/ |
| Ionosphere maps | IONEX (.ion) | https://ftp.aiub.unibe.ch/CODE/ |

## 8. References

- Takasu, T., *RTKLIB: An Open Source Program Package for GNSS Positioning*, 2013. https://rtklib.com/

- IGS Central Bureau, *Products and Services*, https://igs.org/products/

- Hesselbarth, A., *BNC — BKG NTRIP Client*, https://igs.bkg.bund.de/ntrip/

- NRCan, *CSRS-PPP*, https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php

➡️ [[Resources]] · [[Geodesy MOC]]