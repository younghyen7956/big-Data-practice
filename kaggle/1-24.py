import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic2.csv",parse_dates=['Date'],index_col=0)

df['new'] = df['PV'].shift(1)
df['new'] = df['new'].bfill()

df1 = df[(df['Events']==1)&(df['Sales']<=1000000)]

print(df1['new'].sum())









