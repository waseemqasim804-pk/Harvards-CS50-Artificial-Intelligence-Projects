# Project 0a: Degrees (Breadth-First Search)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![AI-Search](https://img.shields.io/badge/Domain-Graph%20Search%20%26%20Shortest%20Path-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Breadth--First%20Search%20(BFS)-green.svg)

## 📌 Problem Overview
According to the "Six Degrees of Kevin Bacon" game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step represents two actors having co-starred in the same film.

This project implements an intelligent graph search agent to find the shortest path between any two actors by modeling the film industry as an undirected bipartite graph of **actors** and **movies**.

---

## 🧠 Core AI Concepts & Algorithms
- **Breadth-First Search (BFS):** Guarantees finding the optimal (shortest) path between the source actor and target actor in an unweighted graph.
- **Search Frontier:** Utilizes a `QueueFrontier` (FIFO queue) to explore all nodes at depth $d$ before moving to depth $d + 1$.
- **State Representation:**
  - **State:** Actor ID (`person_id`).
  - **Action:** Starring in movie ID (`movie_id`).
  - **Node:** Stores state, parent node reference, and transition action.
- **Explored Set:** Maintains a set of visited actor IDs to prevent infinite loops in cyclic graphs.

---

## 📂 Project Structure
```text
00-Degrees-Search/
├── degrees.py       # Core search algorithm and CLI interface
├── util.py          # Node, StackFrontier, and QueueFrontier data structures
├── small/           # Subset CSV dataset (for rapid testing)
│   ├── movies.csv
│   ├── people.csv
│   └── stars.csv
└── large/           # Complete IMDb dataset
```

---

## 🚀 Quickstart & Usage

### 1. Run with Small Dataset (Quick Test)
```bash
python degrees.py small
```
*Prompt:*
```text
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
2 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Jennifer Lawrence starred in The Ballad of Buster Scruggs
```

### 2. Run with Complete Large IMDb Dataset
```bash
python degrees.py large
```

---

## 📊 Algorithmic Complexity
- **Time Complexity:** $\mathcal{O}(V + E)$ where $V$ is actors and $E$ is co-star relations.
- **Space Complexity:** $\mathcal{O}(V)$ for storing the frontier and explored set.
