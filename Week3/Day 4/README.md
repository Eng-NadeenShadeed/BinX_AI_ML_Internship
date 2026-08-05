# Week 3 - Day 4: Trees, Forests, SVMs & k-NN

## Overview

Today I explored four different classification algorithms: Decision Trees, Random Forests, Support Vector Machines (SVM), and k-Nearest Neighbors (k-NN). The goal was not only to train these models, but to understand how each classifier makes decisions and why different problems require different algorithms.

I trained all models using the same train/test split and compared their performance using the same evaluation metrics. This helped me understand that there is no single "best" classifier for every dataset, and model selection depends on the data characteristics, complexity, interpretability requirements, and bias-variance trade-off.

---

## Files

```text
Day 4/
├── data/
│   └── pima-indians-diabetes.csv
├── day4_trees_forests_svm_knn.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## Topics Covered

1. Why We Need Different Classifiers — understanding that different algorithms make different assumptions about data.
2. Bias & Variance Trade-off — the relationship between underfitting, overfitting, and model complexity.
3. Decision Trees — rule-based models, interpretability, splitting decisions, and overfitting problems.
4. Random Forest — ensemble learning, bagging, random feature selection, and feature importance.
5. Support Vector Machines (SVM) — margins, decision boundaries, and the idea behind maximizing separation.
6. k-Nearest Neighbors (k-NN) — distance-based classification and lazy learning.
7. Comparing Classifiers Fairly — using the same dataset split and evaluation metrics for all models.
8. Feature Importance — understanding which features contribute most to tree-based model decisions.
9. Practical Implementation with Scikit-learn — training, predicting, and evaluating multiple classifiers.

---

## Hands-On Lab Summary

Built and compared four classification models using the **Pima Indians Diabetes Dataset** to predict whether a patient has diabetes.

### Models Compared

| Model | Main Idea |
|---|---|
| Decision Tree | Learns a sequence of feature-based rules |
| Random Forest | Combines multiple decision trees to reduce overfitting |
| SVM | Finds the best separating boundary between classes |
| k-NN | Predicts based on similarity to nearby samples |

---

## Model Performance

All models were trained using the same preprocessing steps, train/test split (`random_state=42`), and evaluated using **F1-score for the Diabetes class**.

| Model | F1-Score |
|---|---:|
| Random Forest (100 trees) | 0.626 |
| k-NN (k=5) | 0.619 |
| SVM (RBF kernel) | 0.587 |
| Decision Tree (max_depth=5) | 0.551 |

---

## Confusion Matrix Summary

| Model | True Positives (Caught Diabetes) | False Negatives (Missed Cases) | False Positives |
|---|---:|---:|---:|
| Random Forest | 31 / 50 | 19 | 18 |
| k-NN | 30 / 50 | 20 | 17 |
| SVM | 27 / 50 | 23 | 15 |
| Decision Tree | 27 / 50 | 23 | 21 |

---

## Random Forest Feature Importance

| Feature | Importance |
|---|---:|
| Glucose | 0.297 |
| BMI | 0.190 |
| Age | 0.164 |
| DiabetesPedigreeFunction | 0.161 |
| BloodPressure | 0.095 |
| Pregnancies | 0.093 |

---

## Key Findings

- Learned that different classifiers solve the same problem using different approaches and assumptions.
- Decision Trees are easy to interpret but can overfit when they become too complex.
- Random Forest improved generalization by combining multiple trees and reducing variance.
- SVM focuses on finding the optimal decision boundary by maximizing the margin between classes.
- k-NN does not build an explicit model during training; instead, it predicts based on the closest examples.
- Compared models fairly by keeping the same train/test split and evaluation process.
- Used F1-score instead of accuracy because the dataset is not perfectly balanced and missing diabetes cases is more important than overall accuracy.
- Random Forest achieved the best performance on this dataset, with the highest F1-score and the most correctly detected diabetes cases.
- Feature importance showed that Glucose was the most influential feature for the Random Forest model.
- Model selection depends on the dataset, the goal of the prediction task, and the trade-off between interpretability and performance.

---

## What I Learned

By the end of this day, I understood how tree-based, distance-based, and margin-based classifiers work internally and when each approach is useful.

I learned that machine learning does not have a universal best algorithm; instead, choosing the right model requires understanding the data, evaluating different approaches, and comparing results using meaningful metrics.