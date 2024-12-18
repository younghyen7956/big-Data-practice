import pandas as pd

df = pd.read_csv(r"/data/USvideos.csv")
df['news'] = df['likes']/df['views']
print(len(df[(df['category_id']==10) & (df['news'] > 0.04) & (df['news'] < 0.05)]))




