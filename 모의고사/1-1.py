import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv(r"A:\big-Data-practice\data\mtcars.csv")

m = MinMaxScaler()

df['qsec'] = m.fit_transform(df[['qsec']])

print(len(df[df['qsec']>0.5]))


