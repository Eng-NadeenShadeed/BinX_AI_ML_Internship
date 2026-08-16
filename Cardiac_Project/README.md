# Cardiac Patient Monitoring System
### Heart Disease Prediction — AI & ML Internship Individual Project
**BinX Tech | Palestine**

---

## Project Overview

This project builds a complete supervised machine learning pipeline to predict
whether a patient has heart disease based on clinical measurements. The analysis
covers data loading, exploratory data analysis, data quality handling, feature
engineering, model training and comparison, hyperparameter tuning, and final
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
| Features | 11 original + 3 engineered = 14 |
| Target | `HeartDisease` — 0 (no disease) / 1 (disease) |
| Class balance | 55.3% disease / 44.7% no disease |
| Missing values | None explicit; 172 zero values in `Cholesterol` identified as invalid, converted to NaN, and handled using median imputation inside the preprocessing pipeline |

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

**2. Activate the training virtual environment:**
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

| Section | Content |
|---|---|
| 1. Loading the Dataset | Data loading, first inspection, shape |
| 2. Dataset Structure | Column types, categorical identification |
| 3. Univariate Analysis — Categorical | Frequency distributions for all 5 categorical features |
| 4. Univariate Analysis — Numerical | Histograms, boxplots, outlier analysis, descriptive stats |
| 5. Target Variable Analysis | Class balance, distribution |
| 6. Feature vs Target Analysis | Bivariate analysis — each feature vs `HeartDisease` |
| 7. Correlation Analysis | Pearson matrix, heatmap, scatter plots |
| 8. Data Quality & Preparation | Duplicates, zeros, negatives, NaN conversion |
| 9. Machine Learning Pipeline | Feature engineering → split → preprocessing → models → tuning → final eval |
| 10. Project Summary | Key findings, metrics, limitations |

---

## Machine Learning Pipeline

### Feature Engineering
Three features added before splitting using deterministic transformations that do not learn statistics from the dataset:

| Feature | Construction | Rationale |
|---|---|---|
| `AgeGroup` | Age binned: <45 / 45–55 / 55–65 / 65+ | Captures non-linear age effects |
| `HRReserve` | `220 − Age − MaxHR` | Encodes unused heart rate capacity |
| `HighBP` | `1` if `RestingBP > 140` else `0` | Clinical blood pressure flag |

### Preprocessing Pipeline (ColumnTransformer)

| Group | Features | Steps |
|---|---|---|
| Numeric | Age, RestingBP, Cholesterol, MaxHR, Oldpeak, HRReserve | Median imputation → StandardScaler |
| Binary | FastingBS, HighBP | Passthrough |
| Categorical | Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope, AgeGroup | OneHotEncoder |

### Train / Validation / Test Split
- Training: 60% (550 observations)
- Validation: 20% (184 observations)
- Test: 20% (184 observations)
- `stratify=y` used throughout to preserve class balance across all subsets

### Model Comparison (Validation Set — Weighted F1)

| Model | Accuracy | Precision | Recall | F1 (weighted) | AUC-ROC | CV F1 Mean |
|---|---|---|---|---|---|---|
| Random Forest | 0.832 | 0.831 | 0.832 | 0.831 | 0.898 | 0.862 |
| SVM | 0.815 | 0.815 | 0.815 | 0.815 | 0.888 | 0.869 |
| k-NN | 0.788 | 0.788 | 0.788 | 0.788 | 0.862 | 0.857 |
| Logistic Regression (baseline) | 0.783 | 0.790 | 0.783 | 0.780 | 0.895 | 0.870 |
| Decision Tree | 0.766 | 0.766 | 0.766 | 0.766 | 0.821 | 0.825 |

> All models evaluated on the same train/validation split.  
> Positive-class F1 for the Logistic Regression baseline = 0.80 (reported separately in Section 9.5).

### Hyperparameter Tuning
GridSearchCV with 5-fold CV over 12 Random Forest configurations.  
Best: `n_estimators=100`, `max_depth=5`, `min_samples_split=2`  
Best CV F1: **0.8795**

> The Random Forest CV F1 in the comparison table (0.862) used default settings
> (`max_depth=None`). The tuned CV F1 (0.8795) reflects the best configuration
> found across 12 combinations — this is expected, as GridSearchCV selects the
> most generalizable configuration, not necessarily the highest-scoring default.

---

## Final Results — Test Set

| Metric | Value |
|---|---|
| Accuracy | 0.86 |
| F1-score (positive class) | 0.88 |
| Precision | 0.87 |
| Recall | 0.89 |
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
> The 11 False Negatives represent the most important error type to monitor
> in a screening context.

---

## Key Findings

- `ST_Slope`, `ChestPainType`, and `ExerciseAngina` are the strongest predictors —
  consistent across EDA and feature importance analysis.
- Patients with `ASY` chest pain had a ~79% heart disease rate vs ~14% for `ATA`.
- Patients with exercise-induced angina had an ~85% heart disease rate vs ~35% without.
- `Flat` ST slope: ~83% disease rate; `Up` slope: ~20% disease rate.
- `HRReserve` appeared among the top 10 features, suggesting that the engineered
  combination of age and maximum heart rate provides useful signal for the model.
- The final model makes 11 False Negatives out of 184 test cases — the most
  important error type to monitor in a screening context.

---

## Limitations

- The dataset combines five registries collected decades apart; clinical protocols
  may differ across sources.
- `Cholesterol` has 172 missing values (18.7%) after zero-value conversion;
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