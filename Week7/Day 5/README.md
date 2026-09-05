# Week 7 · Day 5 — Sprint 2 Close-Out

## Overview
I trained and tuned a Dense Network on the 70K Cardiovascular Disease dataset,
testing the Sprint 2 central hypothesis: with 70,000 patients instead of 918,
can a Dense Network outperform the Random Forest baseline? The hypothesis was
confirmed from Experiment 1 — all four Dense Network configurations beat the RF.
The simplest architecture (64→32) produced the best results. The sprint closed
with a formal Sprint Review and Retrospective.

## Files
```
Day 5/
├── day5_sprint2_review.ipynb ← Sprint 2 close-out notebook
└── README.md
```

## Dataset — Cardiovascular Disease
| Property | Value |
|----------|-------|
| Source | Kaggle — Cardiovascular Disease Dataset |
| Total patients | 70,000 |
| After cleaning | 68,645 |
| Features | 12 clinical measurements |
| Target | `cardio` — cardiovascular disease (0/1) |
| Class balance | 49.5% positive — near-perfectly balanced |

### Features
| Feature | Description |
|---------|-------------|
| age | Patient age (converted from days to years) |
| gender | 1: female, 2: male |
| height / weight | cm / kg |
| ap_hi / ap_lo | Systolic / diastolic blood pressure |
| cholesterol | 1: normal, 2: above normal, 3: well above normal |
| gluc | Glucose level (same scale as cholesterol) |
| smoke / alco / active | Binary lifestyle indicators |
| bmi | Derived feature — weight / height² |

### Cleaning Steps
| Issue | Rows Removed | Reason |
|-------|-------------|--------|
| Impossible BP values | 1,322 | ap_hi > 250 or ap_lo < 30 or ap_hi < ap_lo |
| Impossible height/weight | 33 | Height < 100cm or weight < 30kg |
| **Total removed** | **1,355 (1.9%)** | |

## Experiment Log

| Experiment | Architecture | Key Config | Val F1 | Test F1 | Test AUC | Result |
|-----------|-------------|-----------|--------|---------|---------|--------|
| RF Baseline | Random Forest (200 trees) | n_estimators=200 | 0.7016 | 0.7064 | 0.7737 | ← Target |
| **Exp 1 — Simple Dense** | **Dense: 64 → 32** | **BN + Dropout(0.3) + LR=0.001** | **0.7158** | **0.7191** | **0.8023** | **✓ Best** |
| Exp 2 — Deeper | Dense: 128 → 64 → 32 | BN + Dropout(0.3) + LR=0.001 | 0.7133 | 0.7157 | 0.8022 | ✓ Beats RF |
| Exp 3 — Wider | Dense: 256 → 128 → 64 | BN + Dropout(0.2) + LR=0.001 | 0.7133 | 0.7162 | 0.8020 | ✓ Beats RF |
| Exp 4 — Lower LR | Dense: 64 → 32 | BN + Dropout(0.3) + LR=0.0005 | 0.7147 | 0.7168 | 0.8020 | ✓ Beats RF |

## Sprint 2 Results

| | Sprint 1 | Sprint 2 |
|--|----------|----------|
| Dataset | heart.csv (918 rows) | cardio_train.csv (70,000 rows) |
| RF Baseline F1 | 0.9005 | 0.7064 |
| Best NN F1 | 0.8670 ✗ lost to RF | **0.7191 ✓ beat RF** |
| Training behavior | Overfit — train >> val | Healthy — train ≈ val |
| Key finding | Data too small for NN | More data = NN advantage |

## Key Findings
- Sprint 2 goal achieved — Dense Network beats RF on all metrics
- Simplest architecture (64→32) outperformed deeper and wider networks
- Training curves showed no overfitting — data size eliminated Sprint 1's main problem
- Dataset size was the critical limiting factor in Sprint 1, not architecture
- Adding BMI as a derived feature provided an explicit cardiovascular risk signal

## Sprint Retrospective
**What went well:** hypothesis confirmed from Experiment 1 — experiment log
worked as planned — no overfitting with 70K data.

**What to improve:** no ensemble methods tested — Gradio demo not completed —
DistilBERT session loss caused delays.

**Concrete change for Sprint 3:** save every trained model to Drive immediately
after training, before moving to the next cell.

## Sprint 3 Focus
NLP/CV integration and final evaluation — applying this week's architecture
lessons to the complete project pipeline.
