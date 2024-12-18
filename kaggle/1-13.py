import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import power_transform
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv(r"A:\big-Data-practice\data\winequality-red.csv")

# 상관관계가 가장 큰 값과 가장 작은 값 (절대값으로 확인)
max_corr=abs(df.corr()['quality'][:-1]).max()  #0.47
min_corr=abs(df.corr()['quality'][:-1]).min()   #0.013

if max_corr not in df.corr()[['quality']][:-1].values:
    max_corr=-max_corr
if min_corr not in df.corr()[['quality']][:-1].values:
    min_corr=-min_corr

ans=round(max_corr+min_corr,2)
print(ans)

