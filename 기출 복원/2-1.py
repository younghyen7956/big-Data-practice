import pandas as pd

df = pd.read_csv(r"/data/country.csv")

df1 = df.dropna(axis=0)

print(df1['Guam'].quantile(0.3))

