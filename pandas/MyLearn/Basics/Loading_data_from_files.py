import pandas as pd
# Loading data from csv file
df = pd.read_csv("./DataSets/student_performance.csv")

# Saving DataFrame to a csv file
df.to_csv("Filename.csv", index=False)

# Loading data from excel file
df = pd.read_excel("./DataSets/student_performance.xlsx")

# Saving DataFrame to an excel file
df.to_excel("Filename.xlsx", index=False)
