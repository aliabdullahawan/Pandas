import pandas as pd
import numpy as np

df = pd.read_csv("Pokemon.csv")
print(df)


# Most importand part in the pandas is the data cleaning and data transformation. In this file we will learn about the data cleaning and data transformation in pandas.


# -- DATA CLEANING --

df = df.drop(columns=["Height", "No"]) # Dropping the 'Height' and 'No' columns from the DataFrame
df = df.dropna(subset=["Type2"]) # Dropping all rows with NULL values in the 'Type 2' column

df = df.fillna(0)  # Filling all NULL values with 0
df = df.fillna({"Type2": np.random.randint(1, 10)})  # Filling all NULL values in the 'Type 2' column with a random integer between 1 and 10


# -- DATA TRANSFORMATION --

df["Type1"] = df["Type1"].replace("Grass", "Plant")  # Replacing all occurrences of 'Grass' with 'Plant' in the 'Type 1' column
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE"})  # Replacing all occurrences of 'Grass' with 'GRASS' and 'Fire' with 'FIRE' in the 'Type 1' column


# -- STRING OPERATIONS --

df["Name"] = df["Name"].str.upper()  # Converting all values in the 'Name' column to uppercase
df["Name"] = df["Name"].str.lower()  # Converting all values in the 'Name' column to lowercase
df["Name"] = df["Name"].str.title()  # Converting all values in the 'Name' column to title case
df["Name"] = df["Name"].str.capitalize()  # Converting all values in the 'Name' column to capitalize case
df["Name"] = df["Name"].str.swapcase()  # Swapping the case of all values in the 'Name' column
df["Name"] = df["Name"].str.strip()  # Removing leading and trailing whitespace from all values in the 'Name' column
df["Name"] = df["Name"].str.lstrip()  # Removing leading whitespace from all values in the 'Name' column
df["Name"] = df["Name"].str.rstrip()  # Removing trailing whitespace from all values in the 'Name' column


# -- DATA TYPES --

df["Legendary"] = df["Legendary"].astype(int)  # Converting the 'Legendary' column to integer type
df["Legendary"] = df["Legendary"].astype(str)  # Converting the 'Legendary' column to string type
df["Legendary"] = df["Legendary"].astype(bool)  # Converting the 'Legendary' column to boolean type
df["Legendary"] = df["Legendary"].astype(float)  # Converting the 'Legendary' column to float type


# -- SORTING --

df = df.sort_values(by="Name", ascending=False)  # Sorting the DataFrame by the 'Name' column in descending order
df = df.sort_values(by="Name")  # Sorting the DataFrame by the 'Name' column


# -- UNIQUE VALUES and REMOVING DUBLICATES --

df = df["Name"].unique() # Getting all unique values from the 'Name' column
df = df["Name"].nunique() # Getting the number of unique values in the 'Name' column
df = df.drop_duplicates() # Dropping all duplicate rows from the DataFrame







# -- They aree not working I make mistake in the code below and don't know what the error is  --


"""
data1 = df.dropna(inplace=True)  # Dropping all rows with any NULL values
data2 = df.dropna(inplace=False)  # Dropping all rows with any NULL values without modifying the original DataFrame
data3 = df.drop_duplicates(inplace=True)  # Dropping all duplicate rows
data4 = df.drop_duplicates(subset=["Name"], inplace=True)  # Dropping all duplicate rows based on the 'Name' column
data5 = df.dropna(inplace=True, subset=["Type1"])  # Dropping all rows with NULL values in the 'Type 1' column
data6 = df.fillna(0, inplace=True)  # Filling all NULL values with 0
data7 = df.fillna(df.mean(), inplace=True)  # Filling all NULL values with the mean of the column
data8 = df.fillna(df.median(), inplace=True)  # Filling all NULL values with the median of the column
data9 = df.fillna(df.mode().iloc[0], inplace=True)  # Filling all NULL values with the mode of the column
data10 = df.fillna(method="ffill", inplace=True)  # Filling all NULL values with the previous value
data11 = df.fillna(method="bfill", inplace=True)  # Filling all NULL values with the next value

df["Type1"].fillna("Unknown", inplace=True)  # Filling all NULL values in the 'Type 1' column with 'Unknown'
df["Type2"].fillna("Unknown", inplace=True)  # Filling all NULL values in the 'Type 2' column with 'Unknown'
df["Legendary"].fillna(False, inplace=True)  # Filling all NULL values in the 'Legendary' column with False
"""

