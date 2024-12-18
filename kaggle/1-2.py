import numpy as np
import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df1 = df[(df['age']-np.floor(df['age']))!= 0]

print(np.ceil(df1['age']).mean())
print(np.floor(df1['age']).mean())
print(np.trunc(df1['age']).mean())