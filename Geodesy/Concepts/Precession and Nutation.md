---
tags: [aigis, concept, geodesy, astronomy, earth-orientation, reference-frames]
created: 2026-07-27
updated: 2026-07-27
---

# Precession & Nutation

## For Geodesy & Earth Orientation

**Core Idea:** Precession is the slow, long-period rotation of Earth's spin axis (~26,000 year cycle), while nutation is a shorter-period oscillation (~18.6 years dominant). Both must be modeled for accurate reference frame transformations and precise GNSS/GNSS processing.

---

## Fundamental Concepts

### Precession

**General precession:** The spin axis slowly traces a cone due to Sun/Moon torques on Earth's equatorial bulge.
$$

\dot{\psi} \approx 50.26''/\text{yr} \quad \text{(general precession in longitude)}$$- Cycle period: ~25,772 years

- Main contributors: Sun and Moon gravitational pull on equatorial bulge

**Precession matrix (IERS 2010):**$$P = R_1(-\varepsilon_A) \cdot R_3(-\psi_A) \cdot R_1(\varepsilon_0)$$### Nutation

The dominant nutation period is 18.6 years (regression of the lunar nodes).

| Component | Period | Amplitude |
|-----------|--------|-----------|
| Nutation in longitude | 18.6 years | 9.20'' |
| Nutation in obliquity | 18.6 years | 6.86'' |
| Diurnal (Prograde) | 1 sidereal day | ~0.01'' |

**MHB2000 nutation model** (IERS): ~1000 periodic terms.

### Polar Motion

**Chandler wobble:** ~14-month period oscillation of the rotation pole
**Annual wobble:** 12-month period from atmospheric/hydrologic loading
**Secular drift:** ~3.5 cm/yr toward 80°W longitude

---

## In Geodesy Context

### Why it matters

1. **Precise positioning:** Pole position affects ECEF ↔ ECI conversion
2. **Tidal gravity:** Nutation affects gravitational reference
3. **GNSS:** Station coordinates are defined in ECEF, but processing may use ECI

### Earth Orientation Parameters (EOP)

From IERS:

| Parameter | Symbol | Unit | Resolution |
|-----------|--------|------|------------|
| Polar motion |$x_p, y_p$| arcseconds | Daily |
| UT1-UTC |$\Delta UT1$| seconds | Daily |
| Nutation offsets |$\Delta\psi, \Delta\varepsilon$| milliarcseconds | Daily |

---

## Key Equations

| Equation | Name | Use |
|----------|------|-----|
|$\mathbf{r}_{ECI} = P \cdot N \cdot R \cdot \mathbf{r}_{ECEF}$| ECEF to ECI | Reference frame transform |
|$\dot{\psi} = 50.26''/$yr | Precession | Long-term rotation |
| $\Delta\varepsilon_{18.6} = 9.20''$ | Nutation amplitude | Short-term oscillation |

---

## Related Concepts

- [[ITRF]] — International Terrestrial Reference Frame

- [[Precession and Nutation]] — Earth Orientation Parameters

- [[Geodetic Coordinates]] — ECEF coordinates affected by pole

- [[IERS]] — Publishes precession/nutation models

---

*Concept maintained by AIGIS — part of [[Geodesy MOC]]*