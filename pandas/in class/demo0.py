import pandas as pd

# Series from List
marks = [10,20,30,40]
marks = pd.Series(marks)
print(marks)
adf = pd.DataFrame(marks)
print(adf)

country = ["India","Germany","Brazil","Nepal"]
country = pd.Series(country)
print(country)


country = ["India","Germany","Brazil","Nepal"]
marks = [10,20,30,40]
x = pd.Series(marks,index=country,name="Marks Obtained")
print(x)

marks = {"English":91,"Maths":89,"Physics":78,"Computer":90, "Chemistry":91}
marks_series = pd.Series(marks)
print(marks_series)

print(marks_series.index)
print(marks_series.size)
print(marks_series.is_unique)
print(marks_series.dtype)
print(marks_series.values)

print(country[0])
print(country[-1])
print(x[0:2])

data = [
    [100,80,10],
    [94,76,12],
    [120,97,15],
    [110,88,14]
]
df = pd.DataFrame(data,columns=['iq','marks','package'])
print(df)

data = {
    'name':['A','B','C','D'],
    'iq':[100,94,120,110],
    'marks':[80,76,97,88],
    'package':[10,12,15,14]
}
df = pd.DataFrame(data)
df = df.set_index('name',inplace=True)
print(df)