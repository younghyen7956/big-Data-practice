import pandas as pd

# CSV 파일 읽기
df = pd.read_csv(r"/data/Boston.csv")

# 'crim' 열을 기준으로 내림차순 정렬
df1 = df.sort_values('crim', ascending=False)

# 'crim' 열의 10번째 값을 가져와서 0~9번째 값으로 설정
df1.loc[df1.index[:9], 'crim'] = df1.loc[df1.index[9], 'crim']

# 수정된 DataFrame 출력
# print(df1.head(10))

print(df1[df1['age']>=80]['crim'].mean())