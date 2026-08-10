# Week 4 – Day 2: Cross-Validation

## Overview

Day 1 introduced the three-way split as the correct evaluation discipline.
Day 2 addresses the remaining weakness: a single validation set can still
mislead if it happens to be an easy or hard slice by chance. Cross-validation
replaces one split with five rotating ones, averages the scores, and adds a
standard deviation that shows how stable the estimate is.

The learning notebook worked through the concept on the Pima Diabetes dataset
from Week 3. The Hands-On Lab applied the full CV workflow on the Student
Performance dataset and compared the result directly to the Day 1 single-split score.

---

## Datasets

| Notebook | Dataset | Size | Task |
|----------|---------|-----:|------|
| Learning | Pima Indians Diabetes (Week 3) | 768 rows | Binary classification |
| Hands-On Lab | Student Performance (Week 1) | 2,392 rows | 5-class classification |

---

## Topics Covered

- Why cross-validation beats a single validation split
- How k-fold works: rotating folds
- cross_val_score: mean and standard deviation
- Stratified k-fold for balanced classification folds

---

## What I Did

- Used an 80/20 train/test split — no fixed validation set needed since CV handles validation internally
- Set up `StratifiedKFold` explicitly (5 folds, shuffle=True) to preserve class proportions across folds
- Ran `cross_val_score` with weighted F1 and verified that Class 4 stayed at ~0.51 in every fold
- Compared the CV estimate to the Day 1 single-split score and explained the difference
- Trained the final model on the full training portion and evaluated once on the held-out test set

---

## Results

| Metric | Value |
|--------|------:|
| CV mean F1 (weighted) | 0.917 |
| CV std F1 | 0.014 |
| Day 1 single-split val F1 | 0.904 |
| Final test F1 | 0.905 |
| Final test accuracy | 0.912 |

---

## Files

```text
Day 2/
├── day2_cross_validation.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## How to Run

1. Activate your `.venv`.
2. Open the notebook in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all cells from top to bottom.