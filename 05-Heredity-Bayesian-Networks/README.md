# Project 2b: Heredity (Bayesian Networks & Probabilistic Inference)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Domain](https://img.shields.io/badge/Domain-Uncertainty%20%26%20Bayesian%20Inference-darkgreen.svg)
![Concept](https://img.shields.io/badge/Model-Mendelian%20Genetics-orange.svg)

## 📌 Problem Overview
Assessing genetic risk requires reasoning under uncertainty. This project implements a **Bayesian Network** to infer the probability distribution of mutated *GJB2* genes (responsible for hearing impairment) and hearing impairment traits across family lineages.

---

## 🧠 Core AI Concepts
- **Bayesian Networks:** Directed acyclic graph representing joint probability distributions:
  $$P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
- **Mendelian Inheritance with Mutation Probability:**
  - A parent with 2 copies has $1 - \mu$ chance of passing the gene.
  - A parent with 1 copy has a $50\%$ chance of passing either gene.
  - A parent with 0 copies has a $\mu$ mutation chance ($p = 0.01$).
- **Joint Probability & Normalization:** Calculates the joint distribution for every combination of states and normalizes across observed evidence.

---

## 📂 Project Structure
```text
05-Heredity-Bayesian-Networks/
├── heredity.py   # Bayesian inference engine and probability normalizer
└── data/
    ├── family0.csv
    ├── family1.csv
    └── family2.csv
```

---

## 🚀 Quickstart & Usage
```bash
python heredity.py data/family0.csv
```

### Sample Output:
```text
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
...
```
