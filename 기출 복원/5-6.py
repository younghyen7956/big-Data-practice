import pandas as pd
from statsmodels.formula.api import ols

# 데이터 로드
df = pd.read_csv(r"/data/airquality.csv", encoding="euc-kr")

# 결측값이 있는 행을 삭제
df1 = df.dropna(axis=0)
y = df1['Temp']
x = df1[['Ozone','Solar.R','Wind']]
# 회귀 모델 적합
fit = ols('y~x', data=df1).fit()

# 회귀 모델의 파라미터 출력
# print(fit.params)

# 'Ozone'의 계수 출력
# print(fit.params[1])

# print(fit.pvalues[3])

pred = fit.predict(exog=dict(x=[[18,313,11.5]]))

# print(pred[0])

print(fit.conf_int(alpha=0.05))
print(fit.conf_int(alpha=0.05).loc['x[0]'][0])
print(fit.conf_int(alpha=0.05).loc['x[0]'][1])
