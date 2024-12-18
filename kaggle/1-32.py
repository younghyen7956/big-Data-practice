import pandas as pd
df = pd.DataFrame({'Name': {0: '김딴짓', 1: '박분기', 2: '이퇴근'},
                   '수학': {0: 90, 1: 93, 2: 85},
                   '영어': {0: 92, 1: 84, 2: 86},
                   '국어': {0: 91, 1: 94, 2: 83},})

df1 = df.melt(id_vars="Name",value_vars=['수학','영어'])

print(int(df1[df1['value']>=90]['value'].mean()))