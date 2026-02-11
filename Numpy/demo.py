import numpy as np
import pandas as pd

# 26-203 Cabin 10 ML Foundation 

# --- Array Creation & Inspection ---
a = np.array([2, 3, 4])
b = np.array([4, 3, 5])
print(a.shape)      # Returns dimensions of the array: (3,)
print(type(a))       # Confirms it's a numpy.ndarray

# --- Element-wise Arithmetic (Vectorization) ---
# Operations are performed index-by-index
print(a + b)        # Addition
print(a / b)        # Floating point division
print(a // b)       # Floor division (integer result)
print(a - b)        # Subtraction
print(a * b)        # Multiplication

# --- Comparison Operators ---
# Returns boolean arrays
print(a > b)        
print(a < b)
print(a != b)
print(a == b)

# --- Matrix Initializers ---
# Note: Dimensions are passed as a tuple (rows, cols)
print("Zeros: \n", np.zeros((2, 3)))   # 2x3 matrix of 0.0
print("Ones:\n", np.ones((3, 3)))     # 3x3 matrix of 1.0
print("Identity Matrix:\n", np.eye(3)) # 3x3 matrix with 1.0 on diagonal

# --- Numerical Ranges ---
print("Arange:\n", np.arange(0, 10, 2))    # [start, stop, step) -> similar to range()
print("Linspace:\n", np.linspace(0, 1, 5)) # [start, stop, number_of_elements]

# --- Slicing & Reassignment ---
# Caution: Here 'a' is redefined as a standard Python List, not a NumPy array
a = [4, 5, 6, 8]
print(a[1:])     # Slice from index 1 to the end
print(a[::-1])   # Reverse the list
print(a[2:3:1])  # Slice from index 2 to 3 (exclusive) with step 1

# --- Scalar Operations ---
# When 'a' is a list, a*2 replicates the list. 
# If 'a' were an array, it would multiply every number by 2.
print("Scalar multiply", a * 2) 

# --- Statistical & Math Functions ---
# NumPy functions can convert lists to arrays internally to perform math
print(np.sqrt(a))  # Square root of each element
print(np.sum(a))   # Sum of all elements
print(np.max(a))   # Maximum value
print(np.min(a))   # Minimum value
print(np.mean(a))  # Arithmetic mean


# --- 2D Array Indexing & Slicing ---
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Accessing a single element: [row, column]
print("Element at [0,0]:", matrix[0, 0])

# Slicing: [row_start:row_end, col_start:col_end]
# This grabs rows 0-1 and columns 1-2
print("Submatrix (0:2,1:3):\n", matrix[0:2, 1:3])

# --- Shape Manipulation ---
arr = np.arange(1, 7) # Creates [1, 2, 3, 4, 5, 6]

# Changes the structure without changing the data
reshaped = arr.reshape(2, 3)
print("Reshaped (2x3):\n", reshaped)

# Transpose: Flips rows and columns (switches 2x3 to 3x2)
print("Transpose (3x2):\n", reshaped.transpose())

# Flatten: Collapses a multi-dimensional array into 1D
# ravel() is a view, flatten() is a copy
print("Flattened:\n", reshaped.flatten())

# --- Combining Arrays (Joining) ---
# Concatenate: Joins arrays along an existing axis (default is 0)
print("concatinate:", np.concatenate((a, b)))

x = np.array([2, 3, 4])
y = np.array([4, 3, 5])

# Stack: Joins arrays along a NEW axis (creates a 2D array from two 1D arrays)
print("stack:\n", np.stack((x, y)))

# Horizontal Stack: Append arrays side-by-side
print("horizontal stack:", np.hstack((a, b)))

# Vertical Stack: Place arrays one on top of the other (same as np.stack in this case)
print("vertical stack:\n", np.vstack((x, y)))

# --- Linear Algebra ---
# Dot product: (1*4) + (2*5) + (3*6) = 32
print("Dot product:", np.dot(x, y)) 

# Cross Product: Returns the vector perpendicular to the plane of x and y
print("Cross Product:", np.cross(x, y))

# Pandas



data={'A':[1,2,3,4,5,6]}
print(pd.DataFrame(data))
print()
print(pd.Series(data))

rollData={'Rollno':[20,31,np.nan,22,np.nan]}
df=pd.DataFrame(rollData)
print(df.fillna(0))
