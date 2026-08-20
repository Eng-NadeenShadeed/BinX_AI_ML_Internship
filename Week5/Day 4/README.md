# Week 5 — Day 4: t-SNE & Anomaly Detection

## Overview

Day 4 closes the visualization and outlier work that started across Days 1–3.
It introduces t-SNE as a visualization-only alternative to PCA, then applies
Isolation Forest to formally identify anomalous records in the dataset.

Where PCA (Day 3) compresses features by preserving global variance, t-SNE
preserves local neighborhoods — keeping points that were close together in
high-dimensional space close together in 2D. This produces cleaner cluster
separation visually, at the cost of losing interpretable axes.

---

## Files

```text
Day 4/
├── day4_tsne_anomaly.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## Topics Covered

- t-SNE: how it differs from PCA and what it preserves
- The perplexity parameter and how it affects the embedding
- Why t-SNE axes carry no meaning and should not be used as model features
- PCA vs t-SNE: when to use each
- What anomaly detection is and why it is usually unsupervised
- Isolation Forest: random partitioning, path length, and the contamination parameter
- The connection between DBSCAN noise points (Day 2) and Isolation Forest anomalies

---

## Hands-On Lab Summary

Applied t-SNE and Isolation Forest to the insurance dataset using the same
encoding and scaling pipeline as Days 1–3.

**Steps completed:**

1. Re-ran K-Means (k=4) to recover cluster labels from Day 1 for coloring
2. Fit t-SNE (perplexity=30, max_iter=1000) and plotted clusters in 2D
3. Placed the t-SNE plot next to the PCA plot from Day 3 and compared what each reveals
4. Ran Isolation Forest (contamination=5%) and reported the number of flagged points
5. Identified the two most extreme anomalies using the decision score
6. Inspected both records against dataset statistics and documented a hypothesis for each
7. Refit DBSCAN with the Day 2 parameters (eps=1.0, min_samples=3) and computed the actual overlap between its noise points and the Isolation Forest anomalies

---

## Key Findings

**t-SNE** produced noticeably cleaner cluster separation than the PCA projection
from Day 3. The four K-Means clusters appear as more distinct regions in the
t-SNE plot, confirming that the cluster structure from Day 1 is real rather
than an artifact of the algorithm.

**Isolation Forest** flagged 67 records as anomalous (5.0% of 1,338).
The flagged points appear at the edges of the t-SNE plot, in low-density
regions — consistent with how the algorithm works.

**Comparing directly to Day 2:** refitting DBSCAN with Day 2's parameters
(eps=1.0, min_samples=3) on the 9-feature encoded space used throughout Days 3–4
flagged 158 points as noise — far more than the 12 noise points found in Day 2,
because the same `eps` radius behaves differently once dimensionality increases
from 4 to 9 features (distances grow with dimensionality, so the same eps
captures a "tighter" neighborhood). Of those 158 DBSCAN noise points, 40 (25.3%)
were also flagged as anomalies by Isolation Forest. This is partial, not
complete, agreement — expected, since the two methods define "outlier"
differently (density-based vs. isolation-based), and the DBSCAN run here isn't
a like-for-like repeat of Day 2's result due to the feature-space difference.

The two most extreme anomalies were:

- **Row 543** — female, age 54, BMI 47.41, smoker, charges $63,770.
  Two features are simultaneously extreme: BMI sits far above the dataset mean
  of 30.7, and charges are nearly 5× the dataset mean of $13,270.

- **Row 1085** — female, age 39, BMI 18.30, 5 children, smoker, charges $19,023.
  An unusual combination: underweight BMI (below 18.5), maximum child count,
  and smoker status — a profile that does not resemble any cluster center closely.

Both anomalies are smokers with at least two extreme features simultaneously,
consistent with the Week 2 EDA finding that smoking amplifies the effect of
other features on charges.

```text
Visualization of clusters       → t-SNE (cleaner separation)
Compression for modelling       → PCA (interpretable, faster)
Anomaly identification          → Isolation Forest
Noise / outlier detection       → DBSCAN (Day 2)
```

---

## Tools Used

`scikit-learn` (TSNE, IsolationForest, KMeans, StandardScaler, PCA, DBSCAN) •
`matplotlib` • `pandas` • Jupyter Notebook