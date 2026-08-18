# Week 5 — Day 2: DBSCAN & Hierarchical Clustering

## Overview

Day 2 extends the clustering work from Day 1 by introducing two alternatives
to K-Means: DBSCAN for density-based clustering and hierarchical clustering
with dendrograms.

The session focused on understanding the limitations of K-Means and learning
how to choose a clustering method based on the structure, density, and shape
of the data.

The Hands-On Lab was completed during an in-person session.

---

## Files

```text
Day 2/
├── day2_dbscan_hierarchical.ipynb
│   
└── Hands_On_Lab.ipynb
```

---

## Topics Covered

- Why K-Means isn't always the right choice
- The three main limitations of K-Means
- DBSCAN: density-based clustering and noise detection
- DBSCAN point types: core, border, and noise
- DBSCAN parameters: `eps` and `min_samples`
- Hierarchical clustering and dendrograms
- Ward linkage and cutting the dendrogram
- Comparing K-Means, DBSCAN, and hierarchical clustering
- Choosing the right clustering method for different data structures

---

## Hands-On Lab Summary

Applied all three clustering methods to the same insurance dataset
used in Day 1.

**Steps completed:**

1. Reconstructed the K-Means baseline from Day 1
2. Ran DBSCAN and investigated different `eps` and `min_samples` values
3. Identified DBSCAN clusters and noise points (`-1`)
4. Built a hierarchical clustering dendrogram using Ward linkage
5. Compared different cluster counts using silhouette scores
6. Compared K-Means, DBSCAN, and hierarchical clustering visually
7. Documented which method best fits the dataset and why

---

## Key Findings

**K-Means (k=4)** produced the most useful and interpretable segmentation
for the insurance dataset.

**DBSCAN** found a large main cluster, a very small high-cost cluster,
and 12 noise points. The noise points represent patients located in sparse
regions of the feature space.

DBSCAN also isolated a small group of three high-cost smokers into a
separate cluster, demonstrating how density-based clustering can reveal
patterns that are treated differently by K-Means.

**Hierarchical clustering** produced a structure that was broadly consistent
with the four-cluster solution explored in Day 1. The dendrogram provided
an additional way to explore possible cluster counts and relationships
between groups.

The main lesson was that the "best" clustering method depends on the
question being asked:

```text
Patient segmentation       → K-Means
Anomaly / noise detection  → DBSCAN
Nested structure           → Hierarchical clustering