import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\payment.csv")
df['menu'] = df['menu'].str.strip()

# print(df['menu'])
print(len(df[df['menu'].str.contains("라떼")]))

