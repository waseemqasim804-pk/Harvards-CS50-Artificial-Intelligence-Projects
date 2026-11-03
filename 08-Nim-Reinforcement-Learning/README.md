# Project 4b: Nim Game AI (Reinforcement Learning & Q-Learning)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Domain](https://img.shields.io/badge/Domain-Reinforcement%20Learning-crimson.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Q--Learning%20(Temporal%20Difference)-black.svg)

## 📌 Problem Overview
Nim is a mathematical game of strategy where two players take turns removing items from distinct piles. The player forced to take the last remaining item loses.

This project implements a self-improving **Reinforcement Learning Agent** using **Q-Learning**. The agent begins with zero knowledge of the game and trains through 10,000 self-play simulations to learn optimal board strategy.

---

## 🧠 Core AI Concepts
- **Q-Learning Update Rule (Bellman Equation):**
  $$Q(s, a) \leftarrow Q(s, a) + \alpha \left( r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right)$$
  - $\alpha = 0.5$ (learning rate)
  - $\gamma = 1.0$ (discount factor)
- **Reward Function:**
  - $+1$ for taking a move that causes the opponent to lose.
  - $-1$ for taking a move that causes the player to lose.
  - $0$ for non-terminal moves.
- **$\epsilon$-Greedy Policy:**
  Balances exploration (trying random actions to discover new states) and exploitation (choosing the action with highest estimated $Q$-value).

---

## 📂 Project Structure
```text
08-Nim-Reinforcement-Learning/
├── nim.py    # Game environment and Q-Learning agent
└── play.py   # CLI launcher for human vs. AI match
```

---

## 🚀 Quickstart & Usage
```bash
python play.py
```
*The agent self-trains for 10,000 games in seconds, then challenges you to an interactive match!*
