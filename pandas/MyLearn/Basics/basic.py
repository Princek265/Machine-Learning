import pandas as pd
 # Basic usage of pandas
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

data = {
    "Name" : ["Alice", "Bob"],
    "Age" : [25, 30]    
    }
df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())

# Gives summary of DataFrame including data types and non-null counts
print(df.info())
# Provides statistical summary of numerical columns in the DataFrame
print(df.describe())

print(df[["Name","Age"]])

# Filtering rows based on a condition
print(df[df["Age"] > 25])

# Accessing a specific row using iloc
print(df.iloc[0]) # 1st row

# Accessing a specific column using iloc
print(df.iloc[:,0]) # 1st column

# Selecting By Label using loc
print(df.loc[0])

# Selecting a specific column using loc
print(df.loc[:, "Name"])

