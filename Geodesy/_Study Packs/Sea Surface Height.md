---
tags: [geodesy, study-pack, sea-surface, altimetry, oceanography, mean-sea-level]
aliases: [Sea Surface Height, SSH, Tinggi Permukaan Laut]
created: 2026-07-27
---

# Sea Surface Height (Tinggi Permukaan Laut / SSH)

> **Comprehensive Study Pack** — From mean sea level to geocentric sea surface, satellite altimetry missions, ocean circulation, and applications in geodesy and oceanography.

---

## 📋 Overview

**Sea Surface Height (SSH)** is the distance from a reference ellipsoid (or geoid) to the instantaneous sea surface, measured along the radial direction. Understanding SSH is critical for geodesy (geoid determination), oceanography (circulation, sea level rise), and climate science.

**Key Indonesian Context**: Indonesia archipelago with ~108,000 km coastline needs SSH monitoring for coastal zone management, tsunami warning, sea level rise adaptation, and nautical charting.

---

## 🌊 Mean Sea Level (MSL) vs. Sea Surface Height (SSH)

| Quantity | Symbol | Definition | Reference Surface |
|----------|--------|------------|-------------------|
| **Mean Sea Level** | MSL | Time-averaged sea surface (typically over 19 years, e.g., 1983–2001 epoch) | Usually treated as geoid proxy locally |
| **Sea Surface Height** | SSH | Instantaneous height of sea surface above reference | Ellipsoid (altimetry) or geoid |
| **Mean Dynamic Topography** | MDT | $MDT = \overline{SSH} - N $ (mean SSH minus geoid) | Geoid → Ellipsoid |
| **Sea Surface Topography** | SST | Dynamic topography relative to geoid (same as MDT) | Geoid |
| **Absolute Dynamic Topography** | ADT | SSH relative to geoid in absolute (geocentric) frame | Geoid (ITRF-referenced) |

### Fundamental Relations

$$ SSH = h_{\text{sat}} - \rho_{\text{radar}} - \text{corrections}\overline{SSH} = N + MDT = N + SSTADT = SSH - N $$ Where:
-$h_{\text{sat}}$ = satellite altitude above reference ellipsoid (from orbit)
-$\rho_{\text{radar}} $= radar range from satellite to sea surface
-$N$ = [[Geoid Undulation]]
-$MDT$ = Mean Dynamic Topography (dynamic ocean topography)
-$ADT$ = Absolute Dynamic Topography

---

## 🔭 Satellite Altimetry Fundamentals (Dasar Altimetri Satelit)

### Measurement Principl
e

$$\rho = \frac{c \cdot \Delta t}{2} $$ The radar altimeter on a satellite transmits a microwave pulse downward and measures the two-way travel time $\Delta t $. The sea surface height is then:

$$ SSH_{\text{altimetry}} = h_{\text{orbit}} - \rho - \text{dry tropo} - \text{wet tropo} - \text{ionosphere} - \text{sea state bias (SSB)} + \text{solid Earth tide} + \text{ocean tide} $$

### Key Corrections in Altimetry

| Correction | Source | Typical Magnitude |
|------------|--------|-------------------|
| **Wet tropospheric** | Radiometer on altimeter | 5–40 cm |
| **Dry tropospheric** | ECMWF model | 2–2.5 m |
| **Ionospheric** | Dual-frequency altimeter or model (GIM) | 2–20 cm |
| **Sea State Bias (SSB)** | Empirical model (wind speed, SWH) | 2–20 cm |
| **Solid Earth tide** | Theoretical model | ±0.5 m |
| **Ocean tide** | Model (FES2014, TPXO) | 0–2 m (tropical) |
| **Inverse barometer** | Atmospheric pressure | ±0.5 m |
| **Pole tide** | Earth rotation model | cm |
| **Atmospheric loading** | Pressure model | cm |

### Altimeter Range Equatio
n

$$ \rho_{\text{corrected}} = \rho_{\text{raw}} + \delta\rho_{\text{wet}} + \delta\rho_{\text{dry}} + \delta\rho_{\text{iono}} + \delta\rho_{\text{SSB}} - \delta\rho_{\text{tide}} - \delta\rho_{\text{solid}} $$

---

## 🛰️ Major Satellite Altimetry Missions

### Jason Series (CNES/NASA)
| Mission | Launch | Orbit | Repeat | Accuracy | Contribution |
|---------|--------|-------|--------|----------|--------------|
| **TOPEX/Poseidon** | 1992 | 1336 km, 66° | 10 days | 4.2 cm | First dedicated ocean altimetry mission |
| **Jason-1** | 2001 | 1336 km, 66° | 10 days | 3.3 cm | Continuation of TOPEX record |
| **Jason-2 (OSTM)** | 2008 | 1336 km, 66° | 10 days | 3.1 cm | Improved accuracy |
| **Jason-3** | 2016 | 1336 km, 66° | 10 days | 2.5 cm | Operational, reference mission |
| **Jason-CS / Sentinel-6 Michael Freilich** | 2020 | 1336 km, 66° | 10 days | 2.0 cm | Current reference mission |

### Sentinel-3 (ESA)
| Mission | Launch | Orbit | Repeat | Accuracy | Instrument |
|---------|--------|-------|--------|----------|------------|
| **Sentinel-3A** | 2016 | 814 km, 98.65° | 27 days | 4.0 cm | SRAL (SAR altimeter) |
| **Sentinel-3B** | 2018 | 814 km, 98.65° | 27 days | 4.0 cm | SRAL (SAR altimeter) |
| **Sentinel-3C** | 2024 | 814 km, 98.65° | 27 days | 3.5 cm | SRAL (improved) |

### Other Key Missions
| Mission | Type | Key Contribution |
|---------|------|------------------|
| **CryoSat-2** | Radar altimeter (SAR) | Sea ice thickness, coastal altimetry |
| **SARAL/AltiKa** | Ka-band altimeter | Higher resolution, coastal zone |
| **HY-2A/B/C** | Radar altimeter (Chinese) | Global ocean monitoring |
| **ICESat-2** | Laser altimeter (Lidar) | Sea ice, land ice, land elevation |
| **SWOT** (Surface Water Ocean Topography) | Ka-band interferometry | 2D SSH mapping, rivers, lakes, coast |
| **CFOSat** | Scatterometer + altimeter | Wind/wave + SSH |
| **HY-2D** | Radar altimeter | Ocean monitoring |

### Mission Orbit Geometr
y

$$\text{Repeat period} = \frac{\text{orbital period}}{N_{\text{rev}} - N_{\text{nodal}}} $$ Jason-type orbits:$ i \approx 66°$→ covers ocean between $\pm 66°$ latitude.
Sentinel-3 orbits: $ i \approx 98.65°$ (sun-synchronous) → global coverage including polar.

---

## 🌀 Mean Sea Level & Sea Level Rise (Tinggi Laut Rata-Rata & Kenaikan MSL)

### Global Mean Sea Level (GMSL)

- **Rate**: $\sim 3.7 \pm 0.5 \text{ mm/year} $ (2006–2018, IPCC AR6)

- **Acceleration**: $\sim 0.084 \pm 0.025 \text{ mm/year}^2 $- **Contribution breakdown (2006–2018)**:
 - Thermal expansion: $1.4 \text{ mm/yr}$(38%)
 - Glaciers: $0.6 \text{ mm/yr}$(17%)
 - Greenland: $0.7 \text{ mm/yr}$(20%)
 - Antarctica: $0.4 \text{ mm/yr}$(11%)
 - Land water storage: $0.3 \text{ mm/yr}$(8%)

### Regional Variation
s

$$\text{SSH}_{\text{regional}} = \text{GMSL} + \text{regional trends} + \text{interannual variability} $$ Regional variations (not uniform) due to:

- Ocean circulation changes (ENSO, PDO, AMO)

- Glacial Isostatic Adjustment (GIA)

- Land subsidence/uplift

- Gravitational effects of ice mass loss

- Wind and atmospheric pressure patterns

### Indonesia Sea Level Context
| Indicator | Value |
|-----------|-------|
| **Trend (Indonesia waters)** | $\sim 3.5–5.0 \text{ mm/year} $ |
| **Dominant driver** | Thermal expansion + ocean heat content |
| **Critical areas** | Jakarta (subsidence + sea level rise), small islands |
| **Impact** | Coastal flooding, saltwater intrusion, infrastructure risk |

---

## 🔄 Sea Surface Topography & Ocean Circulation

### Mean Dynamic Topography (MDT
)

$$ MDT = \overline{SSH} - N $$

-$N $from geoid model (e.g., EGM2008, GOCE)
-$\overline{SSH} $ from altimetry (multi-year mean)

- MDT $\sim $ 0 to 1.5 m (global range)

### Geostrophic Currents from ADT
Ocean surface currents are derived from the gradient of Absolute Dynamic Topography

$$\vec{u}_g = \frac{g}{f} \hat{k} \times \nabla_{\text{horiz}} ADT

$$ Where:
-$g$ = gravitational acceleration
-$f = 2\Omega\sin\phi$= Coriolis parameter
-$\hat{k} $= vertical unit vector
-$ADT$ = Absolute Dynamic Topography =$SSH - N$**Zonal component**: $u_g = -\frac{g}{f}\frac{\partial ADT}{\partial y}$**Meridional component**: $v_g = \frac{g}{f}\frac{\partial ADT}{\partial x}$### Major Ocean Circulation Patterns (Indonesian Waters)
| Current | Region | Significance |
|---------|--------|-------------|
| **Indonesian Throughflow (ITF)** | Makassar Strait, Maluku Sea | Transport of Pacific → Indian Ocean |
| **South Java Current** | Southern Java | Seasonal, ENSO-driven |
| **Mindanao Current** | Philippine Sea | Western boundary current |
| **New Guinea Coastal Current** | Papua | Seasonal reversal |
| **Agulhas Return Current** | Indian Ocean south of Java | Connects to Indian Ocean circulation |

---

## 🌍 Geocentric Sea Surface & Geoid

### Geocentric SSH
In the ITRF/ECEF frame, SSH is referenced to the ellipsoid

$$ h_{\text{sea}} = h_{\text{sat}} - \rho_{\text{altimeter}} = N + ADT $$ where $ h_{\text{sea}} $ is the ellipsoidal height of the sea surface.

### Geoid from Altimetry (Marine Geoid)
Altimetry provides direct measurement of the sea surface. In the absence of currents (ideal ocean)

$$ SSH_{\text{equilibrium}} = N + MDT_{\text{equilibrium}} \approx N $$

**For geoid determination**:

- Use long-term mean SSH from altimetry

- Subtract known MDT from ocean circulation models

- Result: $N = \overline{SSH} - MDT$**Accuracy limitations**:

- Altimetric SSH: $\pm 2–4 \text{ cm} $ (along-track)

- Geoid ($N$) from EGM2008/GOCE: $\pm 5–10 \text{ cm} $ (global),$\pm 2–3 \text{ cm} $ (regional with local data)

- MDT residual: $\sim 1–2 \text{ cm} $ (dominant error source for coastal zones)

---

## 📊 SSH Data Products & Services

| Product | Source | Resolution | Latency |
|---------|--------|------------|---------|
| **AVISO / CNES** | Multi-mission altimetry | $ 1/4° \times 1/4°$ (gridded), along-track | 3–10 days |
| **Copernicus Marine (CMEMS)** | Sentinel-3, Jason | $ 1/8°$ (regional), global grids | Near-real-time |
| **NASA PODAAC** | Jason, Sentinel-3 | Along-track, gridded | 3–10 days |
| **Jason-3 GDR** | Jason-3 (Reference Mission) | Along-track,$1\text{ Hz}$ | NRT, operational |
| **DUACS** | Multi-mission processing | $ 1/4°$ (gridded) | 3–10 days |

---

## 🛠️ Practical Applications (Aplikasi Praktis)

| Application | How SSH is Used | Key Data |
|-------------|-----------------|----------|
| **Sea Level Rise Monitoring** | Multi-year SSH trends (linear fit) | GMSL time series, regional trends |
| **Tsunami Detection** | Real-time SSH anomalies | Altimetry + DART buoys |
| **ENSO/Monsoon Monitoring** | SSH patterns (warm pool, Kelvin waves) | Tropical Pacific Indian Ocean SSH maps |
| **Ocean Circulation (Geostrophic Currents)** | ADT gradient → current velocity | Gridded ADT from multi-mission |
| **Nautical Charting / Hydrography** | Mean sea level as tidal datum | Altimetry mean SSH |
| **Climate Modeling** | Ocean heat content from SSH + T/S profiles | Multi-mission SSH + Argo floats |
| **Coastal Risk Assessment** | Storm surge + MSL rise | SSH + bathymetry + DEM |
| **Satellite Orbit Determination** | Altimetry as orbit constraint (Jason reference) | On-board altimeter data |
| **Geoid Calibration** | Altimetry SSH → geoid in open ocean | Multi-mission SSH mean - MDT |

---

## 📐 Practical Formulas

### SSH Time Series Analysis

$$

SSH(t) = \text{MSL} + \text{trend} \cdot t + \text{seasonal} + \text{residual}\text{trend} = \frac{\sum(t_i - \bar{t})(SSH_i - \overline{SSH})}{\sum(t_i - \bar{t})^2
}

$$### Sea Level Trend (Linear)$$\text{MSL}(t) = a_0 + a_1 (t - t_0) + \varepsilon

$$ where $ a_1 $= trend (mm/year),$t_0$ = reference epoch.

### Altimeter Accuracy Budge
t

$$\sigma_{\text{SSH}}^2 = \sigma_{\text{orbit}}^2 + \sigma_{\text{range}}^2 + \sigma_{\text{wet}}^2 + \sigma_{\text{iono}}^2 + \sigma_{\text{SSB}}^2 + \sigma_{\text{tide}}^2

$$ Typical values (Jason-3):$\sigma_{\text{orbit}} \approx 1.5 \text{ cm} $,$\sigma_{\text{range}} \approx 1.5 \text{ cm} $, others 1–2 cm each →$\sigma_{\text{SSH}} \approx 2.5 \text{ cm} $.

### Geostrophic Current from SSH

$$ u = -\frac{g}{f}\frac{\partial SSH}{\partial y}, \quad v = \frac{g}{f}\frac{\partial SSH}{\partial x}$$---

## 🔗 Related Notes

- [[Geoid]] — SSH referenced to geoid

- [[Geoid Undulation]] —$ N$ in altimetry context

- [[Vertical Datum]] — MSL as vertical reference

- [[Physical Geodesy]] — Potential theory, geoid determination

- [[Tidal Theory]] — Tides in altimetry correction

- [[Gravity Field]] — Gravity from altimetry

- [[Geodesy MOC]] — Remote sensing context

- [[Geodesy MOC]] — Physical oceanography context

---

## 📚 References

### Mission References
1. **Fu, L.-L. & Cazenave, A.** (eds.), *Satellite Altimetry and Earth Sciences*, Academic Press, 2001.
2. **Ablain, M. et al.**, *Improved sea level record over the satellite altimetry era*, Nature Climate Change, 5, 2015.
3. **CNES/Jason-3**, *Jason-3 Mission Handbook*, 2016.
4. **ESA/Sentinel-3**, *Sentinel-3 Mission Guide*, Copernicus documentation.
5. **NASA/JPL PODAAC**, *Jason Series Data User Handbook*.

### Theory & Methods
6. **Cazenave & Cozannet**, *Global Sea Level Rise and its Regional Implications*, Elsevier, 2014.
7. **Emery & Thomson**, *Data Analysis Methods in Physical Oceanography*, 3rd ed., Elsevier, 2004.
8. **Gill & Niiler**, *The theory of the seasonal variability in the ocean*, Deep-Sea Research, 1973.
9. **Stommel**, *The Gulf Stream*, 2nd ed., Cambridge, 1965.

### Indonesia & Regional
10. **Nugroho et al.**, *Sea level rise and impacts on the Indonesian coastal zone*, various.
11. **BMKG**, *Kondisi Hidro-Oseanografi Wilayah Indonesia*, various annual reports.
12. **BIG/BRIN**, *Indonesian Geoid Model and Altimetry Validation*.
13. **Pramono et al.**, *Sea level variability in the Indonesian Seas from satellite altimetry*, J. Geod., 2019.
14. **Sprintall et al.**, *Indonesian Throughflow*, J. Geophys. Res., 2012.

### IPCC
15. **IPCC AR6 WGI**, *Sea Level Rise Chapter (Ch. 9)*, 2021.

---

#study-pack #sea-surface-height #altimetry #oceanography #mean-sea-level #ssh #jason #sentinel-3