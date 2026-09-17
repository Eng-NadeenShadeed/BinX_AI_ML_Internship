
<div align="center">

# 🌸 Week 9 — Day 5

## Repository Polish, Definition of Done & Sprint Review

**Final Sprint 4 documentation, repository organization, reproducibility, and project review.**

![Week 9](https://img.shields.io/badge/Week%209-Day%205-8B1E3F?style=flat-square&logoColor=white)
![Repository](https://img.shields.io/badge/Repository-Polished-C44569?style=flat-square&logoColor=white)
![Documentation](https://img.shields.io/badge/Documentation-Technical%20Write--Up-F8A5C2?style=flat-square)
![MLOps](https://img.shields.io/badge/MLOps-Reproducibility-8B1E3F?style=flat-square&logoColor=white)

</div>

---

## 📌 Overview

Day 5 concludes **Sprint 4**, the final deployment sprint of the Capstone project.

The focus of the day was to finalize the project documentation, polish the repository, verify the **Definition of Done**, review Sprint 4 deliverables, and prepare the project for the final presentation.

The main activities completed were:

- Polishing the repository structure and documentation
- Completing the technical write-up
- Reviewing the full Definition of Done
- Verifying reproducibility requirements
- Reviewing Sprint 4 deliverables
- Completing the Sprint Review
- Completing the full-project retrospective
- Preparing the project for Week 10

---

## 🎯 Objectives

All Day 5 objectives were completed:

| Objective | Status |
|---|:---:|
| 📁 Repository Polish | ✅ |
| 📝 Technical Write-Up | ✅ |
| ✅ Definition of Done | ✅ |
| 🔁 Reproducibility Review | ✅ |
| 🔍 Sprint Review | ✅ |
| 💭 Full-Project Retrospective | ✅ |
| 🎤 Week 10 Preparation | ✅ |

---

## 📂 1. Repository Polish

The repository was reviewed and organized to provide a clear structure for the complete Capstone project.

```text
Repository
│
├── Week 1 → Week 8
│   └── Learning notebooks and previous project work
│
├── Week 9
│   ├── Day 1 — Model Retraining & Serialization
│   ├── Day 2 — FastAPI
│   ├── Day 3 — Streamlit
│   ├── Day 4 — Public Deployment
│   └── Day 5 — Documentation & Review
│
├── Model Artifacts
├── requirements.txt
├── .gitignore
├── README.md
└── Technical Write-Up
````

### Repository Quality

| Item                           | Status |
| ------------------------------ | :----: |
| Repository structure organized |    ✅   |
| Required artifacts included    |    ✅   |
| Dependencies documented        |    ✅   |
| Documentation updated          |    ✅   |
| Project files reviewed         |    ✅   |

---

## 📝 2. Technical Write-Up

A dedicated technical write-up was completed to document the complete machine learning and deployment workflow.

The write-up covers:

1. Problem Statement
2. Dataset
3. Methodology
4. Model Comparison
5. Key Findings
6. Model Retraining & Serialization
7. Deployment Pipeline
8. Reproducibility
9. Limitations
10. Future Work
11. Conclusion

The technical write-up provides the main technical reference for the project and supports the Week 10 final presentation.

---

## 📊 3. Definition of Done

The complete project was reviewed against the Sprint 4 **Definition of Done**.

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

## 🔁 4. Reproducibility

Reproducibility was reviewed as part of the final project preparation.

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

## 🧪 5. Experiment Tracking

The model development experiments were documented throughout the learning notebooks.

The **Week 7 — Day 2** experiment compared three approaches:

* CNN from Scratch
* CNN + Data Augmentation
* MobileNetV2

### Model Comparison

| Model                  | Test Accuracy |   Test AUC |  Test Loss |
| ---------------------- | ------------: | ---------: | ---------: |
| CNN from Scratch       |        88.11% |     0.9514 |     0.2826 |
| **CNN + Augmentation** |    **88.95%** | **0.9579** | **0.2632** |
| MobileNetV2 (frozen)   |        86.47% |     0.9383 |     0.3165 |

The **CNN + Data Augmentation** model from **Week 7 — Day 2** was selected based on the documented test results.

Week 9 continued from this selected model rather than developing a new model architecture.

---

## 🚀 6. Sprint 4 Review

Sprint 4 continued from the model selected during **Week 7 — Day 2**.

The selected CNN + Data Augmentation approach was retrained during **Week 9 — Day 1** and prepared for deployment.

### Sprint 4 Flow

```text
Week 7 — Day 2
Model Development & Comparison
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
FastAPI
        ↓
Week 9 — Day 3
Streamlit
        ↓
Week 9 — Day 4
Public Deployment
        ↓
Week 9 — Day 5
Documentation & Review
```

### Sprint 4 Deliverables

| Deliverable                | Status |
| -------------------------- | :----: |
| Retrained CNN model        |    ✅   |
| Serialized `.keras` model  |    ✅   |
| FastAPI prediction service |    ✅   |
| Streamlit application      |    ✅   |
| Public deployment          |    ✅   |
| Local testing              |    ✅   |
| Live testing               |    ✅   |
| Technical documentation    |    ✅   |
| Repository review          |    ✅   |

---

## 📈 7. Model Retraining Results

The selected **CNN + Data Augmentation** approach was retrained during Week 9 — Day 1 for deployment preparation.

| Metric                   |     Result |
| ------------------------ | ---------: |
| Best Validation Accuracy | **89.39%** |
| Best Validation AUC      | **0.9597** |

The trained model was saved as:

```text
melanoma_cnn.keras
```

The serialized model was loaded and tested successfully after saving.

---

## 🌐 8. Deployment Verification

The public Streamlit application was tested using the same three test images used during local verification.

| Image    | Prediction | Confidence |  Result |
| -------- | ---------- | ---------: | :-----: |
| `3.jpg`  | Benign     |     61.05% | ✓ Match |
| `22.jpg` | Benign     |     91.12% | ✓ Match |
| `64.jpg` | Malignant  |     99.91% | ✓ Match |

### Verification Result

**3/3 tested inputs produced matching local and live predictions.**

This provided a final verification of consistent behavior for the selected test cases.

---

## 🧹 9. Final Repository Review

The final repository review was completed as part of Day 5.

| Review Item                   | Status |
| ----------------------------- | :----: |
| README.md                     |    ✅   |
| Technical Write-Up            |    ✅   |
| Week 9 notebooks/scripts      |    ✅   |
| Serialized model              |    ✅   |
| requirements.txt              |    ✅   |
| .gitignore                    |    ✅   |
| Deployment configuration      |    ✅   |
| Project documentation         |    ✅   |
| Results documentation         |    ✅   |
| Live deployment documentation |    ✅   |
| Git workflow review           |    ✅   |

---

## 💭 10. Full-Project Retrospective

### What Went Well

* Built the project progressively across multiple stages.
* Compared multiple deep learning approaches before selecting a model.
* Continued from the selected Week 7 model into deployment.
* Practiced both API-based and interactive model serving.
* Verified local and deployed predictions using test cases.

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

## 🎤 11. Preparation for Week 10

The Day 5 work was completed with the final presentation in mind.

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

## 🏁 12. Day 5 Outcome

Day 5 completed the final documentation, repository review, Definition of Done verification, Sprint Review, and retrospective for Sprint 4.

The complete project journey can be summarized as:

```text
Week 7 — Day 2
CNN Experimentation & Model Comparison
          ↓
CNN + Data Augmentation
Selected Model
          ↓
Week 9 — Day 1
Retraining & Serialization
          ↓
FastAPI Service
          ↓
Streamlit Application
          ↓
Public Deployment
          ↓
Repository Polish & Technical Documentation
          ↓
Sprint Review & Retrospective
```

### 🌸 Sprint 4 Complete

**From model experimentation → to deployment → to a complete ML project**

**BinX AI & ML Internship · Week 9 · 2026**

</div>
```
