import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler,StandardScaler

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

df1 = df[df['target']==0]

df2 = df1.sort_values('sepal width (cm)',ascending=False).reset_index(drop=True)

print()

v = df2['sepal width (cm)'][9]

df2['sepal width (cm)'][0:10] = v

print(df2[df2['petal length (cm)']>=1.5]['sepal width (cm)'].mean())