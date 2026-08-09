# Week 4 – Day 1: Train / Validation / Test Splits

## Overview

Today introduced the core discipline behind honest model evaluation: the train/validation/test workflow.

In Week 3, every experiment used a single train/test split — which works for a single final evaluation, but becomes problematic when comparing models or tuning hyperparameters. Every time I use the test score to make a development decision, I give the model indirect information about the test set, making the final score less trustworthy.

The solution is a validation set that absorbs all development decisions, while the test set remains untouched until the very end.

The learning notebook worked through these concepts using the Pima Diabetes dataset from Week 3. The Hands-On Lab applied the complete workflow to the Student Performance dataset — including splitting, model selection, hyperparameter tuning, and final test evaluation.

---

## Dataset 

| Notebook     | Dataset                        |       Size | Task                   |
| ------------ | ------------------------------ | ---------: | ---------------------- |
| Learning     | Pima Indians Diabetes (Week 3) |   768 rows | Binary classification  |
| Hands-On Lab | Student Performance (Week 1)   | 2,392 rows | 5-class classification |

---

## Topics Covered

- The problem with tuning against a single test set
- The three-way split: train, validation, test
- Creating a three-way split in code
- Why one validation set can still mislead (motivating cross-validation)

## What I Did

- **Three-way split** — created a 60/20/20 train/validation/test split using two calls to `train_test_split`, with `stratify` in both to preserve class proportions across all three subsets.
- **Class balance check** — verified that all five grade classes (including Class 0 at 4.5%) were proportionally represented after splitting.
- **Model comparison** — trained Logistic Regression, Decision Tree, and Random Forest on the training set and compared them on the validation set only. Test set stayed locked.
- **Scaling without leakage** — wrapped Logistic Regression in a `make_pipeline` so the `StandardScaler` was fitted on training data only and never saw the validation set.
- **Hyperparameter tuning** — tuned Random Forest `max_depth` ∈ {3, 5, 10, None} on the validation set. `max_depth=None` achieved the highest validation F1 (0.904).
- **Final evaluation** — opened the test set exactly once, after all decisions were final.
- **Data leakage analysis** — documented what would have gone wrong if `max_depth` had been tuned against the test set instead of validation.

---

## Results

### Model Comparison

| Model               | Train F1 |    Val F1 |
| ------------------- | -------: | --------: |
| Logistic Regression |    0.805 |     0.796 |
| Decision Tree       |    0.942 |     0.898 |
| Random Forest       |    1.000 | **0.904** |

Random Forest achieved the highest validation F1 and was selected for hyperparameter tuning.

### Hyperparameter Tuning

| `max_depth` | Train F1 |    Val F1 |
| ----------: | -------: | --------: |
|           3 |    0.844 |     0.803 |
|           5 |    0.890 |     0.864 |
|          10 |    0.975 |     0.901 |
|        None |    1.000 | **0.904** |

The best validation performance came from `max_depth=None`.

### Final Evaluation

| Model                            | Validation F1 |   Test F1 | Test Accuracy |
| -------------------------------- | ------------: | --------: | ------------: |
| Random Forest (`max_depth=None`) |         0.904 | **0.910** |     **0.916** |

The test F1 was slightly higher than the validation F1. This is normal because validation and test sets contain different samples. The important point is that the test set had no influence on any development decision, making 0.910 a trustworthy final estimate.

---

## Key Lesson

The main lesson from today was not simply how to split a dataset, but **how to keep model evaluation honest**:

* **Training →** the model learns.
* **Validation →** I compare models and make development decisions.
* **Test →** I evaluate the finalized model once.

The test set must remain independent from the development process. If I repeatedly use it to choose models or hyperparameters, it stops being an honest estimate of performance on unseen data.

---

## Files

```text
Day 1/
├── day1_train_val_test_splits.ipynb   ← concept walkthrough (Pima Diabetes)
└── Hands_On_Lab.ipynb                 ← full workflow (Student Performance)
```

---

## How to Run

1. Activate your `.venv`.
2. Open either notebook in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all cells from top to bottom.

---
