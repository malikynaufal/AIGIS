---
title: "MGM214716 - Manajemen Proyek TI"
subject: "Ilmu Komputer / Manajemen"
tags: [project-management, agile, scrum, risk-management, gantt]
course_code: "MGM214716"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214716 - Manajemen Proyek TI

## IT Project Management

**Course Code:** MGM214716 
**SKS:** 3 (3-0) 
**Semester:** 6 
**Prerequisites:** Pemrograman Dasar, Dasar-Dasar Manajemen 

---

## Overview / Gambaran Umum

Manajemen Proyek TI (Information Technology Project Management) adalah disiplin yang menerapkan prinsip manajemen untuk proyek teknologi informasi: perencanaan, pelaksanaan, pemantauan, dan penyelesaian. Dalam konteks geodetik, ini berlaku untuk proyek pengembangan sistem informasi geospasial, penataan jaringan GNSS nasional, dan digitalisasi data kadaster. Mata kuliah ini membahas metode Agile (Scrum, Kanban), manajemen risiko, dan alat visualisasi seperti Gantt Charts.

> **Catatan:** "Proyek yang gagal jarang karena teknologi — lebih sering karena manajemen komunikasi dan ekspektasi." — *Prinsip Manajemen*

---

## 1. Metode Manajemen

### 1.1 Perbandingan Pendekatan

| Aspek | Waterfall | Agile (Scrum) |
|-------|-----------|---------------|
| Urutan | Linier (Step-by-step) | Iteratif (Sprint) |
| Dokumentasi | Sangat lengkap | Minimal, cukup untuk bekerja |
| Perubahan | Sulit (kontrak statis) | Mudah (produktif merangkul perubahan) |
| Pengiriman | Sekali di akhir | Setiap 2-4 minggu (MVP) |
| Risiko | Ditemukan di akhir | Ditemukan lebih awal |

### 1.2 Scrum Framework

- **Tim Scrum:** 3-9 orang.

- **Product Backlog:** Daftar semua fitur yang diinginkan.

- **Sprint Backlog:** Daftar fitur yang akan dikerjakan di sprint ini (2-4 minggu).

- **Daily Scrum:** Meeting harian (15 menit): Apa yang dilakukan kemarin? Hari ini? Ada hambatan?

- **Sprint Review:** Demo fitur kepada stakeholder.

- **Sprint Retrospective:** Evaluasi proses tim.

## 2. Manajemen Risiko

### 2.1 Matriks Risiko

Probabilitas $\times$ Dampak = Skor Risiko

| Probabilitas \ Dampak | Rendah (1) | Sedang (2) | Tinggi (3) |
|-----------------------|-----------|-----------|-----------|
| **Sering (3)** | 3 | 6 | 9 |
| **Mungkin (2)** | 2 | 4 | 6 |
| **Jarang (1)** | 1 | 2 | 3 |

- Skor 7-9: Mitigasi aktif (wajib).

- Skor 4-6: Monitor & rencana cadangan.

- Skor 1-3: Diterima.

## 3. Gantt Chart

Bagan batang (bar chart) yang menampilkan jadwal proyek.

**Contoh jadwal proyek Sistem Informasi Kadaster:**

| Fase | Minggu 1-4 | Minggu 5-8 | Minggu 9-12 | Minggu 13-16 |
|------|-----------|-----------|------------|-------------|
| Analisis Kebutuhan | ████████ | | | |
| Desain Arsitektur | | ████████ | | |
| Pengembangan | | | ████████ | ████████ |
| Pengujian | | | | ████████ |
| Deployment | | | | ████████ |

## 4. Studi Kasus: Proyek Pengolahan Data GNSS

Proyek 6 bulan untuk pengolahan 50 stasiun GNSS kontinyu.

**Risiko Utama:**

- Keterlambatan pengadaan server (Prob: 2, Dampak: 3 → Skor 6): Mitigasi pakai cloud provider (AWS) sebagai backup.

- Turnover tim ahli (Prob: 3, Dampak: 3 → Skor 9): Mitigasi knowledge sharing & dokumentasi.

## 5. Referensi

1. **Project Management Institute (PMI).** (2021). *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* (7th ed.). PMI.
2. **Schwaber, K., & Sutherland, J.** (2020). *The Scrum Guide*. Scrum.org.
3. **Larman, C.** (2004). *Agile and Iterative Development: A Manager's Guide*. Addison-Wesley.
4. **Gantt, H. L.** (1910). *Work, Wages and Profit*. Engineering Magazine.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214716. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*