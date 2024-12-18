import pandas as pd

df = pd.read_csv(r"/data/index.csv")

df['bmi'] = df['Weight'] / (df['Height']/100)**2

print(abs(len(df[df['bmi']>=25]) - len(df[df['bmi']<25])))