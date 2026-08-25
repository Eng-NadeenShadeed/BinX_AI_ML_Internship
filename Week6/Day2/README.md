# Week 6 — Day 2: Activations, Forward Propagation & Loss

## Overview
Day 2 covers the mathematical building blocks that make neural networks
work — activation functions, forward propagation, and loss functions.
All concepts are applied to the heart disease binary classification task.

## Files
```
Week6/
└── Day2/
├── day2_activations_forward_pass.ipynb
└── README.md
```

## Topics Covered
- Why activation functions are essential — the linearity problem
- ReLU — formula, plot, and dead neuron problem
- Sigmoid — formula, plot, and use case
- Tanh — formula, plot, and comparison with sigmoid
- Softmax — probability distribution for multi-class tasks
- Visual comparison of all four activation functions
- How to choose an activation by layer and task
- Forward propagation — data flow through the network
- Loss functions — Binary Cross-Entropy, Categorical Cross-Entropy, MSE
- How to choose a loss function by task
- Project choices justified — ReLU (hidden), Sigmoid (output), Binary Cross-Entropy (loss)
- Manual forward pass computed in NumPy — weights, activations, prediction

## Key Decisions for the Heart Disease Project

| Layer | Choice | Reason |
|-------|--------|--------|
| Hidden layers | ReLU | Default — fast, no vanishing gradient |
| Output layer | Sigmoid | Binary task — output is a probability |
| Loss | Binary Cross-Entropy | Standard loss for binary classification |

## Forward Pass Result
A 3-input → 4-hidden → 1-output network with random weights
predicted No Heart Disease with 49.7% confidence —
as expected from an untrained network with random initialization.