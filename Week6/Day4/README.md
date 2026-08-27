# Week 6 — Day 4: Building & Training a Network in Keras

## Overview
Day 4 is where the theory from Days 1–3 becomes a working model.
I built, compiled, and trained two neural network versions on the
heart disease dataset, read the training history, and compared
both against the Random Forest baseline from Day 1.

## Files

```
Week6/
└── Day4/
├── day4_keras_network.ipynb
└── README.md
```

## Topics Covered
- The Keras Sequential API — build, compile, fit
- Reproducing the cardiac monitoring preprocessing pipeline
- Architecture design — input size, hidden layers, output activation
- Compile settings — Adam (lr=0.001), Binary Cross-Entropy, Accuracy
- Reading the training history — loss and accuracy curves
- Diagnosing overfitting from training curves
- Batch Normalization — stabilizing layer inputs during training
- Dropout (rate=0.3) — regularization to reduce overfitting
- Test set evaluation — first and only opening since Day 1
- Comparison table — V1, V2, and RF baseline

## Model Architectures

| Version | Architecture | Regularization |
|---------|-------------|----------------|
| V1 | Input → 64 ReLU → 32 ReLU → 1 Sigmoid | None |
| V2 | Input → 64 ReLU → BN → Dropout(0.3) → 32 ReLU → BN → Dropout(0.3) → 1 Sigmoid | BatchNorm + Dropout |

## Test Set Results

| Model | Accuracy | Precision | Recall | F1-score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| NN V1 (no regularization) | 0.8152 | 0.8542 | 0.8039 | 0.8283 | 0.8727 |
| NN V2 (BN + Dropout) | 0.8424 | 0.8544 | 0.8627 | 0.8585 | 0.8941 |
| RF Baseline (Day 1) | 0.8859 | 0.8716 | 0.9314 | 0.9005 | 0.9427 |

## Key Findings
- V1 showed strong overfitting — train accuracy reached ~99% while
  validation accuracy stayed at ~82%
- V2 with Batch Normalization and Dropout reduced overfitting substantially
  and improved all test metrics over V1
- Both neural network versions remain below the RF baseline —
  systematic tuning with EarlyStopping is planned for Day 5