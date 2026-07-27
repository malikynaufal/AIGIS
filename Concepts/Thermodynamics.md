---
tags: [aigis, concept, physics, thermodynamics, thermal-physics]
created: 2026-07-27
updated: 2026-07-27
---

# Thermodynamics
## Laws, Entropy, Heat Engines, and Thermodynamic Potentials

**Core Idea:** Thermodynamics describes energy, heat, work, and their transformations. Its laws govern everything from heat engines to atmospheric physics.

---

## 1. The Four Laws of Thermodynamics

### Zeroeth Law (Thermal Equilibrium)
$$\text{If } A \leftrightarrow B \text{ and } B \leftrightarrow C \text{, then } A \leftrightarrow C$$

**Meaning:** Temperature is a state function — two systems in thermal equilibrium have the same temperature.

### First Law (Energy Conservation)
$$dU = \delta Q - \delta W \quad \text{or} \quad dU = \delta Q + \delta W_{\text{by}}$$

For infinitesimal changes:
- $dU$: change in internal energy
- $\delta Q$: heat added to system
- $\delta W$: work done by system

**Differential form:** $dU = T\,dS - P\,dV + \mu\,dN$

**Key point:** $U$ is a state function; $Q$ and $W$ are path-dependent.

### Second Law (Entropy)
$$\Delta S \geq \frac{Q}{T_{\text{res}}} \quad \text{(Clausius inequality)}$$

For reversible processes: $\Delta S = \frac{Q}{T}$  
For irreversible processes: $\Delta S > \frac{Q}{T}$

**Entropy as disorder:** $S = k_B \ln \Omega$ (Boltzmann), where $\Omega$ is the number of microstates.

### Third Law (Absolute Zero)
$$\lim_{T \to 0} S = S_0 = \text{constant}$$

Often set to zero: $S(T=0) = 0$ for a perfect crystal.

---

## 2. Thermodynamic Potentials

### Internal Energy
$$U = TS - PV + \mu N$$

For simple compressible systems: $dU = T\,dS - P\,dV$

### Enthalpy
$$H = U + PV$$

$$dH = T\,dS + V\,dP$$

Useful for constant-pressure processes.

### Helmholtz Free Energy
$$F = U - TS$$

$$dF = -S\,dT - P\,dV$$

Useful for constant-$T$, constant-$V$ processes (e.g., chemical reactions).

### Gibbs Free Energy
$$G = H - TS = U + PV - TS$$

$$dG = -S\,dT + V\,dP$$

Useful for constant-$T$, constant-$P$ processes (e.g., phase transitions).

### Maxwell Relations
From $dF = -S\,dT - P\,dV$:
$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V$$

From $dG = -S\,dT + V\,dP$:
$$\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$$

---

## 3. Heat Engines and Refrigerators

### Heat Engine Cycle
A device that converts heat into work:
```
Hot Reservoir (Th) → [Heat Engine] → Work Out + Cold Reservoir (Tc)
```

**Efficiency (Carnot):**
$$\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h}$$

**General efficiency:**
$$\eta = \frac{W}{Q_h} = 1 - \frac{Q_c}{Q_h}$$

### Refrigerator / Heat Pump
Reversed heat engine:
```
Cold Reservoir (Tc) → [Work In] → Hot Reservoir (Th)
```

**Coefficient of Performance (COP):**
$$\text{COP}_{\text{fridge}} = \frac{Q_c}{W} = \frac{T_c}{T_h - T_c}$$
$$\text{COP}_{\text{pump}} = \frac{Q_h}{W} = \frac{T_h}{T_h - T_c}$$

### Carnot Cycle (Reversible)
1. **Isothermal expansion** at $T_h$: $Q_h = nRT_h \ln(V_2/V_1)$
2. **Adiabatic expansion**: $TV^{\gamma-1} = \text{const}$
3. **Isothermal compression** at $T_c$: $Q_c = nRT_c \ln(V_4/V_3)$
4. **Adiabatic compression**: Returns to start

---

## 4. Entropy Calculations

### Entropy Change Formulas

| Process | $\Delta S$ |
|---------|-------------|
| Heating: $T_i \to T_f$ | $\Delta S = \int_{T_i}^{T_f} \frac{C(T)}{T}\,dT$ |
| Phase change (at $T_m$) | $\Delta S = \frac{L_m}{T_m}$ |
| Isothermal expansion | $\Delta S = nR\ln(V_f/V_i)$ |
| Free expansion (ideal gas) | $\Delta S = nR\ln(V_f/V_i)$ |

**Worked Example: Entropy of melting ice**
- Mass of ice: $m = 100$ g = 0.1 kg
- Latent heat of fusion: $L_f = 334$ kJ/kg
- Melting at $T = 273$ K

$$\Delta S = \frac{mL_f}{T} = \frac{0.1 \times 334\times10^3}{273} = 122.3 \text{ J/K}$$

---

## 5. Kinetic Theory of Gases

### Ideal Gas Law
$$PV = nRT = Nk_B T$$

### Pressure from Kinetic Theory
$$P = \frac{1}{3}\frac{N}{V} m\overline{v^2} = \frac{2}{3}\frac{N}{V} \bar{K}_{\text{trans}}$$

### Average Kinetic Energy
$$\bar{K}_{\text{trans}} = \frac{3}{2}k_B T$$

### RMS Speed
$$v_{\text{rms}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3k_B T}{m}} = \sqrt{\frac{3RT}{M}}$$

**Dimensional check:** $[v_{\text{rms}}] = \sqrt{(J/kg)} = \sqrt{(kg\cdot m^2/s^2)/kg} = m/s$ ✓

### Degrees of Freedom
| Molecule | Degrees of Freedom | $C_V$ (per mol) | $C_P$ (per mol) | $\gamma = C_P/C_V$ |
|----------|-------------------|-----------------|----------------|---------------------|
| Monoatomic | 3 | $3R/2$ | $5R/2$ | 5/3 = 1.67 |
| Diatomic | 5 | $5R/2$ | $7R/2$ | 7/5 = 1.40 |
| Linear polyatomic | 5 | $5R/2$ | $7R/2$ | 1.40 |
| Non-linear polyatomic | 6 | $3R$ | $4R$ | 4/3 = 1.33 |

---

## 6. Heat Transfer

### Conduction (Fourier's Law)
$$\frac{dQ}{dt} = -kA\frac{dT}{dx}$$

- $k$: thermal conductivity (W/(m·K))
- $A$: cross-sectional area
- $dT/dx$: temperature gradient

### Convection
$$Q = hA(T_s - T_\infty)$$

- $h$: convective heat transfer coefficient

### Radiation (Stefan-Boltzmann)
$$P = \epsilon\sigma A T^4$$

- $\epsilon$: emissivity (0–1)
- $\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴)

**Black body:** $\epsilon = 1$, absorbs and emits maximally.

---

## 7. Applications in Geophysics

### Atmospheric Thermodynamics
- **Lapse rate:** $\Gamma = -dT/dz \approx 6.5$ K/km (environmental)
- **Dry adiabatic:** $\Gamma_d = g/c_p \approx 9.8$ K/km
- **Moist adiabatic:** $\Gamma_m \approx 5$ K/km (variable)

### Geothermal Gradient
- Average: ~25–30 K/km
- Heat flow: $q = k\,dT/dz \approx 50-100$ mW/m²

---

## Key Equations Summary

| Equation | Name | Use |
|----------|------|-----|
| $PV = nRT$ | Ideal gas law | Gas thermodynamics |
| $dU = \delta Q - \delta W$ | First law | Energy conservation |
| $dS \geq \delta Q/T$ | Second law | Entropy inequality |
| $F = U - TS$ | Helmholtz free energy | Constant $T,V$ |
| $G = H - TS$ | Gibbs free energy | Constant $T,P$ |
| $\eta = 1 - T_c/T_h$ | Carnot efficiency | Max heat engine efficiency |
| $P = \frac{2}{3}\frac{N}{V}\bar{K}$ | Kinetic theory pressure | Gas pressure derivation |
| $P = \epsilon\sigma T^4$ | Stefan-Boltzmann | Black-body radiation |

---

## Study Problems
1. A Carnot engine operates between 500 K and 300 K. Calculate its efficiency and COP as a refrigerator.
2. One mole of ideal monatomic gas undergoes isothermal expansion from 1 L to 10 L at 300 K. Find $Q$, $W$, $\Delta U$, $\Delta S$.
3. Calculate the entropy change when 1 kg of ice at -20°C is heated to steam at 120°C.
4. Derive the Maxwell relation $(\partial S/\partial V)_T = (\partial P/\partial T)_V$ from thermodynamic identities.
5. Show that $C_P - C_V = R$ for an ideal gas.

---

## References
- OpenStax University Physics Vol. 2 (Thermodynamics)
- Kittel & Kroemer, "Thermal Physics"
- Landau & Lifshitz, "Statistical Physics"
- Feynman Lectures Vol. I (Ch. 44-52)

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
