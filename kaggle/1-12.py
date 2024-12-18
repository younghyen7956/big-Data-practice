import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import power_transform
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv(r"A:\big-Data-practice\data\covid-vaccination-vs-death_ratio.csv")
df1 = df.groupby('country').max()
df2 = df1.sort_values('ratio',ascending=False)
cond = df2['ratio'] <= 100
df2 = df2[cond]

print(df2.head(10)['ratio'].mean())
print(df2.tail(10)['ratio'].mean())



