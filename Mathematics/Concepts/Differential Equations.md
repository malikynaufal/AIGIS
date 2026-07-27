---
title: 6. Differential Equations (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, differential-equations, ODE, PDE, aigis, geodesy-applied]
---

# 6. Differential Equations (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

Differential equations describe relationships between functions and their derivatives. They model natural phenomena: motion, heat, waves, population dynamics, and orbital mechanics.

## 1. Classification

### 1.1 By Order
The **order** is the highest derivative present:

- 1st order: $\frac{dy}{dx} = f(x,y) $- 2nd order: $\frac{d^2y}{dx^2} + f\frac{dy}{dx} + g\,y = h $### 1.2 By Linearity
**Linear**: $y $and its derivatives appear only to first power, no products

$$ a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = g(x)$$

**Nonlinear**: Any deviation from linearity.

### 1.3 By Homogeneity

- **Homogeneous**: $g(x) = 0$- **Non-homogeneous**: $g(x) \neq 0$## 2. First-Order Ordinary DEs

### 2.1 Separable Equations

Form: $\frac{dy}{dx} = g(x)h(y) $**Method**: Separate variables, integrate both sides

$$\int \frac{1}{h(y)}\,dy = \int g(x)\,dx

$$**Example**: $\frac{dy}{dx} = xy $,$y(0) = 2 $Separate: $\frac{1}{y}\,dy = x\,dx $Integrate:$\ln|y| = \frac{x^2}{2} + C $Solution:$y = 2e^{x^2/2} $### 2.2 First-Order Linear DEs

Form: $\frac{dy}{dx} + P(x)y = Q(x) $**Integrating factor**: $\mu(x) = e^{\int P(x)\,dx} $Multiply through:$\frac{d}{dx}[\mu y] = \mu Q $

$$ y = \frac{1}{\mu}\int \mu Q\,dx $$**Example**: $\frac{dy}{dx} + 2y = e^{-x} $

$\mu = e^{\int 2\,dx} = e^{2x} $

$$ e^{2x}y = \int e^{2x}e^{-x}\,dx = \int e^{x}\,dx = e^{x} + Cy = e^{-x} + Ce^{-2x}$$

### 2.3 Exact Equations

Form: $M(x,y)\,dx + N(x,y)\,dy = 0 $is exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} $**Method**: Find $F(x,y)$such that $\frac{\partial F}{\partial x} = M $, $\frac{\partial F}{\partial y} = N $Solution:$F(x,y) = C $**Example**: $(2xy + 3)\,dx + (x^2 + 4y)\,dy = 0$

$M_y = 2x$, $N_x = 2x$✓ (exact) $F = x^2y + 3x + 2y^2$, so $x^2y + 3x + 2y^2 = C$### 2.4 Bernoulli Equations

Form: $\frac{dy}{dx} + P(x)y = Q(x)y^n $Substitute $v = y^{1-n} $, transforms to linear DE.

## 3. Second-Order Linear DEs with Constant Coefficients

### 3.1 Homogeneous: $ay'' + by' + cy = 0$**Characteristic equation**: $ar^2 + br + c = 0$ | Roots | General Solution |
|-------|-----------------|
| Distinct real $r_1 \neq r_2$ | $y = C_1e^{r_1x} + C_2e^{r_2x}$ |
| Repeated $r_1 = r_2$ | $y = (C_1 + C_2x)e^{r_1x}$ |
| Complex $r = \alpha \pm \beta i$ | $y = e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$ |

### 3.2 Non-homogeneous: $ay'' + by' + cy = g(x)$**General solution**: $y = y_h + y_p $where $y_h $is homogeneous solution and $y_p $is particular solution.

#### Undetermined Coefficients Method

| $g(x)$ | Trial $y_p$ |
|--------|-------------|
| $ke^{\alpha x}$ | $Ae^{\alpha x}$ |
| $kx^n$ | $A_nx^n + \cdots + A_0$ |
| $k\cos\beta x$ | $A\cos\beta x + B\sin\beta x$ |
| $ke^{\alpha x}\cos\beta x$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

#### Variation of Parameter
s

$$ y_p = -y_1\int\frac{y_2g}{W}\,dx + y_2\int\frac{y_1g}{W}\,dx $$ where $ W = y_1y_2' - y_2y_1'$ is the Wronskian.

## 4. Systems of ODEs

### 4.1 Matrix For
m

$$\mathbf{x}' = A\mathbf{x} $$ where $ A $is constant matrix. Solution involves eigenvalues/eigenvectors of $A $.

If $A $has eigenvalue $\lambda $with eigenvector $\mathbf{v} $:

$$\mathbf{x}(t) = e^{\lambda t}\mathbf{v} $$

### 4.2 Phase Portrait Classification

For $2\times 2 $systems with eigenvalues $\lambda_1, \lambda_2 $:

| Eigenvalues | Type |
|-------------|------|
| $\lambda_1 \neq \lambda_2 $, both negative | Stable node |
| $\lambda_1 \neq \lambda_2 $, both positive | Unstable node |
| Opposite signs | Saddle point |
| Complex, Re $<0 $ | Stable spiral |
| Complex, Re $>0 $ | Unstable spiral |
| Pure imaginary | Center |

## 5. Laplace Transforms

### 5.1 Definitio
n

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st}f(t)\,dt

$$

### 5.2 Common Transforms

| $f(t)$ | $F(s)$ |
|---------|--------|
| $1$ | $\frac{1}{s} $ |
| $t^n$ | $\frac{n!}{s^{n+1}} $ |
| $e^{at}$ | $\frac{1}{s-a} $ |
| $\sin(\omega t) $|$\frac{\omega}{s^2+\omega^2} $ |
| $\cos(\omega t) $|$\frac{s}{s^2+\omega^2} $ |
| $e^{at}f(t)$ | $F(s-a)$ |

### 5.3 Key Properties

- **Linearity**: $\mathcal{L}\{af+bg\} = aF(s)+bG(s) $- **Derivative**: $\mathcal{L}\{f'\} = sF(s) - f(0) $- **Second derivative**: $\mathcal{L}\{f''\} = s^2F(s) - sf(0) - f'(0) $- **Convolution**: $\mathcal{L}\{f*g\} = F(s)G(s) $### 5.4 Solving IVPs with Laplace

**Example**: $y'' + 3y' + 2y = e^{-t}$, $y(0)=0$, $y'(0)=1 $Take Laplace: $(s^2+3s+2)Y - 1 = \frac{1}{s+1}$

$$

Y = \frac{s+2}{(s+1)(s+2)(s+1)} + \frac{1}{(s+1)(s+2)
}

$$ Partial fractions + inverse Laplace: $$ y(t) = -e^{-t} + 3e^{-2t} + te^{-t}$$ ## 6. Practice Problems

### Problem 1
Solve $\frac{dy}{dx} = \frac{x}{y} $, $y(0) = 3$**Solution**: Separable

$$\int y\,dy = \int x\,dx \implies \frac{y^2}{2} = \frac{x^2}{2} + Cy(0) = 3 \implies C = \frac{9}{2}y = \sqrt{x^2+9} $$

### Problem 2
Solve $y'' - 5y' + 6y = 0$, $y(0)=1$, $y'(0)=2$**Solution**: Characteristic equation $r^2-5r+6=0$, roots $r=2,3$

$$ y = C_1e^{2x} + C_2e^{3x}$$

$y(0)=1$: $C_1+C_2=1$
$y'(0)=2$: $2C_1+3C_2=2$

$C_1=1$, $C_2=0$→$y = e^{2x}$### Problem 3
Solve $y' + 2y = 4$, $y(0)=1$**Solution**: $\mu = e^{2x} $

$$ e^{2x}y = \int 4e^{2x}\,dx = 2e^{2x} + Cy = 2 + Ce^{-2x}$$

$y(0)=1$: $C=-1$→$ y = 2 - e^{-2x}$

## 7. Where Geodesy Uses This

- **Dynamic orbit models**: Keplerian motion equations

- **Tide/load time series**: periodic loading functions

- **Inertial navigation**: strapdown IMU equations

- **Crustal deformation**: viscoelastic models

- **Kalman filtering**: state-space ODEs for GPS

- **Atmospheric refraction**: ray-tracing equations

## 8. References

- OpenStax Differential Equations

- MIT OCW 18.03: Differential Equations

- Boyce & DiPrima (2012). *Elementary DEs*

---

*Maintained by AIGIS.*
