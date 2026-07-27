---
title: Abstract Algebra
type: concept
subject: Mathematics
tags: [mathematics, abstract-algebra, groups, rings, fields, galois-theory]
created: 2026-07-27
updated: 2026-07-27
---

# Abstract Algebra

> *"Algebra is the offer made by the devil to the mathematician. The devil says: I will give you this powerful machine, it will answer any question you like. All you need to do is give me your soul: give up geometry and you will have this marvelous machine."* — Michael Atiyah
> Part of [[Mathematics MOC]]. Fundamental to cryptography, coding theory, and symmetry in physics.

## 1. Groups

A **group** $(G, \cdot) $ is a set $ G $ with a binary operation $\cdot $ satisfying:

1. **Closure:** $ a, b \in G \implies a \cdot b \in G $
2. **Associativity:** $ (a \cdot b) \cdot c = a \cdot (b \cdot c) $
3. **Identity:** $\exists e \in G $ such that $ e \cdot a = a \cdot e = a $ 4. **Inverses:**$\forall a \in G, \exists a^{-1} \in G $ such that $ a \cdot a^{-1} = e $ If $ a \cdot b = b \cdot a $ for all $ a, b $, $ G $ is **abelian**.

### Examples

| Group | Operation | Order | Properties |
|-------|-----------|-------|------------|
| $ (\mathbb{Z}, +) $ | Addition | Infinite | Cyclic, abelian |
| $ (\mathbb{Z}/n\mathbb{Z}, +) $ | Addition mod $ n $ | $ n $ | Cyclic, abelian |
| $ S_n $ (permutations) | Composition | $ n!$| Non-abelian for $ n \geq 3 $ |
| $ GL(n, \mathbb{R}) $ | Matrix multiplication | Infinite | Non-abelian |
| $ (\mathbb{R}^*, \cdot) $ | Multiplication | Infinite | Abelian |

### Subgroups

$ H \subseteq G $ is a subgroup if it's a group under the same operation. **Lagrange's Theorem:**

$ $|H| \text{ divides } |G|$$

### Cosets and Normal Subgroups

**Left coset:** $ gH = \{gh : h \in H\} $. **Right coset:** $ Hg $.

$ H $ is **normal** ($ H \trianglelefteq G $) if $ gH = Hg $ for all $ g \in G $, or equivalently $ ghg^{-1} \in H $ for all $ h \in H $.

### Quotient Groups

If $ N \trianglelefteq G $, the set $ G/N = \{gN : g \in G\} $ forms a group with $ (gN)(hN) = (gh)N $.

### Group Homomorphisms

A map $\phi: G \to H $ is a **homomorphism** if $\phi(ab) = \phi(a)\phi(b) $.

**Isomorphism Theorem:** If $\phi: G \to H $ is a homomorphism, then $ G/\ker\phi \cong \text{im}\phi $.

## 2. Rings

A **ring** $ (R, +, \cdot) $ has two operations satisfying:
1. $ (R, +) $ is an abelian group
2. $ (R, \cdot) $ is a monoid (associative with identity)
3. Distributivity: $ a(b+c) = ab + ac $, $ (a+b)c = ac + bc $

### Types of Rings

| Type | Additional Property |
|------|---------------------|
| **Commutative** | $ ab = ba $ |
| **Integral Domain** | Commutative, no zero divisors |
| **Field** | Every non-zero element has a multiplicative inverse |
| **Euclidean Domain** | Division algorithm exists |

### Ideals

$ I \subseteq R $ is an **ideal** if:
- $ I $ is an additive subgroup
- $\forall r \in R, a \in I: ra, ar \in I $**Quotient ring:**$ R/I $ is a ring. If $ I $ is maximal,$ R/I $ is a field.

### Chinese Remainder Theorem (Ring Form)

If $ I_1, \dots, I_k $ are pairwise coprime ideals, then:

$ $ R/(I_1 \cap \dots \cap I_k) \cong R/I_1 \times \dots \times R/I_k $$

## 3. Fields

A **field** $ F $ is a commutative ring where $ F^\times = F \setminus \{0\} $ is a group under multiplication.

### Examples

| Field | Characteristic |
|-------|----------------|
| $\mathbb{Q} $ (rationals) | 0 |
| $\mathbb{R} $ (reals) | 0 |
| $\mathbb{C} $ (complex) | 0 |
| $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z} $ ($ p $ prime) | $ p $ |

### Field Extensions

$ F/K $ is an extension. $ [F:K] $ = degree = dimension of $ F $ as $ K $-vector space.

**Algebraic element:** $\alpha $ satisfies a polynomial $ f(x) \in K[x] $.

**Minimal polynomial:** Monic polynomial of least degree with $\alpha $ as root.

## 4. Galois Theory

The **Galois group** of a polynomial $ f \in K[x] $ is $\text{Gal}(f) = \text{Aut}(E/K) $ where $ E $ is the splitting field.

```mermaid
flowchart TD
 K[Base Field K] --> E[Splitting Field E]
 E --> G[Galois Group G = Aut(E/K)]
 G --> Subgroups[Subgroups H ≤ G]
 Subgroups --> Intermediate[Intermediate Fields K ⊆ F ⊆ E]
 Subgroups -.-> Fundamental[Fundamental Theorem]
 Intermediate -.-> Fundamental
```

**Fundamental Theorem of Galois Theory:** Bijection between:
- Subgroups $ H \leq \text{Gal}(E/K) $
- Intermediate fields $ K \subseteq F \subseteq E $

With correspondences:
- $ H \leftrightarrow E^H $ (fixed field of $ H $)
- $ [E^H : K] = |\text{Gal}(E/K)| / |H|$-$ F/K $ is Galois iff $\text{Gal}(E/F) \trianglelefteq \text{Gal}(E/K) $

### Solvability by Radicals

A polynomial is **solvable by radicals** iff its Galois group is a **solvable group** (has abelian composition factors).

- Degrees 1-4: Always solvable (quadratic, cubic, quartic formulas)
- Degree 5: Not solvable in general ($ S_5 $ is not solvable)

## 5. Applications

| Field | Application |
|-------|-------------|
| **Cryptography** | Finite field arithmetic in AES, ECC |
| **Coding Theory** | Reed-Solomon codes over $\mathbb{F}_{2^m} $ |
| **Physics** | Lie groups in particle physics, gauge theory |
| **Chemistry** | Molecular symmetry groups (point groups) |
| **Cryptography** | Diffie-Hellman in $\mathbb{F}_p^\times $, RSA in $ (\mathbb{Z}/N\mathbb{Z})^\times $ |

## Practice Problems

1. Prove that every group of prime order is cyclic.
2. Find all subgroups of $ D_4 $ (dihedral group of order 8).
3. Show that $\mathbb{Z}[\sqrt{-5}] $ is not a UFD.
4. Compute the Galois group of $ x^4 - 2 $ over $\mathbb{Q}$.

## References

- Dummit, D.S. & Foote, R.M. (2004). *Abstract Algebra* (3rd ed.). Wiley.
- Artin, M. (2011). *Algebra* (2nd ed.). Pearson.
- Gallian, J.A. (2020). *Contemporary Abstract Algebra*. Cengage.

---
*See also: [[Number Theory]], [[Linear Algebra Fundamentals]], [[Complex Analysis]]*
