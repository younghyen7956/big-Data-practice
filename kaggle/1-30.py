import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\payment.csv",parse_dates=['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
m = df[df['month']==12]['price'].sum()
print(m)
print((df[(df['month']==12)&(df['day']==25)]['price'].sum()/m)*100)


