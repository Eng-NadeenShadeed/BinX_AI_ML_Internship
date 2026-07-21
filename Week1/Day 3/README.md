## Day 3 - NumPy: Numerical Computing

### Overview

Covered NumPy, the numerical foundation of the Data Science and AI/ML stack. Work is split across two notebooks.

### Files

- `day3_numpy.ipynb` - detailed notes and worked examples for every concept covered
- `Hands_On_Lab.ipynb` - the four official required exercises

### Topics Covered

- Introduction to NumPy and why libraries exist
- `ndarray` basics: dimensions (0D/1D/2D), `ndim`, `shape`, `size`, `dtype`
- Array creation: `array`, `zeros`, `ones`, `arange`, `linspace`, `logspace`, `eye`, `random`
- Element-wise operations (array + scalar, array + array)
- Indexing and slicing (1D and 2D), including the view vs. copy distinction
- Boolean indexing and fancy indexing
- Broadcasting (including real-world examples: correction factors, normalization)
- Statistical and math functions (`mean`, `std`, `sum`, `sqrt`, `sort`, etc.)
- Linear algebra basics (transpose, dot product, inverse, determinant, eigenvalues)
- Matrix multiplication vs. element-wise multiplication
- `flatten` and `ravel`
- The `axis` concept
- Random seed for reproducibility

### Hands-On Lab

- Created a 4×4 array (values 1–16) and inspected its shape and `dtype`
- Extracted the second column and last row using slicing
- Filtered values greater than the array's mean using a boolean mask
- Added a 1D row to every row of a 2D array using broadcasting, with manual verification