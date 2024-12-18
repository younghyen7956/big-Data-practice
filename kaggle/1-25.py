import pandas as pd

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

# f4를 문자열로 변환
df['f4'] = df['f4'].astype(str)

# 조건에 맞는 데이터 필터링 및 출력
result = df[(df['f4'].str.startswith('E')) &
            (df['city'] == "부산") &
            (df['age'] >= 20) &
            (df['age'] < 30)]
print(result)
print(f"조건에 맞는 사람 수: {len(result)}")
