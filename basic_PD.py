import pandas as pd

data = [ 100, 101, 102, 103, 104, 105]

series = pd.Series(data, index=['Employee1', 'Employee2', 'Employee3', 'Employee4', 'Employee5', 'Employee6'])
print(series)
