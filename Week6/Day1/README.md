# Week 6 — Day 1: Sprint 1 Planning, Neural Network Foundations & Baseline

## Overview
Day 1 of Week 6 covers two things: formal Sprint 1 planning with a recorded
Random Forest baseline, and an introduction to the core building blocks of
neural networks — the neuron, layers, and learned parameters.

## Files
| File | Description |
|------|-------------|
| `day1_sprint_planning_baseline.ipynb` | Sprint plan + NN foundations + baseline model + recorded metrics |

## Topics Covered
- Agile Sprint structure — Goal, Backlog, Definition of Done
- Why deep learning and when it is appropriate vs classical ML
- The neuron: weighted sum + bias + activation (the Week 2 dot product)
- Layers: input, hidden, output — what "deep" means
- Weights and biases as the learned parameters
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
