# Survei Kadastral (*Cadastral Survey*)

**Kode:** TKD213509
**Sifat:** Wajib (Compulsory)
**SKS:** 3
**Prerequisites:** Administrasi Pertanahan, Survei Topografi

---

## 1. Overview

A cadastral survey (*survei kadastral*) is the systematic process of identifying, measuring, and recording the boundaries and area of land parcels for legal and administrative purposes. In Indonesia, cadastral surveys are conducted by licensed surveyors (*surveyor berlisensi*) under the framework of **PP 24/1997** (Land Registration Regulation) and supervised by **ATR/BPN** (*Kementerian Agraria dan Tata Ruang / Badan Pertanahan Nasional*).

---

## 2. Legal Framework

### 2.1 Primary Legislation

| Regulation | Description | Key Provisions |
|-----------|-------------|----------------|
| **UUPA No. 5/1960** | Fundamental Agrarian Law | All land rights, Hak Milik definition |
| **PP 24/1997** | Land Registration | Procedures, certificate types |
| **PP 18/2021** | ATR/BPN Authority | Institutional reform |
| **PP 40/1996** | Hak Guna Usaha | HGU terms and conditions |
| **PP 38/1963** | Hak Guna Bangunan | HGB provisions |
| **PP 40/2007** | Hak Pakai | HP provisions |
| **PP 36/2005** | Hak Guna Bangunan | Updated HGB regulations |

### 2.2 UUPA No. 5/1960 — Key Articles

- **Article 2:** All land is state property (*Bumi adalah pokok-pokok kemakmuran rakyat*)
- **Article 49:** State controls land; no individual holds ultimate ownership
- **Article 14:** Hak Milik can only be owned by WNI (Indonesian citizens)
- **Article 24:** Hak Guna Usaha for agricultural exploitation
- **Article 42:** Hak Guna Bangunan for buildings on state/private land
- **Article 28:** Hak Pakai on state land

### 2.3 Surveyor Requirements

Under **SK Menteri Agraria No. 10/1988**:

| Category | Minimum SKS | Education | Supervision |
|----------|------------|-----------|-------------|
| **Surveyor Penyelia** | 60 SKS | SMA + course | Government surveyor |
| **Surveyor Perencana** | 180 SKS | D3/S1 | Independent |
| **Surveyor Pemegang** | 400 SKS | S1 | Certified |

---

## 3. Boundary Definition (*Penetapan Batas*)

### 3.1 Types of Boundaries

| Type | Definition | Authority |
|------|-----------|-----------|
| **Batas alam** | Natural features (rivers, ridges) | Nature |
| **Batas buatan** | Artificial features (walls, fences) | Owner |
| **Batas hukum** | Legal boundaries per documents | Law |
| **Batas perjanjian** | Agreed boundaries between parties | Contract |
| **Batas negara** | International borders | State |

### 3.2 Boundary Evidence

Boundary determination is based on **5 evidences** (*5 alat bukti*), listed in order of hierarchy under **PP 24/1997**:

| Priority | Evidence | Description |
|----------|----------|-------------|
| 1 | **Sertipikat** | Existing title certificate with Peta Bidang Tanah (PBT) |
| 2 | **Surat Gambar (PBT)** | Registered parcel map |
| 3 | **Akta Notaris/PPAT** | Land transaction deed |
| 4 | **Bukti perolehan lainnya** | Other evidence of acquisition |
| 5 | **Bukti lain yang cukup** | Other sufficient evidence |

### 3.3 Methods of Boundary Establishment

1. **Survei awal** (initial survey) — for unregistered land
2. **Penegasan batas** (boundary reaffirmation) — for previously surveyed land
3. **Ukur dan gambar** (measure and map) — complete re-survey
4. **Revisi PBT** (parcel map revision) — corrections to existing maps

---

## 4. Survey Methodology

### 4.1 Pre-Survey Preparation

1. **Document collection** (*pengumpulan bukti*)
   - Existing PBT (parcel map)
   - Title certificates (*sertipikat*)
   - Transaction deeds (*akta jual beli*)
   - Previous survey records
   - SPPT PBB (tax assessment)

2. **Coordination with parties** (*koordinasi*)
   - Landowner present
   - Neighboring landowners
   - Village head (*kepala desa/lurah*)

3. **Site visit** (*kunjungan lapangan*)
   - Initial reconnaissance
   - Boundary feature identification
   - Photo documentation (4 directions)

### 4.2 Field Measurement Methods

#### Method 1: Intersection (Sudut Silang)

For each boundary point, observe angles to two or more known points:

$$d = \frac{a \cdot \sin A}{\sin(A+B+C)}$$

where $a$ is the distance between known points, and $A, B, C$ are the observed angles.

**Advantages:** Does not require linear measurement, efficient for urban parcels
**Disadvantages:** Requires line-of-sight, error propagation

#### Method 2: Traversing (*Traversing*)

A series of connected survey stations measuring angles and distances:

$$x_B = x_A + d \cdot \cos\alpha$$
$$y_B = y_A + d \cdot \sin\alpha$$

**Angular misclosure check:**

$$f_{\text{angular}} = \sum\beta - (2n - 4) \cdot 90°$$

**Linear misclosure:**

$$f_{\text{linear}} = \sqrt{(f_x)^2 + (f_y)^2}$$

$$\text{Relative precision} = \frac{f_{\text{linear}}}{\text{perimeter}}$$

**Required precision for cadastral surveys:**
| Survey Class | Relative Precision |
|-------------|-------------------|
| Class I (urban) | 1:20,000 or better |
| Class II (rural) | 1:10,000 |
| Class III (forest) | 1:5,000 |

#### Method 3: GNSS/RTK

Direct positioning of boundary points using GNSS:
- **RTK accuracy:** ±2 cm horizontal, ±3 cm vertical
- **Observation time:** 5–10 seconds per point
- **Base station:** Local or INACORS reference station
- **Network RTK (RTN):** Preferred for urban areas

### 4.3 Area Calculation

#### Trapezoidal Rule (Koordinat Method)

$$A = \frac{1}{2} \left| \sum_{i=1}^{n} (x_i \cdot y_{i+1} - x_{i+1} \cdot y_i) \right|$$

**Requirements:**
- Coordinates must be in a local or UTM system
- Points must be in sequence (clockwise or counterclockwise)
- $x_{n+1} = x_1$, $y_{n+1} = y_1$ (closing the polygon)

#### Measured Distance Method

$$A = \frac{1}{2} \sum_{i=1}^{n} d_i \cdot \sin\alpha_i$$

where $d_i$ is the measured distance and $\alpha_i$ is the internal angle.

---

## 5. Indonesia's Land Registration Programs

### 5.1 PTSL (*Pendaftaran Tanah Sistematis Lengkap*)

Systematic Land Registration program — the flagship land registration initiative:

| Aspect | Detail |
|--------|--------|
| **Launched** | 2017 |
| **Target** | 126.5 million parcels nationwide |
| **Coverage** | All land parcels in Indonesia |
| **Subsidized** | Government-funded for land below certain value |
| **Method** | Simultaneous survey of entire village (*desa/kelurahan*) |

**PTSL Process:**
```
1. Persiapan (Planning) — village mapping, socialization
   ↓
2. Pengumpulan Data (Data Collection) — field survey, boundary confirmation
   ↓
3. Pemeriksaan dan Pengukuran (Examination and Measurement) — verification
   ↓
4. Penyelesaian Peralihan (Resolution of disputes) — conflict resolution
   ↓
5. Penerbitan Sertipikat (Certificate issuance) — delivery to landowner
```

### 5.2 UUPA-Based Land Classification

All land in Indonesia is classified as:

1. **Tanah Negara** (State land) — unclaimed land
2. **Tanah Hak** (Righted land) — land with registered rights
3. **Tanah Adat** (Customary land) — recognized under local custom
4. **Tanah Negara** — includes most land that hasn't been formally registered

### 5.3 TORA (*Tanah Objek Reforma Agraria*)

Land redistribution program that targets:
- Abandoned land (*tanah terlantar*)
- Government land (*tanah negara/kas desa*)
- Underutilized state land

---

## 6. Cadastral Survey Documentation

### 6.1 Required Documents

| Document | Purpose |
|----------|---------|
| **Berita Acara** (Report of Proceedings) | Survey documentation |
| **Surat Pernyataan** (Statement Letter) | Boundary agreement |
| **Peta Survei** (Survey Map) | Technical parcel map |
| **Peta Bidang Tanah** (PBT) | Registered parcel map |
| **Sertipikat** (Certificate) | Land right title |
| **Surat Tanda Terima Berkas** | Document receipt |

### 6.2 PBT (Parcel Map) Requirements

| Element | Content |
|---------|---------|
| **Title block** | Survey type, date, surveyor |
| **Scale** | 1:1000 or 1:500 for urban; 1:2500 for rural |
| **Contour** | For hilly areas |
| **Coordinate system** | Local grid or UTM |
| **Area** | In square meters |
| **Boundary dimensions** | All side lengths |
| **Reference points** | Tie points, station marks |
| **Adjacent parcels** | Neighbor identification |

### 6.3 Map Standard Specifications

$$\text{Plan accuracy} = \frac{\text{Plan accuracy (cm)}}{\text{Map scale denominator}} \times 100 = \text{cm per meter}$$

Example: 1:1000 scale with ±5 cm plan accuracy = 0.05 cm/100 cm = 0.05%

---

## 7. Survey Instruments and Tools

| Instrument | Accuracy | Application |
|-----------|----------|-------------|
| **Total station** | ±1" angle, ±2 mm distance | Primary survey |
| **RTK GNSS** | ±2 cm horizontal | Positioning |
| **Measuring tape** | ±1 mm | Minor measurements |
| **Steel chain** | ±5 mm/30 m | Traditional method |
| **Compass** | ±0.5° | Direction (supplementary) |
| **Measuring wheel** | ±1% | Approximate distances |

### 7.1 Total Station Configuration for Cadastral

**Setup:**
1. Occupy known control point (Trikoras)
2. Back-sight to second control point
3. Confirm orientation (angle should match)
4. Measure to boundary points

**Angular measurement:**
- 1 set of directions (4 observations per point: 0°, 90°, 180°, 270°)
- Face Left (FL) and Face Right (FR) observations

**Distance measurement:**
- Horizontal distances preferred
- Vertical distances for elevation
- Slope distances reduced to horizontal

---

## 8. Quality Control

### 8.1 Internal Checks

| Check | Method | Tolerance |
|-------|--------|-----------|
| Angular misclosure | $\sum\beta - (2n-4) \times 90°$ | < 10" for traverse |
| Linear misclosure | $\sqrt{f_x^2 + f_y^2}$ | 1:15,000 minimum |
| Perimeter check | Measured vs. calculated | < 1% |
| Area check | 2 methods compared | < 0.5% |

### 8.2 External Checks

- Independent re-measurement
- GNSS verification of corner points
- ATR/BPN audit

### 8.3 Common Errors

| Error Source | Magnitude | Prevention |
|-------------|-----------|------------|
| Instrument centering | 1–3 mm | Force centering |
| Point identification | 1–50 mm | Permanent marks |
| Reading errors | 1–5 mm | Multiple observations |
| Temperature expansion | 1–5 mm | Temperature correction |
| Prismatic refraction | 1–2 mm | Observation procedures |
| Human error | Variable | Double-checking |

---

## 9. Technology in Modern Cadastral Survey

### 9.1 GNSS-Based Cadastral Survey

- **RTK/RTN:** ±2 cm accuracy for boundary points
- **CORS network:** INACORS stations throughout Indonesia
- **Advantages:** No need for通視 (line of sight between stations)
- **Challenges:** Canopy obstruction, limited in forested areas

### 9.2 UAV for Cadastral

- **Photo mosaic:** Orthophoto for boundary verification
- **3D model:** Building footprints from SfM
- **Advantages:** Visual documentation, area verification
- **Limitations:** Cannot replace ground control; not acceptable as sole evidence for boundaries

### 9.3 GIS Integration

- **Database management** of parcel records
- **Spatial analysis** for overlapping claims
- **Web GIS** for public access to land records
- **Mobile GIS** for field survey data collection

---

## 10. Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Trapezoidal area | $A = \frac{1}{2}|\sum(x_iy_{i+1} - x_{i+1}y_i)|$ |
| Distance from coords | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Bearing (azimuth) | $\alpha = \arctan\frac{y_2-y_1}{x_2-x_1}$ |
| Linear misclosure | $f = \frac{\sqrt{f_x^2+f_y^2}}{\text{perimeter}} \leq \frac{1}{N}$ |
| Angular misclosure | $f_{ang} = \sum\beta - (2n-4) \times 90°$ |

---

## References

1. UU No. 5/1960 — *Undang-Undang Pokok Agraria*
2. PP 24/1997 — *Pendaftaran Tanah*
3. PP 18/2021 — *ATR/BPN*
4. SK Menteri Agraria No. 10/1988 — *Pedoman Pelaksanaan Survei Pemetaan Kadastral*
5. Permen ATR No. 18/2017 — *Tata Cara Pendaftaran Tanah Sistematis Lengkap*
6. World Bank (2018). *Land Registration in Indonesia: An Assessment*.
7. BPN (2021). *Pedoman Pelaksanaan PTSL*.
8. FIG (2014). *Land Tenure and Cadastral Survey*.

---

## Catatan Kuliah

*Catatan perkuliahan akan disimpan di sini.*

## Tugas dan Proyek

*Daftar tugas dan proyek terkait mata kuliah ini.*
