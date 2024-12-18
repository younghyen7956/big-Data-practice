import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\payment.csv",parse_dates=['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(len(df[df['month']==12]))
