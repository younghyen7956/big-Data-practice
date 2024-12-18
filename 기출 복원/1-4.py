import pandas as pd

df = pd.read_csv(r"/data/train_commerce.csv")

df['Reached.on.Time_Y.N'] = df['Reached.on.Time_Y.N'].astype('category')

print(df)

