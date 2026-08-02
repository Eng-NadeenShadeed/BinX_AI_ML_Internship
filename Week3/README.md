# Week 3 - Day 1: Supervised Learning Concepts & Scikit-learn API

## Overview

Today I started Phase 2 of the internship — Supervised Learning. I covered what supervised learning is and how it differs from other types of Machine Learning, the difference between Regression and Classification, how to separate a dataset into features (X) and a target (y), the standard Scikit-learn API, and why every supervised learning project needs a train/test split. I closed the day by applying all of this to a real dataset in the Hands-On Lab.

---

## Files

```text
Day 1/
├── data/
│   └── auto-mpg.csv
├── day1_supervised_learning_basics.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

---

## Topics Covered

- What Machine Learning is, and how it differs from traditional programming
- Types of Machine Learning (Supervised, Unsupervised, Reinforcement, Online, Self-Supervised, Semi-Supervised)
- What Supervised Learning is, and why it's called "supervised"
- Regression vs. Classification
- Features (X) and Target (y)
- The Scikit-learn API: instantiate → fit → predict → score
- Train/Test Split, and how to choose the right split ratio for a given dataset size

---

## Hands-On Lab Summary

**Dataset:** Auto MPG (398 cars, predicting fuel efficiency `mpg` from engine and weight specs)

- Explored the dataset structure and found a hidden data quality issue: `horsepower` was stored as text because of 6 rows containing `"?"` instead of a real missing value
- Cleaned the data: converted `horsepower` to numeric, dropped the 6 incomplete rows, dropped the non-feature `car name` column
- Checked correlations with `mpg` as a sanity check before modeling
- Separated the cleaned data into features (X, 7 columns) and target (y, `mpg`)
- Split the data into training (313 rows) and testing (79 rows) sets with `random_state=42`

---

## Setup

Installed **scikit-learn** for the first time this week and updated `requirements.txt` accordingly.