import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df['f4'] = df['f4'].replace("ESFJ","ISFJ")

print(df[(df['city']=="경기")&(df['f4']=="ISFJ")]['age'].max())