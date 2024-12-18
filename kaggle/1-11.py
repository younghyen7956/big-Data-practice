import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import power_transform
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df['f5'] = MinMaxScaler().fit_transform(df[['f5']])

print(df['f5'].quantile(0.95)+df['f5'].quantile(0.05))

