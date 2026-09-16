<div align="center">

<h1>🧠 Week 8 — Day 4</h1>

<h2>End-to-End NLP Pipeline & Error Analysis</h2>

<p>

<b>Building an end-to-end medical text classification pipeline and comparing TF-IDF, LSTM, and DistilBERT using the same dataset and evaluation protocol.</b>

</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Day%204-DB2777?style=for-the-badge&labelColor=FCE7F3">

<img src="https://img.shields.io/badge/NLP-Medical%20Text-EC4899?style=for-the-badge&labelColor=FFF1F2">

<img src="https://img.shields.io/badge/LSTM-Deep%20Learning-A855F7?style=for-the-badge&labelColor=FAE8FF">

<img src="https://img.shields.io/badge/DistilBERT-Transformers-DB2777?style=for-the-badge&labelColor=FCE7F3">

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

Day 4 delivered the three-way model comparison committed to at the end of Day 2.

The same **MTSamples dataset**, the same **80/20 stratified train/test split**, and the same evaluation metrics were used across all three models to ensure a fair comparison.

The central question was:

> **Does increased model complexity produce a meaningful improvement over the TF-IDF baseline established on Day 2?**

</div>

---

## 📁 Files

| File                                 | Description                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `day4_pipeline_error_analysis.ipynb` | Full notebook containing preprocessing, three-way comparison, error analysis, and model selection |

---

## 📚 Topics Covered

<div style="
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

### 1 — End-to-End Preprocessing Pipeline

A unified cleaning function was applied identically during both training and prediction.

**Pipeline:**

`Lowercase → Strip → Tokenise → Lemmatise`

This prevents **training/serving skew**, where a model receives inputs during prediction that are formatted differently from the data used during training.

---

### 2 — TF-IDF + Logistic Regression

The Day 2 baseline was reproduced with refined parameters:

| Parameter      | Value      |
| -------------- | ---------- |
| `max_features` | `20,000`   |
| `ngram_range`  | `(1,3)`    |
| `min_df`       | `3`        |
| `max_df`       | `0.70`     |
| `sublinear_tf` | `True`     |
| `class_weight` | `balanced` |

`class_weight='balanced'` was used to give greater importance to the minority specialties during training.

---

### 3 — Bidirectional LSTM

A **Bidirectional LSTM** was trained from scratch using a learned embedding layer.

`compute_class_weight` was applied to the training process to address class imbalance.

The model was evaluated using the same test split as the TF-IDF and DistilBERT models.

---

### 4 — DistilBERT Fine-Tuning

The pretrained `distilbert-base-uncased` model was used for medical text classification.

For the main comparison:

* Pretrained transformer weights were frozen
* Only the classification head was trained
* Classification head: **598K parameters**

An additional experiment unfroze the last two transformer layers:

* **14.7M parameters**
* Training accuracy increased to **51.6%**
* The class-imbalance problem was not resolved

---

</div>

---

## 🔄 Fair Comparison Protocol

All three models followed the same evaluation setup:

<div align="center">

```text
                 MTSamples Dataset
                        │
                        ▼
              Top 10 Specialties
                        │
                        ▼
              Stratified 80/20 Split
                    seed = 42
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       TF-IDF          LSTM        DistilBERT
          │             │             │
          └─────────────┼─────────────┘
                        ▼
              Same Test Set
                        │
                        ▼
        Accuracy • Macro F1 • Time
```

</div>

Using the same split and evaluation protocol makes the comparison more meaningful because each model is tested on exactly the same samples.

---

## 📊 Three-Way Model Comparison

| Model           |  Accuracy |  Macro F1 | Train Time |          Inference |
| --------------- | --------: | --------: | ---------: | -----------------: |
| **TF-IDF + LR** |     40.4% | **38.2%** |  **12.2s** | **0.015ms/sample** |
| LSTM            |     37.4% |     14.8% |      46.5s |                  — |
| DistilBERT      | **48.4%** |     25.6% |     104.9s |       4.3ms/sample |

### Key observations

* **DistilBERT** achieved the highest Accuracy at **48.4%**
* **TF-IDF + Logistic Regression** achieved the highest Macro F1 at **38.2%**
* TF-IDF + LR had the shortest training time at **12.2 seconds**
* TF-IDF + LR had the fastest reported inference time at **0.015 ms/sample**
* LSTM achieved **37.4% Accuracy** but only **14.8% Macro F1**
* DistilBERT required significantly more training time than the other models

---

## 🔍 Error Analysis

Error analysis was used to understand **where and why the models failed**, rather than looking only at aggregate metrics.

### Shared Errors

**182 samples** were misclassified by all three models.

These represent cases that were difficult across different modeling approaches.

### Highest Shared Error Rates

| Specialty / Category          | Shared Error Rate |
| ----------------------------- | ----------------: |
| SOAP / Chart / Progress Notes |         **54.5%** |
| Gastroenterology              |         **53.3%** |

Confusion matrices also showed that the three models had **different failure patterns**, meaning that the models did not make exactly the same mistakes.

---

## ⚖️ Class Imbalance

The dataset contained substantial differences between specialty sizes.

<div align="center">

```text
Surgery      ████████████████████████████████████████  1,088
Urology      ██████                                      156
```

</div>

The largest class contained approximately **7×** as many samples as the smallest class.

This imbalance affected the models differently.

The key observation was that the TF-IDF baseline explicitly used:

```python
class_weight="balanced"
```

while the more complex architectures did not achieve the same balance in the final comparison.

---

## 🧩 Model Selection

<div style="
    background: #fff7fa;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

### Production Baseline

**TF-IDF + Logistic Regression** was selected as the production baseline because it achieved:

* Best **Macro F1**
* Fastest training time
* Fast inference
* Interpretable features
* Explicit class-imbalance handling

### Future Candidate

**DistilBERT** was identified as the candidate for future improvement, particularly with:

* Weighted loss
* More training data
* Better handling of class imbalance

</div>

---

## 🧪 Hands-On Lab

### Objective

Build an end-to-end NLP pipeline and compare:

**TF-IDF + LR → Bidirectional LSTM → DistilBERT**

using the same dataset and evaluation protocol.

### Steps Completed

| Step | Task                                             | Status |
| ---- | ------------------------------------------------ | :----: |
| 1    | Built unified preprocessing function             |    ✅   |
| 2    | Reproduced TF-IDF + LR baseline                  |    ✅   |
| 3    | Trained Bidirectional LSTM                       |    ✅   |
| 4    | Fine-tuned DistilBERT                            |    ✅   |
| 5    | Ran additional transformer unfreezing experiment |    ✅   |
| 6    | Created three-way comparison                     |    ✅   |
| 7    | Generated per-metric bar charts                  |    ✅   |
| 8    | Generated confusion matrices                     |    ✅   |
| 9    | Performed shared-error analysis                  |    ✅   |
| 10   | Documented model selection rationale             |    ✅   |

---

## 📦 Dataset

### MTSamples — Medical Transcription Samples

| Property             | Value                            |
| -------------------- | -------------------------------- |
| Dataset              | MTSamples                        |
| Task                 | Medical specialty classification |
| Selected specialties | Top 10                           |
| Total samples        | **3,631**                        |
| Training set         | **2,904**                        |
| Test set             | **727**                          |
| Split                | **80/20**                        |
| Sampling             | **Stratified**                   |
| Random seed          | **42**                           |

### Class Imbalance

| Specialty |   Samples |
| --------- | --------: |
| Surgery   | **1,088** |
| Urology   |   **156** |

Approximate imbalance ratio:

**7 : 1**

---

## 🧠 Key Finding

<div style="
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    border: 1px solid #f2d4de;
    line-height: 1.8;
">

### Class Imbalance Handling Matters

The main lesson from the three-way comparison was that **model complexity alone did not guarantee better classification performance**.

TF-IDF + Logistic Regression achieved the best **Macro F1**, despite being the simplest model.

One important factor was its explicit use of:

```python
class_weight="balanced"
```

This highlighted the importance of handling class imbalance alongside model architecture.

</div>

---

## 🧪 Validation

The pipeline was validated by checking that:

* All models used the same dataset
* The same stratified train/test split was used
* The same test set was used for comparison
* Preprocessing was unified between training and prediction
* Accuracy and Macro F1 were compared consistently
* Confusion matrices were generated for error analysis
* Training and inference efficiency were considered during model selection

---

## 🏆 What We Achieved

* Built a unified **end-to-end NLP preprocessing pipeline**
* Reproduced and improved the **TF-IDF baseline**
* Trained a **Bidirectional LSTM**
* Fine-tuned **DistilBERT**
* Performed an additional transformer-layer unfreezing experiment
* Compared three different modeling approaches fairly
* Analyzed shared and model-specific errors
* Investigated the impact of class imbalance
* Selected a practical production baseline
* Identified DistilBERT as a direction for future improvement

---

## 💡 Key Takeaways

| Concept                 | Takeaway                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------- |
| **End-to-End Pipeline** | Training and prediction should use the same preprocessing                              |
| **TF-IDF**              | Strong and efficient baseline for text classification                                  |
| **LSTM**                | Can model sequential text patterns but remains sensitive to data quality and imbalance |
| **DistilBERT**          | Provides stronger contextual representations but requires more computational resources |
| **Macro F1**            | Important when classes are imbalanced                                                  |
| **Class Weighting**     | Can significantly affect performance across minority classes                           |
| **Error Analysis**      | Reveals weaknesses hidden by aggregate metrics                                         |
| **Model Selection**     | Should consider performance, efficiency, interpretability, and data limitations        |

---

## ➡️ Next

**Day 5 — Advanced NLP & Transformers**

Moving from model comparison and error analysis toward deeper exploration of transformer-based NLP techniques and the next stage of the Sprint 3 pipeline.

---

<div align="center">

<h3>🌸 Week 8 — Sprint 3</h3>

<p>

<b>From Medical Text to Deep Learning & Transformers</b>

</p>

</div>
