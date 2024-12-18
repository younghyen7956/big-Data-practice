import pandas as pd
from pathlib import Path

# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "mtcars.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path)
df1= df.sort_values('mpg',ascending=False)
df2 = df1.head(10)
print(df2)
print(df2[df2['carb']==2]['hp'].mean()-df2[df2['carb']==1]['hp'].mean())
