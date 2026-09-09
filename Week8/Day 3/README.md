<div align="center">

<h1>🩻 Week 8 — Day 3</h1>

<h2>Computer Vision — Chest X-Ray Pneumonia Detection</h2>

<p>

<b>Building an end-to-end computer vision pipeline for pediatric chest X-ray classification using CNNs, OpenCV, and MobileNetV2.</b>

</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Day%203-DB2777?style=for-the-badge&labelColor=FCE7F3">

<img src="https://img.shields.io/badge/Computer%20Vision-OpenCV-EC4899?style=for-the-badge&labelColor=FFF1F2">

<img src="https://img.shields.io/badge/CNN-Deep%20Learning-A855F7?style=for-the-badge&labelColor=FAE8FF">

<img src="https://img.shields.io/badge/Transfer%20Learning-MobileNetV2-DB2777?style=for-the-badge&labelColor=FCE7F3">

</div>

---

## 🧠 Overview

<table>

<tr>

<td bgcolor="#FFF9FC">

Day 3 moved from text-based medical data to <b>computer vision</b> by building a complete image classification pipeline for pediatric chest X-rays.

The objective was to classify chest X-ray images into two categories:

<ul>
<li><b>NORMAL</b></li>
<li><b>PNEUMONIA</b></li>
</ul>

The workflow covered the complete journey from raw medical images to trained deep learning models:

<b>Image Audit → OpenCV Preprocessing → Data Augmentation → CNN → Transfer Learning → Evaluation → Error Analysis → Gradio Prototype</b>

Two approaches were implemented and compared:

<ul>
<li><b>CNN from Scratch</b> — trained specifically for the task</li>
<li><b>MobileNetV2 Transfer Learning</b> — based on ImageNet pretrained visual features</li>
</ul>

The day also highlighted an important machine learning lesson:

<b>High validation performance does not automatically guarantee strong generalization on unseen test data.</b>

</td>

</tr>

</table>

---

## 📁 Files

| File                                         | Description                                       |
| -------------------------------------------- | ------------------------------------------------- |
| `day3_chest_xray_cnn.ipynb`                  | Main notebook — complete computer vision pipeline |
| `Data/chest_xray/train/`                     | Training images                                   |
| `Data/chest_xray/test/`                      | Untouched test images                             |
| `Data/chest_xray/val/`                       | Original validation folder                        |


> <b>Note:</b> The original validation folder contained only 16 images, so it was not suitable for reliable validation. A new 20% validation split was created from the original training set while keeping the test set untouched.

---

## 🏥 Dataset

### Chest X-Ray Images — Pneumonia

The dataset used for this computer vision task is the <b>Chest X-Ray Images (Pneumonia)</b> dataset.

<table>

<tr bgcolor="#FCE7F3">
<th>Property</th>
<th>Value</th>
</tr>

<tr>
<td><b>Total Images</b></td>
<td>5,856</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Source</b></td>
<td>Guangzhou Women and Children's Medical Center</td>
</tr>

<tr>
<td><b>Patient Group</b></td>
<td>Pediatric patients aged 1–5 years</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Task</b></td>
<td>Binary Classification</td>
</tr>

<tr>
<td><b>Classes</b></td>
<td>NORMAL / PNEUMONIA</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Original Training Images</b></td>
<td>5,216</td>
</tr>

<tr>
<td><b>Test Images</b></td>
<td>624</td>
</tr>

</table>

### Class Distribution

The dataset is imbalanced toward the PNEUMONIA class.

| Split      | NORMAL | PNEUMONIA | Total |
| :--------- | -----: | --------: | ----: |
| Training   |  1,073 |     3,100 | 4,173 |
| Validation |    268 |       775 | 1,043 |
| Test       |    234 |       390 |   624 |

The training data contains approximately <b>2.9× more PNEUMONIA images than NORMAL images</b>.

---

## 📚 Topics Covered

<table>

<tr>

<td bgcolor="#FFF9FC">

<ul>
<li>Why CNNs are suitable for image data</li>
<li>Image representation — pixels, channels, and dimensions</li>
<li>Dataset structure and class distribution</li>
<li>Image size variation audit</li>
<li>OpenCV image loading and processing</li>
<li>BGR → RGB color conversion</li>
<li>Image resizing</li>
<li>Pixel normalization</li>
<li>Data augmentation</li>
<li>Training / validation split correction</li>
<li>CNN architecture from scratch</li>
<li>EarlyStopping and ReduceLROnPlateau</li>
<li>Accuracy, Precision, Recall, F1, and AUC</li>
<li>Confusion Matrix analysis</li>
<li>Transfer Learning</li>
<li>MobileNetV2 with ImageNet pretrained weights</li>
<li>Frozen feature extraction</li>
<li>CNN vs MobileNetV2 comparison</li>
<li>Generalization gap analysis</li>
<li>Gradio inference prototype</li>
</ul>

</td>

</tr>

</table>

---

## 🖼️ Why CNNs for Medical Images?

Images contain spatial relationships that ordinary fully connected networks do not exploit efficiently.

A CNN learns hierarchical visual features:

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FCE7F3">

<b>Pixels</b>

<br>

↓

<br>

Edges & Simple Patterns

</td>

<td align="center" bgcolor="#FFF9FC">

<b>Feature Maps</b>

<br>

↓

<br>

Shapes & Structures

</td>

<td align="center" bgcolor="#FAE8FF">

<b>Deep Features</b>

<br>

↓

<br>

Medical Image Patterns

</td>

</tr>

</table>

</div>

CNNs use <b>convolutional filters</b> and <b>parameter sharing</b> to detect meaningful spatial patterns while using fewer parameters than a fully connected approach.

---

## 🔍 Image Representation & Dimensions

A chest X-ray image can be represented as a tensor containing:

* Height
* Width
* Color channels

The original images had substantial variation in spatial dimensions.

<table>

<tr bgcolor="#FCE7F3">
<th>Class</th>
<th>Height Range</th>
<th>Width Range</th>
</tr>

<tr>
<td><b>NORMAL</b></td>
<td>974 – 2,226</td>
<td>1,196 – 2,442</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>PNEUMONIA</b></td>
<td>435 – 2,184</td>
<td>796 – 2,016</td>
</tr>

</table>

Because CNNs require consistent input dimensions, resizing was necessary before training.

---

## 🧪 Dataset Audit

The initial audit focused on:

* Dataset structure
* Class distribution
* Image dimensions
* Pixel ranges
* Data types
* Class imbalance
* Validation set size

The original validation set contained only <b>16 images</b>.

This was considered too small to provide a meaningful estimate of validation performance.

### Validation Set Decision

Instead of using the original validation folder, a <b>20% validation split</b> was created from the original training set.

The test set remained completely untouched.

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FFF9FC">

<b>Original Train</b>

<br>

5,216 images

</td>

<td align="center">

→

</td>

<td align="center" bgcolor="#FCE7F3">

<b>80%</b>

<br>

Training

<br>

4,173 images

</td>

<td align="center">

*

</td>

<td align="center" bgcolor="#FAE8FF">

<b>20%</b>

<br>

Validation

<br>

1,043 images

</td>

</tr>

</table>

</div>

The original <b>624-image test set remained untouched</b> for final evaluation.

---

## 🛠️ OpenCV Fundamentals

OpenCV was used to prepare raw images before they entered the computer vision pipeline.

The main operations included:

<table>

<tr bgcolor="#FCE7F3">
<th>Operation</th>
<th>Purpose</th>
</tr>

<tr>
<td><code>cv2.imread()</code></td>
<td>Load an image from disk</td>
</tr>

<tr bgcolor="#FFF9FC">
<td>BGR → RGB</td>
<td>Convert OpenCV's color order to RGB</td>
</tr>

<tr>
<td><code>cv2.resize()</code></td>
<td>Standardize image dimensions</td>
</tr>

<tr bgcolor="#FFF9FC">
<td>Normalization</td>
<td>Scale pixel values from [0, 255] to [0, 1]</td>
</tr>

</table>

---

## 🔄 Image Preprocessing Pipeline

For the CNN pipeline, every image was transformed into a consistent representation:

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FFF9FC">

<b>Raw Image</b>

<br>

Different Sizes

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FCE7F3">

<b>Resize</b>

<br>

150 × 150

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FAE8FF">

<b>Normalize</b>

<br>

[0, 1]

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FFF9FC">

<b>Model Input</b>

<br>

150 × 150 × 3

</td>

</tr>

</table>

</div>

### CNN Preprocessing

| Property    | Value       |
| :---------- | :---------- |
| Image Size  | `150 × 150` |
| Channels    | `3`         |
| Data Type   | `float32`   |
| Pixel Range | `[0, 1]`    |

The preprocessing step standardized the spatial dimensions and pixel scale without performing medical image enhancement or contrast correction.

---

## 🎨 Data Augmentation

Data augmentation was applied to the training data to introduce controlled visual variation.

The augmentation configuration included:

* Rotation
* Zoom
* Width shift
* Height shift
* Horizontal flip
* Small brightness variation

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FCE7F3">

<b>Original Training Image</b>

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FFF9FC">

<b>Random Transformation</b>

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FAE8FF">

<b>Augmented Image</b>

</td>

</tr>

</table>

</div>

Augmentation was applied <b>only to training data</b>.

Validation and test images were kept unchanged to preserve a realistic evaluation setting.

---

## 🧠 CNN From Scratch

The first model was built entirely from scratch.

### Architecture

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FFF9FC">

<b>Input</b>

<br>

150 × 150 × 3

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FCE7F3">

<b>Conv Block 1</b>

<br>

32 Filters

<br>

MaxPooling

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FFF9FC">

<b>Conv Block 2</b>

<br>

64 Filters

<br>

MaxPooling

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FCE7F3">

<b>Conv Block 3</b>

<br>

128 Filters

<br>

MaxPooling

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FAE8FF">

<b>Classifier</b>

<br>

Dense → Dropout → Sigmoid

</td>

</tr>

</table>

</div>

### Model Configuration

| Component          | Configuration       |
| :----------------- | :------------------ |
| Convolution Blocks | 3                   |
| Filters            | 32 → 64 → 128       |
| Activation         | ReLU                |
| Pooling            | MaxPooling2D        |
| Dense Layer        | 64 units            |
| Dropout            | 0.5                 |
| Output             | Sigmoid             |
| Optimizer          | Adam                |
| Learning Rate      | 0.001               |
| Loss               | Binary Crossentropy |
| Parameters         | 2.46M               |

Training used:

* EarlyStopping
* ReduceLROnPlateau
* Maximum 30 epochs

---

## 📊 CNN Evaluation

The CNN was evaluated on the untouched 624-image test set.

### Results

<table>

<tr bgcolor="#FCE7F3">
<th>Metric</th>
<th>Score</th>
</tr>

<tr>
<td><b>Test Accuracy</b></td>
<td><b>83.01%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Pneumonia Recall</b></td>
<td><b>98.97%</b></td>
</tr>

<tr>
<td><b>F1-Score</b></td>
<td><b>87.93%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>AUC</b></td>
<td><b>0.9401</b></td>
</tr>

</table>

### Confusion Matrix

|                  | Predicted NORMAL | Predicted PNEUMONIA |
| :--------------- | ---------------: | ------------------: |
| Actual NORMAL    |              132 |                 102 |
| Actual PNEUMONIA |                4 |                 386 |

The model achieved very high PNEUMONIA recall but produced a relatively large number of <b>false positives</b> for NORMAL images.

---

## 🚀 Transfer Learning — MobileNetV2

Instead of training an entire CNN from scratch, the second approach used <b>MobileNetV2</b> with ImageNet pretrained weights.

The pretrained convolutional base was frozen, and a new classification head was added.

### Architecture

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FFF9FC">

<b>Input</b>

<br>

224 × 224 × 3

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FCE7F3">

<b>MobileNetV2</b>

<br>

Frozen Base

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FAE8FF">

<b>Global Average Pooling</b>

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FFF9FC">

<b>Dropout</b>

<br>

0.3

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FCE7F3">

<b>Sigmoid</b>

</td>

</tr>

</table>

</div>

### Model Configuration

| Property             | Value                  |
| :------------------- | :--------------------- |
| Architecture         | MobileNetV2            |
| Pretrained Weights   | ImageNet               |
| Input Size           | `224 × 224 × 3`        |
| Base Trainable       | No                     |
| Pooling              | Global Average Pooling |
| Dropout              | 0.3                    |
| Output               | Sigmoid                |
| Total Parameters     | 2,259,265              |
| Trainable Parameters | 1,281                  |

MobileNetV2 preprocessing was used to transform pixel values to the range expected by the pretrained network.

---

## 📈 MobileNetV2 Evaluation

The MobileNetV2 model was evaluated using the same untouched test set.

### Results

<table>

<tr bgcolor="#FCE7F3">
<th>Metric</th>
<th>Score</th>
</tr>

<tr>
<td><b>Test Accuracy</b></td>
<td><b>83.49%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Pneumonia Recall</b></td>
<td><b>99.23%</b></td>
</tr>

<tr>
<td><b>F1-Score</b></td>
<td><b>88.26%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>AUC</b></td>
<td><b>0.9690</b></td>
</tr>

</table>

### Confusion Matrix

|                  | Predicted NORMAL | Predicted PNEUMONIA |
| :--------------- | ---------------: | ------------------: |
| Actual NORMAL    |              134 |                 100 |
| Actual PNEUMONIA |                3 |                 387 |

The model correctly identified <b>387 out of 390 PNEUMONIA cases</b>, corresponding to a PNEUMONIA recall of <b>99.23%</b>.

However, <b>100 NORMAL images were classified as PNEUMONIA</b>, showing that the model still tends to favor the PNEUMONIA class.

---

## ⚖️ CNN vs MobileNetV2

<table>

<tr bgcolor="#FCE7F3">
<th>Metric</th>
<th>CNN</th>
<th>MobileNetV2</th>
</tr>

<tr>
<td><b>Accuracy</b></td>
<td>83.01%</td>
<td><b>83.49%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Precision</b></td>
<td>79.10%</td>
<td><b>79.47%</b></td>
</tr>

<tr>
<td><b>Pneumonia Recall</b></td>
<td>98.97%</td>
<td><b>99.23%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>F1-Score</b></td>
<td>87.93%</td>
<td><b>88.26%</b></td>
</tr>

<tr>
<td><b>AUC</b></td>
<td>0.9401</td>
<td><b>0.9690</b></td>
</tr>

</table>

### Overall Observation

MobileNetV2 achieved the best result across all reported test metrics.

The improvement in Accuracy and F1 was relatively small, while the <b>AUC improvement from 0.9401 to 0.9690</b> was more noticeable.

This suggests that transfer learning provided stronger overall class-separation capability, even though the final classification threshold still produced many false positives.

---

## 🔎 Error Analysis

The confusion matrices revealed an important behavior shared by both models.

Both models achieved:

<b>Very high PNEUMONIA recall</b>

but also produced:

<b>A relatively high number of false positives for NORMAL images.</b>

For MobileNetV2:

* PNEUMONIA Recall → <b>99.23%</b>
* NORMAL Recall → <b>57.26%</b>
* False Positives → <b>100</b>
* False Negatives → <b>3</b>

This demonstrates why evaluating a medical classification model using <b>Accuracy alone</b> can be misleading.

Different metrics describe different aspects of model behavior.

---

## ⚠️ Validation vs Test Performance

One of the most important observations of Day 3 was the difference between validation and test performance.

MobileNetV2 achieved approximately:

<table>

<tr bgcolor="#FCE7F3">
<th>Evaluation Set</th>
<th>Accuracy</th>
</tr>

<tr>
<td><b>Validation</b></td>
<td><b>97.41%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Test</b></td>
<td><b>83.49%</b></td>
</tr>

</table>

The substantial gap indicates that the model's validation performance did not fully represent its generalization performance on the untouched test set.

This requires further investigation before considering the model for any real-world or clinical application.

Possible areas for further investigation include:

* Dataset distribution differences
* Generalization to unseen sources
* Data diversity
* Threshold selection
* False-positive analysis
* Model calibration
* External validation

The exact cause of the gap should not be assumed without additional experiments.

---

## 🎯 Key Decisions

<table>

<tr>

<td width="33%" align="center" bgcolor="#FFF9FC">

### Validation Split

<b>20% Validation Split</b>

The original 16-image validation set was replaced with a larger validation split created from the original training data.

</td>

<td width="33%" align="center" bgcolor="#FCE7F3">

### Test Integrity

<b>Untouched Test Set</b>

The 624 test images were kept separate and were not augmented or used during training.

</td>

<td width="33%" align="center" bgcolor="#FFF9FC">

### Evaluation Focus

<b>Recall + AUC</b>

Recall and AUC were emphasized alongside Accuracy, Precision, and F1 to better understand model behavior.

</td>

</tr>

</table>

---

## 🖥️ Gradio Prototype

After completing training and evaluation, the MobileNetV2 model was connected to a simple <b>Gradio interface</b>.

The prototype allows a user to:

<div align="center">

<table>

<tr>

<td align="center" bgcolor="#FCE7F3">

🩻

<br>

<b>Upload X-Ray</b>

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FFF9FC">

🧠

<br>

<b>MobileNetV2</b>

</td>

<td align="center">→</td>

<td align="center" bgcolor="#FAE8FF">

📊

<br>

<b>Prediction + Confidence</b>

</td>

</tr>

</table>

</div>

The interface was created as an educational prototype to demonstrate how a trained computer vision model can be connected to a simple interactive application.

> <b>Important:</b> The Gradio application is an educational prototype and is not intended for medical diagnosis or clinical decision-making.

---

## 🧪 Validation

The complete Day 3 pipeline was validated across the following stages:

<table>

<tr>

<td bgcolor="#FFF9FC">

✓ Dataset structure inspected

<br>

✓ Class distribution analyzed

<br>

✓ Image dimensions audited

<br>

✓ Original validation set evaluated

<br>

✓ New validation split created

<br>

✓ OpenCV preprocessing implemented

<br>

✓ Image resizing verified

<br>

✓ Pixel normalization verified

<br>

✓ Data augmentation applied to training data

<br>

✓ Validation and test data kept unaugmented

<br>

✓ CNN from scratch trained

<br>

✓ CNN test performance evaluated

<br>

✓ Confusion matrix analyzed

<br>

✓ MobileNetV2 transfer learning implemented

<br>

✓ MobileNetV2 input size verified at 224 × 224

<br>

✓ MobileNetV2 test performance evaluated

<br>

✓ CNN vs MobileNetV2 compared

<br>

✓ Validation–test performance gap documented

<br>

✓ Gradio inference prototype created

</td>

</tr>

</table>

---

## 🏆 What We Achieved

<div align="center">

|            Stage            | Status |
| :-------------------------: | :----: |
|        Dataset Audit        |    ✓   |
| Class Distribution Analysis |    ✓   |
|     Image Size Analysis     |    ✓   |
|     OpenCV Preprocessing    |    ✓   |
|        Image Resizing       |    ✓   |
|     Pixel Normalization     |    ✓   |
|      Data Augmentation      |    ✓   |
| Validation Split Correction |    ✓   |
|       CNN From Scratch      |    ✓   |
|         CNN Training        |    ✓   |
|        CNN Evaluation       |    ✓   |
|  Confusion Matrix Analysis  |    ✓   |
|      Transfer Learning      |    ✓   |
|         MobileNetV2         |    ✓   |
|       Model Comparison      |    ✓   |
|        Error Analysis       |    ✓   |
| Generalization Gap Analysis |    ✓   |
|       Gradio Prototype      |    ✓   |

<br>

<table>

<tr>

<td align="center" bgcolor="#FCE7F3">

### 🩻 Raw X-Ray → Preprocessing → Augmentation → CNN / Transfer Learning → Evaluation → Interactive Prototype

</td>

</tr>

</table>

</div>

---

## 💡 Key Takeaways

<table>

<tr>

<td width="50%" bgcolor="#FFF9FC">

### 🧠 Technical

Computer vision models require carefully standardized inputs.

CNNs can learn spatial patterns directly from images, while transfer learning allows pretrained visual features to be reused for a new task.

</td>

<td width="50%" bgcolor="#FCE7F3">

### 📊 Evaluation

A single metric is not enough.

Accuracy, Precision, Recall, F1, AUC, and the Confusion Matrix reveal different aspects of model behavior.

</td>

</tr>

<tr>

<td width="50%" bgcolor="#FCE7F3">

### 🔍 Generalization

Strong validation performance does not automatically mean strong performance on unseen data.

The MobileNetV2 validation–test gap became an important finding requiring further investigation.

</td>

<td width="50%" bgcolor="#FFF9FC">

### 🩻 Medical AI

High recall can be valuable when missing a positive case is costly, but false positives also matter.

The model therefore requires deeper validation before any real-world clinical use.

</td>

</tr>

</table>

---

## 🔜 Next

<div align="center">

<img src="https://img.shields.io/badge/DAY%204-End--to--End%20Pipeline%20%2B%20Error%20Analysis-DB2777?style=for-the-badge&labelColor=FCE7F3">

### End-to-End Pipeline + Error Analysis

The next stage focuses on bringing the learned concepts together into a more complete machine learning workflow and performing deeper error analysis.

<b>Pipeline Integration → Model Comparison → Error Analysis → Improvement</b>

</div>

---

<div align="center">

## 🌸 Week 8 — Sprint 3

### NLP → Representation → Classification → Computer Vision

`─────────────────────────`

<b>From Medical Text to Medical Images</b>

<br><br>

<sub>BinX Tech AI & ML Internship · Week 8 · Day 3</sub>

</div>
