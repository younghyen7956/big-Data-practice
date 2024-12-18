import numpy as np
import pandas as pd
from statsmodels.formula.api import logit
from statsmodels.formula.api import logit
df = pd.read_csv(r'A:\big-Data-practice\data\Customer_Data.csv')

train = df.iloc[:300]
test = df.iloc[300:]

model = logit('purchase~age+income+marital_status',data=train)
result = model.fit()
print(result.summary())

print(round(-2*result.llf,2))