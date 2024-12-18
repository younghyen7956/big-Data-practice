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
df1= df[df['Month'] == 8].copy()
o = df[(df['Month'] == 8) & (df['Day'] == 26)]['Ozone'].iloc[0]
s = df[(df['Month'] == 8) & (df['Day'] == 26)]['Solar.R'].iloc[0]
ndf = df1.dropna()
print(df1)
print(len(df1[df1['Ozone']>=o]))
print(len(df1[df1['Solar.R']>=s]))

