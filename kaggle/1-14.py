import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df1 = df.groupby(['city','f4'])['f5'].mean()

print(df1.reset_index().sort_values('f5',ascending=False)['f5'].head(7).sum())