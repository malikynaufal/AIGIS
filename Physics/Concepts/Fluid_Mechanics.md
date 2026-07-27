---
tags: [aigis, concept, physics, fluid-mechanics, hydrodynamics]
created: 2026-07-27
updated: 2026-07-27
---

# Fluid Mechanics

## Bernoulli, Navier‑Stokes, Viscosity

**Core Idea:** Fluids (liquids and gases) obey conservation of mass, momentum, and energy. Their motion is described by the continuity equation, Euler/Navier‑Stokes equations, and Bernoulli’s principle.

---

## 1. Continuity Equation (Mass Conservation)
For incompressible flow ( $\rho = $ const) $ A_1 v_1 = A_2 v_2 $ where $  A $ is cross‑sectional area,$  v $ velocity.

For compressible flow (general)

$ $ \frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{v}) = 0

$$

---

## 2. Euler Equation (Ideal Fluid, No Viscosity)

$ $ \rho\left(\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}
ight) = -\nabla p + \rho \mathbf{g} $$

If flow is steady and along a streamline, integrate to obtain **Bernoulli’s equation**.

---

## 3. Bernoulli’s Equation (Steady, Incompressible, Non‑viscous)

$ $ 

p + rac{1}{2}\rho v^2 +
ho g h = 	ext{constant} $$

# ## Applications
| Situation | Quantity Used |
|------------|----------------|
| Pitot tube (air speed) | $ p_{	ext{stagnation}} - p_{	ext{static}} = rac{1}{2}\rho v^2 $ |
| Venturi meter (flow rate) | $ Q = A_2 \sqrt{rac{2(p_1-p_2)}{\rho (1-(A_2/A_1)^2)}} $ |
| Aircraft lift (pressure difference) | $ L = (p_{	ext{lower}} - p_{	ext{upper}})A $ |

### Worked Example: Flow in a Converging Nozzle
Given: $ A_1 = 0.01 $ m², $ A_2 = 0.004 $ m², inlet pressure $ p_1 = 200 $ kPa, inlet velocity $ v_1 = 5 $ m/s,$ \rho = 1.225 $ kg/m³.

1. Continuity: $ v_2 = v_1 (A_1/A_2) = 5 	imes (0.01/0.004) = 12.5 $ m/s.
2. Bernoulli: $ p_2 = p_1 + rac{1}{2}\rho (v_1^2 - v_2^2) $

$ p_2 = 200\,	ext{kPa} + 0.5	imes1.225(5^2 - 12.5^2)pprox 200 - 94.9\,	ext{kPa} = 105.1\,	ext{kPa} $ $ **Dimensional check:**$ [p] = 	ext{N/m}^2 = 	ext{kg/(m·s}^2) $✓$

---

## 4. Navier‑Stokes Equation (Viscous Fluid)
The full momentum equation for a Newtonian fluid:

$ $ \rho\left(\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}
ight) = -\nabla p + \mu \nabla^2 \mathbf{v} + (\lambda + \mu)\nabla (\nabla\cdot \mathbf{v}) + \rho \mathbf{g} $$ -$ \mu $: dynamic viscosity (Pa·s)

- $ \lambda $: second viscosity coefficient (often $-2/3\mu $ for incompressible flow)

### Simplified Forms

- **Laminar, steady, incompressible, fully developed pipe flow** → **Poiseuille’s law**.

- **Stokes flow (low Reynolds)** →$ \nabla p = \mu \nabla^2 \mathbf{v} $.

---

## 5. Viscosity and Reynolds Number

### Dynamic Viscosity $ \mu $ Relates shear stress $ \tau $ to velocity gradient

$ $ \tau = \mu \frac{du}{dy} $ $$$

$ $

### Kinematic Viscosity $ \nu = \mu/\rho $### Reynolds Number (Inertial vs. Viscous forces
)

$ Re = \frac{\rho v L}{\mu} = \frac{v L}{\nu} $$$

- $ Re \ll 1 $: laminar (creeping) flow (Stokes regime)

- $ Re \gg 1 $: turbulent flow

---

## 6. Poiseuille’s Law (Laminar Flow in a Pipe)
For a circular pipe of radius $ R $ and length $  L $:

$ Q = \frac{\pi R^4}{8\mu}\frac{\Delta p}{L}v_{	ext{avg}} = rac{Q}{\pi R^2} = \frac{R^2}{8\mu}\frac{\Delta p}{L} $$$

# ## Example: Blood Flow in an Artery
- $ R = 3 $ mm, $  L = 0.1 $ m,$ \Delta p = 1333 $ Pa (10 mmHg),$ \mu = 3.5	imes10^{-3} $ Pa·s.
- $ Q = rac{\pi (0.003)^4}{8	imes 3.5	imes10^{-3}}rac{1333}{0.1} pprox 1.2	imes10^{-6} $ m³/s ≈ 1.2 mL/s.

---

## 7. Applications in Geophysics & Geodesy
| Phenomenon | Governing Equation |
|------------|--------------------|
| Ocean currents | Navier‑Stokes (with Coriolis term) |
| Atmospheric wind | Navier‑Stokes + hydrostatic balance |
| Groundwater flow | Darcy’s law (simplified Navier‑Stokes) |
| Weather modeling | Full primitive equations (mass, momentum, energy) |

---

## 8. Dimensional Analysis Example
Use Buckingham Pi theorem for a sphere falling in a viscous fluid (drag problem):

- Variables: $F_D $, $ ho $,$ \mu $,$  v $,$  D $ (diameter).

- Fundamental dimensions: $ M $, $  L $, $  T $.

- Pi groups: $ \Pi_1 = rac{F_D}{$
ho v^2 D^2} $ (drag coefficient),$ \Pi_2 = rac{
ho v D}{\mu} $ (Reynolds number).$

---

## 9. Key Equations Summary

| Equation | Name | Use |
|----------|------|-----|
| $ A_1 v_1 = A_2 v_2 $ | Continuity (incompressible) | Flow rate conservation |
| $ p + rac{1}{2}\rho v^2 +$
ho g h = const $ | Bernoulli | Energy balance in streamline |$
| $ \rho(\partial_t \mathbf{v} + (\mathbf{v}\cdot $
abla)\mathbf{v}) = -
abla p + \mu
abla^2\mathbf{v} +
ho\mathbf{g} $ | Navier‑Stokes | General fluid motion |$
| $ au = \mu rac{du}{dy} $ | Newtonian viscosity | Shear stress‑rate relation |
| $ Re = rac{$
ho v L}{\mu} $ | Reynolds number | Laminar vs turbulent classification |$
| $ Q = rac{\pi R^4}{8\mu}rac{\Delta p}{L} $ | Poiseuille’s law | Laminar pipe flow |

---

## Study Problems
1. Compute the pressure drop in a 5‑m long pipe of radius 2 cm carrying water ( $\mu=1.0	imes10^{-3} $ Pa·s) at a flow rate of 0.01 m³/s.
2. A sphere of radius 0.01 m falls through oil (
ho=900 kg/m³, \mu=0.2 Pa·s). Determine its terminal velocity using Stokes’ law.
3. For air at sea level ( $ ho=1.225 $ kg/m³,$ \mu=1.8	imes10^{-5} $ Pa·s) flowing over a wing chord $ L=0.2 $  m with $ v=30 $ m/s, calculate the Reynolds number.
4. Derive the drag coefficient $ C_D $ for a flat plate aligned perpendicular to flow using dimensional analysis.
5. Explain how Bernoulli’s principle underlies the operation of a Pitot‑static tube used in aviation.

---

## References

- OpenStax University Physics Vol. 2 (Ch. 8: Fluid Mechanics)

- Kundu & Cohen, "Fluid Mechanics"

- Batchelor, "An Introduction to Fluid Dynamics"

- MIT OCW 2.004: Fluid Mechanics

- Feynman Lectures Vol. I (Ch. 42) – Viscosity and Flow

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*
