import pandas as pd

# CSV 파일 읽기
df = pd.read_csv(r"/data/housing.csv")

df1 = df.iloc[0:int(len(df)*0.8)]

# print(df1)

df2 = df1.dropna(subset = 'total_bedrooms')

print(df2['total_bedrooms'].std())
m= df1['total_bedrooms'].median()
df1.loc[:,'total_bedrooms'] = df1.loc[:,'total_bedrooms'].fillna(m)

print(df1['total_bedrooms'].std())