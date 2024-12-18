import pandas as pd
from scipy import stats
df = pd.read_csv(r"A:\big-Data-practice\data\blood_pressure.csv")

# print(df)

df1 = df['bp_before']
df2 = df['bp_after']
df['diff'] = df['bp_after']-df['bp_before']

print(df['diff'].mean())

t,p = stats.ttest_ind(df2,df1,equal_var=False,alternative="less")

print(t,p)