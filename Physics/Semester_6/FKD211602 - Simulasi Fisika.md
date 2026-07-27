---
code: FKD211602
name: Simulasi Fisika
SKS: 3
semester: 6
department: Fisika
tags: [physics, simulation, monte-carlo, computational, numerical-methods]
created: 2026-07-27
---

# FKD211602 — Simulasi Fisika

## Course Overview

Computational physics — using computers to simulate physical systems that are too complex for analytical solution. This course covers Monte Carlo methods, molecular dynamics, particle simulations, and GPU computing, empowering students to model real physics problems computationally.

**Contact Hours:** 3 SKS (1 hour lecture + 2 hours lab per week)
**Prerequisites:** Pemrograman Lanjutan, Analisis Numerik, Statistika Dasar
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Monte Carlo Methods (Weeks 1–5)

- **Random number generation:** pseudo-random, seeds, quality testing

- **Monte Carlo integration:**
 - Area/volume estimation by random sampling
 - Variance reduction techniques: importance sampling, antithetic variates
 ```
 I ≈ (V/N) Σ f(x_i), σ² = (V²/N)[(1/N)Σf²_i - (Σf_i/N)²]
 ```

- **Metropolis algorithm** for statistical mechanics:
 - Sample Boltzmann distribution P ∝ exp(-E/kT)
 - Markov chain Monte Carlo (MCMC) — detailed balance condition

- **Applications:** Ising model, integral evaluation, parameter estimation

- **Law of Large Numbers** in action: convergence of MC estimates

### Unit 2: Molecular Dynamics (Weeks 6–9)

- **Classical MD simulation:** integrate Newton's laws for N particles
 ```
 r(t+Δt) = 2r(t) - r(t-Δt) + F(t)/m · Δt² (Verlet algorithm)
 ```

- **Interatomic potentials:** Lennard-Jones (12-6), Morse potential
 ```
 V(r) = 4ε[(σ/r)¹² - (σ/r)⁶]
 ```

- **Ewald summation** for long-range forces (electrostatics)

- **Periodic boundary conditions**

- **Thermostats and barostats:** controlling T, P in simulations

- **Ensemble generation:** NVE, NVT (Nosé-Hoover), NPT

- **Analysis:** radial distribution function g(r), diffusion coefficient

- **Software tools:** LAMMPS, GROMACS (overview)

### Unit 3: Particle Simulations (Weeks 10–13)

- **N-body simulation:** gravitational/solar system dynamics
 - Time-stepping: adaptive (Bulirsch-Stoer), symplectic (leapfrog)
 - **Tree codes** and **fast multipole method** for O(N log N) gravity

- **Plasma physics simulations:** PIC (particle-in-cell) method

- **Radiation transport:** Monte Carlo radiation shielding calculations

- **Geophysical applications:**
 - Seismic wave propagation simulation
 - Groundwater flow modeling
 - Climate system modeling (overview)

### Unit 4: Advanced Topics and Projects (Weeks 14–16)

- **GPU computing** for parallel simulations (CUDA overview)
 ```python
 # CUDA pseudocode for particle update
 i = threadIdx.x + blockIdx.x * blockDim.x
 if i < N:
 forces[i] = compute_force(i, positions, N)
 ```

- **Machine learning in physics simulations:** neural network potentials

- **Uncertainty quantification** in computational models

- **Visualization** of simulation results

- **Final project:** choose a simulation (N-body, Monte Carlo, MD) and present results

---

## 🔬 Key Algorithms

```
Monte Carlo: I ≈ (V/N) Σ f(x_i)
Metropolis: Accept move if exp(-ΔE/kT) > rand()
Verlet (MD): r(t+Δt) = 2r(t) - r(t-Δt) + a(t)Δt²
Leapfrog: v(t+Δt/2) = v(t-Δt/2) + a(t)Δt
Lennard-Jones: V(r) = 4ε[(σ/r)¹² - (σ/r)⁶]
```

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Implement Monte Carlo integration and understand its convergence
2. Perform Markov Chain Monte Carlo sampling for statistical mechanics
3. Build a molecular dynamics simulation using Verlet integration
4. Set up N-body gravitational simulations with appropriate time-stepping
5. Analyze simulation data (radial distribution functions, thermodynamic averages)
6. Apply computational techniques to geophysical and physical research problems

---

## 📚 References

1. Tuckerman, M. (2010). *Statistical Mechanics: Theory and Molecular Simulation*. Oxford.
2. Allen, M.P. & Tildesley, D.J. (2017). *Computer Simulation of Liquids*, 2nd ed. Oxford.
3. Landau, R.H. & Binder, K. (2014). *A Guide to Monte Carlo Simulations in Statistical Physics*, 4th ed. Cambridge.
4. Hockney, R.W. & Eastwood, J.W. (1988). *Computer Simulation Using Particles*. CRC Press.
5. TALENT course: Computational Physics (free lecture notes): http://compphysics.github.io/ComputationalPhysics/doc/
