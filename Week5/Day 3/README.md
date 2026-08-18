# Week 5 — Day 3: Dimensionality Reduction with PCA

## Overview

Day 3 shifts from clustering to dimensionality reduction.
I apply Principal Component Analysis (PCA) to the insurance dataset to understand
how many components are needed to retain most of the data's information,
and to visualize the dataset in 2D.

---

## Files

```text
Day 3/
├── day3_pca.ipynb
│   
└── Hands_On_Lab.ipynb
```

---

## Topics Covered

- The curse of dimensionality: why high-dimensional data causes real problems
- What PCA does: finding principal components as directions of maximum variance
- Feature loadings: how original features contribute to each component
- Explained variance ratio and the cumulative variance plot
- The 95% rule for choosing the number of components
- When (and when not) to use PCA: trade-offs between compression and interpretability
- Connection to linear algebra (Week 2): components as linear combinations of features

---

## Hands-On Lab Summary

Applied a full PCA pipeline to the insurance dataset (9 encoded features).

**Steps completed:**
1. Encoded categorical features (sex, smoker, region) — 7 columns → 9 columns
2. Scaled with `StandardScaler` (required before any PCA)
3. Fit PCA with all components and plotted cumulative explained variance
4. Determined that **7 components** are needed to retain 95.03% of the variance
5. Reduced to 2 components (37.6% variance) and produced a 2D scatter plot colored by smoker status
6. Inspected feature loadings: PC1 is driven by charges + smoker (cost/risk axis), PC2 by region + BMI (geographic axis)
7. Documented in Markdown what the reduction preserved and what it cost

**Key finding:**  
The insurance dataset does not compress aggressively with PCA (9 → 7 for 95%)
because its features measure distinct, largely uncorrelated things.
The 2D scatter confirms the dominant pattern from the EDA: smoker status
drives most of the variance and is partially visible as separation along PC1.

---

## Tools Used

`scikit-learn` (PCA, StandardScaler) • `matplotlib` • `pandas` • Jupyter Notebook