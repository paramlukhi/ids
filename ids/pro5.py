import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

data = {
    'Name': ['aarav', 'diya', 'rohan', 'ananya'],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Department': ['IT', 'CS', 'CE', 'CS'],
    'Maths': [85, 92, 65, 95],
    'Science': [78, 88, 70, 92]
}
df = pd.DataFrame(data)

# 1. Rename and modify columns
df.rename(columns={'Maths': 'Math_Score'}, inplace=True)
df['Name'] = df['Name'].str.title()

# 2. Calculated column
df['Total'] = df['Math_Score'] + df['Science']

# 3. Convert categorical values
le = LabelEncoder()
df['Gender_Code'] = le.fit_transform(df['Gender'])
df = pd.get_dummies(df, columns=['Department'], dtype=int)

# 4. Normalization and Scaling
df['Total_MinMax'] = MinMaxScaler().fit_transform(df[['Total']])
df['Total_ZScore'] = StandardScaler().fit_transform(df[['Total']])

print(df)
