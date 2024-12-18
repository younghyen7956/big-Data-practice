import pandas as pd

df = pd.read_csv(r"/data/insurance.csv")

m= df['charges'].mean()
s = df['charges'].std()

# print(df['charges'].mean(),df['charges'].std())

iqr = m+1.5*s

print(df[df['charges']>=iqr]['charges'].sum())


