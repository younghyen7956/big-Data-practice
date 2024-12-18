import pandas as pd
from pathlib import Path
from statsmodels.formula.api import ols
from scipy.stats import chi2_contingency
# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "titanic.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path, encoding='euc-kr')
print(df)
table = pd.crosstab(df['Sex'],df['Survived'])
# print(table)
# chi2,p,_,_ = chi2_contingency(table)
# print(chi2,p)