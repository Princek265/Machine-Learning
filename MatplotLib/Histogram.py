import matplotlib.pyplot as plt

# Frequencies
ages = [2,5,70,40,30,20,10,80,90,100,55,43,23,37,45,67,89,12,34,56,78]

# setting the ranges and no. of intervals
Range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, Range, color='green', histtype='bar', rwidth=0.8)

# x axis label
plt.xlabel('Ages')
# y axis label
plt.ylabel('No. of People')
# plot title
plt.title('Ages of people')
# function to show the plot
plt.show()