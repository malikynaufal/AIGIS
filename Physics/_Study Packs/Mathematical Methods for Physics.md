---
tags: [physics, study-pack, aigis, mathematics, mathematical-methods]
aliases: [Mathematical Methods, Math Methods for Physics]
created: 2026-07-27
updated: 2026-07-27
---

# 📚 Study Pack — Mathematical Methods for Physics
*Mathematics is the language of physics — these are the essential tools.*

---

## 1. Vector Calculus

### Gradient, Divergence, Curl

$$ \nabla f = \frac{\partial f}{\partial x}\hat{x} + \frac{\partial f}{\partial y}\hat{y} + \frac{\partial f}{\partial z}\hat{z}\nabla \cdot \vec{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}\nabla \times \vec{A} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \partial_x & \partial_y & \partial_z \\ A_x & A_y & A_z \end{vmatrix} $ $

### Fundamental Theorems

**Gradient Theorem (Fundamental Theorem for Line Integrals):*
*

$$ \int_C \nabla f \cdot d\vec{l} = f(\vec{r}_b) - f(\vec{r}_a)

$ $

**Divergence Theorem (Gauss's Theorem):*
*

$$ \oint_S \vec{A} \cdot d\vec{S} = \int_V (\nabla \cdot \vec{A}) \, dV

$ $

**Stokes' Theorem:*
*

$$ \oint_C \vec{A} \cdot d\vec{l} = \int_S (\nabla \times \vec{A}) \cdot d\vec{S} $ $

### Vector Identities (Essential)
| Identity | Formula |
|----------|---------|
| Divergence of curl | $ \nabla \cdot (\nabla \times \vec{A}) = 0 $ |
| Curl of gradient | $ \nabla \times (\nabla f) = \vec{0} $ |
| Triple product | $ \nabla(\vec{A} \cdot \vec{B}) = \vec{A} \times (\nabla \times \vec{B}) + \vec{B} \times (\nabla \times \vec{A}) + (\vec{A} \cdot \nabla)\vec{B} + (\vec{B} \cdot \nabla)\vec{A} $ |
| Laplacian of product | $ \nabla^2(fg) = f\nabla^2 g + g\nabla^2 f + 2\nabla f \cdot \nabla g $ |

### Curvilinear Coordinates

**Spherical $ (r, \theta, \phi) $:**

$ $ \nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial f}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial f}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 f}{\partial\phi^2} $$

**Cylindrical $ (\rho, \phi, z) $:**

$ $ \nabla^2 f = \frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho \frac{\partial f}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 f}{\partial\phi^2} + \frac{\partial^2 f}{\partial z^2} $$

### Physics Applications

- **Gravitational field:**$ \vec{g} = \nabla U $, where $ \nabla^2 U = 4\pi G\rho $- **Electromagnetism:**$ \nabla \cdot \vec{E} = \rho/\epsilon_0 $, $ \nabla \times \vec{E} = -\partial\vec{B}/\partial t $- **Fluid dynamics:**$ \nabla \cdot \vec{v} = 0 $ (incompressible),$ \nabla \times \vec{v} = \vec{\omega} $ (vorticity)

- **Heat conduction:**$ \nabla^2 T = \frac{1}{\kappa}\frac{\partial T}{\partial t} $---

## 2. Complex Analysis

### Cauchy-Riemann Equations
If $ f(z) = u(x,y) + iv(x,y) $ is analytic, then

$ $ \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} $$

### Cauchy's Integral Formul
a

$ $ f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} \, dz $$

### Residue Theore
m

$ $ \oint_C f(z) \, dz = 2\pi i \sum_{k} \text{Res}(f, z_k)

$$

**Computing Residues:**

- **Simple pole:**$ \text{Res}(f, z_0) = \lim_{z \to z_0} (z - z_0) f(z) $- **Pole of order $ n $:** $ \text{Res}(f, z_0) = \frac{1}{(n-1)!} \lim_{z \to z_0} \frac{d^{n-1}}{dz^{n-1}}[(z-z_0)^n f(z)] $### Common Physics Applications

- Evaluating real integrals: $ \int_0^{\infty} \frac{dx}{1+x^2} = \frac{\pi}{2} $ (via semicircular contour)

- Green's functions for PDEs

- Dispersion relations (Kramers-Kronig)

- S-matrix theory in scattering

### Laurent Serie
s

$ $ f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n $$

where $ a_n = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-z_0)^{n+1}} dz $---

## 3. Fourier Methods

### Fourier Transform Pairs

$ $ \tilde{f}(\omega) = \int_{-\infty}^{\infty} f(t) \, e^{-i\omega t} \, dtf(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \tilde{f}(\omega) \, e^{i\omega t} \, d\omeg
a

**### Fourier Series (Periodic Functions) **

 f(x) = \sum_{n=-\infty}^{\infty} c_n \, e^{inx/L}c_n = \frac{1}{2L}\int_{-L}^{L} f(x) \, e^{-inx/L} \, dx $$

### Key Properties
| Property | Time Domain | Frequency Domain |
|----------|-------------|------------------|
| Linearity | $ af(t) + bg(t) $ | $ a\tilde{f}(\omega) + b\tilde{g}(\omega) $ |
| Time shift | $ f(t-t_0) $ | $ e^{-i\omega t_0}\tilde{f}(\omega) $ |
| Frequency shift | $ e^{i\omega_0 t}f(t) $ | $ \tilde{f}(\omega - \omega_0) $ |
| Convolution | $ (f * g)(t) $ | $ \tilde{f}(\omega)\tilde{g}(\omega) $ |
| Differentiation | $ f'(t) $ | $ i\omega \tilde{f}(\omega) $ |

### Parseval's Theore
m

$ $ \int_{-\infty}^{\infty} |f(t)|^2 \, dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |\tilde{f}(\omega)|^2 \, d\omega

$$

### Common Transforms
| Function | Transform |
|----------|-----------|
| Gaussian $ e^{-at^2} $ | $ \sqrt{\pi/a} \, e^{-\omega^2/(4a)} $ |
| Rect function $ \text{rect}(t/T) $ | $ T \, \text{sinc}(\omega T/2\pi) $ |
| Delta $ \delta(t-t_0) $ | $ e^{-i\omega t_0} $ |
| Exponential decay $ e^{-at}u(t) $ | $ 1/(a + i\omega) $ |

### Physics Applications

- **Signal processing:** Time-to-frequency analysis of GNSS signals

- **Quantum mechanics:** Position ↔ momentum wavefunctions: $ \psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int\psi(x)e^{-ipx/\hbar}dx $- **Diffraction:** Far-field pattern = Fourier transform of aperture function

- **Heat equation:** Separation via Fourier modes: $ T(x,t) = \sum A_n e^{-\alpha k_n^2 t}\sin(k_n x) $---

## 4. Ordinary Differential Equations (ODEs)

### First-Order Linea
r

$ $ \frac{dy}{dx} + P(x)y = Q(x)

$$

**Solution via integrating factor:**$ \mu = e^{\int P \, dx} $, then $ y = \frac{1}{\mu}\int\mu Q \, dx $.

### Second-Order Linear (Constant Coefficients)

$ ay'' + by' + cy = 0 $ Characteristic equation: $ ar^2 + br + c = 0 $.

- **Real distinct roots $ r_1 \neq r_2 $:** $ y = c_1 e^{r_1 x} + c_2 e^{r_2 x} $- **Repeated root $ r $:** $ y = (c_1 + c_2 x)e^{rx} $- **Complex $ r = \alpha \pm i\beta $:** $ y = e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x) $### Nonhomogeneous: Method of Undetermined Coefficients
For $ ay'' + by' + cy = f(x) $, try particular solution matching the form of $ f(x) $.

### Euler Equation

$ $ x^2 y'' + ax y' + by = 0 $$

Try $ $ y = x^s $: leads to characteristic equation $ s(s-1) + as + b = 0 $.$

### Bessel's Equation

$ $ x^2 y'' + xy' + (x^2 - \nu^2)y = 0 $$

Solutions: Bessel functions $ $ J_\nu(x) $ and $ Y_\nu(x) $.$

### Legendre's Equation

$ $ (1-x^2)y'' - 2xy' + \nu(\nu+1)y = 0 $$

Solutions: Legendre polynomials $ $ P_n(x) $ (regular at $ x = \pm 1 $).$

### Physics Applications

- **Simple harmonic oscillator:** $ \ddot{x} + \omega_2 x = 0 $- **Damped oscillator:**$ \ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0 $- **RLC circuit:**$ L\ddot{q} + R\dot{q} + q/C = V(t) $- **Rocket equation:**$ m\dot{v} = u\dot{m} - mg $ (separable)

---

## 5. Partial Differential Equations (PDEs)

### The Big Three PDEs of Physics

| PDE | Equation | Physics |
|-----|----------|---------|
| **Wave** | $ \nabla^2 u = \frac{1}{v^2}\frac{\partial^2 u}{\partial t^2} $ | Vibrations, EM waves, acoustics |
| **Heat/Diffusion** | $ \nabla^2 u = \frac{1}{\kappa}\frac{\partial u}{\partial t} $ | Temperature, diffusion |
| **Laplace** | $ \nabla^2 u = 0 $ | Electrostatics, steady-state heat |
| **Poisson** | $ \nabla^2 u = f $ | Gravitation, electrostatics with sources |
| **Schrödinger** | $ i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi $ | Quantum mechanics |

### Separation of Variables
Assume $ u(x,y,t) = X(x)Y(y)T(t) $, substitute, divide through — each factor depends on a different variable, so each must equal a constant.

**Example (1D heat equation on rod):**
$ T(t) = e^{-\alpha k^2 t} $, $ X(x) = \sin(kx) $ (for $ X(0) = X(L) = 0 $).

### Sturm-Liouville Theory

$ $ \frac{d}{dx}\left[p(x)\frac{dy}{dx}\right] + [q(x) + \lambda w(x)]y = 0

$ Eigenfunctions $\{y_n\} $ are orthogonal with respect to weight $ w(x) $: $

$ $ \int_a^b y_m(x) y_n(x) w(x) \, dx = 0 \quad (m \neq n)

$$

This generalizes Fourier series, Legendre, and Bessel expansions.

### Green's Functions
Solve $ \mathcal{L}G(x, x') = \delta(x - x') $, then:

$ $

u(x) = \int G(x, x') f(x') \, dx' $$ | Equation | Green's Function (3D, free space) |
|----------|----------------------------------|
| Poisson | $ G = -\frac{1}{4\pi r} $ |
| Helmholtz | $ G = -\frac{e^{ikr}}{4\pi r} $ |
| Heat | $ G = \frac{1}{(4\pi\kappa t)^{3/2}}e^{-r^2/(4\kappa t)} $ |

---

## 6. Special Functions in Physics

### Bessel Functions $ J_n(x) $- Solutions to cylindrical problems (waves in cylinders, heat in circular plates)

- **Orthogonality:**$ \int_0^a J_n(\alpha_{nm}r/a) J_n(\alpha_{np}r/a) \, r \, dr = 0 $ for $ m \neq p $- **Asymptotic:** $ J_n(x) \sim \sqrt{\frac{2}{\pi x}}\cos\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right) $ for $ x \gg 1 $### Legendre Polynomials $ P_n(x) $- Solutions to spherical problems (electrostatics, quantum mechanics)

- **Rodrigues formula:** $ P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n $- **Orthonormality:**$ \int_{-1}^{1} P_m(x)P_n(x) \, dx = \frac{2}{2n+1}\delta_{mn} $- First few: $ P_0 = 1 $, $ P_1 = x $, $ P_2 = \frac{1}{2}(3x^2 - 1) $### Associated Legendre Functions $ P_n^m(x) $ Used in spherical harmonic expansion: $ Y_l^m(\theta,\phi) = N_{lm}P_l^m(\cos\theta)e^{im\phi} $### Hermite Functions $ H_n(x) $- Quantum harmonic oscillator eigenfunctions: $ \psi_n(x) = N_n e^{-x^2/2} H_n(x) $- **Recursion:** $ H_{n+1}(x) = 2xH_n(x) - 2nH_{n-1}(x) $### Laguerre Polynomials $ L_n(x) $- Hydrogen atom radial wavefunctions: $ R_{nl}(r) \propto e^{-r/na}L_{2l+1}^{2l+1}(2r/na) $### Airy Functions $ \text{Ai}(x) $, $ \text{Bi}(x) $- Solutions near turning points (WKB approximation in QM, optics caustics)

---

## 7. Calculus of Variations

### Euler-Lagrange Equation
For functional $ J[y] = \int_{x_1}^{x_2} F(x, y, y') \, dx $:

$ $ \frac{\partial F}{\partial y} - \frac{d}{dx}\frac{\partial F}{\partial y'} = 0

$$

### Applications

- **Brachistochrone:** Fastest descent curve → cycloid

- **Geodesics on sphere:** Great circle

- **Lagrangian mechanics:** $ S = \int L \, dt $ (principle of least action)

- **Minimal surface:** Soap films →$ \nabla \cdot \left(\frac{\nabla z}{\sqrt{1+|\nabla z|^2}}\right) = 0 $### Multiple Variable
s

$ $ \frac{\partial F}{\partial y_i} - \frac{d}{dx}\frac{\partial F}{\partial y_i'} = 0 \quad \text{for each } y_i

$$

### With Constraints (Lagrange Multipliers)
Add constraint $ g(x, y_1, \ldots, y_n) = 0 $ using multiplier $ \lambda(x) $:

$ $ \frac{\partial F}{\partial y_i} - \frac{d}{dx}\frac{\partial F}{\partial y_i'} + \lambda\frac{\partial g}{\partial y_i} = 0

$$ ---

## 8. Tensors and Differential Geometry

### Tensor Basics
A rank-2 tensor $ T_{ij} $ transforms as

$ $ T'_{ij} = \frac{\partial x'^i}{\partial x^k}\frac{\partial x'^j}{\partial x^l}T_{kl} $$

### Metric Tenso
r

$ ds^2 = g_{ij}dx^i dx^j $ $ - Cartesian: $ g_{ij} = \delta_{ij} $- Spherical: $ g_{rr} = 1 $, $ g_{\theta\theta} = r^2 $, $ g_{\phi\phi} = r^2\sin^2\theta $### Christoffel Symbol $
s

$ $ \Gamma^k_{ij} = \frac{1}{2}g^{kl}\left(\frac{\partial g_{li}}{\partial x^j} + \frac{\partial g_{lj}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l}\right)

$$

### Covariant Derivativ
e

$ $ \nabla_j V^i = \frac{\partial V^i}{\partial x^j} + \Gamma^i_{jk}V^k

$$

### Riemann Curvature Tenso
r

$ $ R^i_{\ jkl} = \frac{\partial\Gamma^i_{jl}}{\partial x^k} - \frac{\partial\Gamma^i_{jk}}{\partial x^l} + \Gamma^i_{mk}\Gamma^m_{jl} - \Gamma^i_{ml}\Gamma^m_{jk} $$

### Physics Applications

- **General relativity:** Einstein field equations $ R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4}T_{\mu\nu} $- **Continuum mechanics:** Stress tensor $ \sigma_{ij} $, strain tensor $ \epsilon_{ij} $- **Crystallography:** Inertia tensor, dielectric tensor

---

## 9. Linear Algebra for Physics

### Eigenvalue Problem
s

$ $ A\vec{v} = \lambda\vec{v} $$

- **Characteristic equation:**$ \det(A - \lambda I) = 0 $- **Diagonalization:** $ A = PDP^{-1} $ where $ D $ = diagonal eigenvalues

### Hermitian Operators

- Real eigenvalues → observable quantities in QM

- Orthogonal eigenvectors → complete basis
-$ A^\dagger = A $: $ \langle\phi|A\psi\rangle = \langle A\phi|\psi\rangle $### Common Physics Matrices
| Matrix | Use |
|--------|-----|
| Pauli matrices $ \sigma_x, \sigma_y, \sigma_z $ | Spin-1/2 algebra |
| Rotation matrix $ R(\theta) $ | 2D rotations, SO(3) |
| Inertia tensor $ I_{ij} $ | Rigid body dynamics |
| Moment of inertia matrix | Principal axes diagonalize it |

---

## Key Formulas Summary

| Formula | Name | Use |
|---------|------|-----|
| $ \oint \vec{A}\cdot d\vec{l} = \int(\nabla\times\vec{A})\cdot d\vec{S} $ | Stokes' theorem | EM, fluid circulation |
| $ \oint\vec{A}\cdot d\vec{S} = \int\nabla\cdot\vec{A}\,dV $ | Divergence theorem | Gauss's law |
| $ \tilde{f}(\omega) = \int f(t)e^{-i\omega t}dt $ | Fourier transform | Spectral analysis |
| $ \oint f(z)dz = 2\pi i\sum\text{Res} $ | Residue theorem | Complex integrals |
| $ \nabla^2 u + k^2 u = 0 $ | Helmholtz equation | Wave phenomena |

---

## Problems
1. Verify Stokes' theorem for $ \vec{A} = y\hat{x} - x\hat{y} $ on a unit disk.
2. Evaluate $ \int_0^{\infty}\frac{\cos x}{x^2+1}dx $ using the residue theorem.
3. Find the Fourier transform of $ f(t) = e^{-a|t|} $ and verify Parseval's theorem.
4. Solve the wave equation on a string with fixed ends using separation of variables.
5. Show that Legendre polynomials are orthogonal using Rodrigues' formula.
6. Compute the Christoffel symbols for 2D polar coordinates.
7. Solve the 1D heat equation on $ [0,L] $ with boundary conditions $ u(0,t)=u(L,t)=0$.

---

*Study Pack maintained by AIGIS — part of [[Physics MOC]]*
