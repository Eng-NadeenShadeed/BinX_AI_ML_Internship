# Week 1 - Python & Data Science Foundations

##  Overview

Week 1 of the BinX Tech AI & ML Internship (400-hour program) - 5 days covering the complete foundation needed before moving into classical machine learning: environment setup, core Python programming, NumPy, Pandas, and Matplotlib.

Each day includes a detailed learning notebook, an official Hands-On Lab (except Day 5, replaced by an integrated mini-project), and a per-day README.

---

##  Repository Structure

```text
Week1/
├── Day 1/
│   ├── day1_environment_setup.ipynb
│   └── README.md
├── Day 2/
│   ├── day2_python_fundamentals.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 3/
│   ├── data/
│   │   └── weekly_evaluations.csv
│   ├── day3_numpy.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 4/
│   ├── data/
│   │   └── melb_data.csv
│   ├── day4_pandas.ipynb
│   ├── Hands_On_Lab.ipynb
│   └── README.md
├── Day 5/
│   ├── day5_matplotlib.ipynb
│   └── README.md
├── Week1_Mini_Project/
│   ├── data/
│   │   └── Student_performance_data__.csv
│   ├── week1_mini_project.ipynb
│   └── README.md
└── README.md
```

---

#  Day-by-Day Breakdown

## Day 1 - Environment Setup

Set up a reproducible Python environment (venv, pip, requirements.txt) and the Jupyter Notebook workflow. Diagnosed and fixed a VS Code kernel misconfiguration (kernel wasn't linked to the project's .venv). Initialized Git and made the first commit.

**Tools:** Python 3.10+, venv, Jupyter, VS Code, Git & GitHub

---

## Day 2 - Python Fundamentals

Core data types, control flow (if/elif/else, while/for), functions (parameters, defaults, docstrings), list comprehensions, and OOP - both basics (classes, `__init__`, `self`, attributes, methods, class vs. instance variables) and advanced concepts (inheritance, polymorphism, encapsulation, abstraction) explored through ML-relevant examples.

**Hands-On Lab:** A `number_stats` function (mean/min/max as a dict), a for-loop rewritten as a list comprehension, and a `DataRecord` class with two attributes and a `display()` method.

---

## Day 3 - NumPy

Why NumPy matters (speed vs. plain Python lists), ndarray basics, array creation (`array`, `zeros`, `ones`, `arange`, `linspace`, `logspace`, `eye`, `random`), attributes (`ndim`, `shape`, `size`, `dtype`), element-wise operations, 1D/2D indexing and slicing (including the critical view-vs-copy distinction), boolean and fancy indexing, broadcasting, statistical/math functions, linear algebra basics (transpose, dot product, inverse, determinant, eigenvalues), matrix multiplication vs. element-wise multiplication, flatten/ravel, the axis concept, and random seeds for reproducibility.

**Hands-On Lab:** Built a 4×4 array, extracted a column and row via slicing, filtered values above the mean with a boolean mask, and added a row to every row of a matrix via broadcasting with manual verification.

---

## Day 4 - Pandas

Series (creation, the attribute-vs-method distinction, all 10 core attributes, `.loc`/`.iloc`, slicing rules, boolean and fancy indexing) and DataFrame (creation, inspection, column/row selection, `.at`/`.iat`, boolean filtering with `isin()`/`between()`/`query()`/`where()`/`mask()`, missing-value and duplicate handling, type conversion, and `groupby`/`agg`).

**Hands-On Lab:** Used the Melbourne Housing Snapshot dataset (13,580 rows) - reported shape/dtypes, counted missing values, filtered houses priced above $1M (found Southern Metropolitan dominates), and grouped by region to compare average prices (~3.5x gap between highest and lowest).

---

## Day 5 - Matplotlib

Why visualization matters for EDA, plot anatomy (Figure, Axes, Axis, Title, Labels, Legend), the four required plot types (line, scatter, bar, histogram) plus bonus types (pie, box plot, heatmap), and subplots.

**Deliverable:** No separate Hands-On Lab - by mentor request, the practical work was folded into the Week 1 Mini-Project below.

---

## Week 1 Mini-Project - Student Performance Analysis

An integrated capstone combining every skill from the week on a real dataset (2,392 students): loaded and verified clean data (Pandas), wrote a custom function to categorize GPA into performance bands (Python), computed GPA z-scores (NumPy), grouped by tutoring and parental support (Pandas), and built three labeled visualizations with interpretations (Matplotlib).

See `Week1_Mini_Project/README.md` for full details and findings.

---

#  Tools & Technologies Used

- Python 3.10+
- venv
- pip
- Jupyter Notebook
- VS Code
- Git & GitHub
- NumPy
- Pandas
- Matplotlib

---

#  Resources Used

- Official BinX Tech course materials
- *Python for Data Analysis* (Wes McKinney)
- Boot.dev/ThePrimeagen Git & GitHub course
- GeeksforGeeks articles
- Kaggle datasets
  - Melbourne Housing Snapshot
  - Student Performance Data

---

#  Progress

- [x] Day 1 - Environment Setup
- [x] Day 2 - Python Fundamentals
- [x] Day 3 - NumPy
- [x] Day 4 - Pandas
- [x] Day 5 - Matplotlib
- [x] Week 1 Integrated Mini-Project