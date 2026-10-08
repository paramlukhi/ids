import pandas as pd
data=pd.read_excel("Book.xlsx")
print(data.head(1))
print(data.tail(2))
print(data.shape)
print(data.columns)
print(data.info(1))
