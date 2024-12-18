import pandas as pd

df = pd.read_csv(r"/data/women.csv")

q1 = df['weight'].quantile(0.25)
q3 = df['weight'].quantile(0.75)

value = abs(q1-q3)

print(int(value))



