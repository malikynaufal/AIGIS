---
title: Semester 2 — Persamaan Diferensial (Expanded)
type: course-notes
subject: Mathematics
tags: [mathematics, differential-equations, semester-2, aigis, geodesy-applied]
---

# Semester 2 — Persamaan Diferensial (Expanded)

**Course**: MGM211202 — Persamaan Diferensial Ordinary (ODE)
**Credits**: 3 SKS
**Prerequisites**: [[Kalkulus I Expanded]], [[Kalkulus II Expanded]]

---

## Course Overview

Ordinary Differential Equations are the language of dynamics. This course covers first-order ODEs, second-order linear ODEs, systems of ODEs, and introduces Laplace transforms. Applications include mechanical vibrations, circuit theory, and population dynamics.

---

## Syllabus

### Weeks 1-3: First-Order ODEs

#### 1.1 General Form

$$\frac{dy}{dx} = f(x,y)

$ $

Existence and Uniqueness Theorem (Picard-Lindelöf): If $ f $ and $ artial f/artial y $ are continuous near $ (x_0, y_0) $, then $ y' = f(x,y) $,$ y(x_0) = y_0 $ has a unique local solution.

#### 1.2 Separable Equation
s

$ $\frac{dy}{dx} = g(x)h(y) \\implies \int \frac{dy}{h(y)} = \int g(x)\,dx

$ $**Example**: $ y' = xy $,$ y(0)=2 $

$ $\int \frac{dy}{y} = \int x\,dx \\implies \ln y = x^2/2 + C

$ $

$ y = 2e^{x^2/2} $#### 1.3 First-Order Linea
r

$ $ y' + P(x)y = Q(x) $ $

Integrating factor $\mu = e^{\int P\,dx} $:

$ $ (\mu y)' = \mu Q $ $**Example**: $ y' + 2y = e^{-x} $,$ y(0)=0 $

$\mu = e^{2x} $

$ (e^{2x}y)' = e^{2x}e^{-x} = e^x $

$ e^{2x}y = e^x - 1 $

$ y = e^{-x} - e^{-2x} $#### 1.4 Exact Equations $ M(x,y)\,dx + N(x,y)\,dy = 0 $ is exact if $ M_y = N_x $.

Find $ F $ with $ F_x = M $, $ F_y = N $. Solution: $  F = C $.

#### 1.5 Bernoulli Equation

$ y' + P(x)y = Q(x)y^n $ Substitute $  v = y^{1-n} $→ linear in $  v $.

**Example**: $ y' + y/x = y^2/x^2 $ ( $ n=2 $)
$ v = y^{-1} $: $ v' - v/x = -1/x^2 $→ linear,$\mu = 1/x $
$ (v/x)' = -1/x^3 $→$ v/x = 1/(2x^2) + C $→$  v = 1/(2x) + Cx $#### 1.6 Homogeneous Equations $ y' = F(y/x) $→ substitute $  v = y/x $, $  y = xv $, $ y' = v + xv'$### Weeks 4-6: Second-Order Linear ODEs

#### 2.1 Homogeneous: $ y'' + py' + qy = 0 $ Characteristic equation $ r^2 + pr + q = 0 $.

| Discriminant | Roots | Solution |
|-------------|-------|----------|
| $\Delta > 0 $|$ r_1 \neq r_2 $ real | $  y = C_1e^{r_1 x} + C_2e^{r_2 x} $ |
| $\Delta = 0 $| repeated $  r $|$  y = (C_1 + C_2 x)e^{rx} $ |
| $\Delta < 0 $|$\alpha m \beta i $|$  y = e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x) $ |

#### 2.2 Worked Example $ y'' - 3y' + 2y = 0 $ Characteristic: $ r^2-3r+2 = (r-1)(r-2) = 0 $

$ y = C_1e^x + C_2e^{2x} $

$ y(0)=1 $: $ C_1+C_2=1 $
$ y'(0)=3 $: $ C_1+2C_2=3 $→$ C_2=2 $, $ C_1=-1 $

$ y = -e^x + 2e^{2x} $#### 2.3 Nonhomogeneous: $ y'' + py' + qy = g(x) $

$ y = y_h + y_p $ (homogeneous + particular)

**Undetermined Coefficients**: Guess form of $ y_p $ based on $ g(x) $:

| $ g(x) $ | Trial $ y_p $ |
|--------|-------------|
| $ Ae^{\alpha x} $ | $ Be^{\alpha x} $ |
| $ A\cos\omega x $ | $ B\cos\omega x + C\sin\omega x $ |
| $ Ax^n $ | $ B_nx^n + \cdots + B_0 $ |
| Product of above | Product of individual trials |

**If trial is a solution to homogeneous**: multiply by $ x $ (or $ x^2 $).

**Example**: $ y''-3y'+2y = e^{3x} $ Trial: $ y_p = Ae^{3x} $

$ 9Ae^{3x} - 9Ae^{3x} + 2Ae^{3x} = e^{3x} $→$ 2A = 1 $→$  A = 1/2 $

$ y = C_1e^x + C_2e^{2x} + \frac{1}{2}e^{3x} $#### 2.4 Variation of Parameters

For $ g(x) $ not matching undetermined coefficients

$ $ y_p = -y_1\int\frac{y_2g}{W}\,dx + y_2\int\frac{y_1g}{W}\,dx $ $

where $ W = y_1y_2' - y_2y_1'$ (Wronskian).

#### 2.5 Mechanical Vibrations $ my'' + cy' + ky = F(t) $-$ c=0 $: undamped (pure oscillation)

- $ c > 0 $: damped (exponential decay × oscillation)

- **Resonance**: $\omega_{ext{drive}} \approx \omega_{ext{natural}} $→ large amplitude

### Weeks 7-9: Systems of ODEs

#### 3.1 Matrix For
m

$ $\mathbf{x}' = A\mathbf{x}, \\quad \mathbf{x}(0) = \mathbf{x}_0

$ $ 3.2 Matrix Exponentia
l $ $

# 3.2 Matrix Exponentia
l

### # 3.2 Matrix Exponentia
l\mathbf{x}(t) = e^{At}\mathbf{x}_0

$ $

#### 3.3 Eigenvalue Solution

If $ A $ has distinct eigenvalues $\lambda_1, \lambda_2 $ with eigenvectors $\mathbf{v}_1, \mathbf{v}_2 $:

$ $\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_
2

$ $**Worked Example**:

$ $

x' = x+y, \\quad y' = 4x+y $ $

$ A = \begin{bmatrix}1&1\\\&1\end{bmatrix} $, $\lambda^2-2\lambda-3=0 $, $\lambda_1=3 $, $\lambda_2=-1 $ Eigenvectors: $\mathbf{v}_1=(1,2)^T $, $\mathbf{v}_2=(1,-2)^T $

$\mathbf{x}(t) = c_1e^{3t}\begin{pmatrix}1\\2\end{pmatrix} + c_2e^{-t}\begin{pmatrix}1\\-2\end{pmatrix} $#### 3.4 Phase Portraits

| Eigenvalue Type | Phase Portrait |
|----------------|---------------|
| Two negative reals | Stable node |
| Two positive reals | Unstable node |
| Opposite signs | Saddle point |
| Complex, negative real part | Stable spiral |
| Complex, positive real part | Unstable spiral |
| Pure imaginary | Center |

### Weeks 10-12: Laplace Transforms

#### 4.1 Definitio
n

$ $ F(s) = \mathcal{L}\\{f(t)\\} = \int_0^{\infty}e^{-st}f(t)\,dt $ $

#### 4.2 Table of Transforms

| $ f(t) $ | $ F(s) $ |
|---------|--------|
| $ 1 $ | $ 1/s $ |
| $ t $ | $ 1/s^2 $ |
| $ t^n $ | $ n!/s^{n+1} $ |
| $ e^{at} $ | $ 1/(s-a) $ |
| $\sin(\omega t) $|$\omega/(s^2+\omega^2) $ |
| $\cos(\omega t) $|$ s/(s^2+\omega^2) $ |
| $ e^{at}f(t) $ | $ F(s-a) $ |
| $\delta(t) $|$ 1 $ |
| $ u(t-a)f(t-a) $ | $ e^{-as}F(s) $ |

#### 4.3 Inverse Transforms

Use partial fractions + table lookup.

**Example**: $\frac{5s+3}{(s+1)(s+2)} = \frac{A}{s+1}+\frac{B}{s+2} $

$ A = \frac{5(-1)+3}{-1+2} = \frac{-2}{1} = -2 $

$ B = \frac{5(-2)+3}{-2+1} = \frac{-7}{-1} = 7 $

$\mathcal{L}^{-1} = -2e^{-t} + 7e^{-2t} $#### 4.4 Solving ODEs with Laplace

**Example**: $ y''+4y=0 $, $ y(0)=1 $, $ y'(0)=0 $

$ s^2Y-s-0+4Y=0 $→$ Y(s^2+4)=s $→$  Y = \frac{s}{s^2+4} $

$ y = \cos(2t) $---

## Practice Problems

1. Solve $ y' = y^2 $, $ y(0) = 1/3 $ 2. Solve $ y'' + 4y' + 4y = e^{-2x} $ 3. Solve the IVP: $\mathbf{x}' = \begin{bmatrix}1&2\\-1&1\end{bmatrix}\mathbf{x} $, $\mathbf{x}(0)=\begin{bmatrix}1\\0\end{bmatrix} $ 4. Use Laplace to solve $ y''-3y'+2y=\sin t $, $ y(0)=0 $, $ y'(0)=1$

---

## Geodesy Connections

- **Orbit propagation**: Satellite motion equations (2nd order ODEs)

- **Inertial navigation**: Strapdown IMU ODEs

- **Kalman filter**: State-space ODEs for GPS positioning

- **Tidal loading**: Time-series ODE models

---

## References

- OpenStax Differential Equations (Chapters 1-4)

- MIT OCW 18.03: Differential Equations

- Boyce, W. & DiPrima, R. *Elementary Differential Equations* (Chapters 1-5)

---

➡️ [[Mathematics MOC]] | ➡️ [[Differential Equations intro]]