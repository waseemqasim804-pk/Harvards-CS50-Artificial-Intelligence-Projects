# Project 1a: Knights & Knaves (Propositional Logic & Inference)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Domain](https://img.shields.io/badge/Domain-Knowledge%20%26%20Reasoning-purple.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Model%20Checking-brightgreen.svg)

## 📌 Problem Overview
In a Knights and Knaves puzzle created by logician Raymond Smullyan:
- **Knights** always tell the truth.
- **Knaves** always lie.

This project formalizes classic logical puzzles into propositional sentences and uses automated **Model Checking** to deduce the identity of each character based strictly on their statements.

---

## 🧠 Core AI Concepts & Logical Representation
- **Propositional Symbols:**
  - $AKnight, AKnave$: Character $A$ is a Knight / Knave.
  - $BKnight, BKnave$: Character $B$ is a Knight / Knave.
  - $CKnight, CKnave$: Character $C$ is a Knight / Knave.
- **Axiomatic Structure of the Game:**
  - Exclusive disjunction (each person is either a Knight or a Knave, but never both):
    $$\text{And}(\text{Or}(AKnight, AKnave), \text{Not}(\text{And}(AKnight, AKnave)))$$
- **Truth Condition (Biconditional equivalence):**
  - A person is a Knight if and only if their statement is true:
    $$AKnight \iff \text{Statement}_A$$
- **Model Checking Algorithm:** Evaluates whether Knowledge Base $\alpha \models \beta$ holds in all possible truth assignments using truth-table enumeration.

---

## 📂 Project Structure
```text
02-Knights-Propositional-Logic/
├── puzzle.py    # Knowledge bases for Puzzles 0, 1, 2, and 3
└── logic.py     # Propositional logic classes (And, Or, Not, Implication, Biconditional)
```

---

## 🚀 Quickstart & Usage
```bash
python puzzle.py
```

### Output:
```text
Puzzle 0:
    A is a Knave
Puzzle 1:
    A is a Knave
    B is a Knight
Puzzle 2:
    A is a Knave
    B is a Knight
Puzzle 3:
    A is a Knight
    B is a Knave
    C is a Knight
```
