---
title: 2. Derivatives (Expanded)
type: concept
subject: Mathematics
tags: [mathematics, calculus, derivatives, aigis, geodesy-applied]
---

# 2. Derivatives (Expanded)

> Part of the [[Mathematics MOC]] study pack. AIGIS built this for your
> future Calculus & Statistics courses, tied to [[Geodesy MOC]] usage.

## Summary

The derivative measures the instantaneous rate of change of a function with respect to its variable. It is the fundamental tool for optimization, modeling change, and understanding local behavior of functions.

## 1. Core Definition

The derivative of $f(x) $at $x = a $is defined as $$ f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$ This limit, if it exists, gives the slope of the tangent line at$ (a, f(a))$.

### Alternative Notations

| Notation | Used By |
|----------|----------|
| $f'(x)$ | Lagrange |
| $\frac{df}{dx} $ | Leibniz |
| $D_x f$ | Differential operator |
| $\dot{f} $ | Physics (time derivative) |

## 2. Differentiation Rules

### 2.1 Basic Rules

| Rule | Formula |
|------|---------|
| Constant | $\frac{d}{dx}[c] = 0 $ |
| Power Rule | $\frac{d}{dx}[x^n] = nx^{n-1} $ |
| Constant Multiple | $\frac{d}{dx}[cf(x)] = cf'(x) $ |
| Sum/Difference | $\frac{d}{dx}[f \pm g] = f' \pm g'$ |

### 2.2 Product Rule

If $f(x) = u(x) \cdot v(x)$, then:

$$\frac{d}{dx}[uv] = u'v + uv
'

$$**Proof**: Using the limit definition:

$$(uv)' = \lim_{h \to 0} \frac{u(x+h)v(x+h) - u(x)v(x)}{h}= \lim_{h \to 0} \left[ \frac{u(x+h)-u(x)}{h}v(x+h) + u(x)\frac{v(x+h)-v(x)}{h} \right]= u'(x)v(x) + u(x)v'(x)$$

### 2.3 Quotient Rule

If $f(x) = \frac{u(x)}{v(x)}$, then:

$$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2} $$**Proof**: Similar to product rule, write $\frac{u}{v} = u \cdot v^{-1} $ and apply product + chain rules.

### 2.4 Chain Rule (Composite Functions)

If $y = f(g(x))$, then:

$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)

$$ In Leibniz notation, if$ y = f(u) $and $u = g(x) $:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} $$**Example**: Find $\frac{d}{dx}[\sin(x^2)] $- Let $u = x^2$,$f(u) = \sin(u)$-$f'(u) = \cos(u)$,$g'(x) = 2x$- Result: $\cos(x^2) \cdot 2x = 2x\cos(x^2) $## 3. Derivatives of Common Functions

### 3.1 Trigonometric Functions

| Function | Derivative |
|----------|------------|
| $\sin x $|$\cos x $ |
| $\cos x $|$-\sin x $ |
| $\tan x $|$\sec^2 x $ |
| $\cot x $|$-\csc^2 x $ |
| $\sec x $|$\sec x \tan x $ |
| $\csc x $|$-\csc x \cot x $ |

### 3.2 Exponential & Logarithmic

| Function | Derivative |
|----------|------------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x $|$\frac{1}{x} $ |
| $\log_a x $|$\frac{1}{x \ln a} $ |

### 3.3 Inverse Functions

If $y = f^{-1}(x)$, then:

$$\frac{dy}{dx} = \frac{1}{f'(y)} $$**Example**: $\frac{d}{dx}[\arcsin x] = \frac{1}{\sqrt{1-x^2}} $## 4. Higher-Order Derivatives

The $n$-th derivative is denoted $f^{(n)}(x)$:

$$ f''(x) = \frac{d}{dx}\left(\frac{df}{dx}\right)f^{(n)}(x) = \frac{d}{dx}\left(f^{(n-1)}(x)\right)$$**Example**: $f(x) = x^4$-$f'(x) = 4x^3$-$f''(x) = 12x^2$-$f'''(x) = 24x$-$f^{(4)}(x) = 24$-$f^{(5)}(x) = 0$## 5. Implicit Differentiation

For equations where $y $is not isolated, differentiate both sides with respect to $x$, treating $y $as $y(x)$.

**Example**: Find $\frac{dy}{dx} $for $x^2 + y^2 = r^2 $1. Differentiate:$\frac{d}{dx}[x^2] + \frac{d}{dx}[y^2] = 0 $ 2.$2x + 2y\frac{dy}{dx} = 0$3. Solve: $\frac{dy}{dx} = -\frac{x}{y} $## 6. Related Rates

Problems where related quantities change with time.

**Example**: A ladder 10 ft long slides down a wall. When the bottom is 6 ft from the wall, it's moving at 2 ft/s. How fast is the top sliding?

Let $x$ = distance from wall,$y$ = height on wal
l

$$ x^2 + y^2 = 10^2 $$ Differentiate:$ 2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 $At $x=6 $: $y = \sqrt{100-36} = 8$

$$2(6)(2) + 2(8)\frac{dy}{dt} = 0\frac{dy}{dt} = -\frac{12}{8} = -1.5 \text{ ft/s}$$ The top slides down at 1.5 ft/s.

## 7. Applications

### 7.1 Optimization

To find local extrema, set $f'(x) = 0 $and check $f''(x)$:

- $f'(x) = 0$: critical point

- $f''(x) > 0$: local minimum

- $f''(x) < 0$: local maximum

### 7.2 Linear Approximation

$$

f(x) \approx f(a) + f'(a)(x-a
)

$$### 7.3 Taylor Series $$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots $$## 8. Practice Problems

### Problem 1
Find $\frac{dy}{dx} $for $y = x^2 \sin x $**Solution**: Use product rul
e

$$ y' = (x^2)'\sin x + x^2(\sin x)' = 2x\sin x + x^2\cos x $$

### Problem 2
Find $\frac{dy}{dx} $for $y = \frac{x^2 + 1}{x^2 - 1} $**Solution**: Use quotient rul
e

$$ y' = \frac{(2x)(x^2-1) - (x^2+1)(2x)}{(x^2-1)^2} = \frac{2x(x^2-1-x^2-1)}{(x^2-1)^2} = \frac{-4x}{(x^2-1)^2}$$

### Problem 3
Find all critical points of $f(x) = x^3 - 3x^2 + 2$**Solution**

$$ f'(x) = 3x^2 - 6x = 3x(x-2)$$ Set$ f'(x) = 0 $: $x = 0 $or $x = 2$

$$ f''(x) = 6x - 6 $$- At $x = 0$: $f''(0) = -6 < 0$→ local maximum,$f(0) = 2$- At $x = 2$: $f''(2) = 6 > 0$→ local minimum,$f(2) = -2$### Problem 4
Find $\frac{dy}{dx} $of $e^{xy} + x^2 = y $at$(1, 1)$**Solution**: Differentiate implicitl
y

$$ e^{xy}(y + x\frac{dy}{dx}) + 2x = \frac{dy}{dx}$$ At$ (1,1)$: $e^1(1 + \frac{dy}{dx}) + 2 = \frac{dy}{dx}$

$$ e + e\frac{dy}{dx} + 2 = \frac{dy}{dx}e + 2 = \frac{dy}{dx}(1 - e)\frac{dy}{dx} = \frac{e+2}{1-e}$$

## 9. Where Geodesy Uses This

- **Linearizing geodetic models** (Newton-Raphson iteration)

- **Jacobian matrices** in least squares adjustment

- **Rate of change** in crustal deformation modeling

- **Curve fitting** for satellite orbits

- **Error propagation** via partial derivatives

## 10. References

- OpenStax Calculus Vol. 1, Chapter 2-3

- MIT OCW 18.01: Single Variable Calculus

- Stewart, J. (2015). *Calculus: Early Transcendentals*

---

*Maintained by AIGIS.*
