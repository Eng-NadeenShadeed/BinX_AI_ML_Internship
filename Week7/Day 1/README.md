# Week 7 · Day 1 — Sprint 2 Planning & CNN Introduction

## Overview
First day of Sprint 2. I updated the project plan after replacing the cardiac
dataset with a larger 70K cardiovascular dataset, initialized the Sprint 2
experiment log with Sprint 1 reference results, and studied the foundations
of Convolutional Neural Networks — how convolution works, what feature maps
show, and why CNNs are far more efficient than dense networks on image data.

## Files
```
Day1/
├── day1_sprint2_planning_cnn_intro.ipynb
├── Hands_On_Lab.ipynb
├── README.md
└── Data/
    └── train/
    ├── Benign/ # 6,289 images
    └── Malignant/ # 5,601 images

```

## Topics Covered
- Sprint 2 planning — dataset change rationale and new experiment log
- Why dense networks fail on images — parameter count and no spatial awareness
- Convolution — filters, feature maps, stride, and padding
- Parameter sharing — one 3×3 filter vs thousands of dense connections
- Translation invariance — detecting patterns regardless of position
- Architecture decision — CNN for melanoma, Dense Network for cardiovascular data

## Hands-On Lab Summary
- Initialized Sprint 2 experiment log with Sprint 1 reference results
- Applied a vertical edge-detection filter to a synthetic grayscale image
- Visualized the resulting feature map and interpreted the output
- Compared Dense vs Conv parameter counts across four image sizes
- Confirmed architecture decisions for all Sprint 2 datasets

## Datasets
| Dataset | Location | Size |
|---------|----------|------|
| Melanoma — Benign | `Data/train/Benign/` | 6,289 images |
| Melanoma — Malignant | `Data/train/Malignant/` | 5,601 images |

> Note: The cardiovascular dataset (cardio_train.csv) will be used starting Day 5.

## Next
**Day 2 — Building a Full CNN:**
CNN architecture from scratch, pooling layers, data augmentation,
and transfer learning with a pretrained model on the Melanoma dataset.