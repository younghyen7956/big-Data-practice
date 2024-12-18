import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\payment.csv")
print(df[df['hour']<13]['date'].value_counts().index[0])
# print(df)
