---
tags: [geodesy, concept, positioning, aigis]
aliases: [GPS, global positioning system, GNSS Receiver, Navstar]
created: 2026-07-12
updated: 2026-07-27
---

# 🛰️ GPS (Global Positioning System)

**GPS** is the United States' Global Navigation Satellite System (GNSS). Originally a military system, it is the most widely used positioning technology worldwide and the **primary source of WGS84 coordinates and ellipsoidal heights**.

## Constellation

| Parameter | Value |
|-----------|-------|
| **Total satellites** | ≥ 31 operational (as of 2024) |
| **Orbital planes** | 6 |
| **Satellites per plane** | 4–6 |
| **Orbital altitude** | ~20,180 km (MEO) |
| **Orbital inclination** | 55° |
| **Orbital period** | Half-sidereal day (~11 hr 58 min) |
| **Repeat cycle** | Same ground track every 4 sidereal days |

The constellation is designed so that **any point on Earth has at least 4 satellites above the horizon** at any time, enabling 3D positioning plus time (PVT).

## Signal Structure

### L-Band Frequencies

GPS transmits on two L-band frequencies using spread-spectrum techniques (CDMA). Each frequency carries multiple signal components:

| Signal | Frequency | Bandwidth | Code | Purpose |
|--------|-----------|-----------|------|---------|
| **L1 C/A** | 1575.42 MHz | 2.046 MHz | Coarse/Acquisition (C/A code) | Civil, all receivers; 1–5 m precision |
| **L1 P(Y)** | 1575.42 MHz | 2.046 MHz | Precise (P code, encrypted as Y) | Military |
| **L2C** | 1227.60 MHz | 1.023 MHz | Civil code | Dual-frequency civil; ionosphere correction |
| **L2 P(Y)** | 1227.60 MHz | 1.023 MHz | Precise | Military |
| **L5** | 1176.45 MHz | 20.46 MHz | Safety-of-Life (SoL) | Aviation; high integrity; 10–30 cm |
| **L1C** | 1575.42 MHz | 2.046 MHz | Civil (interoperable) | Modernized; interoperable with Galileo |

### Signal Components in Detail

Each carrier transmits a **pseudorandom noise (PRN) code** modulated by navigation message bits:

1. **PRN code** — unique per satellite (Gold code). Codes are 1 ms (L1 C/A), 20 ms (L2C), or 10 ms (L5) per chip/period at 1.023 Mchip/s (C/A), 1.023 Mchip/s (L2C), 10.23 Mchip/s (L5).
2. **Navigation message** — transmitted at 50 bps. Contains:
 - Satellite ephemeris (precise orbit for that satellite)
 - Almanac (coarse orbit for all satellites in constellation)
 - Clock correction coefficients
 - Ionosphere model parameters (Klobuchar)
 - Health status and integrity information
3. **Carrier phase** — the carrier signal itself (1575.42 MHz for L1, λ ≈ 19 cm). Carrier-phase measurements enable cm-level precision with carrier smoothing.

### Pseudorange Measurement

The fundamental GPS measurement:

$$\rho_i = \| \mathbf{r}_r - \mathbf{r}_i \| + c\,\delta t_r - c\,\delta t_i + \varepsilon_{\rho} $ $

where $\mathbf{r}_r $= receiver position,$\mathbf{r}_i $= satellite $  i $ position,$  c $ = speed of light,$\delta t_r $= receiver clock error,$\delta t_i $= satellite clock error, and $\varepsilon_\rho $= measurement noise + atmospheric effects.

## Positioning Modes

### Absolute (Standalone) Positioning

- **Principle:** Each satellite provides a pseudorange equation; solve for $ (X, Y, Z, \delta t)$ with ≥ 4 satellites.

- **Accuracy:** 3–5 m (C/A code), ~1–2 m (modern L1C/L5), affected by ionosphere.

- **Method:** Least-squares solution of linearized pseudorange equations.

### Differential GPS (DGPS)

- **Principle:** A reference station at known location computes pseudorange corrections, which are broadcast to the rover.

- **Accuracy:** ~0.5–3 m range-dependent (SDCM, RTCA SC-159 corrections).

- **Standards:** RTCA SC-159, RTCM MSM format.

### SBAS (Satellite-Based Augmentation System)

| System | Region | Corrections | Accuracy |
|--------|--------|-------------|----------|
| **WAAS** | US/Canada | In-flight | 1–2 m |
| **EGNOS** | Europe/Africa | In-flight | 1–2 m |
| **MSAS** | Japan | In-flight | 1–2 m |
| **GAGAN** | India | In-flight | 1–2 m |
| **SDCM** | Russia | In-flight | 1–2 m |
| **SDCM** | Russia | In-flight | 1–2 m |

SBAS provides integrity (alert limits for aviation) plus meter-level accuracy via geostationary satellite broadcast.

### PPP (Precise Point Positioning)

- **Principle:** Use IGS precise orbit/clock products (broadcast or downloaded) + code + carrier-phase measurements.

- **Accuracy:** 2–5 cm horizontally, 3–10 cm vertically after convergence (~30 min).

- **Advantage:** Single receiver, no local reference network needed.

- **Convergence:** Initial ambiguity resolution takes 30 min to a few hours.

### RTK (Real-Time Kinematic) / Network RTK

- **Principle:** Base station(s) + rover, real-time carrier-phase ambiguity resolution.

- **Accuracy:** 1–2 cm horizontal, 2–5 cm vertical (with NRTK/Virtual Base Station).

- **Range:** Limited by baseline length (50 km for classic RTK, up to 100+ km with VRS/NTRIP).

## GNSS vs GPS

While "GPS" refers specifically to the US system, the generic term **GNSS** encompasses all constellations:

| System | Agency | Frequencies (L1/E1) | Operational Satellites |
|--------|--------|----------------------|------------------------|
| **GPS** | US (DoD) | L1 (1575.42), L2 (1227.60), L5 (1176.45) | 31+ |
| **GLONASS** | Russia | L1 (1602.0+kh), L2 (1246.0+kh) | 26+ (near-polar) |
| **Galileo** | EU | E1 (1575.42), E5a (1176.45), E5b (1207.14), E6 (1278.75) | 28+ |
| **BeiDou-3** | China | B1I (1561.098), B1C (1575.42), B2a (1176.45), B2b (1207.14) | 30+ |
| **QZSS** | Japan (SBAS) | L1C/A, L1S, L2C-like | 4 (regional) |
| **NavIC** | India | L5, S-band | 8 (regional) |

Modern multi-GNSS receivers track 4–5 constellations simultaneously, improving geometry (lower GDOP, faster fixes).

## Epoch and Relationship to WGS84

WGS84 coordinates output by GPS receivers are referenced to the **WGS84 (G1762/M2139)** realization, which is tied to [[ITRF]] at the nanosecond level in time. The frame realization epoch is the reference moment from which the satellite orbits and Earth-orientation parameters are computed.

## References

- Ashby, N. (2003). *Relativity in the Global Positioning System*. Living Reviews in Relativity.

- Hofmann-Wellenhof, B. et al. (2008). *GNSS — Global Navigation Satellite Systems*. Springer.

- Montenbruck, O. & Steigenberger, P. (2019). *Satellite Navigation*. Cambridge University Press.

## Related

- [[GNSS]] · [[WGS84]] · [[Geocentric Cartesian ECEF]] · [[Geodetic Coordinates]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
