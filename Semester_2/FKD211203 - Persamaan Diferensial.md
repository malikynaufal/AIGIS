---
code: FKD211203
name: Persamaan Diferensial
SKS: 3
semester: 2
department: Matematika
tags: [mathematics, differential-equations, ODEs, physics-methods]
created: 2026-07-27
---

# FKD211203 — Persamaan Diferensial (ODEs for Physics)

## Course Overview

Differential equations are the language of physics — every fundamental law is expressed as a differential equation. This course introduces ordinary differential equations (ODEs), focusing on analytical techniques and physical applications: oscillatory motion, heat conduction, circuit behavior, and wave propagation.

**Contact Hours:** 3 SKS (2 hours lecture + 1 hour tutorial per week)
**Prerequisites:** Kalkulus I, Fisika Dasar I
**Co-requisites:** Fisika Dasar II, Aljabar Linear

---

## 📋 Topics & Outline

### Unit 1: First-Order ODEs (Weeks 1–5)
- **General form:** dy/dx = f(x,y)
- **Separable equations:** dy/dx = g(x)h(y) → ∫ dy/h(y) = ∫ g(x)dx
- **Linear first-order:** dy/dx + P(x)y = Q(x)
  - Integrating factor method: μ(x) = exp(∫ P(x)dx)
  - Solution: y = (1/μ(x)) ∫ μ(x)Q(x)dx
- **Exact equations:** M(x,y)dx + N(x,y)dy = 0
  - Condition: ∂M/∂y = ∂N/∂x
  - Finding implicit solution F(x,y) = C
- **Substitution methods:** homogeneous equations, Bernoulli equation
- **Physical examples:**
  - Radioactive decay: dN/dt = -λN → N(t) = N₀e^{-λt}
  - Newton's cooling: dT/dt = -k(T - T_env)
  - RC circuit: dq/dt + q/(RC) = ε/R

### Unit 2: Second-Order Linear ODEs (Weeks 6–10)
- **General form:** a(x)y'' + b(x)y' + c(x)y = f(x)
- **Homogeneous equations with constant coefficients:**
  - Characteristic equation: ar² + br + c = 0
  - Three cases: distinct real roots, repeated root, complex roots
  - Solution forms: e^{r₁x}, xe^{rx}, e^{αx}(C₁cos(βx) + C₂sin(βx))
- **Method of undetermined coefficients** for particular solutions
- **Variation of parameters** as general method
- **Physical applications:**
  - **Simple harmonic oscillator:** m(d²x/dt²) + kx = 0
    → ω = √(k/m), x(t) = A cos(ωt + φ)
  - **Damped oscillator:** m\ddot{x} + b\dot{x} + kx = 0
    → Underdamped, critically damped, overdamped
  - **Driven/forced oscillator:** resonance, quality factor Q

### Unit 3: Special Equations and Techniques (Weeks 11–14)
- **Cauchy-Euler equation:** x²y'' + axy' + by = 0
- **Reduction of order**
- **Power series solutions** (Frobenius method)
- **Sturm-Liouville problems** — eigenvalue problems in physics:
  - y'' + λρ(x)y = 0 with boundary conditions
  - Orthogonality of eigenfunctions
  - Applications: quantum mechanics, heat conduction

### Unit 4: Systems of ODEs (Weeks 15–16)
- **Systems of first-order ODEs:** dy/dx = Ay (matrix form)
- **Eigenvalue method:** solution involves eigenvalues of A
- Coupled oscillators: normal modes
- Introduction to nonlinear systems and stability (qualitative)

---

## 🔬 Key ODEs

```
Radioactive decay:    dN/dt = -λN → N = N₀e^{-λt}
Harmonic oscillator:  m\ddot{x} + kx = 0 → ω = √(k/m)
RL Circuit:           L(dI/dt) + RI = ε → τ = L/R
RC Circuit:           R(dq/dt) + q/C = ε → τ = RC
Damped oscillator:    \ddot{x} + 2γ\dot{x} + ω₀²x = 0
Resonance:            \ddot{x} + 2γ\dot{x} + ω₀²x = F₀cos(ωt)/m
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Solve separable, linear, and exact first-order ODEs
2. Solve second-order linear ODEs with constant coefficients
3. Apply ODEs to model physical systems (oscillators, circuits, decay)
4. Analyze coupled oscillators using eigenvalue methods
5. Recognize Sturm-Liouville problems and their importance in physics
6. Use qualitative methods to understand nonlinear behavior

---

## 📚 References

1. Boyce, W.E. & DiPrima, R.C. (2017). *Elementary Differential Equations*, 11th ed. Wiley.
2. Zill, D.G. (2016). *A First Course in Differential Equations*, 11th ed. Cengage.
3. Braun, M. (2013). *Differential Equations and Their Applications*, 4th ed. Springer.
4. MIT OCW 18.03 Differential Equations: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/
5. Arfken, G.B. et al. (2012). *Mathematical Methods for Physicists*, 7th ed. Elsevier.
