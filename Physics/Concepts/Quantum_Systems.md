---
tags: [physics, concept, aigis]
aliases: [Quantum Systems]
created: 2026-07-27
---

# Quantum Systems (Sistem Kuantum)

> Harmonic oscillator, hydrogen atom, angular momentum, spin, perturbation theory

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Quantum mechanics provides exact analytical solutions for key physical systems — harmonic oscillator, hydrogen atom, rigid rotor — and systematic approximation methods for complex systems through perturbation theory.

> **Geodesy Connection:** Atomic clock physics — hydrogen masers and cesium standards depend on quantum energy level transitions. Quantum sensors (atom interferometers) are emerging tools for precision gravimetry.

---

## 🧮 Key Equations

### Quantum Harmonic Oscillator (Osilator Harmonik Kuantum)

The energy eigenvalues of the quantum harmonic oscillator are equally spaced:

$$
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \ldots
$$

The ground state energy $E_0 = \frac{1}{2}\hbar\omega$ is non-zero — this is zero-point energy (energi titik nol). The creation and annihilation operators satisfy:

$$
a^\dagger |n\rangle = \sqrt{n+1}|n+1\rangle, \quad a|n\rangle = \sqrt{n}|n-1\rangle
$$

$$
\hat{H} = \hbar\omega\left(a^\dagger a + \frac{1}{2}\right)
$$

### Hydrogen Atom (Atom Hidrogen)

The energy levels of hydrogen are:

$$
E_n = -\frac{m_e e^4}{32\pi^2\varepsilon_0^2\hbar^2}\frac{1}{n^2} = -\frac{13.6 \text{ eV}}{n^2}
$$

The wavefunctions are characterized by quantum numbers $(n, l, m_l)$:

$$
\psi_{nlm}(r, \theta, \phi) = R_{nl}(r) Y_l^{m_l}(\theta, \phi)
$$

where $R_{nl}$ are radial functions and $Y_l^{m_l}$ are spherical harmonics. The radial functions involve associated Laguerre polynomials:

$$
R_{nl}(r) = N_{nl} \left(\frac{2r}{na_0}\right)^l e^{-r/(na_0)} L_{n-l-1}^{2l+1}\left(\frac{2r}{na_0}\right)
$$

The Bohr radius is $a_0 = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \approx 0.529$ Å.

### Angular Momentum (Momentum Sudut)

The angular momentum operators satisfy the commutation relations:

$$
[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z, \quad [\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x, \quad [\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y
$$

The eigenvalues are:

$$
\hat{L}^2 |l, m\rangle = \hbar^2 l(l+1) |l, m\rangle, \quad \hat{L}_z |l, m\rangle = \hbar m |l, m\rangle
$$

where $l = 0, 1, 2, \ldots$ and $m = -l, -l+1, \ldots, l$.

### Spin (Spin)

Spin is intrinsic angular momentum with no classical analogue. For spin-$\frac{1}{2}$ particles:

$$
\hat{S}^2 = \hbar^2 \frac{1}{2}\left(\frac{1}{2}+1\right) = \frac{3}{4}\hbar^2
$$

The Pauli spin matrices (Matriks Pauli) for spin-$\frac{1}{2}$ are:

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

$$
\hat{S}_i = \frac{\hbar}{2}\sigma_i
$$

### Perturbation Theory (Teori Penggangguan)

**Non-degenerate first-order** (orde pertama):

$$
E_n^{(1)} = \langle n^{(0)} | H' | n^{(0)} \rangle
$$

**Non-degenerate second-order** (orde kedua):

$$
E_n^{(2)} = \sum_{m \neq n} \frac{|\langle m^{(0)} | H' | n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
$$

**First-order wavefunction correction:**

$$
|n^{(1)}\rangle = \sum_{m \neq n} \frac{\langle m^{(0)} | H' | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle
$$

### Variational Method (Metode Variasional)

For any trial wavefunction $|\psi_{\text{trial}}\rangle$:

$$
E_{\text{trial}} = \frac{\langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle}{\langle \psi_{\text{trial}} | \psi_{\text{trial}} \rangle} \geq E_0
$$

The expectation value always overestimates the true ground state energy $E_0$.

### WKB Approximation

For slowly varying potentials, the semiclassical energy quantization condition is:

$$
\int_{x_1}^{x_2} p(x) \, dx = \left(n + \frac{1}{2}\right)\pi\hbar
$$

where $p(x) = \sqrt{2m(E - V(x))}$ is the local momentum.

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** The hydrogen atom is like a 3D standing wave pattern — electron orbitals are not orbits but probability clouds with specific shapes ($s$, $p$, $d$, $f$).

> **Key insight:** Energy quantization arises from boundary conditions on wavefunctions. The harmonic oscillator's equal spacing ($\hbar\omega$) explains why blackbody radiation, lattice vibrations, and photon states all share the same mathematical structure.

> **Geodesy intuition:** Atomic clocks exploit the precise frequency difference between hyperfine levels — the cesium-133 standard uses the transition at 9,192,631,770 Hz. These are quantum energy level transitions, and their stability directly determines GNSS timing accuracy.

---

## 🧪 Worked Examples

### Example 1: Hydrogen Atom — Balmer Series Wavelength

**Problem:** Calculate the wavelength of the $H\alpha$ line (transition from $n=3$ to $n=2$) in the hydrogen spectrum.

**Solution:**

The energy of the emitted photon is:

$$
\Delta E = E_3 - E_2 = -13.6\left(\frac{1}{9} - \frac{1}{4}\right) = -13.6 \times \left(-\frac{5}{36}\right) = 1.889 \text{ eV}
$$

Converting to wavelength:

$$
\lambda = \frac{hc}{\Delta E} = \frac{1240 \text{ eV·nm}}{1.889 \text{ eV}} \approx 656.3 \text{ nm}
$$

This is the characteristic red line of hydrogen, first observed in stellar spectra.

---

### Example 2: Perturbation of the Hydrogen Atom — Stark Effect

**Problem:** An electric field $\mathcal{E}$ is applied to hydrogen in the ground state. Using first-order perturbation theory with $H' = e\mathcal{E} z$, find the energy shift.

**Solution:**

For the ground state $|1,0,0\rangle$, the first-order energy shift is:

$$
E_1^{(1)} = e\mathcal{E} \langle 1,0,0 | z | 1,0,0\rangle
$$

The hydrogen ground state $\psi_{100}(r) = \frac{2}{a_0^{3/2}} e^{-r/a_0}$ is spherically symmetric. Since $z = r\cos\theta$ is odd under parity, the integral vanishes:

$$
E_1^{(1)} = 0
$$

The first-order Stark effect vanishes for the ground state (non-degenerate). However, for degenerate states like $n=2$, the perturbation mixes $|2,0,0\rangle$ and $|2,1,0\rangle$, producing a linear Stark splitting with energy shift:

$$
\Delta E = \pm 3e\mathcal{E} a_0
$$

---

## 📚 References

| Source | Topic | URL |
|--------|-------|-----|
| MIT OCW 8.04 (Quantum Physics I) | Harmonic oscillator, hydrogen atom, perturbation theory | https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/ |
| OpenStax University Physics Vol. 3 | Quantum mechanics, atomic physics | https://openstax.org/books/university-physics-volume-3/ |
| HyperPhysics — Quantum Atom | Hydrogen energy levels, spectral series | http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hydc.html |
| Griffiths, Introduction to Quantum Mechanics (arXiv:1805.09907) | Ch. 6: Time-independent perturbation theory | https://arxiv.org/abs/1805.09907 |
| MIT OCW 8.05 (Quantum Physics II) | Angular momentum, spin, addition of angular momenta | https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/ |

---

## 🔗 Links

- **Related:** [[Quantum_Foundations]] · [[Quantum_Applications]]
- **Geodesy:** [[Atomic_Clocks]] · [[Relativistic_Applications]]
- **Study Pack:** [[_Study Packs/]]

*Created by AIGIS Physics Specialist · Part of the AIGIS Knowledge Machine*
*Last updated: 2026-07-27*
