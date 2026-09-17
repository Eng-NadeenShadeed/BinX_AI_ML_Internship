````markdown
<div align="center">

# 🌸 Technical Write-Up

## Cardiac Patient Monitoring System — Melanoma Classification

**End-to-end deep learning pipeline for binary melanoma image classification, model serving, and public deployment.**

![AI](https://img.shields.io/badge/AI%20%26%20ML-8B1E3F?style=flat-square&logoColor=white)
![CNN](https://img.shields.io/badge/CNN-C44569?style=flat-square&logoColor=white)
![ISIC](https://img.shields.io/badge/ISIC-f8a5c2?style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-8B1E3F?style=flat-square&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-C44569?style=flat-square&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-f8a5c2?style=flat-square)

</div>

---

## 🧠 1. Problem Statement

This project explores a **binary image classification** task using dermoscopic images from a melanoma dataset.

The goal is to develop a deep learning model that classifies an input image into one of two classes:

| Class | Label |
|---|---:|
| Benign | 0 |
| Malignant | 1 |

The project follows an end-to-end machine learning workflow:

```text
Data
  ↓
Preprocessing
  ↓
CNN Development
  ↓
Model Comparison
  ↓
Evaluation
  ↓
Model Serialization
  ↓
FastAPI
  ↓
Streamlit
  ↓
Public Deployment
````

> ⚠️ **Disclaimer:** This project was developed for educational and research purposes and is not intended for clinical diagnosis.

---

## 📊 2. Dataset

The project uses a melanoma image dataset containing **11,888 images** across two classes.

### Dataset Distribution

| Class     |     Images |
| --------- | ---------: |
| Benign    |      6,289 |
| Malignant |      5,601 |
| **Total** | **11,888** |

### Dataset Splits

| Split      | Images | Batches |
| ---------- | -----: | ------: |
| Training   |  8,322 |     261 |
| Validation |  1,783 |      56 |
| Test       |  1,783 |      56 |

### Image Preprocessing

Each image was:

1. Converted to RGB.
2. Resized to **112 × 112 pixels**.
3. Converted into a numerical array.
4. Normalized by dividing pixel values by `255.0`.

This preprocessing pipeline was maintained during inference and deployment.

---

## ⚙️ 3. Methodology

### 3.1 Model Development

During **Week 7**, three approaches were implemented and compared:

* CNN from Scratch
* CNN + Data Augmentation
* MobileNetV2 Transfer Learning

The CNN architecture used convolutional blocks followed by global average pooling and dense classification layers.

### CNN Architecture

```text
Input Image
    ↓
Conv2D — 32
    ↓
Batch Normalization
    ↓
Max Pooling
    ↓
Conv2D — 64
    ↓
Batch Normalization
    ↓
Max Pooling
    ↓
Conv2D — 128
    ↓
Batch Normalization
    ↓
Max Pooling
    ↓
Conv2D — 256
    ↓
Batch Normalization
    ↓
Max Pooling
    ↓
Global Average Pooling
    ↓
Dense — 256 + ReLU
    ↓
Dropout — 0.5
    ↓
Dense — 1 + Sigmoid
```

---

### 3.2 Data Augmentation

The CNN + Data Augmentation approach used transformations including:

* Random flips
* Random rotations
* Random zoom
* Random brightness adjustments

The purpose was to expose the model to varied training examples and address the overfitting observed during the baseline CNN experiment.

---

### 3.3 Transfer Learning

MobileNetV2 pretrained on **ImageNet** was also evaluated.

The convolutional base was kept frozen and a new classification head was added for the binary classification task.

The Week 7 notebook identified **fine-tuning** the pretrained layers as a possible next step.

---

### 3.4 Training Configuration

| Configuration     | Value                |
| ----------------- | -------------------- |
| Optimizer         | Adam                 |
| Learning Rate     | `0.001`              |
| Loss              | Binary Cross-Entropy |
| Metrics           | Accuracy, AUC        |
| Random Seed       | `42`                 |
| Early Stopping    | Enabled              |
| ReduceLROnPlateau | Enabled              |

---

## 🧪 4. Model Comparison

The three approaches were evaluated on the test set during Week 7.

| Model                  | Test Accuracy |   Test AUC |  Test Loss |
| ---------------------- | ------------: | ---------: | ---------: |
| CNN from Scratch       |        88.11% |     0.9514 |     0.2826 |
| **CNN + Augmentation** |    **88.95%** | **0.9579** | **0.2632** |
| MobileNetV2 (frozen)   |        86.47% |     0.9383 |     0.3165 |

### 🏆 Selected Model

The **CNN + Data Augmentation** configuration was selected for the subsequent deployment work because it achieved the highest recorded **Test Accuracy** and **Test AUC** among the evaluated approaches.

---

## 📈 5. Key Findings

### CNN from Scratch

The training curves showed signs of overfitting after approximately **Epoch 8**, where training accuracy continued to increase while validation performance plateaued.

### CNN + Data Augmentation

The augmentation approach achieved the strongest recorded test performance:

```text
Test Accuracy → 88.95%
Test AUC      → 0.9579
Test Loss     → 0.2632
```

### MobileNetV2

The frozen MobileNetV2 configuration achieved lower test performance than the two CNN approaches in this experiment.

Fine-tuning the pretrained layers was identified as a possible future direction.

---

## 🔄 6. Sprint 4 — Model Retraining & Serialization

During **Week 9 Sprint 4**, the selected CNN-based approach was retrained for deployment preparation.

### Retraining Results

| Metric                   |     Result |
| ------------------------ | ---------: |
| Best Validation Accuracy | **89.39%** |
| Best Validation AUC      | **0.9597** |

The trained model was serialized using the Keras format:

```text
melanoma_cnn.keras
```

### Serialized Model Verification

After saving the model, the serialized artifact was loaded again and tested.

| Verification           | Result    |
| ---------------------- | --------- |
| True Class             | Malignant |
| Predicted Class        | Malignant |
| Prediction Probability | 0.5844    |
| Result                 | Correct ✓ |

---

## 🚀 7. Deployment Pipeline

Week 9 Sprint 4 extended the trained model into a complete serving pipeline.

```text
Selected CNN Model
        ↓
Retraining
        ↓
Serialize as .keras
        ↓
FastAPI Prediction Service
        ↓
Streamlit Application
        ↓
Streamlit Community Cloud
        ↓
Public Application
        ↓
Live Testing
        ↓
Local vs Live Verification
```

---

## 🔌 8. FastAPI

A FastAPI service was implemented to expose the model through a REST API.

### Main Features

* Root endpoint
* `/predict` endpoint
* Image upload handling
* JPEG / PNG validation
* RGB conversion
* Image resizing
* Pixel normalization
* Model inference
* Prediction and confidence output

The model is loaded once when the application starts.

---

## 🖥️ 9. Streamlit Application

A Streamlit application was developed as an interactive interface for the model.

Users can:

1. Upload an image.
2. Preview the uploaded image.
3. Run model inference.
4. View the predicted class.
5. View prediction confidence.
6. View Benign and Malignant probabilities.

The model is loaded using Streamlit resource caching.

---

## ☁️ 10. Public Deployment

The Streamlit application was deployed using **Streamlit Community Cloud**.

### 🔗 Live Application

**[Open the Live Streamlit Application](https://binxaimlinternship-ahm9zn2cc7ebk8gzw7fzhh.streamlit.app/)**

### Deployment Configuration

| Component       | Configuration             |
| --------------- | ------------------------- |
| Framework       | Streamlit                 |
| Model Framework | TensorFlow / Keras        |
| Model Format    | `.keras`                  |
| Input Type      | JPG / JPEG / PNG          |
| Input Size      | 112 × 112 × 3             |
| Preprocessing   | RGB + Resize + `/255.0`   |
| Output          | Benign / Malignant        |
| Threshold       | 0.5                       |
| Hosting         | Streamlit Community Cloud |

---

## 📦 11. Deployment Dependencies

The deployment environment uses a focused `requirements.txt`:

```text
streamlit==1.63.0
tensorflow==2.21.0
numpy==2.4.6
Pillow==12.3.0
```

Keeping deployment dependencies focused helps avoid unnecessary packages during cloud installation.

---

## 🧪 12. Live Deployment Testing

The deployed application was tested using the same three images used during local verification.

| Test Image | Prediction | Confidence | Local vs Live |
| ---------- | ---------- | ---------: | ------------- |
| `3.jpg`    | Benign     |     61.05% | Match ✓       |
| `22.jpg`   | Benign     |     91.12% | Match ✓       |
| `64.jpg`   | Malignant  |     99.91% | Match ✓       |

### Verification Result

> **3/3 test cases matched exactly between the local and deployed applications.**

This verifies consistency for the tested inputs between the local and deployed inference pipelines.

---

## 🔁 13. Reproducibility

Several practices were used to improve reproducibility:

| Practice                | Implementation |
| ----------------------- | -------------- |
| Fixed Random Seed       | `42`           |
| Image Size              | `112 × 112`    |
| Normalization           | `/255.0`       |
| Model Artifact          | `.keras`       |
| Training Configuration  | Documented     |
| Dependencies            | Versioned      |
| Inference Preprocessing | Consistent     |

The training and deployment environments use documented dependency versions appropriate to their respective stages.

---

## ⚠️ 14. Limitations

### Dataset Limitations

The reported performance is based on the available dataset and evaluation split. Performance on other datasets or real-world images may differ.

### Image Resolution

Images were resized to **112 × 112 pixels**, which reduces computational requirements but may remove fine-grained visual information.

### Generalization

The reported test metrics describe performance on the evaluated test set and should not be interpreted as a guarantee of performance on unseen real-world populations.

### Clinical Use

The system has not been clinically validated and should not be used as a diagnostic tool.

---

## 🔮 15. Future Work

Potential future improvements include:

* Fine-tuning MobileNetV2 layers.
* Evaluating additional CNN architectures.
* Performing more extensive hyperparameter tuning.
* Experimenting with higher image resolutions.
* Evaluating the model on external datasets.
* Adding comprehensive experiment tracking.
* Expanding automated API and application testing.
* Improving deployment monitoring and logging.

---

## 🎯 16. Conclusion

This project demonstrates an end-to-end deep learning workflow for binary melanoma image classification.

The development journey progressed from CNN experimentation and model comparison in **Week 7**, where CNN + Data Augmentation achieved the strongest recorded test performance, to deployment engineering in **Week 9 Sprint 4**.

The final pipeline includes:

```text
Data
  ↓
Preprocessing
  ↓
CNN Experimentation
  ↓
Model Comparison
  ↓
Model Selection
  ↓
Retraining
  ↓
Serialization
  ↓
FastAPI
  ↓
Streamlit
  ↓
Public Deployment
```

The project combines **deep learning experimentation, model evaluation, serving, deployment, and reproducibility practices** into one complete machine learning workflow.

---

<div align="center">

### 🌸 From Model Development → to Deployment → to a Complete ML System

**BinX Tech · AI & ML Internship · 2026**

</div>
```
