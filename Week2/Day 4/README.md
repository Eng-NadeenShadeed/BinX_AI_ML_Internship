# Week 2 - Day 4: EDA Part 1 - Distributions & Outliers

## Overview

Fourth day of Week 2 and the first introduction to **Exploratory Data Analysis (EDA)** using **Seaborn**. Learned why EDA is a required step before building machine learning models and explored how to understand data through statistical visualizations and outlier detection on a real-world dataset.

---

## Files

- `day4_eda_part1.ipynb` – Detailed notes and worked examples for every concept.
- `Hands_On_Lab.ipynb` – Official hands-on exercise.
- `data/insurance.csv` – Medical Cost Personal Dataset (Kaggle), reused from Day 1.

---

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Topics Covered

- What Exploratory Data Analysis (EDA) is and why it comes before modeling.
- Introduction to **Seaborn** as a statistical visualization library built on top of Matplotlib.
- Univariate analysis.
- Histogram.
- KDE (Kernel Density Estimation) plot.
- Box plot (five-number summary and quartiles).
- Count plot.
- Outlier detection using the IQR (Interquartile Range) method.
- Deciding whether to keep or remove outliers based on data understanding.

---

## Hands-On Lab

Applied **Univariate Exploratory Data Analysis** to the Medical Insurance Charges dataset (1,337 records after removing one duplicate).

### Numeric Variables

- Created histograms for all four numeric variables (`age`, `bmi`, `children`, and `charges`).
- Observed that **charges** has a strong right-skewed distribution.
- Created box plots for **age**, **bmi**, and **charges**.
- Found that **charges** contains the largest number of visible outliers.

### Outlier Detection

Applied the **IQR method** to the `charges` column:

- Calculated **Q1**, **Q3**, **IQR**, and the lower/upper bounds.
- Flagged **139 outliers** (about **10%** of the dataset).
- Found that **136 of the 139 outliers (98%) are smokers**, despite smokers representing only about **20%** of the dataset.
- Decided to **keep the outliers** because they represent real medical costs rather than data errors.

### Categorical Variables

Created count plots for:

- `sex`
- `smoker`
- `region`

Key observations:

- **sex** is well balanced.
- **region** is fairly balanced.
- **smoker** is imbalanced (approximately **80% non-smokers** and **20% smokers**).

---

## Key Finding

The analysis consistently showed that **charges** is highly right-skewed and contains meaningful outliers. Almost all extreme medical costs belong to smokers, indicating that **smoking status is the strongest driver of high insurance charges** in this dataset. This finding provides a strong motivation for the **bivariate analysis and correlation analysis** in **Week 2 - Day 5**.