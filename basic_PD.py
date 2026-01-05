#Simple Usage of Pandas Series 
#Example 1
#Here we create a Pandas Series with custom index labels
import pandas as pd

data = [ 100, 101, 102, 103, 104, 105]

series = pd.Series(data, index=['Employee1', 'Employee2', 'Employee3', 'Employee4', 'Employee5', 'Employee6'])
print(series)

#Example 2
#Here we Access the value in the dictionary inside a Series using iloc
import pandas as pd

scores= [{'Math': 85, 'Science': 90, 'English': 88, 'History': 92}]

series = pd.Series(scores)
print(series.iloc[0]['Math'])


#Example 3
#Here we Modify the value in the dictionary inside a Series using iloc
import pandas as pd

scores= [{'Math': 85, 'Science': 90, 'English': 88, 'History': 92}]

series = pd.Series(scores, index=['Student1'])
series.iloc[0]['Math'] = 97
print(series)

#Example 4 
#Here we Modify the value of a nested dictionary inside a Series using iloc
#We also set display options to avoid truncation of data in the output
import pandas as pd
pd.set_option('display.max_columns', None)  # No truncation for columns
pd.set_option('display.max_colwidth', None)     # No truncation for column width
scores= [{'Math': 85, 'Science': 75, 'English': 88, 'History': 92},
          {'Math': 80, 'Science': 90, 'English': 78, 'History': 85},
            {'Math': 88, 'Science': 76, 'English': 95, 'History': 89}]

series = pd.Series(scores, index=['Student1', 'Student2', 'Student3'])
series.iloc[1]['History'] = 95
print(series)

#Example 5
#Here we use loc (Label wise) and iloc (Index wise) to print the value of a specific index inside a Series
import pandas as pd

datas = [ 200, 201, 202, 203, 204, 205]
series = pd.Series(datas, index=['A', 'B', 'C', 'D', 'E', 'F'])

print(series.loc['C'])
print(series.iloc[1])