import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df1 = df[df['f2']==0].sort_values('age',ascending=True).head(20)
s = df1['f1'].std()
min = df1['f1'].min()
df1['f1'] = df1['f1'].fillna(min)
s1 = df1['f1'].std()
print(round(s**2-s1**2,2))