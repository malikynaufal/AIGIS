---
title: MGM211403 - Aljabar Abstrak (Abstract Algebra)
type: course
semester: 4
sks: 3
tags: [mathematics, abstract-algebra, groups, rings, fields, semester-4]
created: 2026-07-27
---

# MGM211403 - Aljabar Abstrak (Abstract Algebra)

> *"Algebra is the language in which God has written the universe."* — Galileo
> **SKS:** 3 | **Semester:** 4 | **Prerequisite:** [[Number Theory]], [[Linear Algebra Fundamentals]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Groups | Definition, examples, subgroups |
| 2 | Cyclic Groups | Generators, orders, classification |
| 3 | Permutation Groups | Cycles, transpositions, parity |
| 4 | Cosets & Lagrange | Left/right cosets, normal subgroups |
| 5 | Quotient Groups | Factor groups, homomorphism theorem |
| 6 | Group Actions | Orbits, stabilizers, Burnside's lemma |
| 7 | Rings | Definition, ideals, integral domains |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Field Extensions | Algebraic/transcendental, degree |
| 10 | Finite Fields | Construction, applications in coding |
| 11 | Polynomial Rings | Factorization, irreducibility |
| 12 | Galois Theory | Automorphisms, fundamental theorem |
| 13 | Sylow Theorems | Existence, conjugacy, applications |
| 14 | Applications | Cryptography, coding theory |
| 15 | Final Review | Integration project |

## 📚 Core Theorems

### 1. Lagrange's Theorem

If $H \leq G $ (subgroup), then $|H|$ divides $|G|$, and:

$ $|G| = |H| \cdot [G:H]

$$

where $ [G:H] $ is the **index** (number of cosets).

**Corollary:** The order of any element divides the order of the group.

### 2. First Isomorphism Theorem

If $hi: G o H $ is a group homomorphism:$ $G/\kerhi \cong ext{im}hi $$

### 3. Sylow Theorems

For $|G| = p^n \cdot m $ where $ p \nmid m $:

1. **Existence:** There exists a Sylow $ p $-subgroup of order $ p^n $
2. **Conjugacy:** All Sylow $ p $-subgroups are conjugate
3. **Count:** The number $ n_p $ of Sylow $ p $-subgroups satisfies $ n_p \equiv 1 mod{p} $ and $ n_p \mid m $

### 4. Fundamental Theorem of Finite Abelian Groups

Every finite abelian group is a direct product of cyclic groups of prime-power order:

$ $G \cong \mathbb{Z}_{p_1^{k_1}} imes \mathbb{Z}_{p_2^{k_2}} imes \cdots imes \mathbb{Z}_{p_r^{k_r}}$$

### 5. Fundamental Theorem of Galois Theory

For a Galois extension $ E/K $ with Galois group $ G = ext{Gal}(E/K) $:
- There is a bijection between subgroups of $ G $ and intermediate fields
- $ [E:F] = |ext{Gal}(E/F)|$ and $ [F:K] = [G:ext{Gal}(E/F)] $

## 📖 Group Theory Deep Dive

### Definition of a Group

$ (G, \cdot) $ is a group if:
1. **Closure:** $ a, b \in G \implies ab \in G $
2. **Associativity:** $ (ab)c = a(bc) $
3. **Identity:** $\exists e \in G: ea = ae = a $ 4. **Inverse:**$\forall a \in G, \exists a^{-1}: aa^{-1} = e $ If $ ab = ba $ for all $ a, b $, the group is **abelian**.

### Examples of Groups

| Group | Operation | Order | Abelian? |
|-------|-----------|-------|---------|
| $\mathbb{Z}_n $| Addition mod $ n $|$ n $ | Yes |
| $ S_n $ | Composition | $ n!$ | No ($ n \geq 3 $) |
| $ D_n $ | Symmetries of $ n $-gon | $ 2n $ | No ($ n \geq 3 $) |
| $ GL(n, \mathbb{R}) $ | Matrix mult. | $\infty $ | No |
| $\mathbb{Z} $| Addition |$\infty $ | Yes |

### Cyclic Groups

A group $ G $ is **cyclic** if $ G = \langle g \rangle = \{g^n : n \in \mathbb{Z}\} $.

**Classification:** Every cyclic group of order $ n $ is isomorphic to $\mathbb{Z}_n $.

## 💍 Ring Theory

### Definition

$ (R, +, \cdot) $ is a ring if:
1. $ (R, +) $ is an abelian group
2. $ (R, \cdot) $ is a monoid
3. Distributive laws hold

### Types of Rings

| Type | Properties |
|------|-----------|
| **Commutative** | $ ab = ba $ |
| **Integral Domain** | Commutative, no zero divisors |
| **Field** | All non-zero elements invertible |
| **Euclidean Domain** | Has division algorithm |
| **PID** | Every ideal is principal |
| **UFD** | Unique factorization domain |

### Ideals

$ I \subseteq R $ is an ideal if:
- $ (I, +) $ is a subgroup
- $ r \in R, a \in I \implies ra, ar \in I $

## 🔢 Finite Fields (Galois Fields)

$\mathbb{F}_{p^n} $ exists and is unique for every prime power $ p^n $.

**Construction:** $\mathbb{F}_{p^n} = \mathbb{F}_p[x]/\langle f(x) \rangle $ where $ f $ is irreducible of degree $ n $.

### Applications

- **AES:** Operations in $\mathbb{F}_{2^8} $- **Reed-Solomon codes:**$\mathbb{F}_{256} $- **Elliptic curve crypto:**$\mathbb{F}_p $ or $\mathbb{F}_{2^m} $

## 🔐 Cryptography Applications

### RSA

1. Choose primes $ p, q $, compute $ N = pq $, $hi(N) = (p-1)(q-1) $ 2. Choose $ e $ with $\gcd(e, hi(N)) = 1 $ 3. Compute $ d = e^{-1} mod{hi(N)} $ 4. **Encrypt:**$ c = m^e mod{N} $ 5. **Decrypt:**$ m = c^d mod{N} $

### Elliptic Curve Cryptography

Points on $ y^2 = x^3 + ax + b $ form a group under:
- Identity: point at infinity $\mathcal{O} $- Inverse: $ (x, y)^{-1} = (x, -y) $
- Addition: secant/tangent method

## 💡 Solved Example: Sylow Subgroups

**Problem:** Find the number of Sylow 2-subgroups of $ S_4 $.

**Solution:**
$|S_4| = 24 = 2^3 \cdot 3 $ By Sylow's third theorem: $ n_2 \equiv 1 mod{2} $ and $ n_2 \mid 3 $.

So $ n_2 \in \{1, 3\} $.

Since $ S_4 $ has more than one subgroup of order 8 (e.g., $ D_4 $ embedded in different ways), $ n_2 = 3 $.

## 🎯 Practice Problems

1. **Groups:** Prove that every group of order $ pq $ ($ p < q $ primes) has a normal Sylow subgroup.
2. **Rings:** Show that $\mathbb{Z}[\sqrt{-5}] $ is not a UFD.
3. **Fields:** Construct $\mathbb{F}_{16} $ explicitly.
4. **Galois:** Find the Galois group of $ x^4 - 2 $ over $\mathbb{Q} $.
5. **Applications:** Implement RSA with $ p=61, q=53, e=17$.

## 📖 References

- Dummit, D.S. & Foote, R.M. (2004). *Abstract Algebra* (3rd ed.). Wiley.
- Artin, M. (2011). *Algebra* (2nd ed.). Pearson.
- Gallian, J.A. (2020). *Contemporary Abstract Algebra*. Cengage.

---
*See also: [[Number Theory]], [[Abstract Algebra]], [[Linear Algebra Fundamentals]]*
