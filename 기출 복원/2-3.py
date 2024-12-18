import pandas as pd
import numpy as np

# 데이터 로드
df = pd.read_csv(r"/data/country.csv")

print(df.isna().sum().max())