---
tags: [geodesy, concept, positioning, aigis]
aliases: [IGS, International GNSS Service, International GPS Service]
created: 2026-07-12
updated: 2026-07-27
---

# 🛰️ IGS (International GNSS Service)

The **IGS** (International GNSS Service, formerly International GPS Service) provides the precise orbit, clock, station position, and Earth-rotation products that enable cm-level and mm-level [[GNSS]] positioning. It operates under the [[IERS]] framework and is the backbone of scientific geodesy and precise surveying.

## Core Mission

| IGS Product | Description | Update Interval |
|-------------|-------------|-----------------|
| **Precise orbits** | IGS Final orbits (GPS/GLONASS/Galileo/BDS) | Weekly (13-day latency) |
| **Precise orbits** | IGS Rapid orbits | ~17 hours latency |
| **Precise orbits** | IGS Ultra-Rapid orbits | ~3 hours (4-hour latency) |
| **Satellite clocks** | 30-sec clock corrections | Daily |
| **Ionospheric maps** | Total electron content (TEC) | Hourly |
| **Tropospheric zenith** | Zenith wet delay (ZWD) from station network | Daily |
| **Earth rotation** | IERS Bulletin A contribution (EOP) | Daily |
| **Antenna phase center** | Absolute PCO/PCV models | Updated ~every 3 years |
| **Site coordinates** | ITRF2014 station coordinates & velocities | Updated ~annually |

## IGS Network

IGS operates a global network of over 500 continuously operating GNSS stations (CORS) that provide multi-GNSS data:

| Feature | Detail |
|---------|--------|
| **Total active stations** | ~500 (as of 2024) |
| **GPS receivers** | All modern, multi-GNSS capable |
| **Data rate** | 15-sec, 30-sec, 60-sec |
| **Data format** | RINEX 2/3/4 |
| **Data products** | Orbits, clocks, troposphere, ionosphere |
| **Access** | Public via CDDIS (NASA), BNC (BKG) |

### Station Data Availability

| Network Segment | # Stations | Data Rate |
|-----------------|------------|-----------|
| IGS Global | ~100 | 30 sec |
| IGS Regional | ~200 | 15 sec |
| IGS Associate | ~200 | Variable |
| Total | ~500 | 15–60 sec |

### Access and Distribution

| Service | URL | Description |
|---------|-----|-------------|
| **CDDIS** (NASA) | cddis.gsfc.nasa.gov | Primary archive (RINEX, orbits, SP3) |
| **BKG** (Germany) |igs.bkg.bund.de | Real-time IGS products |
| **IGN** (France) | data.ign.fr | European mirror |
| **SOPAC** (UCSD) | igs.igscb.org | SOPAC archives |
| **RTCM SC-104** | rtcm.org | Real-time NTRIP standards |

## IGS Analysis Centers

IGS coordinates data processing at dedicated Analysis Centers:

| Analysis Center | Institution | Specialty |
|-----------------|-------------|-----------|
| **EMR** | Natural Resources Canada | Multi-GNSS orbits |
| **CODE** | Univ. of Bern | GPS/GLONASS orbits, ionosphere |
| **GFZ** | German GeoResearch Center | GPS/Galileo/BDS orbits |
| **JPL** | NASA Jet Propulsion Lab | Multi-GNSS, orbit quality |
| **MIT** | Massachusetts Inst. of Tech | GNSS + SLR combination |
| **ESA/ESOC** | European Space Agency | GPS/GLONASS/Galileo |
| **NRC** | Natural Resources Canada | Multi-GNSS |

## IGS Products for Precise Point Positioning (PPP)

PPP uses IGS products directly for cm-level positioning from a single receiver:

| Product | Latency | Accuracy (PPP) | Convergence |
|---------|---------|----------------|-------------|
| **IGS Final** | 12–14 days | 2–5 cm (horiz), 4–8 cm (vert) | 30 min–2 hr |
| **IGS Rapid** | 17 hours | 3–5 cm (horiz), 5–10 cm (vert) | 30 min–2 hr |
| **IGS Ultra-Rapid (obs)** | ~3 hours | 5–10 cm (horiz), 8–15 cm (vert) | 30 min–2 hr |
| **IGS Ultra-Rapid (pred)** | ~3 hours | 10–15 cm (horiz), 15–30 cm (vert) | 30 min–2 hr |
| **IGS Real-Time** | ~3 s | 10–20 cm | N/A (real-time) |

### PPP Workflow with IGS Products

```
1. Download raw GNSS observations (RINEX) for receiver
2. Obtain IGS precise orbits (SP3) and clocks (RINEX clocks)
3. Apply IGS absolute antenna PCO/PCV models
4. Correct for IERS Earth orientation (polar motion, LOOD)
5. Apply IGS ionosphere-free linear combination
6. Process with PPP software (Bernese, GIPSY-OASIS, RTNet, etc.)
7. Final coords in ITRF2014 (or ITRF2020) at observed epoch
```

## IGS Products for Geodetic Applications

| Application | IGS Product | Typical Accuracy |
|-------------|-------------|-----------------|
| GNSS orbit determination | IGS Final orbits | 2–3 cm radial |
| Reference frame realization | IGS + IVS + ILRS | mm-level |
| Atmospheric science | IGS tropospheric ZWD | ~2 mm path delay |
| Ionospheric monitoring | IGS TEC maps | ~2–5 TECU |
| Sea level monitoring | IGS height time series | ~1 mm/yr |
| Plate tectonics | IGS station velocities | 0.3–1 mm/yr |

## Multi-GNSS Orbit Determination

IGS expanded from GPS-only to multi-constellation support:

| Constellation | IGS Tracking Started | Current Status |
|---------------|---------------------|----------------|
| **GPS** | 1994 | Full support, final products |
| **GLONASS** | 2005 | Full support, final products |
| **Galileo** | 2014 | Full support, rapid products |
| **BeiDou-3** | 2017 | Full support, rapid products |
| **QZSS** | 2018 | Experimental |
| **IRNSS** | 2019 | Experimental |

## Data Access: RINEX Format

IGS distributes data in RINEX (Receiver Independent Exchange Format):

| File Type | Content | Extension |
|-----------|---------|-----------|
| **Navigation** | Broadcast ephemeris | .nav, .gnav, .hnav, .lnav |
| **Observation** | Carrier phase, pseudorange | .obs, .rnx, .XXo (legacy) |
| **SP3** | Precise orbits | .sp3 |
| **Clock** | Precise satellite clocks | .clk |
| **Ionosphere** | TEC maps | .ion, .ionex |
| **Troposphere** | Zenith delay | .tro, .tzd |

## References

- Dow, J. M. et al. (2009). *The International GNSS Service (IGS): status and ongoing enhancements*. Journal of Geodesy, 83(3-4), 191-198.
- Rizos, C. (2002). *IGS: status, future and contributions to geodetic science*. IAG Symposia.
- IGS Central Bureau: https://www.igs.org/
- Johnston, G. et al. (2017). *The International GNSS Service in 2015*. J. Geodesy, 91(7), 611-627.

## Related
- [[GNSS]] · [[IERS]] · [[ITRF]] · [[PPP]] · [[WGS84]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Kurikulum Teknik Geodesi]]
