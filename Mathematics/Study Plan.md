---
tags: [aigis, study-plan, mathematics, planning]
created: 2026-07-13
updated: 2026-07-27
---

# Mathematics Study Plan — 8-Semester Roadmap

**Purpose:** Structured learning path for mathematics across 8 semesters
**Target:** UGM Teknik Geodesi — Studi Komputer (S.Kom)

## 🗺️ Full Progression

```mermaid
graph TD
 S1[Semester 1: Foundations] --> S2[Semester 2: Core Techniques]
 S2 --> S3[Semester 3: Advanced Methods]
 S3 --> S4[Semester 4: Computational]
 S4 --> S5[Semester 5: Applications]
 S5 --> S6[Semester 6: Advanced Applications]
 S6 --> S7[Semester 7: Specialization]
 S7 --> S8[Semester 8: Capstone]

 S1 --> |Calculus I| [[Derivatives]]
 S1 --> |Linear Algebra| [[Linear Algebra Fundamentals]]
 S2 --> |Calculus II| [[Integrals]]
 S2 --> |ODEs| [[Differential Equations]]
 S3 --> |Real Analysis| [[Real Analysis]]
 S3 --> |Probability| [[Probability Foundations]]
 S4 --> |Num Methods| [[Numerical Methods]]
 S4 --> |Complex Analysis| [[Complex Analysis]]
 S5 --> |Optimization| [[Optimization Theory]]
 S5 --> |Graph Theory| [[Graph Theory]]
 S6 --> |Machine Learning| [[Stochastic Processes]]
 S7 --> |Deep Learning| [[Topology]]
```

## 📅 Semester 1 — Foundations (6 SKS math)

### Primary Goals
- [ ] Master differential calculus (limits, derivatives, applications)
- [ ] Build linear algebra fundamentals (vectors, matrices, determinants)
- [ ] Establish statistical intuition (probability, distributions)

### Weekly Rhythm
| Day | Focus | Duration |
|-----|-------|----------|
| Mon | Calculus — new topic | 2 hrs |
| Tue | Linear Algebra — new topic | 2 hrs |
| Wed | Statistics — new topic | 2 hrs |
| Thu | Problem practice (all 3) | 2 hrs |
| Fri | Review + preview | 1.5 hrs |
| Sat | Deep practice (weakest area) | 3 hrs |
| Sun | Rest + light preview | 1 hr |

### Key Concepts
[[Limits Continuity]] → [[Derivatives]] → [[Applications of Derivatives]] → [[Linear Algebra Fundamentals]] → [[Probability Foundations]] → [[Probability Distributions]]

### Milestones
- [ ] **Week 4:** Pass all derivative rules quiz
- [ ] **Week 8:** Solve 3×3 linear systems by hand; compute determinants
- [ ] **Week 12:** Complete probability distributions problem set
- [ ] **Week 16:** Final exam readiness checklist

### Resources
- OpenStax Calculus Vol 1
- MIT OCW 18.01SC (Calculus I)
- Khan Academy Linear Algebra
- 3Blue1Brown: Essence of Linear Algebra

---

## 📅 Semester 2 — Core Techniques (5 SKS math)

### Primary Goals
- [ ] Master integration techniques and series
- [ ] Solve ODEs (first and second order)
- [ ] Deepen linear algebra (eigenvalues, SVD)

### Weekly Rhythm
| Day | Focus | Duration |
|-----|-------|----------|
| Mon | Calculus II — integration, series | 2 hrs |
| Tue | Differential Equations — theory | 2 hrs |
| Wed | Linear Algebra Advanced — eigenvalues | 2 hrs |
| Thu | Problem practice | 2 hrs |
| Fri | Review + cross-connections | 1.5 hrs |
| Sat | Project work + software | 3 hrs |
| Sun | Rest + preview | 1 hr |

### Key Concepts
[[Integrals]] → [[Sequences and Series]] → [[Taylor Series]] → [[Differential Equations]] → [[LU Decomposition]] → [[QR Factorization]] → [[Cholesky Decomposition]]

### Milestones
- [ ] **Week 4:** Master all integration techniques (substitution, parts, partial fractions)
- [ ] **Week 8:** Solve second-order ODEs with initial conditions
- [ ] **Week 12:** Compute eigenvalues and eigenvectors of 4×4 matrices
- [ ] **Week 16:** Pass comprehensive final

---

## 📅 Semester 3 — Advanced Methods (6 SKS math)

### Primary Goals
- [ ] Master vector calculus (gradient, divergence, curl)
- [ ] Understand real analysis foundations (sequences, continuity, compactness)
- [ ] Apply probability theory rigorously

### Weekly Rhythm
| Day | Focus | Duration |
|-----|-------|----------|
| Mon | Vector Calculus — theory | 2 hrs |
| Tue | Real Analysis — proofs | 2 hrs |
| Wed | Probability — theorems | 2 hrs |
| Thu | Problem sets (all 3) | 2 hrs |
| Fri | Review + cross-connections | 1.5 hrs |
| Sat | Deep work on proofs | 3 hrs |
| Sun | Rest + preview | 1 hr |

### Key Concepts
[[Multivariable Calculus]] → [[Advanced Calculus]] → [[Real Analysis]] → [[Probability Foundations]] (rigorous) → [[Differential Equations]] (PDE intro)

### Milestones
- [ ] **Week 4:** Compute line/surface integrals, apply Stokes' theorem
- [ ] **Week 8:** Write epsilon-delta proofs for continuity
- [ ] **Week 12:** Prove Central Limit Theorem (statement level)
- [ ] **Week 16:** Integration project

---

## 📅 Semester 4 — Computational Methods (12 SKS math)

### Primary Goals
- [ ] Implement numerical algorithms (root-finding, quadrature, linear solvers)
- [ ] Derive MLE, construct confidence intervals, perform hypothesis tests
- [ ] Work with groups, rings, finite fields
- [ ] Evaluate complex integrals using residues

### Weekly Rhythm
| Day | Focus | Duration |
|-----|-------|----------|
| Mon | Numerical Methods — algorithms | 2 hrs |
| Tue | Mathematical Statistics — theory | 2 hrs |
| Wed | Abstract Algebra — algebraic structures | 2 hrs |
| Thu | Complex Analysis — residues, mappings | 2 hrs |
| Fri | Problem sets (all 4) | 3 hrs |
| Sat | Review + code implementations | 2 hrs |
| Sun | Rest + preview | 1 hr |

### Key Concepts
[[Numerical Methods]] → [[Bisection Method]] → [[Newton-Raphson Method]] → [[Descriptive Statistics]] → [[Hypothesis Testing]] → [[Sampling Estimation]] → [[Number Theory]] → [[Abstract Algebra]] → [[Complex Analysis]]

### Milestones
- [ ] **Week 4:** Implement Newton-Raphson and compare convergence rates
- [ ] **Week 8:** Derive MLE for normal/gamma distributions
- [ ] **Week 12:** Find residues and evaluate real integrals via contour integration
- [ ] **Week 16:** Complete cross-course project

---

## 📅 Semester 5 — Applications (15 SKS math)

### Primary Goals
- [ ] Solve ODEs/PDEs numerically; implement SVD
- [ ] Analyze graphs, networks, spectral properties
- [ ] Formulate and solve LP/NLP optimization problems
- [ ] Build ML models and AI algorithms
- [ ] Process images and reconstruct 3D scenes

### Key Concepts
[[Numerical Methods]] (advanced) → [[Graph Theory]] → [[Optimization Theory]] → [[Stochastic Processes]] (intro)

### Milestones
- [ ] **Week 4:** Implement RK4 and compare with Euler
- [ ] **Week 8:** Apply Dijkstra's to a GNSS network graph
- [ ] **Week 12:** Solve a constrained optimization with KKT
- [ ] **Week 16:** Complete integration project

---

## 📅 Semester 6 — Advanced Applications (15 SKS)

### Primary Goals
- [ ] Formulate and solve LP/MIP problems (operations research)
- [ ] Design Monte Carlo experiments with variance reduction
- [ ] Build supervised/unsupervised ML pipelines
- [ ] Apply spatial filtering and FFT-based image processing
- [ ] Parallelize computation for large-scale problems

### Key Concepts
[[Optimization Theory]] (advanced) → [[Stochastic Processes]] → [[Fourier Analysis]] (applications) → [[Numerical Methods]] (parallel)

### Milestones
- [ ] **Week 4:** Solve LP with simplex method
- [ ] **Week 8:** Implement MCMC for Bayesian inference
- [ ] **Week 12:** Build SVM classifier on geodetic data
- [ ] **Week 16:** Final integration project

---

## 📅 Semester 7 — Specialization (8 SKS)

### Primary Goals
- [ ] Define capstone research problem and methodology
- [ ] Master PCA, factor analysis, clustering (multivariate stats)
- [ ] Build and train deep neural networks (CNN, RNN, transformers)
- [ ] Apply ethical frameworks to AI/geodesy

### Key Concepts
[[Topology]] (intro) → [[Metric Spaces]] → Deep Learning → [[Stochastic Processes]] (advanced)

### Milestones
- [ ] **Week 4:** Literature review and methodology chapter draft
- [ ] **Week 8:** Implement PCA and clustering on real dataset
- [ ] **Week 12:** Build CNN for satellite image classification
- [ ] **Week 16:** Capstone progress report

---

## 📅 Semester 8 — Capstone (8 SKS)

### Primary Goals
- [ ] Complete research thesis (Skripsi)
- [ ] Demonstrate mathematical rigor in chosen domain
- [ ] Present results professionally
- [ ] Community service (KKN)

### Key Concepts: Synthesis of all prior semesters

### Milestones
- [ ] **Week 4:** Complete experimental results
- [ ] **Week 8:** Draft thesis chapters 1-4
- [ ] **Week 12:** Final revision and submission
- [ ] **Week 16:** Defense preparation

---

## 🎯 Success Habits

### Daily Routine
1. **Morning (30 min):** Review flashcards — formulas, definitions
2. **Afternoon (2 hrs):** New material — lectures, reading
3. **Evening (1.5 hrs):** Practice problems — minimum 10 per topic

### Active Techniques
- **Feynman Method:** Teach concepts to yourself out loud
- **Spaced Repetition:** Review old topics at increasing intervals
- **Problem Breadth:** Solve diverse problem types, not just similar ones
- **Error Journal:** Track mistakes, revisit regularly
- **Cross-linking:** Connect each new concept to at least 2 prior concepts

---

## 📊 Progress Tracking

### Weekly Self-Assessment

| Week | Topic Mastery (1-5) | Problems Solved | Gaps Identified | Next Week Focus |
|------|---------------------|-----------------|-----------------|-----------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

### Monthly Review
1. What can I now solve that I couldn't at start of month?
2. Which concepts feel intuitive vs. require memorization?
3. What real geodetic problems can I approach with what I've learned?
4. What should I review before next month?

---

## 🔗 Math-Geodesy Connections

| Math Topic | Geodesy Application |
|------------|-------------------|
| Derivatives | Rate of change in measurements, slope, curvature |
| Integrals | Area, volume, mass of Earth |
| Matrices | Coordinate transformations, LS adjustment |
| Vectors | 3D positioning, satellite geometry |
| Probability | Error analysis, confidence intervals |
| Statistics | Network quality, blunder detection |
| Complex Analysis | Potential theory, conformal mapping |
| Fourier Analysis | Signal processing, spectral analysis of tides |
| Graph Theory | Survey network design, routing |
| Optimization | GNSS ambiguity resolution, network design |
| Abstract Algebra | Cryptographic protocols for GNSS |

---
*Last updated: 2026-07-27*