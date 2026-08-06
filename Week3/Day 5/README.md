# Week 3 – Day 5: Heart Disease Prediction (End-to-End Mini-Project)

## Overview

Today is the Week 3 capstone. Instead of learning a new algorithm, I took everything from this week and applied it in one complete pipeline on a dataset I hadn't worked with before — Heart Disease UCI (920 patients from four hospitals). The goal was to go from raw, messy data to a trained and evaluated model, making every decision based on what I actually found in the data.

---

## Dataset

- **Source:** Heart Disease UCI Dataset (Kaggle)
- **File:** `data/heart_disease_uci.csv`
- **Size:** 920 patients, 16 columns

---

## What I Did

- **EDA** — explored the dataset structure, checked missing values, identified 172 impossible zero values in `chol`, examined feature distributions, and verified class balance.
- **Cleaning** — dropped high-missing columns (`ca`, `thal`, `slope`), replaced impossible cholesterol values with `NaN`, and converted the target (`num`) into a binary classification problem.
- **Imputation** — filled numeric missing values with the median and categorical values with the mode.
- **Correlation Analysis** — examined relationships between numeric features and the target before modeling.
- **Encoding** — applied one-hot encoding to categorical features (`sex`, `cp`, `restecg`).
- **Split & Scale** — performed an 80/20 stratified train/test split and fitted `StandardScaler` on the training data only.
- **Baseline** — evaluated a majority-class baseline (55.4% accuracy).
- **Modeling** — trained Logistic Regression and Random Forest classifiers.
- **Evaluation** — compared models using accuracy, F1-score, AUC-ROC, confusion matrices, ROC curves, and Random Forest feature importances.
- **Selection** — selected Random Forest as the final model based on its higher AUC-ROC (0.903 vs 0.891).

---

## Key Findings

- The dataset contained several missing values, requiring both column removal and imputation.
- `chol` contained 172 impossible zero values, which were treated as missing values.
- Logistic Regression achieved the highest disease recall (0.86), making it effective at detecting positive cases.
- Random Forest achieved the highest overall AUC-ROC (0.903) and was selected as the final model.

---

## Results

| Model | Accuracy | F1 (Macro) | AUC-ROC |
|-------|---------:|-----------:|--------:|
| Baseline | 0.554 | — | — |
| Logistic Regression | 0.799 | 0.794 | 0.891 |
| Random Forest | 0.793 | 0.790 | 0.903 |

---

## Files

```text
Day 5/
├── data/
│   └── heart_disease_uci.csv
└── Hands_On_Lab.ipynb
```

---

## How to Run

1. Activate your `.venv`.
2. Open `Hands_On_Lab.ipynb` in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all notebook cells from top to bottom.