import pandas as pd


# Reading CSV

df_csv =  pd.read_csv("Pokemon.csv")
print(df_csv)

print(df_csv.head(5))  # Displaying the first 5 rows of the DataFrame
print(df_csv.tail(5))  # Displaying the last 5 rows of the DataFrame
print(df_csv.to_string())  # Displaying the entire DataFrame

# Reading JSON

df_json = pd.read_json("Pokemon.json")
print(df_json)

print(df_json.head(5))  # Displaying the first 5 rows of the DataFrame
print(df_json.tail(5))  # Displaying the last 5 rows of the DataFrame
print(df_json.to_string())  # Displaying the entire DataFrame


# ---------- Working with CSV ----------


## Selection by Columns

print(df_csv["Name"].to_string())  # Accessing the 'Name' column
print(df_csv[["Name", "Type1"]])  # Accessing the 'Name' and 'Type 1' columns
print(df_csv.Name)  # Accessing the 'Name' column)
print(df_csv.iloc[::, 0])  # Accessing the first column
print(df_csv.iloc[::, [0, 1]])  # Accessing the first and second columns
print(df_csv.iloc[::, ::-1])  # Accessing all columns in reverse order
print(df_csv.iloc[::, 0:5])  # Accessing the first 5 columns

## Selection by Rows

print(df_csv.iloc[0:5])  # Accessing the first 5 rows
print(df_csv.iloc[0])  # Accessing the first row
print(df_csv.iloc[0:5])  # Accessing the first 5 rows
print(df_csv.loc[0])  # Accessing the first row
print(df_csv.loc[0:5])  # Accessing the first 5 rows
print(df_csv.loc[df_csv["Type1"] == "Grass"])  # Accessing the rows where 'Type 1' is 'Grass'

## Selection by Rows and Columns

print(df_csv.iloc[0:5, 0:5])  # Accessing the first 5 rows and first 5 columns
print(df_csv.loc[0:5, "Name"])  # Accessing the 'Name' column for the first 5 rows
print(df_csv.loc[0:5, ["Name", "Type1"]]) # Accessing the 'Name' and 'Type 1' columns for the first 5 rows
print(df_csv.loc[df_csv["Type1"] == "Grass", ["Name", "Type1"]]) # Accessing the 'Name' and 'Type 1' columns for the rows where 'Type 1' is 'Grass'
print(df_csv.loc[df_csv["Type1"] == "Grass", ["Name", "Type1"]].head(5)) # Accessing the 'Name' and 'Type 1' columns for the first 5 rows where 'Type 1' is 'Grass'
print(df_csv.loc[::-1, ::-1].to_string()) # Accessing all rows and columns in reverse order

# Making the 'Name' column the index of the DataFrame

df_csv =  pd.read_csv("Pokemon.csv", index_col="Name") ## Here we are setting the index column to be the 'Name' column of the DataFrame 
print(df_csv)

print(df_csv.loc["Bulbasaur"])  # Accessing the row with index 'Bulbasaur'  
print(df_csv.loc[["Bulbasaur", "Ivysaur"]])  # Accessing the rows with index 'Bulbasaur' and 'Ivysaur'

print(df_csv.loc["Bulbasaur":"Ivysaur"])  # Accessing the rows from index 'Bulbasaur' to 'Ivysaur'
print(df_csv.loc["Charizard", ["Height", "Weight"]])  # Accessing the 'Height' and 'Weight' columns for the row with index 'Charizard'
print(df_csv.loc["Charizard", ["Height", "Weight"]])  # Accessing the 'Height' and 'Weight' columns for the row with index 'Charzard'


# Taking user input to access a specific Pokémon's data
pokemon = input("Enter a Pokémon name: ")
try:
    print(df_csv.loc[pokemon])  # Accessing the row with index equal to the user input
except KeyError:
    print(f"{pokemon} not found in the DataFrame.")




# ------------------------------------------------------------------------------------------------------------------------
# See all unique Pokémon names (first 20 for example)
print(df_csv.index.unique()[:20])

# Or search for names containing "Char"
print(df_csv.index[df_csv.index.str.contains("Char")])
print(df_csv.columns.tolist())