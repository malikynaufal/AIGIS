---
tags: [physics, concept, aigis, thermodynamics, heat, energy, earth]
aliases: [Thermodynamics, Thermo Pack]
created: 2026-07-27
updated: 2026-07-27
---

# Thermodynamics & Heat Transfer

## For Geodesy & Geophysics Applications

**Core idea:** Thermodynamics describes energy transfer between heat and work. In geodesy, these principles apply to tropospheric delay modeling, hydrographic surveying, and ocean-atmosphere interactions affecting satellite positioning.

---

## 📚 Core Concept

### The Four Laws of Thermodynamics

**Zeroth Law (Thermal Equilibrium)**
If $A \leftrightarrow B$ and $B \leftrightarrow C$, then $A \leftrightarrow C$. Temperature is defined as the property that determines thermal equilibrium.

**First Law (Conservation of Energy)**
$$ dU = \delta Q - \delta W $$

The internal energy change $dU$ equals heat added $\delta Q$ minus work done $\delta W$. This is the conservation of energy applied to thermodynamic systems.

**Geodesy Connection:** Tropospheric delay modeling — the heat content of the atmosphere affects GNSS signal propagation speed, directly impacting positioning accuracy.

**Second Law (Entropy)**
$$ \Delta S \geq 0 $$

Entropy of an isolated system never decreases. Heat flows spontaneously from hot to cold, not the reverse.

**Geodesy Connection:** Ocean-atmosphere heat exchange drives weather patterns that affect satellite signal propagation and altimetry measurements.

**Third Law**
Absolute zero cannot be reached in a finite number of steps. As $T \to 0$, entropy $S \to 0$ for perfect crystalline substances.

---

## 🧮 Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| $dU = \delta Q - \delta W$ | First Law | Energy conservation |
| $\Delta S \geq 0$ | Second Law | Entropy never decreases |
| $\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$ | Carnot efficiency | Maximum heat engine efficiency |
| $F = U - TS$ | Helmholtz free energy | Available work at constant $T, V$ |
| $G = H - TS$ | Gibbs free energy | Available work at constant $T, P$ |
| $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$ | Maxwell relation 1 | Connecting $T$-$V$-$P$-$S$ |

### Maxwell Relations (Complete Set)

| # | Relation |
|---|----------|
| 1 | $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$ |
| 2 | $\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P$ |
| 3 | $\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V$ |
| 4 | $-\left(\frac{\partial S}{\partial P}\right)_T = \left(\frac{\partial V}{\partial T}\right)_P$ |

---

## 📖 Conceptual Summary

### For Students (S1 Level)

Thermodynamics in geodesy is essential for:

1. **Tropospheric Delay Modeling** — The GNSS signal speed depends on atmospheric temperature, pressure, and humidity. Refractivity $n = 1 + 776.7 \times 10^{-8} \frac{P}{T} + 3.73 \times 10^5 \frac{e}{T^2}$.

2. **Hydrographic Surveying** — Sound speed in seawater depends on temperature, salinity, and pressure via the UNESCO equation.

3. **Ocean-Atmosphere Interactions** — Heat exchange drives sea surface height variations that altimeters measure.

### Key Terminology
- **$U$ (Internal Energy)** — *Energi dalam* — total microscopic energy of a system
- **$S$ (Entropy)** — *Entropi* — measure of disorder; always increases in spontaneous processes
- **$T$ (Temperature)** — *Suhu* — thermodynamic temperature in Kelvin
- **$H$ (Enthalpy)** — *Entalpi* — $H = U + PV$; useful at constant pressure
- **G (Gibbs Free Energy)** — *Energi Bebas Gibbs* — $G = H - TS$; spontaneity criterion at constant $T, P$

---

## 🔢 Worked Examples

### Example 1: Carnot Engine Efficiency

A heat engine operates between a hot reservoir at $T_H = 600\,\text{K}$ and a cold reservoir at $T_C = 300\,\text{K}$.

$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H} = 1 - \frac{300}{600} = 0.50 = 50\%$$

This is the maximum possible efficiency. Real engines achieve less due to irreversibilities.

### Example 2: Tropospheric Refractivity

Given: $P = 1013.25\,\text{hPa}$, $T = 288.15\,\text{K}$, $e = 10\,\text{hPa}$:

$$n - 1 = 776.7 \times 10^{-8} \frac{101325}{288.15} + 3.73 \times 10^5 \frac{1000}{288.15^2}$$

$$n - 1 \approx 2.77 \times 10^{-4} + 4.48 \times 10^{-3} \approx 4.76 \times 10^{-3}$$

This $n - 1$ causes about 2.3 m of GNSS signal delay at zenith.

---

## 🌍 Geodesy Applications

### Tropospheric Delay in GNSS

The troposphere delays GNSS signals by $\sim$2.3 m at zenith. This delay is modeled as:

$$\Delta L_{\text{trop}} = \frac{P_0 \cdot k_1}{p_0} + \text{(hydrostatic)} + \text{(wet component)}$$

where the hydrostatic part dominates and depends on surface pressure (thermodynamic measurement).

### Hydrographic Surveying

Sound velocity in water depends on temperature $T$, salinity $S$, and pressure $p$:

$$c = 1449.2 + 4.6T - 0.055T^2 + 0.00029T^3 + (1.34 - 0.01T)(S - 35) + 0.016z$$

(Chen-Millero equation, 1977)

---

## 🤝 Indonesian Glosses

| Term | Indonesian | English |
|------|-----------|---------|
| Kalor | Heat | Energy transfer due to temperature difference |
| Entropi | Entropy | Measure of system disorder |
| Suhu | Temperature | Thermodynamic temperature (K) |
| Energi dalam | Internal energy | Total microscopic energy |
| Mesin kalor | Heat engine | Device converting heat to work |
| Efisiensi | Efficiency | Ratio of useful work to heat input |
| Keseimbangan termal | Thermal equilibrium | No net heat flow between bodies |

---

## 🔗 Links

- **Related:** [[Kinetic_Theory]] · [[Statistical_Mechanics]]
- **Geodesy:** [[Atmospheric_Physics]] · [[Fluid_Mechanics]]
- **Study Pack:** [[_Study Packs/]]

---

## References

1. **OpenStax University Physics Vol. 2** — Thermodynamics chapters. [https://openstax.org/details/books/university-physics-volume-2](https://openstax.org/details/books/university-physics-volume-2)
2. **MIT OCW 8.044 Statistical Physics I** — [https://ocw.mit.edu/courses/8-044-statistical-physics-i-fall-2013/](https://ocw.mit.edu/courses/8-044-statistical-physics-i-fall-2013/)
3. **IGS Atmospheric Working Group** — GNSS Troposphere Mapping Functions. [https://igscb.bkg.bund.de/](https://igscb.bkg.bund.de/)
4. **Chen & Millero (1977)** — "Sound Speed in Seawater," J. Acoust. Soc. Am. [Open Access via NOAA]
5. **Thorne & Blandford (2017)** — *Modern Classical Physics*, Princeton University Press (freely available at arXiv:1710.05839).

---

*Concept maintained by AIGIS — last updated 2026-07-27*
