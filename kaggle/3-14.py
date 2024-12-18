import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
df = pd.read_csv(r"A:\big-Data-practice\data\christmas_decoration_sales.csv")

model = ols('Sales ~ C(Decoration_Type) * C(Region) ',data=df)

result = model.fit()

print(sm.stats.anova_lm(result))