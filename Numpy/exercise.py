import numpy as np
# Excercise 1: Generate Arrays for basic mathamatical Operations
# a = np.arange(1,6)
# b = np.arange(6,11)

# print("Add: ",a+b)
# print("Add: ",a-b)
# print("Add: ",a*b)
# print("Add: ",a/b)

# Exercise 2: Create a 3x3 Matrix and Perfrom Operations

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Matrix: \n",matrix)
print()

# Transpose Matrix
transpose = matrix.T
print("Transpose Matrix: \n",transpose)
print()

another_matrix = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Addition: \n",matrix + another_matrix)
print()
print("Subtraction: \n",matrix - another_matrix)
print()
print("Multiplication: \n",matrix * another_matrix)
print()
print("Division: \n",matrix / another_matrix)

# Create a 4x4 matrix and calculate the sum of its rows and columns
# Write a program to normalise an array(scale values between 0 and 1)
# Generate a random array and find the minimum and maximum values