---
tags: [aigis, concept, physics, nuclear-physics, particle-physics, standard-model]
created: 2026-07-27
updated: 2026-07-27
---

# Nuclear and Particle Physics
## Radioactive Decay, Nuclear Models, and the Standard Model

**Core Idea:** The nucleus binds protons and neutrons via the strong force. Its instability leads to radioactive decay — essential for geochronology and geodetic applications (cosmogenic nuclide dating, gravimetric surveys). The fundamental particles that make up matter are governed by the Standard Model.

---

## 1. Nuclear Structure

### Nuclear Mass and Binding Energy
The mass of a nucleus is always less than the sum of its constituent nucleons:
$$M(Z,A) = Z m_p + N m_n - \frac{B(A,Z)}{c^2}$$

where $B(A,Z)$ = **binding energy**, $A = Z + N$ = mass number, $Z$ = proton number.

### Semi-Empirical Mass Formula (Bethe-Weizsäcker)
$$B(A,Z) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(A-2Z)^2}{4A} + \delta(A,Z)$$

| Term | Physical Origin | Approximate Value |
|------|----------------|-------------------|
| $a_V A$ | Volume (strong force saturation) | $a_V = 15.56$ MeV |
| $a_S A^{2/3}$ | Surface (fewer neighbors) | $a_S = 17.23$ MeV |
| $a_C Z(Z-1)/A^{1/3}$ | Coulomb repulsion | $a_C = 0.697$ MeV |
| $a_A(A-2Z)^2/4A$ | Asymmetry (Pauli exclusion) | $a_A = 23.29$ MeV |
| $\delta$ | Pairing (even-even > odd > odd-odd) | $\pm 12/\sqrt{A}$ MeV |

### Nuclear Shell Model
Like atomic electrons, nucleons fill quantized shells. **Magic numbers** (nuclei with closed shells) are especially stable:
$$2, 8, 20, 28, 50, 82, 126$$

Nuclei with magic $Z$ and $N$ are **doubly magic** ($^{4}$He, $^{16}$O, $^{40}$Ca, $^{208}$Pb).

### Liquid Drop Model
Nucleus treated as incompressible liquid of nuclear matter:
- Density constant above $A \approx 12$: $\rho_0 \approx 2.3\times10^{17}$ kg/m³
- Radius: $R = r_0 A^{1/3}$, $r_0 \approx 1.2$ fm
- Explains fission (Rayleigh instability of charged liquid drop)

---

## 2. Radioactive Decay

### Exponential Decay Law
$$N(t) = N_0 e^{-\lambda t}$$

where $\lambda$ = decay constant, $N_0$ = initial number of nuclei.

**Activity (disintegrations per second):**
$$A = \lambda N = A_0 e^{-\lambda t}$$

### Half-Life and Mean Life
$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}, \quad \tau_{\text{mean}} = \frac{1}{\lambda}$$

### Types of Radioactive Decay

| Decay | Reaction | Radiation | Energy Range | Key Example |
|-------|----------|-----------|-------------|-------------|
| **Alpha ($\alpha$)** | $^{A}_{Z}X \to ^{A-4}_{Z-2}Y + ^4_2\text{He}$ | $\alpha$ (²He nucleus) | 4–9 MeV | $^{238}$U → $^{234}$Th |
| **Beta-minus ($\beta^-$)** | $n \to p + e^- + \bar{\nu}_e$ | $e^-$ + antineutrino | < 1 MeV | $^{14}$C → $^{14}$N |
| **Beta-plus ($\beta^+$)** | $p \to n + e^+ + \nu_e$ | $e^+$ + neutrino | < 1 MeV | $^{22}$Na → $^{22}$Ne |
| **Electron capture** | $p + e^- \to n + \nu_e$ | X-ray, $\nu_e$ | Variable | $^{40}$K → $^{40}$Ar |
| **Gamma ($\gamma$)** | $^{A}_{Z}X^* \to ^{A}_{Z}X + \gamma$ | Photon | keV–MeV | $^{60}$Co → $^{60}$Ni |
| **Fission** | Heavy nucleus → 2 medium nuclei | Fragments + n + $\gamma$ | ~200 MeV | $^{235}$U + n → fission |

### Beta Decay (Fermi Theory)
$$\frac{dN}{dt} = -G_F^2 |M_{fi}|^2 E_e^2 (E_0 - E_e)^2$$

where $G_F$ = Fermi constant ($1.166\times10^{-5}$ GeV⁻²), $E_0$ = endpoint energy.

**Key properties:**
- Continuous energy spectrum (neutrino carries off energy)
- Parity-violating (V-A theory)
- $K$-capture / electron capture competes with $\beta^+$ when $E < 2m_e c^2$

### Alpha Decay (Tunneling)
The $\alpha$ particle must tunnel through the Coulomb barrier:
$$P \propto \exp\left(-\frac{2}{\hbar}\int_{R}^{b}\sqrt{2m(V(r)-E)}\,dr\right)$$

**Geiger-Nuttall law:**
$$\log_{10}\lambda = a + b\cdot\log_{10}E_\alpha$$

- Shorter half-life → more energetic alpha particle

---

## 3. Geochronological Applications

### Radiocarbon Dating ($^{14}$C)
- $^{14}$C ($t_{1/2} = 5730$ yr) produced in atmosphere by cosmic rays
- Absorbed by living organisms; decays after death
- Range: ~200–50,000 years
$$t = \frac{t_{1/2}}{\ln 2}\ln\frac{A_0}{A} = 8267 \ln\frac{A_0}{A} \text{ (years)}$$

### Potassium-Argon Dating ($^{40}$K)
- $^{40}$K ($t_{1/2} = 1.25$ Ga) decays to $^{40}$Ar by electron capture
- Argon accumulates in mineral crystal; released by melting for analysis
- Range: >100,000 years — used for volcanic rocks in geology and geochronology

### Uranium-Series Disequilibrium
- $^{238}$U decay chain through $^{234}$U → $^{230}$Th → $^{226}$Ra → $^{222}$Rn → ... → $^{206}$Pb
- Different half-lives in chain create disequilibrium
- Useful for dating corals, speleothems (cave deposits): $^{230}$Th/$^{234}$U method (10–350 kyr)

---

## 4. The Standard Model of Particle Physics

### Fundamental Particles

| Generation | Quarks | Leptons |
|------------|--------|---------|
| 1st | u (up), d (down) | $e$ (electron), $\nu_e$ (electron neutrino) |
| 2nd | c (charm), s (strange) | $\mu$ (muon), $\nu_\mu$ (muon neutrino) |
| 3rd | t (top), b (bottom) | $\tau$ (tau), $\nu_\tau$ (tau neutrino) |

**Properties:**
- Quarks carry color charge, have fractional electric charge: u = +⅔e, d = −⅓e
- Leptons: electric charge −1e (or 0 for neutrinos)
- All have spin-½ (fermions)
- Each quark has 3 color states → total quark degrees of freedom = 18

### Bosons (Force Carriers)

| Boson | Spin | Force | Mass (GeV/$c^2$) | Mediates |
|-------|------|-------|------------------|----------|
| $\gamma$ (photon) | 1 | EM | 0 | Electromagnetism |
| $g$ (gluon) | 1 | Strong | 0 | Strong (color) |
| $W^\pm$ | 1 | Weak | 80.4 | Charged weak current |
| $Z^0$ | 1 | Weak | 91.2 | Neutral weak current |
| Higgs | 0 | Mass generation | 125.1 | Gives mass to W, Z, fermions |

### Gauge Symmetry of the Standard Model
$$SU(3)_C \times SU(2)_L \times U(1)_Y \xrightarrow{\text{Higgs}} SU(3)_C \times U(1)_{EM}$$

where:
- $SU(3)_C$ = color symmetry → QCD (strong force)
- $SU(2)_L \times U(1)_Y$ → electroweak unification
- Higgs mechanism breaks electroweak symmetry → $W^\pm, Z^0$ acquire mass

### Fundamental Interactions

| Force | Relative Strength | Range | Mediator | Unification |
|-------|-------------------|-------|----------|-------------|
| Strong | 1 | ~1 fm ($10^{-15}$ m) | Gluons | QCD |
| Electromagnetic | $10^{-2}$ | Infinite | Photon | QED |
| Weak | $10^{-6}$ | ~0.001 fm | $W^\pm$, $Z^0$ | Electroweak |
| Gravitational | $10^{-39}$ | Infinite | Graviton (hypothetical) | General Relativity |

---

## 5. Strong Force and QCD

### Quark Confinement
Quarks are never observed free — they are confined inside hadrons by the strong force.

**Potential between quarks (Cornell potential):**
$$V(r) = -\frac{4}{3}\frac{\alpha_s}{r} + kr$$

where $\alpha_s$ = strong coupling constant (~0.1–0.3 at GeV scales), $k \approx 1$ GeV/fm = string tension.

### Hadron Classification
| Type | Composition | Examples |
|------|-------------|----------|
| Baryons | $qqq$ | p ($uud$), n ($udd$), $\Delta^{++}$ ($uuu$) |
| Mesons | $q\bar{q}$ | $\pi^+$ ($u\bar{d}$), $\pi^0$ (mix), $K^+$ ($u\bar{s}$) |
| Pentaquark | $qqqq\bar{q}$ | Discovered 2015 (LHCb) |

### Color Charge
Each quark carries one of three "colors": red (r), green (g), blue (b).
- Hadrons must be **color singlets** (color-neutral): $qqq$ or $q\bar{q}$
- Gluons carry color-anticolor (8 types)

---

## 6. Weak Force and Beta Decay

### Charged Current (CC)
$$d \to u + W^- \to u + e^- + \bar{\nu}_e$$
$$W^+ \to e^+ + \nu_e$$

### Neutral Current (NC)
$$f + Z^0 \to f + Z^0$$
- Elastic scattering: $\nu_e + e^- \to \nu_e + e^-$ (via $Z^0$)
- Discovered at Gargamelle (CERN, 1973)

### CKM Matrix (Quark Mixing)
$$\begin{pmatrix} d' \\ s' \\ b' \end{pmatrix} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix} \begin{pmatrix} d \\ s \\ b \end{pmatrix}$$

$V_{ud} \approx 0.974$, $V_{us} \approx 0.225$ — small mixing angles for light quarks, large for heavy.

---

## 7. Neutrino Physics

### Neutrino Oscillations
Flavor eigenstates ($\nu_e, \nu_\mu, \nu_\tau$) are mixtures of mass eigenstates ($\nu_1, \nu_2, \nu_3$).

**Oscillation probability (two-flavor approx.):**
$$P(\nu_\alpha \to \nu_\beta) = \sin^2 2\theta \cdot \sin^2\left(\frac{\Delta m^2 L}{4E\hbar c}\right)$$

where $\theta$ = mixing angle, $\Delta m^2 = m_2^2 - m_1^2$, $L$ = propagation distance, $E$ = neutrino energy.

### Evidence for Neutrino Mass
- Atmospheric: $\Delta m^2_{\text{atm}} \approx 2.5\times10^{-3}$ eV² (Super-Kamiokande, 1998)
- Solar: $\Delta m^2_{\text{sol}} \approx 7.5\times10^{-5}$ eV² (SNO, 2001)
- Upper limit: $\sum m_\nu < 0.12$ eV (cosmological bound)

---

## 8. Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $N(t) = N_0 e^{-\lambda t}$ | Exponential decay | Radioactivity |
| $t_{1/2} = \ln 2/\lambda$ | Half-life | Decay rate |
| $B = a_V A - a_S A^{2/3} - \ldots$ | SEMF | Nuclear binding energy |
| $R = r_0 A^{1/3}$ | Nuclear radius | Nucleus size |
| $\alpha_s \approx 0.1\text{–}0.3$ | Strong coupling | QCD |

---

## Problems
1. Calculate the binding energy of $^{12}$C ($M = 12.00000$ u) using the SEMF.
2. Determine the decay constant and activity of $^{238}$U ($t_{1/2} = 4.47$ Ga).
3. Explain why beta decay requires a neutrino (conservation of energy, momentum, and lepton number).
4. Why are $^{14}$C and $^{40}$K useful for dating geological/ archaeological samples?
5. Discuss the evidence for quark confinement from deep inelastic scattering.
6. What determines whether a particle is a meson vs. baryon? Explain in terms of color charge.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
