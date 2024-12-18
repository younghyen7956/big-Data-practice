import pandas as pd
from statsmodels.formula.api import ols

df = pd.read_csv(r"A:\big-Data-practice\data\carprice.csv")

model = ols('price~mileage+mpg+engineSize',data=df).fit()

# print(model.summary())
print(model.pvalues)
print(model.tvalues)
print(model.rsquared)