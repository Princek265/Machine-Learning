import numpy as np
arr = np.array([1,2,3,4,5,6])
evens = arr[arr % 2 == 0] # the values in array which are divisible by 2 will be stored in evens
print("Evens: ", evens)

arr[arr > 3] = 0 # if the values are greater than 3 in the array they will become 0
print("Modified Array: ", arr)