# Week 7 — Sprint 2: CNNs, RNNs & Transformers

## Overview
Sprint 2 of the Cardiac Patient Monitoring System capstone project.
This week covered the three major deep learning architectures beyond
Dense Networks — CNNs for images, RNNs/LSTMs for sequences, and
Transformers for text — each applied to a real dataset in its appropriate
domain. The sprint closed with a Dense Network on 70,000 cardiovascular
patients that beat the Random Forest baseline, confirming that dataset
size was the critical limiting factor in Sprint 1.

## Structure
```
Week7/
├── Day 1/ ← Sprint 2 planning + CNN introduction
├── Day 2/ ← CNN + Transfer Learning (Melanoma)
├── Day 3/ ← RNNs & LSTMs (ECG heartbeats)
├── Day 4/ ← Attention & Transformers (Medical Abstracts)
├── Day 5/ ← Sprint 2 Close-Out (Cardiovascular 70K)
└── README.md
```

## Datasets Used

| Day | Dataset | Task | Size |
|-----|---------|------|------|
| Day 1 | Synthetic image | Convolution demo | — |
| Day 2 | Melanoma Skin Cancer | Benign vs Malignant | 11,890 images |
| Day 3 | MIT-BIH Arrhythmia | 5-class ECG classification | 109,446 heartbeats |
| Day 4 | Medical Abstracts | 5-class disease classification | 14,438 abstracts |
| Day 5 | Cardiovascular Disease | Binary classification | 70,000 patients |

## Results Summary

### Day 2 — CNN & Transfer Learning (Melanoma)

| Model | Test Accuracy | Test AUC |
|-------|--------------|---------|
| CNN from Scratch | 88.11% | 0.9514 |
| **CNN + Augmentation** | **88.95%** | **0.9579** |
| MobileNetV2 (frozen) | 86.47% | 0.9383 |

**Key finding:** Data augmentation reduced overfitting and outperformed
transfer learning — the frozen MobileNetV2 base could not adapt to
melanoma-specific features.

### Day 3 — RNNs & LSTMs (ECG Heartbeats)

| Model | Test Accuracy | Macro F1 |
|-------|--------------|---------|
| Plain RNN | 83.02% | ~0.10 |
| **LSTM + class_weight** | **91.14%** | **0.650** |

**Key finding:** Plain RNN completely failed on minority arrhythmia classes —
predicted Normal for virtually every input. LSTM's gated memory produced
meaningful detection across all 5 classes. Class weighting was necessary
to force attention on rare arrhythmia types.

### Day 4 — Attention & Transformers (Medical Abstracts)

| Model | Test Accuracy | Macro F1 |
|-------|--------------|---------|
| BiLSTM (from scratch) | 71.49% | 0.604 |
| **DistilBERT (fine-tuned)** | **83.61%** | **0.831** |

**Key finding:** Pretrained weights matter most when task-specific data
is small. DistilBERT's advantage was largest on Digestive diseases
(BiLSTM F1: 0.104 vs DistilBERT F1: 0.814) — a class with only ~1,000
training abstracts. Data leakage was discovered and corrected before training.

### Day 5 — Sprint 2 Core Model (Cardiovascular 70K)

| Model | Test F1 | Test AUC |
|-------|---------|---------|
| RF Baseline | 0.7064 | 0.7737 |
| **Dense 64→32 (Exp 1)** | **0.7191** | **0.8023** |
| Dense 128→64→32 (Exp 2) | 0.7157 | 0.8022 |
| Dense 256→128→64 (Exp 3) | 0.7162 | 0.8020 |
| Dense 64→32, LR=0.0005 (Exp 4) | 0.7168 | 0.8020 |

**Key finding:** All Dense Networks beat the RF baseline. The simplest
architecture (64→32) performed best — the cardiovascular features do not
require deep non-linear transformations. Dataset size was the critical
factor: 70,000 patients gave the neural network the data it needed
to outperform classical models.

## Architecture Decision Map

| Data Type | Architecture | Applied To |
|-----------|-------------|-----------|
| Images | CNN + Augmentation | Melanoma classification |
| Sequential | LSTM + class_weight | ECG arrhythmia detection |
| Text | DistilBERT (fine-tuned) | Medical abstracts classification |
| **Tabular** | **Dense Network** | **Cardiovascular risk prediction** |

## Sprint 2 vs Sprint 1

| | Sprint 1 (Week 6) | Sprint 2 (Week 7) |
|--|------------------|------------------|
| Dataset | heart.csv (918 rows) | cardio_train.csv (70,000 rows) |
| RF Baseline F1 | 0.9005 | 0.7064 |
| Best NN F1 | 0.8670 ✗ lost to RF | **0.7191 ✓ beat RF** |
| Training behavior | Overfit | Healthy — train ≈ val |
| Root cause identified | Dataset too small | More data = NN advantage |

## Sprint 2 Retrospective

**What went well:**
- Central hypothesis confirmed from Experiment 1
- Experiment log captured every configuration and result
- All four architectures studied with real datasets and genuine results
- No overfitting on 70K cardiovascular data

**What to improve:**
- No ensemble methods tested on cardiovascular data
- Gradio demo for cardiac model not completed this sprint
- Model saving should happen immediately after training (learned from Day 4)

**Concrete change for Sprint 3:**
Save every trained model to Drive immediately after training completes —
before moving to the next cell.

## Sprint 3 Focus
NLP/CV integration and final project evaluation.

## Tools Used
TensorFlow/Keras • Hugging Face Transformers • Scikit-learn •
Matplotlib • Seaborn • Gradio • Git & GitHub • Google Colab (T4 GPU)
ذذذ
ذ
ذذ
