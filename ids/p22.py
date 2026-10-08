import pandas as pd
students = pd.read_csv('sm.csv')
marks = pd.read_csv('m2.csv')
result = pd.merge(students,marks,on='ID')
print(result)