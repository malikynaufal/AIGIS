---
name: Physics_Inbox
tags: [inbox, physics, capture, fleeting-notes]
created: 2026-07-27
---

# 📥 Physics Inbox

> *Catch-all entry point for physics-related ideas, questions, and fleeting notes. Items here are temporary — they will be processed into permanent notes or moved when clarified.*

---

## ➕ Quick Capture (New Ideas)

**2026-07-27**
- [ ] What is the physical mechanism behind the ionospheric delay being proportional to 1/f²?
- [ ] Derive the relativistic clock correction for GPS from both SR and GR — step by step.
- [ ] How does the Coriolis effect influence ocean current patterns in the Indonesian Throughflow?
- [ ] Why do quartz crystals oscillate? (piezoelectricity × mechanical resonance)
- [ ] Connect: gravitational potential → spherical harmonics → EGM2008 geoid model
- [ ] Konsep Lense-Thirring effect (frame dragging) — relevance for satellite gravimetry?
- [ ] Can we explain the molecular geometry of H₂O using quantum mechanics?
- [ ] Write a Python simulation of a simple pendulum with damping and driving force

---

## ❓ Questions to Investigate

### Mechanics
- Why does a spinning bicycle wheel resist tilting? (gyroscopic precession)
- Why is the Roche limit ≈ 2.44× planetary radius?
- What determines the Q factor of a damped harmonic oscillator?

### Electromagnetism
- Why does a transformer core need to be ferromagnetic, not just conductive?
- What is physically happening during electrical breakdown? (is it Paschen's law?)
- How does an antenna actually radiate? (hint: accelerating charges)

### Quantum
- Why does quantum tunneling probability decrease exponentially with barrier width?
- What does "the wave function collapses" actually mean?
- How does STM achieve atomic resolution if the tip is not perfectly sharp?

### Geophysics / Geodesy
- What causes the free-air gravity correction to be 0.3086 mGal/m?
- Why does the ionosphere affect L1 and L2 GPS frequencies differently?
- How does the Saastamoinen tropospheric delay model work?

---

## 📎 Links to Process

- Paper: "Relativistic effects in GPS" — N. Ashby, Living Rev. Relativity
- Conference: EGU General Assembly 2026 — geophysics sessions
- Tutorial: "Solving the 1D Schrödinger equation numerically" — YouTube
- Book chapter: Goldstein — scattering theory (chapter 3)
- Dataset: EGM2020 gravity model coefficients — need to download
- Software: Try GMT for free-air anomaly maps of Java

---

## 🔍 Research Leads

1. **Quantum gravimeters** — using atom interferometry for precise g measurement. How does this compare to classical (falling corner cube) gravimeters?
2. **GNSS radio occultation** — using GPS signals through Earth's limb for atmospheric profiling. Relevant for atmospheric physics and geodesy!
3. **Geoid in Indonesia** — significant discrepancies between EGM2008 and local gravimetric data. Could be a capstone research topic.
4. **Ionospheric scintillation** near the geomagnetic equator (Indonesia is on it!) — affects GNSS accuracy.

---

## 📅 Study Plan / To-do

- [ ] Review: Maxwell's equations in integral and differential forms
- [ ] Practice: Lagrangian mechanics — solve the double pendulum numerically
- [ ] Read: Chapter 5 of Griffiths QM — harmonic oscillator
- [ ] Code: Monte Carlo simulation of 2D Ising model
- [ ] Prepare: Lab report for RC circuit experiment
- [ ] Watch: Feynman lectures vol. II — 20 minutes/day
- [ ] Read: One paper per week from JGR or J. Geodesy

---

## 📝 Temporary Notes

**Damped oscillator response:**
```
ω_d = √(ω₀² - γ²)   (damped frequency)
Q = ω₀/(2γ)          (quality factor)
τ = 1/γ              (decay time constant)
```
Check against my Python simulation — was getting τ wrong.

**Spherical harmonics expansion:**
The Earth's gravity potential:
```
V(r,θ,φ) = (GM/r) Σ (a/r)^ℓ Σ P_ℓm(cos θ)[C_ℓm cos mφ + S_ℓm sin mφ]
```
Degree ℓ = 2, m = 0 gives oblateness (J₂). Need to understand why.

---

## 🔄 Processing Workflow

```
Inbox → Clarify → File as Permanent Note → Tag → Link to MOC
```

1. Items stay in inbox for max 1 week
2. If unclear for 30 days → delete or move to archive
3. Quantum/GR notes → Concepts folder
4. Course-specific → Semester folders
5. Questions → turn into concept explanations in Concepts/
6. Code snippets → Resources/scripts

---

## 🗄️ Archive

*Items older than 30 days are moved to `_Inbox/_processed/`*

---

*Last updated: 2026-07-27*
