import numpy as np
import pandas as pd
from statsmodels.formula.api import logit

df = pd.read_csv(r'A:\big-Data-practice\data\Customer_Data.csv')

train = df.iloc[:350]
test = df.iloc[350:]

model = logit('purchase~income',data=df)

result = model.fit()

# print(np.exp(result.params['income']))
predictions_income = result.predict(test)
predicted_classes_income = (predictions_income > 0.5).astype(int)

# print((predicted_classes_income == 1).mean())

print(result.llf)

print(result.pvalues['income'])


# print((result.predict(test)>0.5).astype(int))