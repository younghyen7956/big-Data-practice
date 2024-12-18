import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import power_transform

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")
df1 = df[df['age']>=20]

df1.loc[:,'f1'] = df1.loc[:,'f1'].fillna(df1['f1'].mode()[0])
df1['ex'] = power_transform(df1[['f1']],standardize=False)
df1['box'] = power_transform(df1[['f1']],method="box-cox",standardize=False)
# print(df1)
print(round(sum(abs(df1['ex'] - df1['box'])),2))