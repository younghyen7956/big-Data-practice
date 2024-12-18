import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from scipy import stats

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

# 타겟이 0인 데이터와 1인 데이터
s = df[df['target'] == 0]
v = df[df['target'] == 1]

# 두 집단의 'petal length (cm)' 데이터 추출
s_data = s['petal length (cm)']
v_data = v['petal length (cm)']

# 독립표본 t-검정
t, pvalue = stats.ttest_ind(s_data, v_data, equal_var=False)

print(t, pvalue)

t1,pvalue1 = stats.ttest_ind(s['petal width (cm)'],s['sepal width (cm)'],equal_var=False)

print(t1,pvalue1)