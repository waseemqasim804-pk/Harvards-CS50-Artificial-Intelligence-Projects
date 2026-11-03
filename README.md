# 🧠 Harvard CS50AI: Artificial Intelligence with Python — Master Portfolio

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Harvard CS50 AI](https://img.shields.io/badge/Harvard%20University-CS50%20AI-A51C30?style=for-the-badge&logo=harvard&logoColor=white)](https://cs50.harvard.edu/ai/)
[![12 Complete Projects](https://img.shields.io/badge/Projects-12%20%2F%2012%20Completed-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white)]()
[![Tested & Graded](https://img.shields.io/badge/CS50%20Grade-100%25%20Verified-success?style=for-the-badge&logo=githubactions&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> A comprehensive portfolio of **12 Artificial Intelligence projects** covering the complete theoretical foundations and practical implementations of modern AI — from classical search algorithms, logical reasoning, and probabilistic graphical models to reinforcement learning, convolutional vision networks, and transformer attention mechanisms.

---

## 📑 Table of Contents
- [Curriculum & Projects Matrix](#-curriculum--projects-matrix)
- [Projects Overview & Highlights](#-projects-overview--highlights)
  - [0. Search](#0-search)
  - [1. Knowledge](#1-knowledge)
  - [2. Uncertainty](#2-uncertainty)
  - [3. Optimization](#3-optimization)
  - [4. Learning](#4-learning)
  - [5. Neural Networks](#5-neural-networks)
  - [6. Language](#6-language)
- [Resume & CV Impact Bullet Points](#-resume--cv-impact-bullet-points)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Technologies & Tooling](#-technologies--tooling)
- [License](#-license)

---

## 🗺 Curriculum & Projects Matrix

| # | Project | Domain | Key Algorithms & Principles | Tech Stack | Status |
|:---:|:---|:---|:---|:---|:---:|
| **0a** | [**Degrees**](./00-Degrees-Search) | Graph Search | Breadth-First Search (BFS), Shortest Path, Bipartite Graphs | Python, CSV | `100% Verified` |
| **0b** | [**Tic-Tac-Toe**](./01-TicTacToe-Minimax) | Adversarial Search | Minimax Algorithm, $\alpha$-$\beta$ Pruning, Utility Theory | Python, Pygame | `100% Verified` |
| **1a** | [**Knights**](./02-Knights-Propositional-Logic) | Knowledge Representation | Propositional Logic, Model Checking, Truth Tables, Entailment | Python | `100% Verified` |
| **1b** | [**Minesweeper**](./03-Minesweeper-Knowledge-Inference) | Logical Inference | Knowledge-Based Agents, Propositional Subset Inference | Python, Pygame | `100% Verified` |
| **2a** | [**PageRank**](./04-PageRank-Markov-Chain) | Uncertainty & Probability | Random Surfer Markov Model, Iterative Transition Matrix, Damping Factor | Python, Math | `100% Verified` |
| **2b** | [**Heredity**](./05-Heredity-Bayesian-Networks) | Probabilistic Modeling | Bayesian Networks, Joint Probability Distribution, Mendelian Genetics | Python | `100% Verified` |
| **3**  | [**Crossword**](./06-Crossword-Constraint-Satisfaction) | Optimization | Constraint Satisfaction (CSP), AC-3 Arc Consistency, MRV & Degree Heuristics | Python, PIL | `100% Verified` |
| **4a** | [**Shopping**](./07-Shopping-Predictor-ML) | Supervised Learning | $k$-Nearest Neighbors ($k$-NN), Sensitivity & Specificity, Feature Engineering | Python, scikit-learn | `100% Verified` |
| **4b** | [**Nim**](./08-Nim-Reinforcement-Learning) | Reinforcement Learning | Temporal Difference Q-Learning, $\epsilon$-Greedy Policy, Bellman Equation | Python | `100% Verified` |
| **5**  | [**Traffic**](./09-Traffic-Recognition-CNN) | Computer Vision / Deep Learning | Convolutional Neural Networks (CNN), Max-Pooling, Dropout Regularization | Python, TensorFlow, OpenCV | `100% Verified` |
| **6a** | [**Parser**](./10-Parser-Natural-Language-Processing) | Natural Language Processing | Context-Free Grammars (CFG), Syntactic Trees, Noun Phrase (NP) Chunking | Python, NLTK | `100% Verified` |
| **6b** | [**Attention**](./11-Attention-Transformers-Visualization) | Modern Transformers & LLMs | Masked Language Modeling (BERT), Self-Attention Tensors, Attention Heatmaps | Python, HuggingFace, PyTorch | `100% Verified` |

---

## 🔍 Projects Overview & Highlights

### 0. Search
* **[Degrees](./00-Degrees-Search):** Models Hollywood film co-stars as an undirected graph. Implements Breadth-First Search (BFS) using a frontier queue to compute the exact shortest degrees of separation between any two actors from IMDb data.
* **[Tic-Tac-Toe](./01-TicTacToe-Minimax):** Engineered an unbeatable AI opponent utilizing the Minimax decision rule with Alpha-Beta pruning, computing optimal recursive game-tree trajectories in an interactive Pygame GUI.

### 1. Knowledge
* **[Knights](./02-Knights-Propositional-Logic):** Encodes Raymond Smullyan's logical puzzles into formal propositional logic sentences. Uses recursive model checking to evaluate truth conditions and deduce true character identities.
* **[Minesweeper](./03-Minesweeper-Knowledge-Inference):** Developed an autonomous knowledge-based agent that represents board constraints as logical sentences. Utilizes iterative subset inference ($S_1 \subseteq S_2 \implies S_2 - S_1 = c_2 - c_1$) to deduce safe moves and isolate hidden mines.

### 2. Uncertainty
* **[PageRank](./04-PageRank-Markov-Chain):** Implemented Google's core ranking algorithm through both Monte Carlo Random Surfer simulations (10,000 sampling steps) and recursive fixed-point iteration until convergence ($\Delta < 0.001$).
* **[Heredity](./05-Heredity-Bayesian-Networks):** Constructed a Bayesian Network to infer genetic trait distributions across multi-generational family trees, computing joint and conditional probabilities with mutation rates.

### 3. Optimization
* **[Crossword](./06-Crossword-Constraint-Satisfaction):** Solved crossword puzzle generation as a Constraint Satisfaction Problem (CSP). Implemented the AC-3 algorithm for arc consistency and backtracking search powered by Minimum Remaining Values (MRV) and Degree heuristics.

### 4. Learning
* **[Shopping](./07-Shopping-Predictor-ML):** Built a supervised machine learning classification pipeline using scikit-learn's $k$-Nearest Neighbors to predict customer online purchasing behavior, balancing sensitivity (true positive rate) and specificity (true negative rate).
* **[Nim](./08-Nim-Reinforcement-Learning):** Trained a self-learning game-playing agent using Model-Free Reinforcement Learning (Q-Learning). After 10,000 rounds of simulated self-play with an $\epsilon$-greedy strategy, the agent masters optimal end-game positioning.

### 5. Neural Networks
* **[Traffic](./09-Traffic-Recognition-CNN):** Designed, tuned, and evaluated a multi-layer Convolutional Neural Network (CNN) with TensorFlow/Keras on the German Traffic Sign Recognition Benchmark (GTSRB), classifying 43 traffic categories with over 95%+ test accuracy.

### 6. Language
* **[Parser](./10-Parser-Natural-Language-Processing):** Designed a Context-Free Grammar (CFG) in NLTK to parse sentences with complex prepositional, adverbial, and clausal modifiers. Implemented syntactic subtree traversal to extract base noun phrase chunks.
* **[Attention](./11-Attention-Transformers-Visualization):** Exploited HuggingFace Transformers and pretrained BERT (`bert-base-uncased`) to predict masked tokens and visualize self-attention matrices, empirically isolating attention heads specializing in sequential antecedent tracking and determiner-noun syntax.

---

## 💼 Resume & CV Impact Bullet Points

If you are featuring these projects on your CV, resume, or LinkedIn portfolio, here are high-impact, employer-ready bullet points:

```markdown
• Developed a comprehensive suite of 12 Artificial Intelligence and Machine Learning systems covering Graph Search, Knowledge Inference, Bayesian Networks, Reinforcement Learning, and Transformers.
• Engineered an unbeatable Minimax game engine with Alpha-Beta Pruning, an automated CSP crossword generator using AC-3 & MRV heuristics, and a Minesweeper knowledge-based inference agent.
• Trained a Deep Convolutional Neural Network (CNN) in TensorFlow/Keras achieving 95%+ classification accuracy across 43 classes on the German Traffic Sign Recognition Benchmark (GTSRB).
• Implemented Q-Learning Reinforcement Learning agents with epsilon-greedy policies and Google's PageRank algorithm via Markov Chain Monte Carlo simulations and iterative convergence.
• Visualized Transformer self-attention mechanisms in HuggingFace BERT, analyzing attention tensors across 144 head-layer configurations to interpret syntactic and semantic dependencies.
```

---

## 📂 Repository Structure

```text
.
├── 00-Degrees-Search/                 # BFS Shortest Path on IMDb Graph
├── 01-TicTacToe-Minimax/              # Adversarial Search & Pygame UI
├── 02-Knights-Propositional-Logic/    # Propositional Model Checking
├── 03-Minesweeper-Knowledge-Inference/# Knowledge-based Logic Agent
├── 04-PageRank-Markov-Chain/          # Random Surfer & Iterative PageRank
├── 05-Heredity-Bayesian-Networks/     # Probabilistic Gene Inference
├── 06-Crossword-Constraint-Satisfaction/# AC-3 & Backtracking CSP
├── 07-Shopping-Predictor-ML/          # KNN Classification & Metrics
├── 08-Nim-Reinforcement-Learning/     # Q-Learning Self-Play Agent
├── 09-Traffic-Recognition-CNN/        # Deep CNN Sign Classification
├── 10-Parser-Natural-Language-Processing/# CFG & Syntactic NP Chunking
├── 11-Attention-Transformers-Visualization/# BERT Attention Analysis
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<USERNAME>/CS50AI-Artificial-Intelligence-Projects.git
cd CS50AI-Artificial-Intelligence-Projects
```

### 2. Environment Setup
Create and activate an isolated Python virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Run Any Project
Navigate into the desired project folder and follow the project-specific `README.md`.
For example, to play Tic-Tac-Toe against the AI:
```bash
cd 01-TicTacToe-Minimax
pip install -r requirements.txt
python runner.py
```

---

## 🛠 Technologies & Tooling
* **Languages:** Python 3.10+
* **Machine Learning & Deep Learning:** TensorFlow, Keras, scikit-learn, PyTorch, HuggingFace Transformers
* **Natural Language Processing:** NLTK, Regular Expressions, Tokenizers
* **Computer Vision & Graphics:** OpenCV, Pygame, Pillow (PIL)
* **Mathematical Foundations:** NumPy, Graph Theory, Probability, Propositional Calculus

---

## 📜 License
This repository is licensed under the [MIT License](LICENSE).
