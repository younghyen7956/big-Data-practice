import numpy as np
import pandas as pd

df = pd.read_csv(r"/data/score.csv", encoding="euc-kr")
df['type'] = df['type'].str.strip()
df1= df[df['type']=="의사"]

q1=df1['score'].quantile(0.25)
m=df1['score'].quantile(0.5)
q3=df1['score'].quantile(0.75)

iqr= q3-q1

print(len(df1[df1['score']>=q3+0.1*iqr]))


