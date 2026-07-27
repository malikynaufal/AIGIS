---
title: "Sistem Kontrol Lanjutan"
subject: "Fisika Pilihan"
tags:
  - control-systems
  - PID
  - state-space
  - stability
  - SKS: 3
---

# FKD214707 — Sistem Kontrol Lanjutan
**Advanced Control Systems** | 3 SKS (Satuan Kredit Semester)

## Overview

Advanced control systems (sistem kontrol lanjutan) provide the theoretical and practical framework for designing controllers that regulate dynamic systems — from seismic isolators and robotic total stations to geophysical instrumentation and satellite attitude control. This course covers classical PID tuning, state-space representation, observer (estimator) design, stability analysis via Lyapunov and root-locus methods, and modern applications in geodetic and geophysical systems.

---

## 1. PID Control (Kontrol PID)

### 1.1 Ideal PID Equation

The proportional-integral-derivative (PID) controller generates a control signal $u(t)$:

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

In the Laplace domain:

$$C(s) = K_p + \frac{K_i}{s} + K_d s$$

| Term (Suku) | Action (Aksi) | Effect (Efek) | Drawback |
|---|---|---|---|
| Proportional ($K_p$) | Proportional to error | Reduces rise time | Steady-state error remains |
| Integral ($K_i$) | Integral of error | Eliminates steady-state error | Overshoot, windup |
| Derivative ($K_d$) | Rate of change | Reduces overshoot, adds damping | Amplifies high-frequency noise |

### 1.2 Ziegler–Nichols Tuning

For a system with critical gain $K_u$ (at sustained oscillation) and critical period $T_u$:

| Controller | $K_p$ | $K_i$ | $K_d$ |
|---|---|---|---|
| P | $0.5 K_u$ | — | — |
| PI | $0.45 K_u$ | $1.2 K_p / T_u$ | — |
| PID | $0.6 K_u$ | $2 K_p / T_u$ | $K_p T_u / 8$ |

### 1.3 Anti-Windup (Pencegahan Windup)

When the actuator saturates ($u_{\min} \leq u \leq u_{\max}$), the integral term accumulates (windup). Anti-windup strategies include:

**Conditional integration**: Stop integrating when $u = u_{\text{sat}}$ and $\text{error} \cdot u_{\text{sat}} > 0$.

**Back-calculation**:

$$\dot{x}_i = \frac{1}{T_t}(u_{\text{sat}} - u) + e(t)$$

where $T_t$ is the tracking time constant.

---

## 2. State-Space Representation (Representasi Ruang状态)

### 2.1 State Equations

A linear time-invariant (LTI) system of order $n$:

$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)$$
$$\mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)$$

where $\mathbf{x} \in \mathbb{R}^n$ is the state vector, $\mathbf{u} \in \mathbb{R}^m$ is the input, and $\mathbf{y} \in \mathbb{R}^p$ is the output.

**Discrete-time form** (used in digital control):

$$\mathbf{x}[k+1] = \mathbf{A}_d \mathbf{x}[k] + \mathbf{B}_d \mathbf{u}[k]$$

### 2.2 Controllability and Observability

**Controllability matrix**:

$$\mathcal{C} = [\mathbf{B} \;\; \mathbf{A}\mathbf{B} \;\; \mathbf{A}^2\mathbf{B} \;\; \cdots \;\; \mathbf{A}^{n-1}\mathbf{B}]$$

System is controllable (terkendali) if $\text{rank}(\mathcal{C}) = n$.

**Observability matrix**:

$$\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}$$

System is observable (teramati) if $\text{rank}(\mathcal{O}) = n$.

### 2.3 Pole Placement (Penempatan Kutub)

Full-state feedback $\mathbf{u} = -\mathbf{K}\mathbf{x}$ places closed-loop poles at desired locations. The Ackermann formula for SISO systems:

$$\mathbf{K} = [0 \;\; 0 \;\; \cdots \;\; 1] \cdot \mathcal{C}^{-1} \cdot \alpha_d(\mathbf{A})$$

where $\alpha_d(s) = \prod_{i=1}^{n}(s - \lambda_i)$ is the desired characteristic polynomial with poles $\lambda_i$.

---

## 3. Observer Design (Desain Pengamat)

### 3.1 Luenberger Observer

When not all states are measured, a Luenberger observer estimates the state:

$$\dot{\hat{\mathbf{x}}} = \mathbf{A}\hat{\mathbf{x}} + \mathbf{B}\mathbf{u} + \mathbf{L}(\mathbf{y} - \mathbf{C}\hat{\mathbf{x}})$$

The observer gain $\mathbf{L}$ is designed so that the estimation error $\mathbf{e} = \mathbf{x} - \hat{\mathbf{x}}$ decays:

$$\dot{\mathbf{e}} = (\mathbf{A} - \mathbf{L}\mathbf{C})\mathbf{e}$$

Poles of $(\mathbf{A} - \mathbf{L}\mathbf{C})$ are placed 2–5× faster than the controller poles.

### 3.2 Kalman Filter

The Kalman filter is the optimal state estimator for linear systems with Gaussian noise:

**Prediction** (prediksi):

$$\hat{\mathbf{x}}_{k|k-1} = \mathbf{A}\hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B}\mathbf{u}_{k-1}$$
$$\mathbf{P}_{k|k-1} = \mathbf{A}\mathbf{P}_{k-1|k-1}\mathbf{A}^T + \mathbf{Q}$$

**Update** (pembaruan):

$$\mathbf{K}_k = \mathbf{P}_{k|k-1}\mathbf{C}^T(\mathbf{C}\mathbf{P}_{k|k-1}\mathbf{C}^T + \mathbf{R})^{-1}$$
$$\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k(\mathbf{y}_k - \mathbf{C}\hat{\mathbf{x}}_{k|k-1})$$
$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k\mathbf{C})\mathbf{P}_{k|k-1}$$

---

## 4. Stability Analysis (Analisis Stabilitas)

### 4.1 Lyapunov Stability

For the autonomous system $\dot{\mathbf{x}} = f(\mathbf{x})$ with equilibrium at the origin:

A system is stable if there exists a positive-definite function $V(\mathbf{x}) > 0$ such that:

$$\dot{V}(\mathbf{x}) = \frac{\partial V}{\partial \mathbf{x}} f(\mathbf{x}) \leq 0$$

$\dot{V} < 0$ → asymptotically stable (stabil asimtotik).

**Lyapunov function for linear systems**: For $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x}$, choose $V = \mathbf{x}^T\mathbf{P}\mathbf{x}$ where $\mathbf{P}$ solves:

$$\mathbf{A}^T\mathbf{P} + \mathbf{P}\mathbf{A} = -\mathbf{Q}$$

The Lyapunov equation for positive $\mathbf{Q}$ has a positive-definite solution $\mathbf{P}$ iff all eigenvalues of $\mathbf{A}$ have negative real parts.

### 4.2 Nyquist Criterion

The Nyquist criterion relates open-loop behavior to closed-loop stability. For a system with open-loop transfer function $L(s)$, the number of unstable closed-loop poles:

$$Z = P - N$$

where $P$ is the number of unstable open-loop poles and $N$ is the number of clockwise encirclements of $(-1, 0)$.

### 4.3 Gain and Phase Margins

- **Gain margin (marjin penguatan)**: Additional gain before instability
- **Phase margin (marjin fasa)**: Additional phase lag before instability; typical design target: 45°–60°

---

## 5. Applications in Geodetic Systems

### 5.1 Active Seismic Isolation

Active isolation platforms for seismometers use PID + state-space control to reject ground vibrations above 0.1 Hz. The plant model:

$$m\ddot{x} + c\dot{x} + kx = F_{\text{actuator}} + F_{\text{ground}}$$

A 3-DOF state-space controller with acceleration feedback achieves >40 dB attenuation above 0.1 Hz.

### 5.2 Case Study: Satellite Attitude Control (Kontrol Sikap Satelit)

Indonesia's LAPAN-A2 satellite uses a reaction wheel + magnetorquer attitude control system. The Euler equations:

$$\mathbf{J}\dot{\boldsymbol{\omega}} + \boldsymbol{\omega} \times (\mathbf{J}\boldsymbol{\omega}) = \boldsymbol{\tau}_{\text{control}} + \boldsymbol{\tau}_{\text{disturbance}}$$

A PID controller with Kalman filter state estimation achieves pointing accuracy of ±0.1° for the multispectral camera, critical for land-use mapping (pemetaan penggunaan lahan) of the Indonesian archipelago.

---

## References

1. Ogata, K. (2010). *Modern Control Engineering*, 5th ed. Prentice Hall.
2. Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2019). *Feedback Control of Dynamic Systems*, 8th ed. Pearson.
3. Åström, K. J., & Murray, R. M. (2021). *Feedback Systems: An Introduction for Scientists and Engineers*, 2nd ed. Princeton University Press.
4. Lewis, F. L., Vlasits, V. L., & Vrabie, D. (2008). *Optimal and Robust Estimation*. CRC Press.
5. Slotine, J.-J. E., & Li, W. (1991). *Applied Nonlinear Control*. Prentice Hall.
6. LAPAN (2020). "LAPAN-A2 Satellite Operations Manual." Jakarta: Lembaga Penerbangan dan Antariksa Nasional.
