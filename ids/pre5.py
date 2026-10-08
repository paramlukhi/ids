import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

# Sample Dataset (Creating initial DataFrame)
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': [' aarav patel ', 'DIYA SHAH', 'rohan mehta', 'ANANYA JOSHI', 'krish patel'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Department': ['IT', 'CS', 'CE', 'CS', 'IT'],
    'Age': [20, 21, 22, 20, 21],
    'Maths_Marks': [85, 92, 65, 95, 78],
    'Science_Marks': [78, 88, 70, 92, 75],
    'English_Marks': [90, 85, 60, 94, 80]
}

df = pd.DataFrame(data)
print("=== Original DataFrame ===")
print(df)
print("\n" + "="*60 + "\n")


print("--- 1. Renaming and Modifying Columns ---")

df.rename(columns={
    'Maths_Marks': 'Maths',
    'Science_Marks': 'Science',
    'English_Marks': 'English'
}, inplace=True)


df['Name'] = df['Name'].str.strip().str.title()

print("DataFrame after renaming and modifying columns:")
print(df[['Student_ID', 'Name', 'Maths', 'Science', 'English']])
print("\n" + "="*60 + "\n")


print("--- 2. Creating New Calculated Columns ---")
df['Total_Marks'] = df['Maths'] + df['Science'] + df['English']
df['Percentage'] = (df['Total_Marks'] / 300) * 100


df['Grade'] = df['Percentage'].apply(
    lambda x: 'A+' if x >= 90 else ('A' if x >= 80 else ('B' if x >= 70 else 'C'))
)

print("DataFrame with new calculated columns (Total_Marks, Percentage, Grade):")
print(df[['Name', 'Total_Marks', 'Percentage', 'Grade']])
print("\n" + "="*60 + "\n")


print("--- 3. Converting Categorical Values ---")

label_encoder = LabelEncoder()
df['Gender_Encoded'] = label_encoder.fit_transform(df['Gender'])


df_transformed = pd.get_dummies(df, columns=['Department'], prefix='Dept', dtype=int)

print("DataFrame after Categorical Encoding:")
print(df_transformed[['Name', 'Gender', 'Gender_Encoded'] + [c for c in df_transformed.columns if c.startswith('Dept_')]])
print("\n" + "="*60 + "\n")


print("--- 4. Applying Normalization and Scaling Techniques ---")


min_max_scaler = MinMaxScaler()
df_transformed[['Maths_MinMax', 'Total_MinMax']] = min_max_scaler.fit_transform(
    df_transformed[['Maths', 'Total_Marks']]
)

std_scaler = StandardScaler()
df_transformed[['Maths_ZScore', 'Total_ZScore']] = std_scaler.fit_transform(
    df_transformed[['Maths', 'Total_Marks']]
)

print("Comparison of Original vs Scaled Features:")
print(df_transformed[['Name', 'Maths', 'Maths_MinMax', 'Maths_ZScore', 'Total_Marks', 'Total_MinMax', 'Total_ZScore']])
print("\n" + "="*60 + "\n")

print("=== Final Transformed Dataset (Summary View) ===")
print(df_transformed.head())
