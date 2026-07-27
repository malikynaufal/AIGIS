---
title: "Instrumentasi Geofisika"
subject: "Fisika Pilihan"
tags:
 - geophysics
 - instrumentation
 - seismology
 - gravimetry
 - magnetometry
 - SKS: 3
---

# FKD214701 — Instrumentasi Geofisika
**Geophysical Instrumentation** | 3 SKS (Satuan Kredit Semester)

## Overview

Geophysical instrumentation (instrumen geofisika) encompasses the suite of sensors, data loggers, and field systems used to measure physical properties of the Earth — seismic wavefields, gravitational acceleration, magnetic fields, electrical resistivity, and thermal gradients. This course surveys the operating principles, construction, calibration, and field deployment of these instruments, with emphasis on how measurement physics constrains instrument design and data quality.

---

## 1. Seismometers (Seismometer)

### 1.1 Operating Principle

A seismometer is a damped harmonic oscillator whose mass displacement relative to the ground is proportional to ground acceleration over the instrument's passband. For a horizontal instrument with natural period $T_0 = 2\pi\sqrt{L/g} $and damping ratio $\xi$:

$$\ddot{x} + 2\xi\omega_0\dot{x} + \omega_0^2 x = -\ddot{u}(t)$$where $\ddot{u}(t) $is ground acceleration and $x $is the relative displacement of the proof mass.

| Component | Function (Fungsi) | Typical Material |
|---|---|---|
| Proof mass ( massa uji ) | Responds to inertial forces | Brass, copper alloy |
| Spring ( pegas ) | Restoring force; sets natural period | Be-Cu or quartz fiber |
| Damping element (peredam) | Controls $Q = 1/(2\xi)$; prevents ringing | Eddy-current or viscous oil |
| Displacement transducer | Converts $x $to electrical signal | LVDT, capacitive bridge, optical |

### 1.2 Broadband vs. Short-Period

- **Broadband seismometers** (e.g., Streckeistle STS-2, Nanometrics Trillium) achieve flat velocity response from ~120 s to >50 s, using force-feedback (servo) architectures.

- **Short-period instruments** (e.g., Mark L-4C, 4.5 Hz geophone) are passive geophones used in exploration seismology with natural frequencies of 1–100 Hz.

### 1.3 Transfer Function

The seismometer's output voltage $V(\omega) $relates to ground velocity $\dot{u}(\omega) $via
:

$$V(\omega) = H(\omega) \cdot \dot{u}(\omega)$$where the instrument response $H(\omega) $is characterized by poles and zeros in the Laplace domain. Typical calibration yields
:

$$H(s) = \frac{A \cdot (s - z_1)(s - z_2) \cdots}{(s - p_1)(s - p_2) \cdots} $$Correcting raw data requires deconvolution of $H(s)$— a step handled by the SEED (Standard for the Exchange of Earthquake Data) metadata.

---

## 2. Gravimeters (Gravimeter)

### 2.1 Absolute vs. Relative Gravimeters

- **Absolute gravimeters** measure $g $directly via free-fall interferometry: a corner-cube reflector falls in vacuum, and its position is tracked by laser interferometry. The measurement equation is
:

$$g = \frac{2(z_2 - z_1)}{(t_2 - t_1)^2} $$The MICRO-G LaCoste FG5 achieves accuracy $\sigma_g \approx 1\;\mu\text{Gal} $($1\;\mu\text{Gal} = 10^{-8}\;\text{m/s}^2$).

- **Relative gravimeters** (LaCoste-Romberg, Scintrex CG-6) use a zero-length spring mechanism to measure gravity *differences* between stations. The LaCoste-Romberg equation of motion:

$$mg = k \cdot l + \text{beam tilt corrections} $$### 2.2 Tidal Corrections

Gravity observations must be corrected for solid Earth tides (pasut). The tidal acceleration is
:

$$g_{\text{tidal}}(t) = \sum_{i} A_i \cos(\omega_i t + \phi_i)$$with principal tidal constituents $M_2$(period 12.42 h, amplitude ~50 μGal) and $S_2$(12.00 h).

### 2.3 Field Calibration Table

| Parameter | CG-6 (Scintrex) | FG5-250 (Micro-G) |
|---|---|---|
| Type (Jenis) | Relative | Absolute |
| Resolution | 1 μGal | 0.1 μGal |
| Accuracy | 5 μGal | 1 μGal |
| Drift | 0.5 μGal/day | 0 μGal/day |
| Weight | 8 kg | 120 kg |
| Measurement time | 1 min/station | 30 min/station |

---

## 3. Magnetometers (Magnetometer)

### 3.1 Fluxgate Magnetometer

A fluxgate (pengubah fluks) uses a high-permeability ferromagnetic core driven to saturation by an AC excitation field. The external ambient field $H_{\text{ext}} $shifts the saturation timing, producing a second-harmonic voltage proportional to $H_{\text{ext}} $:

$$V_{\text{out}}(2f) \propto H_{\text{ext}} \cdot \sin(2\omega t)$$Sensitivity: typically 0.01 nT; bandwidth: DC–1 kHz. Used widely in ground surveys and satellite missions (e.g., Swarm).

### 3.2 Proton Precession Magnetometer

Exploits Larmor precession of protons in kerosene or water
:

$$f_L = \frac{\gamma_p}{2\pi} \cdot |B| $$where $\gamma_p = 42.577 $MHz/T is the proton gyromagnetic ratio. For Earth's field ($\sim 50\,000 $nT),$f_L \approx 2.13 $kHz. Resolution: ~0.1 nT.

### 3.3 Optical Pumping Magnetometer

Alkali-vapor (cesium, rubidium) magnetometers achieve sensitivity$< 0.001 $nT using quantum spin-exchange relaxation effects. They are the basis for aeromagnetic surveys (pengukuran aeromagnetik).

---

## 4. Electrical Resistivity Meters (Tahanan Kelistrikan)

### 4.1 Basic Survey Configuration

The four-electrode Wenner array has equally-spaced electrodes at spacing $a$. The apparent resistivity is:

$$\rho_a = 2\pi a \frac{\Delta V}{I} $$| Array | Geometric Factor $K$ | Sensitivity Pattern |
|---|---|---|
| Wenner | $2\pi a$ | Good vertical resolution |
| Schlumberger | $\pi \frac{L(L+a)}{a} $ | Good lateral coverage |
| Dipole-Dipole | $\pi n(n+1)(n+2)a$ | Excellent for profiling |
| Pole-Dipole | $2\pi n(n+1)a$ | Asymmetric; requires remote electrode |

### 4.2 Induced Polarization (Polarisasi Terinduksi)

In time-domain IP, the voltage decay after current shutoff is measured
:

$$\text{IP chargeability} \; m = \frac{1}{V_0}\int_{t_1}^{t_2} V(t)\,dt$$

Typical values range from 1–1000 mV/V. IP is critical for mineral exploration (eksplorasi mineral) in volcanic terrain common across Indonesia.

---

## 5. Data Loggers and Field Systems (Pencatat Data)

Modern data loggers (e.g., Nanometrics Digitizer, REF TEK 130, Campbell Scientific CR1000) provide:

- **Sampling rates**: 1 Hz (seismic network) to 200 kHz (microseismic monitoring)

- **ADC resolution**: 24-bit (seismometers), 16-bit (geophysical sensors)

- **Timing**: GPS-disciplined oscillator with $\sigma_t < 1\;\mu\text{s} $

- **Storage**: SD cards (up to 256 GB), telemetry via 4G/satellite

- **Power**: 12 V lead-acid or LiFePO4 batteries; solar panel recharge

### 5.1 Case Study: BMKG Seismic Network

Indonesia's BMKG (Badan Meteorologi Klimatologi dan Geofisika) operates ~180 broadband seismic stations using Nanometrics Meridian systems with 100 sps sampling, GPS timing, and real-time telemetry via VSAT to the Jakarta data center. The network's purpose (tujuan) is earthquake and tsunami monitoring for the Indonesian archipelago.

---

## References

1. Shearer, P. M. (2009). *Introduction to Seismology*, 2nd ed. Cambridge University Press.
2. Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*, 2nd ed. Cambridge University Press.
3. Wielandt, E. (2012). "Seismometer Design," in *New Manual of Seismological Observatory Practice*. GFZ German Research Centre for Geosciences.
4. Lacoste, L. J. B. (1967). "Surface Gravity Measurements Based on the Zero-Length Spring Principle," *Geophysics*, 32(3), 457–463.
5. Frischkorn, H., & Scheingraber, H. (2001). "Magnetometers," in *Magnetotellurics in the Context of the MT-SEM Impedance*. Springer.
6. CG-6 Autograv User Guide, Scintrex Ltd. (2020).
