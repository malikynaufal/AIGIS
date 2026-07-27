---
code: FKD211105
name: Pengantar Pemrograman
SKS: 2
semester: 1
department: Informatika
tags: [programming, python, scientific-computing, introduction]
created: 2026-07-27
---

# FKD211105 — Pengantar Pemrograman

## Course Overview

Introduction to programming using Python — the dominant language in scientific computing and physics research. Students learn computational thinking and Python fundamentals, applying them immediately to physics problems: plotting trajectories, solving equations numerically, and analyzing experimental data.

**Contact Hours:** 2 SKS (1 hour lecture + 1 hour lab per week)
**Prerequisites:** None
**Co-requisites:** Kalkulus I

---

## 📋 Topics & Outline

### Unit 1: Programming Fundamentals (Weeks 1–4)
- Why programmers use Python: readability, libraries, community
- **Variables and data types:** int, float, str, bool
- **Arithmetic operators:** +, -, *, /, //, %, **
- Input/output: `input()`, `print()`, f-strings
- **Control flow:** if/elif/else, comparison operators
- **Loops:** `for` loops with `range()`, `while` loops
- String manipulation and slicing
- Coding style: PEP 8, meaningful variable names

### Unit 2: Data Structures and Functions (Weeks 5–8)
- **Lists:** indexing, slicing, append, list comprehension
- **Dictionaries:** key-value pairs, iteration
- **Tuples** and immutability
- **Functions:** `def`, parameters, return values, scope
- **Docstrings** and function documentation
- Lambda functions: `lambda x: x**2`
- Error handling: `try/except`
- Modular programming: importing libraries, `import math`

### Unit 3: Scientific Python (Weeks 9–12)
- **NumPy:** arrays, vectorized operations, linear algebra
  ```python
  import numpy as np
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])
  print(np.dot(a, b))  # 32
  ```
- **Matplotlib:** plotting data, customizing graphs
  ```python
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2*np.pi, 100)
  plt.plot(x, np.sin(x))
  plt.xlabel('x')
  plt.ylabel('sin(x)')
  plt.title('Sine Wave')
  plt.show()
  ```
- Reading/writing data files (CSV, text)
- Basic numerical methods: bisection, Euler method

### Unit 4: Physics Applications (Weeks 13–16)
- **Projectile motion simulation:**
  ```python
  import numpy as np
  g = 9.81
  v0, theta = 50, np.radians(45)
  t = np.linspace(0, 2*v0*np.sin(theta)/g, 100)
  x = v0 * np.cos(theta) * t
  y = v0 * np.sin(theta) * t - 0.5 * g * t**2
  plt.plot(x, y)
  ```
- Numerical integration (trapezoidal rule)
- Solving equations numerically (Newton's method)
- Data fitting with `scipy.optimize.curve_fit`
- Final project: physics simulation of choice

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Write, run, and debug Python programs using fundamental constructs
2. Use NumPy for array operations and linear algebra computations
3. Create publication-quality plots with Matplotlib
4. Apply programming to solve basic physics problems numerically
5. Read, process, and visualize experimental data
6. Collaborate using version control (Git basics)

---

## 📚 References

1. Downey, A.B. (2015). *Think Python*, 2nd ed. O'Reilly. (Free at greenteapress.com)
2. Langtangen, H.P. (2016). *A Primer on Scientific Programming with Python*, 5th ed. Springer.
3. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly. (Free at jakevdp.github.io)
4. Python Tutorial: https://docs.python.org/3/tutorial/
5. NumPy User Guide: https://numpy.org/doc/stable/user/index.html
