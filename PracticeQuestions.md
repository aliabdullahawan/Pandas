# Pandas Practice Questions

## 1. Create a DataFrame from a dictionary

```python
data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
	'Age': [25, 30, 35, 40, 28],
	'City': ['NY', 'LA', 'NY', 'SF', 'LA'],
	'Salary': [70000, 80000, 120000, 110000, 95000]
}
```

Create a DataFrame from `data` and:

- Set the `Name` column as the index.
- Print the first 3 rows.

## 2. Filter rows by condition

From the DataFrame above, select only the rows where `Age > 30` and `City == 'NY'`.

## 3. Add a new column

Add a column `Bonus` that is 10% of the `Salary` column.

## 4. Group and aggregate

Using the same DataFrame, group by `City` and compute:

- Average `Age`
- Total `Salary`
- Number of employees (`size`)

## 5. Handle missing data

Create a DataFrame like this:

```python
df = pd.DataFrame({
	'A': [1, 2, np.nan, 4],
	'B': [5, np.nan, np.nan, 8],
	'C': [10, 11, 12, 13]
})
```

- Fill all NaN values with the mean of their respective column.
- Then drop any rows that still have missing values.

## 6. Apply a function column-wise

Create a DataFrame with a column `sentence`:

```python
sentences = ["Pandas is great", "I love data science", "Python rocks"]
```

Convert every sentence to title case and count the number of words in each. Store the results in new columns `title_case` and `word_count`.

## 7. Date range and resample

Generate a DateTimeIndex from `2024-01-01` to `2024-01-10` with hourly frequency. Create a DataFrame with a column `value` filled with random integers between 10 and 100. Resample the data to daily frequency, taking the maximum value for each day.

## 8. Merge two DataFrames

```python
df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['A', 'B', 'C', 'D']})
df2 = pd.DataFrame({'id': [2, 3, 4, 5], 'score': [90, 85, 88, 92]})
```

Perform an outer join on `id` and fill missing scores with `0`.

## 9. Pivot table

Given a DataFrame `sales`:

```python
sales = pd.DataFrame({
	'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
	'Product': ['Apple', 'Banana', 'Apple', 'Banana'],
	'Revenue': [100, 200, 150, 250]
})
```

Create a pivot table showing `Product` as rows, `Date` as columns, and `Revenue` as values. Fill any missing combinations with `0`.

## 10. Melt (unpivot)

Take the pivoted table from exercise 9, or a similar wide DataFrame, and melt it back into long format so there are columns: `Product`, `Date`, `Revenue`.

## 11. Sort by multiple columns

Sort the original employee DataFrame from exercise 1 by `City` ascending and then by `Salary` descending. After sorting, reset the index and drop the old index.

## 12. String operations

Create a DataFrame:

```python
df = pd.DataFrame({'email': ['Alice@Example.com', 'bob@test.org', 'CHARLIE@DOMAIN.COM']})
```

- Convert all emails to lowercase.
- Extract the domain part, the string after `@`.

## 13. Cumulative statistics

Create a DataFrame with a column `sales` of 20 random integers between 50 and 200. Add columns:

- `cum_sum` for cumulative sum of sales
- `cum_max` for cumulative maximum
- `rolling_avg` for a 3-period rolling average

## 14. Replace values

In the employee DataFrame, replace all occurrences of `NY` with `New York` and `LA` with `Los Angeles` in the `City` column.

## 15. Rank values

Add a column `rank` to the employee DataFrame that ranks employees by `Salary` so that the highest salary gets rank `1`. Use the `dense` method so that ties get the same rank and the next rank is not skipped.

## 16. Cut into bins

Create a Series of 50 random ages between 18 and 80. Use `pd.cut` to bin them into categories:

- `Young` for 18-35
- `Middle-aged` for 36-55
- `Senior` for 56-80

Count how many people fall into each bin.

## 17. Time series shift and difference

Create a Series indexed by 20 consecutive business days, with values equal to the cumulative sum of random integers from -2 to 2, starting with 100. Calculate the day-over-day change using `diff()` and the percentage change using `pct_change()`.

## 18. Cross-tabulation

Given a DataFrame of survey responses:

```python
data = pd.DataFrame({
	'Gender': ['M', 'F', 'F', 'M', 'F', 'M'],
	'Voted': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
})
```

Create a cross-tabulation showing counts of `Voted` by `Gender`, with row and column totals.

## 19. Read CSV and explore

Assume you have a file `data.csv` with columns `['date', 'value', 'category']`.

- Read it, parsing the `date` column as datetime and using it as the index.
- Show summary statistics for each `category` using `groupby` and `describe`.

## 20. Multiple filter and assign

From the employee DataFrame, select employees whose salary is above the overall median salary. For those selected, increase their salary by 5% and add a column `high_earner = True`. Return the whole DataFrame with the updated values while leaving the others unchanged.
