import pandas as pd
from sklearn.datasets import load_iris
from statsmodels.formula.api import ols
# iris 데이터셋 로드
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df['sepal width (cm)'].corr(df['sepal length (cm)']))