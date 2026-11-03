# Project 0b: Tic-Tac-Toe (Adversarial Search & Minimax)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Pygame](https://img.shields.io/badge/GUI-Pygame-yellow.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Minimax%20w%2F%20Alpha--Beta%20Pruning-red.svg)

## 📌 Problem Overview
An unbeatable artificial intelligence agent that plays Tic-Tac-Toe. Using adversarial search techniques, the agent anticipates every possible future game state to determine the mathematically optimal move, ensuring it never loses a game (always wins or forces a draw).

---

## 🧠 Core AI Concepts & Algorithms
- **Minimax Decision Rule:**
  - **MAX Player ($X$):** Seeks to maximize the board utility score ($+1$).
  - **MIN Player ($O$):** Seeks to minimize the board utility score ($-1$).
  - **Tie Game:** Utility score equals $0$.
- **Mathematical Formulation:**
  $$\text{Minimax}(s) = \begin{cases} \text{Utility}(s) & \text{if Terminal}(s) \\ \max_{a \in \text{Actions}(s)} \text{Min-Value}(\text{Result}(s, a)) & \text{if Player}(s) = X \\ \min_{a \in \text{Actions}(s)} \text{Max-Value}(\text{Result}(s, a)) & \text{if Player}(s) = O \end{cases}$$
- **Optimization (Alpha-Beta Pruning / Depth Cutoff):** Avoids evaluating branches that cannot influence the final decision, significantly cutting down state-space exploration.

---

## 📂 Project Structure
```text
01-TicTacToe-Minimax/
├── tictactoe.py           # Core game logic and Minimax adversarial search
├── runner.py              # Interactive Pygame graphical user interface
├── OpenSans-Regular.ttf   # UI typography font
└── requirements.txt       # Dependencies (pygame)
```

---

## 🚀 Quickstart & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Graphical Game
```bash
python runner.py
```
*Choose to play as either $X$ (First Mover) or $O$ (Second Mover) against the AI.*

---

## 🧪 Verification & Robustness
The agent handles all corner cases, terminal detections, and action availability:
- Winner detection across rows, columns, and diagonals.
- Deepcopy state immutability to prevent game state corruption during recursion.
