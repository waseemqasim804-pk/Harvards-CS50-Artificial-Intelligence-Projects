# Project 1b: Minesweeper (Knowledge-Based Inference)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Pygame-yellow.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Logical%20Subset%20Inference-teal.svg)

## 📌 Problem Overview
Minesweeper is a classic puzzle game where players uncover cells without detonating hidden mines. When a safe cell is clicked, it reveals a number indicating how many neighboring cells contain mines.

This project builds an automated AI agent that models Minesweeper knowledge as logical sentences, performs continuous deduction to infer known safe cells and known mines, and makes calculated risk decisions when forced to guess.

---

## 🧠 Core AI Concepts & Inference Rules
- **Logical Sentence Representation:**
  A sentence consists of a set of undetermined neighboring cells and an integer count of mines:
  $$\text{Sentence}(\text{cells}, \text{count})$$
- **Basic Inferences:**
  - If $\text{count} = 0$, every cell in $\text{cells}$ is guaranteed **SAFE**.
  - If $\text{count} = |\text{cells}|$, every cell in $\text{cells}$ is guaranteed a **MINE**.
- **Subset Inference Rule:**
  If sentence $S_1 = (\text{cells}_1, \text{count}_1)$ and sentence $S_2 = (\text{cells}_2, \text{count}_2)$ where $\text{cells}_1 \subseteq \text{cells}_2$:
  $$S_{\text{new}} = (\text{cells}_2 - \text{cells}_1, \text{count}_2 - \text{count}_1)$$
  This deduction iteratively derives new sentences, revealing hidden mines and safe moves.

---

## 📂 Project Structure
```text
03-Minesweeper-Knowledge-Inference/
├── minesweeper.py   # Game engine, Sentence representation, and MinesweeperAI agent
├── runner.py        # Interactive Pygame graphical board
├── assets/          # Sprites (flags, mines, fonts)
└── requirements.txt # Dependencies (pygame)
```

---

## 🚀 Quickstart & Usage
```bash
pip install -r requirements.txt
python runner.py
```
*Click **"AI Move"** to watch the AI deduce safe moves and clear the board autonomously!*
