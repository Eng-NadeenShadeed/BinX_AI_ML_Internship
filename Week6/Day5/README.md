# Week 6 — Day 5: Tuning, EarlyStopping & Sprint 1 Review

## Overview
Day 5 closes Sprint 1. The V2 network from Day 4 is tuned
systematically using four one-variable-at-a-time experiments,
EarlyStopping is added to all runs, the final model is evaluated
on the test set, and the sprint ends with a formal review and
retrospective.

## Files
```
Week6/
└── Day5/
├── day5_tuning_sprint_review.ipynb
└── README.md
```


## Topics Covered
- Systematic tuning — one variable at a time (same approach as Week 4)
- EarlyStopping — monitor val_loss, patience=15, restore_best_weights
- Experiment 1: Learning rate (0.01 / 0.001 / 0.0001)
- Experiment 2: Network depth and width (32→16 / 64→32 / 128→64)
- Experiment 3: Dropout rate (0.1 / 0.3 / 0.5)
- Experiment 4: Batch size (16 / 32 / 64)
- Final model — best configuration trained with patience=20
- Sprint 1 evidence — full comparison table (baseline vs all NN versions)
- Sprint Review — goal, backlog, definition of done
- Sprint Retrospective — what went well, what to improve, one concrete change

## Tuning Results (Validation Set)

### Experiment 1 — Learning Rate
| lr | Val F1 | AUC-ROC | Epochs |
|----|--------|---------|--------|
| 0.01 | 0.8780 | 0.9287 | 22 |
| **0.001** | **0.8856** | **0.9340** | 30 |
| 0.0001 | 0.8725 | 0.9262 | 120 |

### Experiment 2 — Network Depth & Width
| Architecture | Val F1 | AUC-ROC | Epochs |
|---|--------|---------|--------|
| **Small (32→16)** | **0.8832** | **0.9369** | 53 |
| Medium (64→32) | 0.8792 | 0.9254 | 32 |
| Large (128→64) | 0.8683 | 0.9356 | 31 |

### Experiment 3 — Dropout Rate
| Dropout | Val F1 | AUC-ROC | Epochs |
|---------|--------|---------|--------|
| 0.1 | 0.8744 | 0.9420 | 38 |
| 0.3 | 0.8600 | 0.9378 | 35 |
| **0.5** | **0.8812** | **0.9372** | 70 |

### Experiment 4 — Batch Size
| Batch | Val F1 | AUC-ROC | Epochs |
|-------|--------|---------|--------|
| 16 | 0.8856 | 0.9420 | 27 |
| 32 | 0.8744 | 0.9205 | 31 |
| **64** | **0.8912** | **0.9341** | 40 |

## Sprint 1 — Final Results (Test Set)

| Model | Accuracy | Precision | Recall | F1-score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| RF Baseline (Day 1) | 0.8859 | 0.8716 | 0.9314 | 0.9005 | 0.9427 |
| NN V1 (no regularization) | 0.8152 | 0.8542 | 0.8039 | 0.8283 | 0.8727 |
| NN V2 (BN + Dropout) | 0.8424 | 0.8544 | 0.8627 | 0.8585 | 0.8941 |
| NN Final (tuned) | 0.8533 | 0.8866 | 0.8431 | 0.8643 | 0.9309 |

## Sprint 1 Outcome
The tuned neural network did not surpass the RF baseline on this
tabular dataset — test F1 of 0.864 vs baseline F1 of 0.900.
This is an expected and well-documented result: classical ML
remains highly competitive on structured tabular data. The neural
network showed consistent improvement across versions (V1 → V2 →
Final) and achieved an AUC-ROC of 0.931, within 0.012 of the
baseline. The gap will be revisited in later sprints.