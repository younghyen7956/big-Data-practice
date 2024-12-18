import pandas as pd
from pathlib import Path

# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "airquality.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path)
df1 = df.dropna(axis=0)

q1 = df1['Ozone'].quantile(0.25)
q2 = df1['Ozone'].quantile(0.5)
q3 = df1['Ozone'].quantile(0.75)

# .loc[]를 사용하여 값 수정
df1.loc[df1['Ozone'] <= q1, 'Ozone'] = 0
df1.loc[df1['Ozone'] >= q3, 'Ozone'] = 0

print(df1['Ozone'].mean() + df1['Ozone'].std())
