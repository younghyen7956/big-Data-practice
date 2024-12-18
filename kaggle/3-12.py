import pandas as pd
from scipy import stats
# 데이터 프레임 생성
df = pd.DataFrame({'남자': [100, 200],
                   '여자': [130, 170]},
                  index=['합격', '불합격'])

chi,p,dof,expacted = stats.chi2_contingency(df)

print(chi,p)

print(expacted[0][0])