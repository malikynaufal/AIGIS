---
tags: [aigis, concept, physics, atmospheric-physics, weather, refraction]
created: 2026-07-27
updated: 2026-07-27
---

# Atmospheric Physics

## Atmosphere Layers, Radiation Budget, Weather, and Atmospheric Refraction for Geodesy

**Core Idea:** The atmosphere is a dynamic, stratified fluid that influences everything from local weather to satellite-based positioning systems. Understanding its structure, thermodynamics, and electromagnetic properties is essential for geodesy, satellite navigation, and high-precision surveying.

---

## 1. Structure of the Atmosphere

### Layering by Temperature Gradient
| Layer | Altitude (km) | Temperature Profile (°C) | Key Characteristics |
|-------|---------------|--------------------------|---------------------|
| **Troposphere** | 0–12 (sea level to 11 km) | Gradient decreases with height (average -6.5°C/km) | Weather, holds most mass, contains most water vapor |
| **Tropopause** | 11 km | Isothermal approx -60°C | Boundary layer |
| **Stratosphere** | 12–50 km | Temperature increases from -60°C to +20°C | Ozone layer absorbs UV, stable, airglow |
| **Stratopause** | ~47 km | Peak ~0°C | Level of max heating |
| **Mesosphere** | 50–85 km | Temperature decreases to -90°C | Midnight airglow, noctilucent clouds |
| **Mesopause** | ~85 km | ~ -90°C | Lowest temperature |
| **Thermosphere** | 85–600 km+ | Temperature increases to 1500°C (day) / -150°C (night) | Ionosphere forms, satellites orbit, aurora |
| **Exosphere** | >600 km | Gradual transition | Escape region, cometary tails |

### Density and Pressure Profiles

- **Surface density:** $ \rho_0 \approx 1.225 $ kg/m³, decreasing roughly exponentially with scale height $ H \approx 8.5 $ km $ $ \rho(z) = \rho_0 \exp(-z/H)

$$

**Pressure:**$ P(z) \approx P_0 \exp(-z/H) $ with $ P_0 = 101,325 $ Pa.

### Major Constituents (dry air)
| Gas | Volume % | Mol. Mass (g/mol) | Role |
|-----|----------|-------------------|------|
| N₂ | 78.08 | 28.013 | Main component, inert |
| O₂ | 20.95 | 31.998 | Respiration, combustion |
| Ar | 0.93 | 39.948 | Inert tracer, geodesy |
| CO₂ | 0.04 | 44.010 | Greenhouse gas |
| Ne, He, CH₄, Kr, H₂O | trace | variable | Various effects |

### Vertical Motion and Stability
**Hydrostatic balance:**$ \frac{dP}{dz} = -\rho g $**Stability criterion:** Brunt-Väisälä frequency $ N^2 = -\frac{g}{\theta}\frac{d\theta}{dz} $- $ N > 0 $: stable stratification (most of troposphere)

- $ N < 0 $: unstable (cumulus convection)

---

## 2. Radiation Budget and Energy Balance

### Solar Radiation Arrival

- **Solar constant:** $ S_0 \approx 1361 $ W/m² at 1 AU

- **Planetary albedo:**$ \alpha \approx 0.30 $ (reflected back to space)

- **Net absorbed:** $ S_{\text{abs}} = (1-\alpha) S_0 / 4 = 239 $ W/m² (averaged over Earth surface)

### Greenhouse Effect
**Idealized energy balance model (zero-dimensional):*
*

$ $ \frac{S_0(1-\alpha)}{4} = (1 - \varepsilon_{\text{atm}})\sigma T_s^4 + \varepsilon_{\text{atm}}\sigma T_e^4

$$

where:
- $ T_e = \left[\frac{S_0(1-\alpha)}{4\sigma}\right]^{1/4} = 255 $ K (equilibrium temperature without greenhouse)
-$ \varepsilon_{\text{atm}} $= atmospheric emissivity (total infrared absorptivity)
- $ T_s $ = surface temperature (≈ 288 K)
-$ \sigma $ = Stefan-Boltzmann constant ($ 5.67 \times 10^{-8} $ W/m²·K⁴)

### Energy Transport Mechanisms

- **Conduction:** negligible above top few meters

- **Convection:** dominant in troposphere, transport moisture and latent heat

- **Radiation:** dominates above tropopause, both shortwave (solar) and longwave (IR)

- **Latent heat:** energy released/absorbed by phase changes of water

### Water Vapor Feedback

- Warmer air holds more water vapor: $ e_{\text{sat}} \propto \exp(Lv/(RT)) $- H₂O is a strong greenhouse gas (its concentration varies regionally and seasonally)

- **Positive feedback:** warming → more water vapor → stronger greenhouse → more warming

---

## 3. Weather and Climate

### Atmospheric Circulation (General Circulation)

- **Hadley cell (tropics):** rising warm air at equator, sinking at ~30°N/S (deserts)

- **Ferrel cell (mid-latitudes):** cyclonic flow (low pressure), anti-cyclonic flow (high pressure)

- **Polar cell (poles):** sinking cold air, poleward flow at surface

### Jet Streams

- **Polar front jet:** ~10 km altitude, strong vertical shear, speed ~100 m/s

- **Subtropical jet:** ~12–16 km, speed ~60 m/s (Northern Hemisphere dominated)

### Weather Systems

- **Mid-latitude cyclones:** develop along polar front, frontal boundaries, strong winds

- **Tropical cyclones:** low pressure, warm core, release of latent heat in eyewall

- **Monsoons:** seasonal reversal of wind direction induced by land-sea temperature contrast

### Scale Classifications
| Scale | Horizontal | Vertical | Typical Features |
|-------|------------|----------|------------------|
| Planetary | ~1000–10,000 km | >10 km | Climate patterns, jet streams |
| Synoptic | 100–1000 km | 1–10 km | Mid-latitude weather systems |
| Mesoscale | 1–100 km | <1 km | Thunderstorms, sea breezes, orographic effects |
| Microscale | <1 km | <1 km | Turbulence, wakes, thermal plumes |

---

## 4. Atmospheric Refraction for Geodesy and GNSS

### Refractive Index in the Atmosphere
**Saar and Gordon model (density-dependent refractive index):*
*

$ n = 1 + \frac{577(n_e - 0.8)}{720 + (0.45 T)^2 - 0.0046 (T - 15)^2 \cdot 10^{-3}} $$$

where:
-$ T $ = temperature (°C) at height $ z $- $ n_e $ = number of electrons along line of sight (slant total electron content, STEC)

- Effect is small: $ n \approx 1.0003 $ at sea level

### Speed of Light in Air (C-weighted
)

$ c_w = \frac{c_0}{n(T, N)} $ with $ n(T, N) = 1 + 776.7 \times 10^{-8} \frac{N}{T + 273.15} $ (approx.)

### Refractive Angle (Refraction Solutions)
**Refraction angle $ \delta $** in geometrical astronomy:

$ $ \delta = h \cdot \frac{(n-1)\tan h}{1 - (n-1)\sin h}, \quad h = \text{true altitude} $$

For near-horizontal rays ($ h < 10°$):

$ $ \delta \approx \frac{(n-1)\sec h}{(1 - (n-1)\sin h)^2
}

**Alternative strong-form approximation:**

 \delta = \frac{1}{1.00024} \left( \frac{\tan h}{1 + \frac{h^2}{2} \cdot \frac{d\ln n}{dz}} \right)

$$

### Refraction for Earth’s Surface
When propagating nadir to a point on Earth from satellite:
**Geodetic refraction** accounts for slow arrival time and path curvature:

- **Zenith delay (dry):** ~2.8 m (tropospheric)

- **Zenith delay (wet):** ~0.1–0.3 m (water vapor)

- **Zenith delay (combined):** ~3.0–3.5 m

**Mapping function (elevation-dependent):*
*

$ $ M(e) = \frac{1}{\cos z} \approx \frac{1}{\sin e} \cdot (1 + \frac{0.0026}{\sin e}) $$

for tropospheric total delay: $ \Delta T = M(e) \times ZT $

### Applications in Geodesy

- **GNSS positioning:** Refraction affects range measurements, especially at low elevation angles

- **Satellite surveying:** Need elevation-dependent corrections to sub-cm accuracy

- **IAS (International Altitude System):** Modeled via hydrostatic/excess hydrostatic delay components

- **Chond level:** Determination of tide gauge zero (water level extremes) uses precise atmospheric modeling

### Temperature Inversion Effects
**Inversion layers** can reverse normal lapse rate, causing strong refraction:

- Mirage effects (superior/inferior) for visible light

- Downward bending (inversion) can create **false horizon** for surveying line-of-sight

- Detection via temperature profiles or radiosonde data

---

## 5. Atmospheric Tides and Gravity Waves

### Solar-Tidal (Semidiurnal) and Lunar-Tidal Effects

- ** $ M_2 $ (principal lunar semidiurnal):** dominant in troposphere (~50 hPa)

- ** $ S_2 $ (solar semidiurnal):** also significant

- ** $ K_1 $ (diurnal):** important in stratosphere

### Gravity Wave Spectrum

- Generated by convection, mountain waves, jet stream shear, fronts

- Scales: horizontal 10–1000 km, vertical ~2–10 km

- Momentum flux to stratopause can alter circulation patterns

- Critical for upper atmosphere coupling and climate model accuracy

---

## Key Formulas

| Formula | Name | Use |
|---------|------|-----|
| $ n = 1 + \frac{577(n_e - 0.8)}{720 + (0.45 T)^2 - 0.0046 ...} $ | Refractive index | Atmosphere EM propagation |
| $ \delta = h \frac{(n-1)\tan h}{1 - (n-1)\sin h} $ | Refraction angle | Astronomical line of sight |
| $ M(e) = \frac{1}{\cos z} (1 + \frac{0.0026}{\sin e}) $ | Tropospheric mapping function | GNSS vertical delay |
| $ N^2 = -\frac{g}{\theta}\frac{d\theta}{dz} $ | Brunt-Väisälä frequency | Static stability |
| $ \Gamma_d = -g/c_p \approx -9.8 $ K/km | Dry adiabatic lapse rate | Stability |
| $ e_{\text{sat}} \propto \exp(Lv/(RT)) $ | Clausius-Clapeyron | Saturation vapor pressure |

---

## Problems
1. Derive the refractive index for standard atmosphere at sea level using temperature and density dependencies.
2. Explain why refraction at low elevation angles affects GNSS positioning more than at zenith.
3. Describe the physics of temperature inversions and how they create mirages. Provide examples (Fata Morgana).
4. How does water vapor content influence the atmospheric refractive index and total delay in GNSS measurements?
5. Derive the dry and wet components of tropospheric delay and explain their dependence on temperature and pressure.
6. Explain why the tropopause is a natural boundary for atmospheric stability and static temperature.
7. How does the hydrostatic equation combine with temperature to determine pressure and density profiles in the troposphere?

---

*Concept maintained by AIGIS — part of [[Physics MOC]]*