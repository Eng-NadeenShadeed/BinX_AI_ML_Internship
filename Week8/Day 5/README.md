<div align="center">

<h1>🔍 Week 8 — Day 5</h1>

<h2>SHAP Explainability & Sprint Review</h2>

<p>

<b>Investigating classification difficulty, explaining model decisions with SHAP, retraining on a reduced six-class task, and completing the Week 8 Sprint Review.</b>

</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Day%205-DB2777?style=for-the-badge&labelColor=FCE7F3">

<img src="https://img.shields.io/badge/Explainability-SHAP-EC4899?style=for-the-badge&labelColor=FFF1F2">

<img src="https://img.shields.io/badge/NLP-TF--IDF-A855F7?style=for-the-badge&labelColor=FAE8FF">

<img src="https://img.shields.io/badge/Sprint%20Review-Week%208-DB2777?style=for-the-badge&labelColor=FCE7F3">

</div>

---

## 🧠 Overview

<div style="
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

Day 5 investigated the root causes of the classification difficulty identified during Day 4.

The work focused on four main areas:

* Investigating **data quality and class imbalance**
* Retraining the TF-IDF + Logistic Regression model on a reduced **Top 6** task
* Applying **SHAP explainability** to understand model decisions
* Completing the **Week 8 Sprint Review and Retrospective**

The goal was not only to measure model performance, but also to understand **why the models struggled** and **what could be improved next**.

</div>

---

## 📁 Files

| File                            | Description                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `day5_shap_sprint_review.ipynb` | Full notebook containing data investigation, Top 6 retraining, SHAP explainability, sprint review, and retrospective |

---

## 📚 Topics Covered

<div style="
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

### 1 — Data Quality Investigation

Day 5 started by investigating the reasons behind the limited classification performance observed on Day 4.

#### Class Imbalance

The dataset contained a large difference between the largest and smallest specialty:

| Specialty |   Samples |
| --------- | --------: |
| Surgery   | **1,088** |
| Urology   |   **156** |

Approximate imbalance ratio:

**7 : 1**

#### Vocabulary Overlap

Cosine similarity between several specialties exceeded **0.89**, indicating highly similar TF-IDF language profiles.

This means that some specialties use very similar medical terminology, making them difficult to distinguish using text features alone.

#### Text Length Variation

Transcriptions showed substantial differences in length across specialties.

Different document lengths can affect the amount and distribution of information available to the classifier.

#### Sample Scarcity

Four specialties contained fewer than **200 training samples**, limiting the amount of data available for learning their patterns.

---

### 2 — Top 6 Specialties

To investigate whether the hardest classes were limiting overall performance, the task was reduced from the original Top 10 specialties to a cleaner **Top 6** subset.

The retained specialties were:

**Surgery · Consult - History and Phy. · Orthopedic · Radiology · General Medicine · Cardiovascular / Pulmonary**

The TF-IDF + Logistic Regression model was then retrained on this reduced task.

---

</div>

---

## 📊 Top 10 vs Top 6

| Setting                 |   Accuracy |   Macro F1 |
| ----------------------- | ---------: | ---------: |
| Top 10 — Day 4 baseline |      40.4% |     38.19% |
| **Top 6 — Day 5**       | **53.05%** | **48.81%** |

### Improvement

| Metric   |                 Improvement |
| -------- | --------------------------: |
| Accuracy | **+12.6 percentage points** |
| Macro F1 | **+10.6 percentage points** |

The reduced task produced a substantial improvement in both Accuracy and Macro F1.

This supported the hypothesis that difficult classes, vocabulary overlap, and limited samples were contributing significantly to the Day 4 performance.

---

## ⚙️ TF-IDF + Logistic Regression

The Top 6 model used the following configuration:

| Parameter      | Value      |
| -------------- | ---------- |
| `max_features` | `20,000`   |
| `ngram_range`  | `(1,3)`    |
| `min_df`       | `3`        |
| `max_df`       | `0.70`     |
| `sublinear_tf` | `True`     |
| `C`            | `5.0`      |
| `solver`       | `saga`     |
| `class_weight` | `balanced` |

The `class_weight='balanced'` setting was retained to address the class imbalance during training.

---

## 🔍 SHAP Explainability

**SHAP — SHapley Additive exPlanations** was used to understand how individual TF-IDF features contributed to model predictions.

The Top 6 TF-IDF + Logistic Regression model was explained using:

```python id="shap1"
shap.LinearExplainer
```

### Two Levels of Explanation

| Explanation            | Purpose                                                      |
| ---------------------- | ------------------------------------------------------------ |
| **Global Explanation** | Understand which features are influential across predictions |
| **Local Explanation**  | Understand why the model made one specific prediction        |

---

## 🌍 Global Feature Importance

The top **15 features per specialty** were visualised using SHAP bar charts.

These features provide insight into the vocabulary that strongly influences the classifier's decisions.

### Examples of Influential Features

| Specialty                  | Influential Features                                |
| -------------------------- | --------------------------------------------------- |
| Cardiovascular / Pulmonary | `chest`, `artery`, `heart`, `coronary`, `pulmonary` |
| Orthopedic                 | `joint`, `fracture`, `shoulder`, `screw`            |

Several influential features were clinically meaningful and aligned with the corresponding medical specialties.

---

## 🔬 Local Explanation

A local SHAP explanation was generated for **one individual test prediction**.

This allows the model decision to be examined at the level of a single document rather than only looking at overall feature importance.

The explanation shows which words/features contributed to the prediction and helps answer:

> **Why did the model classify this particular transcription this way?**

---

## 🧩 SHAP Workflow

<div align="center">

```text id="shap2"
             Trained TF-IDF + LR Model
                       │
                       ▼
                 Test Samples
                       │
                       ▼
              SHAP LinearExplainer
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Global Analysis     Local Analysis
              │                 │
              ▼                 ▼
       Top Features        One Prediction
              │                 │
              └────────┬────────┘
                       ▼
             Model Interpretability
```

</div>

---

## 🧪 Hands-On Lab

### Objective

Investigate data quality issues, retrain the model on a cleaner subset, explain model decisions with SHAP, and complete the sprint review.

### Steps Completed

| Step | Task                                      | Status |
| ---- | ----------------------------------------- | :----: |
| 1    | Quantified class imbalance                |    ✅   |
| 2    | Investigated vocabulary overlap           |    ✅   |
| 3    | Analyzed text length variation            |    ✅   |
| 4    | Investigated sample scarcity              |    ✅   |
| 5    | Filtered dataset to Top 6 specialties     |    ✅   |
| 6    | Retrained TF-IDF + LR                     |    ✅   |
| 7    | Measured Top 6 improvement                |    ✅   |
| 8    | Computed SHAP values on 100 test samples  |    ✅   |
| 9    | Generated global feature-importance plots |    ✅   |
| 10   | Produced local explanation                |    ✅   |
| 11   | Completed Sprint Review                   |    ✅   |
| 12   | Completed Sprint Retrospective            |    ✅   |

---

## 📈 Performance Improvement

<div style="
    background: #fff7fa;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

### Accuracy

<div align="center">

**40.4% → 53.05%**

**+12.6 percentage points**

</div>

### Macro F1

<div align="center">

**38.19% → 48.81%**

**+10.6 percentage points**

</div>

</div>

---

## 🔎 Root Causes Identified

The Day 5 investigation identified several factors contributing to the classification difficulty:

| Factor                 | Observation                                                    |
| ---------------------- | -------------------------------------------------------------- |
| **Class Imbalance**    | Surgery had 1,088 samples vs 156 for Urology                   |
| **Vocabulary Overlap** | Several specialty pairs exceeded 0.89 cosine similarity        |
| **Text Length**        | Substantial variation existed between transcription lengths    |
| **Sample Scarcity**    | Four specialties had fewer than 200 training samples           |
| **Task Difficulty**    | Some specialties contained highly overlapping medical language |

These findings explain why simply increasing model complexity did not automatically solve the classification problem.

---

## 📝 Sprint Review

The complete Week 8 Sprint was reviewed across **Days 1–5**.

### Main Sprint Outcome

The sprint successfully progressed from medical text preprocessing and TF-IDF modeling to:

* Deep learning with LSTM
* Transformer-based modeling with DistilBERT
* Three-way model comparison
* Error analysis
* Data quality investigation
* SHAP explainability
* Model selection
* Sprint retrospective

### Final Model Direction

**TF-IDF + Logistic Regression** remained the production baseline because of its Macro F1 performance, efficiency, interpretability, and explicit class-imbalance handling.

**DistilBERT** remained a candidate for future improvement with weighted loss and additional data.

---

## 🔄 Sprint Retrospective

### What Went Well

* Built a complete NLP workflow from preprocessing to evaluation
* Compared traditional ML, recurrent deep learning, and transformers
* Performed systematic error analysis
* Used SHAP to make model decisions more interpretable
* Identified concrete data-related causes of classification difficulty

### What Was Challenging

* Strong class imbalance
* Similar vocabulary between medical specialties
* Limited samples for smaller classes
* Difficulty improving minority-class performance
* Higher computational requirements for transformer models

### What To Improve

* Use additional feature sources
* Increase training data for underrepresented specialties
* Apply stronger class-imbalance strategies
* Improve transformer training with weighted loss
* Investigate richer text representations

---

## 🚀 Next Steps

### 1 — Use the `description` Column

The `description` column is currently unused.

Applying TF-IDF to this column and combining it with `transcription` features could provide additional information for distinguishing specialties.

### 2 — Use the `keywords` Column

The `keywords` column can be incorporated as a third feature source to enrich the classification input.

### 3 — Weighted DistilBERT

Retrain DistilBERT on the Top 6 task using an explicitly weighted `CrossEntropyLoss` to address class imbalance.

### 4 — Collect More Data

Collect additional samples for **Gastroenterology** and **Urology** before reintroducing these specialties into the classification task.

---

## 🏆 What We Achieved

* Investigated the root causes behind Day 4 classification difficulty
* Quantified class imbalance and vocabulary overlap
* Analyzed transcription length variation
* Identified sample scarcity
* Reduced the task from Top 10 to Top 6 specialties
* Improved Accuracy from **40.4% to 53.05%**
* Improved Macro F1 from **38.19% to 48.81%**
* Applied SHAP `LinearExplainer`
* Generated global feature-importance visualizations
* Produced a local prediction explanation
* Completed the Week 8 Sprint Review
* Completed the Sprint Retrospective
* Defined concrete next steps for future model improvement

---

## 💡 Key Takeaways

| Concept                | Takeaway                                                                                  |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| **Data Quality**       | Model performance depends strongly on the quality and structure of the training data      |
| **Class Imbalance**    | Minority classes can significantly affect Macro F1 and overall learning                   |
| **Vocabulary Overlap** | Similar medical terminology makes specialty classification harder                         |
| **Reduced Tasks**      | Removing highly difficult classes can reveal how much task complexity affects performance |
| **SHAP**               | Explainability helps connect model predictions to meaningful input features               |
| **Global Explanation** | Shows which features influence the model across many samples                              |
| **Local Explanation**  | Shows why a specific prediction was made                                                  |
| **Model Selection**    | Performance should be considered together with efficiency and interpretability            |
| **Future Work**        | More data, richer features, and weighted transformer training can improve the system      |

---

## ➡️ Next

**Week 9 — Deployment & MLOps**

Moving from model development and explainability toward **model serialization, API serving, interactive deployment, and production-oriented MLOps practices**.

---

<div align="center">

<h3>🌸 Week 8 — Sprint 3</h3>

<p>

<b>From Medical Text Classification to Explainable AI</b>

</p>

</div>
