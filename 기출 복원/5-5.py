import pandas as pd
from scipy import stats


df = pd.read_csv(r"/data/bugok.csv", encoding="euc-kr")

df1 = df[df['환자구분'] =="정신"]

v1=len(df[df['성별']=="남성"])
v2=len(df[df['성별']=="여성"])

m = len(df[(df['성별']=="남성")&(df["환자구분"]=="정신")])
f = len(df[(df['성별']=="여성")&(df["환자구분"]=="정신")])

result = [[m,f],[v1-m,v2-f]]

chi,pvalue,_,_=stats.chi2_contingency(result)

print(chi,pvalue)