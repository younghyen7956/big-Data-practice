import pandas as pd
from pathlib import Path
from scipy import stats
from statsmodels.stats.anova import AnovaRM
# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "data.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path, encoding='euc-kr')

d1 = df[df['주거지역']=="소도시"]['이용만족도']
d2 = df[df['주거지역']=="중도시"]['이용만족도']
d3 = df[df['주거지역']=="대도시"]['이용만족도']

f,pvalue = stats.f_oneway(d1,d2,d3)

# print(f,pvalue)
# print(df)
df_long = df.melt(id_vars=["고객번호"], value_vars=["품질", "가격", "서비스", "배송"],
                  var_name="Condition", value_name="Satisfaction")

# 반복측정 ANOVA 수행
anova = AnovaRM(data=df_long, depvar="Satisfaction", subject="고객번호", within=["Condition"]).fit()

# 결과 출력
print(anova)