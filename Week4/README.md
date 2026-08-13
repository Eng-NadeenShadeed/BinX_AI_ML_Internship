# Week 4 — Evaluation, Tuning & Pipelines

## Overview

Week 4 focused on turning a model that runs into a model that can be
trusted. The five days covered the full professional ML workflow:
evaluating models honestly with cross-validation, diagnosing fit
problems using the bias-variance framework, engineering better
features, tuning hyperparameters systematically with GridSearchCV,
and packaging everything into a single leakage-free Scikit-learn
Pipeline.

The week closed with an end-to-end pipeline mini-project on the
Medical Cost dataset — the exact structure required for the
Phase 3 capstone.

---

## Datasets

| Day | Dataset | Task |
|-----|---------|------|
| Days 1–4 (Learning) | Pima Indians Diabetes (Week 3) | Binary classification |
| Days 1–4 (Lab) | Student Performance (Week 1) | 5-class classification |
| Day 5 (Lab) | Medical Cost / insurance.csv (Week 2) | Regression |

---

## Daily Breakdown

### Day 1 — Train / Validation / Test Splits
Built the evaluation discipline that every other day depends on.
Compared three models on a held-out validation set, tuned one
hyperparameter without touching the test set, and evaluated
the final model exactly once.

**Lab result:** Test F1 = 0.919 | Test Accuracy = 0.916

---

### Day 2 — Cross-Validation
Replaced a single validation split with 5-fold stratified
cross-validation to get a stable, trustworthy performance estimate.
Verified that StratifiedKFold preserved class proportions across
all folds — critical for the imbalanced Student Performance dataset.

**Lab result:** CV mean F1 = 0.918 ± 0.006 | Test F1 = 0.905

---

### Day 3 — Bias-Variance Trade-off
Diagnosed both overfitting and underfitting deliberately, confirmed
each diagnosis using confusion matrices, and traced the bias-variance
curve across complexity settings. Added a learning curve to show
whether more data would help, and ran a data leakage experiment
(+0.241 F1 from one leaky feature).

**Lab result:** Best val F1 = 0.904 (max_depth=None) | Test F1 = 0.910

---

### Day 4 — Feature Engineering & Hyperparameter Tuning
Designed four engineered features from domain reasoning, tested each
individually against the baseline, then ran GridSearchCV across 24
combinations. Visualized which hyperparameter mattered most using
bar charts and a heatmap.

**Lab result:** Baseline CV F1 = 0.918 → Tuned CV F1 = 0.927

---

### Day 5 — Scikit-learn Pipelines & Mini-Project *(Graded)*
Built a full end-to-end Pipeline with a ColumnTransformer handling
numeric scaling and categorical encoding. Engineered `bmi_smoker`
from EDA (the smoking signal found in Part 1 drove 0.806 feature
importance in the final model). Tuned the complete pipeline with
GridSearchCV and evaluated once on the held-out test set.

**Lab result:** Baseline R² = -0.108 → Final Test R² = 0.876

---

## Key Results

| Day | Baseline | Final |
|-----|--------:|------:|
| Day 1 — Test F1 | — | 0.919 |
| Day 2 — CV F1 | 0.904 (single split) | 0.918 ± 0.006 |
| Day 3 — Val F1 | 0.785 (underfit) | 0.904 (tuned) |
| Day 4 — CV F1 | 0.918 | 0.927 |
| Day 5 — Test R² | -0.108 (numeric baseline) | 0.876 |

---

## Week 4 Deliverables

- [x] Three-way split notebook with correct train/val/test discipline
- [x] Cross-validation notebook — mean ± std, stratified folds
- [x] Bias-variance notebook — diagnosed overfit and underfit with fixes
- [x] Feature engineering + GridSearchCV notebook
- [x] Tuned pipeline mini-project — leak-free, end-to-end *(Graded)*
- [x] All notebooks committed to GitHub

---

## Repository Structure

```text
Week4/
├── Day 1/
│   ├── day1_train_val_test_splits.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 2/
│   ├── day2_cross_validation.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 3/
│   ├── day3_bias_variance.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 4/
│   ├── day4_feature_engineering_hyperparameter_tuning.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 5/
│   ├── data/
│   │   └── insurance.csv
│   ├── Hands_On_Lab.ipynb
│   └── README.md
└── README.md
```

---

## How to Run

1. Activate your `.venv`.
2. Open any notebook in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all cells from top to bottom.