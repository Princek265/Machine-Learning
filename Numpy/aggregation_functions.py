import numpy as np
arr = np.array([[1,2,3], [4,5,6]])

print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Standard Deviation: ", np.std(arr))
print("Sum along rows: ", np.sum(arr, axis=1))
print("Sum along columns: ", np.sum(arr, axis=0)) 