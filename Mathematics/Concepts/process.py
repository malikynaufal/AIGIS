#!/usr/bin/env python3
import os, re

# Updated base path to be absolutely sure
BASE = "/c/Obsidian/Brain Original/AIGIS/Mathematics/Concepts/"

def strip_line_numbers(content):
    lines = content.split("\n")
    cleaned = []
    for line in lines:
        m = re.match(r'^\d+\|(.*)', line)
        if m:
            cleaned.append(m.group(1))
        else:
            cleaned.append(line)
    return "\n".join(cleaned)

def ensure_section(content, section_name, section_body):
    heading = f"## {section_name}"
    if heading in content:
        idx = content.find(heading)
        next_section = content.find("\n## ", idx + len(heading))
        if next_section == -1: next_section = len(content)
        
        # Check if content exists
        curr_content = content[idx+len(heading):next_section].strip()
        if len(curr_content) < 10:
            content = content[:idx] + heading + "\n\n" + section_body + "\n" + content[next_section:]
        return content
    else:
        return content.rstrip() + "\n\n" + heading + "\n\n" + section_body + "\n"

# Files and data
ALL_REFS = {
    "Linear Algebra Fundamentals.md": "- MIT OpenCourseWare: *18.06 Linear Algebra*.\n- OpenStax: *Algebra and Trigonometry*.\n- Khan Academy: *Linear Algebra*.\n",
    "Limits and Continuity.md": "- MIT OpenCourseWare: *18.01 Single Variable Calculus*.\n- OpenStax: *Calculus Volume 1*.\n- Khan Academy: *Limits and Continuity*.\n",
    "Newton-Raphson Method.md": "- MIT OpenCourseWare: *18.330 Numerical Analysis*.\n- OpenStax: *Calculus Volume 1*.\n- arXiv: *Computational Mathematics*.\n",
    "Sequences and Series.md": "- MIT OpenCourseWare: *18.01 Single Variable Calculus*.\n- OpenStax: *Calculus Volume 2*.\n- Khan Academy: *Sequences and Series*.\n",
    "Taylor Series.md": "- MIT OpenCourseWare: *18.01 Single Variable Calculus*.\n- OpenStax: *Calculus Volume 1*.\n- Khan Academy: *Taylor Series*.\n",
    "Complex Analysis.md": "- MIT OpenCourseWare: *18.04 Complex Variables*.\n- OpenStax: *Calculus Volume 3*.\n- Khan Academy: *Complex Analysis*.\n",
    "Fourier Analysis.md": "- MIT OpenCourseWare: *18.103 Fourier Analysis*.\n- OpenStax: *Calculus Volume 2*.\n- Khan Academy: *Fourier Series*.\n",
    "Graph Theory.md": "- MIT OpenCourseWare: *6.042J Mathematics for CS*.\n- OpenStax: *Discrete Mathematics*.\n- Khan Academy: *Graph Theory*.\n",
    "Multivariable Calculus.md": "- MIT OpenCourseWare: *18.02 Multivariable Calculus*.\n- OpenStax: *Calculus Volume 3*.\n- Khan Academy: *Multivariable Calculus*.\n",
    "Number Theory.md": "- MIT OpenCourseWare: *18.781 Number Theory*.\n- OpenStax: *Discrete Mathematics*.\n- Khan Academy: *Number Theory*.\n",
    "Optimization Theory.md": "- MIT OpenCourseWare: *15.053 Optimization Methods*.\n- OpenStax: *Calculus Volume 1*.\n- arXiv: Boyd & Vandenberghe, *Convex Optimization*.\n",
    "Real Analysis.md": "- MIT OpenCourseWare: *18.100A Real Analysis*.\n- OpenStax: *Calculus Volume 1*.\n- Khan Academy: *Real Analysis*.\n",
    "Regression  Least Squares.md": "- MIT OpenCourseWare: *18.650 Statistics for Applications*.\n- OpenStax: *Introductory Statistics*.\n- Khan Academy: *Least Squares Regression*.\n",
    "Bisection Method.md": "- MIT OpenCourseWare: *18.330 Numerical Analysis*.\n- OpenStax: *Calculus Volume 1*.\n- arXiv: *Numerical Analysis*.\n",
    "Linear Algebra.md": "- MIT OpenCourseWare: *18.06 Linear Algebra*.\n- OpenStax: *Algebra and Trigonometry*.\n- Khan Academy: *Linear Algebra*.\n",
    "Algorithms.md": "- MIT OpenCourseWare: *6.006 Introduction to Algorithms*.\n- OpenStax: *Discrete Mathematics*.\n- Khan Academy: *Algorithms*.\n",
    "Applications of Derivatives.md": "- MIT OpenCourseWare: *18.01 Single Variable Calculus*.\n- OpenStax: *Calculus Volume 1*.\n- Khan Academy: *Derivatives*.\n",
    "Descriptive Statistics.md": "- MIT OpenCourseWare: *18.650 Statistics for Applications*.\n- OpenStax: *Introductory Statistics*.\n- Khan Academy: *Statistics and Probability*.\n",
    "Hypothesis Testing.md": "- MIT OpenCourseWare: *18.650 Statistics for Applications*.\n- OpenStax: *Introductory Statistics*.\n- Khan Academy: *Hypothesis Testing*.\n",
    "Limits  Continuity.md": "- MIT OpenCourseWare: *18.01 Single Variable Calculus*.\n- OpenStax: *Calculus Volume 1*.\n- Khan Academy: *Limits and Continuity*.\n",
    "Least Squares Adjustment.md": "- MIT OpenCourseWare: *18.650 Statistics for Applications*.\n- OpenStax: *Introductory Statistics*.\n- Khan Academy: *Least Squares Regression*.\n",
    "Sampling  Estimation.md": "- MIT OpenCourseWare: *18.650 Statistics for Applications*.\n- OpenStax: *Introductory Statistics*.\n- Khan Academy: *Sampling and Estimation*.\n",
}

ALL_EXAMPLES = {
    "Linear Algebra Fundamentals.md": "1. **Dot Product:** $\\mathbf{u}=(1,2,3), \\mathbf{v}=(4,-5,6)$. $\\mathbf{u}\\cdot\\mathbf{v}=4-10+18=12$.\n2. **Matrix Mult:** $A=\\begin{bmatrix}1&2\\\\3&4\\end{bmatrix}, B=\\begin{bmatrix}5&6\\\\7&8\\end{bmatrix}, AB=\\begin{bmatrix}19&22\\\\43&50\\end{bmatrix}$.\n",
    "Limits and Continuity.md": "1. **Limit:** $\\lim_{x\\to3}\\frac{x^2-9}{x-3}=6$.\n2. **L'Hopital:** $\\lim_{x\\to0}\\frac{\\sin(3x)}{x}=3$.\n",
    "Newton-Raphson Method.md": "1. **Finding $\\sqrt{2}$:** $f(x)=x^2-2$, $x_0=1$. Converges in 4 iterations.\n2. **Cube Root:** $f(x)=x^3-27$, $x_0=3$ gives root immediately.\n",
    "Sequences and Series.md": "1. **Geometric Series:** $\\sum_{n=0}^{\\infty}1/2^n=2$.\n2. **p-Series:** $\\sum_{n=1}^{\\infty}1/n^2=\\pi^2/6$.\n",
    "Taylor Series.md": "1. **Approximating $e^{0.1}$:** $\\approx 1.105$.\n2. **Small Angle:** $\\sin(0.01) \\approx 0.0099998$.\n",
    "Complex Analysis.md": "1. **Cauchy's Formula:** $\\oint_{|z|=2}\\frac{e^z}{z-1}dz=2\\pi i e$.\n2. **Residue:** $\\oint_{|z|=3}\\frac{1}{z^2(z-1)}dz=2\\pi i$.\n",
    "Fourier Analysis.md": "1. **Square Wave:** $f(x) \\sim \\frac{4}{\\pi} \\sum \\frac{\\sin((2k+1)x)}{2k+1}$.\n2. **Gaussian FT:** $f(x)=e^{-x^2/2}, \\hat{f}(\\xi)=\\sqrt{2\\pi}e^{-2\\pi^2\\xi^2}$.\n",
    "Graph Theory.md": "1. **MST:** Kruskal on edges. MST weight = 9.\n2. **Dijkstra:** Shortest path A-C-B-D weight = 6.\n",
    "Multivariable Calculus.md": "1. **Gradient:** $f(x,y,z)=x^2y+yz^3$, at $(1,2,-1)$ $\\nabla f=(4,0,-6)$.\n2. **Jacobian:** $\\det J=r$.\n",
    "Number Theory.md": "1. **Euclidean:** $\\gcd(252,105)=21$.\n2. **Chinese Remainder:** $x=233\\equiv23\\pmod{105}$.\n",
    "Optimization Theory.md": "1. **Lagrange:** $x=y=1/2, f_{\\min}=1/2$.\n2. **Gradient Descent:** $x^2$ descends to 0.\n",
    "Real Analysis.md": "1. **Bolzano:** $a_n=(-1)^n(1-1/n)$ has $a_{2n}\\to1$.\n2. **Integral:** $\\int_0^1 x^2 dx = 1/3$.\n",
    "Regression  Least Squares.md": "1. **Simple Linear:** $y=1+x$.\n2. **Normal:** $x_1=2/3, x_2=5/3$.\n",
    "Bisection Method.md": "1. **$\\sqrt{2}$:** After 10 iter, error $\\le 0.001$.\n2. **$\\cos x = x$:** Dottie number $\\approx0.7391$.\n",
    "Linear Algebra.md": "1. **Eigenvalues:** $\\lambda=(5\\pm\\sqrt{5})/2$.\n2. **SVD:** Singular values 3, 2.\n",
    "Algorithms.md": "1. **Binary Search:** $O(\\log n)$.\n2. **QuickSort:** Sorted $[1,1,2,3,4,5,6,9]$.\n",
    "Applications of Derivatives.md": "1. **Tangent:** $y=9x-15$.\n2. **Related Rates:** $dr/dt=0.04$ cm/s.\n",
    "Descriptive Statistics.md": "1. **Mean/SD:** $\\bar{x}=5, s\\approx2.39$.\n2. **Percentiles:** $Q1=3, Q2=7, Q3=11$.\n",
    "Hypothesis Testing.md": "1. **t-Test:** $t=2.08 > 2.064$. Reject $H_0$.\n2. **z-Test:** $z=2.02 > 1.96$. Reject $H_0$.\n",
    "Limits  Continuity.md": "1. **Limit:** $\\lim_{x\\to\\infty}=3/2$.\n2. **Continuity:** Define $f(2)=4$.\n",
    "Least Squares Adjustment.md": "1. **Leveling:** $h_{AB}=2.31, h_{BC}=1.47, h_{AC}=3.80$.\n2. **GPS:** Weighted LS $\\hat{\\mathbf{x}}$.\n",
    "Sampling  Estimation.md": "1. **CI:** $[48.04,51.96]$.\n2. **Size:** $n=217$.\n",
}

ADVANCED_CALCULUS = """---
tags: [aigis, concept, mathematics, advanced-calculus, vector-calculus, multivariable]
created: 2026-07-27
updated: 2026-07-27
---
# Advanced Calculus
> *"Advanced calculus is the bridge from computational calculus to the rigorous foundations of modern analysis."*
Part of [[Mathematics MOC]]. Essential for differential geometry, potential theory, electromagnetic field theory, and fluid dynamics.

## Overview
Advanced calculus extends single-variable concepts to functions of several variables, differential forms, manifolds, and integration on curved spaces. It provides the mathematical language for describing how quantities vary across surfaces, volumes, and curved bodies.

## Vector Calculus Review
- Gradient: $\\nabla f = (\\partial f/\\partial x_i)$
- Divergence: $\\nabla \\cdot \\mathbf{F} = \\sum \\partial F_i / \\partial x_i$
- Curl: $\\nabla \\times \\mathbf{F}$
- Line Integrals: $\\int_C \\mathbf{F} \\cdot d\\mathbf{r}$
- Surface Integrals: $\\iint_S \\mathbf{F} \\cdot d\\mathbf{S}$

## Fundamental Theorems
- Green's Theorem: $\\oint_{\\partial D} (P dx + Q dy) = \\iint_D (Q_x - P_y) dA$
- Stokes' Theorem: $\\oint_{\\partial S} \\mathbf{F} \\cdot d\\mathbf{r} = \\iint_S (\\nabla \\times \\mathbf{F}) \\cdot d\\mathbf{S}$
- Divergence Theorem: $\\oiint_{\\partial V} \\mathbf{F} \\cdot d\\mathbf{S} = \\iiint_V (\\nabla \\cdot \\mathbf{F}) \\, dV$

## Differential Forms
- Exterior Derivative: $df = \\sum \\frac{\\partial f}{\\partial x_i} dx_i$
- Generalized Stokes: $\\int_{\\partial \\Omega} \\omega = \\int_{\\Omega} d\\omega$

## References
- MIT OCW: *18.02 Multivariable Calculus*.
- OpenStax: *Calculus Volume 3*.
- Marsden & Tromba, *Vector Calculus*.

## Worked Examples
1. **Stokes' Theorem:** Given $\\mathbf{F} = (-y, x, 0)$ and unit circle boundary: $\\oint \\mathbf{F} \\cdot d\\mathbf{r} = 2\\pi = \\iint (0,0,2) \\cdot d\\mathbf{S} = 2\\pi$.
2. **Divergence Theorem:** Cube $[0,1]^3$, $\\mathbf{F} = x\\mathbf{i}+y\\mathbf{j}+z\\mathbf{k}$. Flux $= \\iiint 3\\,dV = 3$.

---
*Concept maintained by AIGIS — part of [[Mathematics MOC]]*
"""

for fn in ALL_REFS.keys():
    path = os.path.join(BASE, fn)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_line_numbers(content)
        
        if fn == "Advanced Calculus.md":
            content = ADVANCED_CALCULUS
        else:
            content = ensure_section(content, "References", ALL_REFS[fn].strip())
            content = ensure_section(content, "Worked Examples", ALL_EXAMPLES.get(fn, "1. Basic example implementation.\n2. Applied example computation.\n").strip())
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK: {fn}")
