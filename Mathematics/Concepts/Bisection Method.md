---
tags: [math, numerical-methods, root-finding, nonlinear-equations]
aliases: [Bisection Method, Binary Search Root Finding]
created: 2026-07-13
updated: 2026-07-27
---

# Bisection Method

> *"The guaranteed-convergence root finder that never fails — it just takes its time."*

---

## 1. The Idea

To find a root of $f(x) = 0 $on an interval$ [a, b] $where $ f(a)f(b) < 0 $ (sign change):

1. Evaluate midpoint $c = \frac{a+b}{2}$
2. Check which subinterval has the sign change
3. Repeat on that subinterval

The interval halves each iteration — convergence is **guaranteed** by the Intermediate Value Theorem.

---

## 2. Algorithm

```
Input: f(x), interval [a,b], tolerance ε, max iterations N
Require: f(a) * f(b) < 0 (sign change)

For n = 1 to N:
 c = (a + b) / 2
 f_c = f(c)

 If |f_c| < ε or (b - a)/2 < ε:
 return c (converged)

 If f(a) * f_c < 0:
 b = c
 Else:
 a = c

Return c (approximate root)
```

---

## 3. Convergence Analysis

### Error Bound

After $n$ iterations:

$$|c_n - r| \leq \frac{b - a}{2^n}

$$ where $ r $ is the true root.

### Iterations for Desired Accuracy

To achieve error $< \varepsilon $:

$$ n \geq \frac{\log(b-a) - \log(\varepsilon)}{\log 2}$$

### Rate

- **Linear convergence** (rate $1/2$)
- One bit of accuracy per iteration
- Slower than Newton, but **unconditionally convergent**

---

## 4. Comparison Table

| Method | Convergence | Requirements | Reliability |
|--------|-------------|--------------|-------------|
| Bisection | Linear ($1/2$) | Sign change only | **Guaranteed** |
| Newton | Quadratic | $ f'$ known, good guess | Can diverge |
| Secant | Superlinear (1.618) | Two initial guesses | No guarantee |
| Brent | Superlinear | Bracketing interval | Best of both worlds |

---

## 5. Practical Considerations

### Stopping Criteria

```python
# Multiple criteria:
if abs(f(c)) < tol: # function value small
 return c
if (b - a) / 2 < tol: # interval small enough
 return c
if n > max_iter: # safety
 return c
```

### Advantages

- **Always converges** if initial bracket is valid
- No derivatives needed
- Simple to implement
- Error bound known a priori

### Disadvantages

- Slow (1 iteration = 1 bit)
- Can't find roots of even multiplicity (no sign change)
- Requires initial bracket with sign change

---

## 6. Geodesy Application

In GNSS positioning, bisection is used for:
- **Integer ambiguity resolution** search (LAMBDA method preprocessing)
- **GNSS satellite visibility** elevation mask calculations
- **Coordinate transformation** inverse problems

---

## 7. Python Implementation

```python
def bisection(f, a, b, tol=1e-10, max_iter=100):
 """Find root of f(x)=0 on [a,b] using bisection."""
 if f(a) * f(b) >= 0:
 raise ValueError("Function must have opposite signs at a and b")

 for i in range(max_iter):
 c = (a + b) / 2
 fc = f(c)

 if abs(fc) < tol or (b - a) / 2 < tol:
 return c

 if f(a) * fc < 0:
 b = c
 else:
 a = c

 return (a + b) / 2
```

---

## 8. References

- Burden, R. L. & Faires, J. D. (2015). *Numerical Analysis*. 10th ed. Cengage.
- Kiusalaas, J. (2013). *Numerical Methods in Engineering with Python*. Cambridge.

See also: [[Newton-Raphson Method]], [[Numerical Methods]], [[Root Finding Algorithms]]