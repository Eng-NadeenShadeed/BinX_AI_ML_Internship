# Week 7 · Day 2 — Building CNNs & Transfer Learning

## Overview
I built and compared three approaches for binary melanoma skin cancer
classification (Benign vs Malignant). Starting from a CNN trained from
scratch as a baseline, I added data augmentation to reduce overfitting,
then applied transfer learning using MobileNetV2 pretrained on ImageNet.
Data augmentation produced the best overall result.

## Files
```
Day 2/
├── day2_cnn_transfer_learning.ipynb
├── Hands_On_Lab.ipynb
└── README.md
```

## Topics Covered
- Pooling — shrinking feature maps with Max Pooling
- Full CNN architecture — Conv + Pool blocks + Flatten + Dense
- Data augmentation — random flips, rotations, zooms, brightness
- Transfer learning — frozen MobileNetV2 + new classification head
- GlobalAveragePooling2D vs Flatten
- Training callbacks — EarlyStopping and ReduceLROnPlateau

## Hands-On Lab Summary

### Dataset
| Split | Images | Batches |
|-------|--------|---------|
| Training | 8,322 | 261 |
| Validation | 1,783 | 56 |
| Test | 1,783 | 56 |

### Results

| Model | Test Accuracy | Test AUC | Test Loss |
|-------|--------------|----------|-----------|
| CNN from Scratch | 88.11% | 0.9514 | 0.2826 |
| CNN + Augmentation | **88.95%** | **0.9579** | **0.2632** |
| MobileNetV2 (frozen) | 86.47% | 0.9383 | 0.3165 |

### Key Findings
- CNN from Scratch showed clear overfitting after Epoch 8 —
  training accuracy kept climbing while validation plateaued
- Data augmentation reduced overfitting and improved all three metrics
- MobileNetV2 underperformed despite pretrained weights — the frozen
  convolutional base could not adapt to melanoma-specific features
- Fine-tuning MobileNetV2 layers is the logical next step

## Dataset
| Dataset | Location | Size |
|---------|----------|------|
| Melanoma — Benign | Day 1/Data/train/Benign/ | 6,289 images |
| Melanoma — Malignant | Day 1/Data/train/Malignant/ | 5,601 images |

## Next
**Day 3 — RNNs & LSTMs:**
Sequential data processing, hidden states, vanishing gradient problem,
and LSTM gated memory — on the dataset provided by the mentor.