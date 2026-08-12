# Week 4 — Day 3: Bias-Variance & Diagnosing Model Fit

## Overview

Day 1 taught honest splitting. Day 2 taught reliable evaluation.
Day 3 answers the next question: once I have a reliable score,
how do I know if the model is actually learning well — and if
it isn't, what exactly is wrong?

The answer is the train vs validation gap. A large gap signals
overfitting. No gap but low scores signals underfitting. The same
validation score can mean completely different things depending
on what the training score says alongside it.

---

## Dataset

| Notebook | Dataset | Task | Target |
|----------|---------|------|--------|
| Learning | Pima Indians Diabetes | Binary classification | Outcome (0/1) |
| Learning (Deep Dive B) | Pima Indians Diabetes | Regression | SkinThickness |
| Hands-On Lab | Student Performance | Multiclass classification | GradeClass (0–4) |
| Hands-On Lab (Step 8) | Student Performance | Regression | GPA |

---

## Topics Covered

- What model fit means and its three states: underfitting, good fit, overfitting
- Causes of underfitting: model too simple, weak features, regularization too strong, insufficient training
- Causes of overfitting: model too complex, too many irrelevant features, too little data, noise
- The diagnostic table: reading train vs validation scores together
- Bias and variance as the two fundamental sources of model error
- Irreducible error and why perfect scores are sometimes impossible
- The bias-variance trade-off and the sweet spot
- A practical diagnostic workflow: diagnose before tuning
- Regularization: Ridge (L2) and Lasso (L1) — formulas, intuition, feature selection
- Hyperparameter vs parameter distinction
- Model capacity and the parameters that control it
- Data leakage: four types, detection checklist, target leakage experiment

---

## Hands-On Lab Results

| Step | What I Did | Key Finding |
|------|-----------|-------------|
| Overfit | max_depth=None | Train=1.000, Val=0.832, Gap=0.168 |
| Underfit | max_depth=1 | Train=0.576, Val=0.565, Gap=0.011 |
| Fix | max_depth=5 | Train=0.942, Val=0.898, Gap=0.044  |
| Complexity experiment | depths 1→None | Val peaked at depth=5 |
| Ridge vs Lasso | GPA regression | Lasso zeroed 4/12 features, Val R²=0.955 |
| Learning curve | max_depth=None | Gap stayed wide → complexity problem, not data |
| Final test | Opened once | Test F1 = 0.905  |

---

## Key Findings

**1.** A Train F1 of 1.000 is a warning sign when the gap is large —
it means memorization, not learning.

**2.** A small gap is not automatically evidence of a good model.
Underfitting produces a small gap too — because the model is
equally bad everywhere.

**3.** Lasso zeroed Age, Gender, Ethnicity, ParentalEducation, and
Volunteering from the GPA prediction — confirming that behavioral
factors drive GPA, not demographics.

**4.** The learning curve showed the overfit tree's gap stayed wide
even with more data — the root cause was complexity, not data quantity.

---

## Files

```text
Day 3/
├── day3_bias_variance.ipynb
├── Hands_On_Lab.ipynb
└── README.md

---

## How to Run

1. Activate the project virtual environment (`.venv`)
2. Open either notebook in Jupyter or VS Code
3. Select the `.venv` Python kernel
4. Run all cells from top to bottom

---

## Tools Used

`scikit-learn` • `pandas` • `numpy` • `matplotlib` • Jupyter Notebook