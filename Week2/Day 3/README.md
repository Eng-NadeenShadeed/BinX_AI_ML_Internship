# Week 2 - Day 3: Linear Algebra for Machine Learning

## Overview

Focused on the mathematical foundations of linear algebra used in Machine Learning, including vectors, matrices, dot products, and matrix multiplication.

The day focused on understanding how ML models represent data internally and how predictions are computed using vector and matrix operations.

---

## Files

- `day3_linear_algebra.ipynb` — detailed notes, mathematical explanations, worked examples, visualizations, and NumPy implementations.
- `Hands_On_Lab.ipynb` — practical exercises implementing vectors, matrices, dot products, and ML-style predictions.

---

## Topics Covered

### Linear Algebra Foundations for ML

- Why linear algebra is the language of Machine Learning
- How datasets are represented mathematically
- Relationship between:
  - Features
  - Samples
  - Parameters (weights)
  - Predictions

### Vectors

- Definition of vectors
- Representing a single ML sample as a vector
- Feature vectors in Machine Learning

Example:
[age, income, experience]


- Vector dimensions and interpretation
- Creating and manipulating vectors using NumPy

### Matrices

- Definition of matrices
- Representing complete datasets as matrices
- Matrix shape:
  - Rows → Samples
  - Columns → Features

Covered:

- Creating matrices using NumPy
- Understanding matrix dimensions
- Accessing matrix elements
- Inspecting shapes

Example:
(samples × features)


### Dot Product

- Mathematical definition of dot product
- Element-wise multiplication and summation
- Understanding dot product as the core operation behind ML predictions

Covered:

- Manual dot product calculation
- NumPy implementation using `np.dot()`
- Feature vector × weight vector relationship

ML Connection:


Prediction = features · weights + bias


Understanding dot products as the operation behind models such as:

- Linear Regression
- Logistic Regression

### Matrix Multiplication

- Difference between dot product and matrix multiplication
- Matrix multiplication as multiple dot products
- Shape compatibility rules

Covered:

- Matrix multiplication using:
  - `np.matmul()`
  - `@` operator
- Understanding input and output shapes
- Debugging shape mismatch errors

ML Connection:

- Generating predictions for multiple samples at once
- Batch prediction in Machine Learning models

Example:
(samples × features) @ (features × weights)


---

## Hands-On Lab

Implemented and verified linear algebra operations used in Machine Learning:

- Created a dataset represented as a NumPy matrix.
- Represented individual samples as feature vectors.
- Calculated a dot product manually and verified the result using NumPy.
- Applied matrix multiplication to generate predictions for multiple samples simultaneously.
- Created and analyzed a shape mismatch error to understand matrix dimension rules.

All operations were verified using NumPy and connected to real ML prediction workflows.

---

## Libraries Used

- NumPy
- Jupyter Notebook

---

## Skills Practiced

- Representing ML data using vectors and matrices
- Understanding matrix shapes and dimensions
- Performing vector operations with NumPy
- Computing dot products
- Applying matrix multiplication
- Understanding how ML models calculate predictions internally
- Debugging shape mismatch errors
- Connecting mathematical concepts to Machine Learning algorithms