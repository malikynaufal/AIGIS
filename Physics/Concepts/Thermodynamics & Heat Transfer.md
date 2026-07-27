---
tags: [aigis, concept, physics, thermodynamics, heat, energy, earth]
created: 2026-07-27
updated: 2026-07-27
---

# Thermodynamics & Heat Transfer

## For Geodesy & Geophysics Applications

**Core Idea:** Thermodynamics describes energy, heat, and work in physical systems. In geodesy and geophysics, thermodynamics governs Earth's heat flow, atmospheric dynamics, climate-related sea level change, and the thermal behavior of GPS instruments.

---

## Fundamental Concepts

### The Four Laws of Thermodynamics

| Law | Statement | Mathematical Form |
|-----|-----------|------------------|
| **Zeroth** | If A is in equilibrium with B, and B with C, then A is in equilibrium with C | $T_A = T_B = T_C $ |
| **First** | Energy is conserved | $ \Delta U = Q - W $ |
| **Second** | Entropy always increases | $ \Delta S \geq 0 $ |
| **Third** | Absolute zero is unattainable | $ \lim_{T \to 0} S = 0 $ |

### Heat, Work, and Energy

| Quantity | Symbol | Formula | Units |
|----------|--------|---------|-------|
| Heat | $ Q $ | $ Q = mc\Delta T $ | J |
| Work | $ W $ | $ W = \int P\,dV $ | J |
| Internal energy | $ U $ | $ U = \frac{f}{2}nRT $ | J |
| Enthalpy | $ H $ | $ H = U + PV $ | J |
| Entropy | $ S $ | $ dS = \frac{\delta Q}{T} $ | J/K |
| Specific heat | $ c $ | $ c = \frac{Q}{m\Delta T} $ | J/(kg·K) |
| Latent heat | $ L $ | $ Q = mL $ | J/kg |

### Ideal Gas Law

$ PV = nRT = Nk_B T $ $ | Gas | Degrees of freedom $$ f $ | $ \gamma = C_P/C_V $ |
|-----|----------------------|-------------------|
| Monatomic (He, Ne) | 3 | 5/3 = 1.667 |
| Diatomic (N₂, O₂) | 5 | 7/5 = 1.400 |
| Polyatomic | 3N - 6 | ~1.3 |

### Heat Transfer Mechanisms

| Mechanism | Formula | Description |
|-----------|---------|-------------|
| **Conduction** | $ Q = kA\frac{\Delta T}{\Delta x} $ | Heat flow through material |
| **Convection** | $ Q = hA(T_s - T_\infty) $ | Fluid-mediated heat transfer |
| **Radiation** | $ Q = \varepsilon\sigma A T^4 $ | Electromagnetic emission |

**Thermal conductivity (k):**
| Material | k (W/m·K) |
|----------|-----------|
| Copper | 401 |
| Aluminum | 237 |
| Steel | 50 |
| Rock | 2–3 |
| Soil | 0.2–2 |
| Water | 0.6 |
| Air | 0.025 |

---

## In Geodesy & Geophysics Context

### Earth's Heat Flow

**Surface heat flow:** $ q \approx 87\ \text{mW/m}^2 $ (global average)

Contributions:

- Radiogenic heat (U, Th, K): ~50%

- Primordial heat: ~50%

**Heat equation (1D):**

$ $ \frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial z^2} $$

where thermal diffusivity $ \alpha = k/(\rho c_p) $.

### Geothermal Gradient

$ $ \frac{dT}{dz} \approx 25-30\ \text{K/km} $$

Depth to $ 100^\circ $ C: ~3–4 km

Depth to $ 500^\circ $ C: ~15–20 km

### Sea Level Change (Thermal Expansion)

Steric sea level rise from thermal expansion:

$ $ \Delta h = \int_0^H \alpha_T(z) \cdot \Delta T(z)\, dz

$$ -$ \alpha_T $= thermal expansion coefficient (~$ 10^{-4} $/K near surface)

- Current contribution: ~1.5 mm/yr (about 40% of observed sea level rise)

### Atmospheric Thermodynamics

**First law for atmosphere:**

$ $

c_p \frac{dT}{dt} = \frac{dq}{dt} - \frac{R_d T}{p}\frac{dp}{dt
}

**Potential temperature:**

 \theta = T\left(\frac{p_0}{p}\right)^{R_d/c_p}

$$

This is conserved in adiabatic processes — key for atmospheric stability analysis.

### GPS Antenna Temperature

GNSS antennas warm up when exposed to sunlight. Thermal expansion changes:

- Phase center position (mm-level)

- Cable delay (phase changes with temperature)

This is a systematic error source in high-precision GPS.

---

## Key Equations to Memorize

| Equation | Name | Use |
|----------|------|-----|
| $ PV = nRT $ | Ideal gas law | Atmospheric physics |
| $ Q = mc\Delta T $ | Heat capacity | Warming/cooling |
| $ Q = \varepsilon\sigma AT^4 $ | Stefan-Boltzmann | Radiative cooling |
| $ q = -k\frac{dT}{dz} $ | Fourier's law | Conduction |
| $ \Delta S \geq 0 $ | 2nd law | Irreversibility |
| $ U = \frac{f}{2}nRT $ | Internal energy | Kinetic theory |

---

## Related Concepts

- [[Physical Geodesy]] — Earth's gravity and heat coupling

- [[GNSS]] — Instrumental effects

- [[Newtonian Mechanics]] — Atmospheric dynamics basics

---

## Study Problems

1. **Recall:** If Earth's surface heat flow is 87 mW/m² and the lithosphere thickness is 100 km with $ k = 2.5 $ W/m·K, estimate the temperature difference across the lithosphere.
2. **Application:** Compute the steric sea level rise from warming the top 1000 m of ocean by 0.5°C, given $ \alpha_T = 2 \times 10^{-4} $/K.
3. **Derivation:** Derive the lapse rate in a dry adiabat: $ dT/dz = -g/c_p $. (Hint: use hydrostatic balance and first law.)
4. **Real-world:** A GPS monument is buried 2 m deep in solid rock. If the surface temperature swings ±15°C daily, estimate the thermal time constant and whether the monument moves with daily cycles. (Hint: characteristic time $ \tau = d^2/\alpha $.)

---

## Common Mistakes

1. **Confusing heat and temperature:** Heat is energy transfer, temperature is a state variable.
2. **Forgetting sign conventions:** $ \Delta U = Q - W $ (work done BY system), not $+W $.
3. **Treating entropy as disorder only:** It's more precisely a measure of energy dispersal at a given temperature.
4. **Ignoring latent heat:** Phase changes absorb/release huge energy without temperature change.
5. **Assuming linear response:** Heat flow is nonlinear at large $ \Delta T $ because $ k $, $ c $, $ \alpha $ all vary with temperature.

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*