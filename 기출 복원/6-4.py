import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv(r"/data/eduhealth.csv", encoding="euc-kr")

# 결측값 제거
df1 = df.dropna()

# 성별을 숫자로 변환 (factorize 사용)
df1.loc[:, '성별'] = pd.factorize(df1['성별'], sort=True)[0].astype(int)

# 상관계수 계산
cor = df1[['학년', '키', '몸무게', '성별']].corr()

# 대각 행렬의 값을 제외하고 제일 큰 값 찾기
# 대각 행렬을 제외하기 위해 np.triu를 사용하여 상삼각행렬을 마스킹
cor_values = cor.to_numpy()  # 상관계수 행렬을 numpy 배열로 변환
np.fill_diagonal(cor_values, 0)  # 대각선 값을 0으로 설정
max_correlation = np.max(np.abs(cor_values))  # 절댓값 기준으로 가장 큰 값

print("상관계수 행렬:")

print("\n대각행렬 제외 후 가장 큰 상관계수 값:", max_correlation)

# 회귀 분석 모델 설정
# y = df1[['학년', '키', '몸무게']]  # 종속 변수
# x = df1[['성별']]  # 독립 변수
#
# # 회귀 분석
# formula = '학년 ~ 성별'  # 예시로 성별이 학년에 미치는 영향을 분석하는 회귀모델
# model = ols(formula, data=df1).fit()
#
# # 회귀 분석 결과 출력
# print(model.summary())
