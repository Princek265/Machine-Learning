import pandas as p
import numpy as n
series =p.Series([10,20,30,40,50,"Hello"],index = ["haha","hehe","meowmeownigg","yoyo","lappusachin","chickenlegpiece"])
print(series.size)  # returns no of elements
print(series.index) # returns the index of series
print(series.nbytes) # no of bytes used
print(series.shape) # returns a tuple 
print(series.dtypes)
print(series.values.itemsize)
print(series.empty)
print(series.ndim)
print(series.hasnans)
print(series.head(2))
print(series.tail(2))
print(series.loc["hehe":"lappusachin"])
print(series.iloc[2:5])