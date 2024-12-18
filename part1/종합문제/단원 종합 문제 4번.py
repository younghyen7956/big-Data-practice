import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler,StandardScaler

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

# 특정 target 그룹만 선택하고 복사
target_0_df = df[df['target'] == 0].copy()

# 최소-최대 척도 변환 (Min-Max Scaling)
scaler = MinMaxScaler()
min_max_scaled = scaler.fit_transform(target_0_df[rdf['feature_names']])

# Z-Score 변환
z_scores = (target_0_df[rdf['feature_names']] - target_0_df[rdf['feature_names']].mean()) / target_0_df[rdf['feature_names']].std()

# 최소-최대 변환 후의 평균값 계산
target_0_df.loc[:, 'min_max_mean'] = min_max_scaled.mean(axis=1)

# Z-Score 변환 후의 평균값 계산
target_0_df.loc[:, 'z_score_mean'] = z_scores.mean(axis=1)

# 결과 출력
print(target_0_df[['min_max_mean', 'z_score_mean']].head())
