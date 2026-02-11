import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Sample data
data = pd.read_csv("./DataSets/Salary_Dataset_DataScienceLovers.csv")
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
plt.scatter(df['Rating'], df['Salary'])
plt.show()
# Create Scaller Object
# scaler = MinMaxScaler()
# Apply Scalling
# scaled_data = scaler.fit_transform(df)
# # Convert back to DataFrame
# # columns=df.columns  Takes column names from original DataSet
# scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

scaler = MinMaxScaler()

cols_to_scale = ['Rating','Salary']
    
df_scaled = df.copy()
df_scaled[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
print("\nMin-Max Scaled DataFrame:")
print(df_scaled)
plt.scatter(df_scaled['Rating'], df_scaled['Salary'],color='red')
plt.show()

print(df_scaled[['Rating','Salary']].head())
