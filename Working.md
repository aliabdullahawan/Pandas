# Pandas Study Hub

This folder is a compact Pandas learning path. The lecture files move from Series and DataFrame basics to reading files, indexing, selection, summary statistics, cleaning, and string-based transformations.

## Start Here

1. Read the lecture files in order from `lec1.py` to `lec4.py`.
2. Run each script so you can see the printed results.
3. Rework the examples by hand to make the concepts stick.
4. Use `PracticeQuestions.md` after a few lessons to test yourself.
5. Open the cheat-sheet PDFs when you want a quick syntax reference.

## What Each Lecture Covers

| File      | Main Topic |
| --------- | ---------- |
| `lec1.py` | Pandas basics, `Series`, `DataFrame`, indexing with `loc` and `iloc`, selecting columns and rows, adding and dropping columns, and combining rows with `concat`. |
| `lec2.py` | Reading CSV and JSON files, column and row selection, using `index_col`, filtering rows, and exploring `Index` values. |
| `lec3.py` | Summary statistics such as `mean`, `sum`, `max`, `min`, `std`, `var`, `median`, `mode`, `quantile`, `count`, `describe`, `value_counts`, and grouped aggregation. |
| `lec4.py` | Data cleaning and transformation, including `dropna`, `fillna`, `replace`, string methods, type conversion, sorting, and duplicates. |
| `trick.py` | Common Pandas utility patterns such as sorting, concatenation, uniqueness, reshaping, cumulative operations, filtering helpers, and set-style operations. |

## Core Ideas In One Place

### 1) Series And DataFrames

Pandas revolves around two core objects:

- `Series` for one-dimensional labeled data
- `DataFrame` for tabular data with rows and columns

The early lessons focus on creating both objects, reading values by label or position, and editing columns safely.

### 2) Indexing And Selection

The most important access patterns are:

- `loc` for label-based selection
- `iloc` for position-based selection
- selecting one column, multiple columns, or filtered rows
- setting a column as the index when that makes lookups easier

### 3) Loading Data

Reading files is the normal starting point for real Pandas work. The lessons cover:

- `read_csv`
- `read_json`
- viewing the first and last rows with `head()` and `tail()`
- working with file-backed data instead of hand-built examples

### 4) Summary Statistics

The third lesson focuses on the common descriptive operations you use constantly:

- central tendency like mean and median
- spread like standard deviation and variance
- minimum and maximum values
- percentiles and counts
- `describe()` for quick overview reporting
- `groupby()` for grouped aggregation

### 5) Cleaning And Transformation

The cleaning lesson covers the practical edits you need on messy data:

- removing missing values with `dropna`
- filling missing values with `fillna`
- replacing values with `replace`
- converting text with string methods
- changing data types with `astype`
- sorting and removing duplicates

### 6) Utility Patterns And Tricks

The new `trick.py` file is meant for small reusable patterns that are easy to forget but useful in exercises:

- sorting and concatenating data
- checking uniqueness and membership
- expanding or reshaping data
- cumulative operations like `cumsum`
- summary helpers like `percentile`, `histogram`, `corr`, and `cov`
- clipping values and using set-like operations

## Practice Question Themes

The practice sheet is organized around the same Pandas skills, but in problem form.

### DataFrame Construction And Selection

- building DataFrames from dictionaries
- filtering rows with conditions
- selecting rows and columns with `loc` and `iloc`
- sorting with multiple keys

### Cleaning And Feature Building

- filling missing data
- replacing values
- ranking and grouping
- creating new columns from existing data

### String And Time Series Work

- lowercasing and extracting text parts
- working with dates and resampling
- cumulative statistics and rolling values
- shifting, differences, and percentage change

### Combining And Reshaping

- merging DataFrames
- pivot tables
- melting wide data back into long form
- crosstabs and summary tables

## Cheat-Sheet References

The PDF files in this folder are quick-reference Pandas cheat sheets. They reinforce the same core material used throughout the lectures:

- importing Pandas as `pd`
- creating Series and DataFrames
- reading CSV and JSON files
- indexing, filtering, sorting, grouping, and cleaning

## Study Workflow

If you want the fastest progress, use this loop:

1. Read one lecture file.
2. Run it.
3. Predict the output before you look.
4. Change the values and rerun.
5. Solve a few practice questions from the matching topic.
6. Review the cheat-sheet PDFs when you need a syntax reminder.

## Quick Reminders

- Prefer vectorized Pandas operations over Python loops when possible.
- Use `loc` for label-based filtering and assignment.
- Use `iloc` for position-based slicing.
- Use `groupby()` when you want summaries by category.
- Use `fillna()`, `dropna()`, and `replace()` early when cleaning data.

## Current Focus

The current focus is `lec4.py` and `trick.py`, which extend the course into cleaning, string operations, sorting, and compact utility patterns.
