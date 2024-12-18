import numpy as np
import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\train.csv")

print(df['SalePrice'].skew())
print(df['SalePrice'].kurt())

df['new'] = np.log(df['SalePrice'])

print(df['new'].skew())
print(df['new'].kurt())

print(round(df['SalePrice'].skew()+df['SalePrice'].kurt()+df['new'].skew()+df['new'].kurt(),2))