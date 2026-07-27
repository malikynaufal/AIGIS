---
title: "MGM214714 - Komputasi Awan"
subject: "Ilmu Komputer / Infrastruktur"
tags: [cloud, aws, azure, gcp, serverless, containerization, gis-cloud]
course_code: "MGM214714"
sks: 3
semester: 6
language: "id-ID"
---

# MGM214714 - Komputasi Awan

## Cloud Computing

**Course Code:** MGM214714  
**SKS:** 3 (2-1)  
**Semester:** 6  
**Prerequisites:** Jaringan Komputer, Sistem Operasi  

---

## Overview / Gambaran Umum

Komputasi Awan (Cloud Computing) adalah penyediaan sumber daya komputer (server, storage, database, jaringan, perangkat lunak) melalui internet (awan) dengan model *pay-per-use*. Untuk lembaga geodetik, cloud memungkinkan pengolahan data skala besar tanpa investasi hardware masif. Mata kuliah ini membahas tiga raksasa cloud (AWS, Azure, GCP), arsitektur serverless, containerisasi, serta deployment aplikasi GIS di cloud.

> **Catatan:** "Cloud computing adalah utilitas abad ke-21 — kita tidak perlu membangun pembangkit listrik untuk menyalakan lampu, kita juga tidak perlu membangun data center untuk mengolah data." — *Paradigma Utility Computing*

---

## 1. Fondasi Cloud

### 1.1 Service Models

| Model | Penjelasan | Contoh | Pengelolaan |
|-------|-----------|--------|-------------|
| **IaaS** (Infrastructure) | Virtual machine, jaringan, storage | AWS EC2, Azure VM | User mengelola OS & apps |
| **PaaS** (Platform) | Platform untuk deploy apps | Heroku, Google App Engine | User hanya deploy kode |
| **SaaS** (Software) | Aplikasi siap pakai | ArcGIS Online, Google Earth | Vendor mengelola semua |

### 1.2 Perbandingan Tiga Raksasa Cloud

| Aspek | AWS | Azure | GCP |
|-------|-----|-------|-----|
| Market Share | ~31% | ~25% | ~11% |
| Kekuatan Utama | Paling lengkap, komunitas | Integrasi Microsoft (Active Directory) | AI/ML (TensorFlow) & Data Analytics |
| GIS Service | — | Azure Maps | Google Earth Engine |
| Harga Compute | Kompetitif (EC2 Spot) | Kompetitif (VM B-series) | Sangat Kompetitif (Preemptible) |

## 2. Container dan Orkestrasi

### 2.1 Docker

- Container dibanding VM: lebih ringan (share kernel), startup detik.

- Dockerfile mendefinisikan image; Docker Compose mendefinisikan multi-container service.

- Penting untuk: memastikan environment pengolahan data identik di lokal dan cloud.

### 2.2 Kubernetes (K8s)

Orkestrasi container skala besar. Fitur: *self-healing*, *auto-scaling*, *rolling update*. Digunakan untuk aplikasi GIS yang butuh skalabilitas tinggi.

## 3. Serverless Computing

Tidak ada server yang dikelola; vendor menjalankan kode saat ada event.

- **AWS Lambda:** Kode dipicu oleh event S3 (misal: otomatis proses gambar satelit saat diunggah).

- **Google Cloud Functions:** Kode dipicu HTTP atau event.

- **Kekurangan:** *Cold start*, batasan timeout.

## 4. Deployment GIS di Cloud

- **Data:** Simpan raster/vector data di object storage (AWS S3, GCS) dengan format Cloud Optimized GeoTIFF (COG).

- **Serving:** Deploy GeoServer/MapServer menggunakan Docker di ECS/EKS.

- **Analisis:** Gunakan Dask/Ray di cloud cluster untuk analisis data geospasial skala petabyte.

## 5. Referensi

1. **Armbrust, M., et al.** (2010). A View of Cloud Computing. *Communications of the ACM*, 53(4), 50-58.
2. **Amazon Web Services.** [aws.amazon.com](https://aws.amazon.com)
3. **Microsoft Azure.** [azure.microsoft.com](https://azure.microsoft.com)
4. **Google Cloud.** [cloud.google.com](https://cloud.google.com)
5. **Burns, B., et al.** (2016). *Kubernetes: Up and Running*. O'Reilly.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214714. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*