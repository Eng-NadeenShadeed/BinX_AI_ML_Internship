# Week 6 — Day 5: Tuning, EarlyStopping & Sprint 1 Review

## Overview

Day 5 is the final day of Sprint 1.

I tuned the neural network from Day 4 using EarlyStopping and four
controlled hyperparameter experiments, selected the best configuration,
trained a final model, and evaluated it on the held-out test set.

The sprint was then closed with a full model comparison, Sprint Review,
and Retrospective.

## Files

```text
Week6/

└── Day5/
    ├── day5_tuning_and_review.ipynb
    └── README.md
```

## Topics Covered

- Reproducing the cardiac monitoring preprocessing pipeline
- EarlyStopping — monitoring validation loss and restoring best weights
- Learning rate tuning — 0.01, 0.001, 0.0001
- Network depth and width tuning — 32→16, 64→32, 128→64
- Dropout rate tuning — 0.1, 0.3, 0.5
- Batch size tuning — 16, 32, 64
- Selecting the best hyperparameter configuration
- Training the final tuned neural network
- Final test set evaluation
- Full Sprint 1 model comparison
- Sprint Review and Retrospective

## Tuning Experiments

| Experiment | Values Tested | Selected |
|------------|---------------|----------|
| Learning Rate | 0.01, 0.001, 0.0001 | **0.001** |
| Architecture | 32→16, 64→32, 128→64 | **32→16** |
| Dropout | 0.1, 0.3, 0.5 | **0.3** |
| Batch Size | 16, 32, 64 | **32** |

## Final Model Configuration

| Hyperparameter | Final Value |
|----------------|-------------|
| Learning Rate | 0.001 |
| Architecture | 32→16 |
| Activation | ReLU + Sigmoid |
| Regularization | Batch Normalization + Dropout(0.3) |
| Batch Size | 32 |
| EarlyStopping | Patience = 20 |
| Loss | Binary Cross-Entropy |
| Optimizer | Adam |

## Final Test Set Results

| Model | Accuracy | Precision | Recall | F1-score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| NN V1 (no regularization) | 0.8152 | 0.8542 | 0.8039 | 0.8283 | 0.8727 |
| NN V2 (BN + Dropout) | 0.8424 | 0.8544 | 0.8627 | 0.8585 | 0.8941 |
| **NN Final (tuned)** | **0.8533** | **0.8713** | **0.8627** | **0.8670** | **0.9182** |
| **RF Baseline (Day 1)** | **0.8859** | **0.8716** | **0.9314** | **0.9005** | **0.9427** |

## Key Findings

- EarlyStopping stopped the final model at epoch **58** and restored
  the best weights from epoch **38**, where validation loss reached **0.3280**

- Hyperparameter tuning improved the neural network substantially —
  test F1 increased from **0.8283 (V1)** to **0.8670 (Final)**

- The final neural network also improved AUC-ROC from **0.8727** in V1
  to **0.9182**

- The final neural network did **not** outperform the RF baseline on
  the held-out test set

- RF remained the strongest model, achieving the highest test
  Accuracy (**0.8859**), F1-score (**0.9005**), and AUC-ROC (**0.9427**)

## Sprint 1 Outcome

Sprint 1 was completed successfully.

The neural network was built, trained, regularized, tuned, and evaluated
on the same held-out test set as the Random Forest baseline.

The final results show that a neural network does not automatically
outperform classical machine learning on small structured tabular data.
However, systematic tuning and regularization produced a clear
improvement over the initial neural network.

**Sprint 1 Winner: Random Forest Baseline**