# Cardiac Patient Monitoring System
## Project Plan — BinX Tech AI & ML Internship

**Student:** [Your Name]  
**Track:** AI & Machine Learning  
**Project Guide:** Cardiac Patient Monitoring System — AI & ML Track, Student Individual Project Guide  
**Plan Date:** Week 5, Day 5

---

## 1. Problem Statement

**Question:** Given a set of clinical measurements for a patient, can a machine learning
model predict whether that patient has heart disease?

**Task type:** Binary classification  
**Target variable:** `HeartDisease` — 0 (no disease) / 1 (disease)  
**Primary metric:** Disease-class F1-score — chosen because false negatives
(missed disease) are more costly than false positives in a screening context.

**Dataset:** Heart Disease Prediction Dataset (Kaggle) — 918 records, 11 clinical features.
Combines patient records from five registries: Cleveland, Hungarian, Switzerland,
Long Beach VA, and Stalog.

**Scope:** This is an educational machine-learning project.
It uses only tools covered in the training track: Python, NumPy, Pandas,
Matplotlib, Scikit-learn, and Jupyter Notebook.
The model output must not be used for clinical decisions.

---

## 2. Definition of Done

The project is complete when all of the following are true:

- [ ] The notebook runs from top to bottom without errors after `Kernel → Restart & Run All`
- [ ] EDA includes descriptive statistics, distributions, class balance, and Matplotlib visualizations
- [ ] At least two supervised classification models are trained and compared on the same data split
- [ ] Cross-validation and classification metrics (accuracy, precision, recall, F1, AUC-ROC) are reported and explained
- [ ] A confusion matrix is included with a plain-language explanation of false positives and false negatives
- [ ] Feature engineering is documented with a rationale for each engineered feature
- [ ] A Scikit-learn Pipeline combines preprocessing and modelling into one reproducible workflow
- [ ] An unsupervised section uses K-Means clustering and PCA with at least one visualization and an interpretation
- [ ] `README.md` describes the project objective, dataset, notebook structure, how to run, and known limitations
- [ ] `requirements.txt` allows the environment to be reproduced with `pip install -r requirements.txt`
- [ ] The student can explain the analysis, model choices, metrics, and findings in a 5–10 minute demo without reading from slides

---

## 3. What Has Been Completed (Weeks 1–4)

All work below is in `cardiac_monitoring.ipynb`.

---

### M1 — Environment & Dataset (Days 1–2) ✅

- Loaded the dataset (918 rows, 11 features, 1 target)
- Documented all column types and the target variable `HeartDisease`
- Class balance: 55.3% disease (508), 44.7% no disease (410)
- Identified data quality issues: 172 zero values in `Cholesterol` (clinically invalid),
  1 zero in `RestingBP`

---

### M2 — EDA & Statistics (Days 3–4) ✅

- Descriptive statistics across all numeric features
- Univariate distributions for numeric and categorical features
- Key patterns found:
  - `ASY` chest pain: 79% disease rate vs 14% for `ATA`
  - Exercise angina: 85% disease rate vs 35% without
  - `Flat` ST slope: 83% disease rate; `Up` slope: 20%
- Correlation heatmap identified `ST_Slope`, `ChestPainType`, and `ExerciseAngina`
  as the strongest predictors

---

### M3 — Supervised Baseline (Days 5–6) ✅

- Defined the classification problem with a clear target and metric
- Applied a 60/20/20 stratified train/validation/test split (`stratify=y`)
- Trained Logistic Regression as the baseline:
  F1 = 0.800, AUC-ROC = 0.895 (validation set)

---

### M4 — Model Comparison & Evaluation (Days 7–8) ✅

- Trained 5 classifiers on the same split: LR, RF, DT, SVM, k-NN
- Selected Random Forest based on highest validation F1 (0.831) and strong CV score
- Applied GridSearchCV (5-fold, 60 fits) with documented parameter grid
- Confusion matrix with explanation of the 11 false negatives (patients with disease
  classified as healthy — the most important error type in screening)

| Model | F1 (val) | AUC-ROC | CV F1 |
|---|---|---|---|
| Random Forest | 0.831 | 0.898 | 0.862 |
| SVM | 0.815 | 0.888 | 0.869 |
| k-NN | 0.788 | 0.862 | 0.857 |
| Logistic Regression | 0.800 | 0.895 | 0.870 |
| Decision Tree | 0.766 | 0.821 | 0.825 |

---

### M5 — Feature Engineering & Pipeline (Days 9–10) ✅

- Engineered 4 deterministic features:

| Feature | Formula | Rationale |
|---|---|---|
| `AgeGroup` | Age binned: <45 / 45–55 / 55–65 / 65+ | Non-linear age effects |
| `HRReserve` | `MaxHR / (220 − Age)` | Achieved vs predicted max HR |
| `HighBP` | 1 if `RestingBP > 140` | Clinical BP flag |
| `MaxHR_pct` | `MaxHR / (220 − Age) × 100` | Percentage of predicted max HR |

- Built two Scikit-learn Pipelines (original 11 features, engineered 15 features)
- Compared both tracks on validation set; selected winning model
- Test set opened once for the winning pipeline:

| Metric | Result |
|---|---|
| Accuracy | 0.86 |
| Precision (disease) | 0.87 |
| Recall (disease) | 0.89 |
| F1-score (disease) | 0.88 |
| AUC-ROC | 0.916 |

---

## 4. What Remains — Backlog

---

### M6 — Unsupervised Analysis (Days 11–12) 🔵 Current

**Goal:** Add an unsupervised section to the notebook that explores patient group structure
using K-Means clustering and PCA, then connects the findings back to the supervised results.

---

**Task 6.1 — Prepare data for unsupervised analysis**

*What:* Encode and scale the full dataset (all 918 rows, no train/test split,
target excluded — unsupervised learning does not use labels).

*Acceptance criteria:*
- Categorical features are one-hot encoded
- All features are scaled with `StandardScaler`
- `HeartDisease` is excluded from the feature matrix
- A Markdown cell explains why the full dataset is used and why the target is excluded

---

**Task 6.2 — K-Means clustering with elbow method and silhouette score**

*What:* Find natural patient groupings. Use the elbow method and silhouette score to choose k.
Describe each cluster in plain language using original feature means.

*Acceptance criteria:*
- Elbow plot (inertia vs k=2–10) is included
- Silhouette score is computed for the chosen k and reported
- Cluster centers are compared back to original features
- Each cluster is described in plain language (not just numbers)
- A Markdown cell documents the chosen k and why

---

**Task 6.3 — PCA: dimensionality reduction and 2D visualization**

*What:* Apply PCA and reduce to 2D for visualization.
Color the scatter plot by `HeartDisease` label to check whether the supervised target
aligns with the unsupervised structure.

*Acceptance criteria:*
- Cumulative explained variance plot is included
- Number of components needed for 95% variance is reported and justified
- A 2D scatter plot colors points by `HeartDisease` (0 vs 1)
- Feature loadings for PC1 and PC2 are inspected and the dominant features are named
- A Markdown cell interprets what each component appears to represent

---

**Task 6.4 — Connect findings to supervised results**

*What:* A Markdown cell that links clustering/PCA findings back to the EDA
and feature importance from M2–M5.

*Acceptance criteria:*
- References at least one specific finding from EDA or feature importance
- States whether the unsupervised structure agrees with the supervised findings
- Written in first person and reflects the student's own interpretation

---

### M7 — Final Cleanup & Demo (Days 13–14) ⬜ Planned

**Goal:** Deliver a submission-ready project: a clean notebook that runs top to bottom,
an updated README, a working requirements file, and a prepared demo.

---

**Task 7.1 — Notebook cleanup**

*Acceptance criteria:*
- `Kernel → Restart & Run All` completes without errors
- Section numbering is consistent (1–6)
- Every output has an explanatory Markdown cell

---

**Task 7.2 — Update README**

*Acceptance criteria:*
- README reflects the full notebook structure including Section 6 (unsupervised)
- The Limitations section is updated: remove the note about missing clustering/PCA
- How to Run instructions are tested and correct

---

**Task 7.3 — requirements.txt**

*Acceptance criteria:*
- File exists in project root with pinned versions
- `pip install -r requirements.txt` + `Kernel → Restart & Run All` completes without errors

---

**Task 7.4 — Demo preparation**

*Acceptance criteria:*
- I can answer without notes: What is the problem? What data? What models? Which won and why?
  What did the unsupervised section reveal?
- I can explain one false negative from the confusion matrix in plain language
- I can explain what the Pipeline does without looking at the code

---

## 5. Timeline

```
M1  Days  1–2   ✅  Environment, dataset, cleaning
M2  Days  3–4   ✅  EDA, statistics, visualizations
M3  Days  5–6   ✅  Baseline classifier, train/test split
M4  Days  7–8   ✅  Model comparison, cross-validation, confusion matrix
M5  Days  9–10  ✅  Feature engineering, Pipeline, dual tuning, test evaluation
─────────────────────────────────────────────────────────────────────────────
M6  Days 11–12  🔵  Unsupervised analysis: K-Means + PCA        ← current
M7  Days 13–14  ⬜  Final cleanup, README, requirements, demo
```

---

## 6. Project Structure

```
Cardiac_Project/
├── data/
│   └── heart.csv
├── cardiac_monitoring.ipynb    ← main notebook (Sections 1–6, run top to bottom)
├── README.md
```

---

## 7. Known Limitations

- The dataset combines five registries collected at different time periods;
  clinical protocols may differ across sources.
- `Cholesterol` has 172 invalid zero values (18.7%); median imputation inside the
  pipeline introduces uncertainty for this feature.
- The model was not validated on an independent external dataset.
- This project is educational and must not be used for clinical decisions.