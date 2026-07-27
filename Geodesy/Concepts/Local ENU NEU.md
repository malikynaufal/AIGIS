---
tags: [geodesy, concept, coordinate-system, aigis]
aliases: [Local ENU, Local NEU, East-North-Up, Local Tangent Plane, ENU, NEU]
created: 2026-07-12
updated: 2026-07-27
---

# 🧭 Local ENU / NEU

A **local tangent frame** (East-North-Up or North-East-Up) is a Cartesian coordinate system anchored at a chosen origin point on the Earth's surface. It is commonly used in surveying, [[GNSS]] baseline processing, engineering construction, and any application where planar math (distances, angles) is convenient in a small region.

## Definitions

### ENU (East-North-Up)

| Axis | Direction | Symbol |
|------|-----------|--------|
| **E** | East (tangent to the parallel) | $e$ |
| **N** | North (tangent to the meridian) | $n$ |
| **U** | Up (outward along ellipsoidal normal) | $u$ |

### NEU (North-East-Up)

Same as ENU but with N and E axes swapped. Used in some surveying software.

## Why It Matters

- **Flattens a small region** so you can do planar distance and angle computations without ellipsoid curvature effects.

- **Baseline vectors** from GNSS RTK / network adjustments are usually expressed in ENU (e.g.,$dE$, $dN$, $dU$).

- **Engineering surveys** and stake-out use ENU directly.

- **Topographic corrections** (e.g., slope distance to horizontal) are simple in ENU.

## Rotation Matrix: Geodetic → ENU

Given the origin $(\phi_0, \lambda_0, h_0) $on the ellipsoid, convert a point's ECEF coordinates to a vector in the ENU frame:

**Step 1:** Compute the ECEF displacement vector from the origin
:

$$\Delta\mathbf{X} = \mathbf{X}_P - \mathbf{X}_0$$

**Step 2:** Apply the rotation matrix
:

$$\begin{pmatrix} E \\ N \\ U \end{pmatrix} = \mathbf{R}(\phi_0, \lambda_0) \cdot \Delta\mathbf{X} $$

where:$$\mathbf{R}(\phi_0, \lambda_0) = \begin{pmatrix}
-\sin\lambda_0 & \cos\lambda_0 & 0 \\
-\sin\phi_0\cos\lambda_0 & -\sin\phi_0\sin\lambda_0 & \cos\phi_0 \\
\cos\phi_0\cos\lambda_0 & \cos\phi_0\sin\lambda_0 & \sin\phi_0
\end{pmatrix} $$### Row-by-row interpretation

- **E (row 1):** Project $\Delta\mathbf{X} $onto the local east direction (perpendicular to meridian in the tangent plane).

- **N (row 2):** Project onto the local north direction (tangent to meridian).

- **U (row 3):** Project along the ellipsoidal normal.

## Inverse: ENU → ECE
F

$$\begin{pmatrix} dX \\ dY \\ dZ \end{pmatrix} = \mathbf{R}^T(\phi_0, \lambda_0) \cdot \begin{pmatrix} E \\ N \\ U \end{pmatrix} $$

Since rotation matrices are orthogonal:$\mathbf{R}^{-1} = \mathbf{R}^T$.

## Worked Example

**Problem:** A rover at WGS84 coordinates $(\phi, \lambda, h) = (40.0^\circ\text{N}, -105.0^\circ\text{W}, 1500.0\ \text{m}) $is referenced to a base station at$(\phi_0, \lambda_0, h_0) = (40.0^\circ\text{N}, -105.0^\circ\text{W}, 1000.0\ \text{m})$. Compute the ENU vector of the rover relative to the base.

**Solution:**

1. Compute ECEF for both points (using the [[Geocentric Cartesian ECEF]] forward formulas):

**Base station ($h = 1000 $m):**
-$N_0 = a / \sqrt{1 - e^2\sin^2\phi} = 6378137 / \sqrt{1 - 0.00669438 \times 0.4131759} = 6386993.8 $m
-$X_0 = (6386993.8 + 1000) \times \cos40^\circ \times \cos(-105^\circ) = -1265973.8 $m
-$Y_0 = (6386993.8 + 1000) \times 0.7660444 \times \sin(-105^\circ) = -4725276.4 $m
-$Z_0 = (6386993.8 \times 0.99330562 + 1000) \times 0.6427876 = 4076485.7$ m

**Rover ($h = 1500 $m):**
-$N = 6386993.8 $m (same latitude, same $N$)

- $X = (6386993.8 + 1500) \times \cos40^\circ \times \cos(-105^\circ) = -1265806.4 $m
-$Y = (6386993.8 + 1500) \times 0.7660444 \times \sin(-105^\circ) = -4725078.0 $m
-$Z = (6386993.8 \times 0.99330562 + 1500) \times 0.6427876 = 4076657.6 $m

2. Compute the displacement:

$$\Delta X = -1265806.4 - (-1265973.8) = 167.4\ \text{m}\Delta Y = -4725078.0 - (-4725276.4) = 198.4\ \text{m}\Delta Z = 4076657.6 - 4076485.7 = 171.9\ \text{m} $$3. Apply rotation:

With $\phi_0 = 40.0^\circ = 0.6981317 $rad,$\lambda_0 = -105^\circ = -1.8325957 $rad:

$$\sin\phi_0 = 0.6427876, \cos\phi_0 = 0.7660444\sin\lambda_0 = -0.9659258, \cos\lambda_0 = -0.2588190E = -(\sin\lambda_0)(\Delta X) + (\cos\lambda_0)(\Delta Y)E = -(-0.965926)(167.4) + (-0.258819)(198.4)E = 161.7 - 51.4 = 110.3\ \text{m}N = -(\sin\phi_0\cos\lambda_0)(\Delta X) - (\sin\phi_0\sin\lambda_0)(\Delta Y) + (\cos\phi_0)(\Delta Z)N = -(0.642788 \times -0.258819)(167.4) - (0.642788 \times -0.965926)(198.4) + (0.766044)(171.9)N = -(-0.1664)(167.4) - (-0.6210)(198.4) + 131.6N = 27.9 + 123.2 + 131.6 = 282.7\ \text{m}U = (\cos\phi_0\cos\lambda_0)(\Delta X) + (\cos\phi_0\sin\lambda_0)(\Delta Y) + (\sin\phi_0)(\Delta Z)U = (0.766044 \times -0.258819)(167.4) + (0.766044 \times -0.965926)(198.4) + (0.642788)(171.9)U = -0.1983(167.4) - 0.7399(198.4) + 110.5U = -33.2 - 146.8 + 110.5 = -69.5\ \text{m} $$**Result:** The rover is at$(E, N, U) = (110.3\ \text{m East}, 282.7\ \text{m North}, -69.5\ \text{m Up})$ relative to the base. The negative Up value indicates the rover is 69.5 m lower in ellipsoidal height than the base, consistent with our assumption.

## Applications in GNSS Processing

| Application | Use of ENU |
|-------------|------------|
| **RTK baseline** | Base → Rover vector in ENU ($dE,dN,dU$) |
| **Network adjustment** | Enu difference between CORS stations |
| **Precision agriculture** | Vehicle guidance in ENU |
| **Deformation monitoring** | Time series of ENU offsets |
| **Airport approach** | Flight deck guidance with NEU |
| **Engineering stakeout** | Construction points relative to origin |

## Accuracy and Deformation

Over long baselines (> 1–10 km), the tangent plane approximation introduces curvature error:

| Baseline Length | Curvature Error (ENU approximation vs geodesic) |
|-----------------|-------------------------------------------------|
| 1 km | < 0.1″ (negligible) |
| 10 km | ~ 0.5″ horizontal, ~ 5 mm vertical |
| 100 km | ~ 50″ horizontal, ~ 50 cm vertical |

**Rule of thumb:** Use ENU for baselines < 10 km; use geodesic for longer baselines. Modern software uses geodetic computation for > 1 km.

## References

- Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS*. Springer.

- Gurtner, W. & Giesinger, B. (2019). *Coordinate Transformations in GNSS*. In: Hotine-Marussi Symposium 2020.

## Related

- [[Geodetic Coordinates]] · [[Geocentric Cartesian ECEF]] · [[GNSS]] · [[Geodesy MOC]]

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]
