---
title: Number Theory
type: concept
subject: Mathematics
tags: [mathematics, number-theory, cryptography, modular-arithmetic]
created: 2026-07-27
updated: 2026-07-27
---

# Number Theory

> *"Mathematics is the queen of the sciences and number theory is the queen of mathematics."* — Gauss
> Part of [[Mathematics MOC]]. Fundamental to cryptography, coding theory, and algorithm analysis.

## 1. Divisibility and Primes

### Divisibility

$a \mid b $means $a $divides $b $if there exists $k \in \mathbb{Z} $such that $b = ak $.

**Key Properties:**
- If $a \mid b $and $b \mid c$, then $a \mid c$ (transitivity)
- If $a \mid b $and $a \mid c$, then $a \mid (bx + cy)$for all $x, y \in \mathbb{Z}$

### Fundamental Theorem of Arithmetic

Every integer $n \geq 2 $has a **unique** prime factorization:

$$ n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$$

### Euclidean Algorithm

Find $\gcd(a, b) $by repeated division $$ a = q_1 b + r_1, \quad b = q_2 r_1 + r_2, \quad r_1 = q_3 r_2 + r_3, \quad \dots $$ Continue until$ r_n = 0 $, then $\gcd(a,b) = r_{n-1} $.

**Extended Euclidean Algorithm** also finds $x, y $such that

$$ ax + by = \gcd(a,b)$$## 2. Modular Arithmetic $a \equiv b \pmod{n}$ means $n \mid (a - b)$.

### Congruence Classes

$\mathbb{Z}/n\mathbb{Z} = \{[0], [1], \dots, [n-1]\} $forms a ring under addition and multiplication mod $n $.

### Key Theorems

| Theorem | Statement |
|---------|-----------|
| **Fermat's Little** | If $p $is prime and $\gcd(a,p) = 1 $, then $a^{p-1} \equiv 1 \pmod{p}$ |
| **Euler's** | $a^{\phi(n)} \equiv 1 \pmod{n}$when $\gcd(a,n) = 1 $ |
| **Chinese Remainder** | If $\gcd(m_i, m_j) = 1 $, the system $x \equiv a_i \pmod{m_i}$has a unique solution mod $M = \prod m_i$ |
| **Wilson's** | $(p-1)! \equiv -1 \pmod{p}$ |

Where $\phi(n) $is **Euler's totient function**:$$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)

$$

## 3. Cryptographic Applications

### RSA Encryption

```mermaid
flowchart LR
 P[Choose p, q primes] --> N[Compute N = pq]
 N --> PHI[Compute φ\(N\) = \(\(p-1\)(q-1)\)]
 PHI --> E[Choose e with gcd\(e, φ(N)\) = 1]
 E --> D[Compute d = e⁻¹ mod φ\(N\)]
 D --> PK[Public Key: \(N, e\)]
 D --> SK[Private Key: \(N, d\)]
```

**Encryption:** $c = m^e \pmod{N}$**Decryption:**$m = c^d \pmod{N}$**Security** relies on difficulty of factoring $N = pq $when $p, q$ are large primes.

### Diffie-Hellman Key Exchange

Public: prime $p$, generator $g$. Alice sends $A = g^a \pmod{p}$, Bob sends $B = g^b \pmod{p}$.
Shared secret: $K = g^{ab} \pmod{p} = A^b = B^a$.

## 4. Quadratic Residues

$a $is a **quadratic residue** mod $p $if $x^2 \equiv a \pmod{p}$ has a solution.

**Legendre Symbol:**

$$\left(\frac{a}{p}\right) = \begin{cases} 1 & \text{if } a \text{ is a QR mod } p \\ -1 & \text{if } a \text{ is a QNR mod } p \\ 0 & \text{if } p \mid a \end{cases} $$**Law of Quadratic Reciprocity:** For odd primes $p \neq q$:

$$\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}} $$

## 5. Diophantine Equations

| Type | Form | Solution Method |
|------|------|----------------|
| **Linear** | $ax + by = c$ | Extended Euclidean Algorithm (solution iff $\gcd(a,b) \mid c $) |
| **Pythagorean** | $x^2 + y^2 = z^2$ | $x = m^2 - n^2, \; y = 2mn, \; z = m^2 + n^2$ |
| **Fermat's Last** | $x^n + y^n = z^n$, $n \geq 3$ | No solution (proved by Andrew Wiles, 1995) |

## 6. Applications

| Field | Application |
|-------|-------------|
| **Cryptography** | RSA, ECC, Diffie-Hellman, digital signatures |
| **Coding Theory** | Error-correcting codes (Reed-Solomon, BCH) |
| **Random Number Generation** | Linear congruential generators: $X_{n+1} = (aX_n + c) \pmod{m}$ |
| **Hash Functions** | Modular hashing for data structures |
| **Geodesy** | Pseudorandom codes in GNSS signals |

## Practice Problems

1. Use the Euclidean Algorithm to find $\gcd(252, 105) $and express it as $252x + 105y$.
2. Solve the system: $x \equiv 2 \pmod{3}$, $x \equiv 3 \pmod{5}$, $x \equiv 2 \pmod{7}$.
3. Implement RSA with $p = 61$, $q = 53$, $e = 17$. Encrypt $ m = 42$.
4. Prove that there are infinitely many primes. (Hint: Euclid's proof by contradiction)

## References

- Hardy, G.H. & Wright, E.M. (2008). *An Introduction to the Theory of Numbers*. Oxford.
- Rosen, K.H. (2012). *Elementary Number Theory and Its Applications*. Pearson.
- Koblitz, N. (1994). *A Course in Number Theory and Cryptography*. Springer.

---
*See also: [[Algorithms]], [[Abstract Algebra]], [[Probability Foundations]]*
