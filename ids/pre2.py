import pandas as pd
df = pd.read_excel('Book.xlsx')
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.describe())