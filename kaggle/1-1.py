import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\titanic.csv")

q1 = df['Fare'].quantile(0.25)
q3 = df['Fare'].quantile(0.75)

iqr = q3-q1

df1 = df[(df['Fare']>=q3+1.5*iqr)|(df['Fare']<=q1-1.5*iqr)]
# print(df1['Sex'])
print(len(df1[df1['Sex']=="female"]))