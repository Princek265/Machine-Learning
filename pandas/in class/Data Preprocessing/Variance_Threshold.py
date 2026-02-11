import pandas as pd
from sklearn.feature_selection import VarianceThreshold

# Step 1: Create a sample DataFrame

data = {
    'A': [1, 1, 1, 1, 1],
    'B': [0, 0, 0, 0, 0],
    'C': [10, 20, 30, 40, 50],
    'D': [5, 5, 5, 5, 5]
}

df = pd.DataFrame(data)
# Step 2: Display the original DataFrame
print("Original DataFrame:")
print(df)

# Step 3: Show Variance of Each Feature/Column
print("\nVariance of each feature:")
print(df.var())

# Step 4: Apply Variance Threshold
selector = VarianceThreshold(threshold=0.5)

df_selected = selector.fit_transform(df)

# Step 5: Show selected features
print("\nDataFrame after applying Variance Threshold:")
selected_features = df.columns[selector.get_support()]
print("Selected features based on variance threshold:")
print(selected_features)

# Step 6: Show Final Dataset

print("\nTransformed Dataset:")
print(df_selected)
