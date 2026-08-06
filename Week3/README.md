# Week 3 - Supervised Learning

## Overview

Week 3 of the BinX Tech AI & ML Internship marks the transition from data exploration into building real machine learning models. Throughout the week, I learned the complete supervised learning workflow: preparing data, training regression and classification models, evaluating performance with appropriate metrics, comparing different algorithms, and finishing with a complete end-to-end medical prediction pipeline.

## Repository Structure

```text
Week3/

├── Day 1/
│   ├── data/auto-mpg.csv
│   ├── day1_supervised_learning_basics.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md

├── Day 2/
│   ├── data/auto-mpg.csv
│   ├── day2_linear_regression.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md

├── Day 3/
│   ├── data/pima-indians-diabetes.csv
│   ├── day3_logistic_regression.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md

├── Day 4/
│   ├── data/pima-indians-diabetes.csv
│   ├── day4_trees_forests_svm_knn.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md

├── Day 5/
│   ├── data/heart_disease_uci.csv
│   ├── Hands_On_Lab.ipynb
│   └── README.md

└── README.md   (this file)

## Day-by-Day Breakdown

### Day 1 - Supervised Learning Fundamentals

Learned the foundation of supervised learning: labeled data, regression vs classification, features (`X`) and target (`y`), the Scikit-learn workflow (`instantiate → fit → predict → score`), and the importance of train/test splitting.

Hands-On Lab applied these concepts on the Auto MPG dataset by cleaning the data, handling missing values, separating features from target, and preparing training/testing sets for future modeling.

---

### Day 2 - Linear Regression

Built the first supervised learning model to predict a continuous value (`mpg`) using Multiple Linear Regression. Covered the prediction equation, coefficients, intercept, residuals, least squares, MSE, and regression evaluation metrics (MAE, RMSE, and R²).

Hands-On Lab trained and evaluated a Linear Regression model on Auto MPG, then compared its performance against a baseline to verify that the model learned meaningful patterns.

---

### Day 3 - Logistic Regression & Classification Metrics

Moved from regression to classification using Logistic Regression on the Pima Indians Diabetes dataset. Learned how models convert predictions into probabilities using the sigmoid function and how to evaluate classifiers using confusion matrices, precision, recall, F1-score, and AUC-ROC.

Hands-On Lab focused on medical data exploration, discovering hidden missing values represented as zeros, cleaning the dataset, training the classifier, and understanding why accuracy alone is not enough for classification problems.

---

### Day 4 - Decision Trees, Random Forests, SVM & k-NN

Explored different classification algorithms and learned how each model approaches decision-making. Covered Decision Trees, Random Forests, Support Vector Machines, k-Nearest Neighbors, feature importance, and the bias-variance trade-off.

Hands-On Lab trained and compared multiple classifiers on the same dataset using consistent evaluation metrics. The results showed that model selection depends on the dataset, the problem requirements, and the balance between performance and interpretability.

---

### Day 5 - End-to-End Heart Disease Prediction

Combined everything learned throughout the week into a complete supervised learning pipeline using the Heart Disease UCI dataset (920 patients).

The project followed the full ML workflow: EDA → preprocessing → train/test split → modeling → evaluation.

Performed data exploration, missing value handling, categorical encoding, feature scaling without data leakage, and trained multiple classification models. Compared Logistic Regression and Random Forest using classification metrics and selected the final model based on performance.

---

## Key Finding of the Week

Week 3 was the transition from understanding data into building predictive models. I learned that machine learning projects are not only about choosing algorithms, but about creating a complete pipeline: understanding the data, preparing it correctly, selecting suitable metrics, comparing different models, and making justified decisions based on results.

---

## Progress

- [x] Day 1 - Supervised Learning Fundamentals
- [x] Day 2 - Linear Regression
- [x] Day 3 - Logistic Regression & Classification Metrics
- [x] Day 4 - Decision Trees, Random Forests, SVM & k-NN
- [x] Day 5 - End-to-End Heart Disease Prediction