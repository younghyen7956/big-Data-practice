import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\website.csv")
df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])
df['during'] = (df['EndTime'] - df['StartTime']).dt.total_seconds() / 60

print("1번",df['during'].max())

df1 = df['Page'].value_counts().idxmax()

print("2번",df1)

# 시간대 정의
bins = [0, 6, 12, 18, 24]  # 구간 나누기
labels = ["새벽", "오전", "오후", "저녁"]  # 구간 레이블
df['TimeSlot'] = pd.cut(df['StartTime'].dt.hour, bins=bins, labels=labels, right=False, include_lowest=True)

# 각 구간별 개수 출력
print("3번",df['TimeSlot'].value_counts())

result = df['StartTime'].dt.date

print(result.value_counts().index[0])


