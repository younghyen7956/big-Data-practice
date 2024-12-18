import pandas as pd

df1 = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")
df2 = pd.read_csv(r"A:\big-Data-practice\data\basic3.csv")

df = df1.merge(df2,how="left",on='f4')
df3 =df.dropna(subset='r2')
print(df3.head(20)['f2'].sum())





