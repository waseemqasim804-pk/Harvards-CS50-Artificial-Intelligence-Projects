# Project 2a: PageRank (Markov Chains & Random Surfer Model)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Domain](https://img.shields.io/badge/Domain-Probability%20%26%20Graph%20Theory-blueviolet.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Random%20Surfer%20%26%20Iterative%20PageRank-blue.svg)

## 📌 Problem Overview
PageRank is Google's foundational algorithm that ranks web pages based on incoming hyperlink structure. A page is considered important if other important pages link to it.

This project implements two distinct approaches to compute the PageRank distribution across web corpora:
1. **The Random Surfer Model (Monte Carlo Simulation):** Simulates a user navigating the web via links with random teleportation.
2. **Iterative Transition Formulation (Fixed-Point Iteration):** Mathematically solves the recursive PageRank equation until convergence ($\Delta < 0.001$).

---

## 🧠 Mathematical Formulation
For damping factor $d = 0.85$, total pages $N$, and page $p$:
- **Random Surfer Model:**
  $$P(p) = \frac{1 - d}{N} + d \sum_{i \in \text{In}(p)} \frac{P(i)}{|\text{Out}(i)|}$$
- **Dangling Nodes:** Pages without outgoing links are treated as having links to all pages in the corpus.

---

## 📂 Project Structure
```text
04-PageRank-Markov-Chain/
├── pagerank.py   # Transition model, sampling simulation, and iterative solver
├── corpus0/      # 4-page sample graph
├── corpus1/      # 7-page complex web graph
└── corpus2/      # 8-page cyclic web graph
```

---

## 🚀 Quickstart & Usage
```bash
python pagerank.py corpus0
```

### Sample Output:
```text
PageRank Results from Sampling (n = 10000)
  1.html: 0.2215
  2.html: 0.4308
  3.html: 0.2149
  4.html: 0.1328
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2147
  4.html: 0.1362
```
