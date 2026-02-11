import numpy as np


arr = np.array([1,2,3,4])
# print(arr)

zeroes = np.zeros((3)) # create an array with 3 elements preset as 0
# print(zeroes)

ones = np.ones(3) # create an array with 3 elements preset as 1
# print(ones)

range_array = np.arange(1,10,2) # np.arange(from, till, step)
# print(range_array) # Output: [1 3 5 7 9]

# linspace_array = np.linspace(0,1,5) #np.linspace(from, till, amoount_of_numbers)
linspace_array = np.linspace(0,10,5) # Output: [ 0.   2.5  5.   7.5 10. ]
# It gives given amount of evenly spaced numbers in a range including start and end number
# print(linspace_array) # Output: [0.   0.25 0.5  0.75 1.  ]

