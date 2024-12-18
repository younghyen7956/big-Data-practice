import pandas as pd
from statsmodels.formula.api import logit
df = pd.read_csv(r"A:\big-Data-practice\data\titanic.csv")

df['Pclass'] = pd.factorize(df['Pclass'])[0].astype(int)
# df['Sex'] = pd.factorize(df['Sex'])[0].astype(int)

x = df[['Pclass','Sex','SibSp','Parch']]
y = df['Survived']

# x = x.
formula = "Survived ~ C(Pclass) + Sex + SibSp + Parch"

model = logit(formula, data=df).fit()
print(model.params['Parch'])
# print(df['Parch'])