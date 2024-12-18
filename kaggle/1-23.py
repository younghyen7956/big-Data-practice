import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

m = df.sort_values('f1',ascending=False)['f1'].iloc[9]

df['f1'] = df['f1'].fillna(m)

df1 = df.drop_duplicates(subset='age')

print(abs(df['f1'].median()-df1['f1'].median()))









