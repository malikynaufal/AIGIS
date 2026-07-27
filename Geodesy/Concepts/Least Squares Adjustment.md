---
tags: [geodesy, concept, statistics, computation, aigis]
aliases: [Least Squares, Least Squares Adjustment]
created: 2026-07-12
updated: 2026-07-27
---

# 📐 Least Squares Adjustment

The **least squares adjustment** (also called *least squares estimation* or *collocation*) is the foundational statistical method for combining redundant, noisy measurements to obtain best‑fit estimates of unknowns. Gauss and Legendre independently developed the method at the end of the 18th century; in modern geodesy it underlies every network adjustment — from a simple level run to global GNSS baselines.

> **Indonesian term:** *Perataan Kuadrat Terkecil*

---

## 1. Core Idea

For a system with $n $ observations and $ u $ unknowns ($ n > u $), we write each observation equation as:

$ $\ell_i + v_i = f_i(x_1, x_2, \ldots, x_u
)

$$

or in vector form:$ $\mathbf{L} + \mathbf{V} = \mathbf{F}(\mathbf{X})

$$

where:

| Symbol | Meaning |
|--------|---------|
| $\mathbf{L} $ | Vector of observations (n×1) |
| $\mathbf{V} $ | Vector of residuals (n×1) |
| $\mathbf{F}(\mathbf{X}) $ | Vector of nonlinear functions |
| $\mathbf{X} $ | Vector of unknowns (u×1) |

Linearising about an approximate value $\mathbf{X}_0 $:

$ $\mathbf{V} = \mathbf{A}\,\mathbf{x} - \boldsymbol{\ell} $$

with:
-$\mathbf{A} = \partial\mathbf{F}/\partial\mathbf{X}\big|_{\mathbf{X}_0} $— Jacobian (n×u)
-$\mathbf{x} = \mathbf{X} - \mathbf{X}_0 $— parameter corrections (u×1)
-$\boldsymbol{\ell} = \mathbf{L} - \mathbf{F}(\mathbf{X}_0) $— observed minus computed (n×1)

---

## 2. Least Squares Principle

Minimise the weighted sum of squared residuals

$ $\mathbf{V}^\top \mathbf{W}\,\mathbf{V} \;\longrightarrow\; \min

$$

where $\mathbf{W} = \mathbf{P}^{-1} $ and $\mathbf{P} $ is the **weight matrix** (n×n) of observations. Typically $\mathbf{P} = \text{diag}(\sigma_i^{-2}) $ for variances $\sigma_i^2 $.

---

## 3. Solution – Normal Equation System

Setting the derivative to zero yields the **normal equations**:

$ $\boxed{\;\mathbf{A}^\top\mathbf{P}\,\mathbf{A}\,\hat{\mathbf{x}} = \mathbf{A}^\top\mathbf{P}\,\boldsymbol{\ell}\;} $$

or in matrix form $\mathbf{N}\hat{\mathbf{x}} = \mathbf{U} $, where $\mathbf{N} = \mathbf{A}^\top\mathbf{P}\,\mathbf{A} $ is the **normal‑equation matrix**.

Solution

$ $\hat{\mathbf{x}} = \mathbf{N}^{-1}\,\mathbf{U} $$

Adjusted unknowns: $\hat{\mathbf{X}} = \mathbf{X}_0 + \hat{\mathbf{x}} $.

---

## 4. Residuals and Posteriori Variance

After solving, residuals:

$ $\hat{\mathbf{V}} = \mathbf{A}\hat{\mathbf{x}} - \boldsymbol{\ell
}

$$**Reference variance** (a posteriori variance factor):

$ $\hat{\sigma}_0^2 = \frac{\hat{\mathbf{V}}^\top\mathbf{P}\,\hat{\mathbf{V}}}{n-u} = \frac{\hat{\mathbf{V}}^\top\mathbf{P}\,\hat{\mathbf{V}}}{r}

$$

where $ r = n - u $ is the **redundancy number** (degrees of freedom).

---

## 5. Variance–Covariance Propagation

The variance–covariance matrix of the adjusted parameters is

$ $\boxed{\;\mathbf{Q}_{\hat{\mathbf{X}}} = \sigma_0^2\,\mathbf{N}^{-1}\;} $$

The variance–covariance matrix of the residuals $ $\mathbf{Q}_{\hat{\mathbf{V}}} = \sigma_0^2\bigl(\mathbf{P}^{-1} - \mathbf{A}\,\mathbf{N}^{-1}\,\mathbf{A}^\top\bigr)

$$

For a derived quantity $ y = \mathbf{c}^\top\hat{\mathbf{X}} $ (a single‑parameter function)$ $\sigma_y^2 = \sigma_0^2 \cdot \mathbf{c}^\top\mathbf{N}^{-1}\mathbf{c} $$

---

## 6. Worked Example – Trilateration Network

A simple level‑net: unknowns are the heights of stations B and C relative to A. Observed differences $ h_i $ with weights $ p_i $:

| Observation | $ h_i $ (m) | $\sigma_i $ (mm) | $ p_i = 1/\sigma_i^2 $ |
|-------------|-----------|-----------------|----------------------|
| A → B | 1.234 | 2 | 250 000 |
| B → C | −2.105 | 2 | 250 000 |
| A → C | −0.872 | 2 | 250 000 |

The system in terms of $ x_B, x_C $:

$ $\begin{aligned}
x_B &= h_{AB} - v_1\\
x_C - x_B &= h_{BC} - v_2\\
x_C &= h_{AC} - v_3
\end{aligned
}

$$

Design matrix:$ $

\mathbf{A} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \\ 0 & 1 \end{bmatrix},\quad \boldsymbol{\ell} = \begin{bmatrix} h_{AB} \\ h_{BC} \\ h_{AC} \end{bmatrix},\quad \mathbf{P} = 250\,000\cdot \mathbf{I
}

$$

Normal equations:$ $

\mathbf{N} = \mathbf{A}^\top\mathbf{P}\,\mathbf{A} = 250\,000\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix
}

$$

Solving:$ $\hat{\mathbf{x}} = \begin{bmatrix} x_B \\ x_C \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 2\,h_{AB} + h_{BC} - h_{AC} \\ h_{AB} + 2\,h_{BC} + h_{AC} \end{bmatrix}

$$

With our numbers:
-$ x_B = (2(1.234) + (-2.105) - (-0.872))/3 = 1.235/3 = 0.412 $ m
-$ x_C = (1.234 + 2(-2.105) + (-0.872))/3 = -3.848/3 = -1.283 $ m

Residuals

$ $\hat{\mathbf{V}} = \mathbf{A}\hat{\mathbf{x}} - \boldsymbol{\ell} = \begin{bmatrix} -0.001 \\ 0.000 \\ +0.001 \end{bmatrix} \;\text{m} $$ A posteriori variance $ $\hat{\sigma}_0^2 = \frac{250\,000(0.001^2+0^2+0.001^2)}{3-2} = 0.5\;\text{mm}^2

$$

---

## 7. Special Forms

### 7.1. Parametric adjustment (what we just did
)

$ $\mathbf{V} = \mathbf{A}\mathbf{x} - \boldsymbol{\ell} $$

### 7.2. Condition adjustment

Use only redundancy conditions

$ $\mathbf{B}\mathbf{V} + \mathbf{W} = 0

$$

with solution $\mathbf{V} = -\mathbf{P}^{-1}\mathbf{B}^\top(\mathbf{B}\mathbf{P}^{-1}\mathbf{B}^\top)^{-1}\mathbf{W} $.

### 7.3. Adjustment with constraints

Add constraints $\mathbf{C}\hat{\mathbf{x}} = \mathbf{d} $ via Lagrange multipliers $ $\begin{bmatrix} \mathbf{N} & \mathbf{C}^\top \\ \mathbf{C} & 0 \end{bmatrix}\begin{bmatrix} \hat{\mathbf{x}} \\ \boldsymbol{\lambda} \end{bmatrix} = \begin{bmatrix} \mathbf{U} \\ \mathbf{d} \end{bmatrix} $$

### 7.4. Sequential / Kalman filter

Recursive update for streaming data

$ $\hat{\mathbf{x}}_{k+1} = \hat{\mathbf{x}}_k + \mathbf{K}_{k+1}(\ell_{k+1} - \mathbf{a}_{k+1}\hat{\mathbf{x}}_k)

$$

with gain $\mathbf{K} = \mathbf{Q}_{\hat{\mathbf{x}}_k}\mathbf{a}^\top(\mathbf{a}\mathbf{Q}_{\hat{\mathbf{x}}_k}\mathbf{a}^\top + \sigma^2)^{-1} $.

---

## 8. Variants in Geodesy

| Technique | Application |
|-----------|-------------|
| **Static network adjustment** | Classical baseline / level‑net |
| **Sequential adjustment** | Real‑time GNSS / INS integration |
| **Kalman filter** | RTK, PPP, integrated navigation |
| **Robust M‑estimator** | Detection of outliers (Huber, Danish) |
| **L1‑norm (LAD)** | Outlier‑resistant alternative |
| **Total Least Squares** | Errors in both data and coefficients |

---

## 9. Diagram – Workflow

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200" width="700" height="200">
 <rect width="700" height="200" fill="#1a1a2e" rx="8"/>
 <!-- Boxes -->
 <g font-family="sans-serif" font-size="11" fill="#fff" text-anchor="middle">
 <rect x="20" y="70" width="120" height="60" fill="#4cc9f0" rx="6"/>
 <text x="80" y="105">Observations L</text>
 <rect x="170" y="70" width="120" height="60" fill="#f9c74f" rx="6"/>
 <text x="230" y="105">Linearise (build A, ℓ)</text>
 <rect x="320" y="70" width="120" height="60" fill="#7209b7" rx="6"/>
 <text x="380" y="105">Normal eq. N·x̂ = U</text>
 <rect x="470" y="70" width="120" height="60" fill="#f72585" rx="6"/>
 <text x="530" y="105">Solve: x̂ = N⁻¹·U</text>
 <rect x="580" y="150" width="100" height="40" fill="#06d6a0" rx="6"/>
 <text x="630" y="175">Qxx = σ₀²·N⁻¹</text>
 </g>
 <!-- Arrows -->
 <g stroke="#fff" stroke-width="2" fill="none" marker-end="url(#a)">
 <line x1="140" y1="100" x2="170" y2="100"/>
 <line x1="290" y1="100" x2="320" y2="100"/>
 <line x1="440" y1="100" x2="470" y2="100"/>
 </g>
 <defs><marker id="a" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#fff"/></marker></defs>
</svg>

---

## 10. Related

- [[Resources/least-squares|Resources – Least Squares]] – worked examples in Python.

- [[Datum Transformation]] – adjusted points used in datum shifts.

- [[Helmert Transformation]] – solved by least squares in multi‑datum networks.

- [[GNSS]] – every baseline processor uses least squares.

- [[Statistical tests|Quality assurance]] – global, tau, w‑tests.

---

## 11. References

- Gauss, C.F., *Theoria motus corporum coelestium*, 1809. (public‑domain)

- Legendre, A.M., *Nouvelles méthodes pour la détermination des orbites des comètes*, 1805.

- Mikhail, E.M. & Ackermann, F., *Observations and Least Squares*, University Press of America, 1976.

- Wolf, P.R. & Ghilani, C.D., *Adjustment Computations: Spatial Data Analysis* (6th ed.), Wiley, 2017.

- Koch, K.-R., *Introduction to Bayesian Statistics* (2nd ed.), Springer, 2007. DOI:10.1007/978-3-540-72726-1

- Ghilani, C.D., *Elementary Surveying* (14th ed.), Pearson, 2017. (CC‑BY lecture notes available via Penn State)

- Strang, G. & Borre, K., *Linear Algebra, Geodesy, and GPS*, Wellesley‑Cambridge Press, 1997. (lecture‑slide versions available OA)

➡️ [[Geodesy MOC]] · [[Basic Geodesy]]