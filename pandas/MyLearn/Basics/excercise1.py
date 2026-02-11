#https://raw.githubusercontent.com/seaborn-data/iris/master/iris.csv

# Exercise 1: Loading and Exploring the Iris Dataset
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Loading data from csv file
df = pd.read_csv(url)

# Exploring the DataFrame
# print("First 5 rows: \n", df.head())
# print("Last 5 rows: \n", df.tail())

print(df.info())
print(df.describe())

# Select speicific columns and filter rows

selected_columns = df[["species", "sepal_length"]]
print("Selected Columns :\n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows :\n", filtered_rows)
