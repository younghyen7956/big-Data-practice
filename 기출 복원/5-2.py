import pandas as pd

df = pd.read_csv(r"/data/teacher.csv", encoding="euc-kr")

df['new'] = df['student'] /df['teacher']

print(df.sort_values('new',ascending=False).iloc[0,].loc[('district','teacher'),].iloc[0])
print(df.sort_values('new',ascending=False).iloc[0,].loc[('district','teacher'),].iloc[1])