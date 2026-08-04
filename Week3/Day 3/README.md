# Week 3 - Day 3: Logistic Regression & Classification Metrics

## Overview

Today I trained my first classifier using Logistic Regression to predict whether a patient has diabetes using the Pima Indians Diabetes dataset. Unlike Linear Regression, which predicts continuous values, Logistic Regression predicts class labels by estimating probabilities.

Before building the model, I explored the dataset myself instead of jumping directly into training. During the EDA process, I discovered that several medical measurements used `0` to represent missing values rather than valid observations. I verified this through descriptive statistics, zero-count analysis, and visualizations before deciding how to clean the data. This reinforced the importance of understanding the dataset before applying any machine learning algorithm.

---

## Files

```text
Day 3/
├── data/
│   └── pima-indians-diabetes.csv
├── day3_logistic_regression.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## Topics Covered

1. What Is Classification? — binary, multiclass, and multi-label classification with real-world applications.
2. Logistic Regression: From Weighted Sum to Probability — using the same linear equation from Day 2 but transforming its output into probabilities.
3. The Sigmoid Function — mathematical formula, intuition, behavior, and visualization.
4. Decision Threshold & Decision Boundary — understanding `predict()` vs. `predict_proba()` and visualizing the decision boundary.
5. Why Accuracy Alone Is Misleading — especially for imbalanced datasets.
6. The Confusion Matrix — True Positive, False Positive, False Negative, and True Negative.
7. Precision, Recall & F1-Score — understanding the trade-off between evaluation metrics.
8. AUC-ROC — evaluating classifier performance across every possible decision threshold.
9. Log Loss (Cost Function) — why Mean Squared Error is unsuitable for Logistic Regression and how Log Loss solves the optimization problem.
10. Practical Application with Scikit-learn — implementing the complete machine learning workflow on a real dataset.

> **Note:** Sections **4 (Decision Boundary Visualization)** and **9 (Log Loss)** are beyond the official internship curriculum. I included them to better understand *why* Logistic Regression works, not only how to use it.

---

## Hands-On Lab Summary

Built a complete machine learning workflow using the **Pima Indians Diabetes Dataset** to predict whether a patient has diabetes.

### Model Performance

| Metric | Value |
|---|---:|
| Accuracy | 0.75 |
| Precision (diabetic) | 0.57 |
| Recall (diabetic) | 0.54 |
| F1-score (diabetic) | 0.56 |
| AUC-ROC | 0.75 |

---

### Key Findings

- Explored the dataset before modeling instead of assuming it was already clean.
- Discovered that **five medical features** used `0` to represent missing measurements.
- Verified this issue using `.describe()`, zero-count analysis, and histograms before preprocessing the data.
- Found that nearly **48.7%** of the values in the **Insulin** feature were missing.
- Completed the full machine learning workflow: **data exploration → preprocessing → model training → evaluation**.
- Although the model achieved **75% accuracy**, I did not rely on accuracy alone because the dataset is moderately imbalanced.
- For this disease-screening problem, I concluded that **Recall** is more important than **Precision**, since failing to identify a diabetic patient (False Negative) is more harmful than producing a false alarm (False Positive).
- Based on the evaluation metrics, **Recall (0.54)** was the model's primary weakness at the default decision threshold.

---

## What I Learned

By the end of this day, I understood how Logistic Regression converts a weighted sum into a probability using the sigmoid function, how classification metrics describe different aspects of model performance, and why evaluating a classifier requires much more than simply checking its accuracy. More importantly, I learned that successful machine learning begins with understanding the data itself before training any model.