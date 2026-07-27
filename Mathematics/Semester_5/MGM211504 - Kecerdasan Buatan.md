---
title: MGM211504 - Kecerdasan Buatan (Artificial Intelligence)
type: course
semester: 5
sks: 3
tags: [mathematics, artificial-intelligence, machine-learning, semester-5]
created: 2026-07-27
---

# MGM211504 - Kecerdasan Buatan (Artificial Intelligence)

> *"AI is the new electricity."* — Andrew Ng
> **SKS:** 3 | **Semester:** 5 | **Prerequisite:** [[Optimization Theory]], [[Probability Foundations]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | AI Overview | History, types, applications |
| 2 | Search Algorithms | BFS, DFS, A* |
| 3 | Constraint Satisfaction | Backtracking, CSP |
| 4 | Game Theory | Minimax, alpha-beta pruning |
| 5 | Uncertainty | Bayesian networks, inference |
| 6 | Decision Theory | Utility, decision networks |
| 7 | Markov Decision Processes | Value iteration, policy iteration |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Machine Learning Intro | Supervised, unsupervised, RL |
| 10 | Linear Regression | Gradient descent, regularization |
| 11 | Classification | Logistic regression, SVM, trees |
| 12 | Neural Networks | Perceptron, backpropagation |
| 13 | Deep Learning | CNN, RNN intro |
| 14 | Applications | AI in geodesy, remote sensing |
| 15 | Final Review | Integration project |

## 📚 Mathematical Foundations

### Linear Regression

$$\hat{y} = w^T x + b, \quad \text{minimize } \frac{1}{n}\|Xw - y\|^2$$

### Logistic Regression

$$P(y=1|x) = \sigma(w^T x) = \frac{1}{1 + e^{-w^T x}}$$

### Neural Network (Single Layer)

$$h = \sigma(Wx + b), \quad \text{output} = \sigma(W' h + b')$$

where $\sigma(z) = \frac{1}{1+e^{-z}}$ is the sigmoid function.

### Backpropagation

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \sigma'(z) \cdot \frac{\partial z}{\partial w}$$

Chain rule applied recursively through layers.

## 📐 Geodesy Application

- **Land cover classification:** CNN on satellite imagery
- **Deformation prediction:** RNN/LSTM on time series
- **Point cloud processing:** Deep learning on LiDAR data
- **GNSS positioning:** Neural network for multipath mitigation

## 🎯 Practice Problems

1. Implement A* search for a grid world.
2. Derive gradient of logistic regression loss.
3. Build a simple neural network and train on MNIST.
4. Compare linear regression vs. neural network on geodetic data.
5. Implement policy iteration for a simple MDP.

## 📖 References

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*. Pearson.
- Goodfellow, I. et al. (2016). *Deep Learning*. MIT Press (free online).
- Bishop, C.M. (2006). *Pattern Recognition and Machine Learning*. Springer.

---
*See also: [[Optimization Theory]], [[Probability Foundations]], [[Probability Distributions]]*
