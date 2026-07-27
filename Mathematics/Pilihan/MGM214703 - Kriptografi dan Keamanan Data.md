---
title: "MGM214703 - Kriptografi dan Keamanan Data"
subject: "Matematika Terapan / Ilmu Komputer"
tags: [cryptography, security, RSA, AES, hashing, digital-signatures]
course_code: "MGM214703"
sks: 3
semester: 5
language: "id-ID"
---

# MGM214703 - Kriptografi dan Keamanan Data

## Cryptography and Data Security

**Course Code:** MGM214703 
**SKS:** 3 (3-0) 
**Semester:** 5 
**Prerequisites:** Aljabar Linear, Struktur Diskrit, Probabilitas 

---

## Overview / Gambaran Umum

Kriptografi (cryptography) adalah ilmu dan seni mengamankan informasi dengan mengubahnya menjadi format yang tidak terbaca tanpa kunci yang sesuai. Sejak Caesar cipher pada masa Romawi hingga algoritma kuantum-resistant modern, kriptografi merupakan pilar keamanan siber. Mata kuliah ini mencakup kriptografi simetris (AES, DES), kriptografi asimetris (RSA, ECC), fungsi hash, tanda tangan digital, serta infrastruktur kunci publik (PKI) — semua dengan fondasi matematika bilangan linear, aljabar abstrak, dan teori bilangan.

> **Catatan:** "Keamanan kriptografi harus bergantung pada rahasia kunci, bukan pada kerahasiaan algoritma." — *Prinsip Kerckhoffs (1883)*

---

## 1. Prinsip Dasar Kriptografi

### 1.1 Model Kriptografi

Sistem kriptografi dasar:

$$P \xrightarrow{\text{Encrypt}(K_e)} C \xrightarrow{\text{Decrypt}(K_d)} P$$di mana $P$= plaintext (pesan asli),$C$= ciphertext (terenkripsi),$K_e$= kunci enkripsi,$K_d$ = kunci dekripsi.

### 1.2 Klasifikasi Berdasarkan Kunci

| Aspek | Simetris | Asimetris (Publik) |
|-------|---------|---------------------|
| **Jumlah kunci** | 1 kunci ($K_e = K_d$) | 2 kunci ($K_e \neq K_d$) |
| **Kecepatan** | Sangat cepat (~100× lebih cepat) | Relatif lambat |
| **Masalah kunci** | Distribusi kunci aman (key exchange) | Tidak ada masalah distribusi |
| **Ukuran kunci** | 128–256 bit | 2048–4096 bit (RSA) |
| **Contoh** | AES, 3DES, ChaCha20 | RSA, ECC, ElGamal |
| **Digunakan untuk** | Enkripsi data bulk | Pertukaran kunci, digital signature |

### 1.3 Tingkat Keamanan

- **Kerahasiaan sempurna (perfect secrecy):** $H(P|C) = H(P)$— Enkripsi one-time pad (OTP).

- **Industri:** AES-256, RSA-3072, ECC P-384.

- **Kuantum-resistant (post-quantum):** Lattice-based (CRYSTALS-Kyber), Hash-based (SPHINCS+).

---

## 2. Kriptografi Simetris

### 2.1 DES (Data Encryption Standard)

- 64-bit block, 56-bit kunci (8 parity bits).

- 16 ronde Feistel network.

- **Sudah tidak aman** — brute force dalam waktu singkat (~2²² operasi untuk 2-key 3DES).

### 2.2 3DES (Triple DES
)

$$C = E_{K_3}(D_{K_2}(E_{K_1}(P)))$$

Efektif kunci 112 bit (2TDEA) atau 168 bit (3TDEA). Sertifikasi NIST dihentikan pada 2023.

### 2.3 AES (Advanced Encryption Standard)

**Rijndael** — pemenang kompetisi NIST 2000. Ukuran blok 128 bit, kunci 128/192/256 bit, 10/12/14 ronde.

| Versi AES | Ukuran Kunci | Ronde | Struktur |
|-----------|-------------|-------|----------|
| AES-128 | 128 bit | 10 | SubBytes → ShiftRows → MixColumns → AddRoundKey |
| AES-192 | 192 bit | 12 | Sama |
| AES-256 | 256 bit | 14 | Sama |

**Operasi setiap ronde AES-128:**
1. **SubBytes:** Substitusi non-linear (S-box berdasarkan inverse dalam $GF(2^8)$).
2. **ShiftRows:** Rotasi baris kiri 0/1/2/3 posisi.
3. **MixColumns:** Multiplikasi matriks kolom dalam $GF(2^8)$.
4. **AddRoundKey:** XOR dengan round key.

### 2.4 Mode Operasi

| Mode | Singkatan | Paralelisasi | Sifat |
|------|----------|--------------|-------|
| Electronic Codebook | ECB | Ya | **Tidak aman** (pola berulang) |
| Cipher Block Chaining | CBC | Tidak (sequential) | Umum digunakan (SSL v3) |
| Counter | CTR | Ya | Dapat diparalelkan |
| Galois/Counter | GCM | Ya | Authenticated encryption (AEAD) |
| XEX-based | XTS | Partial | Untuk enkripsi disk |

**Pilihan modern:** AES-GCM (authenticated encryption) atau ChaCha20-Poly1305.

### 2.5 Contoh Enkripsi AES

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256) # Kunci 256 bit
aesgcm = AESGCM(key)
nonce = os.urandom(12) # 96-bit nonce

# Enkripsi dengan AAD (Additional Authenticated Data)
ciphertext = aesgcm.encrypt(nonce, b"Data GNSS Coordinates", b"station-001")

# Dekripsi
plaintext = aesgcm.decrypt(nonce, ciphertext, b"station-001")
```

---

## 3. Kriptografi Asimetris

### 3.1 RSA (Rivest-Shamir-Adleman, 1977)

Berdasarkan **masalah faktorisasi bilangan besar:** $n = pq $sulit difaktor.

**Key Generation:**
1. Pilih dua bilangan prima besar $p $dan $q$.
2. Hitung $n = pq $dan $\phi(n) = (p-1)(q-1)$.
3. Pilih $e $sehingga $\gcd(e, \phi(n)) = 1$(umum:$e = 65537 = 2^{16}+1$).
4. Hitung $d = e^{-1} \mod \phi(n)$(extended Euclidean algorithm).

**Enkripsi/Deskripsi:**

$$C = P^e \mod n \quad \text{(Enkripsi)}P = C^d \mod n \quad \text{(Deskripsi)} $$**Kebenaran:**$P^{ed} = P^{1 + k\phi(n)} \equiv P \pmod{n} $oleh Fermat's Little Theorem.

### 3.2 Contoh RSA Sederhana

| Parameter | Nilai |
|-----------|-------|
| $p$ | 61 |
| $q$ | 53 |
| $n = pq$ | 3233 |
| $\phi(n) = (60)(52)$ | 3120 |
| $e$ | 17 |
| $d = 17^{-1} \bmod 3120$ | 2753 |

**Enkripsi pesan $P = 65$:**

$$C = 65^{17} \mod 3233 = 279
0

$$**Deskripsi:**$$

P = 2790^{2753} \mod 3233 = 65 \quad \checkmark$$### 3.3 ECC (Elliptic Curve Cryptography)

Cryptography berbasis kelompok aditif pada kurva eliptik
:

$$y^2 = x^3 + ax + b \pmod{p} $$

- Operasi: *point addition*$P + Q $dan *point doubling*$2P$.

- *Scalar multiplication:* $kP = \underbrace{P + P + \cdots + P}_{k} $.

- *Elliptic Curve Discrete Logarithm Problem (ECDLP):* Diberikan $P $dan $kP$, cari $k$— sangat sulit secara komputasional.

**Keunggulan:** Kunci lebih pendek dari RSA untuk keamanan setara.

| Keamanan Setara | RSA (bit) | ECC (bit) |
|-----------------|-----------|-----------|
| 80-bit | 1024 | 160 |
| 128-bit | 3072 | 256 |
| 192-bit | 7680 | 384 |
| 256-bit | 15360 | 521 |

---

## 4. Fungsi Hash dan Tanda Tangan Digital

### 4.1 Fungsi Hash Kriptografis

Properti fungsi hash $H: \{0,1\}^* \to \{0,1\}^n$:
1. **Preimage resistance:** Diberikan $h$, sulit menemukan $x $dengan $H(x) = h$.
2. **Second preimage resistance:** Diberikan $x_1$, sulit menemukan $x_2 \neq x_1 $dengan $H(x_1) = H(x_2)$.
3. **Collision resistance:** Sulit menemukan $x_1 \neq x_2 $dengan $H(x_1) = H(x_2)$.

### 4.2 Perbandingan Algoritma Hash

| Algoritma | Output (bit) | Serangan terbaik | Status |
|-----------|-------------|------------------|--------|
| MD5 | 128 | Collision: $2^{21} $(30 detik) | ❌ **Tidak aman** |
| SHA-1 | 160 | Collision:$2^{63} $(Google SHAttered) | ❌ **Tidak aman** |
| SHA-256 | 256 | Collision:$2^{128} $ | ✅ Aman |
| SHA-3 (Keccak) | 224-512 | Collision:$2^{n/2} $ | ✅ Aman |
| BLAKE2 | 256 | Collision:$2^{128} $ | ✅ Aman, cepat |
| Argon2id | Variabel | Brute force:$2^{256} $ | ✅ Khusus password hashing |

### 4.3 Tanda Tangan Digital

$$\text{Sign}: \sigma = \text{Sign}_{sk}(H(m)) \quad \text{— Penandatangan memproduksi } \sigma\text{Verify}: \text{Verify}_{pk}(m, \sigma) \rightarrow \text{true/false} \quad \text{— Verifikator memeriksa} $$**DSA / ECDSA:**
1. Pilih random $k$, hitung $R = kG \pmod{p} $, $r = R_x \mod n$.
2. Hitung $s = k^{-1}(H(m) + d \cdot r) \mod n$.
3. Tanda tangan: $(r, s)$.
4. Verifikasi: hitung $u_1, u_2$, cek $R_x' = r$.

**EdDSA (Ed25519):** Lebih cepat, deterministik (tidak perlu kunci $k $random), resisten timing attack.

### 4.4 Studi Kasus: Verifikasi Integritas Data GNSS

Untuk menjamin integritas data pengukuran GNSS yang ditransmisikan dari stasiun ke pusat pengolahan:

1. Stasiun menghitung $H = \text{SHA-256}(\text{data observasi})$.
2. Stasiun menandatangani $H$ dengan ECDSA-P256 menggunakan private key.
3. Pusat pengolahan memverifikasi signature menggunakan public key stasiun.
4. Integritas terjamin: tidak ada yang dapat memodifikasi data tanpa terdeteksi.

| Komponen | Protokol | Alasan |
|----------|----------|--------|
| Signature | ECDSA P-256 | Ringan, efisien, NIST-approved |
| Hash | SHA-256 | Umum, terbukti |
| Enkripsi data | AES-256-GCM | Cepat, authenticated |
| Key exchange | X25519 (ECDH) | Keamanan forward |

---

## 5. Infrastruktur Kunci Publik (PKI)

### 5.1 Komponen PKI

| Komponen | Fungsi |
|----------|--------|
| **Certificate Authority (CA)** | Menerbitkan dan menandatangani sertifikat digital |
| **Registration Authority (RA)** | Memverifikasi identitas pemohon sertifikat |
| **Certificate Revocation List (CRL)** | Daftar sertifikat yang dicabut |
| **OCSP** | Online Certificate Status Protocol (cek status real-time) |
| **Key Store** | Tempat penyimpanan kunci pribadi |

### 5.2 Sertifikat X.509

Struktur sertifikat X.509 v3:
```
Subject: CN=gnss-station.big.go.id, O=Big, C=ID
Issuer: CA=root-ca.big.go.id
Serial: 0x3A2B1C
Valid: 2025-01-01 to 2026-12-31
Public Key: ECDSA-P256
Signature: SHA256withECDSA
Key Usage: digitalSignature
```

### 5.3 Chain of Trust

```
Root CA (self-signed, 20+ tahun)
├── Intermediate CA 1
│ ├── End-entity cert (server)
│ └── End-entity cert (stasiun GNSS)
└── Intermediate CA 2
 └── End-entity cert (klien)
```

Verifikasi: setiap sertifikat ditandatangani oleh CA induknya hingga Root CA (dipercaya secara a priori).

### 5.4 TLS 1.3 Handshake (Modern)

| Langkah | Klien | Server |
|---------|-------|--------|
| 1 | ClientHello + key share + supported ciphers | — |
| 2 | — | ServerHello + key share + certificate + signature |
| 3 | Verifikasi certificate + derivation keys | — |
| 4 | Finished (MAC) | Finished (MAC) |
| 5 | **Encrypted Application Data** | **Encrypted Application Data** |

Perubahan dari TLS 1.2: hanya 1 round-trip (1-RTT), tidak ada renegotiation, forward secrecy wajib.

---

## 6. Kerentanan dan Serangan Umum

| Serangan | Target | Pertahanan |
|----------|--------|------------|
| **Man-in-the-Middle** | Key exchange | Sertifikat PKI, certificate pinning |
| **Brute force** | Password/kunci | Kunci panjang, rate limiting |
| **Side-channel** | Implementasi | Constant-time implementation |
| **Padding Oracle** | CBC mode | AEAD (GCM), pad validation |
| **Rainbow table** | Password hash | Salt + Argon2id |
| **Quantum (Shor's)** | RSA, ECC | Post-quantum: Kyber, Dilithium |

---

## References / Referensi

1. **Stallings, W.** (2017). *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson.
2. **Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A.** (1996). *Handbook of Applied Cryptography*. CRC Press.
3. **Katz, J., & Lindell, Y.** (2014). *Introduction to Modern Cryptography* (2nd ed.). CRC Press.
4. **Boneh, D., & Shoup, V.** (2023). *A Graduate Course in Applied Cryptography* (Version 0.5). — [crypto.stanford.edu/~dabo/cryptobook](https://crypto.stanford.edu/~dabo/cryptobook)
5. **NIST** (2020). *FIPS 197: Advanced Encryption Standard (AES)*.
6. **NIST** (2023). *FIPS 203/204/205: Module-Lattice-Based, Hash-Based, Code-Based Key-Encapsulation* (Post-Quantum).
7. **RFC 8446** (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*.

---

*File ini dibuat untuk keperluan pembelajaran mata kuliah MGM214703. Konten bersifat ringkasan; rujuk buku teks dan jurnal untuk kedalaman penuh.*