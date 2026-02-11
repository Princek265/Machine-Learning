# Data set students_performance.csv

# Objective: Ananlyze the factors influencing student performance 

# Tasks: 
# - Load and inspect the dataset
# - Handle missing values
# - Create total_score feature
# - Identify top and bottom performances
# - Visualize distributions and relationships

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./Datasets/student_performance.csv")
print(data.head()) # preview the first few rows
print(data.info()) # Basic info
print(data.describe()) # Initial data inspection
print(data.isnull().sum()) # Check for missing values

# Handle missing values by filling with mean for numerical columns
data.fillna(data.mean(numeric_only=True), inplace=True)

# Create a new feature 'total_score'
data['total_score'] = data[['Math', 'Physics', 'Chemistry']].sum(axis=1)
print(data.head())

# Identify top and bottom performers
top_performers = data.nlargest(5, 'total_score')
bottom_performers = data.nsmallest(5, 'total_score')
print("Top Performers:\n", top_performers)
print("Bottom Performers:\n", bottom_performers)

# renaming index column to Index for clarity
data.index.name = 'Index'
print(data.head())

# - Visualize distributions and relationships
plt.plot(data['total_score'], data['Attendance'])
plt.xlabel('Total Score')
plt.ylabel('Attendance')
plt.title('Total Score vs Attendance')

plt.plot(data['Study_Hours'], data['total_score'], '*')
plt.xlabel('Total Score')
plt.ylabel('Study Hours')
plt.title('Total Score vs Study Hours')
plt.show()