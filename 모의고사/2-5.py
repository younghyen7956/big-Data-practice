import pandas as pd
from scipy import stats

df = pd.read_csv(r"A:\big-Data-practice\data\height.csv")

d1 = df['h_before']
d2 = df['h_after']

t,p = stats.ttest_ind(d1,d2,equal_var=False,alternative="less")

print(t,p)