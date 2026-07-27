---
title: 5. Applications of Derivatives
type: concept
subject: Mathematics
tags: [mathematics, calculus, statistics, aigis, geodesy-applied]
created: 2026-07-27
---

# 5. Applications of Derivatives

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Derivatives describe instantaneous rates of change. Their applications span **optimization** (mencari nilai ekstrem), **related rates** (tingkat hubungan), **curve sketching** (menggambar kurva), **Newton's method** (mencari akar), and **economics** — all of which appear repeatedly in computational geodesy and survey adjustment.

## 1. Optimization (Optimasi) — Finding Maxima and Minima

A function $f(x)$has a **critical point** (titik kritis) where$f'(x) = 0$or$f'(x)$is undefined. These points are candidates for local maxima or minima (nilai maksimum atau minimum lokal).

**Second Derivative Test** (Uji Turunan Kedua):$$\text{If } f'(c) = 0 \text{ and } f''(c) > 0 \implies f \text{ has a local minimum at } c
$$

$$\text{If } f'(c) = 0 \text{ and } f''(c) < 0 \implies f \text{ has a local maximum at } c$$

$$
\text{If } f''(c) = 0 \implies \text{test is inconclusive (uji tidak tegas)}$$### Constrained Optimization (Optimasi Terkonstraksi)

In geodesy, many problems minimize a quantity subject to constraints:

**Least-squares adjustment** is a constrained optimization problem: minimise$$S(\mathbf{x}) = \mathbf{v}^T \mathbf{P} \mathbf{v} = (\mathbf{A}\mathbf{x} - \mathbf{L})^T \mathbf{P} (\mathbf{A}\mathbf{x} - \mathbf{L})$$subject to observation equations. Setting$\frac{\partial S}{\partial \mathbf{x}} = \mathbf{0}$yields the **normal equations**:$$\mathbf{A}^T \mathbf{P} \mathbf{A} \hat{\mathbf{x}} = \mathbf{A}^T \mathbf{P} \mathbf{L}
$$

This is the geometric interpretation of the derivative as zero at the minimum — the gradient vanishes at the optimal solution.

### Global vs Local Optimum

A **local optimum** (optimum lokal) is the best point in a neighbourhood; a **global optimum** (optimum global) is the best over the entire domain. For convex functions ($f''(x) > 0$everywhere for univariate), any local minimum is automatically global — a property exploited in least-squares where the sum of squared residuals is always a convex function.

## 2. Related Rates (Tingkat Hubungan)

**Related rates** problems involve finding how one quantity changes with respect to time when another quantity's rate of change is known. The key technique is **implicit differentiation** (diferensiasi implisit) with respect to$t$.

### Classic Example: Expanding Circle
A circle's radius increases at $\frac{dr}{dt} = 2$m/s. How fast is the area increasing when$r = 5$m?$$A = \pi r^2 \implies \frac{dA}{dt} = 2\pi r \frac{dr}{dt} = 2\pi (5)(2) = 20\pi \;\text{m}^2/\text{s}$$### Geodetic Application: GNSS Baseline Rate
If two GNSS receivers on a moving vehicle measure a baseline vector$\mathbf{b}(t)$, the rate of change of baseline length is:
$$

\frac{d|\mathbf{b}|}{dt} = \frac{\mathbf{b} \cdot \dot{\mathbf{b}}}{|\mathbf{b}|}$$where$\dot{\mathbf{b}} = d\mathbf{b}/dt$ is the velocity of the baseline — this is the radial component of relative velocity between the two receivers.

**Tingkat hubungan** is also used in radar/lidar tracking, where range-rate ($\dot{\rho}$) relates to line-of-sight velocity through differentiation of the slant range formula.

## 3. Curve Sketching (Menggambar Kurva)

Derivatives give complete information about a function's shape through calculus:

### First Derivative: Increasing / Decreasing (Naik / Turun)
$$f'(x) > 0 \implies f \text{ increasing (naik)}$$

$$
f'(x) < 0 \implies f \text{ decreasing (turun)}$$Sign changes of$f'$identify **critical points** (titik kritis) — potential maxima or minima.

### Second Derivative: Concavity (Kelengkungan)$$f''(x) > 0 \implies f \text{ concave up (cekung ke atas)}
$$

$$
f''(x) < 0 \implies f \text{ concave down (cekung ke bawah)}$$**Inflection point** (titik belok): where$f''(x)$changes sign — the curve switches concavity.

### Procedure for Sketching (Prosedur Menggambar Kurva)

1. Domain — where is$f$defined?
2. Intercepts —$x$-intercepts ($f(x) = 0$) and $y$-intercept ($x = 0$).
3. Symmetry — even ($f(-x) = f(x)$) or odd ($f(-x) = -f(x)$).
4. Asymptotes — horizontal $\left(\lim_{x\to\pm\infty} f(x) = L\right)$, vertical (where $f$blows up), oblique.
5.$f'(x) = 0$— critical points, intervals of increase/decrease.
6.$f''(x) = 0$— inflection points, concavity.
7. Plot key points and connect with the correct shape.

## 4. Newton's Method (Metode Newton)

Newton's method is an iterative root-finding algorithm using the first derivative:$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$**Geometric interpretation**: at each step, approximate$f$by its tangent line at$x_n$, then find where that tangent meets the $x$-axis.

### Convergence

- **Quadratic convergence** (konvergensi kuadratik): when $f'(x^*) \neq 0$at the root$x^*$, the error roughly squares each iteration:
$$

|e_{n+1}| \approx C |e_n|^2$$meaning the number of correct digits approximately doubles with each step.

### Example: Solving$\cos x = x$Rewrite as$f(x) = \cos x - x = 0$, $f'(x) = -\sin x - 1$:
$$x_0 = 0.5 \implies x_1 = 0.5 - \frac{\cos(0.5) - 0.5}{-\sin(0.5) - 1} \approx 0.7553$$

$$
x_2 \approx 0.7391, \quad x_3 \approx 0.7390851$$Converges within 3 iterations to the Dottie number$\approx 0.7390851$.

**Kekurangan**: requires a good initial guess (tebakan awal); diverges if $f'(x_n) \approx 0$(near-stationary points).

## 5. Economics Applications (Aplikasi Ekonomi)

Derivatives are fundamental in economics, particularly in marginal analysis (analisis marginal):

### Marginal Cost (Biaya Marjinal)
If$C(q)$is the total cost (total biaya) function of producing$q$units:$$MC(q) = C'(q) = \lim_{\Delta q \to 0} \frac{C(q + \Delta q) - C(q)}{\Delta q}$$Marginal cost is the **additional cost** of producing one more unit — the derivative tells us the instantaneous rate of change.

### Profit Maximisation (Maksimisasi Keuntungan)
Total profit:$\Pi(q) = R(q) - C(q)$, where $R(q) = p \cdot q$is revenue (pendapatan).$$\frac{d\Pi}{dq} = MR(q) - MC(q) = 0 \implies MR(q^*) = MC(q^*)$$**Optimal quantity**$q^*$occurs at the point where **marginal revenue equals marginal cost** — a direct application of setting the derivative to zero.

### Elasticity of Demand (Elastisitas Permintaan)
Price elasticity measures the percentage change in quantity demanded for a 1% change in price:$$\varepsilon = \frac{dq}{dp} \cdot \frac{p}{q}$$When$|\varepsilon| > 1$: demand is **elastic** (peka) — small price changes cause large quantity changes. When $|\varepsilon| < 1$: demand is **inelastic** (tidak peka).

### Consumer & Producer Surplus (Surplus Konsumen & Produsen)
Surplus is computed the definite integral (integral tertentu) of the difference between demand/supply curves and the market price:
$$

\text{Consumer Surplus} = \int_{0}^{q^*} \big[D(q) - p^*\big]\, dq$$The integrand$D(q) - p^*$is the difference between the willingness-to-pay and the market price — the derivative of this integral with respect to$q^*$gives the marginal consumer surplus (demand curve at the optimal point).

## 6. Where Geodesy Uses Derivatives

| Application | Derivative Usage |
|-------------|------------------|
| Least-squares adjustment | Gradient$\nabla S = 0$at the minimum sum of squared residuals |
| Geoid modelling | Potential$\Phi \implies \vec{g} = -\nabla\Phi$; gravity derived from the gradient of gravity potential |
| GPS ambiguity resolution | LAMBDA method uses cost function derivatives for integer least squares |
| Map projection scale variation | $k(\phi) = \sec\phi$; derivative $dk/d\phi = \sec\phi\tan\phi$ tells how fast scale changes with latitude |

## Linked vault notes

- [[Geoid Undulation]]

- [[Least Squares Adjustment]]

- [[Mathematics MOC]]

---
*Maintained by AIGIS.*
