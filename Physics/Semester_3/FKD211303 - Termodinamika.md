---
code: FKD211303
name: Termodinamika
SKS: 3
semester: 3
department: Fisika
tags: [physics, thermodynamics, entropy, heat, energy, statistical-foundations]
created: 2026-07-27
---

# FKD211303 — Termodinamika

## Course Overview

Thermodynamics describes energy transfer, entropy, and the direction of natural processes. This course covers the four laws of thermodynamics, the concept of entropy, heat engines and refrigerators, and provides a bridge to the microscopic statistical interpretation that underpins material science, atmospheric physics, and energy systems.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Fisika Dasar I, Kalkulus II
**Co-requisites:** Fisika Klasik, Statistika Dasar

---

## 📋 Topics & Outline

### Unit 1: Laws of Thermodynamics (Weeks 1–4)

- **Zeroth Law:** If A is in thermal equilibrium with B, and B with C, then A with C

- **Temperature** as a fundamental concept: absolute scale, Kelvin

- **Thermal equilibrium** and the concept of temperature

- **First Law:** ΔU = Q - W (or ΔU = Q + W, depending on convention)
 - Internal energy as a state function
 - Heat (Q) and work (W) as path functions
 - Specific heats: C_p vs. C_v, and C_p - C_v = nR (ideal gas)

- **Work done by gas:** W = ∫ P dV
 - Work in isothermal, isobaric, isochoric, adiabatic processes

- **Enthalpy:** H = U + PV, and its usefulness at constant pressure

### Unit 2: Entropy and the Second Law (Weeks 5–9)

- **Second Law of Thermodynamics:**
 - Clausius statement: heat cannot spontaneously flow from cold to hot
 - Kelvin-Planck statement: no engine can convert heat completely to work
 - These statements are equivalent

- **Entropy:** dS ≥ δQ/T (Clausius inequality)
 - Entropy as a state function: ΔS = ∫ δQ_rev/T
 - Entropy is non-decreasing: ΔS_universe ≥ 0

- **Reversible vs. irreversible processes**

- **Entropy and disorder:** statistical interpretation — Ω = microstates
 ```
 S = k_B ln Ω (Boltzmann)
 ```

- **Ideal gas entropy change:** ΔS = nC_v ln(T₂/T₁) + nR ln(V₂/V₁)

### Unit 3: Heat Engines and Refrigerators (Weeks 10–13)

- **Carnot cycle** (four-step: isothermal expansion → adiabatic expansion → isothermal compression → adiabatic compression)
 ```
 η_Carnot = 1 - T_cold/T_hot (maximum efficiency)
 ```

- **Carnot's theorem:** no engine is more efficient than a Carnot engine

- **Reversed Carnot cycle:** refrigerator COP = T_cold/(T_hot - T_cold)

- **Real engines:** Otto cycle (gasoline), Diesel cycle, Brayton cycle

- **Clausius inequality:** ∮ δQ/T ≤ 0 for all cycles

- **Entropy production** in real processes

### Unit 4: Thermodynamic Potentials and Phase Transitions (Weeks 14–16)

- **Free energy:** F = U - TS (Helmholtz free energy, minimizes at equilibrium)

- **Gibbs free energy:** G = H - TS (equilibrium at constant T, P)

- **Maxwell relations:** thermodynamic identities connecting partial derivatives

- **Phase transitions:** first-order (latent heat) and second-order (continuous)
 - Water: solid → liquid → gas
 - Liquid-gas critical point

- **Clausius-Clapeyron equation:** dP/dT = L/(TΔV)

---

## 🔬 Key Equations

```
First Law: ΔU = Q - W
Ideal Gas: PV = nRT
Entropy Change: ΔS = ∫δQ_rev/T
Boltzmann: S = k_B ln Ω
Carnot Efficiency: η = 1 - T_C/T_H
Free Energy: F = U - TS
Gibbs Energy: G = H - TS = U + PV - TS
Clausius-Clapeyron: dP/dT = L/(TΔV)
Specific Heat: C_p - C_v = nR
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Apply the four laws of thermodynamics to physical systems
2. Calculate entropy changes for various processes
3. Analyze heat engines, refrigerators, and their efficiencies
4. Use the Boltzmann interpretation to connect macro- and micro-physics
5. Apply thermodynamic potentials (F, G) to predict equilibrium conditions
6. Understand phase transitions and their thermodynamic description

---

## 📚 References

1. Kittel, C. & Kroemer, H. (1980). *Thermal Physics*, 2nd ed. W.H. Freeman.
2. Zemansky, M.W. & Dittman, R.H. (1997). *Heat and Thermodynamics*, 8th ed. McGraw-Hill.
3. Callen, H.B. (1985). *Thermodynamics and an Introduction to Thermostatistics*, 2nd ed. Wiley.
4. Fermi, E. (1937). *Thermodynamics*. Dover. (Elegant, concise)
5. MIT OCW 8.044 Statistical Physics I: https://ocw.mit.edu
