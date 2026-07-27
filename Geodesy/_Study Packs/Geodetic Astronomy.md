---
tags: [geodesy, study-pack, astronomy, positioning, aigis]
aliases: [Geodetic Astronomy, Astronomi Geodesi]
created: 2026-07-27
---

# 📚 Study Pack — Geodetic Astronomy

_A comprehensive guide to celestial coordinate systems, star observations, and how astronomical methods establish positions and orientation on Earth. Target length: ~4,000 words._

> **Prerequisites:** [[Geodetic Coordinates]], [[Reference Ellipsoid]], [[Tidal Theory]]

---

## 1. Introduction

**Geodetic astronomy** uses observations of celestial bodies (stars, Sun, planets) to determine:
1. **Astronomical latitude** $\varphi^*$and **astronomical longitude**$\lambda^*$ at a point on Earth.
2. **Azimuth** and **time**.
3. The **deflection of the vertical** (the angle between the true plumb line and the ellipsoid normal).

Historically the only way to establish coordinates of points, geodetic astronomy is now a complement to GNSS, providing independent orientation checks and plumb‑line information for [[Physical Geodesy]].

> **Indonesian term:** *Astronomi Geodesi*

---

## 2. Coordinate Systems

### 2.1. Terrestrial (Earth‑fixed) Coordinates

| System | Origin | Axes | Use |
|--------|--------|------|-----|
| **Geodetic**$(\varphi, \lambda, h)$ | Centre of ellipsoid | Latitude, longitude, height above [[Reference Ellipsoid]] | Standard for GNSS/GIS |
| **Astronomical**$(\varphi^*, \lambda^*)$ | Local plumb line | Measured by star observations | Provides local gravity direction |
| **Local ENU** | Station point | East, North, Up | Surveying (see [[Local ENU NEU]]) |

### 2.2. Celestial Coordinates

The celestial sphere is an imaginary sphere of infinite radius centred on the observer. Key coordinate systems:

| System | Equator | Origin | Use |
|--------|---------|--------|-----|
| **Topocentric** (horizontal) | Local horizon | Observer zenith | Star observations from field |
| **Equatorial** | Celestial equator | Vernal equinox (γ) | Star catalogues |
| **Ecliptic** | Ecliptic plane | Vernal equinox | Solar system |
| **Galactic** | Galactic plane | Galactic centre | Galactic astronomy |

### 2.3. Converting between Systems

**Topocentric to Equatorial:**$$
\begin{aligned}
\sin\delta &= \sin\varphi \sin h + \cos\varphi \cos h \cos A \\
\cos\delta \cos\alpha &= \cos\varphi \cos h \sin A - \sin\varphi\cos\delta\sin\alpha \\
\cos\delta\sin\alpha &= \cos h \cos A
\end{aligned}
$$where$ A$= azimuth, $h$= altitude, $\alpha $= right ascension, $\delta $= declination, $\varphi $= latitude.

---

## 3. Star Catalogues and Ephemerides

| Catalogue / Tool | Description | Precision | Access |
|------------------|-------------|-----------|--------|
| **Gaia DR3** (ESA) | ~1.8 billion stars, astrometry | 0.02 mas (bright) | https://gea.esac.esa.int/archive/ |
| **Hipparcos** (ESA) | ~118 000 stars, high precision | 1 mas | https://www.cosmos.esa.int/web/hipparcos |
| **TYCHO‑2** | ~2.5 million stars | 20 mas | https://www.cosmos.esa.int/web/tycho-2 |
| **Gaia Source List (GSC) 2.4** | ~458 million stars | ~0.1 arcsec | https://gcmd.nasa.gov/ |
| **JPL Horizons** | Solar system ephemerides | High | https://ssd.jpl.nasa.gov/horizons/ |

For geodetic work, the most useful are:

- **Gaia DR3** — modern astrometric reference frame.

- **Hipparcos** — bright star observations.

- **JPL Horizons** — Sun, Moon, planet positions.

---

## 4. Observational Techniques

### 4.1. Transit Observation (Meridian Transit)

Observe a star crossing the **local meridian** (the great circle through zenith and celestial poles).
$$
\begin{aligned}
\varphi^* &= \delta + (90° - h_{\text{max}}) \\
\lambda^* &= \text{LST} - \alpha
\end{aligned}
$$where LST = Local Sidereal Time, and$ \delta $, $\alpha $ are from the star catalogue.

### 4.2. Circumpolar Stars (Dome Star)

For high latitudes, use stars that never set. The **Dome (Kozai) star method**:
1. Observe the same star at two positions on the great circle through the pole.
2. Measure altitudes $h_1$, $h_2$ and the azimuth difference.
3. Compute latitude$ $\varphi^* = \delta \pm \arccos\left(\frac{\cos h_1 + \cos h_2}{2\cos(p/2)\cos\delta}\right)
$$where$ p$ is the hour angle difference.

### 4.3. Polaris (North Star
)$ $\varphi^* = h + \epsilon \cos H$$where$ h$= measured altitude of Polaris, $\epsilon \approx 0.6696°$ (Polaris' angular distance from the pole), and $H$= hour angle (from ephemeris).

### 4.4. Time Determination (Longitude
)$ $\lambda^* = \alpha_{\text{star}} - \text{LST} + 12h
$$
Requires accurate time (GPS provides time to ns accuracy).

---

## 5. Deflection of the Vertical (DOV)

The **deflection of the vertical** (plumb‑line anomaly) $\xi, \eta$:$ $\xi = \varphi^* - \varphi\eta = (\lambda^* - \lambda)\cos\varphi
$$where$ \varphi, \lambda $ are the geodetic coordinates from GNSS/leveling.

| Component | Direction | Typical magnitude |
|-----------|-----------|-------------------|
| $\xi$ (meridional) | North–South | 0.1–5″ (arc‑seconds) |
| $\eta$ (prime vertical) | East–West | 0.1–5″ (arc‑seconds) |

**Why DOV matters:**

- The plumb line is perpendicular to the geoid, not the ellipsoid.

- In mountainous areas, DOV can be **5–30″** (e.g., Himalayas, Andes).

- DOV is the link between the geoid and the [[Reference Ellipsoid]]:
 -$\xi \approx -\frac{1}{M\gamma}\frac{\partial N}{\partial\varphi} $-$\eta \approx -\frac{1}{N\gamma\cos\varphi}\frac{\partial N}{\partial\lambda} $---

## 6. Worked Example — Determining Latitude from Polaris

**Observed:** Polaris at transit (hour angle $H = 0$), altitude $h = 45° 32' 15.4″$.

**Given:**$\epsilon = 0° 40' 16.6″$(Polaris angular distance from pole), $H = 0 $.$ $\varphi^* = h + \epsilon \cos H = 45° 32' 15.4″ + 0° 40' 16.6″ = 46° 12' 32.0
″
$$
Cross‑check with GNSS: GNSS latitude = 46° 12' 30.5″.$ $\xi = \varphi^* - \varphi = 1.5″$$This suggests the plumb line is deflected 1.5″ northward — consistent with nearby topographic mass to the south.

---

## 7. Modern Geodetic Astronomy Applications

| Application | Method | Precision |
|-------------|--------|-----------|
| **Absolute gravimetry station orientation** | Star observations for local vertical | ~0.1″ |
| **Gyrotheodolite orientation** | Gyro north + star azimuth | ~10″ |
| **Check on GNSS baseline azimuth** | Astronomical vs geodetic azimuth | ~1″ |
| **Deflection of the vertical** | Multiple star pairs | 0.1–0.5″ |
| **Historical geodetic networks** | Observations from the era before GNSS | ~1″ |

---

## 8. Tools and Equipment

| Instrument | Use | Accuracy |
|------------|-----|----------|
| **Wild T4 / Kern DKM3‑A** | Precision theodolite for stars | 0.1″ |
| **Gyrotheodolite (KVH)** | True north determination (underground) | 5–15″ |
| **Digital zenith camera** | Zenithal imaging for DOV | 0.01″ |
| **GPS receiver** | Time + geodetic coordinates | ns time / mm position |
| **Star catalogues (Gaia, Hipparcos)** | Reference positions | < 0.1″ |

---

## 9. Practice Problems

1. Compute the latitude from Polaris at altitude 35° 12' 05″, hour angle 18h 30m.
2. Determine longitude: if a star with $\alpha = 14h\; 35m\; 20.3s$ transits the local meridian when GPS time reads 02h 10m 15.2s UT1, what is the local longitude?
3. Compute DOV components: GNSS gives $\varphi = -6°\; 12'\; 48.0″$, $\lambda = 106°\; 50'\; 15.0″$. Astronomical gives$ \varphi^* = -6°\; 12'\; 46.5″$, $\lambda^* = 106°\; 50'\; 13.8″$(cos$ \varphi = 0.994 $). What are$ \xi $and$ \eta$?
4. Explain why the plumb line deviates from the ellipsoid normal, and relate this to the geoid undulation gradient.

---

## 10. References

- Bomford, G., *Geodesy* (4th ed.), Oxford University Press, 1980.

- Guinot, B. & Capitaine, N., *Astronomy and Astrophysics*, 2004.

- Torge, W. & Müller, J., *Geodesy* (4th ed.), De Gruyter, 2012.

- Böhme, H., *Geodätische Astronomie*, Vermessungswesen, 1982.

- Lindegren, L. et al., *Gaia Data Release 2: The Gaia astrometric solution*, A&A 616, A2, 2018.

- JPL Horizons Ephemeris System, https://ssd.jpl.nasa.gov/horizons/

- ESA Gaia Archive, https://gea.esac.esa.int/archive/

➡️ [[Geodesy MOC]] · [[_Study Packs]] · [[Geodetic Coordinates]] · [[Physical Geodesy]]