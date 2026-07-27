---
tags: [physics, study-pack, aigis, thermodynamics, statistical-mechanics]
aliases: [Thermodynamics, Thermo Pack]
created: 2026-07-12
updated: 2026-07-27
---

# 📚 Study Pack — Thermodynamics
_Expanded: Statistical Mechanics Basics

---

## 1. The Four Laws (Review)

### Zeroeth Law (Thermal Equilibrium)
If $A \\leftrightarrow B$ and $B \\leftrightarrow C$, then $A \\leftrightarrow C$. Temperature is a state function.

### First Law (Energy Conservation)
$$dU = \\delta Q - \\delta W$$
$$dU = T\\,dS - P\\,dV + \\mu\\,dN$$

### Second Law (Entropy)
$$dS \\geq \\frac{\\delta Q}{T}$$
For reversible: $dS = \\delta Q_{\\text{rev}}/T$

### Third Law (Absolute Zero)
$$S(T=0) = 0 \\quad \\text{(perfect crystal)}$$

---

## 2. Thermodynamic Potentials

| Potential | Definition | Natural Variables | Use |
|-----------|------------|-------------------|-----|
| Internal Energy $U$ | $U = TS - PV + \\mu N$ | $(S, V, N)$ | Fundamental |
| Enthalpy $H$ | $H = U + PV$ | $(S, P, N)$ | Constant $P$ |
| Helmholtz $F$ | $F = U - TS$ | $(T, V, N)$ | Constant $T,V$ |
| Gibbs $G$ | $G = H - TS$ | $(T, P, N)$ | Constant $T,P$ |

### Maxwell Relations (from exact differentials)
$$\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V$$
$$\\left(\\frac{\\partial S}{\\partial P}\\right)_T = -\\left(\\frac{\\partial V}{\\partial T}\\right)_P$$
$$\\left(\\frac{\\partial V}{\\partial S}\\right)_P = \\left(\\frac{\\partial T}{\\partial P}\\right)_S$$
$$\\left(\\frac{\\partial P}{\\partial S}\\right)_V = -\\left(\\frac{\\partial T}{\\partial V}\\right)_S$$

---

## 3. Heat Engines and Efficiency

### Carnot Cycle (Reversible)
1. Isothermal expansion at $T_H$: $Q_H = nRT_H \\ln(V_2/V_1)$
2. Adiabatic expansion: $T_H V_2^{\\gamma-1} = T_C V_3^{\\gamma-1}$
3. Isothermal compression at $T_C$: $Q_C = nRT_C \\ln(V_4/V_3)$
4. Adiabatic compression: Return to start

**Efficiency:**
$$\\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}$$

### Other Cycles
| Cycle | Description | Efficiency |
|-------|-------------|------------|
| Otto | Constant volume heat addition | $1 - 1/r^{\\gamma-1}$ |
| Diesel | Constant pressure heat addition | $1 - \\frac{1}{\\gamma r^{\\gamma-1}}\\frac{\\alpha^{\\gamma}-1}{\\alpha-1}$ |
| Rankine | Steam power plant | $1 - \\frac{T_{\\text{cond}}}{T_{\\text{boiler}}}$ |

---

## 4. Statistical Mechanics (Introduction)

### Microcanonical Ensemble
All microstates with energy $E$ are equally probable.
$$\\Omega(E) = \\text{number of microstates at energy } E$$

**Boltzmann Entropy:**
$$S = k_B \\ln \\Omega(E)$$

### Canonical Ensemble
System in thermal contact with heat bath at temperature $T$:
$$Z = \\sum_i e^{-\\beta E_i}, \\quad \\beta = \\frac{1}{k_B T}$$

**Partition function** $Z$ encodes all thermodynamic information:
- $F = -k_B T \\ln Z$
- $U = -\\frac{\\partial \\ln Z}{\\partial \\beta}$
- $S = k_B (\\ln Z + \\beta U)$
- $P = k_B T \\frac{\\partial \\ln Z}{\\partial V}$

### Ideal Gas (Canonical)
Single particle: $Z_1 = V (\\frac{m k_B T}{2\\pi \\hbar^2})^{3/2}$

$N$ indistinguishable particles: $Z = \\frac{Z_1^N}{N!}$

**Results:**
- $U = \\frac{3}{2} N k_B T$
- $P = N k_B T / V$ (ideal gas law)
- $S = N k_B [\\ln(V/N) + \\frac{3}{2}\\ln T + \\text{const}]$

### Equipartition Theorem
Each quadratic degree of freedom contributes $\\frac{1}{2}k_B T$ to the average energy.

| System | DoF | $C_V$ (per mole) |
|--------|-----|-----------------|
| Monoatomic gas | 3 | $\\frac{3}{2}R$ |
| Diatomic (rigid) | 5 | $\\frac{5}{2}R$ |
| Solid (Einstein) | 6 | $3R$ |

---

## 5. Phase Transitions

### First-Order Transitions
- Discontinuous first derivative of $G$ (volume, entropy)
- Latent heat: $L = T\\Delta S$
- Examples: melting, boiling, sublimation

### Second-Order Transitions
- Continuous first derivatives, discontinuous second derivatives (heat capacity, compressibility)
- Example: ferromagnetic transition, superfluid transition

### Clausius-Clapeyron Equation
$$\\frac{dP}{dT} = \\frac{L}{T\\Delta V}$$

---

## 6. Applications in Geophysics

### Atmosphere
- **Dry adiabatic lapse rate:** $\\Gamma_d = g/c_p \\approx 9.8$ K/km
- **Moist adiabatic:** $\\Gamma_m \\approx 5$ K/km (variable)
- **Potential temperature:** $\\theta = T(p_0/p)^{R/c_p}$

### Interior
- **Adiabatic gradient in Earth:** $\\frac{dT}{dz} = \\frac{\\alpha T g}{C_P} \\approx 0.3$ K/km
- **Geotherm:** $T(z) = T_0 + q z / k$ (conductive)

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $dU = TdS - PdV$ | First law | Energy balance |
| $F = U - TS$ | Helmholtz | Const $T,V$ |
| $G = H - TS$ | Gibbs | Const $T,P$ |
| $S = k_B \\ln \\Omega$ | Boltzmann entropy | Statistical entropy |
| $Z = \\sum e^{-\\beta E}$ | Partition function | All thermodynamics |
| $C_P - C_V = \\frac{TV\\alpha^2}{\\kappa_T}$ | Heat capacity relation | Thermodynamic identity |
| $dP/dT = L/(T\\Delta V)$ | Clausius-Clapeyron | Phase boundaries |

---

## Problems
1. Calculate the Carnot efficiency between 500 K and 300 K. What is the COP as a refrigerator?
2. Derive $S = Nk_B[\\ln(V/N) + \\frac{3}{2}\\ln T + \\text{const}]$ for an ideal monatomic gas.
3. Show that $C_P - C_V = R$ for an ideal gas.
4. Find the latent heat of vaporization at 100°C from $=3 using Clapeyron eq.
5. Compute the entropy change when 1 kg of ice at 0°C melts and then warms to 20°C.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
