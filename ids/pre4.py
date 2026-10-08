import pandas as pd
df = pd.read_csv('book1.csv')
df = pd.DataFrame(df)
def grade(result):
    if result >= 90:
        return 'A'
    elif result >= 80:
        return 'B'
    elif result >= 70:
        return 'C'
    elif result >= 60:
        return 'D'
    else:
        return 'F'


df['Grade'] = df['Result'].apply(grade)
print(df)
