# Week 4 — Day 5: Scikit-learn Pipelines & End-to-End ML Project

## Overview

Day 5 closed Week 4 with a full end-to-end pipeline on the Medical
Cost dataset from Week 2. The work brought together everything from
the week: a correct three-way split, cross-validation, EDA-driven
feature engineering, a ColumnTransformer for mixed data, and
GridSearchCV tuning — all inside one leakage-free Pipeline.

The key finding came from the EDA: smokers showed dramatically higher
charges. That signal became the `bmi_smoker` interaction feature,
which the final model ranked at 0.807 feature importance — confirming
the EDA before a single hyperparameter was touched.

---

## Dataset

| Detail | Value |
|--------|-------|
| Source | Medical Cost Personal Dataset (Week 2) |
| Rows | 1,338 |
| Features | 6 (3 numeric, 3 categorical) |
| Target | `charges` — continuous (regression) |
| Task | Regression |

---

## Topics Covered

- Why Pipelines prevent data leakage
- Building a Pipeline: preprocessing + model in one object
- ColumnTransformer for mixed numeric/categorical data
- Tuning a whole pipeline with GridSearchCV
- Assembling a professional, leak-free workflow

---

## What I Did

- Ran full EDA (5 sections): target distribution, smoking signal,
  numeric distributions, categorical distributions, correlation heatmap
- Built a numeric-only baseline to establish a floor
- Added a `ColumnTransformer` to handle scaling and one-hot encoding
  inside the Pipeline — making leakage structurally impossible
- Engineered two domain-informed features:
  - `bmi_smoker`: BMI × smoker flag — captures the combined risk
  - `age_bmi`: age × BMI product — captures age-related metabolic risk
- Tuned the full Pipeline with GridSearchCV (12 combinations × 5 folds)
- Evaluated once on the held-out test set

---

## Results

| Stage | CV R² | Notes |
|-------|------:|-------|
| Baseline (numeric only) | -0.107 | No encoding — categorical features dropped |
| Simple Pipeline (all features) | 0.835 | ColumnTransformer + RF |
| Pipeline + Feature Engineering | 0.836 | bmi_smoker + age_bmi added |
| Tuned Pipeline (GridSearchCV) | 0.858 | Best: max_depth=10, leaf=5, n=200 |
| **Final Test R²** | **0.876** | Opened once, after all decisions |

Top feature importances from the final model:

| Feature | Importance |
|---------|----------:|
| bmi_smoker | 0.807 |
| age | 0.099 |
| age_bmi | 0.040 |

---

## Files

```text
Day 5/
├── data/
│   └── insurance.csv
└── Hands_On_Lab.ipynb
```

---

## How to Run

1. Activate your `.venv`.
2. Open `Hands_On_Lab.ipynb` in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all cells from top to bottom.