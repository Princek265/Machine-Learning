import matplotlib.pyplot as plt
import numpy as np
# plot 1
x = np.array([0,1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2,2,1) # plt.subplot(row, column, index)
plt.plot(x,y)

# plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,2,2)
plt.plot(x,y)


# plot 3
x = np.array([0,1,2,3])
y = np.array([10,20,50,40])
plt.subplot(2,2,3)
plt.bar(x,y)

# plot 4
x = np.array([0,1,2,3])
y = np.array([32,43,51,12])
plt.subplot(2,2,4)
plt.plot(x,y)
plt.show()
plt.savefig("abc.png")


# To combine multiple plots into a single figure using the subplot() function in Matplotlib, you can specify the number of rows and columns for the grid layout and the index of each subplot. Here's an example code that demonstrates how to create a 2x2 grid of subplots:

# To combine multiple plots in 1 graph keep all subplot's index same.