# Week 5 — Unsupervised Learning

## Overview

Week 5 introduces unsupervised learning — working with data that has no labels.
Where Weeks 1–4 always provided the model with correct answers to learn from,
Week 5 gives it data only and asks it to find structure on its own.

The week covers three families of techniques: clustering (grouping similar points),
dimensionality reduction (compressing many features into fewer while keeping most
of the information), and anomaly detection (finding points that differ significantly
from the norm).

All practical work uses the same `insurance.csv` dataset across Days 1–4,
allowing a direct comparison of what each method reveals about the same data.
Day 5 shifts to project planning: selecting the individual capstone project
and preparing a signed-off Sprint 1 plan before Phase 3 begins.

---

## Repository Structure

```
Week5/
├── Day1/
│   ├── day1_kmeans_clustering.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day2/
│   ├── day2_dbscan_hierarchical.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day3/
│   ├── day3_pca.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day4/
│   ├── day4_tsne_anomaly.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day5/
│   ├── project_plan.md
│   └── README.md
├── data/
│   └── insurance.csv
└── README.md
```

---

## Dataset

**insurance.csv** — Medical Cost Personal Dataset  
1,338 records · 7 original columns · 9 after one-hot encoding · no missing values

| Column | Type | Description |
|--------|------|-------------|
| `age` | numeric | Patient age in years |
| `sex` | categorical | male / female |
| `bmi` | numeric | Body mass index |
| `children` | numeric | Number of dependents |
| `smoker` | categorical | yes / no |
| `region` | categorical | US region (4 values) |
| `charges` | numeric | Annual medical cost in USD |

Key finding carried from Week 2 EDA: smoker status is the dominant driver of charges.
This pattern reappears consistently across every unsupervised method applied this week.

---

## Daily Progress

### Day 1 — K-Means Clustering 

**Theory notebook:** What clustering is, how K-Means works step by step
(centroid assignment, iteration, convergence), the Inertia metric, elbow method,
silhouette score, K-Means limitations.

**Hands-On Lab:** Applied K-Means to the insurance dataset.

- One-hot encoded sex, smoker, region → 9 features
- Scaled with `StandardScaler` (required: K-Means uses distances)
- Ran elbow method (k=2–10) → elbow at k=4
- Silhouette score at k=4: **0.28** — reasonable for real-world data
- Fitted K-Means k=4, plotted scatter colored by cluster
- Profiled each cluster using original feature means:
  - Cluster with high-BMI smokers and extreme charges
  - Young non-smokers with low charges
  - Older non-smokers with moderate-high charges
  - Young smokers with moderate charges

---

### Day 2 — DBSCAN & Hierarchical Clustering 

**Theory notebook:** Three limitations of K-Means, how DBSCAN finds dense regions
(core / border / noise points, eps and min_samples parameters), how hierarchical
clustering builds a merge tree, Ward linkage, reading a dendrogram, method comparison.

**Hands-On Lab:** Applied DBSCAN and hierarchical clustering to the same dataset.

- DBSCAN (eps=0.5, min_samples=5): found 2 clusters + **45 noise points**
  - Noise points = the high-charge smoker outliers already flagged in Week 2 EDA
- Hierarchical (Ward linkage): dendrogram cut at 4 clusters — consistent with K-Means
- Compared all three methods side by side on the same scatter plot
- Conclusion: K-Means suits this dataset (compact, roughly spherical clusters);
  DBSCAN is better when outlier detection is the primary goal

---

### Day 3 — Dimensionality Reduction with PCA 

**Theory notebook:** The curse of dimensionality (4 real problems), how PCA finds
principal components as directions of maximum variance, feature loadings, explained
variance ratio, the 95% rule, when and when not to use PCA.

**Hands-On Lab:** Applied PCA to the 9-feature encoded dataset.

- Fitted PCA with all 9 components and plotted cumulative explained variance
- **7 components** needed to retain 95.03% of variance
  (modest compression — features are largely uncorrelated)
- Reduced to 2 components for visualization: **37.6% variance retained**
- 2D scatter colored by smoker status: partial separation visible along PC1
- Feature loadings:
  - PC1 (21.6%): charges (0.654), smoker_yes (0.581), bmi (0.269) → cost/risk axis
  - PC2 (16.1%): region_southeast (0.632), region_northwest (0.512) → geographic axis

---

### Day 4 — t-SNE & Anomaly Detection 

**Theory notebook:** t-SNE vs PCA (local neighborhoods vs global variance),
the perplexity parameter, why t-SNE axes carry no meaning and must not be used
as model features, what anomaly detection is and why it is unsupervised,
Isolation Forest (random partitioning, path length, contamination parameter),
connection to DBSCAN noise points.

**Hands-On Lab:** Applied t-SNE and Isolation Forest to the insurance dataset.

- Re-ran K-Means k=4 to recover cluster labels for coloring
- Fitted t-SNE (perplexity=30, max_iter=1000):
  clusters appear more separated than in the PCA projection
- Compared t-SNE and PCA side by side — t-SNE for visualization,
  PCA for compression and modelling
- Isolation Forest (contamination=5%): flagged **67 anomalies** (5.0% of 1,338)
- Anomalies appear at the edges of the t-SNE plot — low-density regions
- Two most extreme anomalies inspected:
  - Row 543: female, age 54, BMI 47.41, smoker, charges $63,770
    (BMI and charges both far above dataset means simultaneously)
  - Row 1085: female, age 39, BMI 18.30, 5 children, smoker, charges $19,023
    (underweight BMI + maximum child count + smoker — rare combination)

---

### Day 5 — Phase 3 Project Selection & Sprint 1 Planning 

**Deliverable:** `project_plan.md` — a signed-off project plan for the individual
capstone project (Cardiac Patient Monitoring System).

Contents:
- Problem statement and task definition
- Definition of Done (11 acceptance criteria)
- Progress log for Weeks 1–4 (M1–M5) with actual results
- Backlog for remaining work (M6: unsupervised analysis, M7: final cleanup and demo)
- Written acceptance criteria for every remaining task
- Project timeline and repository structure

The Cardiac Patient Monitoring System was selected as the individual capstone.
The project targets binary classification of heart disease from clinical measurements.
Current status: M1–M5 complete, test-set F1 = 0.88, AUC-ROC = 0.916.
Remaining: M6 (K-Means + PCA on heart.csv) and M7 (cleanup, README, demo).

---

## Key Findings — Week 5

The same pattern appeared consistently across all four unsupervised methods:

```
K-Means       → smoker + high-BMI cluster has the highest charges
DBSCAN        → noise points = the high-charge smoker outliers from Week 2 EDA
PCA           → PC1 is the cost/risk axis (charges + smoker + bmi dominate)
Isolation Forest → most extreme anomalies are smokers with 2+ simultaneous outlier features
```

Every method independently rediscovered the same underlying structure
the Week 2 EDA had already identified through supervised exploration.

---

## Progress Checklist

- [x] Day 1 — K-Means Clustering
- [x] Day 2 — DBSCAN & Hierarchical Clustering
- [x] Day 3 — Dimensionality Reduction with PCA
- [x] Day 4 — t-SNE & Anomaly Detection
- [x] Day 5 — Phase 3 Project Selection & Sprint 1 Planning

---

## Tools Used

`scikit-learn` (KMeans, DBSCAN, PCA, TSNE, IsolationForest, StandardScaler,
silhouette_score) · `scipy` (dendrogram, linkage, fcluster) · `matplotlib` ·
`pandas` · `numpy` · Jupyter Notebook · Git & GitHub