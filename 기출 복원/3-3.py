import pandas as pd

# 데이터 로드
df = pd.read_csv(r"/data/netflixutf.csv")

# 'date_added' 열을 datetime 형식으로 변환
df['date_added'] = pd.to_datetime(df['date_added'])

# year, month, day를 각각 추출하여 새로운 열로 추가
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month
df['day'] = df['date_added'].dt.day
df1 = df[(df['year']==2021)&((df['month']==7) |(df['month']==8))]
print(len(df1[df1['country']=="United Kingdom"]))
