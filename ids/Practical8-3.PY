import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('em1.csv')
plt.hist(df['Salary'])
plt.show()
