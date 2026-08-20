# 🫀 Cardiac Patient Monitoring System

## AI & Machine Learning Internship — Project Planning & Roadmap

**BinX Tech AI & Machine Learning Internship**
**Phase 2 → Phase 3 Transition**
**Planning Document — Week 5, Day 5**

---

# 1. Project Overview

The **Cardiac Patient Monitoring System** is a continuous AI & Machine Learning project developed throughout the internship.

The project was not started as a separate Phase 3 project. Instead, it was intentionally developed incrementally across the previous training weeks, with each week contributing a new stage of the machine learning workflow.

The project began with understanding and preparing a cardiac-related dataset, followed by exploratory data analysis, supervised machine learning, model evaluation, feature engineering, and pipeline development.

During **Week 5**, the project is extended by adding unsupervised learning concepts, including clustering and dimensionality reduction. Day 5 is used to document the complete project plan, review what has already been accomplished, define the remaining work, and establish a clear roadmap for the next phase.

The overall development model is therefore:

**Data → Cleaning → EDA → Supervised Learning → Evaluation → Feature Engineering → Pipelines → Unsupervised Learning → Final Documentation → Future Application**

The project remains focused on the same cardiac dataset and the same overall objective throughout the internship.

---

# 2. Project Problem Statement

## 2.1 Problem

Cardiac-related datasets contain multiple clinical measurements that may be associated with the presence of heart disease.

However, raw clinical data cannot be directly used for reliable machine learning analysis without first understanding its structure, identifying data-quality problems, exploring relationships between variables, and developing an appropriate machine learning workflow.

The project therefore addresses the following problem:

> **How can machine learning techniques be used to analyze cardiac-related patient data, identify patterns associated with heart disease, build and evaluate classification models, and explore hidden structures within the dataset through unsupervised learning?**

---

## 2.2 Proposed Solution

The project addresses this problem through a complete curriculum-aligned machine learning workflow.

The workflow includes:

1. Loading and understanding the dataset.
2. Checking data types and data quality.
3. Identifying invalid and suspicious values.
4. Performing exploratory data analysis.
5. Studying distributions, relationships, correlations, and class balance.
6. Defining heart disease prediction as a supervised classification problem.
7. Training a baseline classification model.
8. Comparing multiple machine learning classifiers.
9. Evaluating models using appropriate classification metrics.
10. Applying cross-validation.
11. Performing feature engineering.
12. Building reusable Scikit-learn preprocessing and modeling pipelines.
13. Performing hyperparameter tuning.
14. Selecting the best model using validation data.
15. Evaluating the selected model once on the held-out test set.
16. Extending the project with unsupervised learning.
17. Applying clustering and dimensionality reduction techniques.
18. Interpreting the discovered structures carefully.
19. Documenting the complete project and its limitations.

The project is intended as an **AI/ML analysis and educational project**, not as a clinical diagnosis or treatment system.

---

# 3. Project Objective

The main objective is to build a complete and reproducible machine learning workflow for cardiac-related data using the techniques covered throughout the AI & Machine Learning internship.

The project specifically aims to:

* Understand and prepare the cardiac dataset.
* Perform meaningful exploratory data analysis.
* Identify important relationships between features and the target.
* Build a supervised classification system for heart disease prediction.
* Compare different machine learning models.
* Evaluate models using consistent and appropriate metrics.
* Use cross-validation to assess model robustness.
* Apply feature engineering to create additional informative features.
* Build Scikit-learn Pipelines for reproducible preprocessing and modeling.
* Tune model hyperparameters.
* Select a final model using validation data without using the test set for model selection.
* Extend the analysis with unsupervised learning.
* Apply clustering to investigate potential patient groups.
* Apply PCA/dimensionality reduction to investigate lower-dimensional structure.
* Document findings, limitations, and future improvements.

---

# 4. Project Scope

## 4.1 In Scope

The project includes:

* Python development.
* NumPy and Pandas.
* Jupyter Notebook.
* Data cleaning and preparation.
* Descriptive statistics.
* Exploratory Data Analysis.
* Data visualization.
* Correlation analysis.
* Supervised classification.
* Multiple classification models.
* Train/validation/test splitting.
* Cross-validation.
* Accuracy, precision, recall, F1-score, and ROC-AUC.
* Confusion matrix analysis.
* Feature engineering.
* Scikit-learn preprocessing.
* Scikit-learn Pipelines.
* Hyperparameter tuning.
* Clustering.
* Dimensionality reduction.
* PCA.
* Visualization and interpretation.
* Git and GitHub based version control.
* Project documentation.

The original project guide explicitly defines this type of workflow as the expected curriculum-aligned scope.

---

## 4.2 Out of Scope

The project does not aim to provide:

* Clinical diagnosis.
* Medical treatment recommendations.
* Emergency medical instructions.
* Identifiable patient information.
* Deep learning or neural networks.
* LLM-based systems.
* MLOps infrastructure.
* Production medical deployment.
* Advanced explainability techniques that were not covered in the training.
* Dependence on another student's project.

These limitations are consistent with the project guide's defined scope.

---

# 5. Dataset

## 5.1 Dataset Description

The project uses the **Heart Disease Prediction Dataset**.

The dataset contains:

* **918 observations**
* **11 original input features**
* **1 target variable**
* Mixed numerical, binary, and categorical features.

The target variable is:

`HeartDisease`

where:

* `0` = No Heart Disease
* `1` = Heart Disease

The original dataset contains 918 observations, with approximately:

* **55.3% Heart Disease**
* **44.7% No Heart Disease**

These characteristics were established during the initial data exploration.

---

## 5.2 Features

The original feature set contains:

### Numerical Features

* Age
* RestingBP
* Cholesterol
* MaxHR
* Oldpeak

### Binary Features

* FastingBS

### Categorical Features

* Sex
* ChestPainType
* RestingECG
* ExerciseAngina
* ST_Slope

### Target

* HeartDisease

---

# 6. Data Quality Plan

One of the first stages of the project was identifying potential data-quality problems rather than assuming that every value in the dataset was valid.

During EDA, suspicious zero values were identified.

Specifically:

* `RestingBP` contained an invalid zero value.
* `Cholesterol` contained **172 zero values**.

These zero values were treated as invalid rather than meaningful measurements.

The invalid values were converted to missing values and handled through median imputation inside the preprocessing pipeline.

This approach prevents manual imputation from leaking information from validation or test data into the training process.

---

# 7. Project Development Strategy

The project follows an **incremental development strategy**.

Instead of implementing the complete machine learning system in one step, the project was developed week by week.

Each training week introduced a new technical concept, and that concept was incorporated into the same cardiac project whenever appropriate.

The development strategy is:

```text
Week 1
   ↓
Python / NumPy / Pandas / Dataset Understanding
   ↓
Week 2
   ↓
Statistics / Probability / EDA
   ↓
Week 3
   ↓
Supervised Learning
   ↓
Week 4
   ↓
Evaluation / Feature Engineering / Pipelines / Tuning
   ↓
Week 5
   ↓
Unsupervised Learning / PCA / Project Planning
   ↓
Phase 3
   ↓
Further Development / Refinement / Finalization
```

This allows the project to demonstrate the progressive application of the internship curriculum rather than treating each week's topics as isolated exercises.

---

# 8. Weekly Project Roadmap

## Week 1 — Foundations and Dataset Preparation

### Main Goal

Establish the project environment and understand the dataset.

### Planned / Completed Activities

* Set up the Python/Jupyter environment.
* Load the cardiac dataset.
* Use Pandas and NumPy for initial inspection.
* Inspect rows and columns.
* Inspect data types.
* Identify numerical and categorical variables.
* Define the target variable.
* Begin data cleaning.
* Check for missing values and duplicates.
* Identify suspicious values.

### Project Outcome

By the end of this stage, the project had a clearly defined dataset and target variable and was ready for deeper statistical and exploratory analysis.

---

# 9. Week 2 — Statistics and Exploratory Data Analysis

## Main Goal

Understand the structure and behavior of the cardiac dataset before applying machine learning.

### Activities

* Descriptive statistics.
* Numerical feature analysis.
* Categorical feature analysis.
* Distribution analysis.
* Target distribution analysis.
* Class-balance analysis.
* Relationship analysis between features and target.
* Correlation analysis.
* Visualization using Matplotlib.
* Identification of potential outliers.
* Identification of important patterns.

### Important Findings

Several meaningful patterns were identified during EDA.

Examples include:

* Patients with heart disease tended to have a higher median age.
* Patients with heart disease tended to have lower maximum heart rates.
* `Oldpeak` showed a different distribution between the two target classes.
* `ST_Slope`, `ChestPainType`, and `ExerciseAngina` showed strong relationships with the target.
* The target classes were reasonably balanced, although heart disease represented the larger class.

These findings were later used to guide the supervised learning stage.

---

# 10. Week 3 — Supervised Learning

## Main Goal

Transform the exploratory findings into a supervised classification problem.

### Problem Definition

The target is:

```text
HeartDisease
```

The machine learning task is therefore:

```text
Input:
Patient clinical measurements

        ↓

Machine Learning Classifier

        ↓

Output:
0 → No Heart Disease
1 → Heart Disease
```

### Activities

* Define `X` and `y`.
* Create the train/validation/test split.
* Preserve class proportions using stratification.
* Build a preprocessing workflow.
* Train a baseline classifier.
* Train additional classification models.
* Compare model performance.
* Identify a suitable candidate model.

### Models Compared

The project evaluated:

* Logistic Regression
* Random Forest
* Decision Tree
* SVM
* k-NN

The models were evaluated using a consistent validation methodology.

### Model Selection

Random Forest was selected as the main candidate based on its strong validation performance, including disease-class F1, recall, and competitive ROC-AUC.

The project therefore continued with Random Forest as the primary model for the next stages.

---

# 11. Week 4 — Evaluation, Feature Engineering, Pipelines and Tuning

## Main Goal

Improve the reliability and reproducibility of the supervised learning workflow.

### 11.1 Train / Validation / Test Strategy

The project uses:

| Dataset    | Percentage | Purpose                        |
| ---------- | ---------: | ------------------------------ |
| Training   |        60% | Model learning                 |
| Validation |        20% | Model comparison and selection |
| Test       |        20% | Final evaluation               |

The split is stratified to preserve the target-class distribution.

The test set is kept isolated until the final evaluation.

This prevents the test set from influencing model selection.

---

## 11.2 Feature Engineering

Four deterministic features were created:

### `AgeGroup`

Age is grouped into meaningful ranges:

```text
<45
45–55
55–65
65+
```

### `HRReserve`

```text
MaxHR / (220 - Age)
```

This represents the achieved maximum heart rate relative to the age-predicted maximum.

### `HighBP`

```text
1 if RestingBP > 140
0 otherwise
```

### `MaxHR_pct`

```text
MaxHR / (220 - Age) × 100
```

The engineered feature set increases the number of features from **11 to 15**.

The features are deterministic formulas and do not learn statistical parameters from the complete dataset before splitting.

---

# 12. Pipeline Development

Two preprocessing tracks were developed:

### Original Feature Track

Uses the original 11 features.

### Engineered Feature Track

Uses the original features plus the four engineered features.

Both tracks use consistent preprocessing logic:

```text
Numerical Features
    ↓
Median Imputation
    ↓
StandardScaler

Categorical Features
    ↓
OneHotEncoder

Binary Features
    ↓
Passthrough

Preprocessed Features
    ↓
Random Forest
```

Using Scikit-learn Pipelines makes preprocessing and model training repeatable and reduces the risk of inconsistent transformations.

---

# 13. Hyperparameter Tuning

Random Forest was tuned using `GridSearchCV` with 5-fold cross-validation.

The same parameter grid was applied to both the original and engineered feature tracks.

Parameters included:

```text
n_estimators
max_depth
min_samples_split
```

The purpose of this stage was to determine whether:

1. Hyperparameter tuning improves the model.
2. Feature engineering improves the model.
3. Combining feature engineering with tuning produces the strongest validation performance.

The three main candidates were therefore:

```text
Default Random Forest
        vs
Tuned Random Forest — Original Features
        vs
Tuned Random Forest — Engineered Features
```

The winner is selected using the validation set only.

---

# 14. Week 5 — Unsupervised Learning Extension

## Main Goal

Extend the project beyond supervised prediction and investigate whether the cardiac dataset contains meaningful hidden structures.

Week 5 introduced:

* K-Means
* DBSCAN
* Hierarchical Clustering
* PCA
* t-SNE
* Anomaly Detection

The Week 5 curriculum specifically requires interns to work with unsupervised learning and then complete project planning as the transition into Phase 3.

---

## 14.1 K-Means

The first planned unsupervised technique is K-Means clustering.

### Purpose

Investigate whether patients can naturally be grouped according to similarities in their clinical measurements without using the `HeartDisease` target during clustering.

### Planned Process

```text
Select numerical features
        ↓
Scale features
        ↓
Test different k values
        ↓
Elbow Method
        ↓
Silhouette Score
        ↓
Select suitable k
        ↓
Fit K-Means
        ↓
Visualize clusters
        ↓
Interpret patient groups
```

Feature scaling is required because K-Means is distance-based.

---

# 15. DBSCAN and Hierarchical Clustering

The project will also compare alternative clustering approaches.

## DBSCAN

DBSCAN will be investigated because it can:

* Discover clusters without specifying `k`.
* Detect noise/outlier points.
* Handle irregularly shaped clusters.

## Hierarchical Clustering

Hierarchical clustering will be used to:

* Explore nested structures.
* Build a dendrogram.
* Investigate different possible cluster counts.

The three approaches will be compared:

```text
K-Means
   vs
DBSCAN
   vs
Hierarchical Clustering
```

The method will not be selected simply because it produces more clusters; the choice will be based on the dataset structure and the interpretation of the resulting groups.

The Week 5 curriculum specifically asks for comparison of these clustering methods and justification of which method best fits the data.

---

# 16. PCA and Dimensionality Reduction

PCA will be applied to investigate the dimensional structure of the dataset.

### Planned Process

```text
Prepare numerical features
        ↓
StandardScaler
        ↓
Apply PCA
        ↓
Calculate explained variance
        ↓
Plot cumulative explained variance
        ↓
Choose appropriate number of components
        ↓
Visualize reduced data
```

The goal is to determine how much of the dataset's variance can be represented using fewer dimensions.

PCA is also useful for visualizing high-dimensional data in two dimensions.

---

# 17. t-SNE and Anomaly Detection

The project roadmap also includes the Week 5 Day 4 concepts.

## t-SNE

t-SNE will be considered primarily as a visualization technique for exploring local structure in the dataset.

It will be compared conceptually with PCA:

| PCA                                    | t-SNE                           |
| -------------------------------------- | ------------------------------- |
| Preserves global variance              | Preserves local neighborhoods   |
| Useful for reduction and visualization | Mainly used for visualization   |
| Faster                                 | More computationally expensive  |
| Components have mathematical meaning   | Axes do not have direct meaning |

The purpose is not to use t-SNE as the final predictive representation, but to visually investigate whether groups identified by clustering appear locally separated.

---

## Anomaly Detection

Isolation Forest may be used to investigate unusual observations in the dataset.

The goal is to identify observations that differ significantly from the general population and then inspect whether those observations correspond to unusual combinations of cardiac measurements.

The results will be interpreted cautiously because an anomaly does not automatically represent an error or a medical condition.

---

# 18. Day 5 — Project Planning

## Why Day 5 Is Different

Day 5 does not require us to abandon the existing cardiac project and select one of the six new project options.

Instead, because the **Cardiac Patient Monitoring System is already an active continuous project**, Day 5 is used to formally document and plan the continuation of this project.

Therefore, the project selection decision is:

> **Continue development of the existing Cardiac Patient Monitoring System as the project's applied AI/ML track.**

The six options listed in the Week 5 curriculum are therefore not treated as alternative projects for this plan. The existing cardiac project is the project being carried forward.

---

# 19. Definition of Done

The project will be considered complete when the following conditions are satisfied:

### Data

* [ ] The cardiac dataset is included and documented.
* [ ] The target variable is clearly defined.
* [ ] Data-quality issues are identified and handled.
* [ ] The preprocessing process is reproducible.

### Exploratory Analysis

* [ ] Descriptive statistics are included.
* [ ] Important distributions are analyzed.
* [ ] Class balance is documented.
* [ ] Relationships and correlations are investigated.
* [ ] Meaningful visualizations are included.

### Supervised Learning

* [ ] A clear classification problem is defined.
* [ ] A baseline classifier is implemented.
* [ ] At least one additional classifier is compared.
* [ ] Models use a consistent evaluation methodology.
* [ ] Cross-validation is performed.
* [ ] Confusion matrix is included.
* [ ] Accuracy, precision, recall, F1-score, and ROC-AUC are reported where appropriate.

### Feature Engineering & Pipelines

* [ ] Engineered features are documented.
* [ ] Preprocessing is implemented through Scikit-learn.
* [ ] Model training is integrated into a reusable Pipeline.
* [ ] Hyperparameter tuning is performed.
* [ ] Final model selection is based on validation data.

### Unsupervised Learning

* [ ] Clustering is performed.
* [ ] K-Means is evaluated using elbow and silhouette analysis.
* [ ] DBSCAN and/or hierarchical clustering are investigated.
* [ ] PCA is applied.
* [ ] Dimensionality reduction is visualized.
* [ ] Results are interpreted rather than only reported.

### Documentation

* [ ] README is complete.
* [ ] Notebook contains clear Markdown explanations.
* [ ] Limitations are documented.
* [ ] Setup and execution instructions are provided.
* [ ] Project is committed to GitHub.
* [ ] Final notebook runs from top to bottom.

The project guide similarly requires a reproducible environment, meaningful EDA, multiple supervised models, cross-validation, feature engineering/pipelines, and an unsupervised analysis.

---

# 20. Sprint Planning

The project will continue using an incremental sprint-based approach.

## Sprint Goal

> **Extend the existing Cardiac Patient Monitoring System from a supervised machine learning project into a more complete AI/ML analysis by integrating unsupervised learning, dimensionality reduction, rigorous interpretation, and professional documentation.**

---

# 21. Sprint Backlog

| ID  | Task                                               | Priority | Expected Output                             |
| --- | -------------------------------------------------- | -------- | ------------------------------------------- |
| S1  | Review current project state                       | High     | Confirm completed stages                    |
| S2  | Finalize Week 5 unsupervised learning requirements | High     | Clustering/PCA analysis                     |
| S3  | Apply K-Means                                      | High     | Clusters + elbow + silhouette               |
| S4  | Apply DBSCAN                                       | High     | Clusters + noise analysis                   |
| S5  | Apply hierarchical clustering                      | Medium   | Dendrogram + interpretation                 |
| S6  | Compare clustering methods                         | High     | Method comparison                           |
| S7  | Apply PCA                                          | High     | Explained variance + reduced representation |
| S8  | Apply t-SNE                                        | Medium   | 2D visualization                            |
| S9  | Investigate anomaly detection                      | Medium   | Isolation Forest analysis                   |
| S10 | Integrate findings into project narrative          | High     | Updated project documentation               |
| S11 | Update README                                      | High     | Complete project roadmap                    |
| S12 | Clean and validate notebook                        | High     | Top-to-bottom reproducibility               |
| S13 | Commit changes to GitHub                           | High     | Version-controlled project                  |
| S14 | Prepare final technical explanation                | High     | Demo-ready project                          |

---

# 22. Acceptance Criteria

Every major task must satisfy the following criteria before it is considered complete.

### Technical

* The notebook cell executes without errors.
* The implementation uses the appropriate library and technique.
* Data preprocessing is applied correctly.
* Results are reproducible.
* No hidden manual steps are required.

### Analytical

* Results are not only displayed but interpreted.
* Method choices are justified.
* Visualizations support the analysis.
* Limitations are acknowledged.
* Unsupervised results are not treated as ground truth without interpretation.

### Documentation

* The work is explained in Markdown.
* Important decisions are documented.
* Metrics and results are recorded.
* The README is updated when the project scope changes.

### Git/GitHub

* Work is committed to the project repository.
* Commit messages clearly describe the change.
* Work is organized consistently.
* Changes can be reviewed independently.

These criteria follow the Week 5 requirement that each backlog task have written acceptance criteria covering execution, Git workflow, documentation, and metric/result tracking.

---

# 23. GitHub Workflow

The project will use GitHub for version control and progress tracking.

The intended workflow is:

```text
Create / Update Task
        ↓
Work on Feature / Task
        ↓
Run and Validate Notebook
        ↓
Document Results
        ↓
Commit Changes
        ↓
Push to GitHub
        ↓
Review
        ↓
Merge
```

The repository should preserve the development history so that the progression of the project can be demonstrated.

---

# 24. Risk Management

Several risks were identified during project planning.

## Risk 1 — Data Quality

Invalid values may affect model performance.

### Mitigation

Identify suspicious values during EDA and handle them inside the preprocessing workflow.

---

## Risk 2 — Data Leakage

Using information from validation or test data during preprocessing or model selection can produce overly optimistic results.

### Mitigation

Use train/validation/test separation and place learned preprocessing operations inside Scikit-learn Pipelines.

---

## Risk 3 — Overfitting

A model may perform well on training data but fail to generalize.

### Mitigation

Use cross-validation, validation-based model selection, and a final held-out test set.

---

## Risk 4 — Misinterpreting Clusters

Unsupervised learning has no predefined correct answer.

### Mitigation

Use elbow analysis, silhouette score, visualization, domain-aware interpretation, and comparison between multiple clustering methods.

---

## Risk 5 — Project Scope Expansion

Adding too many techniques may make the project difficult to maintain or explain.

### Mitigation

Prioritize techniques directly connected to the internship curriculum and the defined project objective.

---

# 25. Project Success Criteria

The project will be considered successful if it demonstrates the complete learning progression:

```text
Understand Data
      ↓
Clean Data
      ↓
Explore Data
      ↓
Define Problem
      ↓
Build Baseline
      ↓
Compare Models
      ↓
Evaluate Models
      ↓
Engineer Features
      ↓
Build Pipelines
      ↓
Tune Model
      ↓
Select Final Model
      ↓
Explore Hidden Structure
      ↓
Clustering
      ↓
PCA / Dimensionality Reduction
      ↓
Interpret Findings
      ↓
Document & Reproduce
```

The project should demonstrate not only that algorithms were executed, but that the student understands **why each stage was performed, what it produced, and how the result affected the next stage**.

---

# 26. Current Project Status

| Project Area                     | Status              |
| -------------------------------- | ------------------- |
| Dataset selection                | ✅ Completed         |
| Dataset loading                  | ✅ Completed         |
| Data understanding               | ✅ Completed         |
| Data cleaning                    | ✅ Completed         |
| EDA                              | ✅ Completed         |
| Statistics                       | ✅ Completed         |
| Supervised problem definition    | ✅ Completed         |
| Baseline model                   | ✅ Completed         |
| Model comparison                 | ✅ Completed         |
| Cross-validation                 | ✅ Completed         |
| Feature engineering              | ✅ Completed         |
| Scikit-learn pipelines           | ✅ Completed         |
| Hyperparameter tuning            | ✅ Completed         |
| Validation-based model selection | ✅ Completed         |
| Final test evaluation            | ✅ Completed         |
| K-Means                          | 🔄 Week 5 extension |
| DBSCAN                           | 🔄 Week 5 extension |
| Hierarchical clustering          | 🔄 Week 5 extension |
| PCA                              | 🔄 Week 5 extension |
| t-SNE                            | 🔄 Week 5 extension |
| Anomaly detection                | 🔄 Week 5 extension |
| Final project documentation      | 🔄 In progress      |
| Final cleanup/reproducibility    | 🔄 Planned          |
| Final technical presentation     | 🔄 Planned          |

---

# 27. Final Roadmap

The project roadmap from the beginning of the internship to the continuation phase is:

### Phase 1 — Foundations

**Weeks 1–2**

```text
Python
↓
NumPy / Pandas
↓
Statistics
↓
Data Understanding
↓
EDA
```

### Phase 2 — Machine Learning

**Weeks 3–4**

```text
Supervised Learning
↓
Model Comparison
↓
Evaluation
↓
Cross-Validation
↓
Feature Engineering
↓
Pipelines
↓
Hyperparameter Tuning
```

### Phase 2 → Phase 3 Transition

**Week 5**

```text
K-Means
↓
DBSCAN
↓
Hierarchical Clustering
↓
PCA
↓
t-SNE
↓
Anomaly Detection
↓
Project Planning
```

### Phase 3 — Continued Project Development

**Future Sprints**

```text
Refine Existing Cardiac Project
        ↓
Complete Unsupervised Analysis
        ↓
Integrate Results
        ↓
Improve Documentation
        ↓
Validate Reproducibility
        ↓
Prepare Final Deliverables
        ↓
Technical Demonstration
```

---

# 29. Final Planning Statement

The **Cardiac Patient Monitoring System** is being developed as a continuous project rather than as a newly selected project on Day 5.

The previous weeks established the foundation of the project through data preparation, exploratory analysis, supervised learning, model evaluation, feature engineering, pipelines, and hyperparameter tuning.

Week 5 extends this foundation by introducing unsupervised learning and dimensionality reduction. Day 5 formalizes the project direction by documenting the problem statement, scope, Definition of Done, backlog, acceptance criteria, risks, and future roadmap.

The project will therefore continue from its existing state rather than restarting from zero.

The main principle of the development plan is:

> **Each new concept learned during the internship should contribute to the same project whenever it is technically relevant, while maintaining a clear, reproducible, and curriculum-aligned machine learning workflow.**

The final goal is to produce an individually owned, well-documented, reproducible AI/ML project that demonstrates the complete progression from raw cardiac data to supervised prediction, rigorous evaluation, feature engineering, reusable pipelines, and unsupervised exploration.
