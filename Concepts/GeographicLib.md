---
tags: [geodesy, concept, tool, aigis]
aliases: [GeographicLib, Karney, GeographicLib.jl, Library]
created: 2026-07-12
updated: 2026-07-27
---

# 🧮 GeographicLib

**GeographicLib** is a self-contained C++ library (with bindings for Python, MATLAB, Java, and Julia) developed by Charles Karney for high-accuracy geodetic computations. It is the modern gold standard for geodesic calculations and is used in GIS software, scientific computing, and precision geodesy.

## Core Algorithms

GeographicLib implements three key algorithms for computations on oblate ellipsoids:

| Algorithm | Problem | Accuracy | Class |
|-----------|---------|----------|-------|
| **Geodesic Inverse** | Two points → distance + azimuths | ~0.1 nm (1.57 m on ellipsoid of Earth's size) | Direct |
| **Geodesic Direct** | Point + distance + azimuth → destination point | ~0.1 nm | Direct |
| **Geodesic Line** | Compute intermediate points along a geodesic | ~0.1 nm | Intermediate |
| **Jacobian** | Sensitivity of geodesic to parameters | Full linearization | Utility |
| **Geodesic Intersection** | Two geodesics meeting at a point | ~0.1 nm | Intersection |

## Comparison with Vincenty

| Aspect | Vincenty | GeographicLib (Karney) |
|--------|----------|------------------------|
| **Accuracy** | ~0.5 mm (well-behaved cases) | ~0.1 nm (1.57 m in worst case) |
| **Convergence** | Fails for near-antipodal points | Converges everywhere |
| **Speed** | 2–4 iterations per call | 1–3 iterations, faster |
| **Near-antipodal** | Fails (infinite loop) | Works robustly |
| **Inverse azimuth** | May be ambiguous at ±180° | Handles correctly |
| **Line extraction** | Not available | Full geodesic line class |
| **Inverse area** | Not available | Included |
| **Available** | Hand-coded only | Well-documented library |

### When Vincenty Fails

Vincenty's iteration diverges for nearly antipodal points (separation ≈ 20,000 km). For any two points on Earth more than ~12,000 km apart, Vincenty may fail. GeographicLib uses a different iterative scheme (Clairaut's equation + Newton iteration) that converges everywhere.

## Usage Examples

### Python (geographiclib package)

```python
from geographiclib.geodesic import Geodesic

# WGS84 geodesic inverse problem
# Distance and azimuth from New York to London
result = Geodesic.WGS84.Inverse(40.7128, -74.0060, 51.5074, -0.1278)
print(f"Distance: {result['s12']:.3f} m")       # ≈ 5,570,226 m
print(f"Azimuth at NYC:  {result['azi1']:.6f}°") # ≈ 51.27° ENE
print(f"Azimuth at Lon:  {result['azi2']:.6f}°") # ≈ 110.16° ESE

# Geodesic direct problem (NYC + 1000km at 050°)
result2 = Geodesic.WGS84.Direct(40.7128, -74.0060, 50, 1000000)
print(f"Lat: {result2['lat2']:.6f}°, Lon: {result2['lon2']:.6f}°")

# Extract geodesic line for intermediate points
line = Geodesic.WGS84.Line(40.7128, -74.0060, 51.27)
# Position at 500 km along line
pos = line.Position(500000)
print(pos['lat2'], pos['lon2'], pos['s12'])
```

### C++

```cpp
#include <GeographicLib/Geodesic.hpp>
using namespace GeographicLib;

Geodesic geod(Constants::WGS84_a(), Constants::WGS84_f());
Geodesic::InverseResult r = geod.Inverse(phi1, lon1, phi2, lon2);
std::cout << "s12 = " << r.s12 << " m, a12 = " << r.a12 << " deg\n";
```

### MATLAB (geographiclib package)

```matlab
[s12, a12, a21] = geoddirect(WGS84_a, WGS84_f, phi1, lambda1, alpha1, s12);
[x, y, z] = geodtoecef(WGS84_a, WGS84_f, phi, lambda, h);
[e, n, u] = ecef_enau(WGS84_a, WGS84_f, phi0, lambda0, x, y, z);
```

## Accuracy Claims (from Karney, 2013)

| Computation | Accuracy |
|-------------|----------|
| Geodesic distance | ≤ 1.5 nm × (equatorial radius / Earth's equatorial radius) ≈ 0.5 mm on Earth |
| Geodesic area | ≤ 4 × 10⁻¹² as relative |
| Arc length (along geodesic) | Same as distance accuracy |
| Reduced length / geodesic scale | Consistent with distance |

The library guarantees that results are correct to floating-point precision (64-bit doubles) for the geodesic itself; no approximation error beyond machine epsilon.

## Additional Capabilities

Besides geodesics, GeographicLib includes:

| Component | Description |
|-----------|-------------|
| `GeodesicLine` | Parametric representation of a geodesic |
| `GeodesicPolygon` | Area and perimeter of geodesic polygons |
| `Geocentric` | ECEF coordinate conversions |
| `LocalCartesian` | ENU frame transformations |
| `NormalGravity` | Somigliana normal gravity formula |
| ` MagneticField` | IGRF magnetic field model |
| `SphericalHarmonic` | Gravity field via spherical harmonics |
| `TransverseMercator` | Accurate TM projection with high-order series |

## Integration with PROJ

PROJ 7+ uses GeographicLib's geodesic library internally, so any PROJ installation benefits from Karney's algorithms under the hood. Python's `pyproj` (≥2.0) also leverages this for all geodetic computations.

## References

- Karney, C. F. F. (2013). *Algorithms for geodesics*. Journal of Geodesy, **87**(1), 43–55. doi:10.1007/s00190-012-0578-z
- Karney, C. F. F. (2011). *GeographicLib: A versatile library for geographic calculations*. www.geographiclib.org
- Karney, C. F. F. (2023). *GeographicLib documentation*. https://geographiclib.sourceforge.io/

## Related
- [[Vincenty Formula]] · [[Geodetic Coordinates]] · [[Geocentric Cartesian ECEF]] · [[Local ENU NEU]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
