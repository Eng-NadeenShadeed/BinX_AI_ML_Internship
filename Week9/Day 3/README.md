<div align="center">

# 🌸 Week 9 — Day 3

## Interactive Streamlit Dashboard

**Building a user-facing Streamlit interface for the serialized ISIC Melanoma CNN.**

![WEEK 9](https://img.shields.io/badge/WEEK%209-f8a5c2?style=flat-square) ![DAY 3](https://img.shields.io/badge/DAY%203-C44569?style=flat-square\&logoColor=white) ![STREAMLIT](https://img.shields.io/badge/STREAMLIT-8B1E3F?style=flat-square\&logoColor=white) ![CNN](https://img.shields.io/badge/CNN-C44569?style=flat-square\&logoColor=white) ![DEPLOYMENT](https://img.shields.io/badge/DEPLOYMENT-f8a5c2?style=flat-square)

</div>

---

## 🧠 Overview

Day 3 focused on transforming the serialized ISIC Melanoma CNN into an interactive Streamlit dashboard designed for non-technical users.

The goal was to create a clean and focused interface where a user can upload a skin lesion image, run the trained CNN, and view the predicted class, confidence score, and class probabilities.

The dashboard uses the same serialized `.keras` model and inference preprocessing pipeline established during Day 1.

---

## 📁 Files

| File                             | Description                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| `day3_streamlit_dashboard.ipynb` | Learning notebook — Streamlit concepts, widgets, caching, usability, and deployment architecture |
| `Hands_On_Lab.ipynb`             | Hands-on lab — Full Streamlit dashboard implementation and testing                               |
| `app/streamlit_app.py`           | Streamlit application for interactive CNN prediction                                             |
| `README.md`                      | Day 3 documentation                                                                              |

---

## 📚 Topics Covered

| Topic                   | Details                                                       |
| ----------------------- | ------------------------------------------------------------- |
| Why Streamlit           | Building a user-facing interface for ML models                |
| Streamlit Basics        | Widgets and top-to-bottom script execution                    |
| Image Upload            | Using `st.file_uploader()` for image input                    |
| Model Caching           | Using `@st.cache_resource` to avoid unnecessary model reloads |
| Inference Preprocessing | RGB conversion, resizing, normalization, and batch dimension  |
| Prediction              | Sigmoid probability and 0.5 classification threshold          |
| Visualization           | Displaying Benign and Malignant probabilities                 |
| FastAPI vs Streamlit    | Programmatic API vs human-facing interface                    |
| Usability               | Designing a focused first-time user workflow                  |

---

## 🖥️ Dashboard Workflow

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
Confidence + Class Probabilities
```

---

## 📊 Hands-On Lab Results

| Test Image | Prediction | Confidence |
| ---------- | ---------- | ---------- |
| `3.jpg`    | Benign     | 61.05%     |
| `22.jpg`   | Benign     | 91.12%     |
| `64.jpg`   | Malignant  | 99.91%     |

All three Streamlit predictions matched the results previously obtained through the FastAPI service.

---

## ⚙️ Model Configuration

| Component                | Configuration           |
| ------------------------ | ----------------------- |
| Model                    | CNN + Data Augmentation |
| Input Size               | 112 × 112 × 3           |
| Output                   | Sigmoid                 |
| Target Classes           | Benign / Malignant      |
| Classification Threshold | 0.5                     |
| Model Format             | `.keras`                |
| Model Source             | Week 9 — Day 1          |

---

## 🚀 Running the Dashboard

From the VS Code terminal:

```bash
cd "Week9\Day 3\app"
streamlit run streamlit_app.py
```

The application runs locally at:

```text
http://localhost:8501
```

---

## 🔗 FastAPI vs Streamlit

| Interface | Purpose                                |
| --------- | -------------------------------------- |
| FastAPI   | Programmatic access to CNN predictions |
| Streamlit | Interactive interface for human users  |

Both interfaces use the same serialized CNN model and consistent inference preprocessing.

---

## ➡️ Next — Day 4

Deploy the Streamlit application publicly using **Hugging Face Spaces** and prepare the project for public access.
