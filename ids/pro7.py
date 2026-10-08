import pandas as pd

df = pd.read_csv('iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

print("--- Group by Species (Mean) ---")
print(df.groupby('species').mean())

print("\n--- Aggregated Statistics ---")
print(df.groupby('species').agg(['mean', 'std', 'min', 'max']))

print("\n--- Group Comparison ---")
print(df.groupby('species')['sepal_length'].mean())

print("\n--- Summarized Report ---")
print(df.groupby('species').describe())
