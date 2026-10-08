import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('em1.csv')
plt.pie(df['Salary'], labels=df['Employee_ID'])
plt.show()