import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic2.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['dayofweek'] = df['Date'].dt.dayofweek
df['weekend'] = df['dayofweek'].apply(lambda x: x>=5)

df1 = df[(df['year']==2022)&(df['month']==5)&(df['weekend'])]
df2 = df[(df['year']==2022)&(df['month']==5)&(~df['weekend'])]

print(round(abs(df1['Sales'].mean()-df2['Sales'].mean()),2))



