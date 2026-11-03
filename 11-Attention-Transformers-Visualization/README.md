# Project 6b: Attention (Transformers & BERT Attention Visualization)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Transformers](https://img.shields.io/badge/Model-BERT%20(HuggingFace)-red.svg)
![Visualization](https://img.shields.io/badge/Analysis-Self--Attention%20Heatmaps-blue.svg)

## 📌 Problem Overview
The Transformer architecture powers modern Large Language Models (LLMs). Central to Transformers is the **Self-Attention mechanism**, allowing every token to dynamically weigh and attend to every other token in a sentence.

This project uses HuggingFace's pretrained `bert-base-uncased` to predict masked words in a sentence and visualizes the attention weights across all 12 layers and 12 attention heads, deciphering the linguistic roles performed by individual heads.

---

## 🧠 Core Architecture & Findings
- **Masked Language Modeling (BERT):**
  Calculates top probability predictions for the `[MASK]` token based on bidirectional contextual embeddings.
- **Attention Matrix Extraction:**
  For sequence length $T$, extracts attention tensors of shape $[12, 12, T, T]$.
- **Linguistic Specialization of Heads (Documented in `analysis.md`):**
  - **Layer 4, Head 6 (Sequential Antecedent Tracking):** Tokens systematically attend to the immediately preceding token ($i - 1$), forming a distinct off-diagonal band.
  - **Layer 8, Head 11 (Syntactic Determiner-Noun Dependencies):** Determiners ("a", "the") attend directly to their governing head nouns, bypassing descriptive adjectives.

---

## 📂 Project Structure
```text
11-Attention-Transformers-Visualization/
├── mask.py           # HuggingFace BERT inference and attention matrix diagram generator
├── analysis.md       # Rigorous linguistic analysis of attention head specializations
├── assets/           # Sample generated attention heatmap visualizations
└── requirements.txt  # Dependencies (transformers, torch, PIL)
```

---

## 🚀 Quickstart & Usage
```bash
pip install -r requirements.txt
python mask.py
```
*Enter a sentence with `[MASK]` (e.g. `We turned down a narrow lane and passed through a small [MASK].`).*
*The program outputs top predictions and saves attention heatmaps for all layers and heads!*
