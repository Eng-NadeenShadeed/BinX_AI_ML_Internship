<div align="center">

<h1>🌸 Week 8 — Day 2</h1>

<h2>Text Representation — TF-IDF & Word Embeddings</h2>

<p>
<b>Transforming cleaned medical transcriptions into numerical representations for machine learning.</b>
</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Day%202-DB2777?style=for-the-badge&labelColor=FCE7F3">
<img src="https://img.shields.io/badge/NLP-TF--IDF-EC4899?style=for-the-badge&labelColor=FFF1F2">
<img src="https://img.shields.io/badge/Embeddings-GloVe-A855F7?style=for-the-badge&labelColor=FAE8FF">
<img src="https://img.shields.io/badge/Text%20Classification-ML-DB2777?style=for-the-badge&labelColor=FCE7F3">

</div>

---

## 🧠 Overview

<table>
<tr>
<td bgcolor="#FFF9FC">

Day 2 continued Sprint 3's NLP track by converting the cleaned
MTSamples medical transcriptions from Day 1 into numerical
representations suitable for machine learning.

Two fundamentally different representation approaches were explored:

* **TF-IDF** — frequency-based and highly interpretable
* **GloVe** — embedding-based and semantically meaningful

The day concluded with a TF-IDF-based baseline classifier
for medical specialty classification.

</td>
</tr>
</table>

---

## 📁 Files

| File                           | Description                              |
| ------------------------------ | ---------------------------------------- |
| `day2_tfidf_embeddings.ipynb`  | Main notebook                            |
| `Data/mtsamples.csv`           | MTSamples Medical Transcriptions dataset |
| `Data/glove/glove.6B.100d.txt` | Pretrained GloVe vectors                 |

> **Note:** The GloVe pretrained file is used locally and is excluded from Git tracking because of GitHub's file-size limitation.

---

## 🏥 Dataset

### MTSamples Medical Transcriptions

The dataset used throughout the NLP pipeline is the **MTSamples Medical Transcriptions** dataset.

<table>
<tr>
<td bgcolor="#FFF9FC">

| Details                    |               Value |
| :------------------------- | ------------------: |
| **Usable Reports**         |               4,966 |
| **Medical Specialties**    |                  40 |
| **Classification Dataset** |  Top 10 specialties |
| **Classification Samples** |               3,631 |
| **Target**                 | `medical_specialty` |
| **Class Distribution**     |          Imbalanced |

</td>
</tr>
</table>

For classification, the dataset was filtered to the **10 most represented specialties** to provide sufficient samples per class and more reliable evaluation.

---

## 📚 Topics Covered

<table>
<tr>
<td bgcolor="#FFF9FC">

* Why raw text cannot enter a machine learning model directly
* Bag of Words — count-based text representation
* Limitations of Bag of Words
* TF-IDF — term frequency and inverse document frequency
* TF-IDF parameter selection
* Unigrams and bigrams
* Top TF-IDF terms per medical specialty
* Cosine similarity between document vectors
* Word embeddings and semantic representation
* Static vs contextual embeddings
* GloVe architecture and pretrained vectors
* GloVe word similarity
* Document representation using averaged embeddings
* Embedding vocabulary coverage
* TF-IDF vs GloVe comparison
* Representation selection for medical specialty classification
* TF-IDF baseline classification with class imbalance handling

</td>
</tr>
</table>

---

## 🔢 From Text to Numbers

<div align="center">

<table>
<tr>
<td align="center" bgcolor="#FFF9FC">

### Raw Medical Text

↓

### Text Representation

↓

<table>
<tr>
<td align="center" bgcolor="#FCE7F3">

**TF-IDF**

Frequency-based
Sparse representation
Highly interpretable

</td>

<td align="center" bgcolor="#FAE8FF">

**GloVe**

Embedding-based
Dense representation
Semantic relationships

</td>
</tr>
</table>

↓

### Numerical Vectors

</td>
</tr>
</table>

</div>

---

## 📊 TF-IDF Representation

### TF-IDF Matrix

The cleaned medical transcriptions were transformed into TF-IDF vectors using unigrams and bigrams.

<table>
<tr bgcolor="#FCE7F3">
<th>Property</th>
<th>Value</th>
</tr>

<tr>
<td><b>Shape</b></td>
<td>4,966 × 10,000</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Features</b></td>
<td>10,000</td>
</tr>

<tr>
<td><b>N-grams</b></td>
<td>Unigrams + Bigrams</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Sparsity</b></td>
<td><b>98.0%</b></td>
</tr>

</table>

### Why TF-IDF?

TF-IDF gives higher importance to terms that are:

1. Frequent within a document
2. Relatively rare across the entire corpus

This makes it particularly useful when different medical specialties
use distinctive vocabulary.

---

## 🔍 Top Terms per Specialty

The mean TF-IDF representation was used to identify characteristic
vocabulary across medical specialties.

<table>
<tr bgcolor="#FCE7F3">
<th>Specialty</th>
<th>Representative Terms</th>
</tr>

<tr>
<td><b>Surgery</b></td>
<td>procedure · patient · diagnosis · incision · remove</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Cardiovascular / Pulmonary</b></td>
<td>artery · coronary · chest · heart · patient</td>
</tr>

<tr>
<td><b>Neurology</b></td>
<td>brain · MRI · normal · exam · right</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Allergy / Immunology</b></td>
<td>allergy · asthma · allergic · food · allergies</td>
</tr>

</table>

This analysis showed that different specialties contain
distinctive medical vocabulary that can provide useful
classification signals.

---

## 📐 Cosine Similarity

Cosine similarity was used to compare TF-IDF document vectors.

<table>
<tr>
<td bgcolor="#FFF9FC">

Because TF-IDF produces high-dimensional sparse vectors,
cosine similarity measures how similar two documents are
based on the direction of their feature vectors rather than
their absolute magnitude.

Same-specialty documents generally showed greater similarity
than documents from unrelated specialties, although similarity
remained relatively low because individual medical reports
can describe very different clinical cases.

</td>
</tr>
</table>

---

## 🧠 Word Embeddings

Unlike TF-IDF, word embeddings represent words as **dense numerical vectors**.

<div align="center">

<table>
<tr>
<td align="center" width="50%" bgcolor="#FFF9FC">

### TF-IDF

Sparse vectors

↓

Word importance

↓

Strong interpretability

</td>

<td align="center" width="50%" bgcolor="#FCE7F3">

### GloVe

Dense vectors

↓

Semantic relationships

↓

Meaning-aware representation

</td>
</tr>
</table>

</div>

GloVe represents words in a continuous vector space where words
appearing in similar contexts tend to have similar vector representations.

---

## 🌐 GloVe — Hands-On

### Pretrained Embeddings

<table>
<tr bgcolor="#FCE7F3">
<th>Property</th>
<th>Value</th>
</tr>

<tr>
<td><b>Vectors Loaded</b></td>
<td>400,000</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Embedding Dimension</b></td>
<td>100</td>
</tr>

<tr>
<td><b>MTSamples Vocabulary Coverage</b></td>
<td><b>91.9%</b></td>
</tr>

</table>

### Word Similarity

Several medical and general-domain terms were tested to observe
semantic relationships in the embedding space.

| Word Pair              | Similarity |
| ---------------------- | ---------: |
| `cardiac` — `heart`    |     0.6697 |
| `physician` — `doctor` |     0.7673 |
| `medication` — `drug`  |     0.6574 |
| `surgery` — `incision` |     0.4292 |
| `allergy` — `asthma`   |     0.7826 |
| `brain` — `neurology`  |     0.3208 |

The results demonstrate how embeddings capture relationships
between words based on their usage in language.

---

## 📄 Document Embeddings

Individual GloVe word vectors were averaged to create a single
dense vector representing each medical transcription.

<div align="center">

**Word Vectors**

`word₁ → vector₁`

`word₂ → vector₂`

`word₃ → vector₃`

↓

**Mean Pooling**

↓

**100-dimensional Document Vector**

</div>

This approach provides a compact semantic representation,
but averaging removes word order and can lose important
specialty-specific information.

---

## ⚖️ TF-IDF vs GloVe

<table>
<tr bgcolor="#FCE7F3">
<th>Aspect</th>
<th>TF-IDF</th>
<th>GloVe</th>
</tr>

<tr>
<td><b>Representation</b></td>
<td>Sparse</td>
<td>Dense</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Dimensions</b></td>
<td>10,000 features</td>
<td>100 dimensions</td>
</tr>

<tr>
<td><b>Semantic Meaning</b></td>
<td>Limited</td>
<td>Strong</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Word Order</b></td>
<td>Ignored</td>
<td>Ignored when averaged</td>
</tr>

<tr>
<td><b>Interpretability</b></td>
<td><b>High</b></td>
<td>Lower</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Speed</b></td>
<td><b>Very Fast</b></td>
<td>Fast</td>
</tr>

<tr>
<td><b>Context Awareness</b></td>
<td>No</td>
<td>No — static embeddings</td>
</tr>

</table>

> **Important:** GloVe is a static embedding. It does not generate a different vector for a word based on its sentence context. Contextual representations such as BERT address this limitation.

---

## 🎯 Representation Decision

<div align="center">

<table>
<tr>
<td align="center" bgcolor="#FCE7F3">

### TF-IDF Selected

</td>
</tr>
</table>

</div>

For the current **MTSamples medical specialty classification task,
TF-IDF was selected as the baseline representation**.

The decision was based on:

* Distinctive vocabulary across medical specialties
* Strong interpretability
* Fast training and inference
* Effective representation for text classification
* Ability to inspect which terms contribute to classification

GloVe remains valuable for capturing semantic relationships,
but the averaged document representation loses word order and
specialty-specific details.

---

## 🤖 Baseline Classifier

A TF-IDF representation was combined with a multiclass classifier
to establish the first measurable classification baseline.

### Class Imbalance Handling

The dataset is highly imbalanced, with **Surgery** being the
largest specialty.

To reduce the influence of the dominant class,
`class_weight='balanced'` was used during training.

### Baseline Configuration

<table>
<tr bgcolor="#FCE7F3">
<th>Component</th>
<th>Configuration</th>
</tr>

<tr>
<td><b>Representation</b></td>
<td>TF-IDF</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Features</b></td>
<td>10,000</td>
</tr>

<tr>
<td><b>N-grams</b></td>
<td>(1, 2)</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Classifier</b></td>
<td>Logistic Regression</td>
</tr>

<tr>
<td><b>Class Weight</b></td>
<td><code>balanced</code></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Classes</b></td>
<td>10 medical specialties</td>
</tr>

</table>

---

## 📈 Key Results

<table>
<tr bgcolor="#FCE7F3">
<th>Metric</th>
<th>Score</th>
</tr>

<tr>
<td><b>Accuracy</b></td>
<td><b>40.4%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Macro F1</b></td>
<td><b>38.2%</b></td>
</tr>

<tr>
<td><b>Weighted F1</b></td>
<td><b>41.3%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Performance vs Random</b></td>
<td><b>4× better</b></td>
</tr>

</table>

The baseline establishes a measurable starting point for the
deep learning models that will be evaluated later in the sprint.

---

## 🎯 Key Decisions

<table>
<tr>

<td width="33%" align="center" bgcolor="#FFF9FC">

### TF-IDF

**Selected for Classification**

Distinctive specialty vocabulary,
fast computation, and strong
interpretability.

</td>

<td width="33%" align="center" bgcolor="#FCE7F3">

### Balanced Classes

**`class_weight='balanced'`**

Reduces the influence of the
dominant Surgery class and gives
minority classes greater importance.

</td>

<td width="33%" align="center" bgcolor="#FFF9FC">

### Top 10 Specialties

**Focused Classification Task**

Classes with very small sample
counts were excluded to provide
more reliable training and evaluation.

</td>

</tr>
</table>

---

## 🔬 Why Bigrams?

The TF-IDF configuration used:

```python
ngram_range=(1, 2)
```

This allows the model to learn both individual words and
two-word expressions.

<div align="center">

<table>
<tr bgcolor="#FFF9FC">
<td align="center">

`coronary`

+</td>

<td align="center">

`artery`

→

</td>

<td align="center">

<b>`coronary artery`</b>

</td>
</tr>

<tr>
<td align="center">

`chest`

+</td>

<td align="center">

`pain`

→

</td>

<td align="center">

<b>`chest pain`</b>

</td>
</tr>
</table>

</div>

Bigrams provide additional contextual information compared
with individual words alone.

---

## 🧪 Validation

<table>
<tr>
<td bgcolor="#FFF9FC">

The Day 2 pipeline was validated across the complete
representation workflow:

* ✓ TF-IDF matrix successfully generated
* ✓ Sparse representation inspected
* ✓ Specialty-specific terms analyzed
* ✓ Cosine similarity evaluated
* ✓ GloVe embeddings loaded successfully
* ✓ Medical vocabulary coverage measured
* ✓ Word-level semantic relationships explored
* ✓ Document embeddings generated
* ✓ TF-IDF and GloVe representations compared
* ✓ Baseline classifier trained
* ✓ Class imbalance addressed
* ✓ Baseline metrics documented

</td>
</tr>
</table>

---

## 🚀 What We Achieved

<div align="center">

|              Stage              | Status |
| :-----------------------------: | :----: |
| Text → Numerical Representation |    ✓   |
|           Bag of Words          |    ✓   |
|              TF-IDF             |    ✓   |
|     TF-IDF Feature Analysis     |    ✓   |
|        Cosine Similarity        |    ✓   |
|      Word Embeddings Theory     |    ✓   |
|          GloVe Loading          |    ✓   |
|         Word Similarity         |    ✓   |
|       Document Embeddings       |    ✓   |
|    TF-IDF vs GloVe Comparison   |    ✓   |
|     Representation Selection    |    ✓   |
|     Baseline Classification     |    ✓   |
|     Class Imbalance Handling    |    ✓   |
|       Baseline Evaluation       |    ✓   |

<br>

<table>
<tr>
<td align="center" bgcolor="#FCE7F3">

### Clean Text → Numerical Representation → Classification Baseline

</td>
</tr>
</table>

</div>

---

## 🔜 Next

<div align="center">

<img src="https://img.shields.io/badge/DAY%203-Computer%20Vision%20%2B%20OpenCV-DB2777?style=for-the-badge&labelColor=FCE7F3">

### Computer Vision Preprocessing with OpenCV

The next stage moves from text to images,
focusing on image standardization, augmentation,
and preprocessing for computer vision models.

**OpenCV → Image Preprocessing → Augmentation → Transfer Learning**

</div>

---

<div align="center">

## 🌸 Week 8 — Sprint 3

### NLP → Representation → Classification → Computer Vision

`─────────────────────────`

</div>
