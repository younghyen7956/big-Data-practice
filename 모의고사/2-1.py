import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\airquality.csv")

df1 = df.dropna(axis=0)

print(df1['Ozone'].quantile(0.4))