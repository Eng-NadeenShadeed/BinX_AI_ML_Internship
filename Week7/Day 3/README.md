# Week 7 · Day 3 — RNNs & LSTMs for Sequential Data

## Overview
I built and compared two sequence models on the MIT-BIH Arrhythmia Dataset —
87,554 segmented ECG heartbeat signals across 5 classes. Starting with a
Plain RNN as a baseline, I identified its complete failure on minority classes
due to the vanishing gradient problem, then trained an LSTM with class
weighting as a targeted improvement. The lab includes confusion matrices,
a classification report, and an interactive Gradio demo for single-heartbeat
classification.

## Files
```
Day 3/
├── day3_rnn_lstm.ipynb
├── Hands_On_Lab.ipynb
├── README.md
└── Data/
├── mitbih_train.csv
└── mitbih_test.csv 
```

## Topics Covered
- Why sequential data needs order-aware architectures
- RNN hidden state and memory across time steps
- Backpropagation Through Time (BPTT)
- Vanishing gradient problem — proven with visualization
- LSTM gates (forget, input, output) and cell state
- GRU — simplified LSTM with two gates
- Embeddings for text sequences (theory)
- Class imbalance handling with class_weight
- Confusion matrix and classification report
- Interactive prediction demo with Gradio

## Dataset
MIT-BIH Arrhythmia Dataset — 5-class ECG heartbeat classification

| Class | Label | Train Count | % |
|-------|-------|-------------|---|
| 0 | Normal | 72,471 | 82.8% |
| 1 | Supraventricular | 2,223 | 2.5% |
| 2 | Ventricular | 5,788 | 6.6% |
| 3 | Fusion | 641 | 0.7% |
| 4 | Unknown | 6,431 | 7.3% |

## Hands-On Lab Results

| Model | Accuracy | Loss | Macro F1 |
|-------|----------|------|----------|
| Plain RNN | 83.02% | 0.6222 | ~0.10 |
| **LSTM + class_weight** | **91.14%** | **0.2949** | **0.650** |

### Per-Class Recall

| Class | Plain RNN | LSTM |
|-------|-----------|------|
| Normal | 99.6% | 95.6% |
| Supraventricular | 5.2% | 36.2% |
| Ventricular | 2.8% | 67.2% |
| Fusion | 0.0% | 35.2% |
| Unknown | 0.0% | 87.4% |

### Key Findings
- Plain RNN predicted Normal for virtually every input — confirmed by
  confusion matrix showing a single dark column
- Vanishing gradient prevented meaningful learning across 187 time steps
- LSTM's gated memory produced a real diagonal in the confusion matrix
- Class weighting was necessary to force attention on minority classes
- Macro F1 (0.650) is the honest metric here — weighted avg (0.911)
  is dominated by Normal performance
- Fusion remains the hardest class (F1: 0.347) — only 641 training samples
- Gradio interface built for interactive single-heartbeat prediction

## Next
**Day 4 — Attention & Transformers:**
Self-attention mechanism, multi-head attention, positional encoding,
and Transformer architecture — with Hugging Face pretrained models.