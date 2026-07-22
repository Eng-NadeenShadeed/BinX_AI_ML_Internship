# Day 4 - Pandas: Tabular Data

## Overview

Covered Pandas in depth - both Series and DataFrame - going well beyond the official requirements, using multiple resources including *Python for Data Analysis* (Wes McKinney), GeeksforGeeks articles, and hands-on practice.

## Files

- `day4_pandas.ipynb` - detailed notes and worked examples for every concept covered
- `Hands_On_Lab.ipynb` - the official required exercises
- `data/melb_data.csv` - Melbourne Housing Snapshot dataset (from Kaggle)

## Topics Covered

### Series (in depth)

- Creation (from list, NumPy array, dict, scalar, range, with custom dtype/index/name)
- Attribute vs. Method distinction
- Core attributes:
  - `values`
  - `index`
  - `dtype`
  - `name`
  - `shape`
  - `size`
  - `ndim`
  - `axes`
  - `empty`
  - `hasnans`
- Label vs. position indexing (`.loc` vs. `.iloc`), slicing differences
- Boolean indexing and fancy indexing

### DataFrame

- Creating from dict, list of dicts, NumPy array, and Series
- Core attributes and inspection methods:
  - `head()`
  - `tail()`
  - `info()`
  - `describe()`
  - `memory_usage()`
- Selection:
  - Single/multiple columns
  - `.loc` / `.iloc`
  - Combined row + column selection
  - `.at` / `.iat`
- Boolean filtering:
  - Comparison operators
  - `&` / `|` / `~`
  - `isin()`
  - `between()`
  - `query()`
  - `where()` / `mask()`
  - Filtering missing values and strings
- Cleaning:
  - `isnull()`
  - `dropna()`
  - `fillna()` (mean / median / mode / constant / ffill / bfill)
  - `duplicated()` / `drop_duplicates()`
  - `astype()`
  - `replace()`
- GroupBy:
  - Basic aggregation
  - `.agg()` with multiple/per-column stats
  - Multi-column grouping
  - `size()` vs. `count()`
  - `.transform()`
  - `.filter()`

## Hands-On Lab

Used the Melbourne Housing Snapshot dataset (13,580 rows, 21 columns):

- Loaded the CSV and reported shape, columns, and dtypes.
- Counted missing values (found gaps in `Car`, `BuildingArea`, `YearBuilt`, `CouncilArea`) and documented handling approach.
- Filtered houses priced above `$1,000,000` and found **Southern Metropolitan** dominates this segment.
- Grouped by region to compare average prices, finding a ~3.5× difference between the highest and lowest regions.