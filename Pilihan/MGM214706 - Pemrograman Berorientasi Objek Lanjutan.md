---
title: "MGM214706 - Pemrograman Berorientasi Objek Lanjutan"
subject: "Ilmu Komputer / Pengembangan Perangkat Lunak"
tags: [oop, design-patterns, solid, inheritance, polymorphism, software-architecture]
course_code: "MGM214706"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214706 - Pemrograman Berorientasi Objek Lanjutan
## Advanced Object-Oriented Programming

**Course Code:** MGM214706  
**SKS:** 3 (2-1)  
**Semester:** 5  
**Prerequisites:** Pemrograman Dasar, Dasar-Dasar OOP  

---

## Overview / Gambaran Umum

Pemrograman Berorientasi Objek (OOP) adalah paradigma yang mengorganisasi perangkat lunak di sekitar **objek** (data dan perilaku). OOP Lanjutan melampaui sintaks dasar, berfokus pada arsitektur perangkat lunak yang tangguh, *maintainable*, dan *scalable*. Mata kuliah ini mencakup desain tingkat lanjut: pola desain (design patterns), prinsip SOLID, ketergantungan (inversion of control), serta mekanika pewarisan dan polimorfisme untuk sistem skala besar. Di bidang geodesi/GIS, ini penting untuk pembuatan library pengolahan data geospasial yang kompleks.

> **Catatan:** "OOP bukan tentang membuat kelas, ini tentang membuat sistem yang komponen-komponennya dapat berkembang secara independen." — *Prinsip Abstraksi*

---

## 1. Fondasi OOP yang Mendalam

### 1.1 Polimorfisme dan Komposisi

- **Polimorfisme:** Kemampuan objek untuk mengambil berbagai bentuk melalui *interface* atau *abstract class*.
- **Komposisi vs Pewarisan (Inheritance):** "Favor composition over inheritance." Pewarisan sering memicu *fragile base class problem* (perubahan parent merusak child). Komposisi (objek memiliki objek lain) lebih fleksibel.

### 1.2 Encapsulation dan Data Hiding

Encapsulation bukan sekadar *getter/setter*. Ini tentang melindungi *invariants* (kondisi valid objek).

```java
public class Coordinate {
    private double lat, lon; // Private field

    public Coordinate(double lat, double lon) {
        setLat(lat); // Validasi di constructor
        setLon(lon);
    }

    public void setLat(double lat) {
        if (lat < -90 || lat > 90) throw new IllegalArgumentException("Invalid latitude");
        this.lat = lat;
    }
    // ...
}
```

---

## 2. Prinsip Desain SOLID

Prinsip ini wajib dipahami untuk sistem besar:

| Huruf | Prinsip | Penjelasan |
|-------|---------|------------|
| **S** | Single Responsibility | Satu kelas hanya punya satu alasan untuk berubah. |
| **O** | Open/Closed | Terbuka untuk ekstensi, tertutup untuk modifikasi. |
| **L** | Liskov Substitution | Subclass harus bisa menggantikan parent tanpa merusak perilaku sistem. |
| **I** | Interface Segregation | Banyak interface khusus lebih baik dari satu interface raksasa (fat interface). |
| **D** | Dependency Inversion | High-level module jangan bergantung pada low-level module; keduanya bergantung pada abstraksi. |

---

## 3. Design Patterns (Pola Desain)

Pola desain adalah solusi standar untuk masalah umum.

### 3.1 Creational Patterns (Pembuatan)
- **Singleton:** Pastikan hanya ada satu instance (misal: koneksi database).
- **Factory Method:** Membuat objek tanpa menyebutkan kelas spesifik (misal: `GeoReader` membuat `ShapefileReader` atau `GeoJSONReader`).
- **Builder:** Konstruksi objek kompleks step-by-step (misal: `TrajectoryBuilder`).

### 3.2 Structural Patterns (Struktur)
- **Adapter:** Membuat interface yang tidak kompatibel bekerja sama (misal: adaptasi API library map lama ke baru).
- **Decorator:** Menambah perilaku pada objek secara dinamis tanpa merubah kelas (misal: `MapLayer` ditambah `ShadowDecorator`, `LabelDecorator`).
- **Proxy:** Representasi objek lain untuk kontrol akses atau lazy loading (misal: `RemoteGeoServiceProxy`).

### 3.3 Behavioral Patterns (Perilaku)
- **Observer:** Mekanisme subscribe/notify (misal: UI ter-update otomatis saat data GIS berubah).
- **Strategy:** Algoritma dapat diganti saat runtime (misal: `RoutePlanner` memakai `StrategyShortestPath` atau `StrategyFastestPath`).
- **Command:** Mengubah operasi menjadi objek (misal: Undo/Redo di perangkat lunak GIS).

---

## 4. Studi Kasus: Arsitektur Library GIS

Misalkan kita membangun library GIS:

**Desain Buruk:** Satu kelas `GISProcessor` berisi semua logika (membaca, hitung jarak, visualisasi).

**Desain SOLID (Baik):**

1. **SRP:** `FileReader` (baca data), `DistanceCalculator` (algoritma), `Renderer` (visualisasi).
2. **OCP:** `DistanceCalculator` menggunakan `Strategy` pattern agar bisa menambah algoritma `Geodesic`, `FlatEarth`, `Vincenty` tanpa edit kelas utama.
3. **DIP:** `GISProcessor` bergantung pada `IGeoReader` (interface), bukan `ShapefileReader`.

```java
public interface IGeoReader {
    List<Geometry> read();
}

public class GISProcessor {
    private final IGeoReader reader; // Inversion of control

    public GISProcessor(IGeoReader reader) {
        this.reader = reader;
    }

    public void process() {
        List<Geometry> data = reader.read();
        // ...
    }
}
```

---

## 5. Pemrograman Generik (Generics)

Generics meningkatkan type safety.

```java
// Java/C# style
public class DataContainer<T> {
    private T item;
    public void set(T item) { this.item = item; }
    public T get() { return item; }
}

// Penggunaan untuk koordinat 2D/3D
DataContainer<Point2D> point2d = new DataContainer<>();
DataContainer<Point3D> point3d = new DataContainer<>();
```

---

## 6. Testing dan Testing-Driven Development (TDD)

OOP Lanjutan tidak lengkap tanpa testing.

- **Unit Test:** `Junit` / `NUnit` untuk test satu method/kelas.
- **Mocking:** `Mockito` untuk memalsukan dependensi (misal: mock `DatabaseService` agar test tidak benar-benar koneksi ke DB).
- **TDD Cycle:** Write test (Red) -> Write code (Green) -> Refactor (Refactor).

---

## References / Referensi

1. **Gamma, E., et al.** (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley (The "Gang of Four" book).
2. **Martin, R. C.** (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
3. **Bloch, J.** (2018). *Effective Java* (3rd ed.). Addison-Wesley.
4. **Freeman, E., et al.** (2020). *Head First Design Patterns* (2nd ed.). O'Reilly.
5. **Gamma, E., et al.** (2004). *Refactoring: Improving the Design of Existing Code*. Addison-Wesley.
6. **Object Management Group (OMG).** *UML Specification*.
7. **Documentation:** Standard library documentation untuk bahasa yang digunakan (Java/C++/C#).

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214706. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*