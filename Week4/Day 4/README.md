# Week 4 — Day 4: Feature Engineering & Hyperparameter Tuning

## Overview

Day 3 taught me how to diagnose model fit before tuning.
Day 4 takes the next step: once I understand what the model is learning,
how can I give it better information — and how can I systematically
find better hyperparameters?

The answer is feature engineering and systematic hyperparameter search.
Instead of immediately choosing a more complex model, I experimented with
creating meaningful features and measured whether they actually improved
performance. I then used GridSearchCV with cross-validation to search for
better model configurations, followed by RandomizedSearchCV to understand
how to handle larger search spaces.

---

## Dataset

| Notebook | Dataset | Task | Target |
|----------|---------|------|--------|
| Learning | Pima Indians Diabetes | Binary classification | Outcome (0/1) |
| Hands-On Lab | Student Performance | Multiclass classification | GradeClass (0–4) |

---

## Topics Covered

- What feature engineering is and why better features can improve a model
- Creating new features from existing variables
- Testing engineered features individually and in combination
- Comparing engineered features against a baseline model
- Hyperparameters vs. learned parameters
- Systematic hyperparameter tuning instead of manual trial and error
- GridSearchCV with 5-fold cross-validation
- `best_params_`, `best_score_`, and `best_estimator_`
- Analyzing `cv_results_` to understand the search process
- Comparing tuned models with untuned baselines
- Understanding how hyperparameters affect model performance
- Search-space size and computational cost
- RandomizedSearchCV for larger hyperparameter spaces
- Feature importance and interpreting engineered features
- Reproducible experiments using fixed random states

---

## Hands-On Lab Results

| Step | What I Did | Key Finding |
|------|-----------|-------------|
| Baseline | Random Forest without new features | CV F1 = 0.918 ± 0.006 |
| Feature Engineering | Created four new features | Combined features → CV F1 = 0.926 |
| Feature Analysis | Tested features individually | Not every feature improved the model |
| GridSearchCV | 24 combinations × 5-fold CV | Best tuned CV F1 ≈ 0.927 |
| Hyperparameter Search | Analyzed `cv_results_` | `min_samples_leaf` had the clearest effect |
| Feature Importance | Compared original and engineered features | Some engineered features added useful signal |

---

## Key Findings

1. **Feature engineering is not automatically beneficial.**
   A feature only helps if it adds information the model can't already
   extract from the original columns.

2. **Testing features individually separates useful from harmful ones.**
   Support_Score and Activity_Count both had educational justification
   but hurt performance — Random Forest was already discovering those
   patterns from the original columns.

3. **Combining engineered features produced the best result.**
   Features that individually hurt performance can complement each other
   when combined, because they capture different dimensions of the data.

4. **GridSearchCV provides a systematic replacement for manual tuning.**
   It tests every combination using cross-validation, removing the
   guesswork and single-split dependence of manual trial and error.

5. **The size of a hyperparameter search space matters.**
   A large grid can require hundreds of model fits — which is why
   RandomizedSearchCV becomes more practical for larger spaces.

6. **The best hyperparameters are not necessarily the most complex.**
   The goal is the combination that generalizes best according to
   cross-validation, not the highest model complexity.

7. **Feature importance helped explain model behavior.**
   GPA and Absences dominated predictions. Among engineered features,
   Absence_risk and Study_Absence_ratio appeared in the top importances.

---

## Files

```
Day4/
├── day4_feature_engineering_hyperparameter_tuning.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## How to Run

1. Activate the project virtual environment (`.venv`)
2. Open either notebook in Jupyter or VS Code
3. Select the `.venv` Python kernel
4. Run all cells from top to bottom

---

## Tools Used

`scikit-learn` • `pandas` • `numpy` • `matplotlib` • Jupyter Notebook
