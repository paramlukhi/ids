from scipy.io import arff
import pandas as pd
data, meta = arff.loadarff('dataset.arff')
df = pd.DataFrame(data)
for col in df.select_dtypes([object]):
    df[col] = df[col].str.decode('utf-8')
df.to_csv('titanic.csv', index=False)
print("conversion completed successfully")
