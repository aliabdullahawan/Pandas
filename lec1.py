import pandas as pd

"""
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
Used for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series.
Pandas is a Python library that provides data structures and data analysis tools. It is built on top of the NumPy library and is designed to work seamlessly with it. 
Pandas is widely used in data science, machine learning, and data analysis tasks.   
Pandas is the Ms-Excel of Python. It is used for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series.
"""

# ---------------------------------------------------------------------------------------------------------------------

""""
-- SERIES --
Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
The axis labels are collectively referred to as the index. A Series is like a fixed-size dictionary in that you can get and set values by index label. 
A Series can be created from a list or array, or from a dictionary.
"""

"""
print(pd.__version__)  # Print the version of pandas

data_series = [1, 2, 3, 4, 5]
series = pd.Series(data_series, index=['a', 'b', 'c', 'd', 'e'])
print(series)

# loc mean location by value
print(series.loc['a'])  # Accessing the value at index 'a'
series.loc["f"] = 6  # Adding a new value to the series
print(series)
series.loc["a"] = 10  # Modifying the value at index 'a'
print(series)
series.loc["a":"c"] = 20  # Modifying the values from index 'a' to 'c'
print(series)
series = series.loc[['a', 'c', 'e']]  # Accessing the values at index 'a', 'c', and 'e'
print(series)

# iloc mean location by index
print(series.iloc[0])  # Accessing the value at index 0

print(series.iloc[0:3])  # Accessing the values from index 0 to 2
print(series.iloc[[0, 2, 4]])  # Accessing the values at index 0, 2, and 4
print(series[series > 3])  # Accessing the values greater than 3

calories = {
    "day1": 420, 
    "day2": 380, 
    "day3": 390
}
series2 = pd.Series(calories)
print(series2)
"""

# ---------------------------------------------------------------------------------------------------------------------

"""
-- DATA FRAME --
DataFrame is a two-dimensional labeled data structure with columns of potentially different types.
You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
It is generally the most commonly used pandas object.
Like Series, DataFrame accepts many different kinds of input:
Dict of 1D ndarrays, lists, dicts, or Series
2-D numpy.ndarray
Structured or record ndarray
A Series
Another DataFrame
"""


data_frame = {
    "calories": [420, 380, 390], 
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data_frame, index=["day1", "day2", "day3"])
print(df)

print(df.loc["day1"])  # Accessing the row with index 'day1'
print(df.loc[["day1", "day2"]])
print(df.loc["day1":"day2"])

print(df.iloc[0])  # Accessing the first row
print(df.iloc[0:2])  # Accessing the first two rows

print(df["calories"])  # Accessing the 'calories' column
print(df.calories)  # Accessing the 'calories' column
print(df[["calories", "duration"]])  # Accessing the 'calories' and 'duration' columns
print(df[df["calories"] > 380])  # Accessing the rows where 'calories' is greater than 380

df["calories"] = df["calories"] + 10  # Modifying the 'calories' column
print(df)
df["protein"] = [10, "N/A", 30]  # Adding a new column 'protein'
print(df)
df.drop("protein", axis=1, inplace=True)  # Dropping the 'protein' column
print(df)
df.drop("day1", axis=0, inplace=True)  # Dropping the 'day1' row
print(df)

new_row = pd.DataFrame({"calories": [400], "duration": [60]}, index=["day4"])
df = pd.concat([df, new_row])  # Adding a new row 'day4
print(df)
new_row = pd.DataFrame({"calories": 450, "duration": 70}, index=["day5"])
df = pd.concat([df, new_row])  # Adding a new row 'day5'
print(df)









