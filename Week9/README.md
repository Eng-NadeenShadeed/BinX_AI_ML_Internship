<div align="center">

# 🌸 Week 9 — Capstone Deployment & MLOps

### **Sprint 4 — From Model to Deployment**

![Week 9](https://img.shields.io/badge/Week%209-f8a5c2?style=flat-square)
![Sprint 4](https://img.shields.io/badge/Sprint%204-C44569?style=flat-square\&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-8B1E3F?style=flat-square\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-C44569?style=flat-square\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-f8a5c2?style=flat-square)
![MLOps](https://img.shields.io/badge/MLOps-8B1E3F?style=flat-square\&logoColor=white)

**From model experimentation → to model serving → to public deployment 🚀**

</div>

---

## 🧠 Overview

Week 9 is the final deployment sprint of the Capstone project.

The week focuses on transforming the selected deep learning model from an experimental notebook into a complete, reproducible, and publicly accessible machine learning application.

The deployment pipeline continues from the **CNN + Data Augmentation model selected during Week 7 — Day 2**.

The week progresses through:

* Sprint 4 planning
* Model retraining and serialization
* Reproducibility and MLOps practices
* FastAPI model serving
* Streamlit dashboard development
* Local prediction verification
* Public deployment
* Repository organization
* Technical documentation
* Definition of Done verification
* Sprint Review
* Full-project retrospective

The final result is a complete ML workflow that connects the trained model to both programmatic and user-facing interfaces.

---

## 📁 Repository Structure

```text
Week9/

├── Day 1/
│   ├── models/
│   │   ├── melanoma_cnn_lab.keras
│   │   └── melanoma_cnn.keras
│   ├── day1_sprint_planning_serialization.ipynb
│   ├── Hands_On_Lab.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── Day 2/
│   ├── app/
│   │   └── main.py
│   ├── day2_fastapi_serving.ipynb
│   ├── Hands_On_Lab.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── Day 3/
│   ├── app/
│   │   └── streamlit_app.py
│   ├── day3_streamlit_dashboard.ipynb
│   ├── Hands_On_Lab.ipynb
│   ├── README.md
│   ├── prediction_probabilities.png
│   └── screenshots/
│
├── Day 4/
│   ├── deployment/
│   │   ├── app.py
│   │   └── melanoma_cnn.keras
│   ├── day4_public_deployment.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── Day 5/
|   ├── day5_repository_polish_dod.ipynb
│   ├── README.md
│   └── Technical Write-Up
│
└── README.md
```

---

## 🎯 Sprint 4 Objectives

| Objective                     | Status |
| ----------------------------- | :----: |
| 📋 Sprint 4 Planning          |    ✅   |
| 💾 Model Serialization        |    ✅   |
| 🔁 Reproducibility            |    ✅   |
| ⚡ FastAPI Model Serving       |    ✅   |
| 🖥️ Streamlit Dashboard       |    ✅   |
| 🌐 Public Deployment          |    ✅   |
| 🧹 Repository Polish          |    ✅   |
| 📝 Technical Write-Up         |    ✅   |
| 📊 Definition of Done         |    ✅   |
| 🔍 Sprint Review              |    ✅   |
| 💭 Full-Project Retrospective |    ✅   |
| 🎤 Week 10 Preparation        |    ✅   |

---

## 🗂️ Project Context

The model used during Week 9 was **not developed from scratch during the deployment sprint**.

The selected model came from **Week 7 — Day 2**, where three deep learning approaches were compared for binary melanoma classification:

1. CNN from Scratch
2. CNN + Data Augmentation
3. MobileNetV2

The **CNN + Data Augmentation** approach was selected based on the documented Week 7 test results.

Week 9 then continued with this selected approach by retraining it and preparing it for deployment.

---

## 📊 Week 7 Model Selection

| Model                       | Test Accuracy |   Test AUC |  Test Loss |
| --------------------------- | ------------: | ---------: | ---------: |
| CNN from Scratch            |        88.11% |     0.9514 |     0.2826 |
| **CNN + Data Augmentation** |    **88.95%** | **0.9579** | **0.2632** |
| MobileNetV2 (frozen)        |        86.47% |     0.9383 |     0.3165 |

The **CNN + Data Augmentation** model was selected for the deployment pipeline.

---

## 🧬 Dataset

The project uses the **ISIC Melanoma dataset** for binary image classification.

| Property       | Value                 |
| -------------- | --------------------- |
| Total Images   | 11,888                |
| Benign         | 6,289                 |
| Malignant      | 5,601                 |
| Training Set   | 8,322                 |
| Validation Set | 1,783                 |
| Test Set       | 1,783                 |
| Input Type     | RGB Images            |
| Task           | Binary Classification |

### Dataset Classes

```text
Benign
   ↓
Class 0

Malignant
   ↓
Class 1
```

The project is an educational machine learning classification project and is **not intended for clinical diagnosis**.

---

## 🧠 Model Configuration

| Component                | Configuration           |
| ------------------------ | ----------------------- |
| Model                    | CNN + Data Augmentation |
| Input Size               | 112 × 112 × 3           |
| Output                   | Sigmoid                 |
| Classes                  | Benign / Malignant      |
| Classification Threshold | 0.5                     |
| Optimizer                | Adam                    |
| Learning Rate            | 0.001                   |
| Loss                     | Binary Cross-Entropy    |
| Metrics                  | Accuracy, AUC           |
| Random Seed              | 42                      |
| Model Format             | `.keras`                |

### CNN Architecture

```text
Input Image
    ↓
Conv2D (32)
    ↓
Batch Normalization
    ↓
MaxPooling
    ↓
Conv2D (64)
    ↓
Batch Normalization
    ↓
MaxPooling
    ↓
Conv2D (128)
    ↓
Batch Normalization
    ↓
MaxPooling
    ↓
Conv2D (256)
    ↓
Batch Normalization
    ↓
MaxPooling
    ↓
Global Average Pooling
    ↓
Dense (256, ReLU)
    ↓
Dropout (0.5)
    ↓
Dense (1, Sigmoid)
    ↓
Prediction
```

---

# 📚 Daily Progress

## 🌸 Day 1 — Sprint Planning & Model Serialization

### 🧠 Focus

Serializing the trained CNN model and preparing it for production deployment.

### Topics Covered

* Sprint 4 planning
* Deployment backlog
* Model serialization
* Keras native `.keras` format
* Training/Serving Skew
* MLOps principles
* Fixed random seeds
* Pinned dependencies
* Model versioning
* `tf.data` pipeline

### Hands-On

* Retrained the selected CNN + Data Augmentation model
* Saved the trained model as `melanoma_cnn.keras`
* Verified that the serialized model could be loaded
* Tested prediction after loading
* Prepared pinned deployment dependencies

### Model Serialization Results

| Metric                   |                  Result |
| ------------------------ | ----------------------: |
| Model                    | CNN + Data Augmentation |
| Dataset                  |           ISIC Melanoma |
| Best Validation Accuracy |              **89.39%** |
| Best Validation AUC      |              **0.9597** |
| Model Size               |                  5.3 MB |
| Saved Format             |                `.keras` |

The serialized model was successfully loaded again and verified for inference.

---

## ⚡ Day 2 — Serving the Model with FastAPI

### 🧠 Focus

Connecting the serialized CNN model to a REST API for local prediction serving.

### Topics Covered

* FastAPI
* REST APIs
* Uvicorn
* Model serving
* Image uploads
* Input validation
* Image preprocessing
* JSON responses
* Swagger UI
* Inference pipeline

### API Endpoint

```text
POST /predict
```

The endpoint accepts an image upload and returns:

* Predicted class
* Confidence
* Filename

### 🔄 Prediction Pipeline

```text
Image Upload
     ↓
File Type Validation
     ↓
Convert to RGB
     ↓
Resize to 112 × 112
     ↓
Convert to NumPy Array
     ↓
Normalize /255.0
     ↓
Add Batch Dimension
     ↓
CNN Prediction
     ↓
Prediction Probability
     ↓
Class + Confidence
     ↓
JSON Response
```

### 🧪 API Testing Results

| Test | Input    | HTTP Status | Prediction | Confidence |
| ---- | -------- | :---------: | ---------- | ---------: |
| 1    | `3.jpg`  |    `200`    | Benign     |     61.05% |
| 2    | `22.jpg` |    `200`    | Benign     |     91.12% |
| 3    | `64.jpg` |    `200`    | Malignant  |     99.91% |
| 4    | PDF file |    `400`    | Rejected   |          — |

The API successfully processed valid JPEG images and rejected unsupported file types.

---

## 🖥️ Day 3 — Interactive Streamlit Dashboard

### 🧠 Focus

Building a user-facing Streamlit interface for the serialized ISIC Melanoma CNN.

### Topics Covered

* Streamlit basics
* Image upload
* Interactive widgets
* Model caching
* `@st.cache_resource`
* Inference preprocessing
* Prediction probabilities
* Confidence display
* Usability
* FastAPI vs Streamlit

### Dashboard Workflow

```text
Upload Image
      ↓
Display Uploaded Image
      ↓
Resize to 112 × 112
      ↓
Normalize Pixel Values
      ↓
CNN Inference
      ↓
Benign / Malignant Prediction
      ↓
Confidence
      ↓
Class Probabilities
```

### 🧪 Dashboard Testing

| Test Image | Prediction | Confidence |
| ---------- | ---------- | ---------: |
| `3.jpg`    | Benign     |     61.05% |
| `22.jpg`   | Benign     |     91.12% |
| `64.jpg`   | Malignant  |     99.91% |

All three Streamlit predictions matched the results previously obtained through FastAPI.

### FastAPI vs Streamlit

| Interface | Purpose                                |
| --------- | -------------------------------------- |
| FastAPI   | Programmatic access to CNN predictions |
| Streamlit | Interactive interface for human users  |

Both interfaces use the same serialized CNN model and consistent inference preprocessing.

---

## 🌐 Day 4 — Public Deployment

### 🧠 Focus

Deploying the Streamlit application publicly and verifying that the deployed model behaves consistently with the local version.

### Deployment Workflow

```text
Local Streamlit Application
          ↓
Deployment Configuration
          ↓
Model + Dependencies
          ↓
Public Cloud Deployment
          ↓
Live Application
          ↓
Prediction Verification
```

### Deployment Platform

The Streamlit application was deployed publicly using **Streamlit Community Cloud**.

### Deployment Configuration

```text
streamlit==1.63.0
tensorflow==2.21.0
numpy==2.4.6
Pillow==12.3.0
```

The serialized model was included with the deployment application.

### 🧪 Live Verification

The same three images used during local testing were submitted to the deployed application.

| Image    | Local Prediction   | Live Prediction    |  Result |
| -------- | ------------------ | ------------------ | :-----: |
| `3.jpg`  | Benign — 61.05%    | Benign — 61.05%    | ✓ Match |
| `22.jpg` | Benign — 91.12%    | Benign — 91.12%    | ✓ Match |
| `64.jpg` | Malignant — 99.91% | Malignant — 99.91% | ✓ Match |

### Verification Result

**3/3 tested inputs produced matching local and live predictions.**

This provided a final verification of consistent behavior for the selected test cases.

---

## 🧹 Day 5 — Repository Polish, Definition of Done & Sprint Review

### 🧠 Focus

Final Sprint 4 documentation, repository organization, reproducibility, and project review.

### Completed Work

* Polished repository structure
* Updated project documentation
* Completed the technical write-up
* Reviewed the Definition of Done
* Verified reproducibility requirements
* Reviewed Sprint 4 deliverables
* Completed the Sprint Review
* Completed the full-project retrospective
* Prepared the project for Week 10

---

## 📊 Definition of Done

| Requirement                                                | Status |
| ---------------------------------------------------------- | :----: |
| Full EDA → preprocessing → modelling → evaluation pipeline |    ✅   |
| Documented and reproducible performance benchmark          |    ✅   |
| Public deployed application                                |    ✅   |
| README and project documentation                           |    ✅   |
| Versioned dependencies                                     |    ✅   |
| Model artifact                                             |    ✅   |
| Experiments documented in notebooks                        |    ✅   |
| Reproducible notebook with fixed seed                      |    ✅   |
| Technical write-up                                         |    ✅   |
| Sprint 4 work reviewed                                     |    ✅   |

---

## 🔁 Reproducibility

The project documents the following configurations:

| Component     | Configuration        |
| ------------- | -------------------- |
| Random Seed   | `42`                 |
| Image Size    | `112 × 112`          |
| Normalization | `/255.0`             |
| Optimizer     | Adam                 |
| Learning Rate | `0.001`              |
| Loss          | Binary Cross-Entropy |
| Metrics       | Accuracy, AUC        |
| Model Format  | `.keras`             |
| Dependencies  | Versioned            |

The serialized model was loaded again after saving to verify that the saved artifact could be used for inference.

---

## 📈 Model Retraining Results

The selected **CNN + Data Augmentation** approach was retrained during Week 9 — Day 1 for deployment preparation.

| Metric                   |     Result |
| ------------------------ | ---------: |
| Best Validation Accuracy | **89.39%** |
| Best Validation AUC      | **0.9597** |

The final serialized model:

```text
melanoma_cnn.keras
```

Model size:

```text
5.3 MB
```

---

## 🚀 Complete Deployment Pipeline

```text
Week 7 — Day 2
CNN Experimentation & Model Comparison
          ↓
CNN + Data Augmentation
Selected Model
          ↓
Week 9 — Day 1
Model Retraining
          ↓
Model Serialization
          ↓
Week 9 — Day 2
FastAPI Model Serving
          ↓
Week 9 — Day 3
Streamlit Dashboard
          ↓
Week 9 — Day 4
Public Deployment
          ↓
Week 9 — Day 5
Repository Polish & Technical Documentation
          ↓
Sprint Review & Retrospective
```

---

## 🧪 Experiment Tracking

The model development experiments were documented throughout the learning notebooks.

The **Week 7 — Day 2** experiment compared:

* CNN from Scratch
* CNN + Data Augmentation
* MobileNetV2

The selected CNN + Data Augmentation model was then carried forward into Week 9.

This created a clear separation between:

```text
Model Development
       ↓
Model Selection
       ↓
Model Retraining
       ↓
Serialization
       ↓
Serving
       ↓
Deployment
```

---

## 💭 Full-Project Retrospective

### What Went Well

* Built the project progressively across multiple stages.
* Compared multiple deep learning approaches before selecting a model.
* Continued from the selected Week 7 model into deployment.
* Practiced both API-based and interactive model serving.
* Verified local and deployed predictions using test cases.
* Maintained consistent preprocessing throughout the deployment pipeline.
* Completed the project with a public application and technical documentation.

### What Was Challenging

* Transitioning from notebooks to deployable application code.
* Maintaining consistent preprocessing between training and inference.
* Managing deployment dependencies and environment differences.
* Organizing the repository while documenting the complete project.

### What We Learned

* A trained model is only one part of a complete ML system.
* Reproducibility is important when moving from experimentation to deployment.
* Model serving requires consistent input preprocessing.
* Documentation is an essential part of the technical workflow.
* Testing should continue after deployment.

### What We Would Improve

* Add more automated tests for the API and application.
* Expand experiment tracking.
* Evaluate additional architectures and fine-tuning strategies.
* Improve monitoring and deployment observability.

---

## 🎤 Week 10 Preparation

The final Week 9 work was completed with the final presentation in mind.

### Presentation Structure

```text
1. Problem
      ↓
2. Dataset
      ↓
3. Methodology
      ↓
4. Model Comparison
      ↓
5. Results
      ↓
6. Deployment
      ↓
7. Limitations
      ↓
8. Future Work
```

The presentation will focus on the technical decisions, experimental results, deployment workflow, and lessons learned throughout the project.

---

## ✅ Week 9 Progress Checklist

* [x] Day 1 — Sprint Planning & Model Serialization
* [x] Day 2 — FastAPI Model Serving
* [x] Day 3 — Streamlit Dashboard
* [x] Day 4 — Public Deployment
* [x] Day 5 — Repository Polish & Sprint Review

### 🌸 Sprint 4 Complete

---

## 🏁 Week 9 Outcome

Week 9 completed the transition from an experimentally developed deep learning model into a complete machine learning application.

The final workflow connects:

**Model Development → Serialization → API Serving → Interactive Dashboard → Public Deployment → Documentation**

The project now includes a serialized CNN model, FastAPI prediction service, Streamlit interface, public deployment, reproducibility configuration, technical documentation, and a completed Sprint 4 review.

<div align="center">

### 🌸 From Learning to Building

**A model is not the end of the journey — it is where the real building begins.**

**Learn → Experiment → Build → Deploy → Improve 🚀**

**BinX AI & ML Internship · Week 9 · 2026**

</div>
