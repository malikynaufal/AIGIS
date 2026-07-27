---
tags: [math, numerical-methods, root-finding, nonlinear-equations, calculus]
aliases: [Newton-Raphson Method, Newton's Method]
created: 2026-07-13
updated: 2026-07-27
---

# Newton-Raphson Method

> *"The quadratic convergence champion — when it works, it works spectacularly."*

---

## 1. Derivation

Starting from Taylor expansion around $x_n$:

$$f(x_{n+1}) = f(x_n) + f'(x_n)(x_{n+1} - x_n) + O((x_{n+1}-x_n)^2)$$

Set $f(x_{n+1}) = 0$ and neglect higher-order terms:

$$0 \approx f(x_n) + f'(x_n)(x_{n+1} - x_n)$$

Solving for $x_{n+1}$:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

---

## 2. Algorithm

```
Input: f(x), f'(x), initial guess x₀, tolerance ε, max iterations N

For n = 0 to N-1:
    f_xn = f(x_n)
    f_prime_xn = f'(x_n)
    
    If f_prime_xn == 0:
        raise "Zero derivative — cannot continue"
    
    x_{n+1} = x_n - f_xn / f_prime_xn
    
    If |x_{n+1} - x_n| < ε or |f(x_{n+1})| < ε:
        return x_{n+1}

Raise "Did not converge"
```

---

## 3. Convergence Analysis

### Quadratic Convergence

If $f'(r) \neq 0$ and $f$ is $C^2$ near root $r$:

$$|x_{n+1} - r| \approx \frac{|f''(r)|}{2|f'(r)|} |x_n - r|^2$$

Error squares each iteration — **doubles correct digits**.

### Conditions for Quadratic Convergence

| Condition | Why |
|-----------|-----|
| $f'(r) \neq 0$ | Simple root (not multiple) |
| $f \in C^2$ | Second derivative exists |
| $x_0$ sufficiently close | Basin of attraction |
| $f'$ bounded away from 0 | No flat spots near root |

### Multiple Roots

If $f(x) = (x-r)^m g(x)$ with $g(r) \neq 0$:
- Convergence becomes **linear** with rate $1 - \frac{1}{m}$
- Modified Newton: $x_{n+1} = x_n - m \frac{f(x_n)}{f'(x_n)}$ restores quadratic

---

## 4. Failure Modes

| Failure Mode | Cause | Fix |
|--------------|-------|-----|
| Divergence | $x_0$ outside basin of attraction | Hybrid methods, better initial guess |
| Oscillation | $f'$ near zero, periodic function | Damping, secant fallback |
| Division by zero | $f'(x_n) = 0$ | Check derivative, perturb |
| Slow convergence | Multiple root | Modified Newton, or use deflation |

---

## 5. Geometric Interpretation

Each iteration:
1. Draw tangent line to $f(x)$ at $(x_n, f(x_n))$
2. Find where tangent crosses x-axis
3. That x-intercept is $x_{n+1}$

```mermaid
graph LR
    A[x₀] --> B[Draw tangent]
    B --> C[x₁ = x₀ - f(x₀)/f'(x₀)]
    C --> D[Draw new tangent]
    D --> E[x₂ = x₁ - f(x₁)/f'(x₁)]
    E --> F[Converge to root]
```

---

## 6. Multidimensional Newton

For system $F(x) = 0$ where $F: \mathbb{R}^n \to \mathbb{R}^n$:

$$x_{k+1} = x_k - J_F(x_k)^{-1} F(x_k)$$

where $J_F$ is the $n \times n$ Jacobian matrix.

**Cost:** $O(n^3)$ per iteration for linear solve — use quasi-Newton (Broyden) for large $n$.

---

## 7. Practical Safeguards

```python
def newton(f, df, x0, tol=1e-10, max_iter=50, damping=True):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            # Perturb or fallback
            x += 1e-6
            continue
            
        step = fx / dfx
        
        # Damping for stability
        if damping and abs(step) > 1:
            step *= 0.5
            
        x_new = x - step
        
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    
    raise RuntimeError("Newton did not converge")
```

---

## 8. Geodesy Application

### 7-Parameter Helmert Transformation

Solving for translation, rotation, scale:
- Iterative Newton solves nonlinear system
- Initial guess from linear approximation
- Converges in 3-5 iterations typically

### GNSS Pseudorange Linearization

$$f(\mathbf{x}) = \sqrt{(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2} - \rho_i$$

Newton-Raphson on system of 4+ satellites for positioning.

---

## 9. Comparison with Other Methods

| Method | Order | Function Evals/Iter | Derivative | Robustness |
|--------|-------|---------------------|------------|------------|
| Bisection | 1 | 1 | No | ★★★★★ |
| Secant | 1.618 | 1 | No | ★★★☆☆ |
| Newton | 2 | 1 | Yes | ★★☆☆☆ |
| Halley | 3 | 1 | Yes (2nd) | ★★☆☆☆ |

---

## 10. References

- Demidovich, B. P. & Maron, I. A. (1987). *Computational Mathematics*. Mir.
- Traub, J. F. (1982). *Iterative Methods for the Solution of Equations*. Chelsea.

See also: [[Bisection Method]], [[Secant Method]], [[Numerical Methods]], [[Least Squares Adjustment]]