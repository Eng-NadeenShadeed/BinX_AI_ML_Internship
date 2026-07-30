# Week 2 - Math Foundations & EDA

## Overview
Week 2 of the BinX Tech AI & ML Internship (Phase 1 → Phase 2 transition) - 5 days covering the mathematical foundations every ML model rests on: descriptive statistics, probability, and linear algebra, applied immediately through a complete Exploratory Data Analysis on a real dataset.

## Repository Structure

```text
Week2/
├── Day 1/
│   ├── data/insurance.csv
│   ├── day1_descriptive_stats.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 2/
│   ├── day2_probability.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 3/
│   ├── day3_linear_algebra.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 4/
│   ├── data/insurance.csv
│   ├── day4_eda_part1.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 5/
│   ├── data/insurance.csv
│   ├── day5_correlation.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
└── README.md   (this file)
```

## Day-by-Day Breakdown

### Day 1 - Descriptive Statistics
Central tendency (mean, median, mode), spread (range, variance, standard deviation, IQR), and percentiles/quartiles. Hands-On Lab applied these to medical insurance charges: found the mean ($13,279) notably higher than the median ($9,386), a first hint of the right-skewed pattern that shaped the rest of the week.

### Day 2 - Probability & Distributions
Probability rules (addition, multiplication, complement), conditional probability, Bayes' theorem (medical test example - 99% accurate test, only ~16.7% actual disease probability given a rare disease), and Normal/Binomial/Uniform distributions. Hands-On Lab simulated 10,000 coin flips, sampled a normal distribution, and verified a conditional probability scenario by hand and simulation.

### Day 3 - Linear Algebra for ML
Vectors, matrices, dot products, and matrix multiplication - the exact operations behind how models compute predictions. Hands-On Lab represented data as a matrix, verified a dot product by hand against `np.dot`, used matrix multiplication for batch predictions, and deliberately triggered and explained a shape-mismatch error.

### Day 4 - EDA Part 1: Distributions & Outliers
First use of Seaborn. Univariate analysis (histogram, KDE, box plot, count plot) and outlier detection with the IQR method. Hands-On Lab found 139 outliers in `charges` (about 10% of the data) - 98% of them smokers, despite smokers being only ~20% of the dataset.

### Day 5 - EDA Part 2: Correlation & Data Storytelling (Graded Milestone)
Bivariate analysis, correlation, correlation heatmaps, and data storytelling. The Hands-On Lab combined the entire week into one complete, narrated EDA notebook, revealing that smoking status correlates with charges (r ≈ 0.79) far more strongly than any purely numeric variable like age (0.30) or BMI (0.20).

## Key Finding of the Week
Across all five days, one theme kept surfacing: medical charges are right-skewed, the outliers aren't random, and smoking status is by far the strongest single factor behind both the skew and the outliers - a pattern that would be essential to capture in any predictive model built on this data.

## Progress
- [x] Day 1 - Descriptive Statistics
- [x] Day 2 - Probability & Distributions
- [x] Day 3 - Linear Algebra for ML
- [x] Day 4 - EDA Part 1
- [x] Day 5 - EDA Part 2 (graded milestone)