# Cardiac Patient Monitoring System
## Project Plan — BinX Tech AI & ML Internship

**Student:** Nadeen Shadeed
**Track:** AI & Machine Learning
**Project Guide:** Cardiac Patient Monitoring System — AI & ML Track, Student Individual Project Guide
**Plan Date:** Week 5, Day 5
**Status Update:** Week 5 — M6 (Unsupervised Analysis) completed; M7 now in progress

---

## 1. Problem Statement

**Question:** Given a set of clinical measurements for a patient, can a machine learning
model predict whether that patient has heart disease?

**Task type:** Binary classification
**Target variable:** `HeartDisease` — 0 (no disease) / 1 (disease)
**Primary metric:** Disease-class F1-score — chosen because false negatives
(missed disease) are more costly than false positives in a screening context.

**Dataset:** Heart Failure Prediction Dataset (Kaggle) — 918 records, 11 clinical features.
Combines patient records from five registries: Cleveland, Hungarian, Switzerland,
Long Beach VA, and Statlog.

**Scope:** This is an educational machine-learning project.
It uses only tools covered in the training track: Python, NumPy, Pandas,
Matplotlib, Scikit-learn, and Jupyter Notebook.
The model output must not be used for clinical decisions.

---

## 2. Definition of Done

The project is complete when all of the following are true:

- [x] The notebook runs from top to bottom without errors after `Kernel -> Restart & Run All`
- [x] EDA includes descriptive statistics, distributions, class balance, and Matplotlib visualizations
- [x] At least two supervised classification models are trained and compared on the same data split
- [x] Cross-validation and classification metrics (accuracy, precision, recall, F1, AUC-ROC) are reported and explained
- [x] A confusion matrix is included with a plain-language explanation of false positives and false negatives
- [x] Feature engineering is documented with a rationale for each engineered feature
- [x] A Scikit-learn Pipeline combines preprocessing and modelling into one reproducible workflow
- [x] An unsupervised section uses K-Means clustering and PCA with at least one visualization and an interpretation *(exceeded -- DBSCAN, Hierarchical Clustering, t-SNE, and Isolation Forest were also added)*
- [x] `README.md` describes the project objective, dataset, notebook structure, how to run, and known limitations
- [ ] `requirements.txt` allows the environment to be reproduced with `pip install -r requirements.txt`
- [ ] The student can explain the analysis, model choices, metrics, and findings in a 5-10 minute demo without reading from slides

---

## 3. What Has Been Completed (Weeks 1-5)

All work below is in `cardiac_monitoring.ipynb`.

---

### M1 — Environment & Dataset (Days 1-2) ✅

- Loaded the dataset (918 rows, 11 features, 1 target)
- Documented all column types and the target variable `HeartDisease`
- Class balance: 55.3% disease (508), 44.7% no disease (410)
- Identified data quality issues: 172 zero values in `Cholesterol` (clinically invalid),
  1 zero in `RestingBP`

---

### M2 — EDA & Statistics (Days 3-4) ✅

- Descriptive statistics across all numeric features
- Univariate distributions for numeric and categorical features
- Key patterns found:
  - `ASY` chest pain: 79% disease rate vs 14% for `ATA`
  - Exercise angina: 85% disease rate vs 35% without
  - `Flat` ST slope: 83% disease rate; `Up` slope: 20%
- Correlation heatmap identified `ST_Slope`, `ChestPainType`, and `ExerciseAngina`
  as the strongest predictors

---

### M3 — Supervised Baseline (Days 5-6) ✅

- Defined the classification problem with a clear target and metric
- Applied a 60/20/20 stratified train/validation/test split (`stratify=y`)
- Trained Logistic Regression as the baseline (validation set):
  F1 = 0.810, AUC-ROC = 0.893

---

### M4 — Model Comparison & Evaluation (Days 7-8) ✅

- Trained 5 classifiers on the same split: LR, RF, DT, SVM, k-NN
- Selected Random Forest based on the highest validation F1 (0.861) and a strong,
  low-variance cross-validation score (CV F1 mean 0.871, std 0.026)
- Applied GridSearchCV (5-fold, 60 fits) with a documented parameter grid
- Confusion matrix included for the winning model, with a plain-language
  explanation of false negatives (patients with disease classified as healthy —
  the most important error type in a screening context). The precise count is
  reported on the final **test** set in M5 (7 false negatives out of 102 disease
  cases)

| Model | F1 (val) | AUC-ROC | CV F1 Mean |
|---|---|---|---|
| Random Forest | 0.861 | 0.902 | 0.871 |
| SVM | 0.833 | 0.884 | 0.872 |
| k-NN | 0.841 | 0.868 | 0.856 |
| Logistic Regression | 0.810 | 0.893 | 0.877 |
| Decision Tree | 0.837 | 0.862 | 0.845 |

---

### M5 — Feature Engineering & Pipeline (Days 9-10) ✅

- Engineered 4 deterministic features:

| Feature | Formula | Rationale |
|---|---|---|
| `AgeGroup` | Age binned: <45 / 45-55 / 55-65 / 65+ | Non-linear age effects |
| `HRReserve` | `MaxHR / (220 - Age)` | Achieved vs predicted max HR |
| `HighBP` | 1 if `RestingBP > 140` | Clinical BP flag |
| `MaxHR_pct` | `MaxHR / (220 - Age) x 100` | Percentage of predicted max HR |

- Built two Scikit-learn Pipelines (original 11 features, engineered 15 features)
- Tuned both tracks with the same GridSearchCV grid; compared all three RF
  variants (default original, tuned original, tuned engineered) on the
  **validation set only** — the untuned, original-feature Random Forest won
  (highest F1 = 0.861); neither tuning nor feature engineering improved on it
  in this run
- Test set opened once for the winning pipeline:

| Metric | Result |
|---|---|
| Accuracy | 0.90 |
| Precision (disease) | 0.89 |
| Recall (disease) | 0.93 |
| F1-score (disease) | 0.91 |
| AUC-ROC | 0.9248 |

Test-set confusion matrix: 70 true negatives, 12 false positives, **7 false
negatives**, 95 true positives — 95 of 102 disease patients were correctly
identified.

---

### M6 — Unsupervised Analysis (Days 11-12) ✅

**Goal:** Add an unsupervised section to the notebook that explores patient group structure
using K-Means clustering and PCA, then connects the findings back to the supervised results.
*Delivered beyond scope: DBSCAN, Hierarchical Clustering, t-SNE, and Isolation Forest were
added alongside the required K-Means and PCA.*

---

**Task 6.1 — Prepare data for unsupervised analysis** ✅

- All 918 rows encoded and scaled to 15 standardized features (5 numeric,
  1 binary, 9 one-hot categorical); no train/test split used
- `HeartDisease` excluded from the feature matrix throughout fitting
- Markdown cell explains why the full dataset is used (exploratory, not a
  predictive model requiring generalization) and why the target is excluded

---

**Task 6.2 — K-Means clustering with elbow method and silhouette score** ✅

- Elbow plot (inertia vs k=2-10) included; suggested a possible elbow near k=5
- Silhouette score computed for k=2-10; highest at **k=2 (0.1781)** — selected
  as the primary solution, with the low score explicitly flagged as weak
  separation rather than definitive evidence of two natural groups
- Cluster centers compared back to original features (cluster profile table)
- Clusters described in plain language: 514 patients (56.0%) vs 404 (44.0%),
  with a substantially different disease composition — 85.0% vs 17.6% disease
  rate — despite the label never being used to form the clusters

---

**Task 6.3 — PCA: dimensionality reduction and 2D visualization** ✅

- Cumulative explained variance plot (scree plot) included for all 15 components
- Components needed for 95% variance: **13** (97.1% retained); for 80%: **9**
  (81.8% retained) — both reported and justified
- 2D scatter plot (PC1 vs PC2) colors points by `HeartDisease`; classes overlap
  substantially, with only a mild separation trend along PC1
- Feature loadings for PC1 and PC2 inspected; `ST_Slope` and `ExerciseAngina`
  identified as the dominant contributors to PC1
- Markdown cell interprets PC1/PC2 in light of these loadings

---

**Task 6.4 — Connect findings to supervised results** ✅

- Links the PCA loadings directly to Section 5.13's feature importance ranking:
  `ST_Slope_Up`, `ST_Slope_Flat`, `ChestPainType_ASY`, `MaxHR`, and `Oldpeak`
  were the top five features driving the Random Forest's decisions, and the
  same variables (`ST_Slope`, `ExerciseAngina`) dominate PC1 — independent
  confirmation from an unsupervised method that these clinical variables carry
  the primary source of variation in the patient population, not just this one
  model's decision boundary
- States that K-Means and Hierarchical Clustering's post-hoc disease-rate split
  (roughly 80-85% vs 17-20%) agrees with the strong bivariate associations
  found in EDA for `ChestPainType`, `ExerciseAngina`, and `ST_Slope`, while
  DBSCAN's density-based grouping showed a much weaker association — evidence
  that the agreement is structural, not an artifact of one algorithm
- Written in first person, reflecting the student's own interpretation

---

## 4. What Remains — Backlog

---

### M7 — Final Cleanup & Demo (Days 13-14) 🔵 Current

**Goal:** Deliver a submission-ready project: a clean notebook that runs top to bottom,
an updated README, a working requirements file, and a prepared demo.

---

**Task 7.1 — Notebook cleanup**

*Acceptance criteria:*
- `Kernel -> Restart & Run All` completes without errors
- Section numbering is consistent (1-7, including the Unsupervised Analysis
  and Project Summary sections)
- Every output has an explanatory Markdown cell

---

**Task 7.2 — Update README** ✅

*Acceptance criteria:*
- [x] README reflects the full notebook structure including Section 6 (unsupervised)
- [x] The Limitations section is updated: removed the note about missing clustering/PCA;
  replaced with limitations specific to the unsupervised results (low silhouette
  scores, the Isolation Forest contamination assumption)
- [ ] How to Run instructions tested end-to-end in a clean environment — still to verify

---

**Task 7.3 — requirements.txt**

*Acceptance criteria:*
- File exists in project root with pinned versions
- `pip install -r requirements.txt` + `Kernel -> Restart & Run All` completes without errors

---

**Task 7.4 — Demo preparation**

*Acceptance criteria:*
- I can answer without notes: What is the problem? What data? What models? Which won and why?
  What did the unsupervised section reveal?
- I can explain one false negative from the confusion matrix in plain language
- I can explain what the Pipeline does without looking at the code
- I can explain, in plain language, why K-Means/Hierarchical and DBSCAN disagreed
  on cluster structure, and what that means about "one right answer" in
  unsupervised learning

---

## 5. Timeline

```
M1  Days  1-2   DONE  Environment, dataset, cleaning
M2  Days  3-4   DONE  EDA, statistics, visualizations
M3  Days  5-6   DONE  Baseline classifier, train/test split
M4  Days  7-8   DONE  Model comparison, cross-validation, confusion matrix
M5  Days  9-10  DONE  Feature engineering, Pipeline, dual tuning, test evaluation
M6  Days 11-12  DONE  Unsupervised analysis: K-Means, PCA, DBSCAN, Hierarchical, t-SNE, Isolation Forest
M7  Days 13-14  DONE  Final cleanup, README, requirements
```

---

## 6. Project Structure

```
Cardiac_Project/
├── data/
│   └── heart.csv
├── cardiac_monitoring.ipynb    <- main notebook (Sections 1-7, run top to bottom)
├── README.md
```

---

## 7. Known Limitations

- The dataset combines five registries collected at different time periods;
  clinical protocols may differ across sources.
- `Cholesterol` has 172 invalid zero values (18.7%); median imputation inside the
  pipeline introduces uncertainty for this feature.
- Feature engineering and hyperparameter tuning did not outperform the untuned
  Random Forest on original features in this run; the simpler model was
  selected on the validation set.
- All three clustering methods (K-Means, DBSCAN, Hierarchical) produced
  relatively low silhouette scores (0.16-0.25), indicating that the discovered
  patient groupings are exploratory rather than strongly separated, validated
  subtypes.
- Isolation Forest's 5% contamination rate is a modeling assumption, not a
  clinically derived threshold.
- The model was not validated on an independent external dataset.
- This project is educational and must not be used for clinical decisions.