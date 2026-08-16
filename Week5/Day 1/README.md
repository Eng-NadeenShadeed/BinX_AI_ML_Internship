# Week 5 — Day 1: Unsupervised Learning & K-Means Clustering

## Overview

Day 1 opened Week 5 with the first unsupervised learning algorithm.
Unlike every model in Weeks 1–4, K-Means receives no labels —
it discovers structure purely from the shape of the data.

The learning notebook covered the full theoretical framework:
why scaling is mandatory, how the elbow method and silhouette score
work together to choose k, and how to interpret cluster profiles.

The Hands-On Lab applied the complete workflow on the insurance dataset.
K-Means discovered a high-cost smoker segment (Cluster 1, n=165) with
89.7% smoking rate — without ever being told about the smoking column.

---

## Dataset

| Detail | Value |
|--------|-------|
| Source | Medical Cost Personal Dataset (Week 2) |
| Rows | 1,338 |
| Features used | age, bmi, children, charges |
| Task | Unsupervised clustering |

---

## Topics Covered

- Supervised vs unsupervised learning — the fundamental shift
- What clustering is and when it is useful
- K-Means: how the centroid-assignment loop works
- Why scaling is required before clustering
- Choosing k: the elbow method
- Choosing k: the silhouette score
- Interpreting clusters as real-world segments

---

## What I Did

- Ran EDA on all four numeric features before touching the algorithm
- Applied StandardScaler and verified mean=0, std=1 per feature
- Ran K-Means for k=1–10 and plotted the elbow curve with a drop table
- Computed silhouette scores for k=2–6 and confirmed k=4 using
  both methods simultaneously on a combined chart
- Fitted the final K-Means (k=4, n_init=10) and recovered centroids
  in original scale using inverse_transform
- Visualized clusters on age vs charges and BMI vs charges scatter plots
- Built cluster profiles with groupby and a four-panel bar chart
- Plotted per-point silhouette scores to assess internal consistency
- Interpreted each of the four segments with real-world labels

---

## Results

| Cluster | Name | n | Avg Charges | Smokers |
|---------|------|--:|------------:|--------:|
| 0 | Older Non-Smokers | 408 | $12,593 | 10.0% |
| 1 | High-Cost Smokers | 165 | $40,308 | 89.7% |
| 2 | Young Families | 346 | $10,710 | 12.4% |
| 3 | Healthy Young Adults | 419 | $5,397 | 10.0% |

Best k: 4 | Silhouette score: 0.294

---

## Files

```text
Day 1/
├── day1_kmeans_clustering.ipynb
└── Hands_On_Lab.ipynb
└── README.md
```

---

## How to Run

1. Activate your `.venv`.
2. Open the notebook in VS Code.
3. Select the `.venv` Jupyter kernel.
4. Run all cells from top to bottom.