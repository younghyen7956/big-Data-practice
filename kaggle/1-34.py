import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\website.csv")
df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])
# df['SessionDuration'] = (df['EndTime'] - df['StartTime']).dt.total_seconds() / 60 / 60
# df = df.groupby(['UserID', 'Page'])['SessionDuration'].mean().reset_index()
#
# idx = df.groupby('Page')['SessionDuration'].idxmax()
# print(df.iloc[idx])
# print(int(df.iloc[idx]['SessionDuration'].sum()))

# bins = [0, 6, 12, 18, 24]  # 구간 나누기
# labels = ["새벽", "오전", "오후", "저녁"]  # 구간 레이블
# df['TimeSlot'] = pd.cut(df['StartTime'].dt.hour, bins=bins, labels=labels, right=False, include_lowest=True)
# df1 = df.groupby(['TimeSlot'])['Page'].value_counts().reset_index()
# idx = df1.groupby('TimeSlot')['count'].idxmax()
# print(df1.iloc[idx]['Page'].value_counts().index[0])
# print(df1.iloc[idx]['count'].max())
# df2 = df1.groupby(['TimeSlot','Page'])['count'].max()
# print(df1)

df['date'] = df['StartTime'].dt.date
df1 = df.groupby(['UserID','date'])['Page'].count().reset_index()
print(df1.groupby(['date'])['Page'].count().reset_index())
df1['date'] = pd.to_datetime(df1['date'])
df1['month'] = df1['date'].dt.month

cond = df1['Page'] > 1
df1 = df1[cond]

print(df1.groupby('month')['Page'].sum().idxmax())
print(df1[df1['Page']>1])