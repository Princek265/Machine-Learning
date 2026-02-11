import numpy as np
# Exercise 1:  Broadcasting exercises

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([1, 0, -1])

result_add = matrix + vector
print("Add: \n", result_add)

result_mul = matrix * 2
print("Multiplication: \n", result_mul)

# Exercise 2: Generate and Filter a Random Dataset

# Generate random dataset
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified dataset: \n", dataset)

# Calculate summary stats
print("Sum: ",np.sum(dataset))
print("Mean: ",np.mean(dataset))
print("Standart Deviation: ", np.std(dataset))
