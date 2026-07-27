# 📚 Pilihan: Struktur Data Spasial

**Kode:** TKD213611
**Sifat:** Pilihan
**SKS:** 3 (3-0)

## Deskripsi Mata Kuliah

Struktur Data Spasial adalah mata kuliah pilihan yang mempelajari struktur data khusus untuk menyimpan dan mengakses data geospasial secara efisien. Mata kuliah ini membahas struktur data spasial seperti R-tree, k-d tree, quadtree, grid, dan jaringan (network), serta algoritma spatial query, spatial join, dan spatial indexing. Mahasiswa akan mempelajari trade-off antara struktur data yang berbeda untuk aplikasi spasial yang berbeda.

Efisiensi penyimpanan dan akses data spasial sangat penting untuk aplikasi SIG skala besar, basisdata geospasial, dan sistem informasi geografis berbasis web. Struktur data yang tepat dapat meningkatkan performa query spasial secara signifikan, terutama untuk data dengan dimensi tinggi dan volume besar seperti data raster atau data jaringan jalan.

Pembelajaran dilakukan melalui kombinasi teori dan praktikum pemrograman. Mahasiswa akan mengimplementasikan struktur data spasial dalam bahasa pemrograman (Python, Java, atau C++) dan menguji performanya terhadap data geospasial nyata. Konsep ini sangat relevan dengan pengembangan sistem SIG modern dan basisdata geospasial.

## Topik Utama

### 1. Struktur Data Spasial Dasar
- R-tree dan varian-variannya (R*-tree, Hilbert R-tree)
- k-d tree dan varian (k-d-B-tree)
- Quadtree dan octree

### 2. Algoritma Spatial Query
- Spatial range query
- Nearest neighbor search
- Spatial join dan overlay

### 3. Implementasi dan Optimasi
- Indexing spasial di basisdata (PostGIS, Oracle Spatial)
- Optimasi memori dan I/O
- Aplikasi pada data raster dan vektor

## Tujuan Pembelajaran

1. Memahami struktur data spasial dasar dan kegunaannya
2. Mengimplementasikan struktur data spasial untuk data geospasial
3. Menganalisis performa struktur data spasial yang berbeda
4. Menerapkan algoritma spatial query pada basisdata geospasial

## Referensi

- de Berg, M., Cheong, O., van Kreveld, M., & Overmars, M. (2008). *Computational Geometry: Algorithms and Applications* (3rd ed.). Springer.
- Samet, H. (2005). *Foundations of Multidimensional and Metric Data Mining*. Cambridge University Press.
- Guttman, A. (1984). "R-trees: A Dynamic Index Structure for Spatial Searching." *ACM SIGMOD*.