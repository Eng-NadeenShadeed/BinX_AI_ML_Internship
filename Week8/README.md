<div align="center">

<h1>🧠 Week 8 — NLP & Computer Vision</h1>

<h2>Medical Text Classification & Chest X-Ray Analysis</h2>

<p>

<b>Building two parallel AI pipelines for medical text classification and computer vision, from preprocessing and representation learning to deep learning, explainability, and sprint review.</b>

</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Sprint%203-DB2777?style=for-the-badge&labelColor=FCE7F3">

<img src="https://img.shields.io/badge/NLP-Medical%20Text-EC4899?style=for-the-badge&labelColor=FFF1F2">

<img src="https://img.shields.io/badge/Computer%20Vision-OpenCV-A855F7?style=for-the-badge&labelColor=FAE8FF">

<img src="https://img.shields.io/badge/Explainability-SHAP-DB2777?style=for-the-badge&labelColor=FCE7F3">

</div>

---

## 🧠 Week Overview

<div style="
    background: white;
    border-radius: 12px;
    padding: 28px 32px;
    border: 1px solid #f2d4de;
    line-height: 1.9;
">

Week 8 focused on two parallel AI pipelines:

**NLP Pipeline** — medical text classification using the MTSamples dataset across Days 1, 2, 4, and 5.

**Computer Vision Pipeline** — pediatric chest X-ray binary classification using OpenCV, CNNs, and MobileNetV2 on Day 3.

The sprint progressed from preprocessing and feature representation to deep learning, transformer models, error analysis, explainability, and model selection.

The sprint concluded with a **three-way NLP model comparison, SHAP explainability, and a complete Sprint Review and Retrospective.**

</div>

---

## 📁 Structure

```text
Week8/
│
├── Day 1/   NLP Preprocessing Pipeline (MTSamples)
├── Day 2/   TF-IDF Representations & GloVe Embeddings
├── Day 3/   Computer Vision — Chest X-Ray
│            (OpenCV + CNN + MobileNetV2)
├── Day 4/   End-to-End Pipeline & Three-Way Model Comparison
├── Day 5/   SHAP Explainability & Sprint Review
│
└── README.md
```

---

## 🗺️ Sprint Roadmap

<div align="center">

```text
Day 1
NLP Preprocessing
      │
      ▼
Day 2
TF-IDF + GloVe
      │
      ├──────────────────────┐
      │                      │
      ▼                      ▼
Day 4                    Day 3
NLP Model Comparison     Computer Vision
      │                      │
      ▼                      ▼
Day 5                  CNN + MobileNetV2
SHAP + Sprint Review
      │
      └──────────────┬───────┘
                     ▼
              Sprint 3 Review
```

</div>

---

# 📝 NLP Track

## Dataset

**MTSamples — Medical Transcription Samples**

| Property             | Value                            |
| -------------------- | -------------------------------- |
| Task                 | Medical specialty classification |
| Selected specialties | Top 10                           |
| Total samples        | **3,631**                        |
| Classes              | **10**                           |
| Task type            | Multi-class classification       |

The goal was to classify clinical transcription text into its corresponding medical specialty.

---

## 📊 NLP Key Results

| Day       | Deliverable                | Result                                                    |
| --------- | -------------------------- | --------------------------------------------------------- |
| **Day 1** | NLP Preprocessing Pipeline | Vocabulary reduced from **70,898 → 32,183** unique tokens |
| **Day 2** | TF-IDF Baseline + GloVe    | **40.4% Accuracy · 38.2% Macro F1**                       |
| **Day 4** | Three-Way Comparison       | TF-IDF best Macro F1 · DistilBERT best Accuracy           |
| **Day 5** | Top 6 Retraining + SHAP    | **53.05% Accuracy · 48.81% Macro F1**                     |

---

## 🔄 NLP Pipeline

<div align="center">

```text
Medical Transcriptions
          │
          ▼
   Text Preprocessing
          │
          ▼
 Tokenisation + Cleaning
          │
          ▼
   Feature Representation
          │
     ┌────┴────┐
     ▼         ▼
   TF-IDF    GloVe
     │
     ▼
  ML Baseline
     │
     ▼
   LSTM + DistilBERT
     │
     ▼
 Model Comparison
     │
     ▼
 Error Analysis
     │
     ▼
   SHAP Explainability
```

</div>

---

## 🧪 Three-Way NLP Comparison

The same **80/20 stratified train/test split with `seed=42`** was used across the three models to ensure a fair comparison.

| Model           |  Accuracy |  Macro F1 | Train Time |          Inference |
| --------------- | --------: | --------: | ---------: | -----------------: |
| **TF-IDF + LR** |     40.4% | **38.2%** |  **12.2s** | **0.015ms/sample** |
| LSTM            |     37.4% |     14.8% |      46.5s |                  — |
| DistilBERT      | **48.4%** |     25.6% |     104.9s |       4.3ms/sample |

### Comparison Summary

* DistilBERT achieved the highest **Accuracy: 48.4%**
* TF-IDF + Logistic Regression achieved the highest **Macro F1: 38.2%**
* TF-IDF + LR had the shortest training time
* TF-IDF + LR also had the fastest reported inference time

---

## ⚠️ NLP Class Imbalance

A major challenge was class imbalance.

| Specialty |   Samples |
| --------- | --------: |
| Surgery   | **1,088** |
| Urology   |   **156** |

Approximate ratio:

**7 : 1**

Because of this imbalance, **Macro F1** was particularly important for evaluating how well the models handled all classes rather than allowing large classes to dominate the metric.

---

## 🔍 NLP Error Analysis

Day 4 investigated the reasons behind the classification difficulty.

### Main Findings

| Issue              | Finding                                                  |
| ------------------ | -------------------------------------------------------- |
| Class imbalance    | Surgery vs Urology approximately **7:1**                 |
| Vocabulary overlap | Several specialties exceeded **0.89 cosine similarity**  |
| Text length        | Substantial variation between transcriptions             |
| Sample scarcity    | Four specialties had fewer than **200 training samples** |
| Shared errors      | **182 samples** failed across all three models           |

The analysis showed that increasing model complexity alone did not resolve the underlying data difficulties.

---

## 🔬 SHAP Explainability

Day 5 introduced **SHAP — SHapley Additive exPlanations** to investigate model decisions.

`shap.LinearExplainer` was applied to the Top 6 TF-IDF + Logistic Regression model.

### Global Explanation

The top **15 features per specialty** were visualised to identify influential vocabulary.

Examples:

| Specialty                  | Influential Features                                |
| -------------------------- | --------------------------------------------------- |
| Cardiovascular / Pulmonary | `chest`, `artery`, `heart`, `coronary`, `pulmonary` |
| Orthopedic                 | `joint`, `fracture`, `shoulder`, `screw`            |

### Local Explanation

A local SHAP explanation was also generated for an individual test prediction to understand which features contributed to that specific decision.

---

## 📈 Top 6 Retraining

Day 5 reduced the classification task to six specialties:

**Surgery · Consult - History and Phy. · Orthopedic · Radiology · General Medicine · Cardiovascular / Pulmonary**

| Setting           |   Accuracy |   Macro F1 |
| ----------------- | ---------: | ---------: |
| Top 10 — Day 4    |      40.4% |     38.19% |
| **Top 6 — Day 5** | **53.05%** | **48.81%** |

### Improvement

**Accuracy:** +12.6 percentage points

**Macro F1:** +10.6 percentage points

This demonstrated how task difficulty and class composition strongly affected the classification results.

---

# 🩻 Computer Vision Track

## Dataset

**Chest X-Ray Pneumonia Dataset — Kaggle**

| Property     | Value                      |
| ------------ | -------------------------- |
| Total images | **5,856**                  |
| Task         | Binary classification      |
| Classes      | **NORMAL / PNEUMONIA**     |
| Population   | Pediatric chest X-rays     |
| Main tools   | OpenCV + CNN + MobileNetV2 |

The goal was to classify pediatric chest X-ray images into **Normal** or **Pneumonia**.

---

## 🖼️ Computer Vision Pipeline

<div align="center">

```text
Chest X-Ray Dataset
        │
        ▼
   Dataset Audit
        │
        ▼
   OpenCV Loading
        │
        ▼
 Image Preprocessing
        │
        ▼
   Data Augmentation
        │
        ├───────────────┐
        ▼               ▼
 CNN From Scratch   MobileNetV2
                        │
                  Transfer Learning
        │               │
        └───────┬───────┘
                ▼
        Model Evaluation
                │
                ▼
        Error Analysis
```

</div>

---

## 📊 Computer Vision Results

| Model            | Test Accuracy | Pneumonia Recall |        AUC |
| ---------------- | ------------: | ---------------: | ---------: |
| CNN From Scratch |    **83.01%** |       **98.97%** | **0.9401** |
| MobileNetV2      |    **83.49%** |       **99.23%** | **0.9690** |

Both models achieved more than **98% Pneumonia recall** on the test set.

MobileNetV2 achieved slightly higher test Accuracy, Recall, and AUC than the CNN trained from scratch.

---

## ⚠️ Validation-to-Test Gap

A significant validation-to-test performance gap was identified during the Computer Vision pipeline.

| Metric   |  Validation |        Test |
| -------- | ----------: | ----------: |
| Accuracy | ≈ **97.4%** | ≈ **83.5%** |

This gap was documented as an important direction for further investigation because strong validation performance did not translate directly to the unseen test set.

---

# 🔗 Connecting Both Tracks

Although NLP and Computer Vision used different data types and architectures, both pipelines followed the same overall machine learning workflow:

<div align="center">

```text
             Data
              │
              ▼
        Preprocessing
              │
              ▼
       Representation
              │
              ▼
       Model Training
              │
              ▼
         Evaluation
              │
              ▼
       Error Analysis
              │
              ▼
     Model Interpretation
              │
              ▼
       Next Improvements
```

</div>

The main difference was the type of representation:

| Pipeline | Input        | Representation                                    | Models                 |
| -------- | ------------ | ------------------------------------------------- | ---------------------- |
| **NLP**  | Medical text | TF-IDF / Embeddings / Transformer representations | LR / LSTM / DistilBERT |
| **CV**   | X-ray images | Pixel features / Learned visual features          | CNN / MobileNetV2      |

---

## 🎯 Key Finding

<div style="
    background: #fff7fa;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.9;
">

### NLP

Class imbalance and data characteristics had a major effect on model performance.

TF-IDF + Logistic Regression achieved the highest **Macro F1** in the three-way comparison while using explicit:

```python
class_weight="balanced"
```

### Computer Vision

Both CNN approaches achieved high Pneumonia recall, while the validation-to-test gap highlighted the importance of checking generalization on untouched test data.

</div>

---

## 🧠 What We Learned

| Area                  | Key Learning                                                                  |
| --------------------- | ----------------------------------------------------------------------------- |
| **NLP Preprocessing** | Consistent preprocessing is essential for reliable text classification        |
| **TF-IDF**            | A strong and efficient baseline for medical text                              |
| **Embeddings**        | Learned representations can capture relationships beyond sparse features      |
| **LSTM**              | Sequential models provide a deep-learning alternative for text                |
| **Transformers**      | DistilBERT provides contextual representations with higher computational cost |
| **Class Imbalance**   | Macro F1 is important when class distributions are uneven                     |
| **Computer Vision**   | CNNs can learn spatial patterns directly from medical images                  |
| **Transfer Learning** | MobileNetV2 provides a pretrained feature representation                      |
| **Error Analysis**    | Aggregate metrics alone do not explain model failures                         |
| **SHAP**              | Explainability connects predictions to influential input features             |
| **Generalization**    | Validation performance should always be checked against an untouched test set |

---

## 🚀 Identified Next Steps

### NLP

1. Apply TF-IDF to the currently unused `description` column
2. Combine `description` features with `transcription`
3. Incorporate the `keywords` column as an additional feature source
4. Retrain DistilBERT with weighted `CrossEntropyLoss` on Top 6 specialties
5. Collect more training samples for Gastroenterology and Urology

### Computer Vision

6. Investigate the validation-to-test performance gap
7. Further evaluate generalization and dataset characteristics

---

## ✅ Progress Checklist

* [x] Week 1 — Python Foundations + NumPy + Pandas + Matplotlib
* [x] Week 2 — Math Foundations + Statistics + Probability + Linear Algebra + EDA
* [x] Week 3 — Supervised Learning Basics
* [x] Week 4 — Advanced Supervised Learning
* [x] Week 5 — Unsupervised Learning — K-Means + DBSCAN + Hierarchical
* [x] Week 6 — Deep Learning Foundations
* [x] Week 7 — CNN + RNN/LSTM + Transformers — DistilBERT
* [x] **Week 8 — NLP Pipeline + CV Pipeline + Model Comparison + SHAP**

---

## 🏆 What We Achieved

<div style="
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.9;
">

### NLP

* Built a complete medical text preprocessing pipeline
* Created TF-IDF representations
* Explored GloVe embeddings
* Trained a Bidirectional LSTM
* Fine-tuned DistilBERT
* Completed a three-way model comparison
* Performed systematic error analysis
* Retrained on a reduced Top 6 task
* Applied SHAP explainability
* Completed model selection and sprint review

### Computer Vision

* Audited a pediatric chest X-ray dataset
* Applied OpenCV preprocessing
* Built a CNN from scratch
* Applied MobileNetV2 transfer learning
* Evaluated both models using Accuracy, Recall, and AUC
* Investigated validation-to-test generalization

### Sprint

* Connected two different AI modalities within one sprint
* Compared traditional ML, deep learning, and transformer approaches
* Identified concrete data and modeling limitations
* Defined clear next steps for future improvement

</div>

---

## 💡 Key Takeaways

> **Better models do not automatically solve difficult data.**

Week 8 demonstrated the importance of combining:

**Data Understanding → Preprocessing → Representation → Modeling → Evaluation → Error Analysis → Explainability**

The sprint also showed that model selection should consider not only predictive performance, but also **class imbalance, efficiency, interpretability, computational cost, and generalization**.

---

## ➡️ Next

**Week 9 — Deployment & MLOps**

Moving from model development and analysis toward:

**Model Serialization → FastAPI → Streamlit → Public Deployment → MLOps**

---

<div align="center">

<h3>🌸 Week 8 — Sprint 3</h3>

<p>

<b>From Medical Text & Images to Explainable AI</b>

</p>

</div>
