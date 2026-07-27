---
title: "MGM214709 - Visi Komputer"
subject: "Ilmu Komputer / Kecerdasan Buatan"
tags: [computer-vision, image-processing, feature-detection, stereo-vision, deep-learning]
course_code: "MGM214709"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214709 - Visi Komputer

## Computer Vision

**Course Code:** MGM214709
**SKS:** 3 (2-1)
**Semester:** 5
**Prerequisites:** Pengolahan Citra Digital, Aljabar Linear

---

## Overview / Gambaran Umum

Visi Komputer (Computer Vision) adalah bidang yang melatih komputer untuk "melihat" dan menginterpretasikan dunia visual. Dari deteksi objek di foto satelit hingga navigasi robot otonom dan rekonstruksi 3D dari foto udara, visi komputer adalah mata bagi sistem geospasial modern. Mata kuliah ini mencakup teknik pengolahan citra fundamental, ekstraksi fitur (SIFT, ORB), stereo vision, dan revolusi pembelajaran mendalam (Deep Learning) untuk klasifikasi dan segmentasi gambar.

> **Catatan:** "Visi komputer adalah upaya mengembalikan makna dari piksel yang berantakan." — *Prinsip Computer Vision*

---

## 1. Fondasi Pengolahan Citra

- **Ruang Warna:** RGB, HSV, Lab (penting untuk segmentasi berdasarkan warna).

- **Filter (Konvolusi):** Smoothing (Gaussian), Sharpening (Laplacian), Edge detection (Sobel, Canny).

- **Transformasi Geometrik:** Affine, Perspective, Homography (penting untuk rektifikasi foto udara).

## 2. Ekstraksi Fitur (Feature Detection)

Metode untuk menemukan titik-titik unik pada gambar yang invariant terhadap rotasi, skala, dan pencahayaan:

- **SIFT (Scale-Invariant Feature Transform):** Sangat robust, paten (sudah expired).

- **ORB (Oriented FAST and Rotated BRIEF):** Sangat cepat, open-source, cocok untuk real-time.

- **Aplikasi:** *Image stitching* untuk membuat orthophoto.

## 3. Stereo Vision dan 3D Reconstruction

- **Epipolar Geometry:** Relasi antara dua kamera melihat titik 3D yang sama.

- **Disparity Map:** Estimasi kedalaman (depth map) berdasarkan pergeseran titik antara dua kamera (stereo).

- **SfM (Structure from Motion):** Merekonstruksi model 3D dari rangkaian foto 2D dengan posisi kamera yang tidak diketahui.

## 4. Deep Learning untuk Visi

- **CNN (Convolutional Neural Networks):** Arsitektur (ResNet, YOLO, EfficientNet).

- **Klasifikasi:** Menentukan kelas objek di gambar.

- **Deteksi:** Menentukan kotak pembatas (Bounding Box).

- **Segmentasi (Semantic/Instance):** Menentukan mask piksel untuk setiap objek (misal: membedakan jalan, vegetasi, bangunan).

## 5. Referensi

1. **Szeliski, R.** (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Springer.
2. **Hartley, R., & Zisserman, A.** (2004). *Multiple View Geometry in Computer Vision*. Cambridge Univ. Press.
3. **Goodfellow, I., et al.** (2016). *Deep Learning*. MIT Press.
4. **OpenCV Documentation.** [docs.opencv.org](https://docs.opencv.org)

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214709. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*