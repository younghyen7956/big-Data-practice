import pandas as pd
from pathlib import Path
from scipy import stats
# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "data.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path, encoding='euc-kr')

df1 = df[df['주거지역'] == "소도시"]
df2 = df[df['주거지역'] == "중도시"]
df3 = df[df['주거지역'] == "대도시"]
x1 = len(df1[df1['쿠폰선호도'] =="예"])
x2 = len(df2[df2['쿠폰선호도'] =="예"])
x3 = len(df3[df3['쿠폰선호도'] =="예"])

result = [[x1,x2],[len(df1)-x1,len(df2)-x2]]

chi,pvalue, dof,expact = stats.chi2_contingency(result)

print(chi,pvalue,dof,expact)

result = [[x1,x3],[len(df1)-x1,len(df3)-x3]]

chi,pvalue, dof,expact = stats.chi2_contingency(result)

print(chi,pvalue,dof,expact)
