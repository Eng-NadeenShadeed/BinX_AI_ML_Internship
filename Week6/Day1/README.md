# Week 6 — Day 1: Sprint 1 Planning & Baseline

## Overview
The first day of Week 6 focuses on planning Sprint 1 and recording the
Random Forest baseline that the neural network will be compared against
throughout the week.

## Files
| File | Description |
|------|-------------|
| `day1_sprint_planning_baseline.ipynb` | Sprint plan + baseline model + recorded metrics |

## Topics Covered
- Agile Sprint structure — Goal, Backlog, Definition of Done
- Why a baseline is required before any deep learning work
- Reproducing the Random Forest pipeline from the cardiac monitoring project
- Recording validation and test metrics as the Sprint 1 target

## Baseline Results (Random Forest)

| Metric | Validation | Test |
|--------|------------|------|
| Accuracy | 0.9130 | 0.8859 |
| Precision | 0.9388 | 0.8716 |
| Recall | 0.9020 | 0.9314 |
| F1-score | 0.9200 | 0.9005 |
| AUC-ROC | 0.9440 | 0.9427 |

## Sprint 1 Target
The neural network built in Days 2–5 needs to match or exceed the test
F1-score of **0.9005** and AUC-ROC of **0.9427**.