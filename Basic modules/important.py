from functools import reduce
numbers = [1,2,3,4]
product = reduce(lambda x,y: x*y, numbers) # 1*2=2 ->2*3=6 -> 6*4=24 

print(product)




# List comprehension

# [expression for item in iterable if condition]

# Create a list of squares
# squares = [x**2 for x in range(1,11)]
# print(squares)

# evens = [x for x in range(0,11) if x%2==0]
# print(evens)


#Lambda Functions

# lambda arguments: expression
# also called as inline or anonymous functions

# add = lambda x,y: x+y;
# print(add(3,5))

# map() Applies a function to each item in an iterable

# numbers = [1,2,3,4]
# map(function,data)
# squares = map(lambda x: x**2, numbers)
# print(list(squares))

# filter() Filters items based on a condition
# filter(function,data)
# evenList = filter(lambda x: x%2==0, numbers)
# print(list(evenList))
