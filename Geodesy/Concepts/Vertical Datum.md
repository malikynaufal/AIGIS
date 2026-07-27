# Vertical Datum

> *Datum Tinggi* — The fundamental reference surface for height determination in geodesy.

## Overview

A **vertical datum** (datum tinggi) is the reference surface from which elevations or heights are measured. Unlike horizontal datums which define latitude/longitude on a reference ellipsoid, vertical datums establish the zero-height surface. The choice of vertical datum directly affects engineering tolerances, flood mapping, and geodetic network alignment.

## Height Systems (Sistem Tinggi)

### 1. Ellipsoidal Height ($h $)

The ellipsoidal height is the distance from a point on the Earth's surface to the reference ellipsoid, measured along the ellipsoid normal.

$$ h = \sqrt{X^2 + Y^2 + \left(\frac{a^2}{b^2} Z\right)^2} - \frac{a^2}{b} \cdot \frac{1}{\sqrt{X^2 + Y^2 + \left(\frac{a^2}{b^2} Z\right)^2}} + Z $$ where $ a $and $b $ are the semi-major and semi-minor axes of the ellipsoid.

**Key properties:**

- Computed directly from geocentric coordinates $(X, Y, Z)$

- Does NOT follow the direction of gravity — the ellipsoid normal does not align with the plumb line

- Used in GPS/GNSS heighting as the native height output

- Not physically meaningful for hydrology or construction

### 2. Orthometric Height ($H$)

The orthometric height is the distance from a point on the Earth's surface to the **geoid** (quasi-geoid), measured along the plumb line.

$$ H = h - N $$ where:
-$h$ = ellipsoidal height
-$N$ = geoid undulation (separation between ellipsoid and geoid)

The geoid undulation $N $is derived from the Bruns formula

$$ N = \frac{\Delta W}{\gamma}$$ where $\Delta W $is the disturbing potential and $\gamma $ is the normal gravity at the surface.

**Key properties:**

- Aligned with gravity — physically meaningful for water flow

- Approximates Mean Sea Level (MSL) extended under land

- The standard for national height networks worldwide

- Two points with equal orthometric height are hydraulically connected

### 3. Normal Height ($h_N$)

The normal height was introduced by Molodenskii as an alternative that avoids the need for gravity data at the Earth's surface.

$$ h_N = h - \zeta $$ where $\zeta $is the **height anomaly** (quasi-geoid undulation)$$\zeta = \frac{T_P}{\gamma_0} $$

-$T_P$ = disturbing potential at point P
-$\gamma_0 $= normal gravity on the telluroid

**Key properties:**

- Can be computed purely from geometric and normal gravity data

- Does not require gravity measurements on the surface

- Used in the Russian/CIS height system and in some modern European systems

- The telluroid (telluroida) is a surface displaced from the ellipsoid by $\zeta $### 4. Normal-Orthometric Height

A hybrid system used in some national surveys that combines the computational simplicity of normal heights with a closer physical approximation to orthometric heights.

## Relationship Between Height Types

$$\begin{aligned}
h &= H + N & \text{(ellipsoidal = orthometric + geoid undulation)} \\
h &= h_N + \zeta & \text{(ellipsoidal = normal + height anomaly)} \\
H &= h_N + (N - \zeta) & \text{(orthometric vs normal difference)}
\end{aligned} $$ The difference$ N - \zeta $ is typically small (< 2 m in most regions) but can be significant for precise levelling.

## The Geoid (Geoid) and Quasi-Geoid

### Geoid Definition
The geoid is the equipotential surface of the Earth's gravity field that best fits, in a least-squares sense, Mean Sea Level (MSL). It is defined such that

$$ W(P_{geoid}) = W_0 = \text{constant}$$ where $ W $is the gravity potential and $W_0 $ is the global equipotential value at MSL.

### Quasi-Geoid (Quasi-Geoid)
The quasi-geoid (kuasi-geoid) is the Molodenskii surface

$$\zeta = \frac{T}{\gamma_0} $$ Unlike the geoid, the quasi-geoid is NOT an equipotential surface but provides a geometrically simpler reference for height determination.

### Geoid Undulation Global Pattern
| Region | Typical $N $range | Notes |
|--------|-------------------|-------|
| Indonesia | −30 to +40 m | Complex due to tectonic activity |
| Europe | −20 to +60 m | Well-determined by GRACE/GOCE |
| Africa | −30 to +20 m | Sparse data coverage |
| Australia | −20 to +40 m | Australian Geoid 2020 (AUSGeoid20) |

## Indonesian Height System: TSSGI 2018

### Standar Tinggi Nasional
Indonesia adopted the **Tinggi Survei Sepuluh Ribuan Indonesia (TSSGI) 2018** as its national vertical datum, referenced to the **Indonesian Geoid 2018 (IGN-2018)**.

**Key specifications:**

- Reference epoch: 2018.0

- Geoid model: IGN-2018 based on GRACE-FO and local gravity data

- Origin benchmark: Mean Sea Level at Jakarta Tide Gauge (Pelabuhan Tanjung Priok)

- Height network: Densification via precise levelling from BIG (Badan Informasi Geospasial)

### Height Determination Formula for Indonesi
a

$$ H_{ortho} = h_{GPS} - N_{IGN2018}$$ where:
-$H_{ortho}$ = orthometric height (height above MSL)
-$h_{GPS}$ = ellipsoidal height from GNSS observation
-$N_{IGN2018}$ = geoid undulation from Indonesian Geoid model

### Accuracy Specifications
| Survey Type | Accuracy | Method |
|-------------|----------|--------|
| First-order levelling | ± 1 mm/√km | Digital level, invar rod |
| Second-order levelling | ± 3 mm/√km | Digital level |
| GNSS levelling | ± 5 cm (with geoid) | RTK + IGN-2018 |
| Third-order levelling | ± 10 mm/√km | Classical levelling |

## Height Reference Surfaces for Construction

### Benchmark Networks
Indonesian height benchmarks are organized hierarchically:

1. **Bench Mark Utama (BMU)** — Primary benchmarks tied to international tide gauges
2. **Bench Mark Induk (BMI)** — Regional benchmarks, ~50 km spacing
3. **Bench Mark Semu (BMS)** — Local benchmarks, ~5 km spacing
4. **Bench Mark Lapangan (BML)** — Field benchmarks for construction

### Common Height Reference Confusions
| Issue | Cause | Solution |
|-------|-------|----------|
| GPS height ≠ site elevation | Ellipsoidal vs orthometric | Apply geoid model |
| Benchmarks disagree | Different epochs, different datums | Re-level with current standards |
| Flood levels inconsistent | Mixed height systems | Standardize to national datum |

## Geoid Modelling Methods

### Remove-Compute-Restore (RCR) Technique

$$ N = N_{long} + N_{res}N_{res} = \frac{G\Delta\rho}{\gamma} \int \int \frac{h - h_P}{r} \, d\sigma $$

1. **Remove**: Remove long-wavelength geoid from satellite data (GRACE/GOCE)
2. **Compute**: Compute residual geoid from local gravity data using Stokes/Helmert integral
3. **Restore**: Add back the long-wavelength component

### Stokes' Formula (Geoid from Gravity Anomaly
)

$$ N = \frac{R}{4\pi\gamma_0} \int \int_{\sigma} \Delta g \cdot S(\psi) \, d\sigma $$

where:
-$S(\psi)$= Stokes kernel function
-$\Delta g $= gravity anomaly
-$\psi $= spherical distance from computation point
-$R$ = mean Earth radius

### Molodenskii Formula (Height Anomaly
)

$$\zeta = \frac{R}{4\pi\gamma_0} \int \int_{\sigma} \Delta g^* \cdot S(\psi) \, d\sigma + \zeta_0

$$ where $\Delta g^*$is the Molodenskii gravity anomaly and $\zeta_0 $ is a constant determined from GNSS/levelling.

## Practical Applications

### Engineering Survey

- All construction elevations must reference a consistent vertical datum

- Geoid model selection affects apparent ground elevation by centimeters

- Dam monitoring requires mm-level precision relative to a stable datum

### Flood Mapping

- 1D flood models require consistent MSL reference

- Sea level rise corrections must account for vertical land motion

- Tidal datums (MSL, MHHW, MLW) serve as local references

### GNSS Levelling Workflo
w

$$ H_{site} = h_{GNSS} - N_{geoid} + \delta H_{tide}$$ where $\delta H_{tide} $ is the tidal correction for the observation epoch.

## Key References

- Heiskanen & Moritz, *Physical Geodesy* (1967)

- Tscherning, *Geoid Determination by Least Squares Collocation* (1985)

- BIG, *Standar Nasional Geoid Indonesia IGN-2018* (2018)

- Torge & Müller, *Geodesy* (5th ed., 2012), Ch. 8

---
**Related:** [[Geodesy Fundamentals]], [[Geodetic Reference Frames]], [[Sea Surface Height]]