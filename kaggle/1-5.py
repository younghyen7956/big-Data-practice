import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

d1 = df[df['f4']=="ENFJ"]
d2 = df[df['f4']=="INFP"]

print(abs(d1['f1'].std()-d2['f1'].std()))
