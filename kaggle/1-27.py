import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\payment.csv")
df['menu'] = df['menu'].str.strip()
df['menu'] = df['menu'].str.replace(' ',"")
df['new'] =df['menu'].map({"바닐라라떼":5,"카페라떼":3,"아메리카노":2}).fillna(0)

print(df['new'].sum())
