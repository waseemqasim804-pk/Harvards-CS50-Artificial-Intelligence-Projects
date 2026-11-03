# Project 6a: Parser (Natural Language Processing & CFG)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![NLTK](https://img.shields.io/badge/NLP-NLTK-blueviolet.svg)
![Formalism](https://img.shields.io/badge/Grammar-Context--Free%20Grammar%20(CFG)-green.svg)

## 📌 Problem Overview
Natural Language Processing requires understanding sentence syntax to interpret meaning. This project builds a **Context-Free Grammar (CFG)** capable of parsing complex English sentences and extracting **Noun Phrase (NP) chunks** without including enclosing noun phrase subtrees.

---

## 🧠 Core NLP Concepts & Grammar Design
- **Context-Free Grammar (CFG):**
  Defines formal production rules combining terminal symbols (lexicon words) and non-terminal syntactic categories:
  $$S \to NP \; VP \mid S \; \text{Conj} \; S$$
- **Syntactic Structures Handled:**
  - Transitive and intransitive verbs with adverbs and auxiliaries.
  - Prepositional phrases acting as adverbial and adjectival modifiers.
  - Compound sentences joined by conjunctions.
- **Noun Phrase Chunking:**
  Extracts base noun phrases ($NP$) that contain nouns and determiners/adjectives, but do not contain other nested $NP$ subtrees.

---

## 📂 Project Structure
```text
10-Parser-Natural-Language-Processing/
├── parser.py          # CFG grammar definitions, parsing logic, and NP chunker
├── sentences/         # 10 test benchmark sentences
└── requirements.txt   # Dependencies (nltk)
```

---

## 🚀 Quickstart & Usage
```bash
pip install -r requirements.txt
python parser.py sentences/1.txt
```

### Sample Output:
```text
              S
  ____________|____
 NP                VP
  |           _____|___
  N          V         NP
  |          |         |
Holmes      sat        N
                       |
                   yesterday

Noun Phrase Chunks
Holmes
yesterday
```
