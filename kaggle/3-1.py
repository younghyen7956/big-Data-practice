import pandas as pd
from scipy import stats
df = pd.read_csv(r"A:\big-Data-practice\data\blood_pressure.csv")

df['diff'] = df['bp_after'] - df['bp_before']

print(round(df['diff'].mean(),2))

t,p = stats.ttest_ind(df['bp_after'],df['bp_before'],alternative="less")

print(t,p)