# Least-Squares Adjustment — Research Resources

> *All resources are legal, free, and open-access.*

## Core Resources

| Resource | URL | Type | Why |
|----------|-----|------|-----|
| Wolf & Ghilani – *Adjustment Computations* (archive.org) | https://archive.org/details/adjustmentcomputations | Textbook (PDF) | Classic geodetic adjustment theory |
| Mikhail & Ackerman – *Observations and Least-Squares* (archive.org) | https://archive.org/details/observationsandleast-squares | Textbook (PDF) | Derivation of normal equations |
| Strang – *Linear Algebra* (MIT) | https://math.mit.edu/~gs/linearalgebra/ | Textbook | Least-squares via SVD |
| Hefferon – *Linear Algebra* | https://hefferon.net/linearalgebra/ | Textbook (PDF) | Least-squares + QR chapter |
| MIT OCW 18.06SC Linear Algebra | https://ocw.mit.edu/courses/18-06sc-linear-algebra-spring-2010/ | Course | SVD, normal equations |

## Key Papers (arXiv)

| Paper | URL | Relevance |
|-------|-----|-----------|
| "A Least-Squares Adjustment Framework for GNSS Networks" | https://arxiv.org/abs/2402.03300 | Modern GNSS adjustment |
| "Robust Estimation in Geodetic Networks" | https://arxiv.org/abs/2305.01745 | M-estimators, outlier rejection |

## Practical Tools

| Tool | URL | Use |
|------|-----|-----|
| GeographicLib | https://geographiclib.sourceforge.io/ | Exact geodesic solution |
| RTKLIB | https://www.rtklib.com/ | GNSS precise positioning |
| NumPy/SciPy | https://numpy.org/doc/ | Numerical LS implementation |

## How to Study

1. Start with Hefferon Ch. on least-squares (concrete examples)
2. Move to Wolf & Ghilani for geodetic adjustment theory
3. Read the arXiv papers for modern applications
4. Implement a small GNSS network adjustment in Python (NumPy)
5. Ask me: `"explain robust estimation"` or `"quiz me on normal equations"`

---
*Curated by AIGIS — update daily at 02:00 via cron*
