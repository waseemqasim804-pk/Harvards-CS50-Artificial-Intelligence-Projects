# Project 4a: Shopping Purchase Predictor (Machine Learning Classification)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange.svg)
![Classifier](https://img.shields.io/badge/Model-k--Nearest%20Neighbors%20(k%3D1)-blue.svg)

## 📌 Problem Overview
E-commerce businesses want to anticipate whether an online shopper browsing their store will make a purchase.

This project trains a supervised machine learning classifier using historical visitor browsing metrics (administrative duration, bounce rates, exit rates, visitor types, seasonality) to predict user purchase intention (`Revenue`).

---

## 🧠 Core AI Concepts & Evaluation Metrics
- **Data Preprocessing & Feature Engineering:**
  - Maps numerical and temporal browser attributes.
  - Encodes categorical features (Months, Visitor Types, Weekend indicator) into numerical tensors.
- **k-Nearest Neighbors ($k=1$):** Classifies user behavior based on closest geometric distance in feature space.
- **Evaluation Beyond Accuracy (Imbalanced Classes):**
  Because non-purchasing visitors far outnumber purchasers, accuracy alone is misleading:
  - **Sensitivity (True Positive Rate):** Proportion of actual buyers correctly identified.
    $$\text{Sensitivity} = \frac{TP}{TP + FN}$$
  - **Specificity (True Negative Rate):** Proportion of non-buyers correctly identified.
    $$\text{Specificity} = \frac{TN}{TN + FP}$$

---

## 📂 Project Structure
```text
07-Shopping-Predictor-ML/
├── shopping.py    # Preprocessor, KNN model trainer, and sensitivity evaluator
└── shopping.csv   # Historical e-commerce session dataset
```

---

## 🚀 Quickstart & Usage
```bash
python shopping.py shopping.csv
```

### Sample Output:
```text
Correct: 4098
Incorrect: 834
True Positive Rate: 41.24%
True Negative Rate: 90.65%
```
