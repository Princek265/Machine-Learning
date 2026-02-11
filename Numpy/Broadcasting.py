import numpy as np

# Array and scalar broadcasting

# Scalar broadcasting
arr = np.array([1,2,3])
print(arr + 10) # All the elements are incremented by 10


# Array broad casting
matrix = np.array([[1,2,3],[4,5,6]]) # 2x3 Matrix
vector = np.array([1,0,1]) # 1x3
print(matrix + vector) 
# This results in 1st row elemets + vector elemets and 2nd row elements + vector
# Basically like.. Matrix 1 + Matrix 2 in Maths
# [            [
#  [1,2,3],  +  [1,0,1],
#  [4,5,6]      [1,0,1] 
#         ]            ]

# we just take a vector and broadcast it to the whole array/matrix