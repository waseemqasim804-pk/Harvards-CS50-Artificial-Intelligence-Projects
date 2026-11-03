# Project 3: Crossword Puzzle Generator (Constraint Satisfaction Problems)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-AC--3%20%26%20Backtracking%20Search-red.svg)
![Heuristics](https://img.shields.io/badge/Heuristics-MRV%20%26%20Degree%20Heuristic-yellow.svg)

## 📌 Problem Overview
Generating crossword puzzles is an NP-complete Constraint Satisfaction Problem (CSP). Given a blank grid structure and a dictionary vocabulary, words must fit into intersecting horizontal and vertical slots while satisfying length and overlap constraints.

---

## 🧠 Core AI Concepts & Algorithms
- **Node Consistency:** Restricts variable domains to words with exact matching character lengths.
- **Arc Consistency (AC-3 Algorithm):** Enforces binary constraints between intersecting variables by pruning inconsistent domain values until every arc is consistent.
- **Backtracking Search with Heuristics:**
  - **Minimum Remaining Values (MRV):** Chooses the variable with the fewest remaining candidate words to fail-first and prune bad subtrees quickly.
  - **Degree Heuristic:** Breaks ties by choosing the variable with the highest number of overlapping neighbors.
  - **Least-Constraining Value:** Orders domain values to rule out the fewest choices for neighboring variables.

---

## 📂 Project Structure
```text
06-Crossword-Constraint-Satisfaction/
├── crossword.py   # Variable and Crossword domain representations
├── generate.py    # AC-3 and Backtracking CSP solver with image renderer
├── data/          # Structures (structure0, structure1, structure2) and word lists
└── assets/        # Fonts for generating visual image output
```

---

## 🚀 Quickstart & Usage
```bash
python generate.py data/structure1.txt data/words1.txt output.png
```
*Generates both a clean terminal grid and an exported PNG image crossword!*
