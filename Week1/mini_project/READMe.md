# Week 1 Mini-Project: Student Performance Analysis

##  Overview

This project brings together everything learned across **Week 1** - Python fundamentals, NumPy, Pandas, and Matplotlib - into a single, real-world data analysis pipeline.

Instead of a separate Hands-On Lab for **Day 5**, this integrated project (requested by the mentor) demonstrates how all four libraries work together in practice: loading a real dataset, cleaning it, engineering a new feature, computing a numeric statistic, grouping data to compare subgroups, and visualizing the results.

---

##  Dataset

- **Source:** Student Performance Dataset (Kaggle)
- **File:** `data/Student_performance_data__.csv`
- **Size:** 2,392 students, 15 columns

| Column | Description |
|--------|-------------|
| StudentID | Unique student identifier |
| Age, Gender, Ethnicity | Demographic information |
| ParentalEducation | Encoded parental education level (0–4) |
| StudyTimeWeekly | Hours spent studying per week |
| Absences | Number of absences |
| Tutoring | Whether the student receives tutoring (0/1) |
| ParentalSupport | Encoded level of parental support (0–4) |
| Extracurricular, Sports, Music, Volunteering | Activity participation flags |
| GPA | Grade Point Average (0–4 scale) |
| GradeClass | Encoded overall grade classification |

The dataset arrived fully clean with:

- **0 missing values**
- **0 duplicate rows**
- **2,392 total records**

---

##  Pipeline & Skills Applied

| Step | What We Did | Library / Skill (Week 1 Day) |
|------|-------------|------------------------------|
| **1–2** | Imported Pandas and loaded the CSV into a DataFrame | Pandas (Day 4) |
| **3** | Inspected shape, data types, `.describe()`, and column names | Pandas (Day 4) |
| **4** | Verified 0 missing values and 0 duplicate rows | Pandas Cleaning (Day 4) |
| **5** | Wrote a custom function (`categorize_performance`) using `if/elif/else` to classify GPA into performance bands, then applied it with `.apply()` | Python Functions & Control Flow (Day 2) |
| **6** | Computed each student's GPA z-score using `np.mean()` and `np.std()` | NumPy (Day 3) |
| **7** | Used `.groupby()` to compare average GPA by tutoring status and parental support level | Pandas GroupBy (Day 4) |
| **8** | Built three labeled visualizations: Histogram (GPA distribution), Scatter Plot (Study Time vs GPA), and Bar Chart (Average GPA by Tutoring) | Matplotlib (Day 5) |
| **9** | Summarized findings in a final Markdown cell | Documentation |

---

##  Key Findings

- **GPA Distribution:** Most students cluster in the lower-middle range:
  - **848** students are **At Risk** (GPA < 1.5)
  - **838** students are **Average** (1.5–2.5)
  - Only **77** students reach the **Excellent** category (3.5+)

- **Study Time Matters:** The scatter plot shows a visible upward trend—students who study more hours per week generally achieve higher GPAs, although there is noticeable variation.

- **Tutoring Helps:** Students receiving tutoring have an average GPA of **2.11**, compared with **1.82** for students without tutoring.

- **Parental Support Matters:** Average GPA increases steadily from **1.54** (no support) to **2.19** (very high support), showing a clear positive relationship.

---

##  Project Structure

```text
Week1_Mini_Project/
├── data/
│   └── Student_performance_data__.csv
├── week1_mini_project.ipynb
└── README.md
```

---

##  How to Run

1. Activate the project's virtual environment (`.venv`).
2. Open `week1_mini_project.ipynb` in **Jupyter Notebook** or **Visual Studio Code**.
3. Select the `.venv` Python kernel.
4. Run all notebook cells from top to bottom.

> **Note:** Ensure that **Pandas**, **NumPy**, and **Matplotlib** are already installed (for example, using the project's `requirements.txt`).
