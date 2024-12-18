import pandas as pd
from scipy import stats
from scipy.stats import binom

# 데이터 프레임 생성

df = pd.read_csv(r"A:\big-Data-practice\data\t3_success.csv")


l = len(df)
v = len(df[df['Success']==1])
p = v/l

print(binom.pmf(60, 100, p))
print(l,v,p)
