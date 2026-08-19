# Cardiac Patient Monitoring System
### Heart Disease Prediction — AI & ML Internship Individual Project
**BinX Tech | Palestine**

---

## Project Overview

This project builds a complete supervised machine learning pipeline to predict
whether a patient has heart disease based on clinical measurements. The analysis
covers data loading, exploratory data analysis, data quality handling, feature
engineering, model training and comparison, dual hyperparameter tuning, and final
evaluation on a held-out test set.

The project was completed as part of the BinX Tech AI & ML Internship (Weeks 1–4).

---

## Dataset

**Source:** Heart Disease Prediction Dataset — Kaggle  
**Origin:** Combined records from Cleveland, Hungarian, Switzerland, Long Beach VA,
and Stalog registries  
**File:** `data/heart.csv`

| Property | Value |
|---|---|
| Observations | 918 |
| Features | 11 original + 4 engineered = 15 |
| Target | `HeartDisease` — 0 (no disease) / 1 (disease) |
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
pip install pandas numpy matplotlib seaborn scikit-learn
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
| 5. Machine Learning Pipeline | 5.1 – 5.13 | See pipeline breakdown below |
| 6. Project Summary | — | Pipeline steps completed, key findings, limitations |

### Section 5 Breakdown

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

---

## Machine Learning Pipeline

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
| Random Forest | 0.832 | 0.831 | 0.832 | 0.831 | 0.898 | 0.862 |
| SVM | 0.815 | 0.815 | 0.815 | 0.815 | 0.888 | 0.869 |
| k-NN | 0.788 | 0.788 | 0.788 | 0.788 | 0.862 | 0.857 |
| Logistic Regression (baseline) | 0.783 | 0.790 | 0.783 | 0.800 | 0.895 | 0.870 |
| Decision Tree | 0.766 | 0.766 | 0.766 | 0.766 | 0.821 | 0.825 |

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

| Track | Features | Best CV F1 |
|---|---|---|
| Original (5.9) | 11 | reported after execution |
| Engineered (5.10) | 15 | reported after execution |

### Winner Selection

The three RF variants (default original, tuned original, tuned engineered) are
compared **on the validation set only** in Section 5.11. The model with the
highest disease-class F1 is selected as the final model. The test set is never
consulted during this decision.

---

## Final Results — Test Set

The values below are from the winning model evaluated once on the held-out test
set (Section 5.12). Exact figures depend on which model wins the validation
comparison upon execution.

| Metric | Value |
|---|---|
| Accuracy | 0.86 |
| Precision (class 1) | 0.87 |
| Recall (class 1) | 0.89 |
| F1-score (class 1) | 0.88 |
| AUC-ROC | 0.916 |

### Confusion Matrix

```
                    Predicted
                 No Disease   Disease
Actual
No Disease           68          14
Disease              11          91
```

> 91 out of 102 patients with heart disease were correctly identified.  
> The 11 False Negatives represent the most important error type in a screening
> context — patients with disease classified as healthy.

---

## Key Findings

- `ST_Slope`, `ChestPainType`, and `ExerciseAngina` are the strongest predictors —
  consistent across EDA and feature importance analysis.
- Patients with `ASY` chest pain had a ~79 % heart disease rate vs ~14 % for `ATA`.
- Patients with exercise-induced angina had an ~85 % heart disease rate vs ~35 % without.
- `Flat` ST slope: ~83 % disease rate; `Up` slope: ~20 % disease rate.
- `HRReserve` and `MaxHR_pct` appeared among the top 10 feature importances,
  confirming that the engineered Age–MaxHR interaction carries additional signal
  beyond the raw columns alone.
- The dual-tuning structure (Sections 5.9 vs 5.10) isolates the contribution of
  feature engineering from hyperparameter tuning, making the comparison rigorous
  and interpretable.
- The final model is selected on the **validation set** and evaluated once on
  the **test set** — ensuring leakage-free final metrics.

---

## Limitations

- The dataset combines five registries collected decades apart; clinical protocols
  may differ across sources.
- `Cholesterol` has 172 missing values (18.7 %) after zero-value conversion;
  median imputation introduces uncertainty for this feature specifically.
- No unsupervised analysis (clustering, PCA) was included — outside the scope
  of the first four training weeks.
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
| Jupyter Notebook | — |

---

## Author

BinX Tech AI & ML Internship — Individual Project  
Track: AI & Machine Learning | Weeks 1–4