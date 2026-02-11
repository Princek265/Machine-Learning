import pandas as pd
import numpy as np
# This kind Questions will be there in CA 1
# Create a sample DataFrame with missing and duplicate values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Judy'],
    'Age': [24, 27, 22, np.nan, 29, 35, 26, np.nan, 28, 31],
    'Salary': [50000, np.nan, 58000, 60000, 52000, 65000, 56000, 62000, np.nan, 61500],
    'Experience': [np.nan, 3, 1, 5, 4, 7, np.nan, 6.5, 3.5, 7.5]
}

df = pd.DataFrame(data)

# Check missing values
print("Missing values in each column:")
print(df.isnull().sum())
# print(df.isna().sum())

# Check duplicate values
print("\nDuplicate rows in the DataFrame:")
print(df.duplicated().sum())

# Replace duplicate values with mean of the column

# df['Age'].fillna(df['Age'].mean(), inplace=True) # wrong way

# correct way
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Experience'] = df['Experience'].fillna(df['Experience'].mean())
print("\nDataFrame after handling missing values:")
print(df)

# Change salary column name with other name

df.rename(columns={'Salary': 'Income'}, inplace=True)

# Add one more Column 

df['Department'] = ['IT', 'HR', 'Finance', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance']

# Check any of Age value is greater than 30

print("\nEmployees with Age greater than 30:")
print(df[df['Age'] > 30])