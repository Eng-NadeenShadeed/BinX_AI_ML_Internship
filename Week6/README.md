# Week 6 — Deep Learning (Sprint 1)

## Overview

Week 6 introduces the fundamentals of Deep Learning and moves from
classical machine learning models to neural networks.

The week focuses on understanding how neural networks learn, starting
from the basic neuron and layer architecture, then moving through
activation functions, forward propagation, loss functions, backpropagation,
gradient descent, and optimizers.

The practical work applies these concepts to the Cardiac Patient
Monitoring System using the heart disease dataset. The week progresses
from a Random Forest baseline to building, training, regularizing, tuning,
and evaluating neural network models using TensorFlow/Keras.

Day 5 completes Sprint 1 by systematically tuning the neural network,
using EarlyStopping, selecting the best configuration, evaluating the
final model on the unseen test set, and comparing it against the
Random Forest baseline.

---

## Repository Structure

```text
Week6/

├── Day1/
│   ├── day1_sprint_planning_baseline.ipynb
│   └── README.md
│
├── Day2/
│   ├── day2_activations_forward_pass.ipynb
│   └── README.md
│
├── Day3/
│   ├── day3_training_mechanics.ipynb
│   └── README.md
│
├── Day4/
│   ├── day4_keras_network.ipynb
│   └── README.md
│
├── Day5/
│   ├── day5_tuning_sprint_review.ipynb
│   └── README.md
│
└── README.md
```
## Dataset

**heart.csv** — Heart Disease Prediction Dataset

918 records · 12 original columns · binary target (`HeartDisease`)

| Column | Type | Description |
|--------|------|-------------|
| `Age` | numeric | Patient age in years |
| `Sex` | categorical | Patient sex |
| `ChestPainType` | categorical | Type of chest pain |
| `RestingBP` | numeric | Resting blood pressure |
| `Cholesterol` | numeric | Serum cholesterol level |
| `FastingBS` | binary | Fasting blood sugar > 120 mg/dl |
| `RestingECG` | categorical | Resting electrocardiogram result |
| `MaxHR` | numeric | Maximum heart rate achieved |
| `ExerciseAngina` | categorical | Exercise-induced angina |
| `Oldpeak` | numeric | ST depression induced by exercise |
| `ST_Slope` | categorical | Slope of the peak exercise ST segment |
| `HeartDisease` | binary | Target variable: 0 = No Disease, 1 = Disease |

Key preprocessing steps:

- Numeric features → median imputation + `StandardScaler`
- Categorical features → most-frequent imputation + `OneHotEncoder`
- `FastingBS` treated as a binary feature
- Train / Validation / Test split: 60% / 20% / 20%
- Test set kept unseen until final evaluation

The same preprocessing pipeline was maintained throughout the sprint
to ensure a fair comparison between the Random Forest baseline and
the neural network models.

---

## Daily Progress

### Day 1 — Sprint Planning, Neural Network Foundations & Baseline

**Theory:** Introduced the Sprint 1 goal, backlog, Definition of Done,
and the role of neural networks in deep learning.

**Hands-On:** Established the Random Forest baseline for the cardiac
project and prepared the data pipeline for neural network experiments.

- Defined the Sprint 1 objective and acceptance criteria
- Reviewed the neuron: weighted sum + bias + activation
- Covered input, hidden, and output layers
- Explained weights, biases, and model parameters
- Prepared train / validation / test splits
- Built the preprocessing pipeline for numerical and categorical features
- Trained and evaluated the Random Forest baseline
- Recorded baseline metrics for later comparison

---

### Day 2 — Activation Functions & Forward Propagation

**Theory:** Studied how activation functions introduce non-linearity
and how data moves forward through a neural network.

**Topics covered:**

- ReLU activation
- Sigmoid activation
- Tanh activation
- Softmax activation
- Choosing activation functions based on the task
- Forward propagation
- Weighted sums and biases
- Producing predictions from the output layer

**Hands-On:** Worked through forward-pass calculations and connected
the mathematical process to the architecture of the cardiac prediction
network.

---

### Day 3 — Backpropagation, Gradient Descent & Optimizers

**Theory:** Covered how neural networks learn by calculating errors,
propagating gradients backward, and updating model weights.

**Topics covered:**

- Binary Cross-Entropy loss
- Backpropagation
- Chain rule
- Gradients
- Gradient descent
- Learning rate
- Epochs and batches
- Training loop
- Adam optimizer
- SGD optimizer
- Comparison of Adam and SGD

**Hands-On:** Connected the mathematical training process to how Keras
updates network parameters during model training.

---

### Day 4 — Building & Training a Network in Keras

**Theory:** Translated the concepts from Days 1–3 into a working neural
network using TensorFlow/Keras.

**Hands-On:** Built and trained two neural network versions for heart
disease classification.

- Used the Keras Sequential API
- Built `Dense` layers and defined the network architecture
- Configured the input and output layers
- Used ReLU for hidden layers and Sigmoid for binary classification
- Compiled the model using Adam and Binary Cross-Entropy
- Trained the network and monitored the training history
- Plotted training and validation loss and accuracy
- Diagnosed overfitting from the learning curves
- Added Batch Normalization to stabilize training
- Added Dropout for regularization
- Evaluated the models on the test set
- Compared V1, V2, and the Random Forest baseline

---

### Day 5 — Hyperparameter Tuning, EarlyStopping & Sprint Review

**Theory:** Completed the neural network training cycle by tuning the
main hyperparameters and reviewing the complete Sprint 1 workflow.

**Hands-On:** Ran four systematic tuning experiments while keeping the
test set reserved for final evaluation.

**Experiment 1 — Learning Rate**

- Tested different learning rates
- Compared training and validation loss curves
- Selected the best learning rate for the following experiments

**Experiment 2 — Network Depth & Width**

- Compared three network sizes:
  - Small: `32 → 16`
  - Medium: `64 → 32`
  - Large: `128 → 64`
- Compared model capacity and validation performance
- Selected the best architecture

**Experiment 3 — Dropout Rate**

- Tested Dropout rates: `0.1`, `0.3`, and `0.5`
- Compared regularization strength and training stability
- Selected the most suitable Dropout rate

**Experiment 4 — Batch Size**

- Tested batch sizes: `16`, `32`, and `64`
- Compared convergence and training stability
- Selected the best batch size

**Final Model:**

- Assembled the best configuration from the four experiments
- Used Batch Normalization and Dropout
- Applied `EarlyStopping` to prevent unnecessary training
- Restored the best validation weights
- Evaluated the final model on the unseen test set
- Compared the final neural network against V1, V2, and the RF baseline

**Sprint Review:**

- Completed the Sprint 1 backlog
- Reviewed the full neural network pipeline
- Compared classical ML and deep learning approaches
- Documented the final findings and lessons learned

---

## Final Sprint 1 Comparison

| Model | Accuracy | Precision | Recall | F1-score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| RF Baseline | 0.8859 | 0.8716 | 0.9314 | 0.9005 | 0.9427 |
| NN V1 | 0.8152 | 0.8542 | 0.8039 | 0.8283 | 0.8727 |
| NN V2 | 0.8424 | 0.8544 | 0.8627 | 0.8585 | 0.8941 |
| NN Final (tuned) | 0.8533 | 0.8713 | 0.8627 | 0.8670 | 0.9182 |

The final tuned neural network improved substantially over the initial
V1 and V2 versions, but it did not surpass the Random Forest baseline
on the held-out test set.

This confirms that neural networks do not automatically outperform
classical machine learning models, especially on structured tabular
datasets where ensemble methods such as Random Forest can be highly
competitive.

---

## Key Findings — Week 6

```text
NN V1
→ Initial network without regularization
→ Showed noticeable overfitting during training

NN V2
→ Added Batch Normalization + Dropout
→ Improved generalization compared with V1

Hyperparameter Tuning
→ Learning rate, architecture, Dropout, and batch size were tested
→ EarlyStopping was used to select the best training point

Final NN
→ Improved over both initial neural network versions
→ Still remained below the Random Forest baseline on the test set

RF Baseline
→ Remained the strongest model in Sprint 1
→ Demonstrated that classical ML is still highly competitive for
  structured tabular heart disease data
  ```

  ## Sprint 1 Retrospective

### What Went Well

- Built a complete neural network training pipeline using TensorFlow/Keras
- Connected neural network theory with practical implementation
- Used training curves to diagnose overfitting and convergence
- Applied Batch Normalization and Dropout as regularization techniques
- Performed systematic hyperparameter experiments
- Used EarlyStopping to control unnecessary training
- Kept the test set reserved for final model evaluation
- Compared the neural network fairly against the established RF baseline

### What to Improve

- Hyperparameter tuning was performed manually, one parameter at a time
- A more systematic search could explore interactions between
  hyperparameters more efficiently
- Cross-validation could provide a more robust estimate of model
  performance on this relatively small tabular dataset

### One Concrete Change for Sprint 2

In Sprint 2, I will keep experiment configurations and validation
metrics in a structured experiment log from the beginning, making
model comparison and decision-making easier to track.

---

## Progress Checklist

- [x] Day 1 — Sprint Planning, NN Foundations & RF Baseline
- [x] Day 2 — Activation Functions & Forward Propagation
- [x] Day 3 — Backpropagation, Gradient Descent & Optimizers
- [x] Day 4 — Building & Training a Network in Keras
- [x] Day 5 — Hyperparameter Tuning, EarlyStopping & Sprint Review

---

## Tools Used

`TensorFlow 2.21` · `Keras` · `scikit-learn` · `pandas` · `numpy` ·
`matplotlib` · Jupyter Notebook · Git & GitHub