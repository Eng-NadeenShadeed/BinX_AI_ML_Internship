<div align="center">

<h1>🌸 Week 8 — Day 1</h1>

<h2>Sprint 3 Planning & NLP Preprocessing</h2>

<p>
<b>Transforming raw medical transcriptions into clean and consistent text representations.</b>
</p>

<br>

<img src="https://img.shields.io/badge/Week%208-Day%201-DB2777?style=for-the-badge&labelColor=FCE7F3">
<img src="https://img.shields.io/badge/NLP-Preprocessing-EC4899?style=for-the-badge&labelColor=FFF1F2">
<img src="https://img.shields.io/badge/MTSamples-Medical%20Data-A855F7?style=for-the-badge&labelColor=FAE8FF">

</div>

---

## 🧠 Overview

<table>
<tr>
<td bgcolor="#FFF9FC">

Day 1 of Week 8 opened Sprint 3's NLP track with a complete
text preprocessing pipeline built from scratch on real medical
transcription data.

The goal was to transform raw medical transcriptions into a cleaner
and more consistent textual representation before numerical feature
extraction and classification.

</td>
</tr>
</table>

---

## 📁 Files

| File                                           | Description                              |
| ---------------------------------------------- | ---------------------------------------- |
| `day1_sprint_planning_nlp_preprocessing.ipynb` | Main notebook                            |
| `Data/mtsamples.csv`                           | MTSamples Medical Transcriptions dataset |

---

## 🏥 Dataset

### MTSamples Medical Transcriptions

The dataset used in this notebook is the **MTSamples Medical Transcriptions**
dataset obtained from Kaggle.

<table>
<tr>
<td bgcolor="#FFF9FC">

| Details                 |               Value |
| :---------------------- | ------------------: |
| **Original Rows**       |               4,999 |
| **After Cleaning**      |               4,966 |
| **Medical Specialties** |                  40 |
| **Target**              | `medical_specialty` |
| **Class Distribution**  | Severely imbalanced |

</td>
</tr>
</table>

**Largest class:** `Surgery` — **1,088 samples**

Some specialties contain fewer than **10 samples**, highlighting
the class imbalance that must be considered during downstream modeling.

### Dataset Source

<div align="center">

<a href="https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions">

<img src="https://img.shields.io/badge/Kaggle-MTSamples%20Medical%20Transcriptions-DB2777?style=for-the-badge&logo=kaggle&logoColor=white">

</a>

<br><br>

<a href="https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions">
View Dataset on Kaggle →
</a>

</div>

---

## 📚 Topics Covered

<table>
<tr>
<td bgcolor="#FFF9FC">

* Sprint 3 planning & backlog mapping (Week 7–8)
* Why raw text cannot enter a model directly
* Tokenization: `split()` vs NLTK `word_tokenize()`
* Sentence tokenization with `sent_tokenize()`
* Text cleaning: lowercase, hyphen handling, punctuation removal
* Stop word removal with custom negation protection
* Lemmatization vs Stemming — comparison on medical terms
* Full 6-step preprocessing pipeline applied to 4,966 rows
* Before vs After analysis across three medical specialties

</td>
</tr>
</table>

---

## ⚙️ Preprocessing Pipeline

<div align="center">

<table>
<tr>
<td align="center" bgcolor="#FFF9FC">

### Raw Medical Text

↓

### 1. Lowercase

`TEXT → text`

↓

### 2. Hyphen Handling

`year-old → year old`

↓

### 3. Remove Non-Alphabetic Characters

`punctuation / special characters → removed`

↓

### 4. Tokenization

`text → tokens`

↓

### 5. Stop Word Removal

`common words → filtered`

`no / not / nor → preserved`

↓

### 6. Lemmatization

`prescribed → prescribe`

`using → use`

↓

### **Clean Medical Text**

</td>
</tr>
</table>

</div>

---

## 📊 Key Results

<table>
<tr bgcolor="#FCE7F3">
<th>Metric</th>
<th>Before</th>
<th>After</th>
<th>Reduction</th>
</tr>

<tr>
<td><b>Total Tokens</b></td>
<td>2.3M</td>
<td>1.3M</td>
<td><b>41.6%</b></td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Unique Vocabulary</b></td>
<td>70,898</td>
<td>32,183</td>
<td><b>54.6%</b></td>
</tr>

<tr>
<td><b>Negation <code>not</code></b></td>
<td>—</td>
<td>7,103 occurrences</td>
<td>Preserved</td>
</tr>

<tr bgcolor="#FFF9FC">
<td><b>Negation <code>no</code></b></td>
<td>—</td>
<td>17,789 occurrences</td>
<td>Preserved</td>
</tr>

</table>

---

## 🎯 Key Decisions

<table>
<tr>

<td width="33%" align="center" bgcolor="#FFF9FC">

### Lemmatization

**Over Stemming**

Stemming produced fragments such as:

`allergi`

`prescrib`

`administ`

Lemmatization produced more interpretable base forms.

</td>

<td width="33%" align="center" bgcolor="#FCE7F3">

### Negation Protection

Important negations such as:

`no`

`not`

`nor`

were explicitly preserved to avoid changing clinical meaning.

</td>

<td width="33%" align="center" bgcolor="#FFF9FC">

### Hyphen Handling

Hyphens were replaced with spaces:

`year-old`

↓

`year old`

This prevents the incorrect form:

`yearold`

</td>

</tr>
</table>

---

## 🔍 Before vs After

<table>
<tr>
<td bgcolor="#FFF9FC">

The before/after analysis compared vocabulary patterns across:

* **Surgery**
* **Neurology**
* **Cardiovascular / Pulmonary**

After preprocessing, common textual noise was reduced and
specialty-specific medical vocabulary became more visible.

This provides a cleaner foundation for the classification stage,
where actual class separability can be evaluated quantitatively.

</td>
</tr>
</table>

---

## 💡 Example Transformation

<table>
<tr bgcolor="#FCE7F3">
<th>Before</th>
<th>After</th>
</tr>

<tr>
<td>

```text
SUBJECTIVE:, This 23-year-old white female presents
with complaint of allergies.
```

</td>

<td>

```text
subjective year old white female present complaint
allergies
```

</td>
</tr>
</table>

---

## 🧪 Validation

<table>
<tr>
<td bgcolor="#FFF9FC">

The complete preprocessing pipeline was applied to all
**4,966 medical transcriptions**.

Validation confirmed that:

* ✓ Important negations survived preprocessing
* ✓ Key medical terms were preserved
* ✓ Total token count was substantially reduced
* ✓ Vocabulary size was substantially reduced
* ✓ Specialty-specific vocabulary became more visible

</td>
</tr>
</table>

---

## 🚀 What We Achieved

<div align="center">

|           Stage          | Status |
| :----------------------: | :----: |
|     Sprint 3 Planning    |    ✓   |
|    Dataset Exploration   |    ✓   |
|       Tokenization       |    ✓   |
|       Text Cleaning      |    ✓   |
|    Stop Word Handling    |    ✓   |
|   Negation Preservation  |    ✓   |
|       Lemmatization      |    ✓   |
|   Full Dataset Pipeline  |    ✓   |
| Before vs After Analysis |    ✓   |

<br>

<table>
<tr>
<td align="center" bgcolor="#FCE7F3">

### Raw Text → Clean Representation → Ready for Modeling

</td>
</tr>
</table>

</div>

---

## 🔜 Next

<div align="center">

<img src="https://img.shields.io/badge/DAY%202-TF--IDF%20%2B%20Text%20Classification-DB2777?style=for-the-badge&labelColor=FCE7F3">

### TF-IDF Representation + Text Classification

The cleaned medical transcriptions will be transformed into
numerical TF-IDF features and used for text classification.

</div>

---

<div align="center">

## 🌸 Week 8 — Sprint 3

### NLP → Representation → Classification

`─────────────────────────`

</div>
