# Week 3 - Day 2: Linear Regression

## Overview

Today I trained my first real supervised learning model — Linear Regression — to predict a continuous value (`mpg`) from the Auto MPG dataset, using 7 features (Multiple Linear Regression). I went beyond the official curriculum to understand not just *how* to call Scikit-learn, but *why* the algorithm actually works — least squares, the cost function, and how it connects back to the dot product from Week 2.

## Files

```text
Day 2/
├── data/
│   └── auto-mpg.csv
├── day2_linear_regression.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

## Topics Covered

1. What is Linear Regression
2. Independent & Dependent Variables (X & y) — including Simple vs. Multiple Linear Regression
3. Best Fit Line — visualized on real data (Weight vs. MPG)
4. The Linear Regression Equation — from math notation (y = mx + b) to ML notation (ŷ = w₁x₁ + ... + wₙxₙ + b), connected back to the dot product from Week 2
5. Coefficients & Intercept — what each one actually means
6. Least Squares & Residuals — why errors are squared before being minimized
7. Cost Function (MSE) — the formula training actually minimizes
8. Evaluation Metrics — MAE, RMSE, R²
9. Comparing Against a Baseline — why a metric alone is meaningless without one
10. Practical Application with Scikit-learn — the Instantiate → Fit → Predict → Evaluate cycle, applied to real data

**Note:** Topics 4, 6, 7, 9, and the coefficient-scaling caveat in the lab aren't part of the official 5-topic curriculum for this day — I added them because they explain the reasoning behind the algorithm, not just the syntax to run it.

## Hands-On Lab Summary

Trained a Multiple Linear Regression model on 7 features to predict `mpg`:

| Metric | Value |
|---|---|
| MAE | 2.42 mpg |
| RMSE | 3.27 mpg |
| R² | 0.79 |
| Baseline RMSE (predicting the mean) | 7.19 mpg |

The model's RMSE is less than half the baseline's, confirming it learned a real relationship from the data rather than just guessing the average. `model year` (positive) and `weight` (negative) had coefficients that matched real-world expectations. `origin` had the largest raw coefficient, but I noted that comparing coefficients directly across features on different scales can be misleading — a fair comparison would need the features scaled first.