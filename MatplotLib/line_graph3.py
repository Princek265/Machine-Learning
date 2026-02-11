import matplotlib.pyplot as plt

# line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1", marker='+', linewidth=2, color='red',linestyle='-', markerfacecolor='green', markersize=10)

# line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2",marker='o', linewidth=2, color='blue',linestyle='dashed', markerfacecolor='yellow', markersize=10)

# naming the x axis
plt.xlabel('X axis')
# naming the y axis
plt.ylabel('Y axis')
# giving a title to the graph
plt.title('Two lines on same graph')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()