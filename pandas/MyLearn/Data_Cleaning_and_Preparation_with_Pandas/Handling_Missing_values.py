# Handling Missing Values
import pandas as pd
import numpy as np
# Create a DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, None, 30, 22],
    "Salary": [50000, 60000, np.nan, 45000]
}

df = pd.DataFrame(data)

df = df.dropna() # Drop rows with missing values
df = df.dropna(axis=1) # Drop columns with missing values

# df["column_name"] = df["column_name"].fillna(df["column_name"].mean()) # Fill missing values with mean of the column

df["salary"] = df["Salary"].fillna(0) # Fill missing values with a specific value

df.fillna(method='ffill') # Fill missing values using forward fill method (propagate last valid observation forward)
df.fillna(method='bfill') # Fill missing values using backward fill method (propagate next valid observation backward)

df["Salary"] = df["Salary"].interpolate() # Fill missing values using interpolation (linear by default)