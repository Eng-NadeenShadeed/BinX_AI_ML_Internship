# Week 4 — Day 4: Feature Engineering & Hyperparameter Tuning

## Overview

Day 3 taught me how to diagnose model fit before tuning.
Day 4 takes the next step: once I understand what the model
is learning, how can I give it better information — and how
can I systematically find better hyperparameters?

The answer is feature engineering and systematic hyperparameter
search. Instead of immediately choosing a more complex model,
I experimented with creating meaningful features and measured
whether they actually improved performance. I then used
GridSearchCV with cross-validation to search for better model
configurations, followed by RandomizedSearchCV to understand
how to handle larger search spaces.

---

## Dataset

| Notebook     | Dataset               | Task                      | Target           |
| ------------ | --------------------- | ------------------------- | ---------------- |
| Learning     | Pima Indians Diabetes | Binary classification     | Outcome (0/1)    |
| Hands-On Lab | Student Performance   | Multiclass classification | GradeClass (0–4) |

---

## Topics Covered

* What feature engineering is and why better features can improve a model
* Creating new features from existing variables
* Testing engineered features individually and in combination
* Comparing engineered features against a baseline model
* Hyperparameters vs. learned parameters
* Systematic hyperparameter tuning instead of manual trial and error
* GridSearchCV with 5-fold cross-validation
* `best_params_`, `best_score_`, and `best_estimator_`
* Analyzing `cv_results_` to understand the search process
* Comparing tuned models with untuned baselines
* Understanding how hyperparameters affect model performance
* Search-space size and computational cost
* RandomizedSearchCV for larger hyperparameter spaces
* Feature importance and interpreting engineered features
* Reproducible experiments using fixed random states

---

## Hands-On Lab Results

| Step                  | What I Did                                 | Key Finding                                     |
| --------------------- | ------------------------------------------ | ----------------------------------------------- |
| Baseline              | Random Forest without new features         | Baseline CV F1 = 0.918 ± 0.006                  |
| Feature Engineering   | Created four new features                  | Combined features improved CV F1 to 0.926       |
| Feature Analysis      | Tested engineered features individually    | Not every engineered feature improved the model |
| GridSearchCV          | 24 combinations × 5-fold CV                | Best tuned CV F1 ≈ 0.927                        |
| Hyperparameter Search | Analyzed `cv_results_`                     | `n_estimators` and `max_depth` affected results |
| RandomizedSearchCV    | Searched a larger space with 20 iterations | Found a strong configuration with fewer fits    |
| Feature Importance    | Compared original and engineered features  | Some engineered features added useful signal    |

---

## Key Findings

**1.** Feature engineering is not automatically beneficial.
Creating a feature only helps if it adds useful information
that the model can learn from.

**2.** Testing engineered features individually helped separate
useful features from features that added little or even reduced
performance.

**3.** Combining the engineered features produced a measurable
improvement over the baseline, showing that feature engineering
and model tuning can work together.

**4.** GridSearchCV provided a systematic way to compare
hyperparameter combinations using 5-fold cross-validation instead
of relying on manual trial and error.

**5.** The size of a hyperparameter search matters. A large grid
can require hundreds or thousands of model fits, which is why
RandomizedSearchCV can be more practical for larger search spaces.

**6.** The best hyperparameters are not necessarily the largest
or most complex values. The goal is to find a configuration that
generalizes well according to cross-validation.

**7.** Feature importance helped explain which variables contributed
most to the Random Forest's predictions and whether the engineered
features provided useful signal.

---

## Files

```text
Day 4/
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

`scikit-learn` • `pandas` • `numpy` • `matplotlib` • `seaborn` • Jupyter Notebook
