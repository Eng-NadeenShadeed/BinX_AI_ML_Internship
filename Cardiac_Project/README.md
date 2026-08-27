# Cardiac Patient Monitoring System
### Heart Disease Prediction — AI & ML Internship Individual Project
**BinX Tech | Palestine**

---

## Project Overview

This project builds a complete machine learning workflow to analyze cardiac
patient data. It began as a **supervised learning** pipeline to predict whether
a patient has heart disease based on clinical measurements, and was later
extended with an **unsupervised learning** analysis to explore hidden structure,
patient groupings, dimensionality reduction, and unusual observations in the
same feature space — without using the `HeartDisease` label during fitting.

The analysis covers data loading, exploratory data analysis, data quality
handling, feature engineering, model training and comparison, dual
hyperparameter tuning, final evaluation on a held-out test set, clustering,
dimensionality reduction, and anomaly detection.

The project was completed as part of the BinX Tech AI & ML Internship
(Weeks 1–5).

---

## Dataset

**Source:** Heart Failure Prediction Dataset — Kaggle
**Origin:** Combined records from Cleveland, Hungarian, Switzerland, Long Beach VA,
and Statlog registries
**File:** `data/heart.csv`

| Property | Value |
|---|---|
| Observations | 918 |
| Features | 11 original (+ 4 engineered for the supervised track = 15) |
| Target | `HeartDisease` — 0 (no disease) / 1 (disease) — **excluded** from the unsupervised input |
| Class balance | 55.3 % disease / 44.7 % no disease |
| Missing values | None explicit; 1 zero in `RestingBP` and 172 zeros in `Cholesterol` identified as invalid, converted to NaN, and handled using median imputation inside the preprocessing pipeline |

---

## Project Structure

```
Cardiac_Project/
├── data/
│   └── heart.csv
├── cardiac_monitoring.ipynb    ← main notebook (run top to bottom)
└── README.md
```

---

## How to Run

**1. Clone the repository and navigate to the project folder:**
```bash
git clone <your-repo-url>
cd Cardiac_Project
```

**2. Activate the virtual environment:**
```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies** (if not already installed):
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

**4. Open the notebook:**
```bash
jupyter notebook cardiac_monitoring.ipynb
```

**5. Run all cells top to bottom:**
`Kernel → Restart & Run All`

The notebook is fully self-contained and requires no manual steps between cells.

---

## Notebook Structure

| Section | Subsections | Content |
|---|---|---|
| 1. Loading the Dataset | 1.1 – 1.3 | Environment setup, data loading, initial shape inspection |
| 2. Understanding the Dataset | 2.1 – 2.3 | Column types, missing value check, categorical identification |
| 3. Exploratory Data Analysis | 3.1 – 3.6 | Univariate analysis (categorical + numerical), target distribution, feature-target relationships, correlation heatmap, EDA summary |
| 4. Data Quality & Preparation | 4.1 – 4.9 | Duplicates, suspicious zeros, negative values, NaN conversion, categorical consistency, data quality summary |
| 5. Machine Learning Pipeline | 5.1 – 5.13 | See supervised pipeline breakdown below |
| 6. Unsupervised Analysis | 6.1 – 6.9 | See unsupervised breakdown below |
| 7. Project Summary | — | Pipeline steps completed, key findings, limitations |

### Section 5 Breakdown — Supervised Pipeline

| Subsection | Content |
|---|---|
| 5.1 Original Feature Set | Define `X_original` (11 features) and `y` |
| 5.2 Train / Validation / Test Split | 60 / 20 / 20 % stratified split — before any modelling |
| 5.3 Preprocessing Pipeline — Original | `preprocessor_original` for 11-feature track |
| 5.4 Baseline + Model Comparison | LR, RF, DT, SVM, k-NN evaluated on validation (original features) |
| 5.5 Random Forest Selection | Documented rationale for selecting RF |
| 5.6 Original RF Performance | Untuned RF baseline — pre-tuning reference |
| 5.7 Feature Engineering | 4 deterministic features added; `X_engineered` built via index alignment |
| 5.8 Preprocessing Pipeline — Engineered | `preprocessor_engineered` for 15-feature track |
| 5.9 Hyperparameter Tuning — Original | GridSearchCV on 11-feature pipeline |
| 5.10 Hyperparameter Tuning — Engineered | GridSearchCV on 15-feature pipeline (same grid) |
| 5.11 Validation Comparison | Side-by-side comparison → winner chosen on validation only |
| 5.12 Final Test Evaluation | Test set opened once for the winning model |
| 5.13 Feature Importance | Importance chart for the winning pipeline |

### Section 6 Breakdown — Unsupervised Analysis

| Subsection | Content |
|---|---|
| 6.1 Data Preparation | Numeric (median impute → scale), binary (scale), categorical (OHE drop-first → scale) → 15 standardized features; `HeartDisease` excluded |
| 6.2 PCA | Full explained-variance breakdown, scree plot, PC1/PC2 loadings, 2D projection colored by `HeartDisease` (post-hoc) |
| 6.3 K-Means Clustering | K selection via Elbow + Silhouette, final clustering, cluster profiles, PCA visualization, crosstab vs `HeartDisease` |
| 6.4 DBSCAN | k-distance analysis for `eps` selection, candidate comparison, final model, PCA visualization, crosstab vs `HeartDisease` |
| 6.5 Hierarchical Clustering | Ward-linkage dendrogram, cluster assignment, Silhouette score, PCA visualization, crosstab vs `HeartDisease` |
| 6.6 Clustering Comparison | Side-by-side comparison of K-Means, DBSCAN, and Hierarchical results |
| 6.7 t-SNE Visualization | Non-linear 2D embedding, unlabeled and label-colored projections |
| 6.8 Isolation Forest | Anomaly detection (5 % contamination), PCA visualization, crosstab vs `HeartDisease` |
| 6.9 Unsupervised Analysis Summary | Consolidated findings across all techniques |

---

## Supervised Machine Learning Pipeline

### Feature Engineering

Four deterministic features are created from existing columns using fixed
formulas. No statistics are learned from the data at this stage, so no
information from the validation or test sets influences the engineered values.

| Feature | Formula | Rationale |
|---|---|---|
| `AgeGroup` | Age binned: `<45` / `45–55` / `55–65` / `65+` | Captures non-linear age effects in clinically meaningful ranges |
| `HRReserve` | `MaxHR / (220 − Age)` | Ratio of achieved to age-predicted maximum HR; values < 1 indicate reduced exercise capacity |
| `HighBP` | `1` if `RestingBP > 140`, else `0` | Clinical blood pressure flag |
| `MaxHR_pct` | `MaxHR / (220 − Age) × 100` | Percentage of age-predicted maximum HR achieved |

### Two Separate Preprocessing Pipelines

The pipeline is built in two versions to allow a fair comparison between the
original and engineered feature sets. Both use the same transformer logic;
only the feature lists differ.

**`preprocessor_original` — 11 features**

| Group | Features | Steps |
|---|---|---|
| Numeric | `Age`, `RestingBP`, `Cholesterol`, `MaxHR`, `Oldpeak` | Median imputation → StandardScaler |
| Binary | `FastingBS` | Passthrough |
| Categorical | `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope` | OneHotEncoder |

**`preprocessor_engineered` — 15 features**

| Group | Features | Steps |
|---|---|---|
| Numeric | `Age`, `RestingBP`, `Cholesterol`, `MaxHR`, `Oldpeak`, `HRReserve`, `MaxHR_pct` | Median imputation → StandardScaler |
| Binary | `FastingBS`, `HighBP` | Passthrough |
| Categorical | `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope`, `AgeGroup` | OneHotEncoder |

### Train / Validation / Test Split

The split is performed on the **original** feature set before any modelling or
feature engineering. The engineered feature sets are aligned to the same split
using index matching, ensuring that both tracks see identical observations.

| Subset | Size | Purpose |
|---|---|---|
| Training | 60 % — 550 observations | Model parameter learning |
| Validation | 20 % — 184 observations | Model comparison, winner selection |
| Test | 20 % — 184 observations | One-time final evaluation for the winning model |

`stratify=y` used throughout to preserve class balance across all subsets.

### Model Comparison (Validation Set — Disease-Class F1)

All five models are evaluated on the same training and validation sets using
`preprocessor_original`. The comparison guides Random Forest selection before
feature engineering begins.

| Model | Accuracy | Precision | Recall | F1 (class 1) | AUC-ROC | CV F1 Mean |
|---|---|---|---|---|---|---|
| Random Forest | 0.842 | 0.841 | 0.882 | 0.861 | 0.902 | 0.871 |
| SVM | 0.815 | 0.833 | 0.833 | 0.833 | 0.884 | 0.872 |
| k-NN | 0.821 | 0.829 | 0.853 | 0.841 | 0.868 | 0.856 |
| Decision Tree | 0.815 | 0.821 | 0.853 | 0.837 | 0.862 | 0.845 |
| Logistic Regression (baseline) | 0.793 | 0.827 | 0.794 | 0.810 | 0.893 | 0.877 |

> All models evaluated on the same train / validation split using original 11 features.

**Random Forest is selected** based on highest F1, strong Recall, competitive
AUC-ROC, and low CV standard deviation (robustness across folds).

### Dual Hyperparameter Tuning

GridSearchCV with 5-fold CV is applied twice — once per feature track — using
**the same parameter grid** to ensure a fair comparison:

```
n_estimators:      [100, 200]
max_depth:         [5, 10, None]
min_samples_split: [2, 5]
```

12 combinations × 5 folds = **60 fits per track**.

| Track | Features | Best Hyperparameters | Best CV F1 |
|---|---|---|---|
| Original (5.9) | 11 | `max_depth=10, min_samples_split=5, n_estimators=200` | 0.8818 |
| Engineered (5.10) | 15 | `max_depth=5, min_samples_split=5, n_estimators=200` | 0.8734 |

### Winner Selection

The three RF variants (default original, tuned original, tuned engineered) are
compared **on the validation set only** in Section 5.11. The model with the
highest disease-class F1 is selected as the final model. The test set is never
consulted during this decision.

| Model | Accuracy | Precision | Recall | F1 | AUC-ROC |
|---|---|---|---|---|---|
| **Default RF — Original (11 feat)** | **0.842** | **0.841** | **0.882** | **0.861** | **0.902** |
| Tuned RF — Original (11 feat) | 0.826 | 0.830 | 0.863 | 0.846 | 0.899 |
| Tuned RF — Engineered (15 feat) | 0.804 | 0.824 | 0.824 | 0.824 | 0.899 |

**✔ Selected model: Default RF — Original (11 features).** Neither hyperparameter
tuning nor feature engineering improved on the untuned baseline's validation F1
in this run, so the untuned original-feature Random Forest is carried forward
to the final test evaluation.

### Final Results — Test Set

The values below are from the winning model evaluated once on the held-out test
set (Section 5.12). Exact figures depend on which model wins the validation
comparison upon execution.

| Metric | Value |
|---|---|
| Accuracy | 0.90 |
| Precision (class 1) | 0.89 |
| Recall (class 1) | 0.93 |
| F1-score (class 1) | 0.91 |
| AUC-ROC | 0.9248 |

**Confusion Matrix**

```
                    Predicted
                 No Disease   Disease
Actual
No Disease           70          12
Disease              7           95
```

> 95 out of 102 patients with heart disease were correctly identified.
> The 7 False Negatives represent the most important error type in a screening
> context — patients with disease classified as healthy.

---

## Unsupervised Analysis

Section 6 shifts the question from *"does this patient have heart disease?"* to
*"does the patient feature space contain structure, groups, or unusual
observations on its own?"* The `HeartDisease` label is excluded from every
fitting step in this section and is used only afterward, post-hoc, to help
interpret what the discovered structure represents.

### Data Preparation

The 11 original features (excluding the target) are transformed into
**15 standardized features**:

| Group | Features | Steps |
|---|---|---|
| Numeric | `Age`, `RestingBP`, `Cholesterol`, `MaxHR`, `Oldpeak` | Median imputation → StandardScaler |
| Binary | `FastingBS` | StandardScaler |
| Categorical | `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope` | OneHotEncoder (`drop="first"`) → StandardScaler |

One-hot encoded columns are scaled as well, so that categorical frequency
does not distort distance-based methods (K-Means) or the variance structure
used by PCA.

### PCA — Dimensionality Reduction

| Metric | Value |
|---|---|
| PC1 explained variance | 22.4 % |
| PC2 explained variance | 11.0 % |
| PC1 + PC2 combined | 33.4 % |
| Components needed for ≥ 80 % variance | 9 (81.8 % retained) |
| Components needed for ≥ 95 % variance | 13 (97.1 % retained) |

The 2D PC1–PC2 projection shows substantial overlap between the two
`HeartDisease` classes, with only a mild separation trend along PC1 —
consistent with `ST_Slope` and `ExerciseAngina` being the top-loading
features on that component.

### Clustering Comparison

| Method | Clusters / Noise | Silhouette Score | Cluster Balance | Post-hoc `HeartDisease` Pattern |
|---|---|---:|---|---|
| K-Means (K=2) | 2 clusters | 0.1781 | 56.0 % / 44.0 % | Strong difference (85.0 % vs 17.6 % disease rate) |
| DBSCAN (eps=4.0, min_samples=5) | 2 clusters + 3 noise | **0.2518** | 94.8 % / 4.9 % / 0.3 % | Weaker difference (56.1 % vs 44.4 %) |
| Hierarchical (Ward, K=2) | 2 clusters | 0.1631 | 41.8 % / 58.2 % | Strong difference (80.3 % vs 20.6 % disease rate) |

- **K-Means** (K selected via Silhouette Score, not the Elbow Method) and
  **Hierarchical Clustering** independently converge on a similar pattern:
  two moderately balanced groups with substantially different disease rates.
- **DBSCAN** reveals a different, density-based structure: one dominant
  cluster (94.8 % of observations), a small secondary cluster, and 3 noise
  points — with a much weaker association to `HeartDisease`.

### t-SNE Visualization

A non-linear complement to PCA: t-SNE preserves local neighborhood
relationships rather than global variance. Applied to the same 15
standardized features, it reveals additional locally distinct regions not
visible in the linear PCA projection, broadly consistent with the clustering
results.

### Isolation Forest — Anomaly Detection

| Metric | Value |
|---|---|
| Contamination rate (assumption) | 5 % |
| Anomalies detected | 46 observations (5.0 %) |
| Normal observations | 872 (95.0 %) |
| Disease rate — anomaly group | 45.7 % |
| Disease rate — normal group | 55.8 % |

The difference in disease rate between the anomaly and normal groups is
present but modest; anomaly status here reflects statistical unusualness in
the feature space, not clinical severity.

---

## Key Findings

**Supervised**
- `ST_Slope`, `ChestPainType`, and `ExerciseAngina` are the strongest predictors —
  consistent across EDA and feature importance analysis.
- Patients with `ASY` chest pain had a ~79 % heart disease rate vs ~14 % for `ATA`.
- Patients with exercise-induced angina had an ~85 % heart disease rate vs ~35 % without.
- `Flat` ST slope: ~83 % disease rate; `Up` slope: ~20 % disease rate.
- Feature engineering (4 added features) did not outperform the original
  11 features on the validation set. The default Random Forest on original
  features was selected as the final model.
- The feature importance analysis confirmed the EDA findings: `ST_Slope_Up`,
  `ST_Slope_Flat`, `ChestPainType_ASY`, `MaxHR`, and `Oldpeak` are the
  top five contributors to the winning model's decisions.
- The dual-tuning structure (Sections 5.9 vs 5.10) isolates the contribution of
  feature engineering from hyperparameter tuning, making the comparison rigorous
  and interpretable.
- The final model is selected on the **validation set** and evaluated once on
  the **test set** — ensuring leakage-free final metrics.

**Unsupervised**
- Structure discovered entirely without the `HeartDisease` label (K-Means,
  Hierarchical) aligns closely with the true label distribution when compared
  post-hoc — evidence that the disease-related signal is embedded in the
  feature-space geometry itself, not only in the supervised model's decision
  boundary.
- Different algorithms surface different aspects of the same feature space:
  K-Means and Hierarchical Clustering agree on a balanced two-group structure;
  DBSCAN instead highlights one dominant dense region and a small secondary
  group; PCA and t-SNE offer complementary global vs. local views.
- All Silhouette Scores (0.16–0.25) indicate that no method found strongly
  separated, well-defined clusters — the discovered groupings are exploratory
  patient groupings, not diagnostic categories.
- Isolation Forest flags a small subset (5 %) of statistically unusual
  patients, with only a modest link to actual disease status.

---

## Limitations

- The dataset combines five registries collected decades apart; clinical protocols
  may differ across sources.
- `Cholesterol` has 172 missing values (18.7 %) after zero-value conversion;
  median imputation introduces uncertainty for this feature specifically.
- Clustering solutions across all three methods show relatively low Silhouette
  Scores, indicating limited natural separation in the feature space; the
  discovered groups should be treated as exploratory, not clinically validated
  patient subtypes.
- Isolation Forest's 5 % contamination rate is a modeling assumption, not a
  clinically derived threshold.
- The model was not validated on an independent external dataset and must not
  be used for clinical decisions.

---

## Tools & Libraries

| Tool | Version |
|---|---|
| Python | 3.10+ |
| pandas | 3.x |
| numpy | 2.x |
| matplotlib | 3.x |
| seaborn | 0.13.x |
| scikit-learn | 1.8.x |
| scipy | 1.x |
| Jupyter Notebook | — |

---

## Author

BinX Tech AI & ML Internship — Individual Project
Track: AI & Machine Learning | Weeks 1–5