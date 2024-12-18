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
df1 = df.sort_values("Solar.R",ascending=False).sample(frac=0.8,random_state=42)
v1 = df1['Ozone'].median()
df2 = df1.copy()
df2["Ozone"] = df2['Ozone'].fillna(df2['Ozone'].mean())
v2 = df2['Ozone'].median()

print(v1,v2)
# print(sum(df1['Ozone'].isna()))
