# Project 5: Traffic Sign Recognition (Convolutional Neural Networks)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![TensorFlow](https://img.shields.io/badge/Deep%20Learning-TensorFlow%20%2F%20Keras-orange.svg)
![Architecture](https://img.shields.io/badge/Architecture-Convolutional%20Neural%20Network%20(CNN)-brightgreen.svg)

## 📌 Problem Overview
Autonomous self-driving vehicles must accurately detect and recognize traffic signs from camera feeds under varying lighting and weather conditions.

This project designs and trains an end-to-end Deep Learning **Convolutional Neural Network (CNN)** on the German Traffic Sign Recognition Benchmark (GTSRB), classifying road signs across 43 unique categories with high accuracy.

---

## 🧠 Neural Network Architecture
The deep architecture is engineered to balance feature representation with regularization:
1. **Input Layer:** Resized image tensors ($30 \times 30 \times 3$).
2. **Convolutional Layer 1:** 32 filters ($3 \times 3$), ReLU activation.
3. **Max Pooling Layer 1:** $2 \times 2$ pool size.
4. **Convolutional Layer 2:** 64 filters ($3 \times 3$), ReLU activation.
5. **Max Pooling Layer 2:** $2 \times 2$ pool size.
6. **Flatten Layer:** Flattens multi-dimensional feature maps into a 1D vector.
7. **Dense Hidden Layer:** 128 neurons, ReLU activation.
8. **Dropout Regularization:** 50% dropout rate ($0.5$) to prevent overfitting.
9. **Output Softmax Layer:** 43 units representing probability distribution over categories.

---

## 📂 Project Structure
```text
09-Traffic-Recognition-CNN/
├── traffic.py          # Image pipeline, model architecture, and training routine
├── README.md           # Experimental analysis and hyperparameter tuning notes
└── requirements.txt    # Dependencies (tensorflow, opencv-python, scikit-learn)
```

---

## 🚀 Quickstart & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train and Evaluate
```bash
python traffic.py gtsrb model.h5
```
*Achieves over 95%+ test accuracy on 43 traffic sign classes.*
