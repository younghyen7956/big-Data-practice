import numpy as np
import pandas as pd
from statsmodels.formula.api import ols

df = pd.read_csv(r"A:\big-Data-practice\data\t3_regression_data.csv")

model = ols('y~x1+x2+x3+x4',data=df)

result = model.fit()

print(result.params[1:5].max())

model1 = ols('y~x1+x2+x3',data=df)

result1 = model1.fit()

print(result1.params[1:4].min())

print(result1.rsquared)

new = pd.DataFrame({'x1':[5],'x2':12,'x3':10,'x4':[3]})

print(result1.predict(new)[0])

df1 = df.corr().to_numpy()
np.fill_diagonal(df1,0)
print(np.max(np.abs(df1)))


model2 = ols('y~x1+x2',data=df)

result2 = model2.fit()

print(result2.summary(),result2.rsquared)

print(result.resid.std())

print(result.get_prediction(new).summary_frame(alpha=0.03))