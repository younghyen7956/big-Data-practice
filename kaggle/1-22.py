import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic2.csv" ,parse_dates=['Date'], index_col=0)

df_w = df.resample('W').sum()

print(df_w['Sales'].max())
print(df_w['Sales'].min())
# df['year'] = df['Date'].dt.year
# df['month'] = df['Date'].dt.month
# df['week'] = df['Date'].dt.week
#
# df1 = df.groupby('week')['Sales'].sum()
# print(df1)







