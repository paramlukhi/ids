import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('em1.csv')
#print(df)
#plt.bar(df['Employee_ID'],df['Salary'])
#plt.pie(df['Salary'], labels=df['Employee_ID'])
#plt.plot(df['Employee_ID'], df['Salary'], marker='o')
#plt.scatter(df['Employee_ID'], df['Salary'])
#plt.boxplot(df['Salary'])
plt.hist(df['Salary'])
plt.title('employee salary')
plt.xlabel('id')
plt.ylabel('salary')
plt.show()