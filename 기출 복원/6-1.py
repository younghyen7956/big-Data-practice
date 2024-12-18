import pandas as pd

df = pd.read_csv(r"/data/score.csv", encoding="euc-kr")
m = df['score'].mean()
s = df['score'].std()
df['new'] = (df['score']-m)/s

print(len(df[df['new']>=0.8]))