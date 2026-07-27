---
title: "MGM214702 - Teori Graf Terapan"
subject: "Matematika Terapan / Ilmu Komputer"
tags: [graph-theory, network-analysis, shortest-path, trees, euler, hamiltonian]
course_code: "MGM214702"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214702 - Teori Graf Terapan

## Applied Graph Theory

**Course Code:** MGM214702
**SKS:** 3 (3-0)
**Semester:** 5
**Prerequisites:** Konsep Dasar Pemrograman, Matematika Diskrit

---

## Overview / Gambaran Umum

Teori graf (graph theory) adalah cabang matematika yang mempelajari struktur relasi antar objek. Graf terdiri dari **simpul (vertices)** dan **sisi (edges)** yang menghubungkan pasangan simpul. Aplikasi mencakup jaringan transportasi, routing data komputer, jaringan sosial, analisis genom, perencanaan kota, dan penentuan jalur terpendek dalam GNSS. Mata kuliah ini mencakup konsep fundamental graf (pohon, konektivitas), teorema klasik (Euler, Hamilton), algoritma jalur terpendek (Dijkstra, Bellman-Ford), serta analisis jaringan modern termasuk flow network dan spectral graph theory.

> **Catatan:** "Teori graf lahir dari masalah Tujuh Jembatan Königsberg (1736) — Euler membuktikan tidak ada jalan yang menyeberangi setiap jembatan tepat sekali." — *Asal-usul topologi dan graf*

---

## 1. Konsep Dasar Graf

### 1.1 Definisi Formal

**Graf tidak terarah:** $G = (V, E) $ di mana $  V $ adalah himpunan simpul dan $  E \subseteq \binom{V}{2} $ (himpunan pasangan tak-terurut).

**Graf terarah (digraf):**$ G = (V, E) $ dengan $  E \subseteq V \times V $ (urutan penting: $  e = (u, v)$).

### 1.2 Istilah Penting

| Istilah | Definisi | Notasi |
|---------|----------|--------|
| **Derajat** | Jumlah sisi yang bersisian dengan simpul | $\deg(v) $ |
| **Derajat masuk** (digraf) | Jumlah sisi masuk ke $ v $ | $\deg^-(v) $ |
| **Derajat keluar** (digraf) | Jumlah sisi keluar dari $ v $ | $\deg^+(v) $ |
| **Jalur (path)** | Urutan simpul berurutan terhubung | $ P = (v_0, v_1, \dots, v_k) $ |
| **Siklus (cycle)** | Jalur tertutup tanpa simpul ulangan (kecuali awal=akhir) | $ C_k $ |
| **Graf terhubung** | Ada jalur antara setiap pasangan simpul | $ G $ connected |
| **Graf lengkap** | Setiap pasangan simpul terhubung | $ K_n $ |
| **Bipartit** | $ V = V_1 \cup V_2 $, sisanya antara $ V_1 $ dan $ V_2 $ | $  G = (V_1, V_2, E) $ |
| **Pohon (tree)** | Graf terhubung tanpa siklus | $|E| = |V| - 1 $ |
| **Forest** | Graf tanpa siklus (kumpulan pohon) | — |

### 1.3 Teorema Dasar

**Lemma jabat tangan (Handshaking Lemma):*
*

$ $\sum_{v \in V} \deg(v) = 2|E| $$

**Korolari:** Jumlah simpul berderajat ganjil selalu genap.

**Teorema (Graf bipartit):**$ G $ adalah graf bipartit $\iff $ $  G $ tidak mengandung siklus ganjil.

**Teorema (Graf pohon):** Untuk graf $ G $ dengan $  n $ simpul

$ $  G \text{ adalah pohon} \iff G \text{ terhubung dan } |E| = n - 1 \iff G \text{ terhubung dan tanpa siklus} \iff G \text{ tidak ada siklus dan } |E| = n - 1 $$

# ## 1.4 Representasi Graf

| Representasi | Kompleksitas Ruang | Akses Edge | Cocok Untuk |
|--------------|---------------------|------------|-------------|
| **Matriks Ketetanggaan**$A_{n \times n} $ | $ O(n^2) $ | $ O(1) $ | Graf padat (dense) |
| **List Ketetanggaan** | $ O(|V| + |E|) $ | $ O(\deg(v)) $ | Graf langka (sparse) |
| **Edge List** | $ O(|E|) $ | $ O(|E|) $ | Algoritma Kruskal |
| **Matriks Insidensi** | $ O(|V| \times |E|)$ | — | Analisis struktural |

---

## 2. Graf Euler dan Hamilton

### 2.1 Graf Euler (Eulerian Graph)

**Definisi:** *Trail* yang melewati setiap sisi tepat sekali disebut *Eulerian trail*. Jika *trail* tersebut juga kembali ke simpul awal, disebut *Eulerian circuit*.

**Teorema Euler (1736, Königsberg):**

Sebuah graf terhubung $G $ memiliki **Eulerian circuit**$\iff $ setiap simpul memiliki derajat genap.$  G $ memiliki **Eulerian trail** (bukan circuit) $\iff $ tepat ada dua simpul berderajat ganjil (kedua ujung trail).

**Algoritma Hierholzer** untuk menemukan Eulerian circuit:
1. Mulai dari sembarang simpul, ikuti sisi-sisi tak-terpakai.
2. Ketika tersangkut, masukkan siklus bagian ke dalam path.
3. Lanjutkan hingga semua sisi terpakai.

Kompleksitas: $O(|E|)$.

### 2.2 Graf Hamilton (Hamiltonian Graph)

**Definisi:** *Cycle* yang mengunjungi setiap simpul tepat sekali disebut *Hamiltonian cycle*. **Tidak ada** uji polinomial yang dikenal untuk menentukan ke-Hamiltonian.

**Kondisi Cukup:**

- **Theorem Dirac (1952):** Jika $\deg(v) \geq n/2 $ untuk setiap $  v \in V $, maka $  G $ Hamilton.

- **Theorem Ore (1960):** Jika $\deg(u) + \deg(v) \geq n $ untuk setiap pasangan takberdekatan $ u, v $, maka $  G $ Hamilton.

- **Theorem Bondy-Chvátal:** Tutup (closure) dari $ G $ adalah $ K_n \implies G $ Hamilton.

| Sifat | Graf Euler | Graf Hamilton |
|-------|-----------|---------------|
| **Objek** | Sisi (edges) | Simpul (vertices) |
| **Uji keberadaan** | Kriteria derajat, O(|E|) | NP-complete |
| **Aplikasi** | Rute pengantaran surat, jembatan Königsberg | Traveling Salesman, routing drone |
| **Algoritma** | Hierholzer $O(|E|) $ | Brute force $ O(n!) $, DP Held-Karp $ O(n^2 2^n)$ |

---

## 3. Pohon (Trees) dan Aplikasinya

### 3.1 Pohon Rentang Minimum (Minimum Spanning Tree)

Diberikan graf terhubung berbobot $G = (V, E, w)$, MST adalah subgraf pohon yang menghubungkan semua simpul dengan bobot total minimum.

**Algoritma Kruskal:**
1. Urutkan semua sisi berdasarkan bobot (ascending).
2. Ambil sisi terkecil yang tidak membentuk siklus (union-find).
3. Lanjutkan hingga $|V| - 1 $ sisi terpilih.

Kompleksitas: $ O(|E| \log |E|)$.

**Algoritma Prim:**
1. Mulai dari sembarang simpul.
2. Selalu tambahkan sisi terkecil yang menghubungkan himpunan visited ke unvisited (priority queue).
3. Lanjutkan hingga semua simpul masuk.

Kompleksitas: $O(|E| \log |V|) $ dengan binary heap.

**Teorema (Cut Property):** Untuk sembarang cut $(S, V \setminus S)$, sisi berbobot minimum yang melintasi cut tersebut pasti ada di MST.

### 3.2 Pohon Biner dan Pohon Pencarian Biner (BST)

Pohon biner di mana setiap node $x $ memenuhi:

- Semua key di subtree kiri $\leq x.key $- Semua key di subtree kanan $\geq x.key $ Operasi dasar (pencarian, sisip, hapus): $ O(h) $ dengan $  h $= tinggi pohon.

**Penyeimbangan (Balancing):**

| Struktur | Jaminan Tinggi | Operasi |
|----------|----------------|---------|
| **BST biasa** | $O(n) $ terburuk | — |
| **AVL** (1962) | $h \leq 1.44 \log_2(n+2) $ | Rotasi LR/RL |
| **Red-Black Tree** (1978) | $ h \leq 2\log_2(n+1) $ | Warna merah/hitam, rotasi |
| **Splay Tree** (1985) | Amortized $ O(\log n) $ | Splay (rotate to root) |
| **B-Tree** (1972) | $ O(\log n)$, tinggi rendah | Digunakan di basis data disk |

### 3.3 Prefix Tree (Trie)

**Trie** menyimpan string sebagai jalur dari root ke leaf. Setiap edge mewakili satu karakter.

Operasi: insert, search, prefix query — semuanya $O(m) $ di mana $ m$ = panjang kata.

Aplikasi dalam georeferencing: kompresi himpunan koordinat awalan untuk indexing spasial.

---

## 4. Jalur Terpendek (Shortest Path)

### 4.1 Algoritma Dijkstra

Untuk graf dengan bobot non-negatif $w(e) \geq 0 $:
1. Inisialisasi $ d(s) = 0 $, $ d(v) = \infty $ untuk $  v \neq s $.
2. Pilih simpul $ u $ dengan $ d(u) $ minimum yang belum di-finalisasi.
3. Relax semua edge $ (u, v) $: $ d(v) = \min(d(v), d(u) + w(u, v)) $.
4. Ulangi hingga semua simpul difinalisasi.

Kompleksitas: $ O((|V| + |E|) \log |V|)$ dengan min-heap.

### 4.2 Algoritma Bellman-Ford

Menangani bobot negatif (dapat mendeteksi negative cycle):
1. Relax semua edge $|V| - 1 $ kali.
2. Relax tambahan ke-$|V| $: jika ada perubahan $\implies $ negative cycle ada.

Kompleksitas: $ O(|V| \cdot |E|) $.

### 4.3 Floyd-Warshall (Semua-pasangan shortest path)

Dinamika pemrograman:

$ $ d_{ij}^{(k)} = \min\left(d_{ij}^{(k-1)}, \, d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\right)$$

Kompleksitas: $ O(|V|^3) $. Cocok untuk graf padat kecil.

### 4.4 Studi Kasus: Routing Jaringan Transportasi

Sebuah kota memiliki 6 persimpangan (A–F) dengan jarak (km):

| Edge | (Asal, Tujuan) | Jarak (km) |
|------|----------------|-------------|
| e1 | A–B | 7 |
| e2 | A–C | 9 |
| e3 | A–F | 14 |
| e4 | B–C | 10 |
| e5 | B–D | 15 |
| e6 | C–D | 11 |
| e7 | C–F | 2 |
| e8 | D–E | 6 |
| e9 | E–F | 9 |

**Tentukan jalur terpendek dari A ke E.**

*Penyelesaian Dijkstra:*

| Iterasi | Finalisasi | $d(A) $ | $ d(B) $ | $ d(C) $ | $ d(D) $ | $ d(E) $ | $ d(F)$ |
|---------|-----------|--------|--------|--------|--------|--------|--------|
| 0 | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A | 0 | 7 | 9 | ∞ | ∞ | 14 |
| 2 | B | 0 | 7 | 9→9 | 22 | ∞ | 14 |
| 3 | C | 0 | 7 | 9 | 20 | ∞ | 11 |
| 4 | F | 0 | 7 | 9 | 20 | 20 | 11 |
| 5 | E | 0 | 7 | 9 | 20 | 20 | 11 |
| 6 | D | 0 | 7 | 9 | 20 | 20 | 11 |

**Jalur terpendek:** A → C → F → E = 9 + 2 + 9 = **20 km**

### 4.5 Aplikasi dalam Geodesi

- **Network adjustment:** shortest path pada weighted graph model jaringan leveling/traverse.

- **GIS routing:** Dijkstra/A* pada graph raster atau road network (OpenStreetMap).

- **Kalman filtering pada jaringan sensor:** graph-based simultaneous localization and mapping (SLAM).

---

## 5. Analisis Jaringan Lanjutan (Network Analysis)

### 5.1 Kapasitas Aliran Maksimum (Max-Flow)

**Max-Flow Min-Cut Theorem (Ford-Fulkerson, 1956):*
*

$ $\text{max flow}(s, t) = \text{min cut capacity}(s, t)

$$

*Algoritma Ford-Fulkerson:*
1. Inisialisasi flow $ f(e) = 0$.
2. Cari augmenting path di residual graph.
3. Tambah flow sebesar bottleneck capacity.
4. Ulangi hingga tidak ada augmenting path.

Kompleksitas: $O(|E| \cdot |f^*|) $ dengan $ f^*$= max flow. Edmonds-Karp (BFS): $ O(|V| \cdot |E|^2)$.

### 5.2 Indeks Konektivitas (Centrality Measures)

| Ukuran | Rumus | Intepretasi |
|--------|-------|-------------|
| **Degree centrality** | $C_D(v) = \deg(v) $ | Jumlah koneksi langsung |
| **Betweenness centrality** | $ C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}} $ | Fraksi jalur terpendek yang melewati $  v $ |
| **Closeness centrality** | $ C_C(v) = \frac{n-1}{\sum_{u \neq v} d(v, u)} $ | Kekinian terhadap semua simpul |
| **Eigenvector centrality** | $\mathbf{Ax} = \lambda_1 \mathbf{x} $ | Pengaruh dalam jaringan (PageRank terinspirasi) |
| **Clustering coefficient** | $ C(v) = \frac{2|\{e_{ij} : v_i, v_j \in N(v)\}|}{\deg(v)(\deg(v)-1)} $ | Seberapa terhubung tetangga $ v$ |

### 5.3 Studi Kasus: Analisis Jaringan Posisi Stasiun GNSS

Sebuah jaringan 8 stasiun GNSS dengan koneksi baseline (edge weight = jarak):

> Analisis **betweenness centrality** mengidentifikasi stasiun "hub" kritis: jika hub tersebut gagal, jaringan terpecah menjadi komponen terputus. Ini menentukan prioritas maintenance dan redundansi pengamatan.

**Hasil:**

- Stasiun B dan D memiliki betweenness centrality tertinggi.

- Min-cut antara jaringan utara dan selatan = 2 edge (bottleneck).

- Edge connectivity maksimum = 3 (mampu bertahan terhadap 2 edge removal tanpa terputus).

---

## 6. Worked Examples / Contoh Terstruktur

### Latihan 1: Apakah graf berikut Eulerian?

Graf $G $ memiliki 5 simpul $\{1,2,3,4,5\} $ dan 7 sisi: $ (1,2), (1,3), (2,3), (2,4), (3,4), (3,5), (4,5) $.

Derajat:

- $\deg(1) = 2 $ (genap ✓)
-$\deg(2) = 3 $ (ganjil ✗)
-$\deg(3) = 4 $ (genap ✓)
-$\deg(4) = 3 $ (ganjil ✗)
-$\deg(5) = 2 $ (genap ✓)

**Jawaban:** Tepat 2 simpul berderajat ganjil (2 dan 4) $\implies $ graf memiliki **Eulerian trail** (bukan circuit) dari simpul 2 ke simpul 4. Contoh: 2-1-3-4-5-3-2-4.

### Latihan 2: MST dengan Kruskal

Sisi diurutkan: $(A,C):2, \, (B,D):3, \, (A,B):5, \, (C,D):6, \, (B,C):7, \, (A,D):10, \, (B,E):8 $ Langkah:
1.$ (A,C):2 $— no cycle, accept.
2.$ (B,D):3 $— no cycle, accept.
3.$ (A,B):5 $— no cycle (A,C dan B,D terpisah, hubungkan), accept.
4.$ (C,D):6 $— C dan D sudah terhubung via A. **Cycle! Skip.**
5.$ (B,C):7 $— B dan C sudah terhubung. **Cycle! Skip.**
6.$ (B,E):8$— E baru, accept.
7. Total MST weight = 2+3+5+8 = 18.

---

## References / Referensi

1. **Cormen, T. H., et al.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press — Ch. 22-24 (Graf).
2. **Diestel, R.** (2017). *Graph Theory* (5th ed.). Springer — Referensi teori graf komprehensif.
3. **Bondy, J. A., & Murty, U. S. R.** (2008). *Graph Theory*. Springer.
4. **Eastment, A. N., & Ratcliffe, J.** (2011). *GPS - Making it Work*, Ed. 5. Ascel-Learning — Routing GNSS.
5. **Newman, M. E. J.** (2010). *Networks: An Introduction*. Oxford University Press — Network analysis and centrality.
6. **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B.** (1993). *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall.
7. **Sedgewick, R., & Wayne, K.** (2011). *Algorithms* (4th ed.). Addison-Wesley — MST and shortest path implementations.

---

## Appendix: Quick Reference / Referensi Cepat

| Istilah | Definisi |
|---------|----------|
| $K_n $ | Graf lengkap (complete graph) |
| $ C_n $ | Siklus sederhana panjang $  n $ |
| $ K_{m,n} $ | Graf bipartit lengkap |
| $ W_n $ | Wheel graph (siklus + hub pusat) |
| $ P_n $ | Path graph |
| $\chi(G) $ | Kromatik (chromatic number) |
| $\kappa(G) $ | Vertex connectivity |
| $\lambda(G) $ | Edge connectivity |
| $\alpha(G) $ | Independence number |
| $\omega(G)$ | Clique number |

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214702. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*