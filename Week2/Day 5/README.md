# Week 2 - Day 5: EDA Part 2 - Correlation & Data Storytelling

## Overview
Final day of Week 2 and the graded mini deliverable milestone.

Covered **bivariate analysis, correlation analysis, and data storytelling**, then integrated all Week 2 concepts into a complete Exploratory Data Analysis (EDA) notebook using the medical insurance dataset.

The goal was to move from analyzing individual variables to understanding relationships between features and extracting meaningful insights before modeling.

---

## Files

- `day5_correlation.ipynb`  
  Detailed notes and practical examples covering:
  - Bivariate analysis
  - Scatter plots
  - Correlation analysis
  - Heatmaps
  - Pair plots
  - Data storytelling

- `Hands_On_Lab.ipynb`  
  Complete Week 2 EDA notebook containing the full analysis pipeline and graded deliverable.

- `data/insurance.csv`  
  Medical Cost Personal Dataset used throughout Week 2.

---

## Topics Covered

### Bivariate Analysis
- Understanding relationships between two variables.
- Types of bivariate relationships:
  - Numerical vs Numerical
  - Categorical vs Categorical
  - Numerical vs Categorical

### Data Visualization
- Scatter plots for numerical relationships.
- Grouped box plots for numerical vs categorical comparisons.
- Pair plots for exploring multiple relationships simultaneously.

### Correlation Analysis
- Pearson correlation coefficient.
- Understanding positive, negative, and weak correlations.
- Correlation heatmaps using Seaborn.
- Understanding that correlation does not imply causation.

### Data Storytelling
- Transforming analysis results into meaningful insights.
- Communicating findings clearly using visualizations and explanations.

---

## Hands-On Lab: Complete EDA Notebook

Combined all Week 2 analysis steps on the medical insurance dataset:

### Day 1 Recap: Descriptive Statistics
- Analyzed the `charges` distribution.
- Mean charge: **$13,279**
- Median charge: **$9,386**
- The difference between mean and median confirmed a **right-skewed distribution**.

### Day 4 Recap: Outlier Detection
- Applied the **IQR method** to detect outliers in `charges`.
- Identified **139 outliers**.
- Found that **98% of detected outliers were smokers**, suggesting a strong relationship between smoking status and high medical costs.

### Day 5: Bivariate Analysis & Correlation
- Analyzed relationships between features using:
  - Scatter plots
  - Correlation matrix
  - Heatmap
  - Grouped visualizations

- Found that `smoker` status has a much stronger relationship with `charges` compared to other features.

- Compared numeric correlations:
  - `age` → charges: **r ≈ 0.30**
  - `bmi` → charges: **r ≈ 0.20**

---

## Key Findings

The analysis showed that:

- **Smoking status is the strongest factor associated with medical charges in this dataset.**
- Smokers tend to have significantly higher medical costs compared to non-smokers.
- Numeric variables such as age and BMI show weaker linear relationships with charges.
- Correlation analysis helps identify important patterns, but it should be combined with domain knowledge and other EDA techniques before making modeling decisions.

---

## Week 2 EDA Outcome

By the end of Week 2, the complete EDA workflow was applied:

1. Data inspection and cleaning.
2. Descriptive statistics.
3. Distribution analysis.
4. Outlier detection.
5. Relationship analysis.
6. Correlation analysis.
7. Insight extraction through data storytelling.

This completed the foundation needed before moving into Machine Learning modeling.