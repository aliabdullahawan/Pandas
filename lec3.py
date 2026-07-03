import pandas as pd

df = pd.read_csv("Pokemon.csv")
print(df)


print(df.mean(numeric_only=True))  # Calculating the mean of all numeric columns
print(df["Weight"].mean())  # Calculating the mean of the 'Attack' column
print(df["Weight"].sum())  # Calculating the sum of the 'Attack' column
print(df["Weight"].max())  # Calculating the maximum value of the 'Attack' column
print(df["Weight"].min())  # Calculating the minimum value of the 'Attack' column
print(df["Weight"].std())  # Calculating the standard deviation of the 'Attack' column
print(df["Weight"].var())  # Calculating the variance of the 'Attack' column
print(df["Weight"].median())  # Calculating the median of the 'Attack' column
print(df["Weight"].mode())  # Calculating the mode of the 'Attack' column
print(df["Weight"].quantile(0.25))  # Calculating the 25th percentile of the 'Attack' column
print(df["Weight"].quantile(0.5))  # Calculating the 50th percentile of the 'Attack' column
print(df["Weight"].count())  # Count does not include any NULL value. Counting the number of non-null values in the 'Attack' column    
print(df["Weight"].describe())  # Displaying the summary statistics of the 'Attack' column

print(df.describe())  # Displaying the summary statistics of all numeric columns
print(df.describe(include="all"))  # Displaying the summary statistics of all columns
print(df.describe(include=[object]))  # Displaying the summary statistics of all object columns
print(df.describe(include=[float]))  # Displaying the summary statistics of all float columns)
print(df.describe(include=[int]))  # Displaying the summary statistics of all integer columns
print(df.describe(include=[object, float]))  # Displaying the summary statistics of all object and float columns

print(df["Type1"].value_counts())  # Counting the occurrences of each unique value in the 'Type 1' column
print(df["Type1"].value_counts(normalize=True)) # Counting the occurrences of each unique value in the 'Type 1' column and normalizing it to percentage
print(df["Type1"].value_counts(normalize=True) * 100)  # Counting the occurrences of each unique value in the 'Type 1' column and normalizing it to percentage

print(df.describe())  # Displaying the summary statistics of all numeric columns
print(df.describe(include="all"))  # Displaying the summary statistics of all columns
print(df.describe(include=[object]))  # Displaying the summary statistics of all object columns
print(df.describe(include=[float]))  # Displaying the summary statistics of all float columns)
print(df.describe(include=[int]))  # Displaying the summary statistics of all integer columns
print(df.describe(include=[object, float]))  # Displaying the summary statistics of all object and float columns


group = df.groupby("Type1")  # Grouping the DataFrame by the 'Type 1' column
print(group.mean(numeric_only=True))  # Calculating the mean of all numeric columns for each group
print(group["Weight"].mean())  # Calculating the mean of the 'Attack' column for each group 
print(group["Weight"].sum())  # Calculating the sum of the 'Attack' column for each group
print(group["Weight"].max())  # Calculating the maximum value of the 'Attack' column for each group
print(group["Weight"].min())  # Calculating the minimum value of the 'Attack'
print(group["Weight"].count())  # Counting the number of non-null values in the 'Attack' column for each group






