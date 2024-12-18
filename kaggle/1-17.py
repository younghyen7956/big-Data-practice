import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic2.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

df1 = df[(df['year']==2022)&(df['month']==5)]

print(df1['Sales'].median())

