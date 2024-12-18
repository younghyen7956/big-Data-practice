import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import statsmodels.api as sm
# 데이터 불러오기
df = pd.read_csv(r"/data/eduhealth.csv", encoding="euc-kr")
df =df.dropna()
x = df[['몸무게','키']]
y = df['성별']
y = pd.factorize(y)[0].astype(int)
x = sm.add_constant(x)

model = sm.Logit(y,x)
# 'Sex' 열을 변환할 때 .loc를 명시적으로 사용

result = model.fit()

print(result.summary())

print(result.pvalues[1:].max())





