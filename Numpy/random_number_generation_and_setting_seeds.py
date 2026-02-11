import numpy as np
# Random Number Generation

random_array = np.random.rand(3,3)

print("Random array: ",random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)

print("\n\n")
# Setting Random Seeds
# It fixes 1 random output
# Every time it will give that same random output every time we re-run the code
np.random.seed(42)

random_array = np.random.rand(3,3)

print("Random array: ",random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)
