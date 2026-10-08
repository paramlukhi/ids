import pandas as pd

df = pd.read_csv('iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
num = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

print("--- Mean ---")
print(num.mean())

print("\n--- Median ---")
print(num.median())

print("\n--- Mode ---")
print(num.mode().iloc[0])

print("\n--- Variance ---")
print(num.var())

print("\n--- Standard Deviation ---")
print(num.std())

print("\n--- Minimum ---")
print(num.min())

print("\n--- Maximum ---")
print(num.max())

print("\n--- Correlation ---")
print(num.corr())
