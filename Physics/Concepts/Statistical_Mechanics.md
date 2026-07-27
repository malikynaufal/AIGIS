---
tags: [aigis, concept, physics, statistical-mechanics, thermodynamics, probability]
created: 2026-07-27
updated: 2026-07-27
---

# Statistical Mechanics

## Microstates, Entropy, and the Partition Function

**Core Idea:** Statistical mechanics bridges microscopic particle behavior to macroscopic thermodynamic observables. The partition function $Z $encodes **all** thermodynamic information — temperature, pressure, entropy, heat capacity — in a single generating function.

---

## 1. Microstates and Phase Space

### Phase Space
A system of $N $particles in 3D occupies a$6N$-dimensional phase space: each particle has 3 position and 3 momentum coordinates:

$$\Gamma = (\vec{r}_1, \vec{p}_1, \vec{r}_2, \vec{p}_2, \ldots, \vec{r}_N, \vec{p}_N
)

$$The number of microstates accessible to the system:$$

\Omega(E, V, N) = \frac{1}{h^{3N} N!}\int_{E \leq H(\Gamma) \leq E+\Delta E} d^{3N}p \, d^{3N}q$$where $h$= Planck's constant (makes $\Omega $dimensionless),$N!$corrects for identical particle indistinguishability.

### Microstate vs. Macrostate

- **Microstate:** Complete specification of all particle positions and momenta

- **Macrostate:** Specification of macroscopic variables$(T, P, V, N)$— many microstates can correspond to the same macrostate

### Fundamental Postulate (Ergodic Hypothesis)
All microstates consistent with macroscopic constraints are **equally probable** (a priori).

---

## 2. Entropy — Boltzmann's Definition

### Boltzmann Entrop
y

$$\boxed{S = k_B \ln \Omega} $$where $k_B = 1.381 \times 10^{-23} $J/K is the Boltzmann constant.

**Physical meaning:** Entropy counts the number of microstates compatible with a given macrostate. Higher $S$→ more disorder → more accessible microstates.

### Thermodynamic Entrop
y

$$dS = \frac{\delta Q_{\text{rev}}}{T} $$

Boltzmann's formula is consistent with this: when you add heat reversibly,$T = (\partial S/\partial E)^{-1} $.

### Gibbs Entropy (More General)

$$S = -k_B \sum_i p_i \ln p_i$$For uniform probability $p_i = 1/\Omega$: reduces to $S = k_B \ln \Omega$.

---

## 3. Ensembles

An ensemble is a collection of virtual copies of the system, one for each possible microstate. Different ensembles correspond to different physical constraints.

### Microcanonical Ensemble (NVE)

- Isolated system: fixed $N$, $V$, $E$- All accessible microstates equally probable:$p_i = 1/\Omega$- **Entropy:**$S = k_B \ln \Omega$- **Temperature:**$1/T = \partial S/\partial E$### Canonical Ensemble (NVT)

- System in thermal contact with heat bath at temperature $T$- Energy fluctuates;$T $fixed

- **Probability of microstate $i$:**

$$p_i = \frac{e^{-\beta E_i}}{Z}, \quad \beta = \frac{1}{k_B T
}

$$- **Partition function:**$$

Z = \sum_{i=1}^{\text{all states}} e^{-\beta E_i} $$

### Grand Canonical Ensemble ($\mu VT$)

- System exchanges both energy and particles with reservoir

- **Grand partition function:**

$$\mathcal{Z} = \sum_{N=0}^{\infty} e^{\beta \mu N} Z(N, V, T)$$where $\mu$= chemical potential.

---

## 4. Partition Function — The Master Key

### Thermodynamics from $Z$(Canonical)

| Quantity | Formula |
|----------|---------|
| **Free energy (Helmholtz)** | $F = -k_B T \ln Z$ |
| **Internal energy** | $U = -\frac{\partial \ln Z}{\partial \beta} $ |
| **Entropy** | $S = k_B (\ln Z + \beta U)$ |
| **Pressure** | $P = k_B T \frac{\partial \ln Z}{\partial V} $ |
| **Heat capacity** | $C_V = \left(\frac{\partial U}{\partial T}\right)_V$ |
| **Chemical potential** | $\mu = -k_B T \frac{\partial \ln Z}{\partial N} $ |

### Single-Particle Partition Function
For non-interacting particles
:

$$Z_1 = \sum_j e^{-\beta \epsilon_j} $$

**Translational (ideal gas):*
*

$$Z_1 = \frac{V}{\lambda_{\text{th}}^3}, \quad \lambda_{\text{th}} = \sqrt{\frac{2\pi\hbar^2}{m k_B T}} = \frac{h}{\sqrt{2\pi m k_B T}} $$where $\lambda_{\text{th}} $= thermal de Broglie wavelength.

###$N$-Particle Ideal Gas (Indistinguishable)

$$Z = \frac{Z_1^N}{N!
}

$$**Free energy:**$$

F = -k_B T N \left[\ln\frac{V}{N\lambda_{\text{th}}^3} + 1\right
]

$$**Entropy (Sackur-Tetrode):**$$

S = Nk_B\left[\ln\left(\frac{V}{N\lambda_{\text{th}}^3}\right) + \frac{5}{2}\right]$$**Equation of state:**$P = Nk_B T/V$(ideal gas law recovered!)

**Internal energy:**$U = \frac{3}{2}Nk_B T$---

## 5. Boltzmann Distribution

### Energy Distribution
In a heat bath, the probability that a system is in energy state $E_i$:

$$p(E_i) \propto e^{-E_i/(k_B T)
}

$$**Mean energy:**$$

\langle E \rangle = \frac{\sum_i E_i e^{-\beta E_i}}{\sum_i e^{-\beta E_i}} = -\frac{\partial \ln Z}{\partial \beta} $$### Equipartition Theorem
Each **quadratic** degree of freedom contributes $\frac{1}{2}k_B T $to the mean energy.

For a Hamiltonian with $f $quadratic terms
:

$$\langle E \rangle = \frac{f}{2} k_B T$$

**Examples:**
| System | Quadratic DoF | $\langle E\rangle$ | $C_V $per particle |
|--------|--------------|---------------------|---------------------|
| Monoatomic ideal gas | 3 (translational) | $\frac{3}{2}k_B T$ | $\frac{3}{2}k_B$ |
| Diatomic gas (rigid) | 5 (3 trans + 2 rot) | $\frac{5}{2}k_B T$ | $\frac{5}{2}k_B$ |
| Diatomic gas (non-rigid) | 7 (3 trans + 2 rot + 2 vib) | $\frac{7}{2}k_B T$ | $\frac{7}{2}k_B$ |
| Einstein solid (3D) | 6 (3 kinetic + 3 potential) | $3k_B T$ | $3k_B$ |

---

## 6. Quantum Statistics

### Classical Limit (Maxwell-Boltzmann)
Valid when $\lambda_{\text{th}} \ll n^{-1/3} $(dilute gas,$T \gg T_F$):

$$n\lambda_{\text{th}}^3 \ll 
1

$$### Bose-Einstein Statistics (Bosons: integer spin)$$

\langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$- Bosons: photons, gluons,$^4 $He at low $T$- Leads to **Bose-Einstein condensation** at $T < T_{\text{BEC}} $### Fermi-Dirac Statistics (Fermions: half-integer spin
)

$$\langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} + 1} $$

- Fermions: electrons, protons, neutrons

- **Pauli exclusion principle:** at most 1 particle per state

- At $T = 0$: all states up to Fermi energy $E_F $are filled

### Classical Limit Recovery
For $e^{\beta(\epsilon - \mu)} \gg 1$: both BE and FD reduce to Maxwell-Boltzmann:

$$\langle n_i \rangle \approx e^{-\beta(\epsilon_i - \mu)} $$---

## 7. Ideal Gas — From Micro to Macro

### Derivation of the Ideal Gas Law
From $F = -k_B T N[\ln(V/N\lambda_{\text{th}}^3) + 1]$:

$$P = -\left(\frac{\partial F}{\partial V}\right)_{T,N} = \frac{Nk_B T}{V}\boxed{PV = Nk_BT = nk_BT
}

$$### Heat Capacity$$

U = \frac{3}{2}Nk_BT \implies C_V = \frac{3}{2}Nk_B, \quad C_P = C_V + Nk_B = \frac{5}{2}Nk_
B

$$### Mayer's Relation$$

C_P - C_V = Nk_B$$### Internal Energy from Equipartition (Polyatomic)
For a molecule with $f $vibrational modes and rigid rotations
:

$$C_V = \frac{1}{2}Nk_B(3 + 2 + 2f)$$(freezing out vibrational modes at low $T$due to quantum effects:$\hbar\omega \gg k_BT$)

---

## 8. Information Theory Connection

### Shannon Entropy (Information Theory)

$$H = -\sum_i p_i \log_2 p_i \quad [\text{bits}]$$**Boltzmann-Gibbs entropy** is the same expression with $\log$→$\ln $and $k_B $scaling
:

$$S = k_B H_{\text{Shannon}} \cdot \ln 2$$

### Minimum Entropy:$S \to 0 $as $T \to 0 $For a perfect crystal, all particles in ground state:$\Omega = 1$,$S = k_B \ln 1 = 0$. This is the **Third Law of Thermodynamics**.

---

## 9. Application to Atmospheric Physics

### Maxwell-Boltzmann Velocity Distribution

$$f(v) = 4\pi n\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/(2k_BT)} $$- Most probable speed:$v_{\text{mp}} = \sqrt{2k_BT/m} $- Mean speed:$\bar{v} = \sqrt{8k_BT/(\pi m)} $- RMS speed:$v_{\text{rms}} = \sqrt{3k_BT/m} $**For $N_2 $at 300 K:**$v_{\text{rms}} \approx 517 $m/s

### Barometric Formula (Gravitational Stratification
)

$$n(z) = n_0 \exp\left(-\frac{mgz}{k_BT}\right) = n_0\exp\left(-\frac{z}{H}\right)$$where $H = k_BT/(mg) $is the scale height (~8.5 km for Earth's atmosphere).

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $S = k_B\ln\Omega$ | Boltzmann entropy | Micro → macro |
| $Z = \sum e^{-\beta E} $ | Partition function | All thermodynamics |
| $F = -k_BT\ln Z$ | Helmholtz free energy | From partition function |
| $p \propto e^{-\beta E} $ | Boltzmann distribution | Energy probabilities |
| $PV = Nk_BT$ | Ideal gas law | Recovered from statistical mechanics |
| $\langle E\rangle = \frac{f}{2}k_BT$ | Equipartition | Heat capacity |

---

## Problems
1. Calculate the thermal de Broglie wavelength of an $N_2 $molecule at 300 K.
2. Derive the Sackur-Tetrode entropy for an ideal gas of$10^{23} $monoatomic particles.
3. Show that the partition function for a 1D harmonic oscillator is $Z_1 = 1/(1-e^{-\beta\hbar\omega})$.
4. Explain why $C_V $for a diatomic gas decreases at very low temperatures (quantum freezing of rotational modes).
5. Derive the Maxwell velocity distribution from the canonical ensemble.
6. Compare the mean energy of a monoatomic ideal gas using classical and quantum (FD) statistics at $T = 300 $K and $T = 3000$ K.
7. Compute the barometric scale height for Earth's atmosphere and explain the observed tropospheric temperature lapse rate.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
