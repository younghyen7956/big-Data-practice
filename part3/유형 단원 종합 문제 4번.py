import pandas as pd
from pathlib import Path
from statsmodels.formula.api import ols

# 현재 파일 경로
current_file_path = Path(__file__)

# 상위 디렉토리
parent_dir = current_file_path.parent.parent
# 파일 경로 설정
file_path = parent_dir / "data" / "mtcars.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path, encoding='euc-kr')

# 숫자형 데이터로 변환
df['mpg'] = pd.to_numeric(df['mpg'], errors='coerce')  # mpg 열을 숫자로 변환

# 회귀 모델 학습
fit = ols('mpg ~ hp + wt + am', data=df).fit()

# 예측할 데이터프레임 생성
predict_data = pd.DataFrame({'hp': [110], 'wt': [3.215], 'am': [0]})

# 예측 수행
pred = fit.predict(predict_data)

# 실제 mpg 값 가져오기 (4번째 행의 mpg 열 값)
true_value = float(df.loc[3, 'mpg'])  # 'mpg' 열의 값을 가져옴

# 예측 오차 계산
error = (true_value - pred.values[0]) / true_value * 100

print(round(fit.conf_int(alpha=0.05).iloc[1,0],4))
print(round(fit.conf_int(alpha=0.05).iloc[1,1],4))
# 출력
# print(f"예측값: {pred.values[0]:.2f}, 오차율: {error:.2f}%")
