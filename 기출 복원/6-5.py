import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
# 데이터 불러오기
df = pd.read_csv(r"/data/eduhealth.csv", encoding="euc-kr")

y = df['몸무게']
x = df['키']

model = ols('y~x',data=df)

result = model.fit()

print(result.rsquared)

print(np.exp(result.params['x']))

