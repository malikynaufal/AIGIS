---
tags: [geodesy, concept, computation, aigis]
aliases: [Vincenty, Vincenty Formula, Vincenty Inverse, Vincenty Direct, Geodesic]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 Vincenty's Formulae

**Vincenty's formulae** are an iterative algorithm for computing the **geodesic** (shortest path on the [[Reference Ellipsoid]]) — both the **inverse problem** (two points → distance + azimuths) and the **direct problem** (point + azimuth + distance → destination point). Accurate to millimeters for separations up to several thousand kilometers.

## Why Geodesics Matter

On a sphere, the shortest path between two points is a great circle arc. On an ellipsoid, the shortest path is a **geodesic** — it does not lie on a great circle of the circumscribing sphere. The difference is small but measurable:

| Separation | Great Circle vs. Geodesic Difference |
|------------|---------------------------------------|
| 100 km | < 1 mm |
| 1000 km | ~10 cm |
| 10,000 km | ~1–2 km (up to 2 km) |
| 20,000 km (antipodal) | May fail for Vincenty |

## Inverse Problem: Two Points → Distance and Azimuths

### Input

- Two geodetic positions: $(\phi_1, \lambda_1)$and$(\phi_2, \lambda_2)$### Output

- **Geodesic distance**$s$(meters)

- **Forward azimuth**$\alpha_1$(at point 1)

- **Back azimuth**$\alpha_2$(at point 2)

- **Geodesic area** (for full ellipse)

### Algorithm (1975)

**Step 1:** Reduced latitudes:$$u_1 = \arctan\left((1-f)\tan\phi_1\right), \quad u_2 = \arctan\left((1-f)\tan\phi_2\right)$$**Step 2:** Iterate to find the angular separation$L$and azimuths:

Initialize:$\lambda = L_{12} = \lambda_2 - \lambda_1$Repeat until convergence:$$\sin\alpha_1 = \frac{\cos u_2 \sin\lambda}{\sqrt{(\cos u_1 \sin u_2 - \sin u_1 \cos u_2 \cos\lambda)^2}}
$$

$$\cos\alpha_1 = \sin u_1 \sin u_2 + \cos u_1 \cos u_2 \cos\lambda$$

$$\sin\sigma = \sqrt{(\cos u_2 \sin\lambda)^2 + (\cos u_1 \sin u_2 - \sin u_1 \cos u_2 \cos\lambda)^2}$$

$$\cos\sigma = \sin u_1 \sin u_2 + \cos u_1 \cos u_2 \cos\lambda$$

$$\sigma = \arctan\left(\frac{\sin\sigma}{\cos\sigma}\right)$$

$$\sin\alpha = \frac{\cos u_1 \cos u_2 \sin\lambda}{\sin\sigma}$$

$$\cos 2\alpha = 1 - \sin^2\alpha$$

$$C = \frac{f}{16}\cos^2\alpha\left[4 + f(4 - 3\cos^2\alpha)\right]$$

$$
\lambda_{k+1} = L_{12} + (1 - C)\sin\alpha \left[\sigma + C\sin\sigma(\cos 2\alpha_m + C\cos\sigma \cdot (-1 + 2\cos^2(\sigma + C)))\right]$$Converges in 2–3 iterations.

**Step 3:** Compute distance:$$u^2 = \cos^2\alpha\cdot\frac{a^2 - b^2}{b^2}
$$

$$A = 1 + \frac{u^2}{16384}\left(4096 + u^2\left(-768 + u^2\left(320 - 175u^2\right)\right)\right)$$

$$B = \frac{u^2}{1024}\left(256 + u^2\left(-128 + u^2\left(74 - 47u^2\right)\right)\right)$$

$$
s = b\cdot A\left(\sigma - B\sin\sigma\left(\cos 2\alpha_m + B/4\left(\cos\sigma\left(-1 + 2\cos^2\sigma\right) - B/6\cdot\cos\sigma\left(-3 + 4\sin^2\sigma\right)\left(-3 + 4\cos^2\sigma\right)\right)\right)\right)$$## Direct Problem: Point + Azimuth + Distance → Destination Point

### Input

- Start position:$(\phi_1, \lambda_1)$- Forward azimuth:$\alpha_1$- Geodesic distance:$s$### Output

- Destination position:$(\phi_2, \lambda_2)$- Back azimuth:$\alpha_2$### Algorithm (1975)

**Step 1:** Reduced latitude$u_1 = \arctan((1-f)\tan\phi_1)$**Step 2:** Compute angular separation$\sigma$:
$$

\sigma = s / (b\cdot A)$$**Step 3:** Iterate to find$\phi_2$, $\alpha_2$:
$$\sin\alpha_1 = \frac{\sin u_1}{\cos u_1} \cdot \frac{1}{A}$$

$$
\sin\alpha = \cos u_1 \sin\alpha_1$$Then compute the destination using the inverse formulas with$\sigma$ as input.

## Accuracy Comparison

| Algorithm | Accuracy (10,000 km) | Speed | Antipodal |
|-----------|---------------------|-------|-----------|
| **Vincenty** | 0.5 mm | Fast (2–4 iters) | ❌ Fails |
| **Karney (GeographicLib)** | 15 nm (0.015 mm) | Moderate (1–3 iters) | ✅ Works |
| **Bowring (1981)** | 0.01 m | Very fast | Limited |
| **Andoyer (1932)** | 0.05 m | Very fast | Limited |

## When Vincenty Fails

Vincenty's inverse iteration diverges when:
1. The two points are **nearly antipodal** (separation ≈ 20,000 km)
2. One or both points are near a **pole**
3. The iteration oscillates and does not converge within the tolerance

**Workaround:** Use [[GeographicLib]] (Karney's algorithm), which handles all cases robustly.

## Worked Example: Inverse Problem

**Problem:** Compute the geodesic distance between New York ($\phi_1 = 40.7128^\circ\text{N}$, $\lambda_1 = -74.006^\circ\text{W}$) and London ($\phi_2 = 51.5074^\circ\text{N}$, $\lambda_2 = -0.1278^\circ\text{W}$) on WGS84.

**Solution:**

Using the Vincenty inverse formula (computed numerically):

| Parameter | Value |
|-----------|-------|
| $s$(geodesic distance) | 5,570,226 m (5570.2 km) |
|$\alpha_1$(forward azimuth from NYC) | 51.270° (ENE) |
|$\alpha_2$ (back azimuth at London) | 110.168° (ESE) |

## Practical Applications

| Application | Use of Geodesics |
|-------------|------------------|
| **Aviation** (great circle routes) | Compute great-circle flight distances |
| **Telecommunications** | Signal path distances for time synchronization |
| **Land surveying** | Precise distances between distant CORS stations |
| **Boundary definitions** | Legal boundaries often reference geodesic lines |
| **Shipping** | Distance calculations for maritime routes |
| **GeographicLib** | The modern standard; used in [[UTM]] conversion, GIS software |

## MATLAB/Python Implementation Notes

Most geodetic software packages include Vincenty:

- **Python:** `pyproj.Geod().inv()` (uses Karney under the hood)

- **MATLAB:** `vincentyv` (Statistics and Machine Learning Toolbox)

- **C++:** Hand-coded or via [[GeographicLib]]

## References

- Vincenty, T. (1975). *Direct and inverse solutions of geodesics on the ellipsoid*. Bulletin Géodésique, 49, 89-103.

- Bowring, B. R. (1981). *The accuracy of geodetic latitude and height equations*. Survey Review.

- Karney, C. F. F. (2013). *Algorithms for geodesics*. Journal of Geodesy, 87(1), 43-55.

## Related

- [[Reference Ellipsoid]] · [[Geodetic Coordinates]] · [[GeographicLib]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
