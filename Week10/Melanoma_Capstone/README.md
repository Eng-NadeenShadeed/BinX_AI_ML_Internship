<div align="center">

# 🌸 Melanoma Classification

## Capstone Project

**End-to-end binary skin lesion classification — from CNN experimentation to a publicly deployed web application.**

![CAPSTONE](https://img.shields.io/badge/CAPSTONE-f8a5c2?style=flat-square) ![CNN](https://img.shields.io/badge/CNN-C44569?style=flat-square&logoColor=white) ![TENSORFLOW](https://img.shields.io/badge/TENSORFLOW-8B1E3F?style=flat-square&logoColor=white) ![STREAMLIT](https://img.shields.io/badge/STREAMLIT-C44569?style=flat-square&logoColor=white) ![FASTAPI](https://img.shields.io/badge/FASTAPI-f8a5c2?style=flat-square)

</div>

---

## 🔗 Live Application

**[Open the Deployed Streamlit App](https://binxaimlinternship-ahm9zn2cc7ebk8gzw7fzhh.streamlit.app/)**

Upload an ISIC skin lesion image → get a prediction (Benign / Malignant) with confidence score and probability bars.

---

## 🧠 Problem

Binary image classification of dermoscopic skin lesion images into **Benign** or **Malignant** classes.

Benign and malignant lesions can appear visually similar, making automated classification a meaningful and non-trivial task. The project follows a complete ML pipeline from data exploration through model comparison, serving, and public deployment.

> ⚠️ Built for educational purposes — not intended for clinical diagnosis.

---

## 📊 Dataset

| | |
|---|---|
| **Source** | ISIC Melanoma Archive |
| **Total images** | 11,888 dermoscopic images |
| **Classes** | Benign (6,289) · Malignant (5,601) |
| **Split** | 70% train · 15% validation · 15% test |

**Preprocessing pipeline:**

| Step | Detail |
|------|--------|
| Convert to RGB | Ensures 3-channel input |
| Resize | 112 × 112 pixels |
| Normalize | Pixel values ÷ 255.0 → [0, 1] |
| Augmentation (train only) | Random flip, rotation, zoom, brightness |

---

## ⚙️ Methodology

Three CNN configurations were trained and compared on the same dataset using the same evaluation protocol:

| Model | Test Accuracy | Test AUC | Test Loss |
|-------|:------------:|:--------:|:---------:|
| CNN from Scratch | 88.11% | 0.9514 | 0.2826 |
| **CNN + Data Augmentation** | **88.95%** | **0.9579** | **0.2632** |
| MobileNetV2 (frozen) | 86.47% | 0.9383 | 0.3165 |

**Selected model:** CNN + Data Augmentation — highest accuracy and AUC, lowest loss.

**Architecture:**

```
Input 112×112×3
    → Conv2D(32) + BatchNorm + MaxPool
    → Conv2D(64) + BatchNorm + MaxPool
    → Conv2D(128) + BatchNorm + MaxPool
    → Conv2D(256) + BatchNorm + MaxPool
    → GlobalAveragePooling2D
    → Dense(256) + ReLU + Dropout(0.5)
    → Dense(1) + Sigmoid
```

**Training configuration:** Adam · lr 0.001 · Binary Cross-Entropy · Early Stopping · ReduceLROnPlateau · Seed 42

---

## 📈 Results

After retraining the selected model for deployment:

| Metric | Value |
|--------|-------|
| Best val Accuracy | **89.39%** |
| Best val AUC | **0.9597** |
| Model size | 5.3 MB |
| Format | `.keras` |

**AUC 0.9597** means the model correctly ranks a malignant image above a benign one 95.97% of the time — across all classification thresholds, not just at 0.5.

---

## 🚀 Deployment Pipeline

```
Train → melanoma_cnn.keras → FastAPI /predict → Streamlit UI → Streamlit Cloud → Public URL
```

| Component | Detail |
|-----------|--------|
| **Serialization** | `model.save("melanoma_cnn.keras")` |
| **API** | FastAPI `POST /predict` — image upload, file type validation, JSON response |
| **UI** | Streamlit — image uploader, confidence metric, probability bars |
| **Hosting** | Streamlit Community Cloud |
| **Dependencies** | `streamlit` · `tensorflow` · `numpy` · `Pillow` |

**Inference preprocessing** (identical to training): RGB conversion → resize 112×112 → normalize ÷ 255.0 → add batch dimension.

---

## 🧪 Live Testing

| Image | Prediction | Confidence | Local vs. Live |
|-------|-----------|:----------:|:--------------:|
| `3.jpg` | Benign | 61.05% | ✓ Match |
| `22.jpg` | Benign | 91.12% | ✓ Match |
| `64.jpg` | Malignant | 99.91% | ✓ Match |

3/3 predictions matched exactly between local and deployed app — no training/serving skew.

---

## 📁 Files

| File | Description |
|------|-------------|
| `Melanoma_Capstone_Presentation.pptx` | Final presentation — 12 slides |
| `Melanoma_Capstone_Presentation.html` | Interactive HTML version |

---

## ⚠️ Limitations

- Evaluated on one dataset — generalization to other populations is unverified
- Images resized to 112×112 — some fine-grained detail is lost
- MobileNetV2 tested with frozen layers only — fine-tuning not evaluated
- No clinical validation — not a diagnostic tool

---

## 🔮 Future Work

- Fine-tune MobileNetV2 pretrained layers on melanoma data
- Evaluate at higher resolutions (224×224)
- Add Grad-CAM for visual explainability
- Evaluate on an external validation dataset

---

<div align="center">

**BinX Tech · AI & ML Internship · 2026**

</div>
