import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\airquality.csv")

df1 = df.dropna(axis=0).reset_index()
df2 = df1[df1['Month']==5]
print(len(df2[df2['Ozone']>=24.125]))

