import pandas as pd

df = pd.read_csv(r"/data/crime.csv", encoding="euc-kr")

df['ym'] = pd.to_datetime(df['ym'])

df['year'] = df['ym'].dt.year
df['month'] = df['ym'].dt.month
r = df[['year','month','cases']]
r1 = r.groupby(by=["year"],dropna=False).sum()
r2 = pd.DataFrame(r1['cases']/12).sort_values('cases',ascending=False)
v = r2.index[0]

print(df[df['year'] == v]['cases'].sum())
print(df[df['year'] == v]['cases'].sum()/12)
# print(r2.index[0])
