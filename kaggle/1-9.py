import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

# scaler = StandardScaler()
# df['f5']=scaler.fit_transform(df[['f5']])
df['f5'] = StandardScaler().fit_transform(df[['f5']])
print(df['f5'].median())