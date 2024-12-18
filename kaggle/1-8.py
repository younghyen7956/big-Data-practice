import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")


df2 = df[df['f2']==1]['f1'].cumsum()
df3 = df2.bfill()

print(df3.mean())
