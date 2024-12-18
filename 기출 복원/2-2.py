import pandas as pd
import numpy as np

# 데이터 로드
df = pd.read_csv(r"/data/country.csv")

# 2000년 데이터만 선택
df1 = df[df['year'] == 2000]

# 1~7열 선택 (0번째 열 제외)
df2 = df1.iloc[:, 1:8]

# 각 행의 평균 계산
m = df2.mean(axis=1).iloc[0]

print(df2[df2>m].count().sum())