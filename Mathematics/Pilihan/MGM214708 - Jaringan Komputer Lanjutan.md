---
title: "MGM214708 - Jaringan Komputer Lanjutan"
subject: "Ilmu Komputer / Jaringan"
tags: [networking, tcp-ip, routing, qos, sdn, iot]
course_code: "MGM214708"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214708 - Jaringan Komputer Lanjutan

## Advanced Networking

**Course Code:** MGM214708 
**SKS:** 3 (2-1) 
**Semester:** 5 
**Prerequisites:** Jaringan Komputer Dasar 

---

## Overview / Gambaran Umum

Jaringan Komputer Lanjutan membahas arsitektur network modern melampaui TCP/IP dasar. Topik mencakup protokol routing canggih (OSPF, BGP), Quality of Service (QoS), Software-Defined Networking (SDN), Network Function Virtualization (NFV), serta protokol khusus IoT. Bagi profesional geomatika, ini adalah infrastruktur yang mendukung komunikasi data GNSS real-time dan layanan cloud GIS.

> **Catatan:** "Jaringan bukan sekadar kabel dan router, jaringan adalah sistem saraf dari infrastruktur digital modern." — *Prinsip Infrastruktur*

---

## 1. TCP/IP Deep Dive

### 1.1 congestion Control (TCP)

TCP mengontrol data yang dikirim dengan *congestion window* (CWND):

- **Slow Start:** CWND meningkat eksponensial.

- **Congestion Avoidance:** CWND meningkat linear saat mencapai *slow start threshold*.

- **Fast Retransmit/Recovery:** Jika packet loss terjadi (dup ACK), kurangi CWND (misal: bagi dua, algoritma Reno/Cubic).

### 1.2 Routing Protokol

| Tipe | Protokol | Prinsip | Contoh |
|------|----------|---------|--------|
| **IGP** (Interior) | OSPF | Link-State (Dijkstra) | Jaringan lokal |
| **IGP** | EIGRP | DUAL (Diffusing Update) | Cisco proprietary |
| **EGP** (Exterior) | BGP | Path-Vector | Internet routing |

---

## 2. SDN dan Virtualisasi

### 2.1 Software-Defined Networking (SDN)

Pemisahan **Control Plane** (otak, controller) dari **Data Plane** (otot, switch/router).

- **Protokol:** OpenFlow.

- **Keuntungan:** Network programmability, sentralisasi manajemen, optimasi trafik dinamis.

### 2.2 Network Function Virtualization (NFV)

Menggantikan hardware router/firewall/load balancer khusus dengan software (Virtual Network Functions - VNF) yang berjalan di server standar (x86).

---

## 3. IoT dan Protokol Khusus

Protokol untuk perangkat low-power/limited bandwidth:

- **MQTT:** Publish/Subscribe, ringan, over TCP.

- **CoAP:** Restful, over UDP (cocok untuk jaringan sensor IoT).

- **LoRaWAN:** Long range, low power (geodesi pemantauan sensor jauh).

---

## 4. Quality of Service (QoS)

Teknik untuk menjaga performa trafik penting (VOIP, data GNSS real-time) di tengah kepadatan jaringan:

1. **Classification:** Menandai paket (DSCP bits).
2. **Policing/Shaping:** Membatasi laju trafik (Traffic shaping menggunakan *token bucket*).
3. **Queueing:** Prioritas antrian (Priority Queueing, Weighted Fair Queueing).

---

## 5. Referensi

1. **Tanenbaum, A. S., & Wetherall, D. J.** (2011). *Computer Networks* (5th ed.). Prentice Hall.
2. **Kurose, J. F., & Ross, K. W.** (2020). *Computer Networking: A Top-Down Approach* (8th ed.). Pearson.
3. **Stallings, W.** (2016). *Foundations of Modern Networking: SDN, NFV, QoE, IoT, and Cloud*. Addison-Wesley.
4. **RFC 793** (TCP), **RFC 791** (IP), **RFC 4271** (BGP-4).

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214708. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*