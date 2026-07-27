---
title: "MGM214707 - Basis Data Terdistribusi"
subject: "Ilmu Komputer / Basis Data"
tags: [distributed-systems, database, cap-theorem, nosql, sharding, replication]
course_code: "MGM214707"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214707 - Basis Data Terdistribusi

## Distributed Databases

**Course Code:** MGM214707  
**SKS:** 3 (2-1)  
**Semester:** 5  
**Prerequisites:** Basis Data Dasar, Sistem Operasi, Jaringan Komputer  

---

## Overview / Gambaran Umum

Basis data terdistribusi (Distributed Database) adalah sistem basis data yang tersebar di beberapa lokasi fisik/node, namun terlihat sebagai satu kesatuan bagi pengguna. Dengan meledaknya data spasial (Big Data GIS) dan tuntutan ketersediaan tinggi (high availability), basis data terdistribusi menjadi krusial. Mata kuliah ini mencakup arsitektur distribusi, Teorema CAP (Consistency, Availability, Partition Tolerance), teknik sharding, replikasi data, serta perbedaan sistem SQL (NewSQL) dan NoSQL.

> **Catatan:** "Sistem terdistribusi adalah sistem di mana kegagalan komputer yang bahkan tidak Anda ketahui keberadaannya dapat membuat komputer Anda sendiri tidak bisa digunakan." — *Leslie Lamport*

---

## 1. Arsitektur dan Teorema CAP

### 1.1 Teorema CAP (Brewer)

Dalam sistem terdistribusi, kita hanya bisa menjamin **dua dari tiga** properti berikut saat terjadi *network partition*:

| Properti | Penjelasan |
|----------|------------|
| **C**onsistency | Setiap read menerima write terbaru atau error. |
| **A**vailability | Setiap request menerima respon (bukan error), tanpa jaminan data terbaru. |
| **P**artition Tolerance | Sistem tetap beroperasi meskipun komunikasi antar node putus. |

**Realita:** P (Partition Tolerance) adalah wajib dalam jaringan modern. Maka kita harus memilih antara **CP** (Consistency + Partition Tolerance) atau **AP** (Availability + Partition Tolerance).

### 1.2 Model PACELC

Perluasan CAP: Jika ada partisi (**P**), pilih **C** atau **A**; sebaliknya (**E**lse), pilih **L**atency atau **C**onsistency.

### 1.3 Konsistensi (Consistency Models)

- **Strong Consistency:** Semua client melihat data yang sama di semua node saat itu juga (sinkron).

- **Eventual Consistency:** Jika tidak ada update baru, semua akses akan mengembalikan data terbaru (asinkron).

- **Causal Consistency:** Operasi yang memiliki hubungan sebab-akibat terlihat dalam urutan yang sama.

---

## 2. Teknik Distribusi Data

### 2.1 Sharding (Horizontal Partitioning)

Membagi tabel berdasarkan kunci (sharding key).

| Metode | Deskripsi |
|--------|-----------|
| **Hash-based** | `hash(key) % node_count` — sebaran merata, susah resize. |
| **Range-based** | Berdasarkan jangkauan (misal: ID 1-1000 di Node A). |
| **Consistent Hashing** | Mengurangi pemindahan data saat penambahan/pengurangan node (ring topology). |

### 2.2 Replikasi

- **Master-Slave:** Master untuk write, slave untuk read. Risiko master gagal.

- **Multi-Master:** Semua node bisa menerima write. Risiko konflik.

- **Quorum-based (Dynamo):** Membutuhkan $R + W > N$ untuk konsistensi ($N$ = jumlah replika).

---

## 3. Jenis Basis Data

### 3.1 Relational Terdistribusi (NewSQL)

- Contoh: Google Spanner, CockroachDB.

- Fitur: ACID penuh, SQL interface, sharding otomatis.

- Cocok untuk data transaksional yang konsisten (misal: kadaster nasional).

### 3.2 NoSQL

| Tipe | Contoh | Karakteristik |
|------|--------|--------------|
| **Key-Value** | Redis, DynamoDB | Kecepatan tinggi, simple lookup. |
| **Document** | MongoDB, CouchDB | JSON/BSON, fleksibel schema. |
| **Column-family** | Cassandra, HBase | Write intensif, skala besar (BigTable model). |
| **Graph** | Neo4j, JanusGraph | Relasi kompleks (sosial, jaringan jalan). |

### 3.3 Basis Data Spasial Terdistribusi

Sistem GIS skala nasional butuh sharding spasial:

- **Quadtree/R-tree sharding:** Membagi data berdasar area geografis.

- **Geo-sharding:** `sharding_key = geo_hash(lat, lon)`.

---

## 4. Studi Kasus: Sistem GNSS Kontinyu Nasional

Sistem pengolahan data ribuan stasiun GNSS per detik:

- **Tuntutan:** High Write (data observasi), Read-intensive (pemrosesan real-time).

- **Arsitektur:**
    - **Cassandra (AP):** Write cepat, toleransi kegagalan node (karena data stasiun independen).
    - **Replikasi:** 3 node di lokasi berbeda.
    - **Consistency:** Eventual (tidak masalah jika data stasiun A delay 1 detik).
    - **Sharding:** Partition key = `station_id` + `date_hour`.

---

## 5. Referensi

1. **Kleppmann, M.** (2017). *Designing Data-Intensive Applications*. O'Reilly.
2. **Coulouris, G., et al.** (2011). *Distributed Systems: Concepts and Design*. Pearson.
3. **Tanenbaum, A. S., & van Steen, M.** (2017). *Distributed Systems*. CreateSpace.
4. **Google.** *Spanner: Google’s Globally-Distributed Database*. OSDI 2012.
5. **Lakshman, A., & Malik, P.** (2010). *Cassandra: A Decentralized Structured Storage System*. ACM SIGOPS.
6. **CockroachDB documentation.** [cockroachlabs.com/docs](https://www.cockroachlabs.com/docs)
7. **MongoDB documentation.** [mongodb.com/docs](https://www.mongodb.com/docs)

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214707. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*