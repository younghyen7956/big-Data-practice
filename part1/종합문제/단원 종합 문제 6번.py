import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler,StandardScaler

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

df1 = df[df['target'] == 0].copy()
m = df1['sepal length (cm)'].median()
df1.loc[:,'new'] = np.where(df1['sepal length (cm)'] > m,1,0)

print(df1[df1['new'] == 1]['sepal length (cm)'].mean())

