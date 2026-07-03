import pandas as pd
import numpy as np


data = np.random.randint(low=1, high=50, size=(6, 4))
df = pd.DataFrame(data, columns=["A", "B", "C", "D"])
print(df)


# Sorting
df_sorted = df.sort_values(by="A", ascending=True)
print(df_sorted)


# Concatenation
df_extra = pd.DataFrame([[51, 52, 53, 54]], columns=["A", "B", "C", "D"])
df_appended = pd.concat([df, df_extra], axis=0, ignore_index=True)
print(df_appended)


# Adding a new column
df_with_new_col = df.copy()
df_with_new_col["E"] = np.ones(len(df_with_new_col))
print(df_with_new_col)


# Unique values and membership checks
values = pd.Series([10, 20, 20, 30, 40, 40, 50])
print(values.unique())
print(values.isin([20, 40]))


# Expanding dimensions style pattern using DataFrame construction
expanded_row = pd.DataFrame([df.iloc[0].values], columns=df.columns)
print(expanded_row)


# Cumulative sum
print(df.cumsum())


# Percentile and histogram style summaries
print(np.percentile(df.to_numpy(), 100))
print(np.histogram(df.to_numpy(), bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]))


# Correlation and covariance
print(df.corr(numeric_only=True))
print(df.cov(numeric_only=True))


# Flipping rows and columns
print(df.iloc[::-1])
print(df.iloc[:, ::-1])


# Using DataFrame.to_numpy() helpers
flat_values = df.to_numpy().ravel()
print(np.unique(flat_values))


# Clipping values
print(df.clip(lower=10, upper=30))


# Set-style operations on Series
set_one = pd.Series([1, 2, 3, 4, 5])
set_two = pd.Series([4, 5, 6, 7, 8])
print(pd.Index(set_one).union(set_two))
print(pd.Index(set_one).intersection(set_two))
print(pd.Index(set_one).difference(set_two))