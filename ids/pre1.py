#2. Data Loading and Inspection:-Write a Python program to load a dataset from CSV and Excel files using Pandas. Perform the
#following tasks:


import pandas as pd
df = pd.read_csv('book1.csv')

#Load dataset using Pandas
   #print(df)

#Display first and last records
   #print(df.head())
   #print(df.tail())

# Check dataset dimensions
   #print(df.shape())
   #print(df.columns)
#print(df['age'].mean())
#print(df['age'].max())
#print(df['age'].min())
#max1=df.loc[df['age'].idxmax()]
#print(df.loc[df['age'].idxmin()])

#print(max1)
#print(max1['name'],max1['age'])
#print(df.groupby("name")["age"].mean())
#print(df[df["marks"] > 80])
#print(df[df["subject"] == "Math"])
#print(df.sort_values("marks"))
#print(df.sort_values("marks", ascending=False))
#print(df.groupby("subject").size())
#print(df.groupby("subject")["marks"].mean())
#df["result"] = "pass"

##print(df["result"])
#df["result"] = df["marks"].apply(lambda x: "distinction" 
 #                                if x >= 90 else "first class"
  #                                if x >= 80 else "second class"
     #                               if x >= 50 else "pass" if x >= 35 else "fail")
#print(df)

df.isnull()
df.isnull().sum()
df.fillna(0, inplace=True)
print(df)