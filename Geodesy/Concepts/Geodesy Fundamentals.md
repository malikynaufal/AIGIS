---
tags: [geodesy, concept, fundamentals, branches, earth-shape, coordinates, measurements, engineering]
aliases: [Geodesy Fundamentals, Dasar Geodesi, Ilmu Geodesi]
created: 2026-07-27
---

# Geodesy Fundamentals (Dasar-Dasar Geodesi)

> **Indonesian Gloss**: **Geodesi** — Ilmu yang mempelajari bentuk dan ukuran bumi, bidang gravitasi, dan penentuan posisi titik di permukaan bumi dalam sistem referensi terukur. Cabang: **Geodesi Geometrik**, **Geodesi Fisis**, **Geodesi Astronomi**.

---

## 🌍 Definition & Scope (Definisi & Ruang Lingkup)

> **Geodesy** (Geodesi) — Ilmu pengukuran dan pemetaan bentuk bumi, bidang gravitasi, serta posisi titik di ruang 3D dalam sistem referensi terukur. Mencakup: penetapan koordinat, transformasi datum, proyeksi peta, pengukuran gravitasi, geoid, referensi frame, dan aplikasinya di survei, navigasi, geodinamika, dan rekayasa.

> **Definisi klasik (Helmert, 1880)**: *"Geodesy is the science of measuring and mapping the Earth's surface."*

> **Definisi modern (IAG/IUGG)**: *"Geodesy is the science of determining the size, shape, and gravity field of the Earth, and their changes with time."*

### Ruang Lingkup Modern
| Domain | Fokus | Aplikasi |
|--------|-------|----------|
| **Geometric Geodesy** | Bentuk, ukuran, posisi, koordinat | GNSS, survei, navigasi, pemetaan |
| **Physical Geodesy** | Bidang gravitasi, geoid, tinggi | Tinggi ortometrik, geoid, gravitasi |
| **Satellite Geodesy** | Satelit buatan, GNSS, SLR, VLBI, DORIS | ITRF, GNSS positioning, orbit |
| **Astronomical Geodesy** | Bintang, rotasi bumi, polar motion | UT1, polar motion, azimuth astronomis |
| **Geodynamics** | Deformasi kerak, rotasi, massa | Tektonik, gempa, GIA, sea level |

---

## 🌐 Branches of Geodesy (Cabang-Cabang Geodesi)

### 1. Geometric Geodesy (Geodesi Geometrik)
> **Fokus**: Bentuk geometris bumi, posisi titik, sistem koordinat, proyeksi.

| Sub-bidang | Topik Utama |
|------------|-------------|
| **Reference Ellipsoid** | [[Reference Ellipsoid]], [[GRS80]], [[WGS84]], flattening $f $, eccentricity $ e $ |
| **Coordinate Systems** | [[Geodetic Coordinates]] ($\phi,\lambda,h $), [[Geocentric Cartesian ECEF]] ($ X,Y,Z $), [[Local ENU NEU]] |
| **Geodesic Problems** | Direct/inverse geodesic, [[Vincenty Formula]], [[GeographicLib]] |
| **Map Projections** | [[Map Projection]], [[UTM]], [[Transverse Mercator]], [[Mercator]], TM3° (Indonesia) |
| **Datum & Transformations** | [[Datum]], [[Horizontal Datum]], [[Datum Transformation]], [[Helmert Transformation]] |
| **Reference Frames** | [[ITRF]], [[ITRF2020]], [[ETRS89]], [[WGS84]], [[NAD83]] |

**Key Formulae**:

- **Geodetic ↔ Cartesian**:

$ $ X = (N+h)\cos\phi\cos\lambda,\quad Y = (N+h)\cos\phi\sin\lambda,\quad Z = (N(1-e^2)+h)\sin\phi $$

where $ N = \frac{a}{\sqrt{1-e^2\sin^2\phi}} $ (radius of curvature in prime vertical)

- **Vincenty Inverse**: Iterative solution for $ s, \alpha_1, \alpha_2 $ given $ (\phi_1,\lambda_1), (\phi_2,\lambda_2) $- **Helmert 7-param**: $\mathbf{X}_B = \mathbf{X}_A + \mathbf{T} + (1+s)\mathbf{R}\mathbf{X}_A $---

### 2. Physical Geodesy (Geodesi Fisis)
> **Fokus**: Bidang gravitasi bumi, geoid, tinggi, potensial.

| Konsep Kunci | Formula / Deskripsi |
|--------------|---------------------|
| **Gravity Potential** | $ W(\mathbf{r}) = V(\mathbf{r}) + \Phi(\mathbf{r}) $ (gravitasi + sentrifugal) |
| **Normal Potential** | $ U(\mathbf{r}) $— potensial elipsoid referensi (GRS80) |
| **Disturbing Potential** | $ T = W - U $ |
| **Gravity Anomaly** | $\Delta g = g_P - \gamma_Q $ (Bouguer, free-air, isostatic) |
| **Geoid** | $ W = W_0 $ (permukaan equipotensial $\approx $ MSL) |
| **Geoid Undulation** | $ N = \frac{T}{\gamma} $ (Bruns formula) |
| **Height Systems** | [[Orthometric Height]] $ H $, [[Ellipsoidal Height]] $ h $, [[Vertical Datum]] |

**Key Formulae**:

- **Bruns Formula**: $ N = \frac{T_P}{\gamma_P} $- **Stokes Integral**: $ N = \frac{R}{4\pi\gamma} \iint \Delta g \, S(\psi) \, d\sigma $- **Fundamental Eq. Physical Geodesy**: $\frac{\partial T}{\partial h} + \frac{2}{R}T = -\Delta g $ (Molodensky)

- **Normal Gravity (GRS80)**: $\gamma(\phi) = \gamma_e \frac{1+k\sin^2\phi}{\sqrt{1-e^2\sin^2\phi}} $---

### 3. Satellite Geodesy (Geodesi Satelit)
> **Fokus**: Penggunaan satelit buatan untuk penetapan orbit, posisi, gravitasi, rotasi bumi.

| Teknik | Prinsip | Aplikasi Utama |
|--------|---------|----------------|
| **GNSS** (GPS, Galileo, GLONASS, BeiDou) | Trilaterasi berbasis rentang kode & fase carrier | Positoning (cm-mm), ITRF, survei, navigasi |
| **SLR** (Satellite Laser Ranging) | Pengukuran jarak laser ke satelit (LAGEOS, LARES) | Pusat massa bumi, skala ITRF, rotasi |
| **VLBI** (Very Long Baseline Interferometry) | Interferometri baseline antar radioteleskop ke kuasar | Rotasi bumi (UT1, polar motion), skala ITRF, frame inersial |
| **DORIS** (Doppler Orbitography) | Doppler shift sinyal radio dari beacon darat | Orbit presisi, ITRF, ionosfer |
| **Satellite Altimetry** | Radar/laser altimeter ke permukaan laut | Mean sea level, geoid marin, sirkulasi laut |
| **Gravity Missions** (GRACE, GRACE-FO, GOCE) | Gravimetri satelit (inter-satellite ranging, gradiometer) | Model gravitasi global, perubahan massa, geoid |

**Key Formulae**:

- **GNSS Pseudorange**: $ P = \rho + c(\delta t_r - \delta t^s) + I + T + \epsilon $- **GNSS Carrier Phase**: $\Phi = \rho + c(\delta t_r - \delta t^s) - I + T + \lambda N + \epsilon $- **SLR Range**: $\rho = \frac{c}{2}\Delta t $- **VLBI Delay**: $\tau = \frac{\mathbf{b}\cdot\mathbf{s}}{c} + \text{clock} + \text{atmo} + \text{relativistic} $---

### 4. Astronomical Geodesy (Geodesi Astronomi)
> **Fokus**: Pengukuran arah (azimuth), latitude, longitude, waktu, rotasi bumi via pengamatan bintang.

| Observasi | Instrumen | Hasil |
|-----------|-----------|-------|
| **Latitude (Talcott)** | Zenith telescope / CCD astrolabe | $\phi $ astronomis |
| **Longitude** | Time transfer (GNSS, VLBI) + UT1 | $\lambda $ astronomis |
| **Azimuth** | Gyrotheodolite / Solar/Star obs | $ A $ astronomis |
| **Polar Motion** | VLBI, SLR, GNSS, DORIS | $ x_p, y_p $ (IERS) |
| **UT1 / LOD** | VLBI, LLR | Rotasi bumi |

**Relasi ke Geodesi Geometrik**

$ $\phi_{\text{astro}} = \phi_{\text{geod}} + \xi, \quad \lambda_{\text{astro}} = \lambda_{\text{geod}} + \frac{\eta}{\cos\phi} $$

where $\xi, \eta $= deflection of vertical (DOV) dari $ T $.

---

### 5. Geodynamics / Crustal Deformation (Geodinamika / Deformasi Kerak)
> **Fokus**: Perubahan posisi, gravitasi, rotasi bumi seiring waktu.

| Fenomena | Skala Waktu | Metode Pengukuran |
|----------|-------------|-------------------|
| **Plate Tectonics** | Tahun–Dekade | GNSS kontinual, SLR, VLBI |
| **Earthquake Cycle** | Detik–Dekade | GNSS, InSAR, leveling |
| **Glacial Isostatic Adjustment (GIA)** | Ribuan tahun | GRACE, GNSS, sea level |
| **Subsidence/Uplift** | Bulan–Tahun | InSAR, GNSS, leveling |
| **Polar Motion** | Hari–Dekade | VLBI, SLR, GNSS |
| **Length of Day (LOD)** | Hari–Dekade | VLBI, LLR |

---

## 🌐 Earth Shape & Reference Surfaces (Bentuk Bumi & Permukaan Referensi)

| Model | Deskripsi | Parameter Utama |
|-------|-----------|-----------------|
| **Sphere** | Bola sempurna | $ R \approx 6371 \text{ km} $ |
| **Ellipsoid of Revolution** | Elipsoid rotasi (oblate spheroid) | $ a $ (semi-major),$ b $ (semi-minor),$ f = \frac{a-b}{a} $, $ e^2 = 2f - f^2 $ |
| **Geoid** | Permukaan equipotensial $ W=W_0 $ | $ N(\phi,\lambda) $— undulasi geoid |
| **Topography** | Permukaan nyata bumi (daratan + laut) | DEM, DTM, DSM |
| **Quasi-geoid** | Permukaan referensi tinggi normal | $\zeta $— height anomaly |

**Standard Ellipsoids**:
| Ellipsoid | $ a $ (m) | $ 1/f $ | Digunakan |
|-----------|---------|-------|-----------|
| **GRS80** | 6,378,137 | 298.257222101 | ITRF, WGS84, NAD83, ETRS89 |
| **WGS84** | 6,378,137 | 298.257223563 | GPS, WGS84 (G1150+) |
| **Bessel 1841** | 6,377,397.155 | 299.1528128 | Indonesia lama (datum lama) |
| **WGS72** | 6,378,135 | 298.26 | Legacy |

---

## 📍 Coordinate Systems & Reference Frames (Sistem Koordinat & Frame Referensi)

### Hierarki Frame Referensi
| Level | Frame | Realisasi | Skala |
|-------|-------|-----------|-------|
| **Inertial** | ICRF (International Celestial Reference Frame) | VLBI ke kuasar | Galaktik |
| **Earth-Fixed (Global)** | **ITRF** (ITRF2020, ITRF2014) | Kombinasi GNSS+SLR+VLBI+DORIS | Global (mm) |
| **Earth-Fixed (Regional)** | ETRS89 (Eropa), NAD83 (AMS), SIRGAS (AmLat), **TSSGI/ITRF (Indonesia)** | Densifikasi regional | Regional (mm-cm) |
| **Local/Project** | Proyek survei, konstruksi | Total station, GNSS RTK | Lokal (mm) |

### Jenis Koordinat
| Sistem | Koordinat | Konversi Utama |
|--------|-----------|----------------|
| **Geodetic (Curvilinear)** | $\phi $ (lat),$\lambda $ (lon),$ h $ (ht) |$\leftrightarrow $ Cartesian |
| **Geocentric Cartesian (ECEF)** | $ X, Y, Z $|$\leftrightarrow $ Geodetic |
| **Local Tangent Plane (ENU/NEU)** | $ E, N, U $ (atau $ N, E, U $) | Rotasi dari ECEF di titik asal |
| **Projected (Grid)** | $ E, N $ (easting, northing) | Proyeksi dari geodetic (UTM, TM3) |

---

## 📏 Measurement Techniques (Teknik Pengukuran)

| Teknik | Prinsip | Instrumen | Akurasi | Aplikasi |
|--------|---------|-----------|---------|----------|
| **GNSS/GPS** | Trilaterasi satelit (kode + fase) | Receiver GNSS (geodetik) | mm–cm (RTK/PPP) | Positioning, navigasi, ITRF |
| **Total Station / Teodolit** | Sudut horizontal/vertikal + EDM | Total station robotik | mm–cm (jarak), arc-sec (sudut) | Survei detail, stakeout, deformasi |
| **Leveling (Spirit/Barcode)** | Perbedaan tinggi via garis pandang horizontal | Level optik/digital + rod | 0.5–2 mm/$\sqrt{\text{km}} $ | Jaring kontrol tinggi, deformasi presisi |
| **InSAR** | Interferometri fasa radar satelit | Sentinel-1, ALOS, TerraSAR-X | mm–cm (LOS) | Deformasi luas, subsidensi |
| **LiDAR** | Laser scanning (airborne/terrestrial/mobile) | LiDAR scanner | cm (3D point cloud) | DEM, 3D mapping, corridor |
| **Photogrammetry** | Triangulasi fotogrametri (aerial/UAV) | Kamera metrik / UAV | cm (GSD-dependent) | Ortophoto, DSM, 3D model |
| **Gravimetry** | Percepatan gravitasi | Gravimeter absolut/relatif | $\mu\text{Gal} $ (abs), mGal (rel) | Geoid, geofisika, minyak/gas |
| **Altimetry** | Radar/laser ke permukaan laut | Jason, Sentinel-6, CryoSat | cm (sea surface) | Mean sea level, geoid marin |

---

## 🏗️ Role in Engineering & Surveying (Peran di Rekayasa & Survei)

| Bidang Rekayasa | Peran Geodesi | Contoh Aplikasi |
|-----------------|---------------|-----------------|
| **Surveying & Mapping** | Dasar semua pemetaan, kontrol horizontal & vertikal | Jaring kontrol geodesi, peta dasar, ortofoto |
| **Construction Engineering** | Stakeout, alignment, deformasi monitoring | Jalan, jembatan, gedung tinggi, bendungan |
| **Transportation** | Alignmen rel/jalan, navigasi GNSS | Kereta cepat, tol, navigasi laut/udara |
| **Hydrographic Survey** | Datum vertikal (CD, MSL), positioning laut | Carta nautika, pipeline, lepas pantai |
| **Cadastral / Land Admin** | Batas tanah, sertifikasi, PPAR | Pendaftaran tanah, batas administratif |
| **Geodynamics / Hazard** | Deformasi tektonik, subsidensi, GIA | Mitigasi gempa, tsunami, banjir bandang |
| **Navigation / GNSS** | ITRF, orbit, klok, ionosfer | Navigasi otomotif, penerbangan, pelayaran |
| **Remote Sensing** | Georeferensi citra, ortorektifikasi | Penginderaan jauh, monitoring lingkungan |
| **GIS / Spatial Data** | Datum, proyeksi, transformasi, metadata | Basis data spasial, analisis geospasial |

---

## 📐 Fundamental Formulae Summary (Ringkasan Rumus Fundamental)

| Kategori | Rumus Kunci |
|----------|-------------|
| **Elipsoid** | $ N = \frac{a}{\sqrt{1-e^2\sin^2\phi}} $, $ M = \frac{a(1-e^2)}{(1-e^2\sin^2\phi)^{3/2}} $ |
| **Geodetic↔Cartesian** | $ X=(N+h)\cos\phi\cos\lambda,\; Y=(N+h)\cos\phi\sin\lambda,\; Z=(N(1-e^2)+h)\sin\phi $ |
| **Geodesic (Vincenty)** | Iteratif: $\lambda \leftarrow L + (1-C)f\sin\alpha \dots $ |
| **Height Systems** | $ h = H + N = H^N + \zeta $ |
| **Bruns** | $ N = T/\gamma $ |
| **Stokes** | $ N = \frac{R}{4\pi\gamma}\iint\Delta g\,S(\psi)d\sigma $ |
| **Molodensky** | $\zeta = \frac{\Delta g}{\gamma}H + \dots $ |
| **Helmert (7-param)** | $\mathbf{X}_B = \mathbf{X}_A + \mathbf{T} + (1+s)\mathbf{R}\mathbf{X}_A $ |
| **GNSS Obs** | $ P = \rho + c\delta t_r - c\delta t^s + I + T + \epsilon $, $\;\Phi = \rho + c\delta t_r - c\delta t^s - I + T + \lambda N + \epsilon $ |
| **Leveling** | $\Delta H = \sum (\text{backsight} - \text{foresight})$ |

---

## 📚 References (Referensi Utama)

### Textbooks (Buku Teks Standar)
1. **Hofmann-Wellenhof & Moritz**, *Physical Geodesy*, 2nd ed., Springer, 2005.
2. **Hofmann-Wellenhof, Lichtenegger & Wasle**, *GNSS — Global Navigation Satellite Systems*, Springer, 2008.
3. **Seeber**, *Satellite Geodesy*, 2nd ed., de Gruyter, 2003.
4. **Torge & Müller**, *Geodesy*, 4th ed., de Gruyter, 2012.
5. **Vaníček & Krakiwsky**, *Geodesy: The Concepts*, 2nd ed., Elsevier, 1986.
6. **Heiskanen & Moritz**, *Physical Geodesy*, Freeman, 1967 (Classic).
7. **Leick, Rapoport & Tatarnikov**, *GPS Satellite Surveying*, 4th ed., Wiley, 2015.
8. **Ghilani & Wolf**, *Adjustment Computations*, 6th ed., Wiley, 2018.

### Standards & Conventions (Standar & Konvensi)
9. **IERS Conventions (2010/2024)** — ITRF, EOP, standards.
10. **IAG Resolutions** — ITRS, IHRS, IGS standards.
11. **SNI 1748, 8067, 8435** — Standar Nasional Indonesia (Survei, Jaring Kontrol, Geodesi).
12. **BIG Technical Guidelines** — TSSGI, InaGeoid, InaCORS, Proyeksi TM3/UTM.

### Indonesian Context
13. **BIG**, *Pedoman Teknis Tata Sistem Tinggi Geodesi Indonesia (TSSGI)*, 2020/2023.
14. **BIG**, *Pedoman Teknis Jaring Kontrol Geodesi (JKG)*, SNI 8067.
15. **BRIN/BIG**, *InaGeoid / TSSGI Geoid Model 2020* — Grid files & documentation.
16. **InaCORS (BIG)**, *Real-time GNSS Correction Service & Geoid Model*.

### Key Papers
17. **Altamimi et al.**, *ITRF2020: A new realization of the ITRS*, J. Geod., 2023.
18. **Pavlis et al.**, *EGM2008 / EGM2020*, gravitational models.
19. **Rapp**, *Geoid determination*, various papers.
20. **Sideris**, *Geoid determination by FFT/Least-squares collocation*.

---

## 🔗 Related Concepts (Tautan Konsep)

- [[Vertical Datum]] — TSSGI, height systems, leveling

- [[Geoid]] / [[Geoid Undulation]] — Physical geodesy core

- [[Physical Geodesy]] — Gravity field, geoid, heights

- [[Reference Ellipsoid]] / [[GRS80]] / [[WGS84]] — Geometric reference

- [[ITRF]] / [[ITRF2020]] / [[WGS84]] — Reference frames

- [[Datum Transformation]] / [[Helmert Transformation]] — Coordinate transforms

- [[Map Projection]] / [[UTM]] / [[Transverse Mercator]] — Projections

- [[GNSS]] / [[GPS]] / [[RTK]] / [[PPP]] — Satellite positioning

- [[Least Squares Adjustment]] — Adjustment theory

- [[Map Projection]] / [[UTM]] / [[TM3]] — Indonesian projections

- [[Indonesia]] / [[TSSGI]] — Indonesian context

---

#concepts #geodesy-fundamentals #branches-of-geodesy #earth-shape #coordinate-systems #measurement-techniques #engineering-surveying