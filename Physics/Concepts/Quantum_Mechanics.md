---
tags: [aigis, concept, physics, quantum-mechanics]
created: 2026-07-27
updated: 2026-07-27
---

# Quantum Mechanics

## Schrödinger Equation, Operators, Hydrogen Atom, Spin

**Core Idea:** Quantum mechanics describes the physics of particles at atomic and subatomic scales using wave functions, operators, and probabilistic interpretation.

---

## 1. Wave Function and Schrödinger Equation

### Wave Function $\Psi(\mathbf{r}, t)$- Contains all information about a quantum system

- Born interpretation:$|\Psi(\mathbf{r}, t)|^2$= probability density

- Normalization:$\int |\Psi|^2 d^3r = 1$### Time-Dependent Schrödinger Equation (TDSE
)

$$i\hbarrac{\partial \Psi(\mathbf{r}, t)}{\partial t} = \hat{H}\Psi(\mathbf{r}, t)$$where $\hat{H} = rac{\hat{p}^2}{2m} + V(\mathbf{r})$,$\hat{p} = -i\hbar
abla$### Time-Independent Schrödinger Equation (TISE)
For stationary states:$\Psi(\mathbf{r}, t) = \psi(\mathbf{r})e^{-iEt/\hbar} $

$$\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})$$This is an **eigenvalue equation** for the Hamiltonian operator.

---

## 2. Operators and Observables

### Correspondence Principle
| Classical Observable | Quantum Operator |
|---------------------|-----------------|
| Position $x$ | $\hat{x} = x$ |
| Momentum $p_x$ | $\hat{p}_x = -i\hbarrac{\partial}{\partial x} $ |
| Energy $E$ | $\hat{H} = i\hbarrac{\partial}{\partial t} $ |
| Angular momentum $L_z$ | $\hat{L}_z = -i\hbarrac{\partial}{\partial \phi} $ |

### Commutation Relations

$$[\hat{x}, \hat{p}_x] = i\hbar[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z \quad 	ext{(cyclic)
}

$$### Expectation Value$$

\langle \hat{A} 
angle = \int \psi^* \hat{A} \psi \, d^3r$$---

## 3. Heisenberg Uncertainty Principle

$$\sigma_x \sigma_p \geq rac{\hbar}{2}\sigma_E \sigma_t \geq rac{\hbar}{2} $$where $\sigma$= standard deviation of measurement results.

---

## 4. Particle in a Box (Infinite Square Well)

### Potentia
l

$$V(x) = 0 	ext{ for } 0 < x < L, \quad \infty 	ext{ otherwise} $$

### Solutions$$\psi_n(x) = \sqrt{rac{2}{L}} \sin\left(rac{n\pi x}{L}
ight), \quad n = 1, 2, 3, \dot
s

$$### Energy Levels$$

E_n = rac{n^2\pi^2\hbar^2}{2mL^2} $$### Key Features

- Zero-point energy:$E_1 = rac{\pi^2\hbar^2}{2mL^2} > 0$- Energy spacing increases with $n$- Wave functions have $n-1 $nodes

---

## 5. Quantum Harmonic Oscillator

### Potentia
l

$$V(x) = rac{1}{2}kx^2 = rac{1}{2}m\omega^2 x^2$$

### Energy Levels$$E_n = \hbar\omega\left(n + rac{1}{2}
ight), \quad n = 0, 1, 2, \dot
s

$$### Creation/Annihilation Operators$$

\hat{a} = \sqrt{rac{m\omega}{2\hbar}}\left(\hat{x} + rac{i}{m\omega}\hat{p}
ight)\hat{a}^\dagger = \sqrt{rac{m\omega}{2\hbar}}\left(\hat{x} - rac{i}{m\omega}\hat{p}
ight)[\hat{a}, \hat{a}^\dagger] = 1$$**Ground state:**$\hat{a}|0
angle = 0$---

## 6. Hydrogen Atom

### Potentia
l

$$V(r) = -rac{e^2}{4\pi\epsilon_0 r} $$

### Quantum Numbers
| Number | Symbol | Values | Meaning |
|--------|--------|--------|---------|
| Principal | $n$ | $1, 2, 3, \dots$ | Energy level |
| Angular | $l$ | $0, 1, \dots, n-1$ | Orbital shape |
| Magnetic | $m$ | $-l, \dots, +l$ | Orientation in space |
| Spin | $s$ | $\pm 1/2$ | Intrinsic angular momentum |

### Energy Level
s

$$E_n = -rac{me^4}{8\epsilon_0^2 h^2}rac{1}{n^2} = -rac{13.6\,	ext{eV}}{n^2} $$

### Radial Wave Functions$$R_{nl}(r) \propto e^{-r/na_0}\left(rac{2r}{na_0}
ight)^l L_{n-l-1}^{2l+1}\left(rac{2r}{na_0}
ight)$$where $a_0 = rac{4\pi\epsilon_0\hbar^2}{me^2} = 0.529\,	ext{Å} $ (Bohr radius).

### Example: 1s State ($n=1, l=0$)

$$\psi_{100}(r) = rac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0} $$---

## 7. Angular Momentum and Spin

### Orbital Angular Momentum

$$\hat{\mathbf{L}} = \hat{\mathbf{r}} 	imes \hat{\mathbf{p}}\hat{L}^2 = \hbar^2 l(l+1)\hat{L}_z = \hbar m$$### Spin Angular Momentum

- Intrinsic property (not from motion in space)
-$\hat{\mathbf{S}}^2 = \hbar^2 s(s+1)$- For electrons:$s = 1/2$, $\hat{S}_z = \pm\hbar/2$### Total Angular Momentum

$$\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}j = l \pm 1/
2

$$### Spin-Orbit Coupling$$

H_{SO} \propto \hat{\mathbf{L}} \cdot \hat{\mathbf{S}} = rac{1}{2}(j(j+1) - l(l+1) - s(s+1))\hbar^2$$---

## 8. Pauli Exclusion Principle
No two identical fermions can occupy the same quantum state simultaneously
.

$$\psi(\dots, x_i, \dots, x_j, \dots) = -\psi(\dots, x_j, \dots, x_i, \dots)$$

---

## 9. Key Equations Summary

| Equation | Name | Use |
|----------|------|-----|
| $i\hbar\partial_t\Psi = \hat{H}\Psi$ | TDSE | Time evolution |
| $\hat{H}\psi = E\psi$ | TISE | Energy eigenvalues |
| $[\hat{x}, \hat{p}] = i\hbar$ | Canonical commutation | Uncertainty principle |
| $E_n = -rac{13.6\,	ext{eV}}{n^2} $ | Hydrogen energy | Atomic spectra |
| $E_n = \hbar\omega(n + 1/2)$ | QHO energy | Vibrational spectra |
| $\hat{a}^\dagger|n
angle = \sqrt{n+1}|n+1
angle$ | Ladder operators | Number states |

---

## Study Problems
1. Normalize the wave function $\psi(x) = A e^{-lpha x^2} $on$(-\infty, \infty)$.
2. Find the expectation value $\langle x 
angle $for the ground state of the infinite square well.
3. Calculate the probability of finding a 1s hydrogen electron within one Bohr radius.
4. Show that$[H, a^\dagger] = \hbar\omega a^\dagger $for the harmonic oscillator.
5. Determine the degeneracy of the $n=3$ energy level in hydrogen (including spin).

---

## References

- Griffiths, "Introduction to Quantum Mechanics" (3rd ed.)

- Sakurai, "Modern Quantum Mechanics"

- MIT OCW 8.04: Quantum Physics I

- Feynman Lectures Vol. III

- OpenStax University Physics Vol. 3 (Quantum Mechanics)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
