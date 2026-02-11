import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sample data
data = {
    'Age': [18,25,30,45,60],
    'Salary': [20000,30000,40000,60000,80000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

plt.scatter(df['Age'], df['Salary'])
plt.show()

# Create Scaller Object
scaler = StandardScaler()

# Apply Scalling
scaled_data = scaler.fit_transform(df)

# Convert back to DataFrame
# columns=df.columns  Takes column names from original DataSet
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("\nStandardized DataFrame (Z-Score Scaling):")
print(scaled_df)
plt.scatter(scaled_df['Age'], scaled_df['Salary'],color='red')
plt.show()

