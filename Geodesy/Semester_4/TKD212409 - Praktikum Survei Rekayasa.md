# Praktikum Survei Rekayasa

**Kode:** TKD212409 
**Sifat:** Wajib 
**SKS:** 1 

## Deskripsi

Praktikum ini memberikan pengalaman praktis dalam survei rekayasa meliputi penggunaan total station, level, setting out, dan pengukuran presisi untuk proyek konstruksi.

## Catatan Kuliah

### Alat Ukur Survei Rekayasa

#### 1. Total Station
Total station menggabungkan theodolite digital dan EDM (Electronic Distance Measurement).

**Akurasi Pengukuran:**

$$\text{Error Horizontal} = \sqrt{(1")^2 + (1 \text{ ppm})^2 \times D}\text{Error Vertical} = \sqrt{(1")^2 + (1 \text{ ppm})^2 \times D} $$Dimana:
-$1"$= akurasi sudut
-$1 $ppm = akurasi jarak
-$D$= jarak pengukuran (meter)

#### 2. Digital Level
**Akurasi Perhitungan:*
*

$$\text{Precision} = \sqrt{\sum_{i=1}^{n} \frac{(h_i - \bar{h})^2}{2n(n-1)}} $$

#### 3. GPS/GNSS RTK
**Akurasi RTK:**

$$\text{Horizontal Error} = \sqrt{(10 \text{ mm} + 1 \text{ ppm} \times D)^2}\text{Vertical Error} = \sqrt{(15 \text{ mm} + 1.5 \text{ ppm} \times D)^2} $$### Metode Setting Out

#### Setting Out Bangunan
1. **Persiapan**: Studi gambar rencana, penentuan titik control
2. **Pencarian Titik**: Tentukan posisi titik pada site plan
3. **Transfer Koordinat**: Hitung jarak dan sudut dari control station
4. **Marking**: Tandai titik dengan patok/beton

#### Formula Setting Out:$$\begin{aligned}
\text{Distance} &= \sqrt{(N_P - N_A)^2 + (E_P - E_A)^2} \\
\text{Azimuth} &= \arctan\left(\frac{E_P - E_A}{N_P - N_A}\right) + \text{correction}
\end{aligned} $$### Precision Levelling
**Prosedur:**
1. Setup level pada posisi tengah
2. Backsight ke benchmark
3. Foresight ke titik pengukuran
4. Hitung elevation difference
5. Loop closure check

**Persyaratan Akurasi:*
*

$$\text{Max Misclosure} = \pm 3\sqrt{K} \text{ mm} $$

Dimana:
-$K$ = jarak total levelling (kilometer)

### Deformasi Monitoring
**Monitoring周期 (Period):**

- Daily: untuk konstruksi aktif

- Weekly: untuk struktur stabil

- Monthly/Yearly: untuk monitor jangka panjang

### Safety and Procedure
**Keselamatan Kerja:**
1. Gunakan APAR (Alat Pelindung Alat Kerja)
2. Koordinasi dengan foreman
3. Perhatikan traffic management
4. Pastikan alat dalam kondisi baik

## Tugas dan Praktikum

### Tugas 1: Total Station Operation
**Objektif:** Melatih pengoperasian total station untuk setting out

**Prosedur:**
1. Setup total station pada control station
2. Orientasi ke north point
3. Hitung jarak dan sudut ke titik setting
4. Tandai titik dengan pin marker

**Laporan:**

- Gambar situasi

- Data pengukuran

- Evaluasi akurasi

### Tugas 2: Digital Level Precision
**Objektif:** Melatih penggunaan digital level untuk precision levelling

**Prosedur:**
1. Setup level di antara benchmark dan titik pengukuran
2. Baca backsight dan foresight
3. Loop measurement untuk verifikasi akurasi
4. Hitung misclosure

**Laporan:**

- Field book

- Calculation sheet

- Elevation profile

### Tugas 3: Deformation Monitoring
**Objektif:** Melatih monitoring pergerakan struktur

**Prosedur:**
1. Instal monitoring points
2. Establish base control network
3. Periodic measurement (2 kali pengukuran)
4. Analisis pergerakan

**Laporan:**

- Monitogram

- Displacement diagram

- Analysis report

### Tugas 4: GPS/GNSS RTK Survey
**Objektif:** Penggunaan RTK untuk coordinate determination

**Prosedur:**
1. Setup base station atau gunakan CORS
2. Kalibrasi rover
3. Measurement points
4. Download dan proses data

### Proyek Kelompok
1. **Site Survey**: Survey seluruh area proyek dengan semua metode
2. **Setting Out Plan**: Buat rencana setting out untuk gedung bertingkat
3. **Monitoring System**: Rancang sistem monitoring untuk struktur

### Penilaian

- **Laporan Tugas (40%)**: Laporan dari 4 tugas praktikum

- **Proyek Akhir (35%)**: Proyek survei rekayasa komprehensif

- **Kemampuan Praktis (15%)**: Evaluasi keterampilan penggunaan alat

- **Presentasi (10%)**: Presentasi proyek dan diskusi