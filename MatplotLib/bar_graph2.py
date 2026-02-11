import matplotlib.pyplot as plt

# heights of bars
heights = [3, 12, 5, 18, 45]
names = ['one', 'two', 'three', 'four', 'five']

# plotting the bar chart
a1 = ['red', 'green']
a2 = ['b', 'g']
plt.bar(names, heights, width=0.8, color=a1)

# naming the x axis
plt.xlabel('X axis')
# naming the y axis
plt.ylabel('Y axis')
# giving a title to the graph
plt.title('Bar graph')
# function to show the plot
plt.show()
