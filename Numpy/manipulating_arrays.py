import numpy as np

# arr = np.array([1,2,3,4,5,6])

# reshaped  = arr.reshape(2,3) # if the array has enough elements it will reshape it to 2x3 matrix otherwise throw an error
# print(reshaped)

# arr1 = np.array([1,2,3,4,5,6,7,8,9])
# reshaped  = arr1.reshape(3,3)
# print(reshaped)

# arr = np.array([1,2,3])
# expanded = arr[:, np.newaxis] 
# print(expanded)
# print(expanded.shape)
# print(arr)
# print(arr.shape)




# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# arr = np.array([4,16,25])
# print(np.sqrt(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))
# print(np.sum(arr))


# Array Indexing
arr = np.array([10,20,30,40,50])
print(arr[1])
print(arr[-1])
# Array Slicing
print(arr[1:3])
print(arr[:3])
print(arr[3:])
print(arr[::-1])

