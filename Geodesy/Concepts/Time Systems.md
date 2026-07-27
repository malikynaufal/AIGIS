---
tags: [aigis, concept, geodesy, time-systems, astronomical-time]
aliases: [Time Systems]
created: 2026-07-27
---

# Time Systems

**Core Idea:** Precise timekeeping is essential for GNSS (positioning = timing) and geodetic astronomy. Different time scales account for Earth's irregular rotation.

## Time Scales

| Scale | Based on | Precision | Use |
|-------|----------|-----------|-----|
| **UTC** | Atomic seconds + leap seconds | 1 s | Civil time |
| **UT1** | Earth's rotation angle | ~1 ms | Earth orientation |
| **TAI** | Atomic clocks (no leap seconds) | 1 ns | Scientific reference |
| **GPS Time** | TAI - 19 s (no leap seconds) | 1 ns | GNSS processing |
| **GLONASS Time** | UTC (includes leap seconds) | 1 μs | GLONASS processing |
| **Sidereal Time** | Earth's rotation relative to stars | ~1 ms | Star observations |
| **Julian Date** | Continuous count since 4713 BC | 1 day | Astronomy |
| **Modified JD** | JD - 2400000.5 | 1 day | Convenient short form |

## Key Conversions
$$\text{GPS Time} = \text{TAI} - 19\ \text{seconds}$$

$$\text{UT1} = \text{UTC} + \Delta\text{UT1}$$

$$
\text{LST} = \text{UT1} + \lambda_{\text{east}}/15° + \text{Greenwich Hour Angle}$$## In GNSS

- **GPS time** is continuous (no leap seconds)

- **Satellite clocks** referenced to GPS time

- **Receiver clocks** biased from GPS time → clock offset is a 4th unknown

- **Relativistic correction:**$\Delta t_{rel} = -\frac{2\sqrt{GM \cdot a}}{c^2} \cdot e \sin E$

## Related

- [[Celestial Coordinates]] — Star positions depend on time

- [[Precession and Nutation]] — Time-dependent corrections

- [[GNSS]] — Positioning via timing

---
*Part of [[Geodesy MOC]]*