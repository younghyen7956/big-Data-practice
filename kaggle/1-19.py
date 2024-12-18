import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic2.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['Sales'] = df.apply(lambda row: row['Sales'] * 0.8 if row['Events'] == 1 else row['Sales'], axis=1)
df1 = df[df['year']==2022]
df2 = df[df['year']==2023]
print(df1.groupby('month')['Sales'].sum().max())
print(df2.groupby('month')['Sales'].sum().max())

print(abs(df1.groupby('month')['Sales'].sum().max()-df2.groupby('month')['Sales'].sum().max()))



