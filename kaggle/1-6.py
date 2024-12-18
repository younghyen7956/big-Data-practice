import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df1 = df.dropna(subset='f1',axis=0)

re = df1.groupby(['city','f2']).sum()


# print(re.columns)
print(re.iloc[0]['f1'])