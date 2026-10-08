import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('em1.csv')
plt.scatter(df['Employee_ID'], df['Salary'])
plt.show()