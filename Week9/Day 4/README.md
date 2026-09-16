<div align="center">

# 🌸 Week 9 — Day 4

## Public Deployment

**Deploying the ISIC Melanoma CNN as a publicly accessible Streamlit application.**

![WEEK 9](https://img.shields.io/badge/WEEK%209-f8a5c2?style=flat-square) ![DAY 4](https://img.shields.io/badge/DAY%204-C44569?style=flat-square\&logoColor=white) ![STREAMLIT](https://img.shields.io/badge/STREAMLIT-8B1E3F?style=flat-square\&logoColor=white) ![TENSORFLOW](https://img.shields.io/badge/TENSORFLOW-C44569?style=flat-square\&logoColor=white) ![DEPLOYMENT](https://img.shields.io/badge/DEPLOYMENT-f8a5c2?style=flat-square)

</div>

---

## 🧠 Overview

Day 4 focused on deploying the ISIC Melanoma CNN as a public Streamlit application.

The goal was to move the application from a local development environment to a cloud-hosted environment where users can access the model through a public URL.

The deployment process included dependency configuration, model packaging, cloud deployment, live testing, and verification against the local application.

---

## 📁 Files

| File                            | Description                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `day4_public_deployment.ipynb`  | Learning notebook — deployment concepts, hosting platforms, dependencies, model files, testing, and MLOps |
| `Hands_On_Lab.ipynb`            | Hands-on lab — deployment preparation, local testing, public deployment, and live verification            |
| `deployment/app.py`             | Deployment-ready Streamlit application                                                                    |
| `deployment/melanoma_cnn.keras` | Serialized CNN model used by the deployed application                                                     |
| `requirements.txt`              | Deployment dependencies required by the Streamlit Cloud environment                                       |
| `README.md`                     | Day 4 documentation                                                                                       |

---

## 📚 Topics Covered

| Topic                     | Details                                                      |
| ------------------------- | ------------------------------------------------------------ |
| Deployment                | Moving an ML application from local to public access         |
| Hosting Platforms         | Evaluating available cloud hosting options                   |
| Streamlit Community Cloud | Public hosting for the Streamlit application                 |
| Dependencies              | Configuring packages required by the deployed application    |
| Python Version            | Selecting a compatible Python runtime                        |
| Model Files               | Packaging and loading the serialized `.keras` model          |
| File Paths                | Using deployment-friendly relative paths                     |
| Build Environment         | Understanding dependency installation during deployment      |
| Live Testing              | Testing the deployed application with real image inputs      |
| Local vs Live             | Verifying consistent predictions across environments         |
| MLOps                     | Connecting deployment with reproducibility and model serving |

---

## 🚀 Deployment Workflow

```text
Trained CNN Model
       ↓
Serialize Model
       ↓
Prepare Streamlit Application
       ↓
Configure requirements.txt
       ↓
Prepare Deployment Files
       ↓
Push to GitHub
       ↓
Deploy to Streamlit Community Cloud
       ↓
Public Streamlit Application
       ↓
Live Testing
       ↓
Local vs Live Verification
```

---

## ☁️ Deployment Platform

The application was deployed using **Streamlit Community Cloud**.

The platform was selected because the project is already implemented as a Streamlit application and requires a Python runtime to execute TensorFlow, NumPy, Pillow, and the serialized CNN model.

The deployment uses the GitHub repository as the application source.

---

## ⚙️ Deployment Configuration

| Component       | Configuration             |
| --------------- | ------------------------- |
| Framework       | Streamlit                 |
| Runtime         | Python 3.13               |
| Model Framework | TensorFlow / Keras        |
| Model Format    | `.keras`                  |
| Input Type      | JPG / JPEG / PNG          |
| Input Size      | 112 × 112 × 3             |
| Preprocessing   | RGB + Resize + `/255.0`   |
| Output          | Benign / Malignant        |
| Threshold       | 0.5                       |
| Hosting         | Streamlit Community Cloud |

---

## 📦 Deployment Dependencies

The deployment environment uses a focused `requirements.txt` containing only the packages required by the Streamlit application:

```text
streamlit==1.63.0
tensorflow==2.21.0
numpy==2.4.6
Pillow==12.3.0
```

Keeping the deployment dependencies focused helps avoid unnecessary packages and platform-specific dependencies during cloud installation.

---

## 🖥️ Deployed Application

### 🔗 Public URL

**[Open the Live Streamlit Application](https://binxaimlinternship-ahm9zn2cc7ebk8gzw7fzhh.streamlit.app/)**

The application allows users to:

1. Upload an ISIC skin lesion image.
2. Preview the uploaded image.
3. Run the serialized CNN model.
4. View the predicted class.
5. View the prediction confidence.
6. View Benign and Malignant probabilities.

---

## 📊 Live Deployment Testing

The deployed application was tested using the same images used during local testing.

| Test Image | Prediction | Confidence | Local vs Live |
| ---------- | ---------- | ---------- | ------------- |
| `3.jpg`    | Benign     | 61.05%     | Match ✓       |
| `22.jpg`   | Benign     | 91.12%     | Match ✓       |
| `64.jpg`   | Malignant  | 99.91%     | Match ✓       |

### Verification Result

**3/3 test cases matched exactly between the local and deployed applications.**

This confirms that the deployed application is using the same model and inference preprocessing pipeline as the local application.

---

## 🔄 Local vs Live Consistency

| Component                | Local     | Live      |
| ------------------------ | --------- | --------- |
| CNN Model                | Same      | Same      |
| Input Size               | 112 × 112 | 112 × 112 |
| RGB Conversion           | ✓         | ✓         |
| Normalization            | `/255.0`  | `/255.0`  |
| Classification Threshold | 0.5       | 0.5       |
| Predictions              | Verified  | Verified  |
| Confidence Values        | Verified  | Verified  |

---

## 🧩 Deployment Structure

```text
deployment/
├── app.py
├── melanoma_cnn.keras
└── requirements.txt
```

The application loads the serialized model from the same directory using a relative path, making the deployment structure independent of the local machine's absolute file paths.

---

## 🔗 Connection to Previous Days

| Day       | Contribution                                    |
| --------- | ----------------------------------------------- |
| Day 1     | Serialized the trained CNN model                |
| Day 2     | Built a FastAPI prediction service              |
| Day 3     | Built an interactive Streamlit dashboard        |
| **Day 4** | **Deployed the Streamlit application publicly** |

The same trained CNN model is reused throughout the deployment pipeline.

---

## 🎯 Day 4 Outcome

By the end of Day 4, the ISIC Melanoma CNN was successfully deployed as a public Streamlit application.

**Deployment Status: PASSED ✓**

**Live Testing: 3/3 Matched ✓**

**Public Access: Available ✓**

---

## ➡️ Next — Day 5

Polish the repository, finalize documentation, review the complete deployment pipeline, and prepare the project for the final Sprint Review.
