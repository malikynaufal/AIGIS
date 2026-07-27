---
tags: [aigis, concept, mathematics, statistics, probability, bayes, conditional-probability, independence]
created: 2026-07-27
updated: 2026-07-27
---

# Probability Foundations

## For Geodesy & Measurement Science

**Core Idea:** Probability quantifies uncertainty. In geodesy, it underlies every measurement and estimate — from the distribution of GNSS errors to the reliability of coordinates from least-squares adjustment. This concept covers Bayes' theorem, conditional probability, independence, and the fundamental rules governing random events.

---

## 1. Fundamental Concepts

### 1.1 Sample Space and Events

The **sample space** $\Omega$ is the set of all possible outcomes of a random experiment. An **event** is any subset of $\Omega$.

| Term | Symbol | Meaning |
|------|--------|---------|
| Sure event | $\Omega$ | Always occurs ($P(\Omega) = 1$) |
| Impossible event | $\emptyset$ | Never occurs ($P(\emptyset) = 0$) |
| Complement | $\bar{A}$ or $A^c$ | $A$ does not occur: $P(\bar{A}) = 1 - P(A)$ |
| Union | $A \cup B$ | At least one of $A$ or $B$ occurs |
| Intersection | $A \cap B$ | Both $A$ and $B$ occur |
| Mutually exclusive | $A \cap B = \emptyset$ | Cannot both occur |

### 1.2 Axioms of Probability (Kolmogorov)

1. **Non-negativity:** $P(A) \geq 0$ for every event $A$
2. **Normalisation:** $P(\Omega) = 1$
3. **Additivity:** For pairwise disjoint events $A_1, A_2, \ldots$:
   $$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

All of probability theory follows from these three axioms.

### 1.3 Classical Definition (Equally Likely Outcomes)

For a finite sample space where all outcomes are equally likely:

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{number of outcomes in } A}{\text{total number of outcomes}}$$

---

## 2. Conditional Probability (Peluang Bersyarat)

The probability of event $A$ given that $B$ has occurred:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### 2.1 The Multiplication Rule

$$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$

**Generalised (chain rule):**
$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1\cap A_2)\cdots P(A_n|A_1\cap\cdots\cap A_{n-1})$$

### 2.2 Law of Total Probability

If $\{B_1, B_2, \ldots, B_k\}$ partition $\Omega$ (mutually exclusive and exhaustive):

$$P(A) = \sum_{i=1}^k P(A|B_i)P(B_i)$$

**In geodesy:** Partitioning error sources — GNSS total error = (tropospheric error) + (ionospheric error) + (receiver noise) + (multipath)...

---

## 3. Independence (Kebebasan)

Two events $A$ and $B$ are **independent** if any of the equivalent conditions hold:

$$P(A \cap B) = P(A)P(B)$$
$$P(A|B) = P(A)$$
$$P(B|A) = P(B)$$

**Pairwise vs Mutual independence:**
- **Pairwise:** $P(A_i \cap A_j) = P(A_i)P(A_j)$ for every pair
- **Mutual:** Also $P(A_1 \cap A_2 \cap \cdots \cap A_k) = P(A_1)P(A_2)\cdots P(A_k)$ for every subset

**Independence of random variables:** $f_{XY}(x,y) = f_X(x)f_Y(y)$ (PDF factorises).

**Geodesy importance:** GNSS range measurements to different satellites are approximately independent; leveling setups are independent; but GNSS epoch measurements may be correlated in time.

---

## 4. Bayes' Theorem

The most important formula for updating beliefs with data:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

### 4.1 Expanded Form (Multiple Hypotheses)

Given a partition $\{B_1, \ldots, B_k\}$:

$$P(B_j|A) = \frac{P(A|B_j)P(B_j)}{\sum_{i=1}^k P(A|B_i)P(B_i)}$$

| Term | Name | Meaning |
|------|------|---------|
| $P(B_j)$ | **Prior** | Belief before observing data |
| $P(A\|B_j)$ | **Likelihood** | Probability of data under hypothesis $j$ |
| $P(B_j\|A)$ | **Posterior** | Updated belief after data |
| Denominator | **Evidence** | Normalising constant |

### 4.2 Bayesian vs Frequentist Interpretation

| Aspect | Bayes | Frequentist |
|--------|-------|-------------|
| Probability | Degree of belief | Long-run frequency |
| Parameters | Random variables | Fixed constants |
| Inference | Posterior distribution | Confidence intervals |
| Prior | Required (subjective/objective) | Not used |
| Result | $P(\theta\|\text{data})$ | $P(\text{data}\|\theta)$ |

### 4.3 Conjugate Priors

A prior $\pi(\theta)$ is **conjugate** for a likelihood $f(x|\theta)$ if the posterior $\pi(\theta|x)$ is in the same family as the prior.

| Likelihood | Conjugate Prior | Posterior Parameters |
|------------|----------------|---------------------|
| Normal (known variance) | Normal | $\mu_n = \frac{\mu_0/\sigma_0^2 + n\bar{x}/\sigma^2}{1/\sigma_0^2 + n/\sigma^2}$ |
| Binomial | Beta | $\alpha + k, \beta + n - k$ |
| Poisson | Gamma | $\alpha + \sum x_i, \beta + n$ |

**Geodesy example:** Prior coordinates from a previous survey $\sim \mathcal{N}(\mathbf{x}_0, \mathbf{C}_0)$ combined with new GNSS observations $\sim \mathcal{N}(\mathbf{l}, \mathbf{C}_l)$ produce a posterior estimate combining both information sources.

---

## 5. Random Variables

### 5.1 Types

| Type | Range | Examples | Notation |
|------|-------|----------|----------|
| **Discrete** | Finite/countable set | Number of cycle slips, integer ambiguities | $P(X=k)$ |
| **Continuous** | Real numbers | Coordinates, distances, angles | $f(x)$, PDF |

### 5.2 Probability Mass Function (PMF) — Discrete

$$p_X(k) = P(X = k)$$

Properties: $0 \leq p_X(k) \leq 1$, $\sum_k p_X(k) = 1$

### 5.3 Probability Density Function (PDF) — Continuous

$$P(a < X < b) = \int_a^b f_X(x)\, dx$$

Properties: $f_X(x) \geq 0$, $\int_{-\infty}^{\infty} f_X(x)\, dx = 1$

### 5.4 Cumulative Distribution Function (CDF)

$$F_X(x) = P(X \leq x) = \begin{cases}
\sum_{k \leq x} p_X(k) & \text{(discrete)} \\
\int_{-\infty}^x f_X(t)\, dt & \text{(continuous)}
\end{cases}$$

Properties: non-decreasing, $\lim_{x\to-\infty}F(x)=0$, $\lim_{x\to\infty}F(x)=1$

### 5.5 Moments

| Moment | Definition | Meaning |
|--------|------------|---------|
| Mean $\mu$ | $E[X] = \int x f(x)\, dx$ | Centre |
| Variance $\sigma^2$ | $\text{Var}(X) = E[(X-\mu)^2]$ | Spread |
| Skewness $\gamma_1$ | $E[(X-\mu)^3]/\sigma^3$ | Asymmetry |
| Kurtosis $\gamma_2$ | $E[(X-\mu)^4]/\sigma^4 - 3$ | Tail weight |

---

## 6. Joint, Marginal, and Conditional Distributions

### 6.1 Joint Distribution

$$f_{XY}(x,y) \quad \text{or} \quad P(X=x, Y=y)$$

### 6.2 Marginal Distribution

$$f_X(x) = \int f_{XY}(x,y)\, dy \quad \text{or} \quad P(X=x) = \sum_y P(X=x, Y=y)$$

### 6.3 Conditional Distribution

$$f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)}$$

### 6.4 Law of Total Expectation and Variance

$$E[Y] = E[E[Y|X]]$$

$$\text{Var}(Y) = \text{Var}(E[Y|X]) + E[\text{Var}(Y|X)]$$

---

## 7. Key Inequalities

| Inequality | Formula | Use |
|------------|---------|-----|
| **Markov** | $P(X \geq a) \leq E[X]/a$ | Upper bound on tail probability |
| **Chebyshev** | $P(|X-\mu| \geq k\sigma) \leq 1/k^2$ | Bounds deviations, any distribution |
| **Jensen** | $E[g(X)] \geq g(E[X])$ for convex $g$ | Expectation of functions |
| **Cauchy-Schwarz** | $|E[XY]| \leq \sqrt{E[X^2]E[Y^2]}$ | Correlation bound |

**Chebyshev example:** At least $1 - 1/k^2$ of data lies within $k$ standard deviations of the mean. For $k=2$: at least 75% within $\mu \pm 2\sigma$ (any distribution).

---

## 8. Geodesy Applications

| Concept | Geodetic Application |
|---------|---------------------|
| Conditional probability | $P(\text{correct ambiguity fix given observation residuals})$ |
| Independence | Assumption that GNSS pseudorange measurements are independent between epochs |
| Bayes' theorem | Combining prior coordinates with new survey data |
| Law of total probability | Decomposing GNSS total error into component contributions |
| Chebyshev inequality | Bounding probability of large residuals without normality |

---

## Key Equations

| Equation | Name | Use |
|----------|------|-----|
| $P(A\|B) = P(A\cap B)/P(B)$ | Conditional probability | Updating knowledge |
| $P(A\cap B) = P(A)P(B)$ | Independence test | Check if events are independent |
| $P(A) = \sum P(A\|B_i)P(B_i)$ | Total probability | Decomposing probability |
| $P(B_j\|A) = P(A\|B_j)P(B_j)/\sum P(A\|B_i)P(B_i)$ | Bayes' theorem | Inference |
| $E[Y] = E[E[Y\|X]]$ | Total expectation | Hierarchical models |
| $P(|X-\mu| \geq k\sigma) \leq 1/k^2$ | Chebyshev | Distribution-free bound |

---

## Related Concepts

- [[Descriptive Statistics]] — Empirical moments
- [[Hypothesis Testing]] — Decision theory
- [[Error Propagation]] — Uncertainty of derived quantities
- [[Probability and Statistics for Geodesy]] — Geodetic applications
- [[Mathematical Statistics]] — Advanced theory

---

*Maintained by AIGIS — part of [[Mathematics MOC]]*
