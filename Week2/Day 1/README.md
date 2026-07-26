# Week 2 - Day 1: Descriptive Statistics

## Overview
- First day of Week 2 (Phase 1 → Phase 2 transition).
- Learned the fundamentals of descriptive statistics.
- Explored measures of central tendency and measures of spread.
- Studied percentiles, quartiles, and their relationship to box plots and outlier detection.
- Applied all concepts to a real-world medical insurance dataset.

## Files
- `day1_descriptive_stats.ipynb` — Notes, explanations, examples, and practice.
- `Hands_On_Lab.ipynb` — Required hands-on exercise.
- `data/insurance.csv` — Medical Cost Personal Dataset (Kaggle).

## Topics Covered

### Why Statistics?
- Why statistics is essential before building ML models.
- Descriptive Statistics vs Inferential Statistics.

### Measures of Central Tendency
- Mean
- Median
- Mode
- Choosing the appropriate measure based on the dataset.
- Effect of outliers on mean vs median.
- Mode for continuous vs categorical data.

### Measures of Spread
- Range (`np.ptp`)
- Variance
- Standard Deviation
- Interquartile Range (IQR)

### Percentiles & Quartiles
- Percentiles
- Quartiles (Q1, Q2, Q3)
- Relationship between quartiles and box plots.
- Using IQR for outlier detection.

## Hands-On Lab

### Dataset
- Medical Insurance Charges dataset.
- 1,338 patient records.
- Removed 1 duplicate row before analysis.

### Analysis Performed
- Loaded the `charges` column using Pandas.
- Calculated:
  - Mean
  - Median
  - Mode
  - Standard Deviation
  - Range
  - IQR
- Used NumPy, Pandas, and SciPy for statistical calculations.

### Findings
- Mean ≈ **$13,279**
- Median ≈ **$9,386**
- Mean is about **$3,900 higher** than the median.
- The distribution is **right-skewed** because of high-cost medical charges.
- The **median** better represents the typical insurance charge.
- The **mode** is not particularly meaningful for a continuous numerical variable like `charges`.

## Key Takeaways
- Different measures of center describe data differently.
- Outliers strongly affect the mean but have little effect on the median.
- Standard deviation and IQR measure spread in different ways.
- Quartiles divide the data into four equal parts.
- IQR is a robust method for detecting potential outliers.
- Descriptive statistics are the foundation of Exploratory Data Analysis (EDA).