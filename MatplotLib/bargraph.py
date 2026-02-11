import matplotlib.pyplot as plt

# Create data for plotting
values = [5, 7, 3, 8, 4]
labels = ['A', 'B', 'C', 'D', 'E']

# Adding an "h" after bar will flip the bars to horizontal
# plt.bar(labels, values, color='yellowgreen') # Vertical bar graph
plt.barh(labels, values, color='yellowgreen') # Horizontal bar graph
plt.show()