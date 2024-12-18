import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\mtcars.csv")

q1 = df['wt'].quantile(0.25)
q3 = df['wt'].quantile(0.75)

iqr = q3-q1

print(df[(df['wt']>=q3+1.5*iqr)| (df['wt']<=q1-1.5*iqr)]['wt'].values)