# Week 6 — Day 3: Backpropagation, Gradient Descent & Optimizers

## Overview
Day 3 completes the training loop introduced conceptually in Day 2.
It covers how the network assigns blame to each weight through
backpropagation, how gradient descent updates those weights, and
what optimizers, epochs, and batches mean in practice.

## Files
```
Week6/
└── Day3/
├── day3_training_mechanics.ipynb
└── README.md
```

## Topics Covered
- The complete 4-step training loop — forward pass, loss, backprop, update
- Gradient descent — the hillside intuition and the update rule
- The learning rate — the most important hyperparameter
- Learning rate experiment — too high, too low, just right (with loss curves)
- Backpropagation — chain rule, gradient computation, automatic differentiation
- Gradient descent visualization — one weight, one update step
- Optimizers — Adam vs SGD, when to use each
- Epochs and batches — definitions, defaults, and steps per epoch

## Key Results — Learning Rate Experiment

| Learning Rate | Final Val Loss | Behaviour |
|---------------|----------------|-----------|
| 1.0 (too high) | 0.7022 | Unstable — overshoots minimum |
| 0.00001 (too low) | 0.7323 | Too slow — barely learns in 80 epochs |
| 0.001 (just right) | 0.4128 | Steady convergence — best result |

## Defaults Used in This Project
- Optimizer: Adam
- Learning rate: 0.001
- Batch size: 32
- Epochs: determined by EarlyStopping (Day 5)