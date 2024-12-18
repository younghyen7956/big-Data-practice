import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\airquality.csv")

print(df.isna().sum().sort_values(ascending=False).index[0])

