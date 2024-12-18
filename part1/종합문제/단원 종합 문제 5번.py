import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler,StandardScaler

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

ndf = df[(df['target']==1)|(df['target']==2)]
df1 = df[(df['target']==1)]
df2 = df[(df['target']==2)]

m = ndf['sepal length (cm)'].median()
m1 = ndf['petal length (cm)'].median()

# print(len(df1['sepal length (cm)']>=m)/df1.shape[0])
print(len(df1[df1['sepal length (cm)']>=m])/len(df1))
print(len(df2[df2['petal length (cm)']>=m1])/len(df2))

