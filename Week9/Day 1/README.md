# 🌸 Week 9 — Day 1

## Sprint 4 Planning & Model Serialization

**Serializing the trained CNN model and preparing it for production deployment.**

![WEEK 9](https://img.shields.io/badge/WEEK%209-f8a5c2?style=flat-square) ![DAY 1](https://img.shields.io/badge/DAY%201-C44569?style=flat-square&logoColor=white) ![SERIALIZATION](https://img.shields.io/badge/SERIALIZATION-8B1E3F?style=flat-square&logoColor=white) ![MELANOMA](https://img.shields.io/badge/MELANOMA-C44569?style=flat-square&logoColor=white) ![KERAS](https://img.shields.io/badge/KERAS-f8a5c2?style=flat-square)

---

## 🧠 Overview

Day 1 of Week 9 opened Sprint 4 — the final deployment sprint of the Capstone project — with a complete model serialization pipeline built on the ISIC Melanoma dataset.

The goal was to retrain the winning CNN model, save it as a production-ready `.keras` file, verify it loads and predicts correctly, and freeze a clean `requirements.txt` for the deployment environment.

---

## 📁 Files

| File | Description |
|------|-------------|
| `day1_sprint_planning_serialization.ipynb` | Learning notebook — Sprint planning, MLOps concepts, serialization |
| `Hands_On_Lab.ipynb` | Hands-on lab — Full serialization pipeline with real results |
| `requirements.txt` | Pinned dependencies for deployment |

---

## 📚 Topics Covered

| Topic | Details |
|-------|---------|
| Sprint 4 Planning | Full backlog defined across 5 days |
| Model Serialization | Keras native `.keras` format |
| Training/Serving Skew | What it is and how to prevent it |
| MLOps Practices | Fixed seeds, pinned dependencies, model versioning |
| tf.data Pipeline | Fast GPU training pipeline |

---

## 📊 Hands-On Lab Results

| Metric | Value |
|--------|-------|
| Model | CNN + Data Augmentation |
| Dataset | ISIC Melanoma (Benign vs Malignant) |
| Best val_AUC | 0.9580 |
| Best val_Accuracy | 89.18% |
| Model size | 5.3 MB |
| Saved format | `.keras` |

---

## ➡️ Next — Day 2

Build a FastAPI `/predict` endpoint that loads `melanoma_cnn.keras` and returns predictions as JSON.