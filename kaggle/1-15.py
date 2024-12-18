import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df1 = df.sort_values('age',ascending=False).head(20)
m = df1['f1'].median()
df1['f1'] = df1['f1'].fillna(m)
# print(df1)
print(df1[(df1['f4']=="ISFJ")&(df1['f5']>=20)]['f1'].mean())