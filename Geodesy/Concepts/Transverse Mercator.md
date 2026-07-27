---
tags: [geodesy, concept, projection, aigis]
aliases: [Transverse Mercator, TM, Gauss-Krüger]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 Transverse Mercator

The **Transverse Mercator** (TM) projection is a conformal [[Map Projection]] that wraps an imaginary cylinder around the [[Reference Ellipsoid]] along a chosen **central meridian**. It preserves angles (conformal) and provides excellent accuracy within narrow north-south strips — making it the basis of [[UTM]] and Indonesia's **TM3°** national grid system.

## Mathematical Definition

The TM projection uses complex variables to map the ellipsoid surface to a plane.

### Complex Analytic Form (Redfearn)

Given geodetic coordinates $(\phi, \lambda)$on an ellipsoid with semimajor axis$a$, eccentricity $e$, and origin at $(\phi_0, \lambda_0)$:

**Complex quantity:**
$$

\zeta + i\,\eta = \omega_0 + k_0 \cdot (q + i\,\eta_q)$$where$\omega_0$is the complex coordinate at the origin,$q = \sinh^{-1}(\tan\phi)$is the isometric latitude, and$k_0$is the scale factor at the central meridian.

### Standard TM Formulas (Snyder)

For geodetic coordinates$(\phi, \lambda)$:

**Step 1:** Compute the quantities:
$$a = \frac{a(1-e^2)}{(1-e^2\sin^2\phi)^{1/2}} \quad \text{(meridional radius of curvature — not semimajor axis)}$$

$$N = \frac{a}{(1-e^2\sin^2\phi)^{1/2}} \quad \text{(prime vertical radius of curvature)}$$

$$t = \tan\phi, \quad c = \frac{e^2 N \cos^2\phi}{a(1-e^2)}$$

$$l = \lambda - \lambda_0 \quad \text{(longitude difference from CM, in radians)}$$

**Step 2:** Compute northing ($N_{\text{UTM}}$):
$$\kappa = k_0\left[N\cos\phi \cdot l + \frac{N\cos^3\phi}{6}\left(1 - t^2 + c + 9\frac{e^2 N^2 \cos^4\phi}{a^2}\right)l^3 + \cdots\right]$$

**Step 3:** Compute northing ($N_{\text{UTM}}$):
$$

N_{\text{UTM}} = N_0 + k_0\left[\tilde{M} - \tilde{M}_0 + N \cos\phi \tan\phi \cdot l^2/2 + \cdots\right]$$where$\tilde{M}$is the **meridian arc length** from equator to latitude$\phi$:
$$

\tilde{M} = a\int_0^\phi \frac{(1-e^2)\,d\phi}{(1-e^2\sin^2\phi)^{3/2}}$$The full series expansion includes terms up to$l^6$.

## Scale Factor

The **TM scale factor** $k$at any point$(\phi, \lambda)$is:$$k = k_0 \left(1 + \frac{l^2}{2}\cos^2\phi(1 + \frac{e^2}{1-e^2}\sin^2\phi + c + \frac{l^2}{12}\cos^2\phi \cdots) \right)$$| Condition |$k$ | Result |
|-----------|-----|--------|
| At the central meridian ($l = 0$) | $k = k_0$ | Scale equals scale factor |
| At standard parallel ($\pm l_0$) | $k = 1$| True scale on the ground |
| At zone edges |$k > 1$| Scale distortion (small for narrow zones) |

### Standard Scale Factors

| System |$k_0$ | True-Scale Lines | Max Distortion at ±3° |
|--------|-------|------------------|-----------------------|
| **UTM** (6° zones) | 0.9996 | ±180 km from CM | +0.040% |
| **TM3°** (Indonesia) | 0.9995 | ±370 km from CM | +0.016% |
| **Gauss-Krüger** | 1.0 | At the CM (zero distortion) | +0.135% at ±3° |
| **State Plane TM** | 0.9996 | Varies | ≤ +0.04% |

## Convergence Angle

The angle between the grid north ($Y$-axis) and true (geodetic) north is the **grid convergence** $\gamma$:
$$

\gamma \approx l \cdot \sin\phi$$This is the fundamental geometric relationship of TM projections: grid lines and meridians converge as you move away from the central meridian.

| Distance from CM |$\gamma$at 45°N |$\gamma$at equator |
|------------------|------------------|---------------------|
| ±0.5° | 0.35° | 0 |
| ±1.0° | 0.71° | 0 |
| ±1.5° | 1.06° | 0 |
| ±3.0° (UTM edge) | 2.12° | 0 |

## Indonesia's TM3° System

Indonesia uses the **TM3°** (Transverse Mercator 3-degree) system as its primary cadastral/mapping projection:

| Property | Value |
|----------|-------|
| Zone width | 3° longitude |
| Central meridian | 102°, 105°, 108°, 111°, 114°, 117°, 120°, 123°, 126°, 129°, 132°, 135° |
|$k_0$| 0.9995 |
| False easting | 500,000 m |
| False northing | 0 m (N) / 10,000,000 m (S) |
| EPSG | 23833–23842 (N), 23933–23942 (S) |

## Comparison: TM vs. UTM

| Feature | TM3° (Indonesia) | UTM (6° zones) |
|---------|-------------------|----------------|
| Zone width | 3° | 6° |
| Max distortion | 0.016% | 0.040% |
| Number of zones (120°E–141°E) | 7 zones | 4 zones |
| Scale factor$k_0$| 0.9995 | 0.9996 |
| Convergence at edge | 1.05° | 2.12° |

The 3° strips provide **better accuracy** (lower distortion) but require **more zones** to cover Indonesia's extent.

## Worked Example

**Problem:** In UTM Zone 33N, what is the convergence angle at a point 1.5° east of the central meridian and latitude 45°N?

**Solution:**$$\gamma = l \cdot \sin\phi = 1.5^\circ \times \sin(45^\circ) = 1.5^\circ \times 0.7071 = 1.06^\circ = 1^\circ 3' 36''
$$

**Interpretation:** The UTM grid lines at this point are rotated 1° 4′ east of true north. Surveyors must apply this convergence when converting compass bearings to grid azimuths.

## References

- Snyder, J. P. (1987). *Map Projections — A Working Manual*. USGS PP 1395, Chapter 2.

- Karney, C. F. F. (2011). *Transverse Mercator with an accuracy of a few nanometers*. J. Geodesy, 85(8), 475–483.

- BIG (Indonesia). *Standard Koordinat Indonesia*. Peraturan BPN No. 3/2009.

## Related

- [[Map Projection]] · [[UTM]] · [[Projected Coordinates]] · [[Map Projection]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Kurikulum Teknik Geodesi]]
