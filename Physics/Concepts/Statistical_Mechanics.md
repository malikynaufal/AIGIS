---
tags: [physics, concept, aigis]
aliases: [Statistical Mechanics]
created: 2026-07-27
---

# Statistical Mechanics

> Microstates, partition functions, ensembles, quantum statistics, phase transitions

> **Part of:** [[Physics MOC]] · [[Physics_Curriculum_Guide]] · [[Study Plan]]

---

## 📚 Core Concept

> **Core idea in one sentence:** Statistical mechanics connects microscopic particle behavior to macroscopic thermodynamic properties using probability and counting.

> **Geodesy Connection:** Atmospheric modeling, particle distributions in plasma (ionosphere), and stochastic processes in geodetic measurements.

---

## 🧮 Key Equations

\begin{equation}
S = k_B \\ln \\Omega
\\end{equation}
\\text{(Boltzmann's entropy formula)}

\begin{equation}
Z = \\sum_i e^{-\\beta E_i}
\\end{equation}
\\text{(Canonical partition function, }\\beta = 1/k_BT\\text{)}

\begin{equation}
f(E) = \\frac{g(E)}{Z} e^{-\\beta E}
\\end{equation}
\\text{(Boltzmann distribution)}

### Distribution Functions

| Statistics | Distribution | Application |
|------------|-------------|-------------|
| Maxwell-Boltzmann | $f(v) = 4\\pi n\\left(\\frac{m}{2\\pi k_BT}\\right)^{3/2} v^2 e^{-mv^2/2k_BT} $ | Classical gas |
| Bose-Einstein | $ f(E) = \\frac{1}{e^{(E-\\mu)/k_BT} - 1} $ | Photons, phonons |
| Fermi-Dirac | $ f(E) = \\frac{1}{e^{(E-\\mu)/k_BT} + 1}$ | Electrons |

---

## 🧭 Physical Intuition & Mental Models

> **Visual analogy:** Like rolling dice millions of times — individual outcomes are random, but averages follow predictable distributions.

> **Key insight:** Temperature is a measure of how spread out energy is among particles; entropy measures the number of ways to arrange them.

> **Geodesy intuition:** Statistical mechanics underpins the probabilistic treatment of measurement errors and the physics of Earth's atmosphere.

---

## 🔗 Links

- **Related:** [[Thermodynamics]] · [[Kinetic_Theory]]
- **Geodesy:** [[Atmospheric_Physics]] · [[Orbital_Mechanics]]
- **Study Pack:** [[_Study Packs/]]

*Last updated: 2026-07-27*