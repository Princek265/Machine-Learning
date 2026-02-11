import matplotlib.pyplot as plt

X_VALUES = [1, 2, 3, 4, 5]
Y_VALUES = [90, 85, 78, 92, 88]
plt.plot(X_VALUES, Y_VALUES)
plt.xlabel("Roll no.")
plt.ylabel("Marks")
plt.title("Line Graph")
plt.ylim(0, 100)
plt.xlim(1, 5)
plt.show()